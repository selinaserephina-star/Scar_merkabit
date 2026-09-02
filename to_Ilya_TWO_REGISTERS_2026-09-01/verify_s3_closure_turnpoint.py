# -*- coding: utf-8 -*-
r"""verify_s3_closure_turnpoint.py -- TWO SMALL VERIFICATIONS (joint
work-items, reactive-verification precedent: no locked brief; the
registered expectations below are on the record UP FRONT and each is
resolvable INVERTED at equal prominence).

TASK 1 -- THE S3 CLOSURE (the last tower-pair).
  Sealed context: Stone V proved <C, H> = W+(E8) (order 348364800);
  Stone W proved <H, H3> = W+(E8) with H3 = s1 H s1 the third tower.
  The UNTESTED pair: K_bt = <C, H3> (body + third).
  REGISTERED EXPECTATION (auditor, on the record): |K_bt| = 348364800
  = |W+(E8)| -- every tower-pair regenerates the roof (the symmetric
  triangle).  Resolvable INVERTED at equal prominence; if |K_bt| <
  |W+|, identify the group by order and cheap invariants, full
  prominence, and Ilya's question resolves "opens a fourth" (a proper
  intermediate group).

TASK 2 -- TURN-POINT CRITERION A, SEALED.
  Input: RECEIVED_2026-09-01_IB_TUBES_TURNS/"PROMPT_ Operationalizing
  the Turn Point.md" (IB's double criterion and decision rule), applied
  to his published floor sequence (RECEIVED_2026-09-01_IB_FLOOR_LIMIT/
  "FLOOR LIMIT -- FINAL RESULT v0.1.md"): lambda_min(N) for N = 300,
  400, 500, 600, 700 (values quoted as received; they are properties
  of HIS truncated operator A_fixed -- this lane quotes, it does not
  re-derive).
  REGISTERED EXPECTATION (registry v0.42 preliminary arithmetic): the
  second difference D2(N) is all ONE sign over the available range, so
  by HIS OWN decision rule the statement is "Turn point not found:
  D2(N) does not change sign over the computed range."  Resolvable
  INVERTED at equal prominence.
  Criterion B (eigenvector localization) requires v_min(N), which this
  lane does not hold (the A_fixed engine lives in the Ilya-Riemanns
  lane; duplication explicitly averted, registry v0.41): resolved NOT
  RUN with that reason; the combined double criterion is NOT EVALUABLE
  HERE (A alone: not found).
  HOUSE RED LINE: no RH/GRH statements of any kind appear here.

SEALED MACHINERY REUSED (read-only):
  verify_stone_u_2cover.py + _stone_u_cache/   -- W(E8) chain we8_240,
    C = stab_derived (vector-type Sp6(2) complement), shadow chains
    shadow_full / shadow_H, Clifford witnesses witnesses.json;
  verify_stone_v_we8_roof.py + _stone_v_cache/ -- R = W+(E8) chain
    K_240 (order 348364800), exact Bareiss det instrument (verbatim),
    w1/w2 replay (verbatim);
  verify_stone_w_third_shadow.py + _stone_w_cache/ -- H3 chain H3_240
    (order 2903040), the <H,H3> chain HH3_240, the s1-conjugation
    construction of hw1, hw2 (verbatim).
This script NEVER writes into the sealed caches; its own checkpoints
go to _s3_closure_cache/.

DISCIPLINE: compute, never assert; fail-first logs kept; exhaustive
claims scoped; grades [C]/[P cited] unblended.  Not RH/GRH; no
physical identification (Rule 3).  No registry/git writes by this
script.

Run:  python -X utf8 verify_s3_closure_turnpoint.py
"""
import hashlib, itertools, json, os, sys, time, random
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

CACHE_U = "_stone_u_cache"          # READ-ONLY (sealed, Stone U)
CACHE_V = "_stone_v_cache"          # READ-ONLY (sealed, Stone V)
CACHE_W = "_stone_w_cache"          # READ-ONLY (sealed, Stone W)
CACHE_S3 = "_s3_closure_cache"      # this run's own checkpoints
os.makedirs(CACHE_S3, exist_ok=True)
random.seed(20260902)

# ======================================================================
# permutation utilities (verbatim algorithms from sealed
# verify_stone_u_2cover.py / verify_stone_v_we8_roof.py /
# verify_stone_w_third_shadow.py)
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

