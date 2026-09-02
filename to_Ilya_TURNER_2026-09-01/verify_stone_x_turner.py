# -*- coding: utf-8 -*-
r"""verify_stone_x_turner.py -- STONE X: THE TURNER (triality made flesh)

Brief: BRIEF_STONE_X_TURNER.md (lock BRIEF_STONE_X_LOCK.sha256, sha verified
before this run AND re-verified as check X0:
7857bc5392dc38009297c01265709533446cc9c9da6fc755eb7efa627bf4ef16).

Question: SM-031 proved the Z3 cycling the three shadow classes is strictly
outer to W(E8)/+-1 -- the turn exists as a symmetry of the catalog, but no
object in our world performs it.  Stone X builds the performer: an explicit,
computable automorphism tau of Omega(q) ~= O8+(2) that cycles
vector -> spin -> spin -> vector.

ROUTE (the brief's declared construction; bars XB1-XB5):
  XB1  half-spin modules over F2: hyperbolic frame e1..e4,f1..f4 in the
       sealed (V,q) = L/2L; spinor module Lambda(E) (16-dim), Clifford
       action e_i by wedge, f_i by contraction; S+ = even part (8-dim);
       transvection decompositions of the roof's Omega-generators (even
       length, exact reproduction); rho+ verified a homomorphism
       (alternative decompositions agree; >=100 random word pairs exact).
  XB2  tau(g) = T+ rho+(g) T+^-1 lands in Omega (q-isometry, Dickson 0);
       automorphism (faithful rho+ => |image| = |Omega|; argument stated).
  XB3  THE TURN (registered expectation): orbit-signature triples of
       tau(C-bar), tau^2(C-bar), tau^3(C-bar) -- expect vector -> spin ->
       other spin -> vector.  PASS / INVERTED at full prominence.
  XB4  tau^3 inner explicitly: exact intertwiner solve h g = tau^3(g) h
       (64 unknowns over F2); expect dim 1; h a q-isometry; <tau> ~= Z3
       mod Inn.
  XB5  the roof-clock question posed in final form + the cheap pure-spinor
       datum (annihilator solids of the 135 singular spinors of (S+,Q+)).

SEALED MACHINERY (READ-ONLY): _stone_u_cache/ (stab_derived_gens = the 24
generators of C = [Stab(alpha),Stab(alpha)]; witnesses.json k0_pair = the
Clifford generating pair g1m,g2m; we8_240 + K_240 chains for membership),
_stone_v_cache/ (K_240 = the sealed roof chain), _stone_w_cache/
(ts_subspaces = the 270 maximal totally singular 4-subspaces).  The
orbit-signature instrument and all replays are VERBATIM from
verify_stone_w_third_shadow.py / verify_stone_u_2cover.py.

INSTANTIATION NOTES (choices the brief left open; no amendment needed):
  (i)   the hyperbolic frame on (V,q) is the one produced by the sealed
        deterministic hyperbolic_basis(qvals) (Stone U stage 5, verbatim
        code): pairs (u_k, v_k); we take e_k = u_k, f_k = v_k.
  (ii)  Lambda(E) basis: subsets S of {1,2,3,4} as 4-bit masks 0..15,
        x_S the ordered wedge e_{i1}^...^e_{ik} (i1<...<ik).  Over F2 the
        alternating signs (-1)^{#{j in S : j < i}} of the wedge e_i^ and
        the contraction iota_{f_i} all reduce to 1, so the operators are
        the sign-free set operations e_i.x_S = x_{S u i} (0 if i in S),
        f_i.x_S = x_{S \ i} (0 if i not in S); the ORDERING convention is
        fixed once (ascending) and used consistently -- the Clifford
        relations are verified on the module, not assumed (X1b/X1c).
  (iii) Omega's generating set: the mod-2 matrices of the 24 sealed Cgens
        plus A1, A2 (the roof R = <C, w1, w2> has image Omega, Stone W
        W1j/W1m); tau is DEFINED on all of O(q) via transvection
        decomposition, and evaluated on these generators.
  (iv)  transvection decomposition ("constructive basis-mapping
        algorithm", the brief's words): left-reduction fixing the
        standard basis e_1..e_8 vector by vector -- these are the
        simple-root masks, all NONSINGULAR (q=1), which matters: the
        pointwise stabilizer of nonsingular vectors stays transvection-
        generated down the O8+ -> Sp6(2) chain, whereas fixing the
        ISOTROPIC hyperbolic frame vectors strands the search (first
        fail-first run: after 5 isotropic anchors only 2 orthogonal
        transvections remain and the orbit closes without reaching the
        target; log kept).  To send y -> u: t_{y+u} when B(y,u)=1, else
        a complete BFS over the transvections orthogonal to the already-
        fixed anchors; correctness gate = exact reproduction + even
        length + q(v)=1 for every letter.
  (v)   alternative decompositions for the well-definedness check: for a
        nonsingular w, decompose(M t_w) + [w] and [w] + decompose(t_w M)
        (t_w an involution) give genuinely different words for M.

DISCIPLINE: compute, never assert; the registered expectation resolvable
INVERTED at equal prominence; fail-first logs kept; exact F2 arithmetic for
all algebraic claims; sealed caches READ-ONLY; own cache _stone_x_cache/.
Outputs: this script, verify_stone_x_turner.log, STONE_X_TURNER.md.
No registry/git/knowledge.yaml writes.  Not RH/GRH; no identifications
(Rule 3).

Run:  python -X utf8 verify_stone_x_turner.py [max_stage]
"""
import hashlib, itertools, json, os, sys, time, random
from collections import Counter
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
CACHE_X = "_stone_x_cache"          # this run's own checkpoints
os.makedirs(CACHE_X, exist_ok=True)
random.seed(20260902)
MAX_STAGE = int(sys.argv[1]) if len(sys.argv) > 1 else 99
def stage_gate(n):
    if n >= MAX_STAGE:
        print(f"\n[staged checkpoint exit after stage {n}; NOT a verdict]",
              flush=True)
        print(f"[so far: {PASS} PASS, {FAIL} FAIL"
              + (f", FAILED: {FAILED}" if FAILED else "") + "]")
        sys.exit(0)

# ======================================================================
# permutation + F2 utilities (verbatim precedents: Stone U/W)
# ======================================================================
def pmul(a, b): return tuple(a[x] for x in b)
def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def pident(n): return tuple(range(n))

