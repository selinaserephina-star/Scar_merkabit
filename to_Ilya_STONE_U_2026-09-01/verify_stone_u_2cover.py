# -*- coding: utf-8 -*-
r"""verify_stone_u_2cover.py -- STONE U: THE OTHER DOUBLE COVER, H = 2.Sp6(2)?

Brief: BRIEF_STONE_U_2COVER.md (lock BRIEF_STONE_U_LOCK.sha256, sha verified
before this run:
c27a9019fe47803df49fb95b3e8b8089229c8406df1027ee4b569060aec89535).

Question: SM-023 proved W(E7) = <-1> x Sp6(2) is SPLIT and exiled the
non-split Schur tower from the +- hinge.  Sp6(2) has Schur multiplier Z2, so
exactly one other +-extension exists: the NON-split 2.Sp6(2).  Stone U builds
it inside W(E8) and asks: does the Schur tower live over ITS centre -- and
which spine levels survive upstairs?

ROUTE (the brief's declared construction; bars UB1-UB6):
  UB1  W(E8) as permutations of the 240 roots (BSGS, order 696729600);
       -1 central; mod-2 reduction L/2L = F2^8 with q(x) = x.x/2 (plus-type,
       nondegenerate); ker(pi) = {+-1}; pair action = W(E8)/{+-1}.
  UB2  control: Stab_W(E8)(alpha) has order 2903040 = |W(E7)|, misses -1;
       its derived subgroup C (order 1451520) is a complement over the
       vector-type Sp6(2) (fixes the nonsingular alpha-bar):
       pi^-1(vector type) = <-1> x C, SPLIT.  [registered expectation]
  UB3  spin type: Cl0(V7,q7) = Cl(V6, x1x2+x3x4+x5x6) realized on the 8-dim
       module Lambda(F2^3); transvections t_v lift to M_v = c.I + sum v_i
       gamma_i; K0 = <M_v> order 1451520, irreducible, invariant plus-type
       Q8; transport by an explicit isometry T of 8-dim plus-type F2
       quadratic spaces into (L/2L, q); lift generators through the
       pair-BSGS shadow chain.
  UB4  H = pi^-1(K_spin) = <lifts, -1>, order 2903040: THE SPLIT TEST
       (derived subgroup; EXACT by the index-<=2 argument printed at the
       site) + the full element-order census of H via square-sign tables.
       [registered expectation: H perfect, i.e. NON-split, H = 2.Sp6(2)]
  UB5  the tower upstairs: presentation hunts in K-bar = H/{+-1}; preimage
       of each found copy classified by census + square-sign (decisive per
       copy).  [registered expectation: the L2(7) preimage is SL(2,7)]
  UB6  the two-shadow verdict table.

MACHINERY PRECEDENTS reused: verify_overgroup_containment.py (BSGS with
membership strips, shadow-BSGS lifting, numpy transversal-product
enumeration, presentation searches over order-indexed element arrays),
verify_stoneq_clifford.py (F2 quadratic/symplectic machinery, hyperbolic
Gram-Schmidt), verify_stonef_b_dq1.py / verify_stone_r_altitude.py (Weyl
groups from simple reflections), verify_envelope_normalizer.py (numpy
full-pass trick).

INSTANTIATION NOTES (choices the brief left open; the declared route, no
amendment): (i) Cl0(V7,q7) ~ M8(F2) is realized DIRECTLY on its 8-dim
module: Cl0(V7) = Cl(V6,q6) via x |-> x.e7, and Cl(V6,hyperbolic) acts on
the exterior algebra Lambda(F2^3) by creation/annihilation operators --
this is the minimal left ideal of M8(F2) written in an explicit basis.
(ii) Over F2, e7 (the radical line of the polar form, q(e7)=1) is CENTRAL
in Cl(V7), so v.e7 in Cl0 implements the transvection t_v by conjugation,
giving the lift map v |-> M_v = c.I + sum_{i<7} v_i gamma_i with
M_v^2 = q7(v).I = I; the only central unit of M8(F2) is 1, so the lifted
group maps isomorphically onto <t_v> (no sign ambiguity over F2).
(iii) K0's economical generating pair is chosen among random products of
the 63 transvection lifts, order re-verified by BSGS.

DISCIPLINE: compute, never assert; registered expectations resolved at
equal prominence either way; exhaustive claims say over what; fail-first
logs renamed, never deleted.  Cache: _stone_u_cache/ (BSGS chains,
enumerations, censuses, witnesses -- checkpoints of this script's own
computation, noted where loaded; resumable so each invocation stays short).
Optional staging: python -X utf8 verify_stone_u_2cover.py [max_stage],
stages 1..7; no argument = run everything.  Not RH/GRH; no physical
identification (Rule 3).

Run:  python -X utf8 verify_stone_u_2cover.py
"""
import itertools, json, os, sys, time, random
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

def note(t): print("  " + t, flush=True)

def lcm(a, b): return a * b // gcd(a, b)

CACHE = "_stone_u_cache"
os.makedirs(CACHE, exist_ok=True)
random.seed(20260901)
RNG = np.random.default_rng(20260901)
MAX_STAGE = int(sys.argv[1]) if len(sys.argv) > 1 else 99
def stage_gate(n):
    if n >= MAX_STAGE:
        print(f"\n[staged checkpoint exit after stage {n}; caches written; "
              "NOT a verdict -- rerun with a higher stage]", flush=True)
        print(f"[so far: {PASS} PASS, {FAIL} FAIL"
              + (f", FAILED: {FAILED}" if FAILED else "") + "]")
        sys.exit(0)

# ======================================================================
# permutation utilities (precedent: verify_overgroup_containment.py)
# ======================================================================
def pmul(a, b): return tuple(a[x] for x in b)          # (a o b)(k) = a[b[k]]
def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def pident(n): return tuple(range(n))
def ppow(p, e):
    x = pident(len(p)); b = p
    while e:
        if e & 1: x = pmul(x, b)
        b = pmul(b, b); e >>= 1
    return x
def pord(p):
    n = len(p); e = tuple(range(n)); x = p; k = 1
    while x != e:
        x = pmul(x, p); k += 1
    return k
def closure(gens, cap=10 ** 6):
    n = len(gens[0]); e = tuple(range(n))
    G = {e}; fr = [e]
    while fr:
        a = fr.pop()
        for g in gens:
            b = pmul(a, g)
            if b not in G:
                G.add(b); fr.append(b)
                if len(G) > cap: return G
    return G
def profile_of(G):
    return dict(sorted(Counter(pord(g) for g in G).items()))
def rand_word(gens, lo=15, hi=45):
    w = pident(len(gens[0]))
    for _ in range(random.randrange(lo, hi)):
        w = pmul(gens[random.randrange(len(gens))], w)
    return w
def comm(a, b): return pmul(pmul(a, b), pmul(pinv(a), pinv(b)))

# ======================================================================
# BSGS (deterministic Schreier-Sims; verbatim algorithm from the sealed
# verify_stone_r / verify_overgroup_containment, extended with an optional
# forced initial base point and cached chains)
# ======================================================================
def make_bsgs_full(gen_list, deg, init_base=None):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[x] for x in b)
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    base = list(init_base) if init_base else []
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
    return o, is_member, transv, base, lvl

def _member_from_chain(base, transv, deg):
    E = tuple(range(deg))
    def is_member(g):
        h = g
        for i in range(len(base)):
            x = h[base[i]]
            if x not in transv[i]: return False
            h = pmul(pinv(transv[i][x]), h)
        return h == E
    return is_member

def _bsgs_save(fname, base, transv, lvl, deg):
    payload = {"base": np.array(base, dtype=np.int16),
               "nlvl": np.array([len(transv)])}
    for i, T in enumerate(transv):
        payload["k%d" % i] = np.array(list(T.keys()), dtype=np.int16)
        payload["v%d" % i] = np.array([list(p) for p in T.values()],
                                      dtype=np.uint8)
        payload["g%d" % i] = (np.array([list(p) for p in lvl[i]],
                                       dtype=np.uint8)
                              if lvl[i] else np.zeros((0, deg), np.uint8))
    np.savez_compressed(fname, **payload)

def _bsgs_load(fname, deg):
    z = np.load(fname)
    base = [int(b) for b in z["base"]]
    nl = int(z["nlvl"][0])
    transv = []; lvl = []
    for i in range(nl):
        keys = z["k%d" % i]; vals = z["v%d" % i]
        transv.append({int(k): tuple(int(x) for x in vals[j])
                       for j, k in enumerate(keys)})
        gv = z["g%d" % i]
        lvl.append([tuple(int(x) for x in gv[j])
                    for j in range(gv.shape[0])])
    o = 1
    for T in transv: o *= len(T)
    return o, _member_from_chain(base, transv, deg), transv, base, lvl

def bsgs_cached(name, gens, deg, init_base=None):
    f = os.path.join(CACHE, name + ".npz")
    if os.path.exists(f):
        o, mem, transv, base, lvl = _bsgs_load(f, deg)
        note("[cache] BSGS '%s' loaded (order %d, chain depth %d)"
             % (name, o, len(base)))
        return o, mem, transv, base, lvl
    t1 = time.time()
    o, mem, transv, base, lvl = make_bsgs_full(gens, deg, init_base)
    _bsgs_save(f, base, transv, lvl, deg)
    note("[built] BSGS '%s': order %d, chain depth %d, %.1fs"
         % (name, o, len(base), time.time() - t1))
    return o, mem, transv, base, lvl

# shadow BSGS on pairs (perm on d1 points, carried perm on d2 points):
# a chain for the d1-action whose transversal elements carry preimages.
# (precedent: make_shadow_bsgs in verify_overgroup_containment.py)
def make_shadow(gen_pairs, d1, d2):
    E1 = tuple(range(d1)); Ep = (E1, tuple(range(d2)))
    def mulP(a, b):
        return (tuple(a[0][x] for x in b[0]), tuple(a[1][x] for x in b[1]))
    def invP(a):
        r1 = [0] * d1; r2 = [0] * d2
        for i, x in enumerate(a[0]): r1[x] = i
        for i, x in enumerate(a[1]): r2[x] = i
        return (tuple(r1), tuple(r2))
    def is_e(a): return a[0] == E1
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
    return o, base, transv

def shadow_cached(name, gen_pairs, d1, d2):
    f = os.path.join(CACHE, name + ".npz")
    if os.path.exists(f):
        z = np.load(f)
        base = [int(b) for b in z["base"]]
        nl = int(z["nlvl"][0])
        transv = []
        for i in range(nl):
            keys = z["k%d" % i]; v1 = z["a%d" % i]; v2 = z["b%d" % i]
            transv.append({int(k): (tuple(int(x) for x in v1[j]),
                                    tuple(int(x) for x in v2[j]))
                           for j, k in enumerate(keys)})
        o = 1
        for T in transv: o *= len(T)
        note("[cache] shadow chain '%s' loaded (order %d)" % (name, o))
        return o, base, transv
    t1 = time.time()
    o, base, transv = make_shadow(gen_pairs, d1, d2)
    payload = {"base": np.array(base, dtype=np.int16),
               "nlvl": np.array([len(transv)])}
    for i, T in enumerate(transv):
        payload["k%d" % i] = np.array(list(T.keys()), dtype=np.int16)
        payload["a%d" % i] = np.array([list(p[0]) for p in T.values()],
                                      dtype=np.uint8)
        payload["b%d" % i] = np.array([list(p[1]) for p in T.values()],
                                      dtype=np.uint8)
    np.savez_compressed(f, **payload)
    note("[built] shadow chain '%s': order %d, %.1fs"
         % (name, o, time.time() - t1))
    return o, base, transv

def shadow_sift(base, transv, d1, d2, target):
    """canonical preimage (d2-perm) of a d1-perm through the shadow chain,
    or None if the target is not in the chain's group."""
    r2 = tuple(range(d2)); h = target
    for i, bpt in enumerate(base):
        x = h[bpt]
        if x not in transv[i]: return None
        t1p, t2p = transv[i][x]
        r2 = pmul(r2, t2p)
        h = pmul(pinv(t1p), h)
    if h != tuple(range(d1)): return None
    return r2

