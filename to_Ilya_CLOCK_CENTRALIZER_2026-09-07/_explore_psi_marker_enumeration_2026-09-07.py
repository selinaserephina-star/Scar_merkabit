"""Free exploration (NOT sealed) -- IB's REQUEST of 2026-09-06 (received 2026-09-07):
'Please provide the canonical pair (a,b) ... and test Psi C2 Psi^-1 = C2 for each of the three C2's.'
House answer by enumeration, no choice: every C2 he can build lies in a PSL(2,7) inside W(E7) acting on
the 56 (SM-013: the bridge class; W(E7) = 2 x Sp6(2), the perfect part lifts uniquely).  So the question
'is some C2 = <z> fixed by Psi' is 'does any involution z of W(E7) commute with Psi'.  We enumerate the
centralizer of Psi in S56 (Psi has cycle type [18,18,18,2]: |C| = 18^3 * 3! * 2 = 69984), take its
involutions (231), and test each for W(E7)-membership by the pair-type test (score = 1  <=>  linear).
Then the bridge involution class: one bridge PSL(2,7) built by (2,3,7) search inside W(E7); its 21
involutions' cycle type on 56 and trace on the 7-dim rep, to compare with whatever survives.
Board machinery VERBATIM from verify_stone_af_three_eighteens.py (= verify_stone_ac_parity_rule.py 55-108).
"""
import itertools, json, random, time, math
from collections import Counter
import numpy as np
random.seed(20260907)
T0 = time.time()
# ---------------------------------------------------------------- VERBATIM board setup
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=8):
    if signs.count(-1) % 2 == 0: roots.append(tuple(signs))
ridx = {r: k for k, r in enumerate(roots)}
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
SIMPLE = [(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0),(0,-2,2,0,0,0,0,0),
          (0,0,-2,2,0,0,0,0),(0,0,0,-2,2,0,0,0),(0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0)]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
Gm = np.array(GRAM, dtype=np.int64); Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
coords = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64); coords.append([int(x) for x in Ginv @ d])
rmask = [int(sum((coords[k][i] & 1) << i for i in range(8))) for k in range(240)]
qvals = []
for m in range(256):
    cv = np.array([(m >> i) & 1 for i in range(8)], dtype=np.int64); qvals.append(((int(cv @ Gm @ cv)) // 2) % 2)
ALPHA_R = SIMPLE[0]; ALPHA = rmask[ridx[ALPHA_R]]
D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]; vidx = {v: k for k, v in enumerate(verts)}
PSI, IOTA = D["PSI"], D["IOTA"]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]; B56 = [r for r in roots if dot4(r, ALPHA_R) == 1]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi[i]] for i in range(7)]
root_of = {}
for r in B56: root_of[vidx[tuple(dot4(r, b) for b in BETA)]] = r
assert len(root_of) == 56
mask = {k: rmask[ridx[root_of[k]]] for k in range(56)}
def ptype(k, l):
    s = mask[k] ^ mask[l]
    if s == ALPHA: return "v"
    return "P" if qvals[s] == 1 else "S"
W2 = {k: tuple(2*x - a for x, a in zip(root_of[k], ALPHA_R)) for k in range(56)}
PAIRS = [(k, l) for k in range(56) for l in range(k + 1, 56)]
def compose(p, q): return [p[q[k]] for k in range(56)]
def score(p): return sum(1 for k, l in PAIRS if ptype(p[k], p[l]) == ptype(k, l)) / len(PAIRS)
def refl(r, b): c = dot4(r, b); return tuple(x - c * y for x, y in zip(r, b))
vert_of_root = {root_of[k]: k for k in range(56)}
S7 = [[vert_of_root[refl(root_of[k], b)] for k in range(56)] for b in BETA]
# ---------------------------------------------------------------- helpers
def cyc(p):
    seen = set(); c = []
    for k in range(len(p)):
        if k in seen: continue
        o = 0; x = k
        while x not in seen: seen.add(x); o += 1; x = p[x]
        c.append(o)
    return tuple(sorted(c, reverse=True))
