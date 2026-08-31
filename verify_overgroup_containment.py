# -*- coding: utf-8 -*-
r"""verify_overgroup_containment.py -- THE CONTAINMENT RUN (joint target).

Both parties agreed (2026-08-31): the exact overgroup of the full 7->1 descent
and BOTH shadows.  Confirmed reading: the two shadows are the two towers --
quotient shadow = Sp6(2), cover shadow = W(E7), the +- centre as the hinge.
This run tests COMPUTATIONALLY what W(E7) does and does not contain.

Towers under test:
  Tower A (spine):  PSL(2,7) -> C6xZ2 -> A5 -> S4 -> A4 -> Z2 -> 1
  Tower B (covers): SL(2,7), SL(2,5)=2I, SL(2,3)=2T, GL(2,3)=2.S4, 2O,
                    split covers Ih=A5xZ2 / Th=A4xZ2, W(E6)<Sp6(2), PGL(2,7)

ROUTE (checks 1-8):
  1. W(E7) on the 56 weights, order 2903040, -1 central.
  2. SPLITNESS: W+ = even-word subgroup, |W+| = 1451520, -1 NOT in W+,
     hence W(E7) = <-1> x W+ = Z2 x Sp6(2), a SPLIT direct product.
  3. STRUCTURE LEMMA [P] for subgroups of Z2 x S, verified on examples.
     Consequence: a non-split central Z2-cover (unique involution) can sit in
     W(E7) only via an embedding into Sp6(2), never over the +- hinge.
  4. Full element-order census of Sp6(2) (exhaustive, all 1451520 elements).
     14 absent  =>  SL(2,7) not in Sp6(2)  =>  (lemma) not in W(E7) at all.
  5. Exhaustive presentation searches in Sp6(2) for 2I, 2T, 2O over every
     involution class; GL(2,3) by normalizer extension over every SL(2,3)
     copy (center-normalized).
  6. Spine containment in Sp6(2): C6xZ2 (exhaustive centralizer scan),
     A5, S4, A4 (constructive witnesses); PSL(2,7) cited (SM-003/SM-015).
  7. Split covers over the hinge: <-1> x A5 = Ih, <-1> x A4 = Th inside
     W(E7), matching sealed SM-013 (PSL(2,7) preimage = 2 x L2(7)).
  8. Verdict.

DISCIPLINE: compute, never assert; every exhaustive claim says over what.
Cache: _overgroup_cache/ (element enumeration + order census, resumable).

Run:  python -X utf8 verify_overgroup_containment.py
"""
import json, os, time, random
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
PASS = 0; FAIL = 0; FAILED = []
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:
        FAIL += 1; FAILED.append(tag)
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""),
          flush=True)

def banner(t):
    print("\n" + "-" * 78); print(t); print("-" * 78, flush=True)

def lcm(a, b): return a * b // gcd(a, b)

CACHE = "_overgroup_cache"
os.makedirs(CACHE, exist_ok=True)
random.seed(56728)

print("=" * 78)
print("THE CONTAINMENT RUN -- what W(E7) = 2 x Sp6(2) contains of the two towers")
print("=" * 78)
print(f"[t={time.time()-T0:6.1f}s] start")

# ======================================================================
# shared utilities (reused from sealed verify_stonef_b_dq1 / verify_stone_r)
# ======================================================================
D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]
idx = {v: k for k, v in enumerate(verts)}
IOTA, FRAME = D["IOTA"], D["FRAME"]
N = 56
C7 = [[ 2, 0,-1, 0, 0, 0, 0],
      [ 0, 2, 0,-1, 0, 0, 0],
      [-1, 0, 2,-1, 0, 0, 0],
      [ 0,-1,-1, 2,-1, 0, 0],
      [ 0, 0, 0,-1, 2,-1, 0],
      [ 0, 0, 0, 0,-1, 2,-1],
      [ 0, 0, 0, 0, 0,-1, 2]]
S = []
for i in range(7):
    perm = []
    for k in range(N):
        w = verts[k]
        img = tuple(w[j] - w[i] * C7[i][j] for j in range(7))
        perm.append(idx[img])
    S.append(tuple(perm))

def mul(a, b): return tuple(a[b[k]] for k in range(N))
def inv(a):
    r = [0] * N
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
E56 = tuple(range(N))
def perm_pow(p, e):
    x = E56 if len(p) == N else tuple(range(len(p)))
    for _ in range(e): x = tuple(x[p[k]] for k in range(len(p)))
    return x
def pord(p):
    n = len(p); e = tuple(range(n)); x = p; k = 1
    while x != e:
        x = tuple(x[p[i]] for i in range(n)); k += 1
    return k
def mul28(a, b): return tuple(a[b[k]] for k in range(28))
def inv28(a):
    r = [0] * 28
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
E28 = tuple(range(28))
def to28(p56):
    out = [0] * 28
    for x in range(N): out[FRAME[x]] = FRAME[p56[x]]
    return tuple(out)
def closure(gens, cap=100000):
    n = len(gens[0]); e = tuple(range(n))
    G = {e}; fr = [e]
    while fr:
        a = fr.pop()
        for g in gens:
            b = tuple(a[g[i]] for i in range(n))
            if b not in G:
                G.add(b); fr.append(b)
                if len(G) > cap: return G
    return G
def profile_of(G):
    return dict(sorted(Counter(pord(g) for g in G).items()))

# BSGS with membership test (verbatim algorithm from sealed verify_stone_r)
def make_bsgs_full(gen_list, deg):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    base = []
    for g in strong:
        if all(g[b] == b for b in base):
            base.append(next(i for i in range(deg) if g[i] != i))
    lvl = [[g for g in strong if all(g[b] == b for b in base[:i])]
           for i in range(len(base))]
    transv = [None] * len(base)
    def rebuild(i):
        b = base[i]; T = {b: E}; q = [b]
        while q:
            x = q.pop(0)
            for g in lvl[i]:
                y = g[x]
                if y not in T:
                    T[y] = mulD(g, T[x]); q.append(y)
        transv[i] = T
    for i in range(len(base)): rebuild(i)
    def strip_from(g, start):
        h = g
        for i in range(start, len(base)):
            x = h[base[i]]
            if x not in transv[i]: return h, i
            h = mulD(invD(transv[i][x]), h)
        return h, len(base)
    i = len(base) - 1
    while i >= 0:
        clean = True
        for x in list(transv[i].keys()):
            for g in lvl[i]:
                sg = mulD(invD(transv[i][g[x]]), mulD(g, transv[i][x]))
                if sg == E: continue
                h, j = strip_from(sg, i + 1)
                if h != E:
                    clean = False
                    if j == len(base):
                        base.append(next(p for p in range(deg)
                                         if h[p] != p))
                        lvl.append([]); transv.append(None)
                    for k2 in range(i + 1, j + 1):
                        lvl[k2].append(h); rebuild(k2)
                    i = j
                    break
            if not clean: break
        if clean: i -= 1
    o = 1
    for T in transv: o *= len(T)
    def is_member(g):
        h, _ = strip_from(g, 0)
        return h == E
    return o, is_member, transv

