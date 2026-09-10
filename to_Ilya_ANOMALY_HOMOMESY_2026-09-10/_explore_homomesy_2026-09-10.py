# free exploration (NOT sealed): homomesy under rowmotion on E7 (56), E6 (27) and D5 half-spin (16) from the Cartan-label machine.
# A statistic f on states is homomesic under R iff its average over every R-orbit is the same.
# Statistics: (a) each label l_i (linear; Rush-Wang: colour counts are homomesic); (b) #(+1 labels), #(-1 labels), #(0 labels);
# (c) toggle size |delta(w)| = number of simple roots toggled; (d) per-state kept count: #{u : type(w,u) preserved by R};
# (e) the quadratic form <w,w'> with w' fixed: linear -> covered; (f) number of neighbours (covers up + down).
import os
from fractions import Fraction
from collections import Counter
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
aqsrc = open("verify_stone_aq_rush_shi_defect.py", encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
W_CAP = 400000
exec(compile(aqsrc[start:end], "aq", "exec"))
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
for fam, n, k in [("E", 7, 7), ("E", 6, 1), ("D", 5, 5), ("A", 7, 4), ("D", 7, 7), ("A", 5, 2)]:
    M = Minuscule(fam, n, k); R = M.R; orbs = orbits(R); N = M.N
    print("%s%d w%d: orbits %s" % (fam, n, k, sorted((len(o) for o in orbs), reverse=True)))
    lab = M.W
    # toggle multiset size: delta(w) = R(w) - w as a sum of simple roots -> count with multiplicity
    def toggles(x):
        d = [M.W[R[x]][i] - M.W[x][i] for i in range(n)]      # in label coordinates: delta = sum c_j alpha_j -> labels = C^T c
        # solve C^T c = d  (C symmetric) -> c = Cinv d
        c = [sum(M.Cinv[i][j] * d[j] for j in range(n)) for i in range(n)]
        assert all(v.denominator == 1 for v in c)
        return c
    stats = {
        "#(+1 labels)": lambda x: sum(1 for v in lab[x] if v == 1),
        "#(-1 labels)": lambda x: sum(1 for v in lab[x] if v == -1),
        "#(0 labels)":  lambda x: sum(1 for v in lab[x] if v == 0),
        "toggle size |delta| (with multiplicity)": lambda x: sum(abs(v) for v in toggles(x)),
        "#distinct colours toggled": lambda x: sum(1 for v in toggles(x) if v != 0),
        "#covers below (down-degree)": lambda x: len(M.down[x]),
        "#covers above (up-degree)": lambda x: sum(1 for y in range(N) if x in M.down[y]),
        "rank in L (height)": lambda x: sum(1 for y in range(N) if M.leq[y][x]) - 1,
    }
    # per-state kept count under one tick
    def kept_count(x): return sum(1 for y in range(N) if y != x and M.IP[R[x]][R[y]] == M.IP[x][y])
    stats["kept-count (pairs with x preserved by R)"] = kept_count
    for name, f in stats.items():
        ok, avgs = homomesic(f, orbs)
        print("   %-46s %s  orbit averages %s" % (name, "HOMOMESIC" if ok else "no       ", [str(a) for a in avgs][:6]))
    # linear check (Rush-Wang): orbit-mean label vectors
    means = [tuple(Fraction(sum(lab[x][i] for x in o), len(o)) for i in range(n)) for o in orbs]
    print("   %-46s %s  %s" % ("label vector (Rush-Wang colour counts)", "HOMOMESIC" if len(set(means)) == 1 else "no       ", [tuple(str(v) for v in m) for m in means][:2]))
