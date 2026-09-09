# -*- coding: utf-8 -*-
r"""verify_stone_aq_rush_shi_defect.py -- STONE AQ: THE RUSH-SHI DEFECT ACROSS THE MINUSCULE FAMILY

Brief: BRIEF_STONE_AQ_RUSH_SHI_DEFECT.md (lock BRIEF_STONE_AQ_LOCK.sha256, re-verified as check AQ0).

Rush-Shi (J. Algebraic Combin. 37 (2013) 545-569): rowmotion on J(P_lambda) is conjugate to a Coxeter element on
the weights W.lambda.  A Coxeter element keeps every pairwise inner product; rowmotion, transported by the natural
bijection, does not.  Three defects -- the kept fraction kappa(R), the best Coxeter agreement a(R), the altitude
nu(R) -- and the linear centralizer C_W(R), computed for A_n (all omega_k, n<=7), D_n (omega_1, both half-spins,
n=4..7), E6 (omega_1, omega_6), E7 (omega_7), from the Cartan matrix alone.

BARS: AQ0 lock; AQ1 anchor (E7: 56, |P|=27, [18,18,18,2], kappa=1002/1540, kappa0=0.4823, a=14, C_W trivial;
E6: 27, |P|=16, [12,12,3], kappa=63.53%); AQ2 Rush-Shi seen on the data (order h, Coxeter cycle type);
AQ3 GUESS: R in W iff P is a chain; AQ4 GUESS: C_W(R) trivial off the chains, <c> on them; AQ5 GUESS: kappa > kappa0
off the chains and increasing with n in A_n omega_2, D_n half-spin, D_n omega_1; AQ6 [obs] the table; AQ7 [P] the
bilinear identity for delta = Rw - w on every pair.

Machinery: own, from scratch; exact rationals; W enumerated as permutations of the weights where |W| <= 400,000
(E7: SM-016's nu = 38 cited; C_W(R) by SM-054's method).  Own cache _stone_aq_cache/table_aq.json.

DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED at equal prominence; no registry/git
writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_aq_rush_shi_defect.py
"""
import itertools, json, os, sys, time, hashlib
from fractions import Fraction
from collections import Counter

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_aq_rush_shi_defect.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))
W_CAP = 400000