# small matrix groups mod p (reused from sealed verify_tower_b)
def mmul(A, B, p):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e+b*g) % p, (a*f+b*h) % p, (c*e+d*g) % p, (c*f+d*h) % p)
def mdet(M, p):
    a, b, c, d = M; return (a*d - b*c) % p
def mord(M, p):
    I = (1, 0, 0, 1); x = M; k = 1
    while x != I: x = mmul(x, M, p); k += 1
    return k
def SL2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if mdet((a, b, c, d), p) == 1]
def GL2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if mdet((a, b, c, d), p) != 0]
def mat_profile(G, p): return dict(sorted(Counter(mord(M, p) for M in G).items()))
def mat_closure(gens, mulfn, cap=100000):
    Ident = gens[0]
    # find identity by powering; simpler: closure from gens
    G = set(gens); fr = list(gens)
    while fr:
        a = fr.pop()
        for g in gens:
            b = mulfn(a, g)
            if b not in G:
                G.add(b); fr.append(b)
                if len(G) > cap: return G
    return G

# F9 = F3[i], i^2 = -1 encoded 0..8 as a + 3b  <->  a + b*i
def f9mul(u, v):
    a, b = u % 3, u // 3; c, d = v % 3, v // 3
    return ((a*c - b*d) % 3) + 3*((a*d + b*c) % 3)
def f9add(u, v):
    a, b = u % 3, u // 3; c, d = v % 3, v // 3
    return ((a + c) % 3) + 3*((b + d) % 3)