IDM8 = tuple(1 << i for i in range(8))
IDM16 = tuple(1 << i for i in range(16))
def mvec(M, x):
    y = 0
    while x:
        b = x & -x
        y ^= M[b.bit_length() - 1]
        x ^= b
    return y
def mmul(A, B): return tuple(mvec(A, c) for c in B)
def madd(A, B): return tuple(a ^ b for a, b in zip(A, B))
def f2_matinv_n(M, n):
    rows = []
    for i in range(n):
        r = 0
        for j in range(n):
            if (M[j] >> i) & 1: r |= 1 << j
        rows.append(r | (1 << (n + i)))
    piv = 0
    for col in range(n):
        p = next((k for k in range(piv, n) if (rows[k] >> col) & 1), None)
        if p is None: return None
        rows[piv], rows[p] = rows[p], rows[piv]
        for k in range(n):
            if k != piv and (rows[k] >> col) & 1: rows[k] ^= rows[piv]
        piv += 1
    inv_cols = []
    for j in range(n):
        c = 0
        for i in range(n):
            if (rows[i] >> (n + j)) & 1: c |= 1 << i
        inv_cols.append(c)
    return tuple(inv_cols)
def f2_matinv(M): return f2_matinv_n(M, 8)
def f2_rank(masks):
    basis = []
    for m in masks:
        for b in basis:
            m = min(m, m ^ b)
        if m:
            basis.append(m); basis.sort(reverse=True)
    return len(basis)
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

def _bsgs_load(fname, deg):
    z = np.load(fname)
    base = [int(b) for b in z["base"]]
    nl = int(z["nlvl"][0])
    transv = []
    for i in range(nl):
        keys = z["k%d" % i]; vals = z["v%d" % i]
        transv.append({int(k): tuple(int(x) for x in vals[j])
                       for j, k in enumerate(keys)})
    o = 1
    for T in transv: o *= len(T)
    E = tuple(range(deg))
    def is_member(g):
        h = g
        for i in range(len(base)):
            x = h[base[i]]
            if x not in transv[i]: return False
            h = pmul(pinv(transv[i][x]), h)
        return h == E
    return o, is_member

def bsgs_load_sealed(cache, name, deg):
    f = os.path.join(cache, name + ".npz")
    assert os.path.exists(f), "sealed chain missing: %s" % f
    o, mem = _bsgs_load(f, deg)
    note("[sealed cache %s] BSGS '%s' loaded (order %d)" % (cache, name, o))
    return o, mem

print("=" * 78)
print("STONE X -- THE TURNER: an explicit triality automorphism of "
      "Omega(q) ~= O8+(2)")
print("=" * 78)
print("[t=%6.1fs] start" % (time.time() - T0))

# ======================================================================
banner("STAGE 0 -- X0: brief lock; sealed machinery replayed VERBATIM "
       "(Stone U/W); the roof's Omega-generators as matrices")
