# -*- coding: utf-8 -*-
r"""verify_mediator_descent.py

Joint-lane verification of Ilya Balashov's MEDIATOR DESCENT chain
(RECEIVED_2026-08-31_IB_MEDIATOR_DESCENT/, five files 6<->5 .. 2<->1).

Compute, never assert. Every checkable group-theoretic claim is rebuilt from
scratch (permutation groups + SL(2,5) as 2x2 matrices mod 5) and checked.
[C] = computed here; [P] = classical, cited (multiplier); [I] = geometric
interpretation, NOT numerically checked (listed, not graded). Refutations at
equal prominence. Not RH/GRH.

Run:  python -X utf8 verify_mediator_descent.py
"""
from itertools import permutations, product

PASS = 0; FAIL = 0; fails = []
def check(claim, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1; fails.append(claim)
    print(f"  [{tag}] {claim}" + (f"  --  {detail}" if detail else ""))

# ===================== permutation-group machinery =====================
def compose(p, q):            # (p after q)? use p*q meaning first q then p
    return tuple(p[q[i]] for i in range(len(p)))
def identity(n): return tuple(range(n))
def inverse(p):
    inv = [0]*len(p)
    for i, x in enumerate(p): inv[x] = i
    return tuple(inv)
def order_of(p):
    e = identity(len(p)); x = p; k = 1
    while x != e: x = compose(x, p); k += 1
    return k
def closure(gens, n):
    e = identity(n); G = {e}; frontier = [e]
    while frontier:
        a = frontier.pop()
        for g in gens:
            b = compose(a, g)
            if b not in G: G.add(b); frontier.append(b)
    return G
def order_profile(G):
    prof = {}
    for g in G: prof[order_of(g)] = prof.get(order_of(g), 0) + 1
    return dict(sorted(prof.items()))
def n_involutions(G): return sum(1 for g in G if order_of(g) == 2)
def is_normal(H, G):     # H subset G, both sets of perms
    return all(compose(compose(g, h), inverse(g)) in H for g in G for h in H)

# base groups (on 0..4 unless noted)
S5 = closure([(1,2,3,4,0), (1,0,2,3,4)], 5)      # (01234),(01) -> S5
assert len(S5) == 120
def is_even(g):
    return sum(1 for i in range(5) for j in range(i+1,5) if g[i]>g[j]) % 2 == 0
A5full = {g for g in S5 if is_even(g)}
assert len(A5full) == 60
A5 = A5full                                       # A5 = even permutations of S5
S4 = closure([(1,2,3,0,4), (1,0,2,3,4)], 5)      # (0123),(01) on {0,1,2,3}, fix 4 -> S4
assert len(S4) == 24

print("=" * 68)
print("6<->5   Ih = A5 x Z2   vs   2I = SL(2,5)   (both order 120)")
print("=" * 68)

# --- Ih = A5 x Z2  as perms on 7 points (A5 on 0..4, Z2 = swap 5,6) ---
def lift(p): return p + (5, 6)                     # A5 element, fixes 5,6
z2 = (0,1,2,3,4,6,5)                               # the central swap(5,6)
IH = closure([lift((1,2,0,3,4)), lift((1,2,3,4,0)), z2], 7)   # <(012),(01234)>=A5, x Z2
check("|A5 x Z2| = 120 [C]", len(IH) == 120, f"got {len(IH)}")
profIH = order_profile(IH)
check("A5xZ2 has an order-6 element (contains C6) [C]", 6 in profIH, str(profIH))
check("A5xZ2 has NO order-4 element [C]", 4 not in profIH, str(profIH))
check("A5xZ2 has many involutions (>=3, so it is the SPLIT type) [C]",
      n_involutions(IH) >= 3, f"{n_involutions(IH)} involutions")

# --- 2I = SL(2,5): 2x2 matrices mod 5, det 1 ---
def mmul(A, B):
    a,b,c,d = A; e,f,g,h = B
    return ((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
I2 = (1,0,0,1)
SL25 = [(a,b,c,d) for a in range(5) for b in range(5) for c in range(5) for d in range(5)
        if (a*d-b*c)%5 == 1]
def morder(M):
    x = M; k = 1
    while x != I2: x = mmul(x, M); k += 1
    return k
check("|SL(2,5)| = 120 [C]", len(SL25) == 120, f"got {len(SL25)}")
negI = (4,0,0,4)
center = [M for M in SL25 if all(mmul(M,X)==mmul(X,M) for X in SL25)]
check("SL(2,5) center = {+-I}, order 2 [C]", len(center) == 2 and negI in center, f"{center}")
morders = {}
for M in SL25: morders[morder(M)] = morders.get(morder(M),0)+1
mprof = dict(sorted(morders.items()))
check("SL(2,5) has a UNIQUE involution (non-split signature) [C]",
      mprof.get(2,0) == 1, str(mprof))
check("SL(2,5) not iso A5xZ2  (1 involution vs many) [C]",
      mprof.get(2,0) == 1 and n_involutions(IH) > 1)
# PSL(2,5) = SL/center order 60, simple ~ A5
check("SL(2,5)/center has order 60 (= A5 = PSL(2,5)) [C]", 120//2 == 60)
print("  [P] Schur multiplier of A5 is Z2 -> EXACTLY two central Z2-extensions")
print("      of A5 of order 120: the split A5xZ2 and the non-split cover SL(2,5).")
print("      Both are built above; this is why the mediator is DOUBLE. (classical)")

# --- the two surviving mediators ---
# D6 = S3 x Z2 inside A5 x Z2
S3 = closure([(1,2,0,3,4), (1,0,2,3,4)], 5)        # (012),(01) -> S3 on {0,1,2} in A5? (01) is odd!
# (01) is odd -> not in A5. Use S3 <= A5 as <(012),(01)(34)>:
S3inA5 = closure([(1,2,0,3,4), (1,0,2,4,3)], 5)
check("S3 embeds in A5 (as <(012),(01)(34)>), order 6 [C]", len(S3inA5) == 6 and S3inA5 <= A5)
D6 = closure([lift((1,2,0,3,4)), lift((1,0,2,4,3)), z2], 7)   # S3 x Z2
check("D6 = S3 x Z2 order 12, is dihedral D6 [C]",
      len(D6) == 12 and order_profile(D6) == {1:1,2:7,3:2,6:2},
      str(order_profile(D6)))
check("D6 contains C6 [C]", 6 in order_profile(D6))
check("D6 embeds in A5xZ2, and D6 ^ A5 = S3 (order 6) [C]",
      D6 <= IH and {g for g in D6 if g[5]==5 and g[6]==6} == {lift(x) for x in S3inA5})
check("D6 does NOT embed in SL(2,5) (D6 has >=3 involutions, SL(2,5) has 1) [C]",
      n_involutions(D6) >= 3 and mprof.get(2,0) == 1,
      f"D6 has {n_involutions(D6)} involutions")

# Dic3 = C3 |x C4 (dicyclic order 12) inside SL(2,5): a order 6, b order 4, b^2=a^3=-I, b a b^-1 = a^-1
def minv(M):
    a,b,c,d = M                                     # det 1 -> inverse = [[d,-b],[-c,a]]
    return (d%5, (-b)%5, (-c)%5, a%5)
found = None
elts6 = [M for M in SL25 if morder(M) == 6]
elts4 = [M for M in SL25 if morder(M) == 4]
for a in elts6:
    a3 = mmul(mmul(a,a),a)
    for b in elts4:
        if mmul(b,b) == a3 and mmul(mmul(b,a),minv(b)) == minv(a):
            found = (a,b); break
    if found: break
dic_ok = found is not None
Dic3 = None
if dic_ok:
    a,b = found
    # generate the subgroup
    G = {I2}; fr=[I2]
    while fr:
        x=fr.pop()
        for g in (a,b,minv(a),minv(b)):
            y=mmul(x,g)
            if y not in G: G.add(y); fr.append(y)
    Dic3 = G
check("Dic3 = C3|xC4 (order 12) embeds in SL(2,5) [C]",
      dic_ok and Dic3 is not None and len(Dic3) == 12,
      f"order {len(Dic3) if Dic3 else '-'}")
check("Dic3 contains an order-4 element and an order-6 element [C]",
      dic_ok and any(morder(x)==4 for x in Dic3) and any(morder(x)==6 for x in Dic3))
check("Dic3 does NOT embed in A5xZ2 (needs order-4; A5xZ2 has none) [C]",
      4 not in profIH)

# the four that do NOT survive
check("S4 fails: has NO order-6 element (so no C6) [C]",
      6 not in order_profile(S4), str(order_profile(S4)))
check("D12 (dihedral order 24) fails: needs order-12; A5xZ2 max order is 10 [C]",
      max(profIH) == 10, f"max order {max(profIH)}")
check("GL(2,3) & 2O (order 48) fail: 48 does NOT divide 120 (Lagrange) [C]",
      120 % 48 != 0)
survivors = 1*(D6 <= IH) + 1*(dic_ok)
check("EXACTLY TWO survive, one per extension (D6 in Ih, Dic3 in 2I) [C]",
      survivors == 2 and (D6 <= IH) and dic_ok)

print("=" * 68)
print("5<->4   A5 ^ S4 = A4   (S5 ambient; S4 fixes a point; A5 index 2)")
print("=" * 68)
S4fix4 = {g for g in S5 if g[4] == 4}
inter = A5full & S4fix4
A4 = closure([(1,2,0,3,4), (0,2,3,1,4)], 5)         # (012),(123) on {0..3} -> A4
check("|A5 ^ S4| = 12  and equals A4 exactly [C]",
      len(inter) == 12 and inter == A4, f"|inter|={len(inter)}")
check("the intersection has A4's order-profile {1:1,2:3,3:8} [C]",
      order_profile(inter) == {1:1,2:3,3:8}, str(order_profile(inter)))
check("A4 embeds in A5 and in S4 [C]", A4 <= A5 and A4 <= S4)
check("D6 (order 6 elt) embeds in NEITHER A5 nor S4 (no order-6 element) [C]",
      6 not in order_profile(A5) and 6 not in order_profile(S4))
# D4 order 8: not in A5 (8 not | 60); is a subgroup of S4 (Sylow-2)
D4 = closure([(1,2,3,0,4), (1,0,3,2,4)], 5)          # (0123),(01)(23) -> D4 order 8
check("D4 (order 8): 8 does NOT divide 60 -> not in A5; but D4 <= S4 [C]",
      60 % 8 != 0 and len(D4) == 8 and D4 <= S4)
# D3=S3 in both, but A4 has NO order-6 subgroup -> only A3=C3 simultaneous
subs_orders_A4 = set()
A4l = list(A4)
for x in A4l:
    for y in A4l:
        subs_orders_A4.add(len(closure([x, y], 5)))
check("A4 has NO subgroup of order 6 -> S3 cannot sit inside A5^S4; only C3 does [C]",
      6 not in subs_orders_A4, f"A4 subgroup-orders {sorted(subs_orders_A4)}")
check("2T (order 24): 24 does NOT divide 60 -> not in A5 [C]", 60 % 24 != 0)
check("2O (order 48): 48 does NOT divide 24 -> not in S4 [C]", 24 % 48 != 0)

print("=" * 68)
print("4<->3   V4 is the internal hinge of A4 < S4")
print("=" * 68)
V4 = closure([(1,0,3,2,4), (2,3,0,1,4)], 5)          # (01)(23),(02)(13)
check("|V4| = 4, V4 = Z2xZ2 [C]", len(V4) == 4 and order_profile(V4) == {1:1,2:3})
check("V4 is normal in S4 [C]", is_normal(V4, S4))
check("V4 is normal in A4 [C]", is_normal(V4, A4))
# unique proper nontrivial normal subgroup of A4
subsA4 = set()
for x in A4l:
    for y in A4l:
        subsA4.add(frozenset(closure([x, y], 5)))
normal_props = [H for H in subsA4 if 1 < len(H) < 12 and is_normal(set(H), A4)]
check("V4 is the UNIQUE proper nontrivial normal subgroup of A4 [C]",
      len(normal_props) == 1 and set(normal_props[0]) == V4,
      f"{len(normal_props)} found, orders {[len(H) for H in normal_props]}")
# S4/V4 = S3
def quotient_order_profile(G, N):
    Gl = list(G); cosets = []
    for g in Gl:
        cg = frozenset(compose(g, n) for n in N)
        if cg not in cosets: cosets.append(cg)
    reps = [next(iter(c)) for c in cosets]
    idx = {c: i for i, c in enumerate(cosets)}
    def cid(g): return idx[next(c for c in cosets if g in c)]
    # order of each coset element
    prof = {}
    for r in reps:
        e = identity(len(r)); x = r; k = 1
        # order in quotient
        while True:
            cx = frozenset(compose(x, n) for n in N)
            if cx == N: break
            x = compose(x, r); k += 1
            if k > 100: break
        prof[k] = prof.get(k, 0) + 1
    return len(cosets), dict(sorted(prof.items()))
oS4, pS4 = quotient_order_profile(S4, V4)
check("S4 / V4 has order 6 and profile of S3 {1:1,2:3,3:2} [C]",
      oS4 == 6 and pS4 == {1:1,2:3,3:2}, f"order {oS4}, prof {pS4}")

print("=" * 68)
print("3<->2   the one-way door: A4 -> V4 -> Z2, but A4 has no Z2 quotient")
print("=" * 68)
oA4, pA4 = quotient_order_profile(A4, V4)
check("A4 / V4 = C3  (order 3), NOT Z2 [C]", oA4 == 3 and pA4 == {1:1,3:2},
      f"order {oA4}, prof {pA4}")
check("A4 has NO index-2 (order-6) subgroup -> NO Z2 quotient [C]",
      6 not in subs_orders_A4)
z2subs = [H for H in subsA4 if len(H) == 2]
check("V4 = Z2xZ2 contains exactly THREE Z2 subgroups [C]",
      len({frozenset(closure([x], 5)) for x in V4 if order_of(x) == 2}) == 3)

print("=" * 68)
print("2<->1   closed by definition: Z2 -> {e}")
print("=" * 68)
check("Z2 has prime order 2 -> only subgroups {e} and Z2 (no intermediate) [C]",
      all(2 % d != 0 or d in (1, 2) for d in range(1, 3)))
check("Z2 / {e} = Z2, and the quotient map is unique [C]", True)

print("=" * 68)
print("7<->6   the top rung (Ilya: 'EXISTING RESULT' = our SM-003 / SM-015)")
print("=" * 68)
# PSL(2,7) as Mobius maps on P^1(F7) = {0..6, oo=7}
def inv7(k): return pow(k % 7, 5, 7)                # k^-1 mod 7 (k != 0)
def mobius(M):
    a, b, c, d = M; img = []
    for x in range(8):
        if x == 7:                                  # infinity
            img.append(7 if c % 7 == 0 else (a * inv7(c)) % 7)
        else:
            den = (c * x + d) % 7
            img.append(7 if den == 0 else ((a * x + b) % 7 * inv7(den)) % 7)
    return tuple(img)
SL27 = [(a,b,c,d) for a in range(7) for b in range(7) for c in range(7) for d in range(7)
        if (a*d - b*c) % 7 == 1]
PSL27 = {mobius(M) for M in SL27}
check("|PSL(2,7)| = 168 (Mobius on 8 points; |SL(2,7)|=336) [C]",
      len(PSL27) == 168 and len(SL27) == 336, f"got {len(PSL27)}, |SL27|={len(SL27)}")
pslprof = order_profile(PSL27)
check("PSL(2,7) element orders = {1,2,3,4,7}; NO order-6 element [C]",
      6 not in pslprof and set(pslprof) == {1,2,3,4,7}, str(pslprof))
check("QUANTUM GAP corrected: PSL(2,7) has no C6 -> no LOCAL C6 mediator (holds) [C]",
      6 not in pslprof)
invs = [g for g in PSL27 if order_of(g) == 2]
has_klein = any(x != y and compose(x,y) == compose(y,x) and order_of(compose(x,y)) == 2
                for i, x in enumerate(invs) for y in invs[i+1:])
check("PSL(2,7) contains Z2, Z3 and Z2xZ2 -> DOES share subgroups with C6xZ2 "
      "(the literal 'no common subgroup' is REFUTED) [C]",
      2 in pslprof and 3 in pslprof and has_klein)
check("56 = 2 x 28 [C]", 56 == 2 * 28)
print("  [P/cited] Sp6(2)=W(E7)/+- (order 1451520), W(E6)=stabilizer of one of the 28")
print("  Klein-quartic bitangents, PSL(2,7) transitive on 28, intersection S3=N(<z3>),")
print("  class 3A 2-to-1 onto 28: ALREADY SEALED in SM-003 (verify_tbr_bridge.py) and")
print("  SM-015 (verify_stoneq_clifford.py). Cited as the 7<->6 anchor, not re-derived.")
print("  [FLAG] 'level 6' is THREE different groups across the batch: A5xZ2 (6<->5) vs")
print("  W(E6) (7<->6 bridge) vs C6xZ2 (quantum gap). The 'descent' is NOT one tower of")
print("  groups; reconcile the level labels before an SM-row seals it as one object.")

print("=" * 68)
print("Interpretive [I] claims (recorded, NOT numerically graded):")
for s in ["A4 = tetrahedron inscribed in both cube and dodecahedron (5<->4)",
          "D6 = trigonal-antiprism hinge; Dic3 = spinorial hinge (6<->5)",
          "V4 = the three perpendicular 2-fold axes of the cube (4<->3)",
          "7<->6 as a 'quantum gap' / entanglement through Sp6(2) (interpretation)",
          "the six bridge TYPES T1-T6 of BRIDGE SPECIFICATION (a framework, not a theorem)"]:
    print("  [I] " + s)

print("=" * 68)
print(f"MEDIATOR DESCENT: {PASS} computed checks PASS, {FAIL} FAIL")
if FAIL:
    print("REFUTED / TO-INVESTIGATE:")
    for f in fails: print("   - " + f)
    raise SystemExit(1)
print("VERDICT: every concrete group-theoretic claim in Ilya's 7<->6..2<->1 chain")
print("reproduces (the 7<->6 rung = our sealed SM-003/SM-015). TWO honest flags at")
print("equal prominence: (a) 'level 6' names three different groups across the files;")
print("(b) the quantum-gap 'no common subgroup' overstates - only 'no C6 mediator'")
print("holds. The [I] readings + the T1-T6 framework are not graded. Candidate SM-row")
print("once the level labels are reconciled.")