def mmul9(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (f9add(f9mul(a, e), f9mul(b, g)), f9add(f9mul(a, f), f9mul(b, h)),
            f9add(f9mul(c, e), f9mul(d, g)), f9add(f9mul(c, f), f9mul(d, h)))
I9 = (1, 0, 0, 1); mI9 = (2, 0, 0, 2)
def mord9(M):
    x = M; k = 1
    while x != I9: x = mmul9(x, M); k += 1
    return k

# ======================================================================
banner("CHECK 1 -- W(E7) on the 56 weights; -1 central")
# ======================================================================
check("1a", "the 7 simple reflections are involutions permuting the 56 weights",
      all(all(s[s[k]] == k for k in range(N)) for s in S))
oW, memW, _ = make_bsgs_full(S, N)
check("1b", "|<s1..s7>| = 2903040 = |W(E7)| (BSGS on the 56)", oW == 2903040,
      f"order {oW}")
anti = tuple(idx[tuple(-x for x in verts[k])] for k in range(N))
check("1c", "the antipode iota = -1 equals the data's IOTA, is a fixed-point-"
      "free involution, and commutes with every reflection (central)",
      list(anti) == IOTA and all(anti[k] != k for k in range(N))
      and mul(anti, anti) == E56
      and all(mul(s, anti) == mul(anti, s) for s in S))
print(f"[t={time.time()-T0:6.1f}s] check 1 done")

# ======================================================================
banner("CHECK 2 -- SPLITNESS: W(E7) = <-1> x W+ = Z2 x Sp6(2), SPLIT")
# ======================================================================
TW = [mul(S[0], S[i]) for i in range(1, 7)]        # even-word generators
oWp, memWp, _ = make_bsgs_full(TW, N)
check("2a", "W+ = <s1s2,...,s1s7> (the even words) has order 1451520 "
      "= |W(E7)|/2", oWp == 1451520, f"order {oWp}")
check("2b", "-1 is NOT in W+ (BSGS membership strip)", not memWp(anti))
S28 = [to28(s) for s in S]
o28, mem28, TR28 = make_bsgs_full(S28, 28)
check("2c", "the 28-pair action of W(E7) has image of order 1451520 = Sp6(2); "
      "kernel has order 2 and contains {1, -1}, so ker = {+-1}",
      o28 == 1451520 and oW // o28 == 2 and to28(anti) == E28)
TW28 = [to28(t) for t in TW]
oWp28, _, _ = make_bsgs_full(TW28, 28)
oFull, _, _ = make_bsgs_full(TW + [anti], N)
check("2d", "pi restricted to W+ is INJECTIVE (W+ ^ ker pi = W+ ^ {+-1} = 1 "
      "by 2b) and ONTO (image order 1451520): W+ = Sp6(2); and <W+, -1> "
      "= all of W(E7).  CONCLUSION: W(E7) = <-1> x W+ = Z2 x Sp6(2), a "
      "SPLIT direct product -- the load-bearing structural fact",
      oWp28 == 1451520 and oFull == 2903040)
print(f"[t={time.time()-T0:6.1f}s] check 2 done")

# shadow BSGS: chain for Sp6(2) on 28 points whose transversal elements carry
# a W(E7)-preimage on the 56 -- used to LIFT any Sp6(2) element into W+.
def make_shadow_bsgs(gen_pairs):
    d1 = 28
    Ep = (E28, E56)
    def mulP(a, b):
        return (tuple(a[0][b[0][k]] for k in range(28)),
                tuple(a[1][b[1][k]] for k in range(56)))
    def invP(a):
        r1 = [0]*28; r2 = [0]*56
        for i, x in enumerate(a[0]): r1[x] = i
        for i, x in enumerate(a[1]): r2[x] = i
        return (tuple(r1), tuple(r2))
    def is_e(a): return a[0] == E28
    strong = [g for g in gen_pairs if not is_e(g)]
    base = []
    for g in strong:
        if all(g[0][b] == b for b in base):
            base.append(next(i for i in range(d1) if g[0][i] != i))
    lvl = [[g for g in strong if all(g[0][b] == b for b in base[:i])]
           for i in range(len(base))]
    transv = [None] * len(base)
    def rebuild(i):
        b = base[i]; T = {b: Ep}; q = [b]
        while q:
            x = q.pop(0)
            for g in lvl[i]:
                y = g[0][x]
                if y not in T:
                    T[y] = mulP(g, T[x]); q.append(y)
        transv[i] = T
    for i in range(len(base)): rebuild(i)
    def strip_from(g, start):
        h = g
        for i in range(start, len(base)):
            x = h[0][base[i]]
            if x not in transv[i]: return h, i
            h = mulP(invP(transv[i][x]), h)
        return h, len(base)
    i = len(base) - 1
    while i >= 0:
        clean = True
        for x in list(transv[i].keys()):
            for g in lvl[i]:
                sg = mulP(invP(transv[i][g[0][x]]), mulP(g, transv[i][x]))
                if is_e(sg): continue
                h, j = strip_from(sg, i + 1)
                if not is_e(h):
                    clean = False
                    if j == len(base):
                        base.append(next(p for p in range(d1)
                                         if h[0][p] != p))
                        lvl.append([]); transv.append(None)
                    for k2 in range(i + 1, j + 1):
                        lvl[k2].append(h); rebuild(k2)
                    i = j
                    break
            if not clean: break
        if clean: i -= 1
    o = 1
    for T in transv: o *= len(T)
    return o, base, transv, mulP

oSh, SHbase, SHtransv, SHmul = make_shadow_bsgs(
    [(S28[i], S[i]) for i in range(7)])
def lift_to_Wplus(b28):
    """explicit preimage in W+ of an Sp6(2) element given on the 28 pairs"""
    r = (E28, E56); h = b28
    for i, bpt in enumerate(SHbase):
        x = h[bpt]
        if x not in SHtransv[i]: return None
        t = SHtransv[i][x]
        r = SHmul(r, t)
        h = mul28(inv28(t[0]), h)
    if h != E28: return None
    u = r[1]
    if to28(u) != b28: return None
    if not memWp(u): u = mul(anti, u)
    if not (memWp(u) and to28(u) == b28): return None
    return u
lift_ok = all(lift_to_Wplus(S28[i]) is not None and
              to28(lift_to_Wplus(S28[i])) == S28[i] for i in range(7))
check("2e", "shadow-BSGS lift Sp6(2) -> W+ verified on the 7 generator "
      "images (round trip pi(lift(x)) = x, lift in W+)",
      oSh == 1451520 and lift_ok)
print(f"[t={time.time()-T0:6.1f}s] check 2e done (shadow chain)")

# ======================================================================
banner("CHECK 3 -- STRUCTURE LEMMA [P] for subgroups of Z2 x S, + examples")
# ======================================================================
print("""[P] LEMMA. Let G = <z> x S with z central of order 2, pi: G -> S the
    projection (ker pi = <z> x 1).  For any subgroup H <= G:
      (i)  if z in H:   H = <z> x (H ^ S'), split, where S' = 1 x S; and
           H ^ S' maps isomorphically onto pi(H);
      (ii) if z not in H:  pi is injective on H, so H embeds into S.
    Proof: (ii) ker(pi|H) = H ^ <z> = 1.  (i) for h in H, either h in S'
    or zh in S'; so H = (H^S') u z(H^S').  [one-line, standard]
    CONSEQUENCE for the hinge: a NON-SPLIT central Z2-extension (unique
    involution = its centre) inside W(E7) = <-1> x W+ can never contain -1:
    if -1 in H then H = <-1> x B with B = H/<-1> of even order, so B brings
    a second involution -- contradiction with uniqueness.  Hence any Schur
    cover 2.X (X in {PSL(2,7), A5, A4, S4-nonsplit}) sits in W(E7) ONLY via
    an embedding into W+ = Sp6(2), and then its central involution is a
    NON-central involution of W(E7).  The +- hinge reading is IMPOSSIBLE
    for non-split covers.""")
n_ex = 0; n_ok = 0
for trial in range(24):
    w = E56
    for _ in range(random.randrange(20, 60)):
        w = mul(S[random.randrange(7)], w)
    og = pord(w)
    H = [E56]; x = w
    while x != E56: H.append(x); x = mul(x, w)
    for Hx in (H, sorted(set(H) | {mul(anti, h) for h in H})):
        n_ex += 1
        has = anti in Hx
        B = [h for h in Hx if memWp(h)]
        if has:
            ok = (2 * len(B) == len(Hx)
                  and set(Hx) == set(B) | {mul(anti, b) for b in B}
                  and len({to28(b) for b in B}) == len(B))
        else:
            ok = len({to28(h) for h in Hx}) == len(Hx)
        if ok: n_ok += 1
check("3a", "lemma verified on 48 example subgroups (24 random cyclic H and "
      "their <-1>-extensions): the (i)/(ii) dichotomy holds in every case",
      n_ex == 48 and n_ok == 48, f"{n_ok}/{n_ex} conform")
print(f"[t={time.time()-T0:6.1f}s] check 3 done")

# ======================================================================
banner("CHECK 4 -- exhaustive element-order census of Sp6(2); the order-14 bar")
# ======================================================================
EN_f = os.path.join(CACHE, "sp62_elements.npy")
ORD_f = os.path.join(CACHE, "sp62_orders.npy")
if os.path.exists(EN_f) and os.path.exists(ORD_f):
    EN = np.load(EN_f); ORDv = np.load(ORD_f)
    print(f"  [cache] loaded enumeration + census from {CACHE}/")
else:
    L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
         for T in TR28]
    EN = L[-1]
    for j in range(len(L) - 2, -1, -1):
        EN = np.concatenate([L[j][i][EN] for i in range(L[j].shape[0])])
    ORDv = None
Nel = EN.shape[0]
ID28 = np.arange(28, dtype=np.uint8)
def compose_rows(A, B):          # rowwise a o b
    return np.take_along_axis(A, B, axis=1)
# powers needed later regardless of cache
P = EN.copy(); Pk = {}
need_ord = ORDv is None
if ORDv is None:
    ORDv = np.zeros(Nel, dtype=np.uint8)
k = 1
while True:
    if need_ord:
        m = (P == ID28).all(axis=1) & (ORDv == 0)
        ORDv[m] = k
    if k in (3, 4, 5): Pk[k] = P.copy()
    done_ord = (not need_ord) or not (ORDv == 0).any()
    if k >= 5 and done_ord: break
    if k > 64: break
    P = compose_rows(P, EN); k += 1
del P
if not os.path.exists(EN_f): np.save(EN_f, EN)
if not os.path.exists(ORD_f): np.save(ORD_f, ORDv)
check("4a", "the BSGS transversal products enumerate 1451520 DISTINCT "
      "elements of Sp6(2) (uniqueness verified row-wise)",
      Nel == 1451520 and np.unique(EN, axis=0).shape[0] == 1451520)
cmask = np.ones(Nel, bool)
for g in S28:
    gn = np.array(g, np.uint8)
    cmask &= (EN[:, gn] == gn[EN]).all(axis=1)
check("4b", "the centre of Sp6(2) is trivial (exhaustive scan: only the "
      "identity commutes with all 7 generators); hence Z(W(E7)) = {+-1}",
      int(cmask.sum()) == 1)
counts = np.bincount(ORDv)
order_set = sorted(int(o) for o in range(len(counts)) if counts[o] > 0)
census = {int(o): int(counts[o]) for o in order_set}
print(f"  ELEMENT-ORDER CENSUS of Sp6(2), exhaustive over all 1451520:")
for o in order_set:
    print(f"    order {o:2d}: {census[o]:7d} elements")
check("4c", "the element-order set of Sp6(2) is exactly "
      "{1,2,3,4,5,6,7,8,9,10,12,15} (expected)",
      order_set == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15],
      f"measured {order_set}")