def porder(p):
    x = list(range(56)); n = 0
    while True:
        x = compose(p, x); n += 1
        if x == list(range(56)): return n
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
IP = {(k, l): sum(a*b for a, b in zip(W2[k], W2[l])) for k in range(56) for l in range(56)}
NORM = IP[(0, 0)]
def trace7(p):  # trace of the linear action on the 7-dim rep (weights span; Gram sum is W-invariant => c.I)
    return 7 * sum(IP[(p[k], k)] for k in range(56)) / (56 * NORM)
def islinear(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
assert islinear(IOTA) and abs(trace7(IOTA) + 7) < 1e-9 and all(islinear(s) for s in S7) and all(abs(trace7(s) - 5) < 1e-9 for s in S7)
print("board ok: iota linear, trace -7; the 7 simple reflections linear, trace 5   [t=%.1fs]" % (time.time() - T0))

# ---------------------------------------------------------------- 1. the centralizer of Psi in S56 and its involutions
cycles = []
seen = set()
for k in range(56):
    if k in seen: continue
    c = []; x = k
    while x not in seen: seen.add(x); c.append(x); x = PSI[x]
    cycles.append(c)
big = [c for c in cycles if len(c) == 18]; two = [c for c in cycles if len(c) == 2]
assert len(big) == 3 and len(two) == 1
cent_invs = []
for sigma in itertools.permutations(range(3)):
    for shifts in itertools.product(range(18), repeat=3):
        for eps in (0, 1):
            p = [None] * 56
            for i in range(3):
                for j in range(18):
                    p[big[i][j]] = big[sigma[i]][(j + shifts[i]) % 18]
            p[two[0][0]] = two[0][eps]; p[two[0][1]] = two[0][1 - eps]
            if p == list(range(56)): continue
            if compose(p, p) == list(range(56)): cent_invs.append(p)
n_cent = 6 * 18**3 * 2
assert all(compose(p, PSI) == compose(PSI, p) for p in cent_invs)
print("centralizer of Psi in S56: order %d; involutions in it: %d (expected 15 + 3*72 = 231)" % (n_cent, len(cent_invs)))
lin = [p for p in cent_invs if islinear(p)]
print("involutions commuting with Psi that lie in W(E7): %d" % len(lin))
for p in lin:
    print("   cycle type", cyc(p), " fixed points", sum(1 for k in range(56) if p[k] == k), " trace7", trace7(p),
          " = iota?", p == IOTA, " commutes with iota?", compose(p, IOTA) == compose(IOTA, p))
# near misses, for the record
best = max(cent_invs, key=score)
print("best pair-type agreement among the 231 (1.0 = linear): %.4f" % score(best))
P9 = PSI
for _ in range(8): P9 = compose(PSI, P9)
print("Psi^9: involution", compose(P9, P9) == list(range(56)), " linear", islinear(P9), " score %.4f" % score(P9),
      " iota*Psi^9 linear", islinear(compose(IOTA, P9)), " score %.4f" % score(compose(IOTA, P9)))

# ---------------------------------------------------------------- 2. one bridge PSL(2,7) inside W(E7) on the 56, by (2,3,7) search
def rand_elt(n=40):
    p = list(range(56))
    for _ in range(n): p = compose(random.choice(S7), p)
    return p
def closure(gens, cap=200):
    idp = list(range(56)); seen = {tuple(idp)}; frontier = [idp]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = compose(s, g)
                t = tuple(h)
                if t not in seen:
                    seen.add(t); nxt.append(h)
                    if len(seen) > cap: return None
        frontier = nxt
    return [list(t) for t in seen]
ANTI = {k: IOTA[k] for k in range(56)}
def pairs_orbits(H):  # orbits of H on the 28 antipodal pairs
    reps = {}
    pairs = [frozenset((k, IOTA[k])) for k in range(56)]
    pairs = list({p for p in pairs}); pidx = {p: i for i, p in enumerate(pairs)}
    parent = list(range(28))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for h in H:
        for p in pairs:
            q = frozenset(h[k] for k in p)
            a, b = find(pidx[p]), find(pidx[q])
            if a != b: parent[a] = b
    return sorted(Counter(find(i) for i in range(28)).values(), reverse=True)
# 1b. the WHOLE centralizer of Psi in S56 against W(E7)
n_lin_all = 0; orders_lin = Counter()
for sigma in itertools.permutations(range(3)):
    for shifts in itertools.product(range(18), repeat=3):
        for eps in (0, 1):
            p = [None] * 56
            for i in range(3):
                for j in range(18):
                    p[big[i][j]] = big[sigma[i]][(j + shifts[i]) % 18]
            p[two[0][0]] = two[0][eps]; p[two[0][1]] = two[0][1 - eps]
            if islinear(p):
                n_lin_all += 1; orders_lin[porder(p)] += 1
print("ALL %d elements of C_S56(Psi) tested: %d lie in W(E7), by order %s   [t=%.1fs]" % (n_cent, n_lin_all, dict(orders_lin), time.time() - T0))

# targeted sampling: SM-013 gives the bridge PSL(2,7)'s permutation character on the 56 as 2(chi1+2chi6+chi7+chi8),
# so its involutions fix 2(1+4-1+0) = 8 points (type 2^24 1^8) and its order-3 elements fix 2(1+0+1-1) = 2 (type 3^18 1^2)
T2 = tuple([2]*24 + [1]*8); T3 = tuple([3]*18 + [1]*2)
invs, thr = [], []; seen_types = Counter(); budget = 60000
for _ in range(budget):
    g = rand_elt(30); ct = cyc(g)
    if ct == T2 and g not in invs: invs.append(g)
    elif ct == T3 and g not in thr: thr.append(g)
    if ct[0] == 2 and porder(g) == 2: seen_types[("inv", ct)] += 1
print("sampled %d elements of W(E7): %d involutions of type 2^24 1^8, %d order-3 of type 3^18 1^2   [t=%.1fs]" % (budget, len(invs), len(thr), time.time() - T0))
print("   involution cycle types seen (fixed points -> count):", sorted(((56 - 2*c.count(2)), n) for c, n in ((c, n) for (_, c), n in seen_types.items())))
found = None
tried = 0
for a in invs:
    for b in thr:
        ab = compose(a, b)
        if porder(ab) != 7: continue
        tried += 1
        H = closure([a, b], cap=170)
        if H is None or len(H) != 168: continue
        orb = pairs_orbits(H)
        if orb == [28]:
            found = (a, b, H); break
    if found: break
print("(2,3,7) pairs with |ab| = 7 tried: %d; bridge copy found: %s   [t=%.1fs]" % (tried, found is not None, time.time() - T0))
if found:
    a, b, H = found
    Hinv = [h for h in H if h != list(range(56)) and compose(h, h) == list(range(56))]
    print("bridge PSL(2,7) on the 56: order %d, transitive on the 28 pairs, %d involutions" % (len(H), len(Hinv)))
    types = Counter((cyc(h), round(trace7(h), 6)) for h in Hinv)
    print("   its involutions: (cycle type on 56, trace on 7):", dict(types))
    # do any of them commute with Psi?  (copy-dependent; the class answer above is the universal one)
    print("   involutions of THIS copy commuting with Psi:", sum(1 for h in Hinv if compose(h, PSI) == compose(PSI, h)))
    # for the record: which C2's of this copy are NORMALIZED by Psi (Psi z Psi^-1 = z is the same as commuting for an involution)
    # class of the bridge involutions among W(E7) involutions with the same trace: fixed-point count on 56
    print("   compare: linear involutions commuting with Psi (above) have (cycle type, trace7) =",
          [(cyc(p), round(trace7(p), 6)) for p in lin])
print("done [t=%.1fs]" % (time.time() - T0))