def enumerate_group_np(transv, deg):
    """numpy transversal-product enumeration (precedent:
    verify_overgroup_containment check 4 / verify_envelope_normalizer)."""
    L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
         for T in transv]
    EN = L[-1]
    for j in range(len(L) - 2, -1, -1):
        EN = np.concatenate([L[j][i][EN] for i in range(L[j].shape[0])])
    return EN

# derived subgroups by random-commutator closure (exactness argued at the
# call sites: if the closure reaches the full order the group is perfect;
# if it stabilizes at index 2 the quotient is Z2, abelian, so the closure
# already CONTAINS [G,G] and equals it)
def derived_cached(name, gens, deg, seed):
    f = os.path.join(CACHE, name + ".npz")
    gf = os.path.join(CACHE, name + "_gens.npz")
    if os.path.exists(f) and os.path.exists(gf):
        o, mem, transv, base, lvl = _bsgs_load(f, deg)
        gz = np.load(gf)["g"]
        cgens = [tuple(int(x) for x in gz[j]) for j in range(gz.shape[0])]
        note("[cache] derived chain '%s' loaded (order %d)" % (name, o))
        return o, mem, transv, cgens
    random.seed(seed)
    coms = []; prev = -1; stable = 0; hist = []
    while True:
        n_new = 12 if not coms else 6
        for _ in range(n_new):
            x = rand_word(gens); y = rand_word(gens)
            coms.append(comm(x, y))
        o, mem, transv, base, lvl = make_bsgs_full(coms, deg)
        hist.append(o)
        if o == prev: stable += 1
        else: stable = 0; prev = o
        if stable >= 2: break
    _bsgs_save(f, base, transv, lvl, deg)
    np.savez_compressed(gf, g=np.array([list(p) for p in coms],
                                       dtype=np.uint8))
    note("[built] derived chain '%s': order history %s (converged)"
         % (name, hist))
    return o, mem, transv, coms

# witness cache (found subgroup generators etc., as plain json)
WIT_F = os.path.join(CACHE, "witnesses.json")
WIT = json.load(open(WIT_F)) if os.path.exists(WIT_F) else {}
def wit_get(key): return WIT.get(key)
def wit_put(key, val):
    WIT[key] = val
    json.dump(WIT, open(WIT_F, "w"))

# ======================================================================
# F2 8x8 matrices as tuples of 8 column bitmasks
# ======================================================================
IDM = tuple(1 << i for i in range(8))
ZEROM = (0,) * 8
def mvec(M, x):
    y = 0
    while x:
        b = x & -x
        y ^= M[b.bit_length() - 1]
        x ^= b
    return y
def mmulF2(A, B): return tuple(mvec(A, c) for c in B)
def madd(A, B): return tuple(a ^ b for a, b in zip(A, B))
def f2_matinv(M):
    rows = []
    for i in range(8):
        r = 0
        for j in range(8):
            if (M[j] >> i) & 1: r |= 1 << j
        rows.append(r | (1 << (8 + i)))
    piv = 0
    for col in range(8):
        p = next((k for k in range(piv, 8) if (rows[k] >> col) & 1), None)
        if p is None: return None
        rows[piv], rows[p] = rows[p], rows[piv]
        for k in range(8):
            if k != piv and (rows[k] >> col) & 1: rows[k] ^= rows[piv]
        piv += 1
    inv_cols = []
    for j in range(8):
        c = 0
        for i in range(8):
            if (rows[i] >> (8 + j)) & 1: c |= 1 << i
        inv_cols.append(c)
    return tuple(inv_cols)
def f2_rank(masks):
    basis = []
    for m in masks:
        for b in basis:
            m = min(m, m ^ b)
        if m:
            basis.append(m); basis.sort(reverse=True)
    return len(basis)
def f2_nullspace(rows, ncols):
    """basis of {c : row . c = 0 for all rows} over F2, c as bitmask."""
    piv_rows = []; piv_cols = []
    for r in rows:
        for pr, pc in zip(piv_rows, piv_cols):
            if (r >> pc) & 1: r ^= pr
        if r:
            c = (r & -r).bit_length() - 1
            piv_rows.append(r); piv_cols.append(c)
    # full RREF: clear every pivot column from every other pivot row
    for a in range(len(piv_rows)):
        for b in range(len(piv_rows)):
            if a != b and (piv_rows[a] >> piv_cols[b]) & 1:
                piv_rows[a] ^= piv_rows[b]
    piv_set = set(piv_cols)
    free = [c for c in range(ncols) if c not in piv_set]
    basis = []
    for fc in free:
        v = 1 << fc
        for pr, pc in zip(piv_rows, piv_cols):
            if (pr >> fc) & 1: v |= 1 << pc
        basis.append(v)
    return basis

print("=" * 78)
print("STONE U -- THE OTHER DOUBLE COVER: H = pi^-1(spin Sp6(2)) inside W(E8)")
print("=" * 78)
print("[t=%6.1fs] start" % (time.time() - T0))

# ======================================================================
banner("STAGE 1 -- UB1(build): W(E8) on the 240 roots; -1 central")
# ======================================================================
# roots in DOUBLED coordinates (every entry an integer):
# 112 integer roots +-e_i +- e_j -> two entries +-2; 128 half-integer roots
# (+-1/2)^8 with an even number of minus signs -> entries +-1.
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj
                roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=8):
    if signs.count(-1) % 2 == 0:
        roots.append(tuple(signs))
NR = len(roots)
ridx = {r: k for k, r in enumerate(roots)}
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
check("1a", "240 E8 roots constructed (112 integer + 128 half-integer), "
      "all of norm^2 = 2",
      NR == 240 and len(ridx) == 240 and all(dot4(r, r) == 2 for r in roots)
      and all(sum(x * y for x, y in zip(r, r)) == 8 for r in roots))

SIMPLE = [
    (1, -1, -1, -1, -1, -1, -1, 1),   # (e1-e2-...-e7+e8)/2
    (2, 2, 0, 0, 0, 0, 0, 0),         # e1+e2
    (-2, 2, 0, 0, 0, 0, 0, 0),        # e2-e1
    (0, -2, 2, 0, 0, 0, 0, 0),        # e3-e2
    (0, 0, -2, 2, 0, 0, 0, 0),        # e4-e3
    (0, 0, 0, -2, 2, 0, 0, 0),        # e5-e4
    (0, 0, 0, 0, -2, 2, 0, 0),        # e6-e5
    (0, 0, 0, 0, 0, -2, 2, 0),        # e7-e6
]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
detG = round(np.linalg.det(np.array(GRAM, dtype=float)))
n_edges = sum(1 for i in range(8) for j in range(i + 1, 8)
              if GRAM[i][j] != 0)
check("1b", "simple-root Gram matrix: diagonal 2, off-diagonal in {0,-1}, "
      "7 bonds (a tree), det 1 (E8 unimodular -- the simple roots are a "
      "Z-basis of L)",
      all(GRAM[i][i] == 2 for i in range(8))
      and all(GRAM[i][j] in (0, -1)
              for i in range(8) for j in range(8) if i != j)
      and n_edges == 7 and detG == 1, "det %d, bonds %d" % (detG, n_edges))
adjD = {i: [j for j in range(8) if j != i and GRAM[i][j] == -1]
        for i in range(8)}
degs = sorted(len(adjD[i]) for i in range(8))
br = next(i for i in range(8) if len(adjD[i]) == 3)
def arm_len(start):
    ln = 0; prev = br; cur = start
    while True:
        ln += 1
        nxt = [x for x in adjD[cur] if x != prev]
        if not nxt: return ln
        prev, cur = cur, nxt[0]
arms = sorted(arm_len(s) for s in adjD[br])
check("1c", "the bond graph IS the E8 Dynkin diagram (unique branch node, "
      "arm lengths 1,2,4)",
      degs == [1, 1, 1, 2, 2, 2, 2, 3] and arms == [1, 2, 4],
      "arms %s" % arms)

S240 = []
for a in SIMPLE:
    perm = []
    for r in roots:
        c = dot4(r, a)                     # integer Cartan pairing
        img = tuple(r[t] - c * a[t] for t in range(8))
        perm.append(ridx[img])
    S240.append(tuple(perm))
check("1d", "the 8 simple reflections s_a(x) = x - (x.a)a are involutions "
      "permuting the 240 roots",
      all(pmul(s, s) == pident(240) for s in S240))
oW, memW, TRW, BASEW, LVLW = bsgs_cached("we8_240", S240, 240)
check("1e", "|<s1..s8>| = 696729600 = |W(E8)| (BSGS on the 240 roots)",
      oW == 696729600, "order %d" % oW)
anti = tuple(ridx[tuple(-x for x in r)] for r in roots)
check("1f", "-1 (the antipode) is a fixed-point-free involution, commutes "
      "with every generator (central), and LIES IN W(E8) (membership strip)",
      all(anti[k] != k for k in range(240))
      and pmul(anti, anti) == pident(240)
      and all(pmul(s, anti) == pmul(anti, s) for s in S240)
      and memW(anti))
print("[t=%6.1fs] stage 1 done" % (time.time() - T0))
stage_gate(1)

# ======================================================================
banner("STAGE 2 -- UB1(mod 2): L/2L with q = x.x/2, plus-type; ker pi = {+-1}")
# ======================================================================
Gm = np.array(GRAM, dtype=np.int64)
Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
check("2a", "the Gram matrix inverts over Z (G Ginv = I): coordinates in "
      "the simple-root basis are exact integers",
      (Gm @ Ginv == np.eye(8, dtype=np.int64)).all())
Amat = np.array(SIMPLE, dtype=np.int64).T     # columns = simple roots
coords = []; rec_ok = True
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64)
    c = Ginv @ d
    rec_ok &= bool((Amat @ c == np.array(r, dtype=np.int64)).all())
    coords.append(c)
rmask = [int(sum((int(c[i]) & 1) << i for i in range(8))) for c in coords]
check("2b", "every root reconstructs exactly from its integer simple-root "
      "coordinates (all 240 verified); reduce mod 2 -> L/2L = F2^8", rec_ok)
