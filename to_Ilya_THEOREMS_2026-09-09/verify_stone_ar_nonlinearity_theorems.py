# -*- coding: utf-8 -*-
r"""verify_stone_ar_nonlinearity_theorems.py -- STONE AR: THE NON-LINEARITY THEOREMS (merkabit side)

Brief: BRIEF_STONE_AR_NONLINEARITY_THEOREMS.md (lock BRIEF_STONE_AR_LOCK.sha256, re-verified as check AR0).
The proofs are in the brief; this script re-checks on the data every ingredient they use:
AR1 the lemma data (R(top) = bottom, the bottom's unique cover p0 = R(bottom), <l,l> - <l,w0 l> = c_k = colour-k count);
AR2 Theorem 1 (c_k = 1 <=> chain <=> R in W; on chains R = the product of the simple reflections);
AR3 Theorem 2 (principal orbit = rank truncations; <w(j),w(j+1)> = <l,l> - s_j; extended rank sequence (h/2)-periodic
<=> R^(h/2) in W; the periodic cases); AR4 the vector half-turn formula; AR5 Theorem 3's two kappa formulas (n = 3..9)
and the explicit rowmotion on 2-subsets; AR6 [obs] a(R) >= C(n,2) - (n-1) on A_n omega_2; AR7 REGISTERED GUESS: the
changed-pair count on A_n omega_3 is a degree-4 polynomial in n (interpolant through n = 5..9 predicts n = 10).

Machinery: the Minuscule class of verify_stone_aq_rush_shi_defect.py loaded VERBATIM from that file (its sha256 logged).
DISCIPLINE: compute, never assert; registered guess resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_ar_nonlinearity_theorems.py
"""
import itertools, json, os, sys, time, hashlib, math
from fractions import Fraction
from collections import Counter

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ar_nonlinearity_theorems.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AR -- THE NON-LINEARITY THEOREMS (chains, the half-turn, the kept fraction)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AR_NONLINEARITY_THEOREMS.md"; LOCK = open("BRIEF_STONE_AR_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AR0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AR_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- the AQ machine, VERBATIM (loaded from the sealed file)
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
aqsha = hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices")
end = aqsrc.index("# ---------------------------------------------------------------- the cases")
W_CAP = 400000
exec(compile(aqsrc[start:end], AQ, "exec"))
note("Minuscule machine loaded verbatim from %s (sha256 %s), lines of the Cartan/machine block" % (AQ, aqsha[:16]))

# ---------------------------------------------------------------- helpers
def colour_of(M, p):
    q = M.down[p][0]; d = tuple(M.W[p][i] - M.W[q][i] for i in range(M.n))
    for i in range(M.n):
        if d == tuple(M.C[i]): return i
    raise ValueError("no colour")
def ranks_of_P(M):
    # rank in P = longest chain below within P (min elements rank 0)
    Pset = set(M.P); rk = {}
    for p in sorted(M.P, key=lambda a: sum(1 for b in M.P if M.leq[b][a])):
        below = [q for q in M.P if q != p and M.leq[q][p]]
        rk[p] = 0 if not below else 1 + max(rk[q] for q in below)
    return rk
def in_W(M, g, Wset):
    return (g in Wset) if Wset is not None else M.isometry(g)
def ppow(M, p, e):
    x = tuple(range(M.N))
    for _ in range(e): x = M.compose(p, x)
    return x
def ck_pred(fam, n, k):
    if fam == "A": return min(k, n + 1 - k)
    if fam == "D": return 2 if k == 1 else n // 2
    if fam == "E": return {6: 2, 7: 3}[n]

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
MODELS = {}; WSETS = {}
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); MODELS[(fam, n, k)] = M
    WSETS[(fam, n, k)] = M.enumerate_W() if weyl_order(fam, n) <= W_CAP else None
tick("42 models built, W enumerated where |W| <= %d" % W_CAP)