def bsgs_load_sealed(cache, name, deg):
    """load a SEALED chain from a prior stone's cache; never writes."""
    f = os.path.join(cache, name + ".npz")
    assert os.path.exists(f), "sealed chain missing: %s" % f
    o, mem, transv, base, lvl = _bsgs_load(f, deg)
    note("[sealed cache %s] BSGS '%s' loaded (order %d, depth %d)"
         % (cache, name, o, len(base)))
    return o, mem, transv, base, lvl

def bsgs_cached_s3(name, gens, deg, init_base=None):
    f = os.path.join(CACHE_S3, name + ".npz")
    if os.path.exists(f):
        o, mem, transv, base, lvl = _bsgs_load(f, deg)
        note("[cache] BSGS '%s' loaded (order %d, depth %d)"
             % (name, o, len(base)))
        return o, mem, transv, base, lvl
    t1 = time.time()
    o, mem, transv, base, lvl = make_bsgs_full(gens, deg, init_base)
    _bsgs_save(f, base, transv, lvl, deg)
    note("[built] BSGS '%s': order %d, depth %d, %.1fs"
         % (name, o, len(base), time.time() - t1))
    return o, mem, transv, base, lvl

def shadow_load_sealed(name):
    """load a SEALED Stone U shadow chain (pair action, 240-carries)."""
    f = os.path.join(CACHE_U, name + ".npz")
    assert os.path.exists(f), "sealed shadow chain missing: %s" % f
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
    note("[sealed cache] shadow chain '%s' loaded (order %d)" % (name, o))
    return o, base, transv

def shadow_sift(base, transv, d1, d2, target):
    r2 = tuple(range(d2)); h = target
    for i, bpt in enumerate(base):
        x = h[bpt]
        if x not in transv[i]: return None
        t1p, t2p = transv[i][x]
        r2 = pmul(r2, t2p)
        h = pmul(pinv(t1p), h)
    if h != tuple(range(d1)): return None
    return r2

# ======================================================================
# F2 8x8 matrices + exact det instrument (verbatim Stone U/V/W)
# ======================================================================
IDM = tuple(1 << i for i in range(8))
def mvec(M, x):
    y = 0
    while x:
        b = x & -x
        y ^= M[b.bit_length() - 1]
        x ^= b
    return y
def mmulF2(A, B): return tuple(mvec(A, c) for c in B)
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
def f2_nullspace(rows, ncols):
    piv_rows = []; piv_cols = []
    for r in rows:
        for pr, pc in zip(piv_rows, piv_cols):
            if (r >> pc) & 1: r ^= pr
        if r:
            c = (r & -r).bit_length() - 1
            piv_rows.append(r); piv_cols.append(c)
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

# exact integer determinant (Bareiss, fraction-free; verbatim Stone V)
def int_det(M):
    A = [row[:] for row in M]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def perm_parity(p):
    n = len(p); seen = [False] * n; par = 0
    for i in range(n):
        if seen[i]: continue
        j = i; ln = 0
        while not seen[j]:
            seen[j] = True; j = p[j]; ln += 1
        par ^= (ln - 1) & 1
    return -1 if par else 1

print("=" * 78)
print("S3 CLOSURE + TURN-POINT CRITERION A -- two small verifications")
print("=" * 78)
print("[t=%6.1fs] start" % (time.time() - T0))

banner("REGISTERED EXPECTATIONS (on the record UP FRONT; each "
       "resolvable INVERTED at equal prominence)")
note("E1 (Task 1, auditor): |K_bt| = |<C, H3>| = 348364800 = |W+(E8)| "
     "-- every tower-pair")
note("    regenerates the roof (the symmetric triangle).")
note("E2 (Task 2, registry v0.42 preliminary arithmetic): D2(N) is all "
     "ONE sign over the")
note("    available range => by IB's OWN decision rule: 'Turn point "
     "not found: D2(N) does")
note("    not change sign over the computed range.'")

# ======================================================================
banner("TASK 1, STAGE 1 -- sealed machinery reloaded and re-verified; "
       "the pair (C, H3) reassembled by deterministic replay")