# ======================================================================
BRIEF = "BRIEF_STONE_X_TURNER.md"
LOCK = "7857bc5392dc38009297c01265709533446cc9c9da6fc755eb7efa627bf4ef16"
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("X0", "the brief is sha-locked: sha256(%s) equals the value in "
      "BRIEF_STONE_X_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

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
def Bform(x, y): return qvals[x ^ y] ^ qvals[x] ^ qvals[y]
sidx = [ridx[a] for a in SIMPLE]
def M2_of(w):
    return tuple(rmask[w[sidx[j]]] for j in range(8))
def dickson(M):
    return f2_rank([M[j] ^ (1 << j) for j in range(8)]) & 1
SING = [m for m in range(1, 256) if qvals[m] == 0]
NONSING = [m for m in range(256) if qvals[m] == 1]
check("X0b", "mod-2 replay: q plus-type on L/2L (135 singular nonzero + "
      "120 nonsingular); simple-root masks = the standard basis",
      len(SING) == 135 and len(NONSING) == 120
      and [rmask[sidx[j]] for j in range(8)] == list(IDM8))

# --- C (sealed vector-type complement) and the K_spin pair (verbatim
#     Stone W stage-1 replay: k0_pair -> invariant Q8 -> transport)
gz = np.load(os.path.join(CACHE_U, "stab_derived_gens.npz"))["g"]
Cgens = [tuple(int(x) for x in gz[j]) for j in range(gz.shape[0])]
aix = ridx[SIMPLE[0]]
alpha_mask = rmask[aix]
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
    """VERBATIM Stone U stage 5 (deterministic)."""
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
Tmat = mmul(U2, f2_matinv(U1))
Ti = f2_matinv(Tmat)
A1 = mmul(Tmat, mmul(g1m, Ti)); A2 = mmul(Tmat, mmul(g2m, Ti))

Cmats = [M2_of(g) for g in Cgens]
OMEGA_GENS = Cmats + [A1, A2]
oK, memK = bsgs_load_sealed(CACHE_V, "K_240", 240)
oW, memW = bsgs_load_sealed(CACHE_U, "we8_240", 240)
check("X0c", "sealed roof chain K_240: order 348364800 = |W+(E8)|; all 24 "
      "Cgens pass its membership strip and fix alpha; sealed we8_240 order "
      "696729600", oK == 348364800 and oW == 696729600
      and all(memK(g) for g in Cgens)
      and all(g[aix] == aix for g in Cgens) and len(Cgens) == 24)
iso_ok = all(all(qvals[mvec(M, x)] == qvals[x] for x in range(256))
             for M in OMEGA_GENS)
dick_ok = all(dickson(M) == 0 for M in OMEGA_GENS)
check("X0d", "the 26 Omega-generator matrices (24 C-bar images + A1 + A2, "
      "replayed verbatim) are q-isometries with Dickson 0: they generate "
      "the roof's image Omega(q), order 174182400 [sealed: Stone W "
      "W1j/W1m via K_pair_120]", iso_ok and dick_ok)
oKp, _ = bsgs_load_sealed(CACHE_V, "K_pair_120", 120)
check("X0e", "sealed K_pair_120 order = 174182400 = |Omega8+(2)| (the "
      "roof's matrix image; ker = <-1>, Stone W W1j)", oKp == 174182400)
print("[t=%6.1fs] stage 0 done" % (time.time() - T0))
stage_gate(0)

# ======================================================================
banner("STAGE 1 -- XB1(module): hyperbolic frame; Lambda(E); Clifford "
       "action verified on the module")
# ======================================================================
HB = hyperbolic_basis(qvals)
EVEC = [HB[k][0] for k in range(4)]     # e_1..e_4
FVEC = [HB[k][1] for k in range(4)]     # f_1..f_4
frame_ok = (all(qvals[e] == 0 for e in EVEC)
            and all(qvals[f] == 0 for f in FVEC)
            and all(Bform(EVEC[i], FVEC[j]) == (1 if i == j else 0)
                    for i in range(4) for j in range(4))
            and all(Bform(EVEC[i], EVEC[j]) == 0
                    for i in range(4) for j in range(4))
            and all(Bform(FVEC[i], FVEC[j]) == 0
                    for i in range(4) for j in range(4)))
UF = tuple(EVEC + FVEC)                 # columns e1..e4,f1..f4
UFi = f2_matinv(UF)
check("X1a", "hyperbolic frame e1..e4,f1..f4 in (V,q) (sealed "
      "deterministic Gram-Schmidt): q(e_i)=q(f_i)=0, B(e_i,f_j)=delta_ij, "
      "B(e_i,e_j)=B(f_i,f_j)=0; the 8 vectors are a basis (U invertible)",
      frame_ok and UFi is not None and mmul(UF, UFi) == IDM8,
      "e=%s f=%s" % (EVEC, FVEC))

# Lambda(E): basis x_S, S in 0..15 (4-bit masks, ordered ascending wedge).
# Over F2 the alternating signs vanish; operators are sign-free:
E_OP = [tuple((1 << (S | (1 << i))) if not (S >> i) & 1 else 0
              for S in range(16)) for i in range(4)]
F_OP = [tuple((1 << (S & ~(1 << i))) if (S >> i) & 1 else 0
              for S in range(16)) for i in range(4)]
ZERO16 = (0,) * 16
rel_ok = True
for i in range(4):
    for j in range(4):
        EE = madd(mmul(E_OP[i], E_OP[j]), mmul(E_OP[j], E_OP[i]))
        FF = madd(mmul(F_OP[i], F_OP[j]), mmul(F_OP[j], F_OP[i]))
        EF = madd(mmul(E_OP[i], F_OP[j]), mmul(F_OP[j], E_OP[i]))
        rel_ok &= (EE == ZERO16 and FF == ZERO16
                   and EF == (IDM16 if i == j else ZERO16))
check("X1b", "Clifford relations on the module (char 2: anticommute = "
      "commute, + = XOR of operators): e_i e_j + e_j e_i = 0 (incl. "
      "e_i^2 = 0), f_i f_j + f_j f_i = 0, e_i f_j + f_j e_i = "
      "delta_ij . id -- all 48 relations exact", rel_ok)

def op_of(v):
    """the Clifford action of v in V on Lambda(E): v = sum a_i e_i + b_i
    f_i in frame coordinates; op(v) = sum a_i E_i + b_i F_i (linear)."""
    c = mvec(UFi, v)
    M = ZERO16
    for i in range(4):
        if (c >> i) & 1: M = madd(M, E_OP[i])
        if (c >> (4 + i)) & 1: M = madd(M, F_OP[i])
    return M
OPS = [op_of(v) for v in range(256)]    # small table, reused throughout
sq_ok = all(mmul(OPS[v], OPS[v]) == (IDM16 if qvals[v] else ZERO16)
            for v in range(256))
check("X1c", "op(v)^2 = q(v).id on the module for ALL 256 v in V "
      "(exhaustive -- the key consistency gate; q in frame coordinates "
      "is sum a_i b_i, matching the sealed q)", sq_ok)
conj_ok = True
for v in NONSING:                        # all 120 q=1 vectors
    Mv = OPS[v]
    for u in UF:                         # the 8 frame basis vectors
        tu = u ^ (v if Bform(u, v) else 0)
        conj_ok &= (mmul(Mv, mmul(OPS[u], Mv)) == OPS[tu])
check("X1d", "for every one of the 120 nonsingular v: op(v) op(x) op(v) "
      "= op(t_v x) on the whole frame basis (op(v)^2 = id, so this IS "
      "Clifford conjugation implementing the transvection t_v)", conj_ok)
print("[t=%6.1fs] stage 1 done" % (time.time() - T0))
stage_gate(1)

# ======================================================================
banner("STAGE 2 -- XB1(decomposition): every Omega-generator as an EVEN "
       "product of orthogonal transvections, exactly")
# ======================================================================
def transvect(v):
    """matrix of t_v(x) = x + B(x,v) v, q(v)=1."""
    return tuple((1 << j) ^ (v if Bform(1 << j, v) else 0)
                 for j in range(8))

# anchor basis for the decomposition: the standard basis = the
# simple-root masks (X0b), all NONSINGULAR -- see instantiation note (iv)
ANCHORS = [1 << j for j in range(8)]
assert all(qvals[a] == 1 for a in ANCHORS)

def _route(y, u, fixed):
    """transvection vectors [v..] whose left-to-right application maps
    y -> u, each fixing every anchor in `fixed`.  Requires q(y) = q(u)
    and B(f,y) = B(f,u) for f in fixed (holds when y is the image of u
    under an isometry fixing `fixed`).  Direct step when B(y,u)=1, else
    a complete BFS over the allowed transvections (the first fail-first
    run showed constrained one/two-intermediate searches can be empty
    for isotropic anchors; with nonsingular anchors the BFS always
    lands, and exact reproduction is the gate either way)."""
    if y == u: return []
    if Bform(y, u) == 1:
        return [y ^ u]
    # complete BFS: moves = the transvections orthogonal to all of `fixed`
    allowed = [v for v in NONSING
               if all(Bform(f, v) == 0 for f in fixed)]
    prev = {y: None}
    frontier = [y]
    while frontier:
        nxt = []
        for x in frontier:
            for v in allowed:
                if Bform(x, v) == 0: continue
                x2 = x ^ v
                if x2 in prev: continue
                prev[x2] = (x, v)
                if x2 == u:
                    path = []
                    c2 = x2
                    while prev[c2] is not None:
                        px, pv = prev[c2]
                        path.append(pv); c2 = px
                    return list(reversed(path))
                nxt.append(x2)
        frontier = nxt
    raise RuntimeError("routing failed (would need an AMENDMENT)")

_DECOMP_MEMO = {}
def decompose(M):
    """list ws of q=1 vectors with t_{ws[0]} . t_{ws[1]} ... t_{ws[-1]}
    = M (matrix product order; rightmost applied first).  Memoized (the
    memo only shortcuts identical inputs; each stored word passed the
    exact-reproduction gate when first computed)."""
    got = _DECOMP_MEMO.get(M)
    if got is not None: return got
    cur = M
    word = []
    fixed = []
    for u in ANCHORS:
        y = mvec(cur, u)
        for v in _route(y, u, fixed):
            cur = mmul(transvect(v), cur)
            word.append(v)
        fixed.append(u)
    assert cur == IDM8, "reduction did not reach identity"
    assert word_matrix(word) == M, "decomposition does not reproduce M"
    _DECOMP_MEMO[M] = word
    return word              # M = t_{word[0]} ... t_{word[-1]}

def word_matrix(ws):
    M = IDM8
    for v in ws: M = mmul(M, transvect(v))
    return M

DECOMPS = []
dec_ok = True; lens = []
for M in OMEGA_GENS:
    ws = decompose(M)
    DECOMPS.append(ws)
    lens.append(len(ws))
    dec_ok &= (word_matrix(ws) == M and len(ws) % 2 == 0
               and all(qvals[v] == 1 for v in ws))
check("X2a", "all 26 Omega-generators decompose into orthogonal "
      "transvections t_v (q(v)=1): product reproduces the matrix "
      "EXACTLY, every length EVEN (consistent with Dickson 0 [P cited: "
      "Dickson invariant = transvection-length parity, a homomorphism "
      "O(q) -> F2])", dec_ok,
      "lengths %s" % sorted(Counter(lens).items()))
print("[t=%6.1fs] stage 2 done" % (time.time() - T0))
stage_gate(2)

# ======================================================================
banner("STAGE 3 -- XB1(rho+): the half-spin representation; "
       "WELL-DEFINEDNESS verified honestly")
# ======================================================================
EVEN = [S for S in range(16) if bin(S).count("1") % 2 == 0]
assert EVEN == [0, 3, 5, 6, 9, 10, 12, 15]
EPOS = {S: i for i, S in enumerate(EVEN)}
EVEN_MASK = sum(1 << S for S in EVEN)

def rho_full(ws):
    """16x16 spin matrix of the word (product of op(v), matrix order)."""
    P = IDM16
    for v in ws: P = mmul(P, OPS[v])
    return P

def splus_of(P):
    """restriction of a parity-even 16x16 P to S+ (8x8), or None."""
    cols = []
    for S in EVEN:
        c = P[S]
        if c & ~EVEN_MASK: return None
        cols.append(sum(((c >> T) & 1) << EPOS[T] for T in EVEN))
    return tuple(cols)

def rho_splus(ws):
    sp = splus_of(rho_full(ws))
    assert sp is not None, "even word not parity-preserving?!"
    return sp

# intertwining: rho(M) op(x) rho(M)^-1 = op(Mx) -- the decomposition and
# the module action cohere
int_ok = True
for M, ws in zip(OMEGA_GENS, DECOMPS):
    P = rho_full(ws)
    Pinv = rho_full(list(reversed(ws)))          # ops are involutions
    int_ok &= (mmul(P, Pinv) == IDM16)
    for u in UF:
        int_ok &= (mmul(P, mmul(OPS[u], Pinv)) == OPS[mvec(M, u)])
check("X3a", "for every generator: rho(g) op(x) rho(g)^-1 = op(g x) on "
      "the whole frame basis (the spin word implements EXACTLY the "
      "orthogonal action it was built from); rho(g) parity-even, "
      "restriction to S+ well-posed", int_ok
      and all(splus_of(rho_full(ws)) is not None for ws in DECOMPS))

# well-definedness A: alternative decompositions of the SAME matrix
WSAMPLE = [w for w in NONSING[:3]]
alt_ok = True; n_alt = 0
for gi in range(0, 26, 3):               # 9 generators sampled
    M = OMEGA_GENS[gi]
    P0 = rho_full(DECOMPS[gi])
    for w in WSAMPLE:
        tw = transvect(w)
        alt1 = decompose(mmul(M, tw)) + [w]      # M = (M t_w) t_w
        alt2 = [w] + decompose(mmul(tw, M))      # M = t_w (t_w M)
        for aw in (alt1, alt2):
            n_alt += 1
            alt_ok &= (word_matrix(aw) == M and rho_full(aw) == P0)
check("X3b", "WELL-DEFINEDNESS (empirical): %d alternative transvection "
      "words for 9 sampled generators (append/prepend t_w tricks, "
      "genuinely different words) ALL give the identical 16x16 spin "
      "matrix -- over F2 the +-1 spin ambiguity collapses (theory line "
      "[P]: the central units of the even Clifford algebra of plus type "
      "over F2 are trivial, so equal vector actions force equal spin "
      "elements); no amendment needed" % n_alt, alt_ok)

def rand_elem():
    M = IDM8
    for _ in range(random.randrange(3, 9)):
        M = mmul(M, OMEGA_GENS[random.randrange(26)])
    return M

hom_ok = True
for _ in range(100):
    Ga = rand_elem(); Gb = rand_elem()
    ra = rho_splus(decompose(Ga))
    rb = rho_splus(decompose(Gb))
    rab = rho_splus(decompose(mmul(Ga, Gb)))
    hom_ok &= (mmul(ra, rb) == rab)
check("X3c", "HOMOMORPHISM: rho+(g1) rho+(g2) = rho+(g1 g2) on 100 "
      "random word pairs in the Omega-generators, each factor AND the "
      "product decomposed independently -- exact every time", hom_ok)

ntr_ok = all(rho_splus(ws) != IDM8 for ws, M in zip(DECOMPS, OMEGA_GENS)
             if M != IDM8)
ker_ok = True
for _ in range(50):
    G = rand_elem()
    if G == IDM8: continue
    ker_ok &= (rho_splus(decompose(G)) != IDM8)
check("X3d", "FAITHFULNESS: rho+ nontrivial on every generator and on 50 "
      "random nonidentity elements (no kernel witness); theory line: "
      "Omega ~= O8+(2) is SIMPLE [P cited: ATLAS], so the nontrivial "
      "homomorphism rho+ is faithful -- [C] computed nontriviality + [P]",
      ntr_ok and ker_ok)
print("[t=%6.1fs] stage 3 done" % (time.time() - T0))
stage_gate(3)

# ======================================================================
banner("STAGE 4 -- Q+ and T+: the invariant quadratic form on S+ and the "
       "isometry transport back to (V,q)")
# ======================================================================
RHOP = [rho_splus(ws) for ws in DECOMPS]
rowsQ = []
for M in RHOP:
    for x in range(256):
        y = mvec(M, x)
        r = 0
        for t, (i, j) in enumerate(mon):
            if (((x >> i) & (x >> j)) ^ ((y >> i) & (y >> j))) & 1:
                r |= 1 << t
        if r: rowsQ.append(r)
NSP = f2_nullspace(rowsQ, 36)
check("X4a", "the space of rho+(Omega)-invariant quadratic forms on S+ "
      "is EXACTLY 1-dimensional (exact nullspace over all 26 generators, "
      "all 256 points -- the dimension itself is the check)",
      len(NSP) == 1, "nullspace dim %d" % len(NSP))
cQP = NSP[0]
QP = []
for x in range(256):
    v = 0
    for t, (i, j) in enumerate(mon):
        if (cQP >> t) & 1 and ((x >> i) & 1) and ((x >> j) & 1): v ^= 1
    QP.append(v)
def BP(x, y): return QP[x ^ y] ^ QP[x] ^ QP[y]
nsingP = sum(1 for x in range(1, 256) if QP[x] == 0)
radP = [x for x in range(1, 256)
        if all(BP(x, y) == 0 for y in range(256))]
invP = all(QP[mvec(M, x)] == QP[x] for M in RHOP for x in range(256))
check("X4b", "Q+ is nondegenerate, PLUS-TYPE (135 singular nonzero / 120 "
      "nonsingular -- the plus-type count), invariant under all 26 "
      "generators' rho+ (verified pointwise)",
      nsingP == 135 and not radP and invP,
      "singular nonzero %d" % nsingP)
def ts_witness(pairs, qtab):
    us = [p[0] for p in pairs]
    if f2_rank(us) != 4: return False
    for bits in range(16):
        w0 = 0
        for k in range(4):
            if (bits >> k) & 1: w0 ^= us[k]
        if qtab[w0] != 0: return False
    return True
HBP = hyperbolic_basis(QP)
UP = basis_matrix(HBP)
TP = mmul(U2, f2_matinv(UP))        # T+: (S+,Q+) -> (V,q)
TPi = f2_matinv(TP)
tp_ok = (TPi is not None
         and all(qvals[mvec(TP, x)] == QP[x] for x in range(256)))
check("X4c", "T+: (S+,Q+) -> (V,q) built by the sealed Gram-Schmidt "
      "transport (Witt-index-4 witnesses on both sides); q(T+ x) = Q+(x) "
      "for ALL 256 x -- an explicit isometry",
      ts_witness(HBP, QP) and tp_ok)

def tau_of(M):
    """tau(g) = T+ rho+(g) T+^-1 -- defined on any Dickson-0 q-isometry
    via transvection decomposition (well-defined by X3b/X3c)."""
    return mmul(TP, mmul(rho_splus(decompose(M)), TPi))
print("[t=%6.1fs] stage 4 done" % (time.time() - T0))
stage_gate(4)

# ======================================================================
banner("STAGE 5 -- XB2: tau lands in the roof's world and is an "
       "automorphism of Omega")
# ======================================================================
TAU_GENS = [tau_of(M) for M in OMEGA_GENS]
in_ok = all(all(qvals[mvec(M, x)] == qvals[x] for x in range(256))
            and dickson(M) == 0 for M in TAU_GENS)
check("X5a", "every tau(generator) is a q-isometry (all 256 points) with "
      "Dickson invariant 0: tau maps the generators into Omega(q) "
      "[P cited: Omega = ker(Dickson) inside O(q)]; hence tau(<gens>) "
      "<= Omega", in_ok)
homt_ok = True
for _ in range(20):
    Ga = rand_elem(); Gb = rand_elem()
    homt_ok &= (mmul(tau_of(Ga), tau_of(Gb)) == tau_of(mmul(Ga, Gb)))
check("X5b", "tau(g1) tau(g2) = tau(g1 g2) on 20 random pairs (each side "
      "decomposed independently): the homomorphism property inherits "
      "from rho+ (tau is conjugation-by-T+ of rho+)", homt_ok)
note("image-order argument (stated cleanly): tau = conj_T+ o rho+ with")
note("rho+ faithful (X3d: nontrivial + Omega simple [P]).  A faithful")
note("homomorphism Omega -> Omega between FINITE groups of equal order")
note("174182400 is bijective, so tau is an AUTOMORPHISM of Omega and")
note("|<tau(gens)>| = |tau(Omega)| = |Omega| = 174182400 -- no BSGS")
note("needed; the containment tau(Omega) <= Omega is X5a + closure.")
check("X5c", "tau is an automorphism of Omega: faithful (X3d) + into "
      "Omega (X5a) + |Omega| finite => bijective  [C modulo the two "
      "cited [P] facts]", in_ok and ntr_ok and ker_ok)
print("[t=%6.1fs] stage 5 done" % (time.time() - T0))
stage_gate(5)

# ======================================================================
banner("STAGE 6 -- XB3: THE TURN -- orbit-signature triples of "
       "tau^k(C-bar) (REGISTERED EXPECTATION resolved here)")
# ======================================================================
# --- the sealed Stone W instrument, reloaded READ-ONLY and re-calibrated
TS_F = os.path.join(CACHE_W, "ts_subspaces.npz")
z = np.load(TS_F)
SUBS = [frozenset(int(x) for x in row) for row in z["s"]]
sub_idx = {S: i for i, S in enumerate(SUBS)}
N4 = len(SUBS)
subs_ok = (N4 == 270 and all(len(S) == 16 and 0 in S for S in SUBS)
           and all(all(qvals[x] == 0 for x in S) for S in SUBS)
           and all(f2_rank([x for x in S if x]) == 4 for S in SUBS))
cls = [0] * N4
S0 = SUBS[0]
for i in range(1, N4):
    d = (len(S0 & SUBS[i])).bit_length() - 1
    cls[i] = 0 if d % 2 == 0 else 1
FAM_A = [i for i in range(N4) if cls[i] == 0]
FAM_B = [i for i in range(N4) if cls[i] == 1]
def sub_image_perm(M):
    out = []
    for S in SUBS:
        S2 = frozenset(mvec(M, x) for x in S)
        out.append(sub_idx[S2])
    return tuple(out)
clsa = np.array(cls)
pres_ok = all((clsa[list(sub_image_perm(M))] == clsa).all()
              for M in OMEGA_GENS)
W0m = M2_of(S240[0])
swap_ok = (clsa[list(sub_image_perm(W0m))] == 1 - clsa).all()
check("X6a", "sealed TS enumeration reloaded: 270 maximal totally "
      "singular 4-subspaces; families recomputed by the RECORDED "
      "convention (dim(U cap V) even = same family, class of SUBS[0] = "
      "A): sizes [135,135]; every Omega-generator PRESERVES each family, "
      "the reflection s1-bar SWAPS them (instrument re-calibrated)",
      subs_ok and len(FAM_A) == 135 and len(FAM_B) == 135
      and pres_ok and bool(swap_ok))

def orbit_sizes_points(mats, pts):
    idx = {p: i for i, p in enumerate(pts)}
    seen = [False] * len(pts)
    sizes = []
    for i0 in range(len(pts)):
        if seen[i0]: continue
        orb = [i0]; seen[i0] = True; fr = [pts[i0]]
        while fr:
            x = fr.pop()
            for M in mats:
                y = mvec(M, x)
                j = idx[y]
                if not seen[j]:
                    seen[j] = True; orb.append(j); fr.append(y)
        sizes.append(len(orb))
    return sorted(sizes)

def orbit_sizes_subs(mats, fam):
    perms = [sub_image_perm(M) for M in mats]
    fam_set = set(fam)
    seen = set()
    sizes = []
    for i0 in fam:
        if i0 in seen: continue
        orb = {i0}; fr = [i0]
        while fr:
            i = fr.pop()
            for p in perms:
                j = p[i]
                assert j in fam_set, "family not preserved!"
                if j not in orb:
                    orb.add(j); fr.append(j)
        seen |= orb
        sizes.append(len(orb))
    return sorted(sizes)

def signature(mats):
    return (tuple(orbit_sizes_points(mats, SING)),
            tuple(orbit_sizes_subs(mats, FAM_A)),
            tuple(orbit_sizes_subs(mats, FAM_B)))

SIG_VEC = ((63, 72), (135,), (135,))          # sealed Stone W values
SIG_SPIN = ((135,), (135,), (63, 72))
SIG_K3 = ((135,), (63, 72), (135,))
K3m = [mmul(W0m, mmul(A, W0m)) for A in (A1, A2)]
sigC = signature(Cmats)
sigS = signature([A1, A2])
sigK3 = signature(K3m)
check("X6b", "instrument calibration: the signatures of C-bar, K_spin, "
      "K3 reproduce the SEALED Stone W triples verbatim (vector "
      "[63,72]|[135]|[135]; K_spin [135]|[135]|[63,72]; K3 "
      "[135]|[63,72]|[135])",
      sigC == SIG_VEC and sigS == SIG_SPIN and sigK3 == SIG_K3,
      "C %s / S %s / K3 %s" % (sigC, sigS, sigK3))

t1C = [tau_of(M) for M in Cmats]
t2C = [tau_of(M) for M in t1C]
t3C = [tau_of(M) for M in t2C]
sig_t1C = signature(t1C)
sig_t2C = signature(t2C)
sig_t3C = signature(t3C)
sig_t1S = signature([tau_of(A1), tau_of(A2)])
sig_t1K3 = signature([tau_of(M) for M in K3m])

def sig_name(s):
    return {SIG_VEC: "VECTOR   [63,72]|[135]|[135]",
            SIG_SPIN: "K_spin   [135]|[135]|[63,72]",
            SIG_K3: "K3       [135]|[63,72]|[135]"}.get(s, "OTHER %s" % (s,))

print("\n  THE CYCLE MAP UNDER tau (positioned orbit-signature triples,")
print("  points | family A | family B -- the sealed SM-031 instrument):")
for lbl, s in (("C-bar          ", sigC), ("tau(C-bar)     ", sig_t1C),
               ("tau^2(C-bar)   ", sig_t2C), ("tau^3(C-bar)   ", sig_t3C),
               ("K_spin         ", sigS), ("tau(K_spin)    ", sig_t1S),
               ("K3             ", sigK3), ("tau(K3)        ", sig_t1K3)):
    print("    %s : points %s | A %s | B %s   = %s"
          % (lbl, list(s[0]), list(s[1]), list(s[2]), sig_name(s)))

spin_sigs = {SIG_SPIN, SIG_K3}
turn_ok = (sig_t1C in spin_sigs and sig_t2C in spin_sigs
           and sig_t1C != sig_t2C and sig_t3C == SIG_VEC)
if turn_ok:
    check("X6c", "REGISTERED EXPECTATION RESOLVED -- PASS: tau(C-bar) "
          "has a SPIN signature (%s), tau^2(C-bar) the OTHER spin "
          "signature (%s), tau^3(C-bar) is back to the VECTOR signature: "
          "tau cycles vector -> spin -> spin -> vector"
          % (sig_name(sig_t1C).split()[0], sig_name(sig_t2C).split()[0]),
          True)
    EXPECT = "PASS (tau realizes the outer 3-cycle)"
else:
    check("X6c", "REGISTERED EXPECTATION RESOLVED -- INVERTED (full "
          "prominence): tau does NOT cycle; the computed class action is "
          "tau(C)=%s, tau^2(C)=%s, tau^3(C)=%s -- tau SWAPS vector <-> "
          "K_spin and FIXES K3 (an outer INVOLUTION on classes, not the "
          "3-cycle); the diagnosis and the corrected turner follow "
          "(X6d/X6e), the finding is recorded at full prominence"
          % (sig_name(sig_t1C).split()[0], sig_name(sig_t2C).split()[0],
             sig_name(sig_t3C).split()[0]), False)
    EXPECT = ("INVERTED: tau = the (vector K_spin) swap fixing K3 -- a "
              "THIRD outer involution, not the 3-cycle; the 3-cycle is "
              "tau' = conj_ref o tau (X6e/X7d)")

# --- diagnosis (mandated by the brief for the inverted outcome)
sig_refC = signature([mmul(W0m, mmul(M, W0m)) for M in Cmats])
note("diagnosis: the class actions on {VECTOR, K_spin, K3} found so far:")
note("  inner (Omega):        identity            [Stone W W3e]")
note("  reflection conj_s1:   fixes VECTOR, swaps K_spin <-> K3  "
     "[verified: conj_s1(C-bar) sig = %s; K3 = conj_s1(K_spin), W3b]"
     % sig_name(sig_refC).split()[0])
note("  tau (this stone):     fixes K3, swaps VECTOR <-> K_spin  [X6c]")
note("tau's class action differs from the identity AND from the "
     "reflection's, so tau is")
note("neither inner nor in the reflection coset: it is a THIRD outer "
     "involution.  The three")
note("involutions and their products exhaust S3: composing tau with the "
     "reflection MUST give")
note("the 3-cycle.  WHY tau inverted: the declared Gram-Schmidt "
     "transport T+ is one of the")
note("two isometry cosets (S+,Q+) -> (V,q); the sealed one lands in the "
     "coset whose tau")
note("swaps -- correcting T+ by the Dickson-odd reflection s1-bar "
     "(T+' = s1-bar . T+, still")
note("an isometry) flips the coset.  The construction route is "
     "unchanged; only the open")
note("choice of T+ is resolved to the OTHER coset.")
check("X6d", "tau is outer and NOT in the reflection coset: its class "
      "action (swap vector/K_spin, fix K3) differs from the identity "
      "and from the reflection's (fix vector, swap K_spin/K3) -- with "
      "the reflection, the FULL S3 on the three classes is realized by "
      "explicit machines  [C via positioned-signature conjugacy "
      "invariance, sealed Stone W W3e]",
      sig_t1C == SIG_SPIN and sig_t2C == SIG_VEC
      and sig_t1K3 == SIG_K3 and sig_refC == SIG_VEC)

def tau_p(M):
    """the CORRECTED turner tau'(g) = s1-bar tau(g) s1-bar = "
    "(s1-bar T+) rho+(g) (s1-bar T+)^-1 -- transport by T+' = s1-bar T+,
    the other isometry coset."""
    return mmul(W0m, mmul(tau_of(M), W0m))
assert mmul(W0m, W0m) == IDM8
tp1C = [tau_p(M) for M in Cmats]
tp2C = [tau_p(M) for M in tp1C]
tp3C = [tau_p(M) for M in tp2C]
sig_p1C = signature(tp1C)
sig_p2C = signature(tp2C)
sig_p3C = signature(tp3C)
sig_p1S = signature([tau_p(A1), tau_p(A2)])
sig_p1K3 = signature([tau_p(M) for M in K3m])
print("\n  THE CYCLE MAP UNDER tau' = conj_s1 o tau (the corrected "
      "turner):")
for lbl, s in (("C-bar          ", sigC), ("tau'(C-bar)    ", sig_p1C),
               ("tau'^2(C-bar)  ", sig_p2C), ("tau'^3(C-bar)  ", sig_p3C),
               ("tau'(K_spin)   ", sig_p1S), ("tau'(K3)       ", sig_p1K3)):
    print("    %s : points %s | A %s | B %s   = %s"
          % (lbl, list(s[0]), list(s[1]), list(s[2]), sig_name(s)))
turn_p_ok = (sig_p1C in spin_sigs and sig_p2C in spin_sigs
             and sig_p1C != sig_p2C and sig_p3C == SIG_VEC
             and sig_p1S == SIG_VEC and sig_p1K3 != sig_p1C
             and sig_p1K3 in spin_sigs)
check("X6e", "THE TURN, CONSTRUCTED: tau'(C-bar) has a SPIN signature, "
      "tau'^2(C-bar) the OTHER spin signature, tau'^3(C-bar) the VECTOR "
      "signature; the full class map is the 3-cycle vector -> K3 -> "
      "K_spin -> vector.  tau' moves the points column, which the "
      "identity and the reflection's class action both preserve, so "
      "tau' is NOT inner and NOT in the reflection coset: tau' REALIZES "
      "THE OUTER 3-CYCLE (the brief's performer, reached through the "
      "recorded T+-coset correction)", turn_p_ok)
print("[t=%6.1fs] stage 6 done" % (time.time() - T0))
stage_gate(6)

# ======================================================================
banner("STAGE 7 -- XB4: the intertwiner solves (tau^3 as registered; "
       "tau^2 and tau'^3 as the diagnosis requires)")
# ======================================================================
def intertwiner(pairs):
    """exact F2 solve of {h g = g' h} over the generator pairs
    (64 unknowns h_ij); returns (dim, h or None)."""
    rows_h = []
    for G, TG in pairs:
        for j in range(8):
            for i in range(8):
                r = 0
                k = G[j]
                while k:
                    b = k & -k; kk = b.bit_length() - 1; k ^= b
                    r ^= 1 << (8 * kk + i)          # (h G)_ij term
                for m2 in range(8):
                    if (TG[m2] >> i) & 1:
                        r ^= 1 << (8 * j + m2)      # (G' h)_ij term
                if r: rows_h.append(r)
    NH = f2_nullspace(rows_h, 64)
    if len(NH) != 1: return len(NH), None
    return 1, tuple((NH[0] >> (8 * k)) & 255 for k in range(8))

def conj_checks(pairs, Hm):
    Hi = f2_matinv(Hm)
    return (Hi is not None
            and all(qvals[mvec(Hm, x)] == qvals[x] for x in range(256))
            and all(mmul(Hm, mmul(G, Hi)) == TG for G, TG in pairs))

T3_GENS = [tau_of(tau_of(tau_of(M))) for M in OMEGA_GENS]
d3, H3m = intertwiner(list(zip(OMEGA_GENS, T3_GENS)))
check("X7a", "AS REGISTERED, RESOLVED INVERTED (full prominence): the "
      "intertwiner system {h g = tau^3(g) h} has solution space dim 0 "
      "-- tau^3 is NOT inner (consistent with X6c: tau has order 2 mod "
      "Inn, so tau^3 = tau mod Inn, and tau is outer); the brief's "
      "expected dim 1 belongs to tau'^3, solved below (X7d)",
      d3 == 0, "nullspace dim %d" % d3)

T2_GENS = [tau_of(tau_of(M)) for M in OMEGA_GENS]
d2, H2m = intertwiner(list(zip(OMEGA_GENS, T2_GENS)))
h2_ok = H2m is not None and conj_checks(list(zip(OMEGA_GENS, T2_GENS)),
                                        H2m)
check("X7b", "tau^2 IS inner, explicitly: intertwiner space dim 1 (V is "
      "Omega-irreducible => uniqueness); h2 invertible, a q-isometry, "
      "Dickson %s, and tau^2(g) = h2 g h2^-1 for ALL 26 generators "
      "(exact): <tau> ~= Z2 modulo Inn -- the constructed tau is the "
      "THIRD outer involution, on the nose"
      % (dickson(H2m) if H2m else "-"), d2 == 1 and h2_ok
      and H2m is not None and dickson(H2m) == 0,
      "dim %d, h2 columns %s" % (d2, (H2m,)))

TP3_GENS = [tau_p(tau_p(tau_p(M))) for M in OMEGA_GENS]
dp, HPm = intertwiner(list(zip(OMEGA_GENS, TP3_GENS)))
hp_ok = HPm is not None and conj_checks(list(zip(OMEGA_GENS, TP3_GENS)),
                                        HPm)
check("X7d", "tau'^3 IS inner, explicitly (the brief's XB4 content, on "
      "the corrected turner): intertwiner space dim EXACTLY 1; h' "
      "invertible, a q-isometry, Dickson %s, and tau'^3(g) = h' g h'^-1 "
      "for ALL 26 generators (exact)"
      % (dickson(HPm) if HPm else "-"), dp == 1 and hp_ok
      and HPm is not None and dickson(HPm) == 0,
      "dim %d, h' columns %s" % (dp, (HPm,)))
check("X7e", "hence tau'^3 is inner while tau' is not (X6e): the class "
      "of tau' in Out(Omega) has order EXACTLY 3 -- <tau'> ~= Z3 modulo "
      "inner: the turn constructed, order three on the nose",
      dp == 1 and hp_ok and turn_p_ok)
print("[t=%6.1fs] stage 7 done" % (time.time() - T0))
stage_gate(7)

# ======================================================================
banner("STAGE 8 -- XB5: the roof-clock question posed; the cheap "
       "pure-spinor datum")
# ======================================================================
print("""
  THE ROOF-CLOCK QUESTION (final form, with the turner in hand):
  SOUGHT: an operator Phi -- promotion/rowmotion-like, acting on a state
  space that the roof R = W+(E8) acts on (candidates: the 135+270-element
  triality geometry of (L/2L, q); a lattice-level object above it) --
  whose INDUCED action on subgroup classes of Omega = R/<-1> is tau: the
  footprint of Phi cycles vector -> spin -> spin -> vector, the way Psi's
  footprint at E7 is iota.  tau is now an explicit matrix machine (T+,
  rho+, decompose -- this stone), so the hunt is a SEARCH FOR Phi WITH
  FOOTPRINT tau, not for the turn itself.  The full hunt is the successor
  -- named, not computed.""")
ann_dims = []
ann_fams = []
ann_idx = []
pure_ok = True
for i8 in range(1, 256):
    if QP[i8] != 0: continue
    xs = 0
    for i in range(8):
        if (i8 >> i) & 1: xs |= 1 << EVEN[i]
    imgs = []
    for k in range(8):
        imgs.append(mvec(OPS[1 << k], xs))
    ann = [v for v in range(256)
           if mvec(OPS[v], xs) == 0]      # rank check via full census
    dim = (len(ann)).bit_length() - 1
    ann_dims.append(dim)
    if dim != 4:
        pure_ok = False; continue
    Sf = frozenset(ann)
    ok_ts = all(qvals[v] == 0 for v in ann) and Sf in sub_idx
    pure_ok &= ok_ts
    if ok_ts:
        j = sub_idx[Sf]
        ann_idx.append(j)
        ann_fams.append(cls[j])
distinct = len(set(ann_idx))
famset = sorted(set(ann_fams))
check("X8a", "CHEAP DATUM (pure-spinor correspondence): every one of the "
      "135 Q+-singular spinors in S+ has annihilator {v : op(v).x = 0} "
      "a maximal totally singular 4-subspace of (V,q) (a PURE spinor); "
      "the 135 annihilators are pairwise DISTINCT and all lie in ONE "
      "family -- composing with T+^-1 gives an explicit BIJECTION "
      "{135 singular points of (V,q)} <-> {135 solids of family %s}: "
      "the turner's geometry transports points to one solid family"
      % ("A" if famset == [0] else "B" if famset == [1] else "?"),
      pure_ok and distinct == 135 and len(famset) == 1,
      "dims %s, distinct %d, families %s"
      % (sorted(Counter(ann_dims).items()), distinct, famset))

# --- witnesses for the record (own cache only)
wit = {"brief_sha": sha,
       "frame_e": EVEC, "frame_f": FVEC,
       "Qplus_coeff_mask": cQP,
       "Qplus_dim_invariant_space": len(NSP),
       "Tplus_cols": list(TP),
       "tau_gen_cols": [list(M) for M in TAU_GENS],
       "decomp_lengths": lens,
       "signatures": {
           "C": [list(x) for x in sigC],
           "tauC": [list(x) for x in sig_t1C],
           "tau2C": [list(x) for x in sig_t2C],
           "tau3C": [list(x) for x in sig_t3C],
           "Kspin": [list(x) for x in sigS],
           "tauKspin": [list(x) for x in sig_t1S],
           "K3": [list(x) for x in sigK3],
           "tauK3": [list(x) for x in sig_t1K3],
           "taupC": [list(x) for x in sig_p1C],
           "taup2C": [list(x) for x in sig_p2C],
           "taup3C": [list(x) for x in sig_p3C],
           "taupKspin": [list(x) for x in sig_p1S],
           "taupK3": [list(x) for x in sig_p1K3]},
       "intertwiner_dims": {"tau3": d3, "tau2": d2, "taup3": dp},
       "h2_cols": list(H2m) if H2m else None,
       "hprime_cols": list(HPm) if HPm else None,
       "expectation": EXPECT,
       "pure_spinor_family": famset}
json.dump(wit, open(os.path.join(CACHE_X, "witnesses_x.json"), "w"),
          indent=1)
note("witnesses written to %s/witnesses_x.json" % CACHE_X)

print("\n" + "=" * 78)
print("VERDICT: %d PASS, %d FAIL%s"
      % (PASS, FAIL, ("  FAILED: %s" % FAILED) if FAILED else ""))
print("registered expectation (XB3): %s" % EXPECT)
print("[t=%6.1fs] total" % (time.time() - T0))
print("=" * 78)