check("4d", "14 is NOT an element order of Sp6(2) (the load-bearing bar; "
      "exhaustive over all 1451520 elements)", 14 not in order_set)
SL27 = SL2(7)
sl27_orders = sorted(set(mord(M, 7) for M in SL27))
sl27_ninv = sum(1 for M in SL27 if mord(M, 7) == 2)
check("4e", "SL(2,7) HAS elements of order 14 (-I times an order-7 element) "
      "and a UNIQUE involution -I (from the 336 matrices)",
      14 in sl27_orders and sl27_ninv == 1,
      f"SL(2,7) order set {sl27_orders}")
check("4f", "VERDICT SL(2,7): no order-14 element => SL(2,7) is NOT a "
      "subgroup of Sp6(2); by the lemma (unique involution, even quotient) "
      "it cannot contain -1 either => SL(2,7) is NOT a subgroup of W(E7) "
      "AT ALL", 14 not in order_set and 14 in sl27_orders and sl27_ninv == 1)
print(f"[t={time.time()-T0:6.1f}s] check 4 done")

# ======================================================================
banner("CHECK 5 -- exhaustive embedding searches in Sp6(2): 2I, 2T, 2O, GL(2,3)")
# ======================================================================
# involution conjugacy classes (exhaustive)
inv_rows = EN[ORDv == 2]
inv_set = {tuple(int(v) for v in r) for r in inv_rows}
n_inv_total = len(inv_set)
classes = []
remaining = set(inv_set)
while remaining:
    x0 = min(remaining)
    orb = {x0}; q = [x0]
    while q:
        x = q.pop()
        for g in S28:                      # generators are involutions
            y = mul28(g, mul28(x, g))
            if y not in orb:
                orb.add(y); q.append(y)
    remaining -= orb
    rep = min(orb)
    classes.append((rep, len(orb), sum(1 for i in range(28) if rep[i] == i)))
classes.sort(key=lambda c: c[1])
check("5a", "involution conjugacy classes of Sp6(2) computed exhaustively: "
      f"{len(classes)} classes, sizes {[c[1] for c in classes]}, total "
      f"{sum(c[1] for c in classes)} = census count {int(counts[2])}",
      sum(c[1] for c in classes) == n_inv_total == int(counts[2]))
for i, (rep, sz, fx) in enumerate(classes):
    print(f"    class {i+1}: size {sz}, fixed points on 28: {fx}")

# model-group certificates: the standard generators EXIST in each cover,
# so searching (s,t) with the stated power conditions is exhaustive for
# subgroup existence.
SL25 = SL2(5); SL23 = SL2(3); GL23 = GL2(3)
prof_2I = mat_profile(SL25, 5); prof_2T = mat_profile(SL23, 3)
prof_GL23 = mat_profile(GL23, 3)
mI5 = (4, 0, 0, 4); mI3 = (2, 0, 0, 2)
def model_pair(G, p, mI, o_s, e_s, o_t, e_t, full):
    Ss = [M for M in G if mord(M, p) == o_s and
          all_pow(M, e_s, p) == mI]
    Ts = [M for M in G if mord(M, p) == o_t and
          all_pow(M, e_t, p) == mI]
    for A in Ss:
        for B in Ts:
            AB = mmul(A, B, p)
            if mmul(AB, AB, p) == mI:
                cl = mat_closure([A, B], lambda X, Y: mmul(X, Y, p))
                if len(cl) == full: return True
    return False
def all_pow(M, e, p):
    x = (1, 0, 0, 1)
    for _ in range(e): x = mmul(x, M, p)
    return x
ok_2I_model = model_pair(SL25, 5, mI5, 6, 3, 10, 5, 120)
ok_2T_model = model_pair(SL23, 3, mI3, 6, 3, 6, 3, 24)
check("5b", "model certificates: SL(2,5) contains (s,t), ord 6/10, with "
      "s^3 = t^5 = (st)^2 = -I generating all 120; SL(2,3) contains (s,t), "
      "ord 6/6, s^3 = t^3 = (st)^2 = -I generating all 24; both have a "
      "UNIQUE involution -I.  Hence the presentation searches below are "
      "EXHAUSTIVE for subgroup existence (any embedded copy supplies such "
      "a pair, with z its central involution, conjugated onto a class "
      "representative)",
      ok_2I_model and ok_2T_model
      and prof_2I.get(2) == 1 and prof_2T.get(2) == 1)
# 2O built inside SL(2,9) (preimage route): search s^4=t^3=(st)^2=-I
SL29 = [(a, b, c, d) for a in range(9) for b in range(9)
        for c in range(9) for d in range(9)
        if f9add(f9mul(a, d), f9mul(2, f9mul(b, c))) == 1]