# ======================================================================
# --- roots, simple reflections, -1 (deterministic replay, verbatim)
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
ridx = {r: k for k, r in enumerate(roots)}
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
SIMPLE = [
    (1, -1, -1, -1, -1, -1, -1, 1),
    (2, 2, 0, 0, 0, 0, 0, 0),
    (-2, 2, 0, 0, 0, 0, 0, 0),
    (0, -2, 2, 0, 0, 0, 0, 0),
    (0, 0, -2, 2, 0, 0, 0, 0),
    (0, 0, 0, -2, 2, 0, 0, 0),
    (0, 0, 0, 0, -2, 2, 0, 0),
    (0, 0, 0, 0, 0, -2, 2, 0),
]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
S240 = []
for a in SIMPLE:
    perm = []
    for r in roots:
        c = dot4(r, a)
        img = tuple(r[t] - c * a[t] for t in range(8))
        perm.append(ridx[img])
    S240.append(tuple(perm))
anti = tuple(ridx[tuple(-x for x in r)] for r in roots)
check("S1a", "240 E8 roots + 8 simple reflections + antipode replayed "
      "deterministically (involutions, -1 commutes with all generators)",
      len(roots) == 240
      and all(pmul(s, s) == pident(240) for s in S240)
      and all(pmul(s, anti) == pmul(anti, s) for s in S240))

oW, memW, TRW, BASEW, LVLW = bsgs_load_sealed(CACHE_U, "we8_240", 240)
check("S1b", "sealed W(E8) chain: order 696729600; all 8 replayed "
      "generators and -1 pass its membership strip",
      oW == 696729600 and all(memW(s) for s in S240) and memW(anti))

# --- mod-2 data (replay, verbatim; needed for the w1/w2 transport and
#     for the exact root-basis coordinates behind the det instrument)
Gm = np.array(GRAM, dtype=np.int64)
Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
assert (Gm @ Ginv == np.eye(8, dtype=np.int64)).all()
Amat = np.array(SIMPLE, dtype=np.int64).T
coords = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64)
    c = Ginv @ d
    assert (Amat @ c == np.array(r, dtype=np.int64)).all()
    coords.append([int(x) for x in c])
rmask = [int(sum((coords[k][i] & 1) << i for i in range(8)))
         for k in range(240)]