say("=" * 78); say("STONE AQ -- THE RUSH-SHI DEFECT ACROSS THE MINUSCULE FAMILY"); say("=" * 78)
BRIEF = "BRIEF_STONE_AQ_RUSH_SHI_DEFECT.md"; LOCK = open("BRIEF_STONE_AQ_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AQ0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AQ_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- Cartan matrices (Bourbaki numbering, 0-based)
def cartan_A(n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        C[i][i] = 2
        if i+1 < n: C[i][i+1] = C[i+1][i] = -1
    return C
def cartan_D(n):
    C = [[0]*n for _ in range(n)]
    for i in range(n): C[i][i] = 2
    for i in range(n-2): C[i][i+1] = C[i+1][i] = -1
    C[n-3][n-1] = C[n-1][n-3] = -1
    return C
def cartan_E(n):  # Bourbaki: chain 1-3-4-5-...-n, node 2 attached to 4
    C = [[0]*n for _ in range(n)]
    for i in range(n): C[i][i] = 2
    chain = [0] + list(range(2, n))
    for a, b in zip(chain, chain[1:]): C[a][b] = C[b][a] = -1
    C[1][3] = C[3][1] = -1
    return C
def coxeter_number(fam, n): return {"A": n+1, "D": 2*n-2, "E": {6: 12, 7: 18}.get(n)}[fam]
def weyl_order(fam, n):
    import math
    return {"A": math.factorial(n+1), "D": 2**(n-1)*math.factorial(n), "E": {6: 51840, 7: 2903040}.get(n)}[fam]

def inverse_frac(C):
    n = len(C); A = [[Fraction(C[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0); A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]; A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]; A[r] = [x - f*y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]

# ---------------------------------------------------------------- the generic machine
class Minuscule:
    def __init__(self, fam, n, k):
        self.fam, self.n, self.k = fam, n, k
        C = {"A": cartan_A, "D": cartan_D, "E": cartan_E}[fam](n); self.C = C; r = n
        self.Cinv = inverse_frac(C)
        lam = tuple(int(i == k-1) for i in range(r))
        # orbit
        orbit = {lam}; frontier = [lam]
        while frontier:
            nxt = []
            for w in frontier:
                for i in range(r):
                    if w[i] != 0:
                        v = tuple(w[j] - w[i]*C[i][j] for j in range(r))
                        if v not in orbit: orbit.add(v); nxt.append(v)
            frontier = nxt
        self.W = sorted(orbit, reverse=True); self.idx = {w: i for i, w in enumerate(self.W)}; N = len(self.W); self.N = N
        assert all(all(x in (-1, 0, 1) for x in w) for w in self.W), "not minuscule"
        # simple reflections as permutations
        self.S = []
        for i in range(r):
            self.S.append(tuple(self.idx[tuple(w[j] - w[i]*C[i][j] for j in range(r))] for w in self.W))
        # inner products
        def ip(a, b): return sum(Fraction(a[i]) * self.Cinv[i][j] * b[j] for i in range(r) for j in range(r))
        self.IP = [[ip(a, b) for b in self.W] for a in self.W]
        # lattice: down-edges w -> w - alpha_i when label_i = 1
        self.down = [[] for _ in range(N)]
        for a, w in enumerate(self.W):
            for i in range(r):
                if w[i] == 1: self.down[a].append(self.idx[tuple(w[j] - C[i][j] for j in range(r))])
        below = [set() for _ in range(N)]  # strict
        order = sorted(range(N), key=lambda a: sum(self.W[a][i] * sum(self.Cinv[i][j] for j in range(r)) for i in range(r)))  # by height
        for a in order:
            for b in self.down[a]: below[a] |= {b} | below[b]
        # first run: this matrix was stored transposed (b <= a) and read as a <= b -- instrumentation, fixed; FIRSTRUN log kept
        self.leq = [[(a == b) or (a in below[b]) for b in range(N)] for a in range(N)]   # leq[a][b]  <=>  a <= b
        self.top = self.idx[lam]; self.bottom = next(a for a in range(N) if not self.down[a])
        assert sum(1 for a in range(N) if not self.down[a]) == 1
        # join-irreducibles
        self.P = [a for a in range(N) if len(self.down[a]) == 1]
        self.chain = all(self.leq[a][b] or self.leq[b][a] for a in self.P for b in self.P)
        # rowmotion
        R = []
        for x in range(N):
            Sx = [p for p in self.P if not self.leq[p][x]]
            if not Sx: R.append(self.bottom); continue
            mins = [p for p in Sx if not any(q != p and self.leq[q][p] for q in Sx)]
            ub = [y for y in range(N) if all(self.leq[p][y] for p in mins)]
            join = [y for y in ub if not any(z != y and self.leq[z][y] for z in ub)]
            assert len(join) == 1, "join not unique"
            R.append(join[0])
        assert sorted(R) == list(range(N)), "rowmotion not a bijection"
        self.R = tuple(R)
    def compose(self, p, q): return tuple(p[q[i]] for i in range(self.N))
    def cyc(self, p):
        seen = set(); c = []
        for a in range(self.N):
            if a in seen: continue
            o = 0; x = a
            while x not in seen: seen.add(x); o += 1; x = p[x]
            c.append(o)
        return tuple(sorted(c, reverse=True))
    def order(self, p):
        e = tuple(range(self.N)); x = p; n = 1
        while x != e: x = self.compose(p, x); n += 1
        return n
    def coxeter_elements(self):
        out = set()
        for perm in itertools.permutations(range(self.n)):
            p = tuple(range(self.N))
            for i in perm: p = self.compose(self.S[i], p)
            out.add(p)
        return out
    def kept(self, p):
        N = self.N; kept = 0; tot = 0
        for a in range(N):
            for b in range(a+1, N):
                tot += 1
                if self.IP[p[a]][p[b]] == self.IP[a][b]: kept += 1
        return Fraction(kept, tot)
    def baseline(self):
        cnt = Counter(self.IP[a][b] for a in range(self.N) for b in range(self.N) if a != b); T = sum(cnt.values())
        return sum(Fraction(c, T)**2 for c in cnt.values())
    def isometry(self, p):
        return all(self.IP[p[a]][p[b]] == self.IP[a][b] for a in range(self.N) for b in range(a+1, self.N))
    def enumerate_W(self):
        e = tuple(range(self.N)); seen = {e}; frontier = [e]
        while frontier:
            nxt = []
            for g in frontier:
                for s in self.S:
                    h = self.compose(s, g)
                    if h not in seen:
                        seen.add(h); nxt.append(h)
                        if len(seen) > W_CAP: return None
            frontier = nxt
        return seen
    def centralizer_in_sym(self, p):
        # explicit centralizer of a permutation from its cycles: for each cycle length, shifts x permutations of equal cycles
        cycles = []; seen = set()
        for a in range(self.N):
            if a in seen: continue
            c = []; x = a
            while x not in seen: seen.add(x); c.append(x); x = p[x]
            cycles.append(c)
        bylen = {}
        for c in cycles: bylen.setdefault(len(c), []).append(c)
        groups = list(bylen.items())
        def gen():
            choices = []
            for L, cs in groups:
                m = len(cs)
                choices.append([(sig, sh) for sig in itertools.permutations(range(m)) for sh in itertools.product(range(L), repeat=m)])
            for combo in itertools.product(*choices):
                q = [None]*self.N
                for (L, cs), (sig, sh) in zip(groups, combo):
                    for i, c in enumerate(cs):
                        for j in range(L): q[c[j]] = cs[sig[i]][(j + sh[i]) % L]
                yield tuple(q)
        return gen()

# ---------------------------------------------------------------- the cases
CASES = []
for n in range(2, 8):
    for k in range(1, n+1): CASES.append(("A", n, k))
for n in range(4, 8):
    for k in (1, n-1, n): CASES.append(("D", n, k))
CASES += [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
TABLE = []
banner("AQ6 -- the table (computed case by case; the registered bars are read off it afterwards)")
say("  case        |Wl| |P|  h  chain  cycle type of R           order  kept kappa      kappa0     a(R)  nu(R)  |C_W(R)|  R in W  |W|enum")
for fam, n, k in CASES:
    M = Minuscule(fam, n, k)
    h = coxeter_number(fam, n); ct = M.cyc(M.R); od = M.order(M.R)
    cox = M.coxeter_elements(); cct = Counter(M.cyc(c) for c in cox)
    agree = max(sum(1 for a in range(M.N) if M.R[a] == c[a]) for c in cox)
    kap = M.kept(M.R); kap0 = M.baseline()
    Wsize = weyl_order(fam, n)
    if Wsize <= W_CAP:
        Wset = M.enumerate_W(); Wn = len(Wset)
        inW = M.R in Wset
        nu = min(sum(1 for a in range(M.N) if g[a] != M.R[a]) for g in Wset)
        cent = sum(1 for g in Wset if M.compose(g, M.R) == M.compose(M.R, g))
    else:
        Wset = None; Wn = None; inW = M.isometry(M.R); nu = None
        cent = sum(1 for q in M.centralizer_in_sym(M.R) if M.isometry(q))
    row = dict(fam=fam, n=n, k=k, N=M.N, P=len(M.P), h=h, chain=M.chain, cycle=list(ct), order=od, cox_cycle=[list(c) for c in cct],
               n_cox=len(cox), kept=[kap.numerator, kap.denominator], kept_f=float(kap), kappa0=float(kap0), agree=agree, nu=nu,
               cent=cent, inW=bool(inW), W_enum=Wn, W_formula=Wsize)
    TABLE.append(row)
    say("  %s%d w%-2d  %4d %3d %3d  %-5s  %-24s %5d  %5d/%-5d %.4f  %.4f  %3d   %-5s  %5d    %-5s  %s" % (
        fam, n, k, M.N, len(M.P), h, M.chain, " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(ct).items(), reverse=True)),
        od, kap.numerator, kap.denominator, float(kap), float(kap0), agree, nu if nu is not None else "cited", cent, inW, Wn))
    # AQ7 identity on this case
    bad = 0
    for a in range(M.N):
        for b in range(a+1, M.N):
            da = tuple(M.W[M.R[a]][i] - M.W[a][i] for i in range(M.n)); db = tuple(M.W[M.R[b]][i] - M.W[b][i] for i in range(M.n))
            def ipv(u, v): return sum(Fraction(u[i]) * M.Cinv[i][j] * v[j] for i in range(M.n) for j in range(M.n))
            lhs = M.IP[M.R[a]][M.R[b]] - M.IP[a][b]
            rhs = ipv(da, M.W[b]) + ipv(M.W[a], db) + ipv(da, db)
            if lhs != rhs: bad += 1
    row["aq7_bad"] = bad
    row["cox_ct_match"] = (ct in cct)
    tick("%s%d w%d done" % (fam, n, k))

# ---------------------------------------------------------------- the bars
def find(fam, n, k): return next(r for r in TABLE if (r["fam"], r["n"], r["k"]) == (fam, n, k))
banner("AQ1 -- the anchor: E7 and E6 from the Cartan matrix alone")
e7 = find("E", 7, 7); e6 = find("E", 6, 1)
check("AQ1a", "E7 omega7: 56 weights, |P| = 27, R of type [18,18,18,2], kappa = 1002/1540, kappa0 = 0.4823, a(R) = 14, C_W(R) trivial, R not in W",
      e7["N"] == 56 and e7["P"] == 27 and e7["cycle"] == [18, 18, 18, 2] and e7["kept"] == [501, 770] and abs(e7["kappa0"] - 0.4823) < 5e-4
      and e7["agree"] == 14 and e7["cent"] == 1 and not e7["inW"],
      "N %d P %d cycle %s kept %s kappa0 %.4f a %d C_W %d inW %s" % (e7["N"], e7["P"], e7["cycle"], e7["kept"], e7["kappa0"], e7["agree"], e7["cent"], e7["inW"]))
check("AQ1b", "E6 omega1: 27 weights, |P| = 16, R of type [12,12,3], kappa = 63.53 %% (AC5c's sheet value)",
      e6["N"] == 27 and e6["P"] == 16 and e6["cycle"] == [12, 12, 3] and abs(e6["kept_f"] - 0.6353) < 5e-4,
      "N %d P %d cycle %s kappa %.4f" % (e6["N"], e6["P"], e6["cycle"], e6["kept_f"]))

banner("AQ2 -- Rush-Shi seen on the data: order h and a Coxeter element's cycle type, every case")
ok2 = all(r["order"] == r["h"] and r["cox_ct_match"] for r in TABLE)
check("AQ2", "in all %d cases R has order h and the cycle type of a Coxeter element" % len(TABLE), ok2,
      [(r["fam"], r["n"], r["k"]) for r in TABLE if not (r["order"] == r["h"] and r["cox_ct_match"])])

banner("AQ3 -- REGISTERED GUESS: R in W exactly when P is a chain")
chains = [r for r in TABLE if r["chain"]]; nonch = [r for r in TABLE if not r["chain"]]
ok3 = all(r["inW"] for r in chains) and all(not r["inW"] for r in nonch)
check("AQ3", "R in W for every chain case (%d) and R not in W for every non-chain case (%d)" % (len(chains), len(nonch)), ok3,
      "chains in W: %s; non-chains in W: %s" % ([(r["fam"], r["n"], r["k"]) for r in chains if not r["inW"]],
                                                  [(r["fam"], r["n"], r["k"]) for r in nonch if r["inW"]]))
if not ok3: say("  [INVERTED] recorded at equal prominence.")

banner("AQ4 -- REGISTERED GUESS: C_W(R) trivial off the chains, of order h on them")
ok4 = all(r["cent"] == 1 for r in nonch) and all(r["cent"] == r["h"] for r in chains)
check("AQ4", "|C_W(R)| = 1 in every non-chain case and = h in every chain case", ok4,
      "non-chain centralizers: %s" % sorted(Counter((r["fam"], r["cent"]) for r in nonch).items()))
if not ok4: say("  [INVERTED] recorded at equal prominence: %s" % [((r["fam"], r["n"], r["k"]), r["cent"]) for r in nonch if r["cent"] != 1])

banner("AQ4b -- POST-REVEAL, labelled: what the order-2 linear centralizers are")
ident = {}
for fam, n, k in [("A", 3, 2), ("D", 4, 3), ("D", 4, 4)] + [("D", n, 1) for n in range(4, 8)]:
    M = Minuscule(fam, n, k); Wset = M.enumerate_W(); e = tuple(range(M.N))
    cent = [g for g in Wset if g != e and M.compose(g, M.R) == M.compose(M.R, g)]
    pw = {}; x = M.R; j = 1
    while x != e: pw[x] = j; x = M.compose(M.R, x); j += 1
    for g in cent:
        is_minus = all(M.W[g[a]] == tuple(-v for v in M.W[a]) for a in range(M.N))
        ident[(fam, n, k)] = dict(cycle=" ".join("%d^%d" % (l, m) for l, m in sorted(Counter(M.cyc(g)).items(), reverse=True)),
                                  power_of_R=pw.get(g), is_minus_one=is_minus, fixed=sum(1 for a in range(M.N) if g[a] == a), R_cycle=list(M.cyc(M.R)))
    say("  %s%d w%d: R type %s; centralizer element%s: %s" % (fam, n, k, ident[(fam, n, k)]["R_cycle"], "s" if len(cent) > 1 else "", ident[(fam, n, k)]))
allpow = all(v["power_of_R"] == coxeter_number(f, n) // 2 for (f, n, k), v in ident.items())
check("AQ4b", "POST-REVEAL: in every inverted case the non-trivial linear centralizer is R^(h/2), the half-turn of the clock itself "
      "(so C_W(R) = <R^(h/2)> of order 2 and R^(h/2) is the only power of R that is linear) -- while for E7, Psi^9 is not linear (SM-054)",
      allpow and all(v["power_of_R"] is not None for v in ident.values()), {k: (v["power_of_R"], v["cycle"], v["is_minus_one"]) for k, v in ident.items()})

banner("AQ5 -- REGISTERED GUESS: kappa > kappa0 off the chains, increasing with n in three families")
ok5a = all(r["kept_f"] > r["kappa0"] for r in nonch)
def fam_seq(sel): return [(r["n"], r["kept_f"]) for r in TABLE if sel(r)]
seqA2 = fam_seq(lambda r: r["fam"] == "A" and r["k"] == 2 and r["n"] >= 3)
seqDs = fam_seq(lambda r: r["fam"] == "D" and r["k"] == r["n"])
seqD1 = fam_seq(lambda r: r["fam"] == "D" and r["k"] == 1)
def inc(seq): return all(b[1] > a[1] for a, b in zip(seq, seq[1:]))
check("AQ5a", "kappa(R) > kappa0 in every non-chain case", ok5a, [((r["fam"], r["n"], r["k"]), r["kept_f"], r["kappa0"]) for r in nonch if not r["kept_f"] > r["kappa0"]])
check("AQ5b", "kappa increases with n in A_n omega2 (n=3..7), D_n half-spin (n=4..7), D_n omega1 (n=4..7)",
      inc(seqA2) and inc(seqDs) and inc(seqD1), "A_n w2 %s; D_n spin %s; D_n w1 %s" % (
          ["%.4f" % v for _, v in seqA2], ["%.4f" % v for _, v in seqDs], ["%.4f" % v for _, v in seqD1]))
if not (inc(seqA2) and inc(seqDs) and inc(seqD1)): say("  [INVERTED] recorded at equal prominence.")

banner("AQ7 -- [P] the bilinear identity on every pair of every case")
check("AQ7", "B(Rw,Rw') - B(w,w') = B(dw,w') + B(w,dw') + B(dw,dw') with dw = Rw - w, exactly, all pairs, all cases",
      all(r["aq7_bad"] == 0 for r in TABLE))

banner("[obs] -- what the table shows (not claimed; a later stone may register it)")
for fam in ("A", "D"):
    for r in TABLE:
        if r["fam"] == fam and not r["chain"]:
            note("%s%d w%d: kappa - kappa0 = %+.4f; a(R)/N = %.3f; nu/N = %s" % (fam, r["n"], r["k"], r["kept_f"] - r["kappa0"], r["agree"]/r["N"], ("%.3f" % (r["nu"]/r["N"])) if r["nu"] is not None else "n/a"))
note("E6 w1: kappa - kappa0 = %+.4f; a/N = %.3f; nu/N = %.3f" % (e6["kept_f"] - e6["kappa0"], e6["agree"]/27, e6["nu"]/27))
note("E7 w7: kappa - kappa0 = %+.4f; a/N = %.3f; nu = 38 (SM-016, cited) -> nu/N = 0.679" % (e7["kept_f"] - e7["kappa0"], e7["agree"]/56))

json.dump({"brief_sha": sha, "table": TABLE}, open(os.path.join("_stone_aq_cache", "table_aq.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