def pow9(M, e):
    x = I9
    for _ in range(e): x = mmul9(x, M)
    return x
S8m = [M for M in SL29 if mord9(M) == 8 and pow9(M, 4) == mI9]
T6m = [M for M in SL29 if mord9(M) == 6 and pow9(M, 3) == mI9]
twoO = None
for A in S8m:
    for B in T6m:
        AB = mmul9(A, B)
        if mmul9(AB, AB) == mI9:
            cl = mat_closure([A, B], mmul9, cap=200)
            if len(cl) == 48:
                twoO = cl; break
    if twoO: break
prof_2O = dict(sorted(Counter(mord9(M) for M in twoO).items())) if twoO else None
n_inv_2O = sum(1 for M in twoO if mord9(M) == 2) if twoO else -1
check("5c", "model certificate: 2O (binary octahedral) realized inside "
      "SL(2,9) from a pair s^4 = t^3 = (st)^2 = -I of orders 8/6, order 48, "
      "UNIQUE involution -I (an order-48 image of the <2,3,4> triangle "
      "presentation with z != 1 IS 2O)", twoO is not None and n_inv_2O == 1,
      f"2O profile {prof_2O}")
print(f"[t={time.time()-T0:6.1f}s] model certificates done")

P3, P4, P5 = Pk[3], Pk[4], Pk[5]
def pair_search(z, S_idx, T_idx, cap=400000):
    """all (s,t), s in EN[S_idx], t in EN[T_idx], with (st)^2 = z"""
    z_np = np.array(z, np.uint8)
    Ta = EN[T_idx]
    hits = []; total = 0
    for ii in range(len(S_idx)):
        s = EN[S_idx[ii]]
        ST = s[Ta]
        ST2 = np.take_along_axis(ST, ST, axis=1)
        m = (ST2 == z_np).all(axis=1)
        w = np.nonzero(m)[0]
        total += w.size
        if len(hits) < cap:
            for j in w[:cap - len(hits)]:
                hits.append((int(S_idx[ii]), int(T_idx[int(j)])))
    return hits, total

def row_tuple(i): return tuple(int(v) for v in EN[i])

def certify(s, t, z, expect, ref_prof, unique_inv=True):
    G = closure([s, t], cap=4 * expect)
    prof = profile_of(G)
    invs = [g for g in G if pord(g) == 2]
    ok = (len(G) == expect and prof == ref_prof
          and (not unique_inv or (len(invs) == 1 and invs[0] == z)))
    return ok, prof

# ---- 5d: SL(2,5) = 2I, exhaustive over every involution class
found_2I = None; stats_2I = []
for ci, (z, sz, fx) in enumerate(classes):
    z_np = np.array(z, np.uint8)
    S_idx = np.nonzero((P3 == z_np).all(axis=1) & (ORDv == 6))[0]
    T_idx = np.nonzero((P5 == z_np).all(axis=1) & (ORDv == 10))[0]
    hits, total = pair_search(z, S_idx, T_idx) if len(S_idx) and len(T_idx) \
        else ([], 0)
    stats_2I.append((ci + 1, len(S_idx), len(T_idx), total))
    if hits and found_2I is None:
        for hs, ht in hits[:200]:
            s, t = row_tuple(hs), row_tuple(ht)
            ok, prof = certify(s, t, z, 120, prof_2I)
            if ok:
                found_2I = (ci + 1, s, t, z, len(hits), total); break
print("  2I search: per class (class, #s: s^3=z ord 6, #t: t^5=z ord 10, "
      "#pairs (st)^2=z):")
for row in stats_2I: print(f"    {row}")
if found_2I:
    ci, s, t, z, nh, tot = found_2I
    check("5d", f"SL(2,5) = 2I FOUND in Sp6(2) (class {ci} centre): order "
          "120, unique involution = z, profile matches SL(2,5)", True,
          f"witness s={list(s)} t={list(t)}")
else:
    no_pairs = all(r[3] == 0 for r in stats_2I)
    check("5d", "SL(2,5) = 2I NOT FOUND: exhaustive over every involution "
          "class z of Sp6(2) and ALL pairs (s,t) with s^3 = z (order 6), "
          "t^5 = z (order 10), no pair satisfies (st)^2 = z  =>  "
          "SL(2,5) is NOT a subgroup of Sp6(2), hence (lemma) NOT a "
          "subgroup of W(E7) at all", no_pairs,
          "zero satisfying pairs across all classes" if no_pairs else
          "pairs existed but none certified -- INVESTIGATE")
print(f"[t={time.time()-T0:6.1f}s] 2I search done")

# ---- 5e: SL(2,3) = 2T, exhaustive over every involution class
found_2T = None; stats_2T = []; hits_2T_by_class = {}
for ci, (z, sz, fx) in enumerate(classes):
    z_np = np.array(z, np.uint8)
    S_idx = np.nonzero((P3 == z_np).all(axis=1) & (ORDv == 6))[0]
    hits, total = pair_search(z, S_idx, S_idx) if len(S_idx) else ([], 0)
    stats_2T.append((ci + 1, len(S_idx), total))
    hits_2T_by_class[ci] = hits
    if hits and found_2T is None:
        for hs, ht in hits[:200]:
            s, t = row_tuple(hs), row_tuple(ht)
            ok, prof = certify(s, t, z, 24, prof_2T)
            if ok:
                found_2T = (ci + 1, s, t, z, len(hits), total); break
print("  2T search: per class (class, #s: s^3=z ord 6, #pairs (st)^2=z):")
for row in stats_2T: print(f"    {row}")
if found_2T:
    ci, s, t, z2T, nh, tot = found_2T
    check("5e", f"SL(2,3) = 2T FOUND in Sp6(2) (class {ci} centre): order 24, "
          "unique involution = z, profile matches SL(2,3)", True,
          f"witness s={list(s)} t={list(t)}")
else:
    no_pairs = all(r[2] == 0 for r in stats_2T)
    check("5e", "SL(2,3) = 2T NOT FOUND: exhaustive over every involution "
          "class z and ALL pairs (s,t), s^3 = t^3 = z (order 6), none with "
          "(st)^2 = z  =>  SL(2,3) not in Sp6(2), hence not in W(E7)",
          no_pairs)
print(f"[t={time.time()-T0:6.1f}s] 2T search done")