# ---------------------------------------------------------------- AR1 lemma data
banner("AR1 -- the lemma data on all 42 cases")
ok1 = True; details = []
for key, M in MODELS.items():
    fam, n, k = key
    top, bot = M.top, M.bottom
    covers_of_bottom = [a for a in range(M.N) if bot in M.down[a]]
    p0 = covers_of_bottom[0] if len(covers_of_bottom) == 1 else None
    kstar = [i for i in range(M.n) if M.W[bot][i] != 0]
    ck = M.IP[top][top] - M.IP[top][bot]
    colours = Counter(colour_of(M, p) for p in M.P)
    cond = (M.R[top] == bot and len(covers_of_bottom) == 1 and M.R[bot] == p0 and len(kstar) == 1 and M.W[bot][kstar[0]] == -1
            and tuple(M.W[p0][i] - M.W[bot][i] for i in range(M.n)) == tuple(M.C[kstar[0]])
            and ck == colours[k - 1] and ck == ck_pred(fam, n, k) and min(M.P, key=lambda p: sum(1 for q in M.P if M.leq[q][p])) == p0)
    ok1 &= cond
    if not cond: details.append(key)
check("AR1", "R(top) = bottom; the bottom has one cover p0 = bottom + alpha_{k*} = R(bottom) = min P; <l,l> - <l,w0 l> = c_k = "
      "#colour-k join-irreducibles = the predicted value, all 42 cases", ok1, details or "c_k: " + str({("%s%d w%d" % key): MODELS[key].IP[MODELS[key].top][MODELS[key].top] - MODELS[key].IP[MODELS[key].top][MODELS[key].bottom] for key in list(MODELS)[:8]}) + " ...")

# ---------------------------------------------------------------- AR2 Theorem 1
banner("AR2 -- Theorem 1 on the data: c_k = 1 <=> chain <=> R in W")
ok2 = True; bad = []; conv = Counter()
for key, M in MODELS.items():
    ck = M.IP[M.top][M.top] - M.IP[M.top][M.bottom]; inW = in_W(M, M.R, WSETS[key])
    if not ((ck == 1) == M.chain == inW): ok2 = False; bad.append(key)
    if M.chain:
        fwd = tuple(range(M.N)); bwd = tuple(range(M.N))
        for i in range(M.n): fwd = M.compose(M.S[i], fwd); bwd = M.compose(M.S[M.n - 1 - i], bwd)
        conv["s1..sn" if M.R == fwd else ("sn..s1" if M.R == bwd else "neither")] += 1
check("AR2", "c_k = 1 <=> P is a chain <=> R in W on all 42 cases; on the 12 chains R is a product of the simple reflections in order",
      ok2 and conv.get("neither", 0) == 0 and sum(conv.values()) == 12, "chain convention: %s; failures %s" % (dict(conv), bad))

# ---------------------------------------------------------------- AR3 Theorem 2
banner("AR3 -- Theorem 2 on the data: the principal orbit, the rank sequence, the half-turn")
periodic_cases = []; halfturn_cases = []; ok3 = True; ok3seq = True; bad3 = []
def rect_ranks(n, k): q = min(k, n + 1 - k); return [min(j + 1, q, n - j) for j in range(n)]
def stair_ranks(n): return [sum(1 for i in range(1, n) if i <= (j + 2) / 2 and j + 2 - i <= n - 1) for j in range(2 * n - 3)]
for key, M in MODELS.items():
    fam, n, k = key; h = coxeter_number(fam, n)
    rk = ranks_of_P(M); r = max(rk.values()) + 1
    s = [sum(1 for p in M.P if rk[p] == j) for j in range(r)]
    ck = M.IP[M.top][M.top] - M.IP[M.top][M.bottom]
    ext = s + [ck]
    # principal orbit = rank truncations
    w = M.bottom; orbit_ok = True
    for j in range(h):
        ideal = {p for p in M.P if M.leq[p][w]}
        if ideal != {p for p in M.P if rk[p] < j}: orbit_ok = False
        w2 = M.R[w]
        if M.IP[w][w2] != M.IP[M.top][M.top] - ext[j]: orbit_ok = False
        w = w2
    if w != M.bottom or r + 1 != h: orbit_ok = False
    ok3 &= orbit_ok
    # named rank sequences
    if fam == "A" and 1 < k < n: ok3seq &= (s == rect_ranks(n, k))
    if fam == "D" and k == n and n >= 4: ok3seq &= (s == stair_ranks(n))
    if fam == "D" and k == 1: ok3seq &= (s == [1] * (n - 2) + [2] + [1] * (n - 2) and ck == 2)
    if fam == "E" and n == 6: ok3seq &= (s == [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1] and ck == 2)
    if fam == "E" and n == 7: ok3seq &= (s == [1, 1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1] and ck == 3)
    if h % 2 == 0:
        m = h // 2
        per = all(ext[(j + m) % h] == ext[j] for j in range(h))
        Rm = ppow(M, M.R, m); lin = in_W(M, Rm, WSETS[key])
        if per != lin: bad3.append((key, per, lin))
        if per: periodic_cases.append(key)
        if lin: halfturn_cases.append(key)
