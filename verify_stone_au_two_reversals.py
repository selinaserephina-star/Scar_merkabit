# -*- coding: utf-8 -*-
r"""verify_stone_au_two_reversals.py -- STONE AU: THE REVERSAL THEOREM, THE SHADOW, THE MIRROR AS TWO REVERSALS

Brief: BRIEF_STONE_AU_TWO_REVERSALS.md (lock BRIEF_STONE_AU_LOCK.sha256, re-verified as AU0).
AU1 w0 R w0 = R^-1 on all 42 boards (the theorem's data); AU2 pairs preserved by R^k = fix(R^2k)/2 on self-dual boards
(E7: SM-044's column); AU3 the two reversals on the 56 (w0(E6) in W(E6), reverses Psi6 not Psi; iota reverses both);
AU4 pr = iota o w0(E6) o t (t = pole swap); AU5 GUESS: the reversers of Psi in W(E7) are {iota}, of Psi6 in W(E6) are
{w0(E6)}; AU6 consequences (pr commutes with Psi6, not with Psi; pr^2 = 1); AU7 [obs] relation table.
Machinery: AQ machine VERBATIM; AP board block VERBATIM; numpy BFS enumeration of W(E6), W(E7) on the 56.
DISCIPLINE: compute, never assert; registered guess resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_au_two_reversals.py
"""
import itertools, json, os, sys, time, hashlib, math
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_au_two_reversals.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AU -- THE REVERSAL THEOREM, THE SHADOW, AND THE MIRROR AS THE PRODUCT OF TWO REVERSALS"); say("=" * 78)
BRIEF = "BRIEF_STONE_AU_TWO_REVERSALS.md"; LOCK = open("BRIEF_STONE_AU_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AU0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AU_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- AQ machine VERBATIM
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
note("Minuscule machine loaded verbatim from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16]))
def diagram_aut(fam, n):
    if fam == "A": return {i: n - 1 - i for i in range(n)}
    if fam == "D": return {**{i: i for i in range(n - 2)}, n - 2: n - 1, n - 1: n - 2}
    if fam == "E" and n == 6: return {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
    return {i: i for i in range(n)}
def tcomp(p, q): return tuple(p[q[i]] for i in range(len(p)))
def tinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def tpow(p, e):
    x = tuple(range(len(p)))
    for _ in range(e): x = tcomp(p, x)
    return x

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
banner("AU1 -- the reversal theorem on all 42 boards; AU2 -- the shadow corollary on the self-dual ones")
ok1 = True; bad1 = []; ok2 = True; bad2 = []; e7col = None; selfdual_cases = []
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); r = n; h = coxeter_number(fam, n)
    minus_in_W = (fam == "D" and n % 2 == 0) or (fam == "E" and n == 7)
    sig = diagram_aut(fam, n) if not minus_in_W else {i: i for i in range(r)}; inv_sig = {v: u for u, v in sig.items()}
    w0 = tuple(M.idx[tuple(-w[inv_sig[j]] for j in range(r))] for w in M.W)
    R = tuple(M.R)
    inW = (w0 in M.enumerate_W()) if weyl_order(fam, n) <= W_CAP else M.isometry(list(w0))
    good = inW and w0[M.top] == M.bottom and tcomp(tcomp(w0, R), w0) == tinv(R)
    ok1 &= good
    if not good: bad1.append((fam, n, k))
    lam = M.W[M.top]
    if tuple(-x for x in lam) in M.idx:
        selfdual_cases.append((fam, n, k))
        IO = tuple(M.idx[tuple(-x for x in w)] for w in M.W)
        col = []
        for kk in range(1, h):
            Rk = tpow(R, kk); R2k = tpow(R, 2 * kk)
            kept = sum(1 for a in range(M.N) if a < IO[a] and Rk[IO[a]] == IO[Rk[a]])
            fix2 = sum(1 for a in range(M.N) if R2k[a] == a)
            col.append((kept, fix2 // 2))
            if kept != fix2 // 2: ok2 = False; bad2.append((fam, n, k, kk, kept, fix2))
        if (fam, n, k) == ("E", 7, 7): e7col = [c[0] for c in col]
tick("42 boards done")
check("AU1", "on all 42 boards w0 = -sigma lies in W, sends the top to the bottom, and w0 R w0 = R^-1", ok1, bad1)
check("AU2", "on every self-dual board (%d) and every k: #antipodal pairs preserved by R^k = fix(R^2k)/2; E7 column = %s" % (len(selfdual_cases), e7col),
      ok2 and e7col == [1] * 8 + [28] + [1] * 8, bad2[:8] or selfdual_cases)

# ---------------------------------------------------------------- the 56-board, AP block VERBATIM
AP = "verify_stone_ap_clock_centralizer.py"; apsrc = open(AP, encoding="utf-8").read(); fence = "# " + "=" * 69
blk = apsrc.split(fence)[2]; blk = blk[blk.index("\n") + 1:]; exec(compile(blk, AP, "exec"))
note("board block loaded verbatim from %s (sha256 %s); scar56_data.json sha256 %s" % (AP, hashlib.sha256(apsrc.encode("utf-8")).hexdigest()[:16], hashlib.sha256(open("scar56_data.json", "rb").read()).hexdigest()[:16]))
PR = D["PR"]
def comp(p, q): return [p[q[k]] for k in range(56)]
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def islin(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
def cyc(p):
    seen_ = set(); c = []
    for a in range(56):
        if a in seen_: continue
        x = a; L = 0
        while x not in seen_: seen_.add(x); L += 1; x = p[x]
        c.append(L)
    return sorted(c, reverse=True)
def porder(p):
    x = list(range(56)); n_ = 0
    while True:
        x = comp(p, x); n_ += 1
        if x == list(range(56)): return n_
labels = {k: tuple(verts[k]) for k in range(56)}
C7inv = [[Fraction(x) for x in row] for row in np.linalg.inv(np.array(C7, dtype=float)).round(6).tolist()]
def cow6(k): return sum(C7inv[6][j] * labels[k][j] for j in range(7))
sheet = {k: cow6(k) for k in range(56)}; poles = [k for k in range(56) if abs(sheet[k]) == Fraction(3, 2)]
banner("AU3 -- the two reversals on the 56")
check("AU3a", "the node-7 coweight splits the 56 into two poles (+-3/2) and two 27-sheets (+-1/2) (SM-053 AO1)",
      Counter(sheet.values()) == Counter({Fraction(1, 2): 27, Fraction(-1, 2): 27, Fraction(3, 2): 1, Fraction(-3, 2): 1}))
def sheet_rowmotion():
    R6 = [None] * 56
    for sval in (Fraction(1, 2), Fraction(-1, 2)):
        S = [k for k in range(56) if sheet[k] == sval]; down = {k: [] for k in S}
        for k in S:
            for i in range(6):
                if labels[k][i] == 1:
                    tgt = tuple(labels[k][j] - C7[i][j] for j in range(7))
                    for m in S:
                        if labels[m] == tgt: down[k].append(m)
        below = {k: set() for k in S}
        order = sorted(S, key=lambda a: sum(C7inv[i][j] * labels[a][j] for i in range(6) for j in range(7)))
        for a in order:
            for b in down[a]: below[a] |= {b} | below[b]
        leq = lambda a, b: a == b or a in below[b]
        P = [a for a in S if len(down[a]) == 1]
        for x in S:
            Sx = [p for p in P if not leq(p, x)]
            if not Sx: R6[x] = next(a for a in S if not down[a]); continue
            mins = [p for p in Sx if not any(q != p and leq(q, p) for q in Sx)]
            ub = [y for y in S if all(leq(p, y) for p in mins)]
            join = [y for y in ub if not any(z != y and leq(z, y) for z in ub)]
            assert len(join) == 1; R6[x] = join[0]
    for p in poles: R6[p] = p
    return R6
PSI6 = sheet_rowmotion()
check("AU3b", "the sheet clock Psi6 (rowmotion on each sheet from the E6 covers, poles fixed) has cycle type [12,12,3]^2 1^2 and order 12",
      cyc(PSI6) == [12, 12, 12, 12, 3, 3, 1, 1] and porder(PSI6) == 12, cyc(PSI6))
sig6 = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
by_sheet = {}
for k in range(56): by_sheet.setdefault(sheet[k], {})[labels[k][:6]] = k
w0e6 = [k if k in poles else by_sheet[sheet[k]][tuple(-labels[k][:6][sig6[j]] for j in range(6))] for k in range(56)]
# W(E6) and W(E7) on the 56 by BFS
def enum(gens_):
    gens_ = [np.array(s, dtype=np.uint8) for s in gens_]; ident = np.arange(56, dtype=np.uint8)
    seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
    while len(frontier):
        cand = np.concatenate([frontier[:, g] for g in gens_], axis=0); keep = []
        for row in cand:
            b = row.tobytes()
            if b not in seen: seen.add(b); keep.append(row)
        frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, 56), dtype=np.uint8)
        if len(frontier): layers.append(frontier)
    return np.concatenate(layers, axis=0), seen
G6, W6b = enum(S7[:6]); G7, W7b = enum(S7); tick("W(E6) = %d, W(E7) = %d enumerated on the 56" % (len(G6), len(G7)))
w0b = np.array(w0e6, dtype=np.uint8).tobytes()
check("AU3c", "w0(E6) (labels -> -sigma(labels) on each sheet, poles fixed) lies in W(E6) (51,840 on the 56) and is an involution",
      len(G6) == 51840 and w0b in W6b and comp(w0e6, w0e6) == list(range(56)))
rev6 = comp(comp(w0e6, PSI6), w0e6) == pinv(PSI6); rev7 = comp(comp(w0e6, PSI), w0e6) == pinv(PSI)
irev6 = comp(comp(IOTA, PSI6), IOTA) == pinv(PSI6); irev7 = comp(comp(IOTA, PSI), IOTA) == pinv(PSI)
check("AU3d", "w0(E6) reverses the sheet clock Psi6 and does NOT reverse the board clock Psi; iota reverses both",
      rev6 and not rev7 and irev6 and irev7, (rev6, rev7, irev6, irev7))
banner("AU4 -- the mirror identity")
t = list(range(56)); t[poles[0]], t[poles[1]] = poles[1], poles[0]
cand = comp(IOTA, w0e6)
check("AU4", "pr = iota o w0(E6) o t exactly (t the pole swap); pr o t = iota o w0(E6) is SM-016's nearest Weyl element; agreement without t is 54/56",
      PR == comp(cand, t) and comp(PR, t) == cand and sum(1 for k in range(56) if PR[k] == cand[k]) == 54 and islin(cand))
banner("AU5 -- REGISTERED GUESS: the reversers are unique")
PSI_A = np.array(PSI, dtype=np.uint8); PSIi_A = np.array(pinv(PSI), dtype=np.uint8)
PSI6_A = np.array(PSI6, dtype=np.uint8); PSI6i_A = np.array(pinv(PSI6), dtype=np.uint8)
rev_in_W7 = np.nonzero(np.all(G7[:, PSI_A] == PSIi_A[G7], axis=1))[0]           # g Psi = Psi^-1 g
rev6_in_W6 = np.nonzero(np.all(G6[:, PSI6_A] == PSI6i_A[G6], axis=1))[0]
ok5 = (len(rev_in_W7) == 1 and G7[rev_in_W7[0]].tolist() == IOTA) and (len(rev6_in_W6) == 1 and G6[rev6_in_W6[0]].tolist() == w0e6)
check("AU5", "REGISTERED GUESS: exactly one element of W(E7) reverses Psi (iota) and exactly one element of W(E6) reverses Psi6 (w0(E6))",
      ok5, "reversers in W(E7): %d, in W(E6): %d" % (len(rev_in_W7), len(rev6_in_W6)))
if not ok5: say("  [INVERTED] recorded at equal prominence.")
# how many of W(E7) reverse Psi6?  (obs)
rev6_in_W7 = int(np.all(G7[:, PSI6_A] == PSI6i_A[G7], axis=1).sum())
note("[obs] elements of W(E7) that reverse the sheet clock Psi6: %d" % rev6_in_W7)
banner("AU6 -- consequences of the identity")
check("AU6", "pr commutes with Psi6 (both factors reverse it, t fixes the sheets); pr neither commutes with nor reverses Psi; pr^2 = 1; iota and w0(E6) commute; both commute with t",
      comp(PR, PSI6) == comp(PSI6, PR) and comp(PR, PSI) != comp(PSI, PR) and comp(comp(PR, PSI), PR) != pinv(PSI) and comp(PR, PR) == list(range(56))
      and comp(IOTA, w0e6) == comp(w0e6, IOTA) and comp(IOTA, t) == comp(t, IOTA) and comp(w0e6, t) == comp(t, w0e6))
banner("AU7 -- [obs] the relation table")
names = {"iota": IOTA, "w0E6": w0e6, "t": t, "pr": PR, "Psi": PSI, "Psi6": PSI6, "iota.w0E6": cand}
for a in ("iota", "w0E6", "t", "pr", "iota.w0E6"):
    note("%-10s order %2d  cycle type %s  fixed %d  linear %s" % (a, porder(names[a]), Counter(cyc(names[a])).most_common(), sum(1 for k in range(56) if names[a][k] == k), islin(names[a])))
for a, b in (("iota", "w0E6"), ("iota", "pr"), ("w0E6", "pr"), ("w0E6", "Psi"), ("w0E6", "Psi6"), ("iota.w0E6", "Psi"), ("pr", "Psi6"), ("iota", "Psi6")):
    note("order of %s * %s = %d" % (a, b, porder(comp(names[a], names[b]))))
json.dump({"brief_sha": sha, "poles": poles, "w0E6": w0e6, "PSI6": PSI6, "e7_pairs_column": e7col, "reversers_W7": int(len(rev_in_W7)), "reversers_W6": int(len(rev6_in_W6)), "rev6_in_W7": rev6_in_W7},
          open(os.path.join("_stone_au_cache", "witnesses_au.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
