# free exploration (NOT sealed): the two time reversals on the 56-board and the mirror.
# w0(E7) = iota (the antipode).  w0(E6) acts on each 27-sheet as -sigma (sigma = the E6 diagram automorphism 0<->5, 2<->4).
# Questions: (1) is w0(E6) in W(E6) on the 56 and does it reverse the sheet clock Psi6 and the board clock Psi?
#            (2) is pr o (pole swap) = iota o w0(E6)  -- i.e. is SM-016's nearest Weyl element to the mirror the product of the two reversals?
#            (3) shadow: pairs preserved by Psi^k = fixed points of Psi^(2k) / 2 (corollary of the reversal), against SM-044's table.
import os, itertools, json, math
from fractions import Fraction
from collections import Counter
import numpy as np
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
src = open("verify_stone_ap_clock_centralizer.py", encoding="utf-8").read()
fence = "# " + "=" * 69
blk = src.split(fence)[2]; blk = blk[blk.index("\n") + 1:]; exec(blk)
PR = D["PR"]
def comp(p, q): return [p[q[k]] for k in range(56)]
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def ppw(p, e):
    x = list(range(56))
    for _ in range(e): x = comp(p, x)
    return x
def islin(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
labels = {k: tuple(verts[k]) for k in range(56)}
# sheets and poles by the node-6 coweight (Bourbaki node 7 = index 6): value = sum_j C7inv[6][j] * label_j
C7inv = [[Fraction(x) for x in row] for row in np.linalg.inv(np.array(C7, dtype=float)).round(6).tolist()]
def cow6(k): return sum(C7inv[6][j] * labels[k][j] for j in range(7))
classes = Counter(cow6(k) for k in range(56)); print("node-6 coweight classes:", dict(classes))
poles = [k for k in range(56) if abs(cow6(k)) == Fraction(3, 2)]
sheet = {k: cow6(k) for k in range(56)}
sig = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
# w0(E6) candidate: on each sheet, labels (l0..l5) -> (-l_{sig^-1(j)}) ; poles fixed
by_sheet = {}
for k in range(56): by_sheet.setdefault(sheet[k], {})[labels[k][:6]] = k
w0e6 = [None] * 56
for k in range(56):
    if k in poles: w0e6[k] = k; continue
    l = labels[k][:6]; tgt = tuple(-l[sig[j]] for j in range(6))
    w0e6[k] = by_sheet[sheet[k]][tgt]
assert sorted(w0e6) == list(range(56))
# W(E6) on the 56 from the six simple reflections S7[0..5]; is w0e6 in it?  is it the longest element?
gens = [tuple(s) for s in S7[:6]]
seen = {tuple(range(56))}; frontier = [tuple(range(56))]
while frontier:
    nxt = []
    for g in frontier:
        for s in gens:
            h = tuple(s[g[i]] for i in range(56))
            if h not in seen: seen.add(h); nxt.append(h)
    frontier = nxt
print("|W(E6)| on the 56:", len(seen), " w0(E6) candidate in W(E6):", tuple(w0e6) in seen, " linear:", islin(w0e6))
# reversal properties
PSI6 = None
print("w0(E6) reverses the board clock Psi (w0 Psi w0 = Psi^-1):", comp(comp(w0e6, PSI), w0e6) == pinv(PSI))
# the sheet clock Psi6: rowmotion on each sheet = the E6 rowmotion; from SM-041/053 it is Psi restricted?  No -- Psi6 is the sheet's own rowmotion.
# Build it from the sheet lattice: within a sheet, covers are subtraction of an E6 simple root (nodes 0..5).
def sheet_rowmotion():
    R6 = [None] * 56
    for sval in (Fraction(1, 2), Fraction(-1, 2)):
        S = [k for k in range(56) if sheet[k] == sval]
        # lattice on the sheet by E6 covers
        down = {k: [] for k in S}
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
def cyc(p):
    seen_ = set(); c = []
    for a in range(56):
        if a in seen_: continue
        x = a; L = 0
        while x not in seen_: seen_.add(x); L += 1; x = p[x]
        c.append(L)
    return sorted(c, reverse=True)
print("sheet clock Psi6 cycle type on the 56:", cyc(PSI6), " (expected [12,12,3,12,12,3,1,1])")
print("w0(E6) reverses the sheet clock (w0 Psi6 w0 = Psi6^-1):", comp(comp(w0e6, PSI6), w0e6) == pinv(PSI6))
print("iota reverses the sheet clock? :", comp(comp(IOTA, PSI6), IOTA) == pinv(PSI6), "  pr commutes with Psi6 (SM-053):", comp(PR, PSI6) == comp(PSI6, PR))
# (2) the mirror against the two reversals
t = list(range(56)); t[poles[0]], t[poles[1]] = poles[1], poles[0]
w_sm016 = comp(PR, t)                      # SM-016: pr o (pole swap) is a Weyl element
cand = comp(IOTA, w0e6)
print("pr o (pole swap) == iota o w0(E6):", w_sm016 == cand, " | pr == iota o w0(E6) o (pole swap):", PR == comp(cand, t))
print("agreement of pr with iota o w0(E6) pointwise:", sum(1 for k in range(56) if PR[k] == cand[k]), "of 56")
# (3) shadow: pairs preserved by Psi^k vs fixed points of Psi^(2k)/2
for k in (1, 2, 3, 9):
    Pk = ppw(PSI, k)
    kept_pairs = sum(1 for a in range(56) if a < IOTA[a] and Pk[IOTA[a]] == IOTA[Pk[a]])
    fixed2k = sum(1 for a in range(56) if ppw(PSI, 2 * k)[a] == a)
    print("k = %d: antipodal pairs preserved by Psi^k = %d ; fixed points of Psi^(2k) / 2 = %d" % (k, kept_pairs, fixed2k // 2))
