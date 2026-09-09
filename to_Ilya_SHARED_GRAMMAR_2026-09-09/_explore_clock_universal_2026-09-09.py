# free exploration (NOT sealed): is the clock a universal gate relative to the Weyl group?  <W(E7), Psi> = ?  <W(E7), pr> = ?
# and does any reflection of W(E7) stay a symmetry after one tick (Psi s Psi^-1 linear)?
import itertools, json, math, os
from collections import Counter
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
src = open("verify_stone_ap_clock_centralizer.py", encoding="utf-8").read()
fence = "# " + "=" * 69
parts = src.split(fence)
blk = parts[2]                      # the VERBATIM board block (between the first and second fences)
blk = blk[blk.index("\n") + 1:]     # drop the "# VERBATIM ..." comment line
exec(blk)
PR = D["PR"]
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def comp(p, q): return [p[q[k]] for k in range(56)]
def islin(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
def sign(p):
    seen = set(); s = 0
    for a in range(56):
        if a in seen: continue
        x = a; L = 0
        while x not in seen: seen.add(x); L += 1; x = p[x]
        s += L - 1
    return (-1) ** s
W = PermutationGroup([Permutation(list(s)) for s in S7])
print("|W(E7)| on 56 =", W.order(), "(expected 2903040)")
print("parity: Psi", sign(PSI), " pr", sign(PR), " iota", sign(IOTA), " reflection", sign(S7[0]))
G1 = PermutationGroup([Permutation(list(s)) for s in S7] + [Permutation(list(PSI))])
o1 = G1.order(); print("|<W, Psi>| = 56!/2 ?", o1 == math.factorial(56) // 2, " = 56! ?", o1 == math.factorial(56))
G2 = PermutationGroup([Permutation(list(s)) for s in S7] + [Permutation(list(PR))])
o2 = G2.order(); print("|<W, pr>|  = 56!   ?", o2 == math.factorial(56), " = 56!/2 ?", o2 == math.factorial(56) // 2)
PSIi = pinv(PSI)
refls = set(tuple(s) for s in S7); gens = [tuple(s) for s in S7]; changed = True
while changed:
    changed = False
    for r in list(refls):
        for g in gens:
            c = tuple(comp(comp(list(g), list(r)), pinv(list(g))))
            if c not in refls: refls.add(c); changed = True
print("reflections of W(E7) on the board:", len(refls))
for k in (1, 2, 3, 9):
    Pk = list(range(56))
    for _ in range(k): Pk = comp(PSI, Pk)
    Pki = pinv(Pk)
    lin_after = sum(1 for r in refls if islin(comp(comp(Pk, list(r)), Pki)))
    print("reflections whose conjugate by Psi^%d is still linear: %d of %d" % (k, lin_after, len(refls)))

from sympy import factorint
print("|<W, pr>| =", o2, " factored:", factorint(o2), " index in S56 huge; ratio to |W|:", o2 // W.order() if o2 % W.order() == 0 else "not a multiple")
print("|<W, pr>| / |W(E8)| =", o2 / 696729600, " |<W,pr>|/|W(E7)| =", o2 / 2903040)
# orbits of <W, pr> on the 56: does pr merge the two 28-sheets... (W is transitive already); check <W,pr> orbits on pairs
G2o = G2.orbits(); print("<W,pr> orbits on 56:", sorted(len(o) for o in G2o))
# is <W, pr> = W(E7) x <something>? test whether pr normalizes W: pr s pr in W for the 7 generators
prW = all(islin(comp(comp(PR, list(s)), PR)) for s in S7)
print("pr normalizes W(E7) (pr s pr linear for all simple s):", prW)
# random sample of W: fraction whose clock-conjugate is linear
import random
random.seed(1)
hits = 0; n = 3000
for _ in range(n):
    g = list(W.random().array_form)
    if islin(comp(comp(PSI, g), PSIi)): hits += 1
print("random W elements whose Psi-conjugate is linear: %d of %d" % (hits, n))