check("AR3a", "the R-orbit of the bottom is the rank truncations P_{<j}, of length h, with <w(j),w(j+1)> = <l,l> - s_j (s_r = c_k), all 42 cases", ok3)
check("AR3b", "the rank sequences of the rectangle, the shifted staircase, D_n omega_1, E6, E7 are as stated in the proof (and c_k as stated)", ok3seq)
expected = {key for key in MODELS if MODELS[key].chain and coxeter_number(key[0], key[1]) % 2 == 0} | {("A", 3, 2), ("D", 4, 1), ("D", 4, 3), ("D", 4, 4), ("D", 5, 1), ("D", 6, 1), ("D", 7, 1)}
check("AR3c", "for h even: the extended rank sequence is (h/2)-periodic <=> R^(h/2) in W, and the periodic cases are exactly the even-h chains, "
      "D3..D7 omega_1 (A3 omega_2 = D3) and D4 omega_3/omega_4", not bad3 and set(periodic_cases) == set(halfturn_cases) == expected,
      "mismatches %s; periodic %s" % (bad3, sorted(periodic_cases)))

# ---------------------------------------------------------------- AR4 the vector half-turn formula, n = 3..9
banner("AR4 -- the vector half-turn: R^(n-1) = (e_i -> -e_{n-i}, e_n -> (-1)^(n-1) e_n) in W(D_n), n = 3..9")
def dn_vector_labels(n):
    # simple roots: alpha_i = e_i - e_{i+1} (i < n), alpha_n = e_{n-1} + e_n  (0-based: nodes 0..n-1)
    def lab(v):
        out = []
        for i in range(n - 1): out.append(v[i] - v[i + 1])
        out.append(v[n - 2] + v[n - 1])
        return tuple(out)
    vecs = {}
    for j in range(n):
        for sgn in (1, -1):
            v = [0] * n; v[j] = sgn; vecs[(sgn, j)] = lab(v)
    return vecs
ok4 = True; det4 = []
for n in range(3, 10):
    M = Minuscule("D", n, 1); labs = dn_vector_labels(n); idx = {labs[key]: key for key in labs}
    assert set(idx) == set(M.W), "vector weights mismatch"
    name = {M.idx[labs[key]]: key for key in labs}   # machine index -> (sign, j) with j 0-based
    def img(sgn, j): return name[M.R[M.idx[labs[(sgn, j)]]]]
    # the stated cycle: -e1 -> -e2 -> ... -> -e_{n-1} -> e_{n-1} -> ... -> e1 -> -e1 ; e_n <-> -e_n
    cyc_ok = all(img(-1, j) == (-1, j + 1) for j in range(n - 2)) and img(-1, n - 2) == (1, n - 2) and all(img(1, j) == (1, j - 1) for j in range(1, n - 1)) and img(1, 0) == (-1, 0) and img(1, n - 1) == (-1, n - 1) and img(-1, n - 1) == (1, n - 1)
    Rm = ppow(M, M.R, n - 1)
    def imgm(sgn, j): return name[Rm[M.idx[labs[(sgn, j)]]]]
    form_ok = all(imgm(s_, j) == (-s_, n - 2 - j) for j in range(n - 1) for s_ in (1, -1)) and imgm(1, n - 1) == ((-1) ** (n - 1), n - 1)
    signs = (n - 1) + (1 if n % 2 == 0 else 0)
    Wset = M.enumerate_W() if weyl_order("D", n) <= W_CAP else None
    inW = (Rm in Wset) if Wset is not None else None
    ok4 &= cyc_ok and form_ok and signs % 2 == 0 and (inW is None or inW)
    det4.append((n, cyc_ok, form_ok, signs, inW))
check("AR4", "for n = 3..9 the rowmotion cycle on D_n omega_1 is as stated and R^(n-1) equals the signed permutation e_i -> -e_{n-i}, "
      "e_n -> (-1)^(n-1) e_n, with an even number of sign changes (in W(D_n); membership checked directly for n <= 7)", ok4, det4)