# ---- 5f: 2O, exhaustive presentation search s^4 = t^3 = (st)^2 = z
found_2O = None; stats_2O = []
for ci, (z, sz, fx) in enumerate(classes):
    z_np = np.array(z, np.uint8)
    S_idx = np.nonzero((P4 == z_np).all(axis=1) & (ORDv == 8))[0]
    T_idx = np.nonzero((P3 == z_np).all(axis=1) & (ORDv == 6))[0]
    hits, total = pair_search(z, S_idx, T_idx) if len(S_idx) and len(T_idx) \
        else ([], 0)
    stats_2O.append((ci + 1, len(S_idx), len(T_idx), total))
    if hits and found_2O is None:
        for hs, ht in hits[:200]:
            s, t = row_tuple(hs), row_tuple(ht)
            ok, prof = certify(s, t, z, 48, prof_2O)
            if ok:
                found_2O = (ci + 1, s, t, z, len(hits), total); break
print("  2O search: per class (class, #s: s^4=z ord 8, #t: t^3=z ord 6, "
      "#pairs (st)^2=z):")
for row in stats_2O: print(f"    {row}")
if found_2O:
    ci, s, t, z, nh, tot = found_2O
    check("5f", f"2O (binary octahedral) FOUND in Sp6(2) (class {ci} "
          "centre): order 48, unique involution = z, profile matches the "
          "SL(2,9)-built 2O", True, f"witness s={list(s)} t={list(t)}")
else:
    no_pairs = all(r[3] == 0 for r in stats_2O)
    check("5f", "2O NOT FOUND: exhaustive over every involution class z and "
          "ALL pairs (s,t) with s^4 = z (order 8), t^3 = z (order 6), none "
          "with (st)^2 = z  =>  2O not in Sp6(2), hence not in W(E7)",
          no_pairs)
print(f"[t={time.time()-T0:6.1f}s] 2O search done")

# ---- 5g: GL(2,3) = 2.S4 -- normalizer extension over EVERY SL(2,3) copy
# (center-normalized: every GL(2,3) contains a unique SL(2,3) (index 2,
#  abelianization Z2), same centre; conjugate the centre onto a class rep;
#  then its SL(2,3) is one of the copies enumerated from the 2T hits.)
prof_SL23xZ2 = {}
for o, c in prof_2T.items():
    prof_SL23xZ2[o] = prof_SL23xZ2.get(o, 0) + c
    prof_SL23xZ2[lcm(o, 2)] = prof_SL23xZ2.get(lcm(o, 2), 0) + c
prof_SL23xZ2 = dict(sorted(prof_SL23xZ2.items()))
found_GL = None; gl_stats = []
if found_2T:
    RH = np.random.default_rng(56728).integers(1, 2**63, size=28,
                                               dtype=np.uint64)
    def hrows(X): return (X.astype(np.uint64) * RH).sum(axis=1)
    for ci in range(len(classes)):
        hits = hits_2T_by_class.get(ci, [])
        if not hits: continue
        z = classes[ci][0]; z_np = np.array(z, np.uint8)
        # C(z) once per class
        cz_mask = (EN[:, z_np] == z_np[EN]).all(axis=1)
        cz_idx = np.nonzero(cz_mask)[0]
        Cz = EN[cz_idx]
        Cz_inv = np.argsort(Cz, axis=1).astype(np.uint8)
        # distinct copies from hits
        copies = {}
        for hs, ht in hits:
            s, t = row_tuple(hs), row_tuple(ht)
            Hset = frozenset(closure([s, t], cap=100))
            if len(Hset) == 24 and Hset not in copies:
                copies[Hset] = (s, t)
        types_seen = Counter(); n_copies = len(copies)
        for Hset, (s, t) in copies.items():
            Hhash = np.array(sorted(
                int(hrows(np.array([list(h)], np.uint8))[0])
                for h in Hset), dtype=np.uint64)
            mask_n = np.ones(len(cz_idx), bool)
            for h in (s, t):
                hn = np.array(h, np.uint8)
                CONJ = np.take_along_axis(Cz[:, hn], Cz_inv, axis=1)
                mask_n &= np.isin(hrows(CONJ), Hhash)
            cand = np.nonzero(mask_n)[0]
            for j in cand:
                r = tuple(int(v) for v in Cz[j])
                if r in Hset: continue
                # exact normalizer verification
                rin = inv28(r)
                if any(mul28(r, mul28(h, rin)) not in Hset for h in (s, t)):
                    continue
                if pord(r) != 2: continue
                K = set(Hset) | {mul28(h, r) for h in Hset}
                if len(K) != 48: continue
                profK = profile_of(K)
                if profK == prof_GL23:
                    types_seen["GL(2,3)"] += 1
                    if found_GL is None:
                        found_GL = (ci + 1, s, t, r)
                elif profK == prof_SL23xZ2:
                    types_seen["SL(2,3) x Z2"] += 1
                elif profK == prof_2O:
                    types_seen["2O"] += 1
                else:
                    types_seen[str(profK)] += 1
            if found_GL: break
        gl_stats.append((ci + 1, n_copies, dict(types_seen)))
        if found_GL: break
    print("  GL(2,3) normalizer-extension scan (class, #distinct SL(2,3) "
          "copies with centre = rep, extension types seen up to stop):")
    for row in gl_stats: print(f"    {row}")
    if found_GL:
        ci, s, t, r = found_GL
        Kw = closure([s, t, r], cap=200)
        n_inv_K = sum(1 for g in Kw if pord(g) == 2)
        check("5g", f"GL(2,3) = 2.S4 FOUND in Sp6(2) (class {ci} centre): "
              "order 48 = <2T, r> with r an involution normalizing the 2T "
              f"copy; profile matches GL(2,3), {n_inv_K} involutions "
              "(split-type cover, transpositions lift to involutions)",
              len(Kw) == 48 and profile_of(Kw) == prof_GL23,
              f"r={list(r)}")
    else:
        check("5g", "GL(2,3) NOT FOUND by involution extension over every "
              "enumerated SL(2,3) copy (centre-normalized, exhaustive over "
              "the recorded 2T hit pairs)", False,
              "expected FOUND via SL(2,3) < S8 < Sp6(2) -- INVESTIGATE")
else:
    check("5g", "GL(2,3) and 2O over SL(2,3): SL(2,3) itself absent, so "
          "both order-48 covers fail A FORTIORI (each contains SL(2,3) "
          "index 2)", True)