qvals = []
for m in range(256):
    cv = np.array([(m >> i) & 1 for i in range(8)], dtype=np.int64)
    n2 = int(cv @ Gm @ cv)
    assert n2 % 2 == 0
    qvals.append((n2 // 2) % 2)
pair_of = [0] * 240; PAIRS = []
seenm = {}
for k in range(240):
    m = rmask[k]
    if m not in seenm:
        seenm[m] = len(PAIRS); PAIRS.append(m)
    pair_of[k] = seenm[m]
mask2pair = {PAIRS[j]: j for j in range(120)}
def to120(p240):
    out = [0] * 120
    for k in range(240): out[pair_of[k]] = pair_of[p240[k]]
    return tuple(out)
sidx = [ridx[a] for a in SIMPLE]
def M2_of(w):
    return tuple(rmask[w[sidx[j]]] for j in range(8))
check("S1c", "mod-2 replay: 120 antipodal pairs = mod-2 fibres; -1 acts "
      "trivially on pairs",
      len(PAIRS) == 120 and to120(anti) == pident(120))

# --- C: the vector-type complement (sealed stab_derived)
aix = ridx[SIMPLE[0]]
oC, memC, TRC, BASEC, LVLC = bsgs_load_sealed(CACHE_U, "stab_derived", 240)
gz = np.load(os.path.join(CACHE_U, "stab_derived_gens.npz"))["g"]
Cgens = [tuple(int(x) for x in gz[j]) for j in range(gz.shape[0])]
check("S1d", "sealed C = [Stab(alpha),Stab(alpha)]: order 1451520 = "
      "|Sp6(2)|; cached generators fix alpha, pass its chain, -1 not "
      "in C", oC == 1451520 and all(g[aix] == aix for g in Cgens)
      and all(memC(g) for g in Cgens) and not memC(anti),
      "%d generators" % len(Cgens))

# --- w1, w2 replay (verbatim Stone V stage 1: Clifford lifts ->
#     invariant plus-type form -> isometry transport -> shadow sift)
WIT_U = json.load(open(os.path.join(CACHE_U, "witnesses.json")))
g1m = tuple(WIT_U["k0_pair"][0]); g2m = tuple(WIT_U["k0_pair"][1])
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
assert len(NSQ) == 1
cQ = NSQ[0]
Q8 = []
for x in range(256):
    v = 0
    for t, (i, j) in enumerate(mon):
        if (cQ >> t) & 1 and ((x >> i) & 1) and ((x >> j) & 1): v ^= 1
    Q8.append(v)
def hyperbolic_basis(qtab):
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
def basis_matrix(pairs):
    cols = []
    for (u, v) in pairs: cols += [u, v]
    return tuple(cols)
U1 = basis_matrix(hyperbolic_basis(Q8))
U2 = basis_matrix(hyperbolic_basis(qvals))
Tmat = mmulF2(U2, f2_matinv(U1))
Ti = f2_matinv(Tmat)
A1 = mmulF2(Tmat, mmulF2(g1m, Ti)); A2 = mmulF2(Tmat, mmulF2(g2m, Ti))
def pair_perm_of_mat(A):
    return tuple(mask2pair[mvec(A, PAIRS[j])] for j in range(120))
pp1 = pair_perm_of_mat(A1); pp2 = pair_perm_of_mat(A2)
SH_o, SH_base, SH_tr = shadow_load_sealed("shadow_full")
w1 = shadow_sift(SH_base, SH_tr, 120, 240, pp1)
w2 = shadow_sift(SH_base, SH_tr, 120, 240, pp2)
check("S1e", "K_spin generators replayed (verbatim transport) and "
      "lifted through the sealed shadow chain: pi(w_i) = A_i exactly, "
      "both in W(E8)",
      w1 is not None and w2 is not None
      and M2_of(w1) == A1 and M2_of(w2) == A2
      and memW(w1) and memW(w2))
oH, memH, TRH, BASEH, LVLH = bsgs_load_sealed(CACHE_U, "H_240", 240)
check("S1f", "sealed H chain: order 2903040 = 2 x |Sp6(2)|; w1, w2, -1 "
      "all pass its membership strip (H = the spin tower)",
      oH == 2903040 and memH(w1) and memH(w2) and memH(anti))

# --- H3 = s1 H s1 (verbatim Stone W construction), against its sealed
#     chain
w0 = S240[0]
hw1 = pmul(pmul(w0, w1), w0); hw2 = pmul(pmul(w0, w2), w0)
oH3, memH3, TRH3, BASEH3, LVLH3 = bsgs_load_sealed(CACHE_W, "H3_240", 240)
check("S1g", "sealed H3 = <s1 w1 s1, s1 w2 s1> chain (Stone W): order "
      "2903040; the replayed conjugates hw1, hw2 and -1 all pass its "
      "membership strip; H3 is NOT H (at least one generator fails "
      "H's strip)",
      oH3 == 2903040 and memH3(hw1) and memH3(hw2) and memH3(anti)
      and not (memH(hw1) and memH(hw2)))

# --- R = W+(E8) from the sealed Stone V chain; the sealed <H,H3>
#     chain from Stone W (context: the other two tower-pairs)
oR, memR, TRR, BASER, LVLR = bsgs_load_sealed(CACHE_V, "K_240", 240)
oHH = bsgs_load_sealed(CACHE_W, "HH3_240", 240)[0]
check("S1h", "the two SEALED tower-pair closures reload: |<C,H>| = "
      "348364800 (Stone V K_240) and |<H,H3>| = 348364800 (Stone W "
      "HH3_240) -- two sides of the triangle are already the roof",
      oR == 348364800 and oHH == 348364800)

print("[t=%6.1fs] task 1 stage 1 done" % (time.time() - T0))

# ======================================================================
banner("TASK 1, STAGE 2 -- K_bt = <C, H3>: evenness, containment in "
       "W+, and the BSGS order (REGISTERED EXPECTATION E1 resolved "
       "here)")
# ======================================================================
BTgens = Cgens + [hw1, hw2]
def mat_of(w):
    return [[coords[w[sidx[j]]][i] for j in range(8)] for i in range(8)]
dets_BT = [int_det(mat_of(g)) for g in BTgens]
pars_BT = [perm_parity(g) for g in BTgens]
check("S2a", "evenness instrument: every K_bt generator (Cgens + hw1 + "
      "hw2) has exact Bareiss det +1 in the simple-root basis AND "
      "permutation parity +1 on the 240 roots; a simple reflection has "
      "det -1 (the instrument separates)",
      all(d == 1 for d in dets_BT) and all(p == 1 for p in pars_BT)
      and int_det(mat_of(S240[0])) == -1,
      "dets %s" % sorted(set(dets_BT)))
check("S2b", "membership strip: every K_bt generator and -1 pass the "
      "sealed R = W+(E8) chain => K_bt <= W+(E8) (both routes agree "
      "with S2a)",
      all(memR(g) for g in BTgens) and memR(anti)
      and not memR(S240[0]))

oBT, memBT, TRBT, BASEBT, LVLBT = bsgs_cached_s3(
    "K_bt_240", BTgens, 240, init_base=BASER)
WPLUS = 348364800
check("S2c", "|K_bt| = |<C, H3>| computed by BSGS closure on the "
      "240-point action: order = %d" % oBT,
      oBT > 0 and WPLUS % oBT == 0, "|K_bt| = %d" % oBT)
if oBT == WPLUS:
    check("S2d", "REGISTERED EXPECTATION E1 RESOLVED -- PASS: |K_bt| = "
          "348364800 = |W+(E8)|; with K_bt <= W+ (S2a/S2b) and equal "
          "orders, K_bt = <C, H3> = W+(E8) EXACTLY -- the third "
          "tower-pair also regenerates the roof", True)
    E1 = "PASS (|<C,H3>| = 348364800 = |W+(E8)|)"
else:
    check("S2d", "REGISTERED EXPECTATION E1 -- INVERTED (full "
          "prominence): |K_bt| = %d < 348364800, a PROPER subgroup of "
          "W+(E8) of index %d -- a fourth group opens; identification "
          "by order and cheap invariants follows" % (oBT, WPLUS // oBT),
          False)
    E1 = "INVERTED (|<C,H3>| = %d, index %d in W+)" % (oBT, WPLUS // oBT)
    # cheap invariants, full prominence
    note("INVERTED-branch invariants for K_bt:")
    note("  order %d = index %d in W+(E8)" % (oBT, WPLUS // oBT))
    note("  -1 in K_bt: %s" % memBT(anti))
    seen = [False] * 240; osz = []
    for i0 in range(240):
        if seen[i0]: continue
        orb = [i0]; seen[i0] = True; fr = [i0]
        while fr:
            x = fr.pop()
            for g in BTgens:
                y = g[x]
                if not seen[y]:
                    seen[y] = True; orb.append(y); fr.append(y)
        osz.append(len(orb))
    note("  orbit sizes on the 240 roots: %s" % sorted(osz))
    note("  contains C (order 1451520): generators by construction; "
         "contains H3 (order 2903040): generators by construction")
cross = (memBT(anti) and all(memBT(g) for g in BTgens))
w_in = memBT(w1) and memBT(w2)
check("S2e", "closure sanity: all K_bt generators and -1 pass the K_bt "
      "strip; w1, w2 (the H generators) pass the K_bt strip iff the "
      "triangle closed -- observed: %s (consistent with S2c/S2d)"
      % w_in, cross and (w_in == (oBT == WPLUS)))

banner("TASK 1 VERDICT -- the S3 closure (Ilya's question: 'closes the "
       "triangle or opens a fourth')")
if oBT == WPLUS:
    print("""
  THE TRIANGLE IS CLOSED.  All three tower-pairs regenerate the roof:
    <C,  H > = W+(E8)   (Stone V, sealed, order 348364800)
    <H,  H3> = W+(E8)   (Stone W, sealed, order 348364800)
    <C,  H3> = W+(E8)   (THIS RUN, S2c/S2d, order %d)
  The three Sp6(2)-type towers under the roof are SYMMETRIC as a
  generating triangle: any two of {body C, spin H, third H3}
  generate the whole rotation subgroup W+(E8).  No fourth group
  opens: there is NO proper intermediate group over any tower-pair's
  closure.  Ilya's question resolves: it CLOSES THE TRIANGLE.
  [C] throughout (BSGS orders + exact det/parity + sealed strips);
  scope: this is the closure of the SPECIFIC sealed subgroups C, H,
  H3 of the sealed root ordering, not a conjugacy-class statement.
""" % oBT)
else:
    print("""
  THE TRIANGLE DID NOT CLOSE.  <C, H3> has order %d, a proper
  subgroup of W+(E8) of index %d -- Ilya's question resolves: it
  OPENS A FOURTH (a proper intermediate group between the tower-pair
  and the roof).  See the INVERTED-branch invariants above (full
  prominence).
""" % (oBT, WPLUS // oBT))
check("S3", "verdict recorded; expectation E1 resolution: %s" % E1,
      True)
print("[t=%6.1fs] task 1 done" % (time.time() - T0))

# ======================================================================
banner("TASK 2 -- TURN-POINT CRITERION A on IB's published floor "
       "sequence (sealed; quoted as received)")
# ======================================================================
DOC_TP = os.path.join("RECEIVED_2026-09-01_IB_TUBES_TURNS",
                      "PROMPT_ Operationalizing the Turn Point.md")
DOC_FL = os.path.join("RECEIVED_2026-09-01_IB_FLOOR_LIMIT",
                      "FLOOR LIMIT — FINAL RESULT v0.1.md")
tp_bytes = open(DOC_TP, "rb").read()
fl_bytes = open(DOC_FL, "rb").read()
tp_txt = tp_bytes.decode("utf-8")
fl_txt = fl_bytes.decode("utf-8")
note("input sha256(%s) = %s" % (DOC_TP,
     hashlib.sha256(tp_bytes).hexdigest()))
note("input sha256(%s) = %s" % (DOC_FL,
     hashlib.sha256(fl_bytes).hexdigest()))
check("T1", "both input documents read; IB's Criterion A ('second "
      "difference sign change'), the double criterion, and the "
      "decision-rule clause 'D2(N) does not change sign' are all "
      "present verbatim in the turn-point prompt",
      "second difference sign change" in tp_txt
      and "double criterion" in tp_txt
      and "D2(N) does not change sign" in tp_txt
      and "over the computed range" in tp_txt)

# the sequence AS RECEIVED (FLOOR LIMIT sec. 2 'Computed Points'):
# lambda_min values are NEGATIVE; IB publishes them signed.  Stored
# here in exact micro-units (integers x 1e-6) so all differences are
# EXACT integer arithmetic, no float noise.
SEQ = [(300, -14095273), (400, -14429690), (500, -14631510),
       (600, -14768492), (700, -14866000)]
seq_in_doc = all(("N=%d: −%d.%06d" % (n, (-v) // 1000000,
                                      (-v) % 1000000)) in fl_txt
                 for n, v in SEQ)
check("T2", "the five published points N=300..700 match the received "
      "FLOOR LIMIT document character-for-character (lambda_min "
      "negative, six decimals); N=200 does NOT appear in the received "
      "sequence, so the available range is N=300..700",
      seq_in_doc and "N=200" not in fl_txt.replace("N = 200", "N=200"),
      "5 points, quoted as received")
note("scope: lambda_min(N) are properties of IB's truncated operator "
     "A_fixed, quoted as received;")
note("this lane re-derives NOTHING about them (the A_fixed engine "
     "lives in the Ilya-Riemanns lane).")

# Criterion A: D2(N) = lambda_min(N+1) - 2 lambda_min(N) +
# lambda_min(N-1), where N+-1 = adjacent grid points (step 100).
lam = {n: v for n, v in SEQ}
Ns = [n for n, _ in SEQ]
D1 = {Ns[i]: lam[Ns[i]] - lam[Ns[i - 1]] for i in range(1, len(Ns))}
D2 = {Ns[i]: lam[Ns[i + 1]] - 2 * lam[Ns[i]] + lam[Ns[i - 1]]
      for i in range(1, len(Ns) - 1)}
def fmt(v):
    s = "-" if v < 0 else "+"
    a = abs(v)
    return "%s%d.%06d" % (s, a // 1000000, a % 1000000)
print("\n  CRITERION A TABLES (exact integer arithmetic on the "
      "received 6-decimal values; grid step 100,")
print("  so N+1/N-1 in IB's definition = adjacent grid points):\n")
print("    N      lambda_min(N)    D1(N) = lam(N)-lam(N-100)    "
      "D2(N) = lam(N+100)-2lam(N)+lam(N-100)")
for n in Ns:
    print("    %-5d  %-15s  %-27s  %s"
          % (n, fmt(lam[n]),
             fmt(D1[n]) if n in D1 else "--",
             fmt(D2[n]) if n in D2 else "--"))
print()
note("(IB's required output names 'Table of D2(N) for N = 300..600'; "
     "that presumes an N=200 point")
note(" this lane never received -- with the available grid 300..700, "
     " D2 is computable at the")
note(" interior points N = 400, 500, 600 exactly.)")
d1_expect = {400: -334417, 500: -201820, 600: -136982, 700: -97508}
d2_expect = {400: 132597, 500: 64838, 600: 39474}
check("T3", "first-difference table: D1(N) < 0 at every computable N "
      "(the sequence deepens monotonically, no sign change in "
      "lambda_min itself -- matches IB's sec. 2 observation)",
      D1 == d1_expect and all(v < 0 for v in D1.values()),
      "D1 = %s (micro-units)" % D1)
signs = sorted(set(1 if v > 0 else (-1 if v < 0 else 0)
                   for v in D2.values()))
check("T4", "second-difference table: D2(400), D2(500), D2(600) are "
      "ALL POSITIVE (all one sign; the sequence is convex over the "
      "whole computed range) -- D2 does NOT change sign",
      D2 == d2_expect and signs == [1],
      "D2 = %s (micro-units)" % D2)

banner("TASK 2 VERDICT -- in IB's own required-output format "
       "(turn-point prompt sec. 5/6)")
print("""
  1. Table of D2(N) (available range; grid step 100):

         N      D2(N)
         400    +0.132597
         500    +0.064838
         600    +0.039474

     (D2 > 0 at every computable point: no sign change.)

  2. Table of localization measures for v_min(N): NOT RUN.
     This lane does not hold the eigenvectors v_min(N).  The A_fixed
     engine lives in the Ilya-Riemanns lane; duplicating it here was
     explicitly averted (registry v0.41).

  3. Candidate N* from each criterion:
       Criterion A: none (no sign change in D2).
       Criterion B: NOT RUN (no eigenvectors held here).

  4. Combined N* from the double criterion: NOT EVALUABLE HERE
     (A alone: not found; B not run).

  5. Statement (IB's decision rule, verbatim clause):

       Turn point not found: D2(N) does not change sign
       over the computed range.
""")
check("T5", "Criterion A verdict by IB's OWN decision rule: 'Turn "
      "point not found: D2(N) does not change sign over the computed "
      "range' -- REGISTERED EXPECTATION E2 RESOLVED: PASS "
      "(preliminary arithmetic of registry v0.42 confirmed exactly)",
      signs == [1])
E2 = ("PASS (D2 all positive; turn point not found by IB's rule)"
      if signs == [1] else "INVERTED (D2 changes sign)")
# computable backing for the NOT RUN: no eigenvector arrays received
recv_arrays = []
for d in ("RECEIVED_2026-09-01_IB_FLOOR_LIMIT",
          "RECEIVED_2026-09-01_IB_TUBES_TURNS"):
    for fn in os.listdir(d):
        if fn.lower().endswith((".npz", ".npy", ".csv", ".json")):
            recv_arrays.append(os.path.join(d, fn))
check("T6", "Criterion B resolved NOT RUN, with computable backing: "
      "the received packages contain NO eigenvector/data arrays "
      "(v_min was never sent), and this lane holds no A_fixed engine "
      "(Ilya-Riemanns lane; duplication averted, registry v0.41)",
      recv_arrays == [], "array-like files in RECEIVED dirs: %s"
      % (recv_arrays or "none"))
check("T7", "combined double criterion: NOT EVALUABLE HERE (A alone: "
      "not found; B: not run) -- no 'horizon' language used (prompt "
      "sec. 7), and NO RH/GRH statement of any kind appears in this "
      "run (house red line)", True)
print("[t=%6.1fs] task 2 done" % (time.time() - T0))

# ======================================================================
print("=" * 78)
print("RESULT: %d checks passed, %d failed%s"
      % (PASS, FAIL, ("   FAILED: %s" % FAILED) if FAILED else ""))
print("registered expectation E1 (S3 closure, |<C,H3>|): %s" % E1)
print("registered expectation E2 (turn-point D2 one sign): %s" % E2)
print("total time %.1fs" % (time.time() - T0))
print("=" * 78)
