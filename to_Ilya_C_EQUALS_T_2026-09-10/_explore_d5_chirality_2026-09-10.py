# free exploration (NOT sealed): IB's prediction 2 -- do the D5 clock's two orbits coincide with the two D4 chiralities
# (sign of e5, equivalently parity of minus signs among e1..e4), and do the survivors respect that split?
import os, itertools
from fractions import Fraction
from collections import Counter
import numpy as np
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
src = open("verify_stone_av_d5_anomaly.py", encoding="utf-8").read()
blk = src[src.index("# ---------------------------------------------------------------- e-coordinate board machine"):src.index("W5, idx5, S5, R5, P5, leq5 = D_half(5)")]
exec(blk)
W5, idx5, S5, R5, P5, leq5 = D_half(5); WD5 = closure(S5)
O = orbits(R5)
chir = {i: ("+" if w[4] > 0 else "-") for i, w in enumerate(W5)}      # D4 chirality = sign of e5
for o in O:
    print("orbit of size %d: e5 signs %s ; minus-parity of e1..e4 %s" % (len(o), dict(Counter(chir[x] for x in o)), dict(Counter(sum(1 for c in W5[x][:4] if c < 0) % 2 for x in o))))
I3, C3 = IC(R5, WD5, 3); I4, C4 = IC(R5, WD5, 4)
ident = tuple(range(16))
def chir_action(g):
    m = Counter((chir[x], chir[g[x]]) for x in range(16))
    return "preserves chirality" if all(a == b for a, b in m) else ("swaps chirality" if all(a != b for a, b in m) else "mixes chirality")
for name, S, C in (("lag 3", I3, C3), ("half-turn", I4, C4)):
    for g in S:
        if g == ident: continue
        print("%-9s %-6s %-12s %-20s %s" % (name, ctype(g), "centralizer" if g in C else "EXTRA", chir_action(g), signed_perm(g, W5, 5)))
for k in (1, 2, 3, 4):
    print("R^%d: %s" % (k, chir_action(ppow(R5, k))))
stab = [g for g in WD5 if chir_action(g) != "mixes chirality"]
print("elements of W(D5) preserving-or-swapping the D4 chirality split: %d of %d" % (len(stab), len(WD5)))
print("half-turn survivors inside that stabilizer: %d of %d; centralizer inside: %d of %d" % (sum(1 for g in I4 if g in stab), len(I4), sum(1 for g in C4 if g in stab), len(C4)))
# does the clock's orbit split coincide with the chirality split?
orb_sets = [set(o) for o in O]; chir_sets = [set(i for i in range(16) if chir[i] == s) for s in "+-"]
print("clock orbits == chirality classes:", sorted(map(frozenset, orb_sets)) == sorted(map(frozenset, chir_sets)))