print(f"[t={time.time()-T0:6.1f}s] GL(2,3) stage done")

# ---- 5h: the hinge fact for whatever cover was found
if found_2T:
    ci, s, t, z2Tw, nh, tot = found_2T
    s56 = lift_to_Wplus(s); t56 = lift_to_Wplus(t)
    if s56 is None or t56 is None:
        check("5h", "lift of the 2T witness into W+ (shadow BSGS)", False,
              "lift failed -- INVESTIGATE")
    else:
        z56 = perm_pow(s56, 3)
        noncentral = any(mul(g, z56) != mul(z56, g) for g in S)
        check("5h", "THE HINGE FACT on the found copy: lifting the 2T "
              "witness into W+ < W(E7), its central involution lands in "
              "W+, is NOT -1, and is NON-CENTRAL in W(E7) (Z(W(E7)) = "
              "{+-1} by 4b).  Any Schur cover that does embed sits AWAY "
              "from the +- hinge",
              memWp(z56) and z56 != anti and noncentral
              and len(closure([s56, t56], cap=100)) == 24)
else:
    print("  [5h] no non-split cover found in Sp6(2); the hinge fact is "
          "vacuous -- the lemma already forbids covers over the hinge.")
print(f"[t={time.time()-T0:6.1f}s] check 5 done")

# ======================================================================
banner("CHECK 6 -- SPINE containment in Sp6(2) = W+ < W(E7)")
# ======================================================================
print("  [cited] L7 = PSL(2,7) < Sp6(2): SEALED in SM-003 (T-BR bridge) and "
      "SM-015\n  (verify_stoneq_clifford), transitive on the 28; not rebuilt "
      "here.")
check("6a", "PSL(2,7) < Sp6(2) [cited SM-003/SM-015, sealed]", True)

# C6 x Z2 -- exhaustive centralizer scan for a witness
found_C6Z2 = None
idx6 = np.nonzero(ORDv == 6)[0]
for a_i in idx6[:40]:
    a = row_tuple(a_i)
    a_np = EN[a_i]
    cmask_a = (EN[:, a_np] == a_np[EN]).all(axis=1)
    cent_idx = np.nonzero(cmask_a & (ORDv == 2))[0]
    a3 = perm_pow(a, 3)
    for b_i in cent_idx:
        b = row_tuple(b_i)
        if b == a3: continue
        Gab = closure([a, b], cap=48)
        if len(Gab) == 12 and profile_of(Gab) == {1: 1, 2: 3, 3: 2, 6: 6}:
            found_C6Z2 = (a, b, int(cmask_a.sum()))
            break
    if found_C6Z2: break
if found_C6Z2:
    a, b, csz = found_C6Z2
    check("6b", "C6 x Z2 < Sp6(2): commuting a (order 6), b (order 2), "
          "b not in <a>, |<a,b>| = 12, profile {1:1,2:3,3:2,6:6} (abelian "
          "C6 x C2)", True,
          f"|C(a)| = {csz}; a={list(a)} b={list(b)}")
else:
    check("6b", "C6 x Z2 < Sp6(2)", False, "no witness in scanned "
          "centralizers -- INVESTIGATE")

def rand28():
    w = E28
    for _ in range(random.randrange(15, 45)):
        w = mul28(S28[random.randrange(7)], w)
    return w
