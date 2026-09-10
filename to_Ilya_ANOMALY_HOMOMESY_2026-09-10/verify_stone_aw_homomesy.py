# -*- coding: utf-8 -*-
r"""verify_stone_aw_homomesy.py -- STONE AW: HOMOMESY ON THE BOARDS

Brief: BRIEF_STONE_AW_HOMOMESY.md (lock BRIEF_STONE_AW_LOCK.sha256, re-verified as AW0).
AW1 Rush-Wang on the data (orbit-mean weights zero, 42 boards); AW2 the ternary label counts homomesic with means |P|/h,
|P|/h, r - 2|P|/h; AW3 GUESS: toggle size |I delta R(I)| homomesic with mean 2|P|/h; AW4 registered negatives;
AW5 GUESS: on the 56 the ternary counts are homomesic under Psi6 and pr, the kept count under neither, and NOT under pr.Psi;
AW6 [obs] the table.  Machinery: AQ machine VERBATIM; AP board block VERBATIM; sheet rowmotion VERBATIM from Stone AU.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_aw_homomesy.py
"""
import os, sys, time, json, hashlib, itertools
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_aw_homomesy.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AW -- HOMOMESY ON THE BOARDS: WHAT THE CLOCK CONSERVES ON AVERAGE"); say("=" * 78)
BRIEF = "BRIEF_STONE_AW_HOMOMESY.md"; LOCK = open("BRIEF_STONE_AW_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AW0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AW_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
note("Minuscule machine loaded verbatim from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16]))
def orbits(p):
    seen = set(); out = []
    for a in range(len(p)):
        if a in seen: continue
        o = []; x = a
        while x not in seen: seen.add(x); o.append(x); x = p[x]
        out.append(o)
    return out
def homomesic(f, orbs):
    avgs = [Fraction(sum(f(x) for x in o), len(o)) for o in orbs]
    return len(set(avgs)) == 1, avgs

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
banner("AW1-AW4 -- all 42 boards")
ok1 = ok2 = ok3 = True; bad = []; neg = {"colours": 0, "kept": 0, "below": 0}; nonchain = 0; TABLE = []
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); R = M.R; orbs = orbits(R); N = M.N; h = coxeter_number(fam, n); r = n; lab = M.W
    means = [tuple(Fraction(sum(lab[x][i] for x in o), len(o)) for i in range(r)) for o in orbs]
    if not all(m == tuple([Fraction(0)] * r) for m in means): ok1 = False; bad.append(("AW1", fam, n, k))
    def toggles(x):
        d = [lab[R[x]][i] - lab[x][i] for i in range(r)]
        return [sum(M.Cinv[i][j] * d[j] for j in range(r)) for i in range(r)]
    fplus = lambda x: sum(1 for v in lab[x] if v == 1); fminus = lambda x: sum(1 for v in lab[x] if v == -1); fzero = lambda x: sum(1 for v in lab[x] if v == 0)
    ftog = lambda x: sum(abs(v) for v in toggles(x))
    fcol = lambda x: sum(1 for v in toggles(x) if v != 0)
    fkept = lambda x: sum(1 for y in range(N) if y != x and M.IP[R[x]][R[y]] == M.IP[x][y])
    fbelow = lambda x: sum(1 for y in range(N) if M.leq[y][x]) - 1
    hp, ap = homomesic(fplus, orbs); hm, am = homomesic(fminus, orbs); hz, az = homomesic(fzero, orbs)
    P_over_h = Fraction(len(M.P), h)
    if not (hp and hm and hz and ap[0] == P_over_h and am[0] == P_over_h and az[0] == r - 2 * P_over_h): ok2 = False; bad.append(("AW2", fam, n, k, str(ap[0]), str(am[0]), str(az[0])))
    ht, at = homomesic(ftog, orbs)
    if not (ht and at[0] == 2 * P_over_h): ok3 = False; bad.append(("AW3", fam, n, k, [str(a) for a in at]))
    if not M.chain:
        nonchain += 1
        if not homomesic(fcol, orbs)[0]: neg["colours"] += 1
        if not homomesic(fkept, orbs)[0]: neg["kept"] += 1
        if not homomesic(fbelow, orbs)[0]: neg["below"] += 1
    TABLE.append(dict(fam=fam, n=n, k=k, N=N, P=len(M.P), h=h, orbits=sorted((len(o) for o in orbs), reverse=True), plus=str(ap[0]), zero=str(az[0]), toggle=str(at[0]), chain=M.chain))
    tick("%s%d w%d: orbits %s  +1 %s  0 %s  toggle %s" % (fam, n, k, sorted((len(o) for o in orbs), reverse=True), ap[0], az[0], at[0]))
check("AW1", "Rush-Wang seen on the data: the mean weight of every rowmotion orbit is zero on all 42 boards", ok1, [b for b in bad if b[0] == "AW1"])
check("AW2", "the ternary label counts #(+1), #(-1), #(0) are homomesic on all 42 boards with means |P|/h, |P|/h, r - 2|P|/h", ok2, [b for b in bad if b[0] == "AW2"][:6])
check("AW3", "REGISTERED GUESS: the toggle size |I delta R(I)| is homomesic on all 42 boards with mean 2|P|/h", ok3, [b for b in bad if b[0] == "AW3"][:6])
if not ok3: say("  [INVERTED] recorded at equal prominence.")
check("AW4", "registered negatives on every non-chain board (%d): #distinct colours toggled, the kept count, and the number of lattice elements below are NOT homomesic" % nonchain,
      neg["colours"] == nonchain and neg["kept"] == nonchain and neg["below"] == nonchain, neg)

banner("AW5 -- REGISTERED GUESS: on the 56 under the sheet clock, the mirror, and pr.Psi")
AP = "verify_stone_ap_clock_centralizer.py"; apsrc = open(AP, encoding="utf-8").read(); fence = "# " + "=" * 69
blk = apsrc.split(fence)[2]; blk = blk[blk.index("\n") + 1:]; exec(compile(blk, AP, "exec"))
PR = D["PR"]
def comp(p, q): return [p[q[k]] for k in range(56)]
labels = {k: tuple(verts[k]) for k in range(56)}
C7inv = [[Fraction(x) for x in row] for row in np.linalg.inv(np.array(C7, dtype=float)).round(6).tolist()]
def cow6(k): return sum(C7inv[6][j] * labels[k][j] for j in range(7))
sheet = {k: cow6(k) for k in range(56)}; poles = [k for k in range(56) if abs(sheet[k]) == Fraction(3, 2)]
# sheet rowmotion VERBATIM from verify_stone_au_two_reversals.py
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
def tern(k, which, six=False):
    L = labels[k][:6] if six else labels[k]
    return sum(1 for v in L if v == which)
def kept56(p): return lambda x: sum(1 for y in range(56) if y != x and ptype(p[x], p[y]) == ptype(x, y))
res = {}
for name, p, six in (("Psi6 (E6 labels, per sheet)", PSI6, True), ("pr", PR, False), ("pr.Psi", comp(PR, PSI), False), ("Psi", PSI, False)):
    orbs = orbits(p)
    res[name] = {w: homomesic(lambda x, w=w: tern(x, w, six), orbs)[0] for w in (1, -1, 0)}
    res[name]["kept"] = homomesic(kept56(p), orbs)[0]
    note("%-28s orbits %s  ternary counts homomesic %s  kept-count homomesic %s" % (name, Counter(len(o) for o in orbs).most_common(), [res[name][w] for w in (1, -1, 0)], res[name]["kept"]))
ok5 = (all(res["Psi6 (E6 labels, per sheet)"][w] for w in (1, -1, 0)) and all(res["pr"][w] for w in (1, -1, 0))
       and not res["Psi6 (E6 labels, per sheet)"]["kept"] and not res["pr"]["kept"] and not all(res["pr.Psi"][w] for w in (1, -1, 0)))
check("AW5", "REGISTERED GUESS: on the 56 the ternary counts are homomesic under Psi6 (E6 labels) and under pr; the kept count under neither; the ternary counts NOT homomesic under pr.Psi", ok5, res)
if not ok5: say("  [INVERTED] recorded at equal prominence.")
# POST-REVEAL, labelled: the sheet clock on the sheets alone (the two poles are fixed points of Psi6 and were included as size-1 orbits above)
orbs6 = [o for o in orbits(PSI6) if len(o) > 1]
res6 = {w: homomesic(lambda x, w=w: tern(x, w, True), orbs6)[0] for w in (1, -1, 0)}
avg6 = {w: [str(a) for a in homomesic(lambda x, w=w: tern(x, w, True), orbs6)[1]] for w in (1, -1, 0)}
check("AW5b", "POST-REVEAL: on the two 27-sheets alone (poles excluded) the ternary E6-label counts are homomesic under the sheet clock Psi6 across both sheets (Rush-Wang on each E6 sheet; means 4/3, 4/3, 10/3)",
      all(res6.values()) and avg6[1][0] == "4/3" and avg6[0][0] == "10/3", avg6)
json.dump({"brief_sha": sha, "table": TABLE, "AW5": {k: {str(a): b for a, b in v.items()} for k, v in res.items()}}, open(os.path.join("_stone_aw_cache", "table_aw.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