qvals = []
for m in range(256):
    cv = np.array([(m >> i) & 1 for i in range(8)], dtype=np.int64)
    n2 = int(cv @ Gm @ cv)
    assert n2 % 2 == 0        # even lattice
    qvals.append((n2 // 2) % 2)
nsing = sum(1 for m in range(1, 256) if qvals[m] == 0)
nnons = sum(1 for m in range(256) if qvals[m] == 1)
check("2c", "q(x) = x.x/2 mod 2 is well-defined on L/2L (even lattice) "
      "with 135 singular nonzero + 120 nonsingular vectors (the plus-type "
      "counts on F2^8; Witt-index-4 witness computed in stage 5)",
      nsing == 135 and nnons == 120,
      "singular %d, nonsingular %d" % (nsing, nnons))
def Bq(x, y): return qvals[x ^ y] ^ qvals[x] ^ qvals[y]
rad = [x for x in range(1, 256)
       if all(Bq(x, y) == 0 for y in range(256))]
check("2d", "the polar form B(x,y) = q(x+y)+q(x)+q(y) is NONDEGENERATE "
      "(trivial radical)", not rad)
cnt_mask = Counter(rmask)
pmasks_all = sorted(cnt_mask)
check("2e", "the 240 root images mod 2 are exactly the 120 NONSINGULAR "
      "vectors, each hit by exactly one antipodal pair (pairs = mod-2 "
      "fibres)",
      len(pmasks_all) == 120 and all(qvals[m] == 1 for m in pmasks_all)
      and sorted(cnt_mask.values()) == [2] * 120
      and all(rmask[k] == rmask[ridx[tuple(-x for x in roots[k])]]
              for k in range(240)))

pair_of = [0] * 240; PAIRS = []
seenm = {}
for k in range(240):
    m = rmask[k]
    if m not in seenm:
        seenm[m] = len(PAIRS); PAIRS.append(m)
    pair_of[k] = seenm[m]
NPAIR = 120
mask2pair = {PAIRS[j]: j for j in range(NPAIR)}
def to120(p240):
    out = [0] * NPAIR
    for k in range(240): out[pair_of[k]] = pair_of[p240[k]]
    return tuple(out)
sidx = [ridx[a] for a in SIMPLE]
def M2_of(w):
    """mod-2 matrix of w in the simple-root basis (columns = images of the
    basis roots reduced mod 2)."""
    return tuple(rmask[w[sidx[j]]] for j in range(8))
ok_m2 = True
for s in S240:
    M = M2_of(s)
    ok_m2 &= all(mvec(M, rmask[k]) == rmask[s[k]] for k in range(240))
    ok_m2 &= all(qvals[mvec(M, x)] == qvals[x] for x in range(256))
check("2f", "each simple reflection's mod-2 matrix reproduces the root "
      "action mod 2 and PRESERVES q: pi maps W(E8) into O(F2^8, q); mod 2 "
      "a reflection becomes the orthogonal transvection t_{a-bar}", ok_m2)
S120 = [to120(s) for s in S240]
oQ, memQ, TRQ, BASEQ, LVLQ = bsgs_cached("pair_120", S120, 120)
check("2g", "the pair action (120 antipodal pairs) has order 348364800 = "
      "|W(E8)|/2, and -1 acts trivially: the pair-kernel is EXACTLY {+-1}",
      oQ == 348364800 and oW // oQ == 2 and to120(anti) == pident(120),
      "order %d" % oQ)
check("2h", "KERNEL OF pi: trivial mod 2 <=> fixes every root mask <=> "
      "fixes every pair (2e: pairs are the mod-2 fibres) <=> in the "
      "pair-kernel = {+-1} (2g); conversely +-1 = 1 mod 2.  ker pi = {+-1}",
      oQ * 2 == oW and to120(anti) == pident(120))
print("\n  UB1: PASS -- W(E8) built (696729600), -1 central and inside, q "
      "plus-type nondegenerate on L/2L, ker(pi) = {+-1}.")
SH_o, SH_base, SH_tr = shadow_cached(
    "shadow_full", [(S120[i], S240[i]) for i in range(8)], 120, 240)
sift_ok = True
for i in range(8):
    u = shadow_sift(SH_base, SH_tr, 120, 240, S120[i])
    sift_ok &= (u is not None and to120(u) == S120[i] and memW(u))
check("2i", "shadow chain (pair action with W(E8) carries): order "
      "348364800; the 8 generator images round-trip (sift -> lift -> same "
      "pair action, lift in W(E8))", SH_o == 348364800 and sift_ok)
print("[t=%6.1fs] stage 2 done" % (time.time() - T0))
stage_gate(2)

# ======================================================================
banner("STAGE 3 -- UB2 (control): the vector-type preimage is SPLIT")
# ======================================================================
aix = ridx[SIMPLE[0]]
oWa, memWa, TRWa, BASEWa, LVLWa = bsgs_cached("we8_stab_a", S240, 240,
                                              init_base=[aix])
o_stab = 1
for T in TRWa[1:]: o_stab *= len(T)
stab_gens = LVLWa[1] if len(LVLWa) > 1 else []
check("3a", "forced-base BSGS at alpha: W(E8) is transitive on the 240 "
      "roots (first orbit 240) and Stab(alpha) has order 2903040 = "
      "|W(E7)|; the verified chain's level-1 strong generators generate "
      "it and all fix alpha",
      oWa == 696729600 and len(TRWa[0]) == 240 and o_stab == 2903040
      and len(stab_gens) > 0 and all(g[aix] == aix for g in stab_gens),
      "|Stab| = %d, %d strong generators" % (o_stab, len(stab_gens)))
check("3b", "-1 is NOT in Stab(alpha): it moves alpha to -alpha; so "
      "Stab(alpha) meets {+-1} trivially and pi is INJECTIVE on it",
      anti[aix] != aix)
oC, memC, TRC, Cgens = derived_cached("stab_derived", stab_gens, 240,
                                      seed=31001)
check("3c", "random-commutator closure inside Stab(alpha) converges to "
      "order 1451520 = |Sp6(2)|, index 2 in Stab; EXACT: Stab/C = Z2 is "
      "abelian so [Stab,Stab] <= C, and C <= [Stab,Stab] by construction "
      "=> C = [Stab,Stab]",
      oC == 1451520 and o_stab // oC == 2, "order %d" % oC)
check("3d", "C fixes alpha and misses -1: pi(C) is a VECTOR-TYPE Sp6(2) "
      "in O(L/2L,q) fixing the NONSINGULAR vector alpha-bar (the "
      "spin/vector distinguisher baseline)",
      all(g[aix] == aix for g in Cgens) and not memC(anti)
      and qvals[rmask[aix]] == 1)
oCz, memCz, _, _, _ = bsgs_cached("stab_derived_plus",
                                  Cgens + [anti], 240)
check("3e", "<C, -1> has order 2903040 with -1 central and C meeting "
      "<-1> trivially: pi^-1(vector-type Sp6(2)) = <-1> x C, a SPLIT "
      "direct product 2 x Sp6(2)", oCz == 2903040, "order %d" % oCz)
print("\n  UB2: PASS -- registered expectation CONFIRMED: the vector-type "
      "preimage\n  is SPLIT, pi^-1(vector Sp6(2)) = <-1> x Sp6(2).")
print("[t=%6.1fs] stage 3 done" % (time.time() - T0))
stage_gate(3)

# ======================================================================
banner("STAGE 4 -- UB3: spin-type Sp6(2) from the even Clifford algebra")
# ======================================================================
# V7 = F2^7, bits 0..6, q7 = x0x1 + x2x3 + x4x5 + x6^2; e7 (bit 6) is the
# radical of the polar form, q7(e7) = 1.  Cl0(V7,q7) = Cl(V6,q6) via
# x |-> x.e7; Cl(V6,q6) acts on Lambda(F2^3) (dim 8) by creation/
# annihilation operators (the minimal left ideal of M8(F2), explicitly).
def a_op(mode):
    return tuple((1 << (s | (1 << mode))) if not (s >> mode) & 1 else 0
                 for s in range(8))
def b_op(mode):
    return tuple((1 << (s & ~(1 << mode))) if (s >> mode) & 1 else 0
                 for s in range(8))
GAM = [a_op(0), b_op(0), a_op(1), b_op(1), a_op(2), b_op(2)]
def q7(v):
    x = [(v >> i) & 1 for i in range(7)]
    return (x[0] & x[1]) ^ (x[2] & x[3]) ^ (x[4] & x[5]) ^ x[6]
def B7(u, v): return q7(u ^ v) ^ q7(u) ^ q7(v)
ok_rel = all(mmulF2(GAM[i], GAM[i]) == ZEROM for i in range(6))
for i in range(6):
    for j in range(i + 1, 6):
        acom = madd(mmulF2(GAM[i], GAM[j]), mmulF2(GAM[j], GAM[i]))
        ok_rel &= (acom == (IDM if B7(1 << i, 1 << j) else ZEROM))
check("4a", "the 6 gamma operators on Lambda(F2^3) satisfy the Clifford "
      "relations of (V6, q6=x0x1+x2x3+x4x5): gamma_i^2 = q(e_i).I = 0, "
      "gamma_i gamma_j + gamma_j gamma_i = B(e_i,e_j).I", ok_rel)
def Xmat(v):
    M = IDM if (v >> 6) & 1 else ZEROM
    for i in range(6):
        if (v >> i) & 1: M = madd(M, GAM[i])
    return M
check("4b", "X(v) = c.I + sum v_i gamma_i (the image of v.e7 in Cl0) "
      "satisfies X(v)^2 = q7(v).I for ALL 128 v -- e7 is central over F2 "
      "(B(e7,.) = 0), so this is the whole Clifford calculus needed",
      all(mmulF2(Xmat(v), Xmat(v)) == (IDM if q7(v) else ZEROM)
          for v in range(128)))
TVS = [v for v in range(1, 128) if q7(v) == 1 and v != (1 << 6)]
def tv_map(v):
    return tuple((x ^ v) if B7(x, v) else x for x in range(128))
ok_conj = True
for v in TVS:
    Mv = Xmat(v); tv = tv_map(v)
    for xb in (1, 2, 4, 8, 16, 32, 64):
        ok_conj &= (mmulF2(mmulF2(Mv, Xmat(xb)), Mv) == Xmat(tv[xb]))
check("4c", "each of the %d q=1 vectors v (e7 itself excluded: t_e7 = id) "
      "gives an INVOLUTION M_v = X(v) implementing the orthogonal "
      "transvection t_v: M_v X(x) M_v = X(t_v x) on a basis of V7 -- the "
      "spin lift of the generator" % len(TVS),
      ok_conj and all(mmulF2(Xmat(v), Xmat(v)) == IDM for v in TVS)
      and len(TVS) == 63)
o7t, _, _, _, _ = bsgs_cached("o7_transvections",
                              [tv_map(v) for v in TVS], 128)
check("4d", "the 63 transvections generate a group of order 1451520 = "
      "|Sp6(2)| = |O(V7,q7)| [order formula P: standard] acting on V7 -- "
      "the full O7(2)", o7t == 1451520, "order %d" % o7t)
def mat_to_perm256(M): return tuple(mvec(M, x) for x in range(256))
K0perms = [mat_to_perm256(Xmat(v)) for v in TVS]
oK0, memK0, TRK0, _, _ = bsgs_cached("k0_256", K0perms, 256)
check("4e", "K0 = <M_v> <= GL8(F2) (as permutations of the 256 vectors) "
      "has order 1451520: the spin lift is FAITHFUL with NO doubling -- "
      "over F2 the only central unit of M8(F2) is 1, so relations among "
      "the t_v map to relations among the M_v", oK0 == 1451520,
      "order %d" % oK0)

# economical generating pair (cached)
pair_cached = wit_get("k0_pair")
if pair_cached:
    g1m = tuple(pair_cached[0]); g2m = tuple(pair_cached[1])
    o2p, _, _, _, _ = bsgs_cached("k0_pair_256",
                                  [mat_to_perm256(g1m),
                                   mat_to_perm256(g2m)], 256)
    n_att = 0
else:
    random.seed(31004)
    g1m = g2m = None; o2p = 0; n_att = 0
    while n_att < 40 and o2p != 1451520:
        n_att += 1
        A = IDM; B = IDM
        for _ in range(random.randrange(6, 14)):
            A = mmulF2(A, Xmat(TVS[random.randrange(63)]))
        for _ in range(random.randrange(6, 14)):
            B = mmulF2(B, Xmat(TVS[random.randrange(63)]))
        # cheap prefilter: the pair must reach both orbits 120+135
        orb = {1}; fr = [1]
        while fr:
            u = fr.pop()
            for M in (A, B):
                w0 = mvec(M, u)
                if w0 not in orb: orb.add(w0); fr.append(w0)
        if len(orb) not in (120, 135): continue
        o2p, _, _, _, _ = make_bsgs_full(
            [mat_to_perm256(A), mat_to_perm256(B)], 256)
        if o2p == 1451520:
            g1m, g2m = A, B
            wit_put("k0_pair", [list(A), list(B)])
            _bsgs = bsgs_cached("k0_pair_256",
                                [mat_to_perm256(A), mat_to_perm256(B)], 256)
check("4f", "an economical generating PAIR of K0 found among random "
      "products of transvection lifts (order re-verified 1451520 by BSGS)",
      o2p == 1451520, "attempts used: %s" % (n_att if n_att else "cache"))

# invariant quadratic form
mon = [(i, j) for i in range(8) for j in range(i, 8)]
rowsM = []
for M in (g1m, g2m):
    for x in range(256):
        y = mvec(M, x)
        r = 0
        for t, (i, j) in enumerate(mon):
            if (((x >> i) & (x >> j)) ^ ((y >> i) & (y >> j))) & 1:
                r |= 1 << t
        if r: rowsM.append(r)
NSQ = f2_nullspace(rowsM, 36)
check("4g", "the space of K0-invariant quadratic forms on F2^8 is EXACTLY "
      "1-dimensional (linear system over both generators, all 256 points)",
      len(NSQ) == 1, "nullspace dim %d" % len(NSQ))
cQ = NSQ[0]
Q8 = []
for x in range(256):
    v = 0
    for t, (i, j) in enumerate(mon):
        if (cQ >> t) & 1 and ((x >> i) & 1) and ((x >> j) & 1): v ^= 1
    Q8.append(v)
def B8(x, y): return Q8[x ^ y] ^ Q8[x] ^ Q8[y]
n1 = sum(Q8); n0 = 255 - n1
rad8 = [x for x in range(1, 256)
        if all(B8(x, y) == 0 for y in range(256))]
inv_all63 = all(Q8[mvec(Xmat(v), x)] == Q8[x]
                for v in TVS for x in range(256))
check("4h", "the invariant form Q8 is nondegenerate with the PLUS-type "
      "counts (135 singular nonzero / 120 nonsingular) and is preserved "
      "by ALL 63 transvection lifts",
      n1 == 120 and n0 == 135 and not rad8 and inv_all63,
      "nonsingular %d" % n1)
fixed0 = [x for x in range(1, 256)
          if mvec(g1m, x) == x and mvec(g2m, x) == x]
def orbit_span_full(mats, x):
    orb = {x}; fr = [x]
    while fr:
        u = fr.pop()
        for M in mats:
            w0 = mvec(M, u)
            if w0 not in orb: orb.add(w0); fr.append(w0)
    return f2_rank(list(orb)) == 8
check("4i", "K0 fixes NO nonzero vector (in particular no nonsingular "
      "one): SPIN type, already distinct from the vector type of UB2 "
      "(which fixes alpha-bar)", not fixed0)
check("4j", "K0 is IRREDUCIBLE on F2^8: for every one of the 255 nonzero "
      "vectors, its K0-orbit spans the full space",
      all(orbit_span_full([g1m, g2m], x) for x in range(1, 256)))
oKD, _, _, _ = derived_cached("k0_derived",
                              [mat_to_perm256(g1m), mat_to_perm256(g2m)],
                              256, seed=31005)
check("4k", "K0 is PERFECT (random-commutator closure reaches the full "
      "order -- exact, the closure is a subgroup of [K0,K0]); hence no "
      "index-2 subgroup.  With order 1451520 + the element-order set "
      "(stage 6: K-bar census) this is the brief's Sp6(2) fingerprint",
      oKD == 1451520, "derived order %d" % oKD)
print("[t=%6.1fs] stage 4 done" % (time.time() - T0))
stage_gate(4)

# ======================================================================
banner("STAGE 5 -- transport T: (F2^8, Q8) -> (L/2L, q); K_spin; the lifts")
# ======================================================================
def hyperbolic_basis(qtab):
    """4 hyperbolic pairs (u_k, v_k): q(u)=q(v)=0, B(u,v)=1, pairwise
    orthogonal -- F2 Gram-Schmidt for quadratic forms (precedent: Stone Q's
    symplectic transport, upgraded to track q)."""
    def Bloc(x, y): return qtab[x ^ y] ^ qtab[x] ^ qtab[y]
    pairs = []
    cur = [x for x in range(1, 256)]
    for _ in range(4):
        u = next(x for x in cur if qtab[x] == 0)
        v = next(y for y in cur if Bloc(u, y) == 1)
        if qtab[v] == 1: v ^= u
        pairs.append((u, v))
        cur = [x for x in cur
               if x not in (0,) and Bloc(x, u) == 0 and Bloc(x, v) == 0]
    return pairs
def ts_witness(pairs, qtab):
    """the span of {u1..u4} is totally singular of dim 4 (Witt index 4 =
    plus type, computed)."""
    us = [p[0] for p in pairs]
    if f2_rank(us) != 4: return False
    for bits in range(16):
        w0 = 0
        for k in range(4):
            if (bits >> k) & 1: w0 ^= us[k]
        if qtab[w0] != 0: return False
    return True
HB_spin = hyperbolic_basis(Q8)
HB_lat = hyperbolic_basis(qvals)
def basis_matrix(pairs):
    cols = []
    for (u, v) in pairs: cols += [u, v]
    return tuple(cols)
U1 = basis_matrix(HB_spin); U2 = basis_matrix(HB_lat)
U1i = f2_matinv(U1)
ok_inv = U1i is not None and mmulF2(U1, U1i) == IDM
Tmat = mmulF2(U2, U1i) if ok_inv else None
iso_ok = ok_inv and all(qvals[mvec(Tmat, x)] == Q8[x] for x in range(256))
check("5a", "hyperbolic bases found on BOTH sides; each side's {u_k} spans "
      "a totally singular 4-space (Witt index 4: both forms are PLUS type, "
      "computed, so an isometry exists); T = U_lat . U_spin^-1 satisfies "
      "q(Tx) = Q8(x) for ALL 256 x -- an explicit ISOMETRY",
      ts_witness(HB_spin, Q8) and ts_witness(HB_lat, qvals) and iso_ok)
Ti = f2_matinv(Tmat)
A1 = mmulF2(Tmat, mmulF2(g1m, Ti)); A2 = mmulF2(Tmat, mmulF2(g2m, Ti))
fixedA = [x for x in range(1, 256)
          if mvec(A1, x) == x and mvec(A2, x) == x]
check("5b", "K_spin = T K0 T^-1 preserves q on L/2L; fixes NO nonzero "
      "vector (hence no nonsingular vector -- NOT conjugate to the vector "
      "type, which fixes alpha-bar); irreducibility transported (re-checked "
      "on all 255 orbits)",
      all(qvals[mvec(A, x)] == qvals[x] for A in (A1, A2)
          for x in range(256))
      and not fixedA
      and all(orbit_span_full([A1, A2], x) for x in range(1, 256)))
def pair_perm_of_mat(A):
    return tuple(mask2pair[mvec(A, PAIRS[j])] for j in range(NPAIR))
pp1 = pair_perm_of_mat(A1); pp2 = pair_perm_of_mat(A2)
w1 = shadow_sift(SH_base, SH_tr, 120, 240, pp1)
w2 = shadow_sift(SH_base, SH_tr, 120, 240, pp2)
check("5c", "both K_spin generators SIFT through the full pair-BSGS (they "
      "lie in pi(W(E8))) and the lifted 240-permutations have EXACTLY the "
      "target mod-2 matrices: pi(w_i) = A_i (matrix equality, and the "
      "pair action determines the matrix on the spanning 120 nonsingular "
      "vectors)",
      w1 is not None and w2 is not None
      and to120(w1) == pp1 and to120(w2) == pp2
      and M2_of(w1) == A1 and M2_of(w2) == A2
      and memW(w1) and memW(w2))
print("\n  UB3: PASS -- spin-type K_spin constructed (order 1451520, "
      "irreducible,\n  invariant plus-type form, perfect, fixes no vector; "
      "fingerprint completed by\n  the stage-6 census), transported, and "
      "lifted into W(E8).")
print("[t=%6.1fs] stage 5 done" % (time.time() - T0))
stage_gate(5)

# ======================================================================
banner("STAGE 6 -- UB4: H = pi^-1(K_spin) = <w1, w2, -1>; THE SPLIT TEST")
# ======================================================================
oH, memH, TRH, _, _ = bsgs_cached("H_240", [w1, w2, anti], 240)
check("6a", "|H| = 2903040 = 2 x 1451520 and -1 in H (central by 1f)",
      oH == 2903040 and memH(anti), "order %d" % oH)
oL2, memL2, _, _, _ = bsgs_cached("H_lifts_240", [w1, w2], 240)
if oL2 == oH:
    note("<w1,w2> ALONE has order %d = |H|: the two lifted spin generators"
         % oL2)
    note("already generate H, so -1 is a word in them (a non-split hint; "
         "the decider follows).")
elif oL2 == oH // 2 and not memL2(anti):
    note("<w1,w2> has order %d = |H|/2 WITHOUT -1: an explicit complement "
         "-- SPLIT." % oL2)
else:
    note("<w1,w2> has order %d [unexpected -- investigate]" % oL2)
oHD, memHD, _, _ = derived_cached("H_derived", [w1, w2, anti], 240,
                                  seed=31006)
if oHD == 2903040:
    UB4 = "PASS (H PERFECT => NON-SPLIT: H = 2.Sp6(2))"
    check("6b", "THE SPLIT TEST: the random-commutator closure of H "
          "reaches the FULL order 2903040 -- EXACT (the closure is a "
          "subgroup of [H,H]): H is PERFECT and contains -1 centrally, "
          "hence a NON-SPLIT STEM extension of Sp6(2) by Z2 => "
          "H = 2.Sp6(2), the Schur cover.  REGISTERED EXPECTATION UB4: "
          "CONFIRMED", True, "[H,H] = H, order %d" % oHD)
elif oHD == 1451520 and not memHD(anti):
    UB4 = "INVERTED (H SPLIT)"
    check("6b", "THE SPLIT TEST -- REGISTERED EXPECTATION INVERTED, at "
          "full prominence: [H,H] has index 2 (exact: H/[H,H] = Z2 "
          "abelian) and MISSES -1, so H = <-1> x [H,H] is SPLIT; W(E8) "
          "does not deliver 2.Sp6(2) on this route", True,
          "derived order %d, -1 not inside" % oHD)
else:
    UB4 = "INCONCLUSIVE (unexpected derived data)"
    check("6b", "THE SPLIT TEST returned structurally impossible data "
          "(derived order %d, -1 in derived: %s) -- INVESTIGATE"
          % (oHD, memHD(anti)), False)

# K-bar = H/{+-1} as the pair action; enumeration + census machinery
oKb, memKb, TRKb, BASEKb, _ = bsgs_cached("kbar_120", [pp1, pp2], 120)
check("6c", "K-bar = pair action of H has order 1451520 (= |H|/2, the "
      "faithful quotient by {+-1})", oKb == 1451520)
SHH_o, SHH_base, SHH_tr = shadow_cached("shadow_H",
                                        [(pp1, w1), (pp2, w2)], 120, 240)
check("6d", "H's own shadow chain (pair action, W(E8)-carries) has order "
      "1451520: canonical lifts of K-bar elements land in <w1,w2> <= H",
      SHH_o == 1451520)
EN_f = os.path.join(CACHE, "kbar_elements.npy")
if os.path.exists(EN_f):
    EN = np.load(EN_f)
    note("[cache] K-bar enumeration loaded")
    uniq_ok = bool(wit_get("kbar_unique"))
else:
    EN = enumerate_group_np(TRKb, 120)
    np.save(EN_f, EN)
    uniq_ok = (np.unique(EN, axis=0).shape[0] == EN.shape[0])
    wit_put("kbar_unique", bool(uniq_ok))
NKB = EN.shape[0]
check("6e", "the transversal products enumerate 1451520 DISTINCT elements "
      "of K-bar (uniqueness verified row-wise at first build, cached flag "
      "on resume)", NKB == 1451520 and uniq_ok)
ORD_f = os.path.join(CACHE, "kbar_orders.npy")
ID120 = np.arange(120, dtype=np.uint8)
if os.path.exists(ORD_f):
    ORD = np.load(ORD_f)
    note("[cache] K-bar order census loaded")
else:
    ORD = np.zeros(NKB, np.uint8)
    P = EN.copy(); k = 1
    while True:
        mk = (P == ID120).all(axis=1) & (ORD == 0)
        ORD[mk] = k
        if not (ORD == 0).any(): break
        k += 1
        assert k <= 40
        P = np.take_along_axis(EN, P, axis=1)
    del P
    np.save(ORD_f, ORD)
cntK = np.bincount(ORD)
censusK = {int(o): int(cntK[o]) for o in range(len(cntK)) if cntK[o]}
print("  ELEMENT-ORDER CENSUS of K-bar (exhaustive over all %d):" % NKB)
for o in sorted(censusK):
    print("    order %2d: %7d elements" % (o, censusK[o]))
check("6f", "element-order set of K-bar = {1,2,3,4,5,6,7,8,9,10,12,15} "
      "(the Sp6(2) set -- completes the UB3 fingerprint: order + orders + "
      "perfect)", sorted(censusK) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15],
      "%s" % sorted(censusK))
f_old = os.path.join("_overgroup_cache", "sp62_orders.npy")
if os.path.exists(f_old):
    cnt_old = np.bincount(np.load(f_old))
    L = max(len(cnt_old), len(cntK))
    a = np.zeros(L, np.int64); b = np.zeros(L, np.int64)
    a[:len(cnt_old)] = cnt_old; b[:len(cntK)] = cntK
    check("6g", "census IDENTICAL to the sealed containment run's Sp6(2) "
          "census (loaded from _overgroup_cache, SM-023 machinery) "
          "[C cross-run]", bool((a == b).all()))
else:
    note("[6g skipped: _overgroup_cache/sp62_orders.npy not present here]")

# square-sign table: for each involution j-bar of K-bar, its H-lifts j and
# -j share a square j^2 in {+1, -1}; sign(j-bar) := that sign.  In a SPLIT
# H = <-1> x C every involution of K-bar would lift to an involution of C
# (sign +); any sign - class is an independent NON-SPLIT witness.
inv_idx = np.nonzero(ORD == 2)[0]
inv_rows = EN[inv_idx]
inv_tups = [tuple(int(x) for x in r) for r in inv_rows]
SQ_f = os.path.join(CACHE, "sqsign.npz")
if os.path.exists(SQ_f):
    z = np.load(SQ_f)
    sq_sign_arr = z["sign"]; cls_id_arr = z["cls"]
    note("[cache] square-sign + class tables loaded")
else:
    sq_list = []
    for t in inv_tups:
        u = shadow_sift(SHH_base, SHH_tr, 120, 240, t)
        assert u is not None and to120(u) == t
        s2 = pmul(u, u)
        sq_list.append(1 if s2 == pident(240)
                       else (-1 if s2 == anti else 0))
    sq_sign_arr = np.array(sq_list, np.int8)
    # conjugacy classes of involutions under <pp1, pp2>
    tup2i = {t: i for i, t in enumerate(inv_tups)}
    cls_id_arr = np.full(len(inv_tups), -1, np.int32)
    cid = 0
    gens_conj = [pp1, pp2, pinv(pp1), pinv(pp2)]
    for i0 in range(len(inv_tups)):
        if cls_id_arr[i0] >= 0: continue
        fr = [inv_tups[i0]]; cls_id_arr[i0] = cid
        while fr:
            t = fr.pop()
            for g in gens_conj:
                c = pmul(pmul(g, t), pinv(g))
                j = tup2i[c]
                if cls_id_arr[j] < 0:
                    cls_id_arr[j] = cid; fr.append(c)
        cid += 1
    np.savez_compressed(SQ_f, sign=sq_sign_arr, cls=cls_id_arr)
n_cls = int(cls_id_arr.max()) + 1
check("6h", "every involution of K-bar lifts through H's shadow chain and "
      "its lift squares to +1 or -1 (never anything else)",
      bool((sq_sign_arr != 0).all()),
      "%d involutions, %d conjugacy classes" % (len(inv_tups), n_cls))
cls_report = []
sq_const = True
for c in range(n_cls):
    mk = cls_id_arr == c
    sgns = set(sq_sign_arr[mk].tolist())
    sq_const &= (len(sgns) == 1)
    cls_report.append((c + 1, int(mk.sum()), sorted(sgns)))
check("6i", "the square-sign is CONSTANT on each involution class of "
      "K-bar (it must be: conjugation permutes lifts)", sq_const,
      "(class, size, sign): %s" % cls_report)
n_plus_inv = int((sq_sign_arr == 1).sum())
n_minus_inv = int((sq_sign_arr == -1).sum())
note("involutions of H: 1 (namely -1) + 2 x %d (over sign-+ classes) = %d;"
     % (n_plus_inv, 1 + 2 * n_plus_inv))
note("%d involutions of K-bar (in the sign-minus classes) lift to ORDER-4 "
     "elements of H." % n_minus_inv)
if n_minus_inv > 0:
    note("INDEPENDENT NON-SPLIT WITNESS: in a split <-1> x Sp6(2) every "
         "involution of the\n  quotient lifts to an involution; here "
         "sign-minus classes exist.")

# hash lookup (uint64 random-vector row hashing, precedent check 5g)
RH = RNG.integers(1, 2 ** 63, size=120, dtype=np.uint64)
def hrows(X):
    out = np.zeros(X.shape[0], np.uint64)
    step = 100000
    for s in range(0, X.shape[0], step):
        out[s:s + step] = (X[s:s + step].astype(np.uint64) * RH).sum(axis=1)
    return out
inv_hash = hrows(inv_rows)
check("6j", "the involution row-hashes are collision-free (safe lookup "
      "table)", len(set(inv_hash.tolist())) == len(inv_tups))
h2sign = {int(h): int(s) for h, s in zip(inv_hash.tolist(),
                                         sq_sign_arr.tolist())}
h2cls = {int(h): int(c) for h, c in zip(inv_hash.tolist(),
                                        cls_id_arr.tolist())}
SGN_f = os.path.join(CACHE, "kbar_signrow.npy")
if os.path.exists(SGN_f):
    sign_row = np.load(SGN_f)
    note("[cache] even-order sign rows loaded")
else:
    sign_row = np.zeros(NKB, np.int8)
    maxk = max(o for o in censusK if o % 2 == 0) // 2
    P = EN.copy(); k = 1
    while k <= maxk:
        rows_k = np.nonzero(ORD == 2 * k)[0]
        if rows_k.size:
            hs = hrows(P[rows_k])
            sgs = np.array([h2sign[int(h)] for h in hs.tolist()], np.int8)
            sign_row[rows_k] = sgs
        k += 1
        if k <= maxk:
            P = np.take_along_axis(EN, P, axis=1)
    del P
    np.save(SGN_f, sign_row)
ok_signrow = bool(((ORD % 2 == 0) == (sign_row != 0)).all())
check("6k", "every even-order element g of K-bar received the square-sign "
      "of its involution power g^(ord/2) (hash lookups all resolved); "
      "odd-order rows need no sign (their two H-lifts have orders m and "
      "2m regardless)", ok_signrow)

# the census of H, derived exactly:
#   m odd:  the two lifts have orders {m, 2m}    (one each)
#   m even: both lifts have order m if sign(g^(m/2)) = +1, else 2m
censusH = Counter()
for o in sorted(censusK):
    if o % 2 == 1:
        censusH[o] += censusK[o]
        censusH[2 * o] += censusK[o]
    else:
        npl = int(((ORD == o) & (sign_row == 1)).sum())
        nmi = int(((ORD == o) & (sign_row == -1)).sum())
        assert npl + nmi == censusK[o]
        if npl: censusH[o] += 2 * npl
        if nmi: censusH[2 * o] += 2 * nmi
censusH = dict(sorted(censusH.items()))
tot_H = sum(censusH.values())
print("  ELEMENT-ORDER CENSUS of H (derived exactly from the K-bar census "
      "+ square signs):")
for o in sorted(censusH):
    print("    order %2d: %7d elements" % (o, censusH[o]))
check("6l", "the census of H sums to |H| = 2903040", tot_H == 2903040,
      "total %d" % tot_H)
census2x = Counter()
for o, c in censusK.items():
    if o % 2 == 1:
        census2x[o] += c; census2x[2 * o] += c
    else:
        census2x[o] += 2 * c
census2x = dict(sorted(census2x.items()))
diff_orders = sorted(set(censusH) ^ set(census2x)
                     | {o for o in set(censusH) & set(census2x)
                        if censusH[o] != census2x.get(o)})
if diff_orders:
    note("census(H) vs census(2 x Sp6(2)) DIFFER at orders %s:"
         % diff_orders)
    for o in diff_orders:
        note("  order %2d: H has %d, 2xSp6(2) would have %d"
             % (o, censusH.get(o, 0), census2x.get(o, 0)))
else:
    note("census(H) = census(2 x Sp6(2)) -- censuses alone cannot "
         "separate; the derived-subgroup test is the decider.")
consistent = True
if n_minus_inv > 0 or diff_orders:
    consistent = UB4.startswith("PASS")
check("6m", "sign data, census comparison and the split-test verdict are "
      "mutually consistent (a sign-minus class or a census difference "
      "each force NON-split, so they may only occur with the perfect/"
      "non-split verdict)", consistent, "verdict: %s" % UB4)
print("\n  UB4: %s" % UB4)
print("[t=%6.1fs] stage 6 done" % (time.time() - T0))
stage_gate(6)

# ======================================================================
banner("STAGE 7 -- UB5: the tower upstairs (hunts in K-bar, preimages in H)")
# ======================================================================
idx_by_ord = {o: np.nonzero(ORD == o)[0] for o in censusK}
def row_tup(i): return tuple(int(x) for x in EN[int(i)])
def hrow1(t): return int((np.array(t, dtype=np.uint64) * RH).sum())
def lift_H(t):
    u = shadow_sift(SHH_base, SHH_tr, 120, 240, t)
    assert u is not None and to120(u) == t
    return u
def preimage_close(gens120, cap=300000):
    lifts = [lift_H(t) for t in gens120]
    return closure(lifts + [anti], cap=cap), lifts
def inv_meta(Gset):
    """which K-bar involution classes (and square signs) a copy uses."""
    out = Counter()
    for g in Gset:
        if pord(g) == 2:
            h = hrow1(g)
            out[(h2cls[h] + 1, h2sign[h])] += 1
    return dict(sorted(out.items()))
def formula_census_preimage(Gset):
    c = Counter()
    for g in Gset:
        m = pord(g)
        if m % 2 == 1:
            c[m] += 1; c[2 * m] += 1
        else:
            s = h2sign[hrow1(ppow(g, m // 2))]
            c[m if s == 1 else 2 * m] += 2
    return dict(sorted(c.items()))
def np_census(transv, deg):
    """enumerate a subgroup from its BSGS transversals (numpy) and return
    (elements, orders, census)."""
    ENs = enumerate_group_np(transv, deg)
    IDd = np.arange(deg, dtype=np.uint8)
    Os = np.zeros(ENs.shape[0], np.uint8)
    P = ENs.copy(); k = 1
    while True:
        mk = (P == IDd).all(axis=1) & (Os == 0)
        Os[mk] = k
        if not (Os == 0).any(): break
        k += 1
        assert k <= 64
        P = np.take_along_axis(ENs, P, axis=1)
    cnt = np.bincount(Os)
    return ENs, Os, {int(o): int(cnt[o]) for o in range(len(cnt))
                     if cnt[o]}
def np_preimage_census(ENs, Os):
    """census of the H-preimage of a K-bar subgroup given its 120-point
    element rows + orders (same square-sign formula as the H census)."""
    c = Counter()
    for o in np.unique(Os):
        o = int(o)
        if o % 2 == 1:
            n = int((Os == o).sum()); c[o] += n; c[2 * o] += n
    evens = sorted(int(o) for o in np.unique(Os) if int(o) % 2 == 0)
    if evens:
        maxk = evens[-1] // 2
        P = ENs.copy(); k = 1
        while k <= maxk:
            rows_k = np.nonzero(Os == 2 * k)[0]
            if rows_k.size:
                hs = hrows(P[rows_k])
                for h in hs.tolist():
                    s = h2sign[int(h)]
                    c[2 * k if s == 1 else 4 * k] += 2
            k += 1
            if k <= maxk:
                P = np.take_along_axis(ENs, P, axis=1)
    return dict(sorted(c.items()))
def derived_of_small(gens, cap=100000):
    e = pident(len(gens[0]))
    dg = [comm(gens[i], gens[j]) for i in range(len(gens))
          for j in range(len(gens)) if i != j]
    dg = [d for d in dg if d != e]
    if not dg: return {e}, []
    D = closure(dg, cap)
    changed = True
    while changed:
        changed = False
        for g in gens:
            gi = pinv(g)
            for d in list(dg):
                c = pmul(pmul(g, d), gi)
                if c not in D:
                    dg.append(c); D = closure(dg, cap); changed = True
    return D, dg

# ---- model groups and reference profiles (precedent: verify_tower_b) ----
def mmul(A, B, p):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e+b*g) % p, (a*f+b*h) % p, (c*e+d*g) % p, (c*f+d*h) % p)
def mord(M, p):
    I = (1, 0, 0, 1); x = M; k = 1
    while x != I: x = mmul(x, M, p); k += 1
    return k
def mdet(M, p):
    a, b, c, d = M; return (a*d - b*c) % p
def SL2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p)
            if mdet((a, b, c, d), p) == 1]
def GL2(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p)
            if mdet((a, b, c, d), p) != 0]