# ---------------------------------------------------------------- AR5 Theorem 3
banner("AR5 -- Theorem 3: the explicit rowmotion on 2-subsets and the two kappa formulas, n = 3..9")
ok5 = True; det5 = []
for n in range(3, 10):
    M = Minuscule("A", n, 2)
    def lab2(a, b):  # e_a + e_b, 1-based a<b, labels <., e_i - e_{i+1}>
        return tuple(int(i == a) - int(i + 1 == a) + int(i == b) - int(i + 1 == b) for i in range(1, n + 1))
    subs = {(a, b): lab2(a, b) for a in range(1, n + 2) for b in range(a + 1, n + 2)}
    assert set(subs.values()) == set(M.W)
    back = {M.idx[v]: ab for ab, v in subs.items()}
    def Rexp(a, b):
        if a >= 2 and b >= a + 2: return (a - 1, b - 1)
        if a >= 2 and b == a + 1: return (a - 1, n + 1)
        if a == 1 and b >= 3: return (b - 2, b - 1)
        return (n, n + 1)
    form_ok = all(back[M.R[M.idx[subs[(a, b)]]]] == Rexp(a, b) for (a, b) in subs)
    N = M.N; tot = N * (N - 1) // 2
    kapA = M.kept(M.R); predA = 1 - Fraction(3 * n * n - 9 * n + 4, tot)
    MD = Minuscule("D", n, 1); kapD = MD.kept(MD.R); predD = 1 - Fraction(2 * (n - 1), n * (2 * n - 1))
    ok5 &= form_ok and kapA == predA and kapD == predD
    det5.append((n, form_ok, str(kapA), str(predA), str(kapD), str(predD)))
check("AR5", "n = 3..9: the explicit R on 2-subsets equals the machine's R; kappa(A_n w2) = 1 - (3n^2-9n+4)/C(C(n+1,2),2) and "
      "kappa(D_n w1) = 1 - 2(n-1)/(n(2n-1)) exactly", ok5, det5)
tick("AR5 done")

# ---------------------------------------------------------------- AR6 [obs]
banner("AR6 -- [obs] a(R) >= C(n,2) - (n-1) on A_n omega_2")
det6 = []
for n in range(3, 9):
    M = Minuscule("A", n, 2); cox = M.coxeter_elements()
    a = max(sum(1 for x in range(M.N) if M.R[x] == c[x]) for c in cox); bound = math.comb(n, 2) - (n - 1)
    det6.append((n, a, bound, a == bound))
check("AR6", "[obs] a(R) >= C(n,2) - (n-1) for n = 3..8 (equality where marked)", all(a >= b for _, a, b, _ in det6), det6)
tick("AR6 done")

# ---------------------------------------------------------------- AR7 registered guess
banner("AR7 -- REGISTERED GUESS: the changed-pair count on A_n omega_3 is a degree-4 polynomial in n")
D3 = {}
for n in range(5, 11):
    M = Minuscule("A", n, 3); N = M.N; tot = N * (N - 1) // 2
    D3[n] = (1 - M.kept(M.R)) * tot
    assert D3[n].denominator == 1; D3[n] = int(D3[n])
    tick("A%d w3: N = %d, changed pairs %d" % (n, N, D3[n]))
def lagrange(xs, ys, x):
    tot = Fraction(0)
    for i, xi in enumerate(xs):
        term = Fraction(ys[i])
        for j, xj in enumerate(xs):
            if j != i: term *= Fraction(x - xj, xi - xj)
        tot += term
    return tot
pred10 = lagrange(list(range(5, 10)), [D3[n] for n in range(5, 10)], 10)
# finite differences for the record
seq = [D3[n] for n in range(5, 11)]; diffs = [seq]
while len(diffs[-1]) > 1: diffs.append([b - a for a, b in zip(diffs[-1], diffs[-1][1:])])
ok7 = (pred10 == D3[10])
check("AR7", "REGISTERED GUESS: the degree-4 interpolant through n = 5..9 predicts D3(10) = %s; measured %d" % (pred10, D3[10]), ok7,
      "D3(n) n=5..10: %s; difference table: %s" % (seq, diffs[1:]))
if not ok7: say("  [INVERTED] recorded at equal prominence.")

json.dump({"brief_sha": sha, "aq_sha": aqsha, "periodic_cases": [list(k) for k in periodic_cases], "AR4": det4, "AR5": det5, "AR6": det6, "AR7": {"D3": D3, "pred10": str(pred10)}},
          open(os.path.join("_stone_ar_cache", "witnesses_ar.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