def find_pair(o_ab, target_order, ref_prof, tries=300000):
    for _ in range(tries):
        g = rand28(); og = pord(g)
        if og % 2: continue
        aa = perm_pow(g, og // 2)
        h = rand28(); oh = pord(h)
        if oh % 3: continue
        bb = perm_pow(h, oh // 3)
        if pord(mul28(aa, bb)) != o_ab: continue
        G = closure([aa, bb], cap=4 * target_order)
        if len(G) == target_order and profile_of(G) == ref_prof:
            return aa, bb, G
    return None
# reference profiles from small permutation models
A5m = closure([(1, 2, 0, 3, 4), (1, 2, 3, 4, 0)])
S4m = closure([(1, 0, 2, 3), (1, 2, 3, 0)])
A4m = closure([(1, 2, 0, 3), (0, 2, 3, 1)])
prof_A5, prof_S4, prof_A4 = profile_of(A5m), profile_of(S4m), profile_of(A4m)
r5 = find_pair(5, 60, prof_A5)
check("6c", "A5 < Sp6(2): witness a^2 = b^3 = (ab)^5 = 1, |<a,b>| = 60, "
      "profile matches A5 (the <2,3,5> presentation of order 60 IS A5)",
      r5 is not None,
      f"a={list(r5[0])} b={list(r5[1])}" if r5 else "no witness")
r4 = find_pair(4, 24, prof_S4)
check("6d", "S4 < Sp6(2): witness a^2 = b^3 = (ab)^4 = 1, |<a,b>| = 24, "
      "profile matches S4", r4 is not None,
      f"a={list(r4[0])} b={list(r4[1])}" if r4 else "no witness")
A4w = None
if r4:
    aa, bb, S4w = r4
    S4l = list(S4w)
    comms = set()
    for x in S4l:
        xi = inv28(x)
        for y in S4l:
            yi = inv28(y)
            comms.add(mul28(mul28(x, y), mul28(xi, yi)))
    A4w = closure(sorted(comms), cap=48)
check("6e", "A4 < Sp6(2): the derived subgroup of the found S4 has order 12 "
      "with profile matching A4", A4w is not None and len(A4w) == 12
      and profile_of(A4w) == prof_A4)
check("6f", "Z2 < Sp6(2): trivially (any involution, e.g. the class-1 "
      "representative)", len(classes) > 0)
print(f"[t={time.time()-T0:6.1f}s] check 6 done")

# ======================================================================
banner("CHECK 7 -- the SPLIT covers over the +- hinge: Ih and Th in W(E7)")
# ======================================================================
prof_Ih = {}
for o, c in prof_A5.items():
    prof_Ih[o] = prof_Ih.get(o, 0) + c
    prof_Ih[lcm(o, 2)] = prof_Ih.get(lcm(o, 2), 0) + c
prof_Ih = dict(sorted(prof_Ih.items()))
prof_Th = {}
for o, c in prof_A4.items():
    prof_Th[o] = prof_Th.get(o, 0) + c
    prof_Th[lcm(o, 2)] = prof_Th.get(lcm(o, 2), 0) + c
prof_Th = dict(sorted(prof_Th.items()))
ok7a = False; H120 = []
if r5:
    a56, b56 = lift_to_Wplus(r5[0]), lift_to_Wplus(r5[1])
    if a56 is not None and b56 is not None:
        K60 = closure([a56, b56], cap=240)
        H120 = closure([a56, b56, anti], cap=480)
        ok7a = (len(K60) == 60
                and anti not in K60 and len(H120) == 120
                and set(H120) == set(K60) | {mul(anti, k) for k in K60}
                and all(mul(anti, h) == mul(h, anti) for h in H120)
                and profile_of(H120) == prof_Ih)
check("7a", "Ih = <-1> x A5 < W(E7) OVER THE HINGE: the A5 witness lifts "
      "into W+ (order 60, -1 not inside), and <A5, -1> has order 120 with "
      "-1 central and profile = A5 x Z2 (31 involutions -- NOT the unique-"
      "involution 2I)", ok7a,
      f"profile {profile_of(H120) if H120 else '--'} vs Ih {prof_Ih}")
ok7b = False; H24 = []
if A4w:
    A4l = sorted(A4w)
    gens_A4_28 = []; Kc = {E28}
    for g in A4l:
        if g in Kc: continue
        gens_A4_28.append(g); Kc = closure(gens_A4_28, cap=48)
        if len(Kc) == 12: break
    gens_A4_56 = [lift_to_Wplus(g) for g in gens_A4_28]
    if all(g is not None for g in gens_A4_56):
        K12 = closure(gens_A4_56, cap=48)
        H24 = closure(gens_A4_56 + [anti], cap=96)
        ok7b = (len(K12) == 12 and anti not in K12 and len(H24) == 24
                and set(H24) == set(K12) | {mul(anti, k) for k in K12}
                and all(mul(anti, h) == mul(h, anti) for h in H24)
                and profile_of(H24) == prof_Th)
check("7b", "Th = <-1> x A4 < W(E7) OVER THE HINGE: the A4 witness lifts "
      "into W+, and <A4, -1> has order 24 with -1 central and profile "
      "= A4 x Z2 (7 involutions -- NOT the unique-involution 2T)", ok7b,
      f"profile {profile_of(H24) if H24 else '--'} vs Th {prof_Th}")
print("  [cited] SM-013 (verify_stonef_b_dq1): the full preimage of "
      "PSL(2,7) in W(E7)\n  is the SPLIT extension 2 x L2(7) -- same "
      "pattern: the cover shadow W(E7) holds\n  exactly the SPLIT covers "
      "over the hinge, never the Schur covers.")
check("7c", "consistency with sealed SM-013: preimage of PSL(2,7) is "
      "2 x L2(7) (split), matching the split-only hinge picture "
      "[cited, not rebuilt]", True)
print(f"[t={time.time()-T0:6.1f}s] check 7 done")

# ======================================================================
banner("CHECK 8 -- VERDICT")
# ======================================================================
spine_ok = all([r5 is not None, r4 is not None, A4w is not None,
                found_C6Z2 is not None])
_spine = "ALL VERIFIED" if spine_ok else "GAPS -- see FAILs"
_s2T = "FOUND" if found_2T else "NOT FOUND"
_sGL = "FOUND" if found_GL else "NOT FOUND"
_s2O = "FOUND" if found_2O else "NOT FOUND"
_s2I = "FOUND" if found_2I else "NOT FOUND"
if found_2I:
    _v2I = "contained in Sp6(2) (away from the hinge only)"
else:
    _v2I = ("NOT a subgroup of Sp6(2) (exhaustive presentation search, "
            "check 5d), hence NOT a subgroup of W(E7) at all")
print(f"""
VERDICT (all claims computed above; exhaustive claims say over what):

  SPLITNESS.  W(E7) = <-1> x W+ with W+ = Sp6(2): a SPLIT direct product
  Z2 x Sp6(2) (checks 2a-2d).  Every subgroup question about W(E7) reduces
  by the structure lemma [P] (check 3) to Sp6(2) plus the hinge dichotomy.

  WHAT W(E7) CONTAINS of the two towers:
    Tower A (spine), all six levels, inside W+ = Sp6(2) hence inside W(E7):
      PSL(2,7) [cited SM-003/SM-015]; C6xZ2, A5, S4, A4, Z2 with explicit
      witnesses (checks 6a-6f): {_spine}.
    Split covers over the +- hinge: Ih = <-1> x A5 and Th = <-1> x A4 sit in
    W(E7) with the +- centre as the Z2 (checks 7a-7b), matching sealed
    SM-013 (preimage of PSL(2,7) = 2 x L2(7), split).
    Non-split covers found INSIDE Sp6(2) (away from the hinge):
      SL(2,3) = 2T: {_s2T};  GL(2,3) = 2.S4: {_sGL};  2O: {_s2O};
      SL(2,5) = 2I: {_s2I};
      each found copy has its central involution NON-central in W(E7)
      (check 5h) -- present, but never over the hinge.

  WHAT W(E7) PROVABLY DOES NOT CONTAIN:
    Any non-split Schur cover OVER THE +- HINGE: impossible for every
    unique-involution cover (2I, 2T, 2O, SL(2,7)) by the lemma -- if -1
    were the cover's centre the extension would split.
    SL(2,7): NOT a subgroup of W(E7) AT ALL -- Sp6(2) has no element of
    order 14 (exhaustive census, check 4), and -1 in a copy is impossible
    (unique involution), so neither branch of the lemma admits it.
    SL(2,5) = 2I: {_v2I}.

  THE HINGE READING.  'Cover shadow = W(E7) holds the Schur tower over the
  +- centre' is REFUTED: W(E7) = 2 x Sp6(2) is split, and holds over the
  hinge exactly the SPLIT covers (Ih, Th, 2 x L2(7), ...).  The Schur tower
  over a hinge would need the NON-split double cover 2.Sp6(2) (Sp6(2) has
  Schur multiplier Z2) -- a DIFFERENT group from W(E7) = 2 x Sp6(2).  That
  is the natural successor question; NOT computed here.
""")

print("=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed"
      + (f"   FAILED: {FAILED}" if FAILED else ""))
print(f"total time {time.time()-T0:.1f}s")
print("=" * 78)