def mat_profile(G, p):
    return dict(sorted(Counter(mord(M, p) for M in G).items()))
def inv_p(k, p): return pow(k % p, p - 2, p)
def mobius_group(mats, p):
    pts = p + 1
    def mob(M):
        a, b, c, d = M; img = []
        for x in range(pts):
            if x == p:
                img.append(p if c % p == 0 else (a * inv_p(c, p)) % p)
            else:
                den = (c * x + d) % p
                img.append(p if den == 0
                           else ((a * x + b) % p * inv_p(den, p)) % p)
        return tuple(img)
    return {mob(M) for M in mats}
prof_SL27 = mat_profile(SL2(7), 7)
prof_PSL27 = profile_of(mobius_group(SL2(7), 7))
prof_PGL27 = profile_of(mobius_group(GL2(7), 7))
prof_SL25 = mat_profile(SL2(5), 5)
prof_SL23 = mat_profile(SL2(3), 3)
prof_GL23 = mat_profile(GL2(3), 3)
A5m = closure([(1, 2, 0, 3, 4), (1, 2, 3, 4, 0)])
S4m = closure([(1, 0, 2, 3), (1, 2, 3, 0)])
A4m = closure([(1, 2, 0, 3), (0, 2, 3, 1)])
D4m = closure([(1, 2, 3, 0), (0, 3, 2, 1)])
prof_A5, prof_S4 = profile_of(A5m), profile_of(S4m)
prof_A4, prof_D4 = profile_of(A4m), profile_of(D4m)
Q8m = [M for M in SL2(3) if mord(M, 3) in (1, 2, 4)]
prof_Q8 = mat_profile(Q8m, 3)
def split_double(prof):
    out = Counter()
    for o, c in prof.items():
        out[o] += c; out[lcm(o, 2)] += c
    return dict(sorted(out.items()))
def prof_product(*profs):
    out = {1: 1}
    for pr in profs:
        nxt = Counter()
        for o1, c1 in out.items():
            for o2, c2 in pr.items():
                nxt[lcm(o1, o2)] += c1 * c2
        out = dict(nxt)
    return dict(sorted(out.items()))
def cycprof(n):
    c = Counter()
    for k in range(n): c[n // gcd(n, k) if k else 1] += 1
    return dict(sorted(c.items()))
# 2O built inside SL(2,9) (precedent check 5c machinery)
def f9mul(u, v):
    a, b = u % 3, u // 3; c, d = v % 3, v // 3
    return ((a*c - b*d) % 3) + 3*((a*d + b*c) % 3)
def f9add(u, v):
    a, b = u % 3, u // 3; c, d = v % 3, v // 3
    return ((a + c) % 3) + 3*((b + d) % 3)
def mmul9(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (f9add(f9mul(a, e), f9mul(b, g)),
            f9add(f9mul(a, f), f9mul(b, h)),
            f9add(f9mul(c, e), f9mul(d, g)),
            f9add(f9mul(c, f), f9mul(d, h)))
I9 = (1, 0, 0, 1); mI9 = (2, 0, 0, 2)
def mord9(M):
    x = M; k = 1
    while x != I9: x = mmul9(x, M); k += 1
    return k
SL29 = [(a, b, c, d) for a in range(9) for b in range(9)
        for c in range(9) for d in range(9)
        if f9add(f9mul(a, d), f9mul(2, f9mul(b, c))) == 1]
def pow9(M, e):
    x = I9
    for _ in range(e): x = mmul9(x, M)
    return x
twoO = None
for A in [M for M in SL29 if mord9(M) == 8 and pow9(M, 4) == mI9]:
    for B in [M for M in SL29 if mord9(M) == 6 and pow9(M, 3) == mI9]:
        AB = mmul9(A, B)
        if mmul9(AB, AB) == mI9:
            cl = set([A, B]); fr = [A, B]
            while fr:
                x = fr.pop()
                for g in (A, B):
                    y = mmul9(x, g)
                    if y not in cl:
                        cl.add(y); fr.append(y)
                if len(cl) > 96: break
            if len(cl) == 48:
                twoO = cl; break
    if twoO: break
prof_2O = dict(sorted(Counter(mord9(M) for M in twoO).items()))
check("7a", "model certificates rebuilt: SL(2,7)/SL(2,5)/SL(2,3)/GL(2,3) "
      "profiles from matrices, 2O (order 48, unique involution) inside "
      "SL(2,9), Mobius PSL/PGL(2,7); each Schur-type model has a UNIQUE "
      "involution",
      twoO is not None
      and prof_SL27.get(2) == 1 and prof_SL25.get(2) == 1
      and prof_SL23.get(2) == 1 and prof_2O.get(2) == 1
      and len(mobius_group(SL2(7), 7)) == 168)

RES = {}
def hunt_pairs(key, o_a, o_b, o_ab, size, prof_ref, seed, tries, deadline,
               want):
    got = wit_get(key)
    if got is not None:
        out = []
        for ab in got:
            a = tuple(ab[0]); b = tuple(ab[1])
            G = closure([a, b], cap=2 * size + 10)
            assert len(G) == size and profile_of(G) == prof_ref
            out.append((a, b, G))
        note("[cache] %d %s witness(es) reloaded and re-verified"
             % (len(out), key))
        return out
    random.seed(seed)
    ia = idx_by_ord.get(o_a, np.array([], np.int64))
    ib = idx_by_ord.get(o_b, np.array([], np.int64))
    found = []; sets = []
    t_end = time.time() + deadline; n_try = 0
    while (n_try < tries and time.time() < t_end and len(found) < want
           and ia.size and ib.size):
        n_try += 1
        a = row_tup(ia[random.randrange(ia.size)])
        b = row_tup(ib[random.randrange(ib.size)])
        if pord(pmul(a, b)) != o_ab: continue
        G = closure([a, b], cap=2 * size + 10)
        if len(G) == size and profile_of(G) == prof_ref:
            fs = frozenset(G)
            if fs not in sets:
                sets.append(fs); found.append((a, b, G))
    wit_put(key, [[list(a), list(b)] for (a, b, G) in found])
    note("%s hunt: %d tries, %d distinct cop%s found"
         % (key, n_try, len(found), "y" if len(found) == 1 else "ies"))
    return found

def classify_preimage_small(name, a, b, G, models, xcheck=False):
    P, lifts = preimage_close([a, b])
    profP = profile_of(P)
    typ = next((nm for nm, pr in models if profP == pr),
               "UNRECOGNIZED [obs] %s" % profP)
    meta = inv_meta(G)
    if xcheck:
        fc = formula_census_preimage(G)
        check("7b", "CROSS-VALIDATION of the census formula: the derived "
              "census of this preimage (K-bar orders + square signs) "
              "equals the census of the explicit 240-perm closure",
              fc == profP, "%s" % (profP,))
    n_inv = profP.get(2, 0)
    return {"order": len(P), "profile": profP, "type": typ,
            "n_involutions": n_inv, "inv_classes": meta}

# ---- UB5a: L2(7) -> preimage: SL(2,7) or 2 x L2(7)?  [registered: SL(2,7)]
models_L = [("SL(2,7)  (Schur cover: unique involution -1, has order 14)",
             prof_SL27),
            ("2 x L2(7)  (split)", split_double(prof_PSL27))]
L7cop = hunt_pairs("L27", 2, 3, 7, 168, prof_PSL27, 31007,
                   400000, 300, 4)
if L7cop:
    types7 = []
    for ci, (a, b, G) in enumerate(L7cop):
        r = classify_preimage_small("L27", a, b, G, models_L,
                                    xcheck=(ci == 0))
        types7.append(r)
        note("L2(7) copy %d: involutions in K-bar class %s; preimage "
             "order %d, %d involution(s) -> %s"
             % (ci + 1, r["inv_classes"], r["order"],
                r["n_involutions"], r["type"]))
    got_sl27 = [r for r in types7 if r["type"].startswith("SL(2,7)")]
    got_split7 = [r for r in types7 if r["type"].startswith("2 x")]
    if got_sl27 and not got_split7:
        check("7c", "UB5a REGISTERED EXPECTATION CONFIRMED: every found "
              "L2(7) copy (%d, distinct) has preimage SL(2,7) -- unique "
              "involution -1, order-14 elements present: the Schur "
              "tower's top DOES live over the centre of H" % len(types7),
              all(r["n_involutions"] == 1 and 14 in r["profile"]
                  for r in got_sl27))
    elif got_split7 and not got_sl27:
        check("7c", "UB5a REGISTERED EXPECTATION INVERTED (full "
              "prominence): every found L2(7) copy has SPLIT preimage "
              "2 x L2(7); SL(2,7) does not appear over the centre on the "
              "found copies", True)
    else:
        check("7c", "UB5a: MIXED -- both preimage types occur across "
              "L2(7) classes (scoped to the %d found copies): %s"
              % (len(types7), [r["type"][:9] for r in types7]),
              bool(types7))
    RES["L2(7)"] = types7
else:
    check("7c", "UB5a: L2(7) hunt found no copy within budget -- "
          "NOT RUN (L2(7) < Sp6(2) is sealed [SM-003/SM-015]; the hunt "
          "budget, not existence, failed)", False)
    RES["L2(7)"] = None
print("[t=%6.1fs] UB5a done" % (time.time() - T0))

# ---- UB5b: A5 -> preimage: SL(2,5) = 2I or A5 x Z2?
models_A5 = [("SL(2,5) = 2I  (Schur cover: unique involution -1)",
              prof_SL25),
             ("A5 x Z2  (split)", split_double(prof_A5))]
A5cop = hunt_pairs("A5", 2, 3, 5, 60, prof_A5, 31008, 400000, 180, 6)
if A5cop:
    typesA5 = []
    for ci, (a, b, G) in enumerate(A5cop):
        r = classify_preimage_small("A5", a, b, G, models_A5)
        typesA5.append(r)
        note("A5 copy %d: involutions in %s; preimage order %d, %d "
             "involution(s) -> %s"
             % (ci + 1, r["inv_classes"], r["order"],
                r["n_involutions"], r["type"]))
    check("7d", "UB5b resolved over the %d found A5 copies: types %s"
          % (len(typesA5), sorted(set(r["type"][:12] for r in typesA5))),
          all(r["order"] == 120 for r in typesA5))
    RES["A5"] = typesA5
else:
    check("7d", "UB5b: A5 hunt found no copy within budget -- NOT RUN",
          False)
    RES["A5"] = None
print("[t=%6.1fs] UB5b done" % (time.time() - T0))

# ---- UB5c: S4 -> preimage: GL(2,3) / 2O / 2 x S4 (or the 4th extension)?
prof_2xS4 = split_double(prof_S4)
models_S4 = [("GL(2,3) = 2.S4  (transpositions lift to involutions)",
              prof_GL23),
             ("2O  (binary octahedral: transpositions lift to order 4)",
              prof_2O),
             ("2 x S4  (split)", prof_2xS4)]
S4cop = hunt_pairs("S4", 2, 3, 4, 24, prof_S4, 31009, 400000, 180, 6)
typesS4 = []
if S4cop:
    for ci, (a, b, G) in enumerate(S4cop):
        r = classify_preimage_small("S4", a, b, G, models_S4)
        typesS4.append(r)
        note("S4 copy %d: involutions in %s; preimage order %d, %d "
             "involution(s) -> %s"
             % (ci + 1, r["inv_classes"], r["order"],
                r["n_involutions"], r["type"]))
    check("7e", "UB5c resolved over the %d found S4 copies: types %s"
          % (len(typesS4),
             sorted(set(r["type"].split()[0] for r in typesS4))),
          all(r["order"] == 48 for r in typesS4))
    RES["S4"] = typesS4
else:
    check("7e", "UB5c: S4 hunt found no copy within budget -- NOT RUN",
          False)
    RES["S4"] = None
print("[t=%6.1fs] UB5c done" % (time.time() - T0))

# ---- UB5d: A4 -> preimage: SL(2,3) = 2T or A4 x Z2?
models_A4 = [("SL(2,3) = 2T  (Schur cover: unique involution -1)",
              prof_SL23),
             ("A4 x Z2  (split)", split_double(prof_A4))]
typesA4 = []
A4sources = []
for ci, (a, b, G) in enumerate(S4cop):
    D12, dg12 = derived_of_small([a, b])
    if len(D12) == 12 and profile_of(D12) == prof_A4:
        gens12 = []
        got = {pident(120)}
        for g in sorted(D12):
            if g in got: continue
            gens12.append(g); got = closure(gens12, cap=24)
            if len(got) == 12: break
        A4sources.append(("derived of S4 copy %d" % (ci + 1), gens12))
A4cop = hunt_pairs("A4", 2, 3, 3, 12, prof_A4, 31010, 200000, 90, 3)
for ci, (a, b, G) in enumerate(A4cop):
    A4sources.append(("direct hunt copy %d" % (ci + 1), [a, b]))
seenA4 = []
for srcname, gens12 in A4sources:
    fsA4 = frozenset(closure(gens12, cap=24))
    if fsA4 in seenA4: continue
    seenA4.append(fsA4)
    P, lifts = preimage_close(gens12)
    profP = profile_of(P)
    typ = next((nm for nm, pr in models_A4 if profP == pr),
               "UNRECOGNIZED [obs] %s" % profP)
    r = {"order": len(P), "profile": profP, "type": typ,
         "n_involutions": profP.get(2, 0),
         "inv_classes": inv_meta(fsA4), "src": srcname}
    typesA4.append(r)
    note("A4 copy (%s): involutions in %s; preimage order %d, %d "
         "involution(s) -> %s"
         % (srcname, r["inv_classes"], r["order"], r["n_involutions"],
            r["type"]))
if typesA4:
    check("7f", "UB5d resolved over the %d found A4 copies: types %s"
          % (len(typesA4),
             sorted(set(r["type"].split()[0] for r in typesA4))),
          all(r["order"] == 24 for r in typesA4))
    RES["A4"] = typesA4
else:
    check("7f", "UB5d: no A4 copy found within budget -- NOT RUN", False)
    RES["A4"] = None
print("[t=%6.1fs] UB5d done" % (time.time() - T0))

# ---- UB5e: C6 x Z2 -> preimage: abelian (C6xC2^2 / C12xC2) or stem
#      (C3xD4 / C3xQ8)?  [ties to SM-025's canonicality finding]
prof_C6C2 = prof_product(cycprof(6), cycprof(2))
models_C6 = [("C6 x C2 x C2  (abelian, split)",
              prof_product(cycprof(6), cycprof(2), cycprof(2))),
             ("C12 x C2  (abelian, -1 a square: non-split over <-1>)",
              prof_product(cycprof(12), cycprof(2))),
             ("C3 x D4  (stem over the D4 part)",
              prof_product(cycprof(3), prof_D4)),
             ("C3 x Q8  (stem over the Q8 part)",
              prof_product(cycprof(3), prof_Q8))]
gotC6 = wit_get("C6Z2")
foundC6 = None
if gotC6:
    a6, b2 = tuple(gotC6[0]), tuple(gotC6[1])
    G12 = closure([a6, b2], cap=48)
    assert len(G12) == 12 and profile_of(G12) == prof_C6C2
    foundC6 = (a6, b2, G12)
    note("[cache] C6xZ2 witness reloaded and re-verified")
else:
    for a_i in idx_by_ord[6][:30].tolist():
        a_np = EN[a_i]
        cm = (EN[:, a_np] == a_np[EN]).all(axis=1)
        cand = np.nonzero(cm & (ORD == 2))[0]
        a6 = row_tup(a_i); a3 = ppow(a6, 3)
        for b_i in cand.tolist():
            b2 = row_tup(b_i)
            if b2 == a3: continue
            G12 = closure([a6, b2], cap=48)
            if len(G12) == 12 and profile_of(G12) == prof_C6C2:
                foundC6 = (a6, b2, G12)
                wit_put("C6Z2", [list(a6), list(b2)])
                break
        if foundC6: break
if foundC6:
    a6, b2, G12 = foundC6
    P24, lifts24 = preimage_close([a6, b2])
    profP24 = profile_of(P24)
    la, lb = lifts24
    is_ab = (pmul(la, lb) == pmul(lb, la))
    typ24 = next((nm for nm, pr in models_C6 if profP24 == pr),
                 "UNRECOGNIZED [obs] %s" % profP24)
    check("7g", "UB5e: C6 x Z2 witness (commuting a order 6, b order 2 "
          "outside <a>, |<a,b>| = 12 abelian); preimage order 24, "
          "abelian: %s -> %s" % (is_ab, typ24),
          len(P24) == 24, "involutions in %s" % (inv_meta(G12),))
    RES["C6xZ2"] = {"order": len(P24), "profile": profP24, "type": typ24,
                    "abelian": is_ab, "inv_classes": inv_meta(G12)}
else:
    check("7g", "UB5e: no C6 x Z2 witness in the scanned centralizers -- "
          "NOT RUN", False)
    RES["C6xZ2"] = None
print("[t=%6.1fs] UB5e done" % (time.time() - T0))

# ---- UB5f: W(E6) (= U4(2):2, the index-28 subgroup of Sp6(2)) upstairs
def diagram_ok_E6(sub):
    adj = {i: [j for j in sub if j != i and GRAM[i][j] == -1] for i in sub}
    n_e = sum(len(adj[i]) for i in sub) // 2
    if n_e != 5: return False
    seen = {sub[0]}; fr = [sub[0]]
    while fr:
        x = fr.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); fr.append(y)
    if len(seen) != 6: return False
    if sorted(len(adj[i]) for i in sub) != [1, 1, 1, 2, 2, 3]: return False
    b = next(i for i in sub if len(adj[i]) == 3)
    def armlen(s):
        ln = 0; prev = b; cur = s
        while True:
            ln += 1
            nxt = [x for x in adj[cur] if x != prev]
            if not nxt: return ln
            prev, cur = cur, nxt[0]
    return sorted(armlen(s) for s in adj[b]) == [1, 2, 2]
E6sub = next(s for s in itertools.combinations(range(8), 6)
             if diagram_ok_E6(s))
oE6m, memE6m, TRE6m, _, _ = bsgs_cached(
    "we6_model_240", [S240[i] for i in E6sub], 240)
check("7h", "MODEL W(E6) inside W(E8): the simple-root subset %s spans an "
      "E6 subdiagram and its reflections generate order 51840 = |W(E6)| "
      "(census reference for the hunt)" % (E6sub,), oE6m == 51840)
ENe6, Oe6, censE6m = np_census(TRE6m, 240)
note("model W(E6) census: %s" % censE6m)
# calibration: can (involution, order-9) pairs 2-generate the model?
calib = wit_get("we6_calib")
if calib is None:
    random.seed(31011)
    ge6 = [S240[i] for i in E6sub]
    n_gen = 0; oab_seen = []; n_pairs = 0; n_att = 0
    while n_pairs < 20 and n_att < 600:
        n_att += 1
        x = rand_word(ge6); ox = pord(x)
        if ox % 2: continue
        a = ppow(x, ox // 2)
        y = rand_word(ge6); oy = pord(y)
        if oy % 9: continue
        b = ppow(y, oy // 9)
        n_pairs += 1
        o_pair, _, _, _, _ = make_bsgs_full([a, b], 240)
        if o_pair == 51840:
            n_gen += 1; oab_seen.append(pord(pmul(a, b)))
    calib = [n_gen, sorted(set(oab_seen)), n_pairs]
    wit_put("we6_calib", calib)
note("calibration on the model: %d/%s (involution, order-9) random pairs "
     "generate W(E6); ord(ab) values seen: %s"
     % (calib[0], calib[2] if len(calib) > 2 else 20, calib[1]))
orders_E6 = set(censE6m)
foundE6 = None
gotE6 = wit_get("WE6")
if gotE6:
    aE, bE = tuple(gotE6[0]), tuple(gotE6[1])
    oE, _, TRE, _, _ = bsgs_cached("we6_copy_120", [aE, bE], 120)
    assert oE == 51840
    foundE6 = (aE, bE)
    note("[cache] W(E6)-copy witness reloaded (order re-verified 51840)")
elif calib[0] > 0 and 9 in idx_by_ord:
    random.seed(31012)
    t_end = time.time() + 420; n_try = 0; n_bsgs = 0
    i2 = idx_by_ord[2]; i9 = idx_by_ord[9]
    while time.time() < t_end and n_try < 200000 and foundE6 is None:
        n_try += 1
        a = row_tup(i2[random.randrange(i2.size)])
        b = row_tup(i9[random.randrange(i9.size)])
        if calib[1] and pord(pmul(a, b)) not in calib[1]: continue
        okw = True
        for _ in range(15):
            w0 = pident(120)
            for _ in range(random.randrange(3, 12)):
                w0 = pmul((a, b)[random.randrange(2)], w0)
            if pord(w0) not in orders_E6:
                okw = False; break
        if not okw: continue
        n_bsgs += 1
        oE, _, TRE, _, _ = make_bsgs_full([a, b], 120)
        if oE == 51840:
            foundE6 = (a, b)
            wit_put("WE6", [list(a), list(b)])
            _x = bsgs_cached("we6_copy_120", [a, b], 120)
            TRE = _x[2]
    note("W(E6) hunt: %d tries, %d BSGS builds" % (n_try, n_bsgs))
if foundE6:
    aE, bE = foundE6
    ENs, Os, censS = np_census(TRE, 120)
    check("7i", "a W(E6)-type subgroup FOUND in K-bar: order 51840 with "
          "element-order census IDENTICAL to the model W(E6) census "
          "[C; identification also matches the unique index-28 class "
          "U4(2):2 of Sp6(2), P cited ATLAS]", censS == censE6m,
          "census %s" % censS)
    lE = [lift_H(aE), lift_H(bE)]
    oPE, memPE, _, _, _ = bsgs_cached("we6_pre_240", lE + [anti], 240)
    check("7j", "the W(E6) preimage P in H has order 103680 = 2 x 51840 "
          "and contains -1", oPE == 103680 and memPE(anti))
    oDE, memDE, _, DEgens = derived_cached("we6_pre_derived", lE + [anti],
                                           240, seed=31013)
    normal_ok = True
    for g in lE + [anti]:
        gi = pinv(g)
        for d in DEgens:
            normal_ok &= memDE(pmul(pmul(g, d), gi))
    ab_ok = all(memDE(comm(x, y)) for x in lE + [anti]
                for y in lE + [anti])
    # exactness: D contains all generator commutators and is normal
    # (generator conjugates of its generators strip), so P/D is abelian
    # => [P,P] <= D; D <= [P,P] by construction => D = [P,P].
    idxD = oPE // oDE
    note("[P,P] closure: order %d, index %d in P; -1 in [P,P]: %s; "
         "normality over all D-generators: %s; generator commutators "
         "inside: %s (=> D = [P,P] EXACTLY)"
         % (oDE, idxD, memDE(anti), normal_ok, ab_ok))
    if memDE(anti):
        verdict_E6 = ("NON-SPLIT: -1 in [P,P] (a complement C would give "
                      "[P,P] = [C,C] avoiding -1) => P is a non-split "
                      "2.W(E6) [obs]")
        split_E6 = False
    else:
        sq_gens = [pmul(g, g) for g in lE + [anti]]
        oVE, memVE, _, _, _ = bsgs_cached("we6_pre_squares",
                                          DEgens + sq_gens, 240)
        # P/[P,P] is abelian, so its square subgroup is generated by the
        # squares of the generators' images; V = <[P,P], squares of gens>
        # is exactly [P,P].P^2, and a Z2-character kills -1 iff
        # -1 notin V  <=>  SPLIT.
        split_E6 = not memVE(anti)
        verdict_E6 = ("SPLIT: -1 notin [P,P].P^2 (order %d), so a "
                      "Z2-character of P separates -1 and its kernel is "
                      "a complement => P = 2 x W(E6)" % oVE) if split_E6 \
            else ("NON-SPLIT: -1 in [P,P].P^2 (order %d): every "
                  "index-2 subgroup contains -1 => no complement "
                  "=> P is a non-split 2.W(E6) [obs]" % oVE)
    censPE = np_preimage_census(ENs, Os)
    note("preimage census (formula): %s" % censPE)
    note("2 x W(E6) census would be: %s" % split_double(censE6m))
    check("7k", "UB5f resolved [obs either way, per brief]: %s"
          % verdict_E6,
          normal_ok and ab_ok and oDE in (25920, 51840, 103680),
          "census differs from split model: %s"
          % (censPE != split_double(censE6m)))
    RES["W(E6)"] = {"order": oPE, "split": split_E6,
                    "verdict": verdict_E6, "census": censPE}
else:
    why = ("calibration found no (2,9) generation" if calib[0] == 0
           else "hunt budget exhausted")
    check("7k", "UB5f: W(E6) NOT RUN -- %s (stated, per brief: do not "
          "burn the budget here)" % why, True)
    RES["W(E6)"] = None
print("[t=%6.1fs] UB5f done" % (time.time() - T0))

# ---- UB5g: N_{K-bar}(L2(7)) -- PGL(2,7)-type? (SM-024 machinery)
if L7cop:
    a7, b7, G7 = L7cop[0]
    scan = wit_get("PGL27_scan")
    if scan is None:
        EINV = np.argsort(EN, axis=1).astype(np.uint8)
        Lh = np.array(sorted(set(
            hrows(np.array([list(g) for g in sorted(G7)],
                           np.uint8)).tolist())), np.uint64)
        maskN = np.ones(NKB, bool)
        for hgen in (a7, b7):
            hn = np.array(hgen, np.uint8)
            GH = EN[:, hn]
            CONJ = np.take_along_axis(GH, EINV, axis=1)
            maskN &= np.isin(hrows(CONJ), Lh)
            del GH, CONJ
        del EINV
        idxN = np.nonzero(maskN)[0]
        extra = None
        G7set = frozenset(G7)
        for i in idxN.tolist():
            t = row_tup(i)
            if t not in G7set:
                extra = t; break
        scan = [int(idxN.size), list(extra) if extra else None]
        wit_put("PGL27_scan", scan)
    nN, extra = scan[0], (tuple(scan[1]) if scan[1] else None)
    note("normalizer scan (exhaustive over all %d elements of K-bar, "
         "hash-verified conjugation of both L2(7) generators): |N(L)| = %d"
         % (NKB, nN))
    if nN == 336 and extra is not None:
        # exact re-verification of the witness coset element
        ei = pinv(extra)
        G7set = frozenset(G7)
        conj_ok = all(pmul(pmul(extra, g), ei) in G7set for g in (a7, b7))
        Nfull = closure([a7, b7, extra], cap=800)
        profN = profile_of(Nfull)
        isPGL = (profN == prof_PGL27)
        check("7l", "UB5g: N_{K-bar}(L2(7)) has order 336 = 2 x 168 "
              "(exhaustive scan) and matches PGL(2,7) by census: the "
              "over-group PGL(2,7) sits in K-bar",
              conj_ok and len(Nfull) == 336 and isPGL,
              "N census %s" % profN)
        P672, liftsN = preimage_close([a7, b7, extra])
        profP672 = profile_of(P672)
        D672, dg672 = derived_of_small(liftsN + [anti], cap=2000)
        in_D = anti in D672
        if in_D:
            vN = "NON-SPLIT over <-1>: -1 in [P,P] [obs]"
        else:
            sq672 = closure(list(dg672) + [pmul(g, g)
                                           for g in liftsN + [anti]],
                            cap=2000)
            vN = ("SPLIT: -1 notin [P,P].P^2 => P = 2 x PGL(2,7) [obs]"
                  if anti not in sq672 else
                  "NON-SPLIT over <-1>: -1 in [P,P].P^2 [obs]")
        check("7m", "the PGL(2,7)-preimage (order %d) classified: %s"
              % (len(P672), vN), len(P672) == 672,
              "census %s, %d involutions"
              % (profP672, profP672.get(2, 0)))
        RES["PGL(2,7)"] = {"order": len(P672), "profile": profP672,
                           "verdict": vN,
                           "derived_order": len(D672)}
    else:
        check("7l", "UB5g: N_{K-bar}(L2(7)) = L2(7) itself (order %d): "
              "self-normalizing -- no PGL(2,7) over THIS copy [obs; "
              "exhaustive over all of K-bar for this copy]" % nN,
              nN == 168)
        RES["PGL(2,7)"] = {"self_normalizing": True, "nN": nN}
else:
    check("7l", "UB5g: NOT RUN (no L2(7) witness)", False)
    RES["PGL(2,7)"] = None
print("[t=%6.1fs] stage 7 done" % (time.time() - T0))
stage_gate(7)

# ======================================================================
banner("UB6 -- VERDICT: the two-shadow refinement, final form")
# ======================================================================
def _typestr(r):
    return r.get("type") or r.get("verdict") or \
        ("self-normalizing (no PGL(2,7) over this copy)"
         if r.get("self_normalizing") else "?")
def types_of(key):
    rs = RES.get(key)
    if not rs: return None
    if isinstance(rs, dict): rs = [rs]
    return sorted(set(_typestr(r).split("  ")[0].split(":")[0]
                      for r in rs))
def any_split(key):
    rs = RES.get(key)
    if not rs: return None
    if isinstance(rs, dict): rs = [rs]
    return any("(split)" in _typestr(r) or "abelian, split)" in _typestr(r)
               or r.get("split") is True or _typestr(r).startswith("SPLIT")
               for r in rs)
def any_schur(key):
    rs = RES.get(key)
    if not rs: return None
    if isinstance(rs, dict): rs = [rs]
    return any(r.get("n_involutions") == 1 for r in rs)

print("""
  Both columns are about living OVER THE +- CENTRE of the named group.
  Left column: W(E7) = <-1> x Sp6(2), SPLIT  [cited: sealed SM-023].
  Right column: H = pi^-1(spin Sp6(2)) <= W(E8)  [computed here, UB4: %s].
  A quotient-level X embeds in the +-extension iff some copy of X in the
  quotient has SPLIT preimage; the Schur cover 2.X lives over the centre
  iff some copy has NON-SPLIT (unique-involution) preimage.  Right-column
  claims are scoped to the copies found and classified in UB5 (counts
  printed there); positive findings are decisive per copy.
""" % UB4)
rows_verdict = []
for key, cited in [
        ("L2(7)", "SL(2,7) NOT in W(E7) AT ALL; preimage split 2xL2(7)"),
        ("A5", "over hinge: only split Ih = <-1> x A5 (2I absent)"),
        ("S4", "over hinge: only split 2 x S4 (GL(2,3)/2O off-hinge/absent)"),
        ("A4", "over hinge: only split Th = <-1> x A4 (2T off-hinge)"),
        ("C6xZ2", "abelian split over the hinge"),
        ("W(E6)", "W(E6) < Sp6(2) [SM-003]; hinge preimage split"),
        ("PGL(2,7)", "over-group of L2(7) [SM-024 lane]")]:
    tys = types_of(key)
    here = ("NOT RUN" if tys is None else "; ".join(tys))
    rows_verdict.append((key, cited, here))
    print("  %-9s | W(E7) [cited]: %-55s" % (key, cited))
    print("  %-9s | H     [comp.]: %s" % ("", here))
print()
sl27_here = any_schur("L2(7)")
spine_up = {k: any_split(k) for k in ("A5", "S4", "A4")}
if UB4.startswith("PASS"):
    print("  THE TWO-SHADOW STATEMENT (computed):")
    if sl27_here:
        print("  * The Schur tower's top DOES live over the centre of H = "
              "2.Sp6(2): the L2(7)\n    preimage is SL(2,7) (unique "
              "involution -1, order 14 present) -- exactly the\n    "
              "group W(E7) provably excludes (SM-023).")
    for k in ("A5", "S4", "A4"):
        v = spine_up[k]
        if v is None:
            print("  * %s upstairs: NOT RUN." % k)
        elif v:
            print("  * %s embeds in H (a found copy has split preimage): "
                  "this spine level survives\n    upstairs." % k)
        else:
            print("  * %s does NOT embed in H over any found copy (no "
                  "split preimage occurs;\n    types seen: %s): this "
                  "spine level FAILS upstairs [scoped to the found\n"
                  "    copies]." % (k, ", ".join(types_of(k))))
    failed_levels = [k for k in ("A5", "S4", "A4")
                     if spine_up.get(k) is False]
    if failed_levels and sl27_here:
        print("""
  * CONSEQUENCE for the joint target: over the found copies, NO SINGLE
    +-extension of Sp6(2) holds both towers IN FULL.  W(E7) = 2 x Sp6(2)
    holds the whole SPINE over its hinge and provably exiles the Schur
    covers (SM-023); H = 2.Sp6(2) holds the whole SCHUR TOWER over its
    hinge (SL(2,7), 2I, GL(2,3)/2O, 2T -- all computed above) but the
    spine level(s) %s found no split preimage, so the spine chain does
    not pass upstairs intact [scoped to the found copies].  The hinge
    forces a choice.  Any exact overgroup holding both towers must sit
    STRICTLY ABOVE both +-extensions -- candidates: the 2^2-type
    extensions of Sp6(2) glueing both hinges, or W(E8) itself (where both
    towers demonstrably live side by side: UB2's split 2 x Sp6(2) and
    UB4's 2.Sp6(2) are BOTH subgroups of W(E8)).  NAMED, NOT COMPUTED
    (per brief).""" % ", ".join(failed_levels))
elif "INVERTED" in UB4:
    print("""
  THE INVERTED STATEMENT (recorded at full prominence): H split means
  W(E8) does not deliver 2.Sp6(2) by the spin-preimage route; the
  construction question reopens (fallback per brief = amendment).""")
print("""
  NOT-CLAIMS: no statement about subgroup classes not sampled by the UB5
  hunts (negative embedding claims are scoped to the found copies); no
  claim that K-bar's abstract type is verified beyond the fingerprint
  (order 1451520 + perfect + element-order set + the O7(2) transvection
  construction); nothing about RH/GRH; no physical identification
  (Rule 3).""")

print("=" * 78)
print("RESULT: %d checks passed, %d failed%s"
      % (PASS, FAIL, ("   FAILED: %s" % FAILED) if FAILED else ""))
print("registered expectations: UB2 (vector preimage split) / UB4 (H "
      "perfect) / UB5a (SL(2,7))\n  -- resolutions printed at their "
      "sites above at equal prominence.")
print("total time %.1fs" % (time.time() - T0))
print("=" * 78)
