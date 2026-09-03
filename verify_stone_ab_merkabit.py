# -*- coding: utf-8 -*-
r"""verify_stone_ab_merkabit.py -- STONE AB: THE MERKABIT UNDER THE STILL POINT

Brief: BRIEF_STONE_AB_MERKABIT_STILLPOINT.md (lock BRIEF_STONE_AB_LOCK.sha256,
re-verified as check AB0: 6f907705b652369d0f569a89b5ba2e7e2c71d683fe6b34e5a5595b23352f90cb).

Question: where does the 56-machine sit in the roof's state space and what
does the still point G2(2) do to it?  Identification (declared): the 56 E7
weights = the 56 E8 roots with <r,alpha> = 1 = the 56 nonsingular u with
B(u,v) = 1 (matched to the sealed scar56_data.json vertices bijectively by
Dynkin label); iota = t_v; the 64 phase points of Stone Q = the coset
{x : B(x,v)=1} mod v (28 odd = bitangents, 36 even = thetas).

ROUTE (bars AB1-AB6): AB1 identification + iota = t_v + Psi/pr do not extend
linearly; AB2 the counts; AB3 G2(2)'s orbits on 56/28/36/63 (registered:
transitive on 28, 36, 63 with stabilizers 432, 336, 192); AB4 theta <-> seven
bijection (registered), the bridge copy's [1,7,7,21]; AB5 |W(E6) cap G2(2)|
and the 192; AB6 Psi/pr against the roof's incidence on the board (the
well-posed substitute for the twisted-Coxeter comparison; see brief).

MACHINERY: Stone X + SM-038 replay VERBATIM from verify_stone_aa_roofclock.py;
scar56_data.json (SM-005) READ-ONLY; own cache _stone_ab_cache/.  No
registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ab_merkabit.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_ab_merkabit.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True); LOG.write(s + "\n"); LOG.flush()
PASS = 0; FAIL = 0; FAILED = []
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:
        FAIL += 1; FAILED.append(tag)
    say(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))
def banner(t):
    say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))

CACHE_U = "_stone_u_cache"; CACHE_V = "_stone_v_cache"
CACHE_X = "_stone_x_cache"; CACHE_L = "_liftlaw_cache"
CACHE_Z = "_stone_z_cache"; CACHE_AB = "_stone_ab_cache"
os.makedirs(CACHE_AB, exist_ok=True)
random.seed(20260903)

# ======================================================================
# permutation + F2 utilities, BSGS, sift  (VERBATIM from SM-038)
# ======================================================================
def pmul(a, b): return tuple(a[x] for x in b)
def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def pident(n): return tuple(range(n))
def ppow(p, e):
    if e < 0: p = pinv(p); e = -e
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
def comm(a, b): return pmul(pmul(a, b), pmul(pinv(a), pinv(b)))
def profile_of(G):
    return dict(sorted(Counter(pord(g) for g in G).items()))

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

# BSGS -- verbatim algorithm (Schur-pin / lift-law); base returned too
def make_bsgs_full(gen_list, deg):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    if not strong:
        return 1, (lambda g: g == E), [], []
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
                        base.append(next(p for p in range(deg) if h[p] != p))
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
    return o, is_member, transv, base
def enumerate_group_np(transv, deg):
    L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
         for T in transv]
    EN = L[-1]
    for j in range(len(L) - 2, -1, -1):
        EN = np.concatenate([L[j][i][EN] for i in range(L[j].shape[0])])
    return EN
def member_mask(EN, base, transv):
    """vectorized sift of every row of EN through (base, transv): the same
    strip as is_member, applied to all rows at once, level by level."""
    N, deg = EN.shape
    h = EN.copy(); alive = np.ones(N, dtype=bool)
    ar = np.arange(deg, dtype=np.uint8)
    for i, T in enumerate(transv):
        x = h[:, base[i]]
        keys = np.array(list(T.keys()), dtype=np.uint8)
        alive &= np.isin(x, keys)
        for k, t in T.items():
            sel = alive & (x == k)
            if sel.any():
                tinv = np.array(pinv(t), dtype=np.uint8)
                h[sel] = tinv[h[sel]]
    return alive & (h == ar).all(axis=1)

say("=" * 78)
say("STONE AB -- THE MERKABIT UNDER THE STILL POINT")
say("the 56-board inside the V-block; iota = t_v; G2(2) on 56 / 28 / 36 / 63;")
say("theta <-> seven; Psi against the roof's incidence   [caches READ-ONLY]")
say("=" * 78)

# ======================================================================
banner("STAGE 0 -- AB0: brief lock; Stone X + SM-038 machinery replayed VERBATIM")
# ======================================================================
BRIEF = "BRIEF_STONE_AB_MERKABIT_STILLPOINT.md"
LOCK = "6f907705b652369d0f569a89b5ba2e7e2c71d683fe6b34e5a5595b23352f90cb"
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AB0", "the brief is sha-locked: sha256(%s) equals the value in "
      "BRIEF_STONE_AB_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

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
Gm = np.array(GRAM, dtype=np.int64)
Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
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
    qvals.append((n2 // 2) % 2)
def Bform(x, y): return qvals[x ^ y] ^ qvals[x] ^ qvals[y]
sidx = [ridx[a] for a in SIMPLE]
def M2_of(w):
    return tuple(rmask[w[sidx[j]]] for j in range(8))
def dickson(M):
    return f2_rank([M[j] ^ (1 << j) for j in range(8)]) & 1
SING = [m for m in range(1, 256) if qvals[m] == 0]
NONSING = [m for m in range(256) if qvals[m] == 1]
NS_IDX = {m: i for i, m in enumerate(NONSING)}
def perm_of(M):
    """the action of a q-isometry on the 120 nonsingular vectors."""
    return tuple(NS_IDX[mvec(M, v)] for v in NONSING)
def mat_of_perm(p):
    """inverse of perm_of: the standard basis vectors are nonsingular."""
    return tuple(NONSING[p[NS_IDX[1 << j]]] for j in range(8))
def is_isometry(M):
    return all(qvals[mvec(M, x)] == qvals[x] for x in range(256))

gz = np.load(os.path.join(CACHE_U, "stab_derived_gens.npz"))["g"]
Cgens = [tuple(int(x) for x in gz[j]) for j in range(gz.shape[0])]
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
Tmat = mmul(U2, f2_matinv(U1))
Ti = f2_matinv(Tmat)
A1 = mmul(Tmat, mmul(g1m, Ti)); A2 = mmul(Tmat, mmul(g2m, Ti))
Cmats = [M2_of(g) for g in Cgens]
OMEGA_GENS = Cmats + [A1, A2]
assert all(is_isometry(M) and dickson(M) == 0 for M in OMEGA_GENS)

# --- module, decomposition, spin lift (verbatim Stone X stages 1-4)
HB = hyperbolic_basis(qvals)
EVEC = [HB[k][0] for k in range(4)]; FVEC = [HB[k][1] for k in range(4)]
UF = tuple(EVEC + FVEC); UFi = f2_matinv(UF)
E_OP = [tuple((1 << (S | (1 << i))) if not (S >> i) & 1 else 0
              for S in range(16)) for i in range(4)]
F_OP = [tuple((1 << (S & ~(1 << i))) if (S >> i) & 1 else 0
              for S in range(16)) for i in range(4)]
ZERO16 = (0,) * 16
def op_of(v):
    c = mvec(UFi, v)
    M = ZERO16
    for i in range(4):
        if (c >> i) & 1: M = madd(M, E_OP[i])
        if (c >> (4 + i)) & 1: M = madd(M, F_OP[i])
    return M
OPS = [op_of(v) for v in range(256)]
def transvect(v):
    return tuple((1 << j) ^ (v if Bform(1 << j, v) else 0)
                 for j in range(8))
ANCHORS = [1 << j for j in range(8)]
assert all(qvals[a] == 1 for a in ANCHORS)
def _route(y, u, fixed):
    if y == u: return []
    if Bform(y, u) == 1:
        return [y ^ u]
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
def word_matrix(ws):
    M = IDM8
    for v in ws: M = mmul(M, transvect(v))
    return M
def decompose(M):
    got = _DECOMP_MEMO.get(M)
    if got is not None: return got
    cur = M; word = []; fixed = []
    for u in ANCHORS:
        y = mvec(cur, u)
        for v in _route(y, u, fixed):
            cur = mmul(transvect(v), cur)
            word.append(v)
        fixed.append(u)
    assert cur == IDM8, "reduction did not reach identity"
    assert word_matrix(word) == M, "decomposition does not reproduce M"
    _DECOMP_MEMO[M] = word
    return word
EVEN = [S for S in range(16) if bin(S).count("1") % 2 == 0]
EPOS = {S: i for i, S in enumerate(EVEN)}
EVEN_MASK = sum(1 << S for S in EVEN)
def rho_full(ws):
    P = IDM16
    for v in ws: P = mmul(P, OPS[v])
    return P
def splus_of(P):
    cols = []
    for S in EVEN:
        c = P[S]
        if c & ~EVEN_MASK: return None
        cols.append(sum(((c >> T) & 1) << EPOS[T] for T in EVEN))
    return tuple(cols)
def rho_splus(ws):
    sp = splus_of(rho_full(ws))
    assert sp is not None
    return sp
DECOMPS = [decompose(M) for M in OMEGA_GENS]
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
assert len(NSP) == 1
cQP = NSP[0]
QP = []
for x in range(256):
    v = 0
    for t, (i, j) in enumerate(mon):
        if (cQP >> t) & 1 and ((x >> i) & 1) and ((x >> j) & 1): v ^= 1
    QP.append(v)
HBP = hyperbolic_basis(QP)
UP = basis_matrix(HBP)
TP = mmul(U2, f2_matinv(UP)); TPi = f2_matinv(TP)
def tau_of(M):
    return mmul(TP, mmul(rho_splus(decompose(M)), TPi))
W0m = M2_of(S240[0])
assert mmul(W0m, W0m) == IDM8
def tau_p(M):
    """tau'(g) = s1-bar tau(g) s1-bar  (the sealed corrected turner)."""
    return mmul(W0m, mmul(tau_of(M), W0m))
def intertwiner_space(pairs):
    """exact F2 solve of {h g = g' h} over the pairs; nullspace basis."""
    rows_h = []
    for G, TG in pairs:
        for j in range(8):
            for i in range(8):
                r = 0
                k = G[j]
                while k:
                    b = k & -k; kk = b.bit_length() - 1; k ^= b
                    r ^= 1 << (8 * kk + i)
                for m2 in range(8):
                    if (TG[m2] >> i) & 1:
                        r ^= 1 << (8 * j + m2)
                if r: rows_h.append(r)
    return f2_nullspace(rows_h, 64)
def mat_from_bits(v): return tuple((v >> (8 * k)) & 255 for k in range(8))
def conj_by(Hm, G):
    return mmul(Hm, mmul(G, f2_matinv(Hm)))
def good_intertwiners(pairs):
    """all invertible Dickson-0 q-isometries h in the solution space with
    h g h^-1 = g' on every pair (enumerated over the nullspace)."""
    NH = intertwiner_space(pairs)
    out = []
    for bits in range(1, 2 ** len(NH)):
        v = 0
        for k in range(len(NH)):
            if (bits >> k) & 1: v ^= NH[k]
        Hm = mat_from_bits(v)
        if f2_matinv(Hm) is None: continue
        if not is_isometry(Hm) or dickson(Hm) != 0: continue
        if all(conj_by(Hm, G) == TG for G, TG in pairs): out.append(Hm)
    return len(NH), out


# ======================================================================
# SM-038 replay: tau'' = inn(y^-1) o tau' and the still point G (7 s)
# ======================================================================
WX = json.load(open(os.path.join(CACHE_X, "witnesses_x.json")))
check("AB0a", "REPLAY cross-check: tau on the 26 generators and T+ "
      "reproduce the sealed Stone X witnesses byte-for-byte",
      [list(tau_of(M)) for M in OMEGA_GENS] == WX["tau_gen_cols"]
      and list(TP) == WX["Tplus_cols"])
aix = ridx[SIMPLE[0]]; ALPHA = rmask[aix]
assert qvals[ALPHA] == 1 and all(mvec(M, ALPHA) == ALPHA for M in Cmats)
Cperm = [perm_of(M) for M in Cmats]
oC, memC, trC, baseC = make_bsgs_full(Cperm, 120)
EN_C = enumerate_group_np(trC, 120)
TpC = [tau_p(M) for M in Cmats]
oT, memT, trT, baseT = make_bsgs_full([perm_of(M) for M in TpC], 120)
G_rows = EN_C[member_mask(EN_C, baseT, trT)]
G_set = set(tuple(int(x) for x in r) for r in G_rows)
G_list = sorted(G_set)
zf = os.path.join(CACHE_Z, "G_rows.npy")
same_G = (set(tuple(int(x) for x in r) for r in np.load(zf)) == G_set
          if os.path.exists(zf) else None)
def find_gens(elems, order, tries=60):
    for k in (2, 3):
        for _ in range(tries):
            gs = [random.choice(elems) for _ in range(k)]
            if len(closure(gs, cap=order + 5)) == order: return gs
    raise RuntimeError("no small generating set")
Ggens = find_gens(G_list, len(G_list))
Gmats = [mat_of_perm(p) for p in Ggens]
dY, Ys = good_intertwiners(list(zip(Gmats, [tau_p(M) for M in Gmats])))
assert len(Ys) == 1
Ym = Ys[0]; Yi = f2_matinv(Ym)
ZJ = json.load(open(os.path.join(CACHE_Z, "turner_normalized.json")))
def tau_pp(M): return mmul(Yi, mmul(tau_p(M), Ym))
ord3 = all(tau_pp(tau_pp(tau_pp(M))) == M for M in OMEGA_GENS)
check("AB0b", "SM-038 replayed: |G| = 12096 (exhaustive sift%s); y unique "
      "and equal to the sealed y_cols; tau'' fixes G's generators; "
      "tau''^3 = id on all 26 generators"
      % (", identical to the cached G_rows" if same_G else ""),
      len(G_list) == 12096 and (same_G in (True, None))
      and list(Ym) == ZJ["y_cols"]
      and all(tau_pp(M) == M for M in Gmats) and ord3 and oC == 1451520)
tick("stage 0 done")

# ======================================================================
banner("STAGE 1 -- AB1: the board identified -- 56 weights = 56 roots with <r,alpha>=1")
# ======================================================================
D56 = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D56["verts"]]
vidx = {v: k for k, v in enumerate(verts)}
PSI, PR, IOTA = D56["PSI"], D56["PR"], D56["IOTA"]
EDGES = D56["EDGES"]
C7 = [[ 2, 0,-1, 0, 0, 0, 0],
      [ 0, 2, 0,-1, 0, 0, 0],
      [-1, 0, 2,-1, 0, 0, 0],
      [ 0,-1,-1, 2,-1, 0, 0],
      [ 0, 0, 0,-1, 2,-1, 0],
      [ 0, 0, 0, 0,-1, 2,-1],
      [ 0, 0, 0, 0, 0,-1, 2]]
ALPHA_R = SIMPLE[0]
E7_ROOTS = [r for r in roots if dot4(r, ALPHA_R) == 0]
B56 = [r for r in roots if dot4(r, ALPHA_R) == 1]
assert len(E7_ROOTS) == 126 and len(B56) == 56
# a base of E7 from a generic functional (deterministic)
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
def fval(r): return sum(a * b for a, b in zip(FUNC, r))
pos = [r for r in E7_ROOTS if fval(r) > 0]
assert len(pos) == 63
posset = set(pos)
def is_sum(r):
    for s in pos:
        t = tuple(a - b for a, b in zip(r, s))
        if t in posset: return True
    return False
BASE = [r for r in pos if not is_sum(r)]
assert len(BASE) == 7
CART = [[dot4(a, b) for b in BASE] for a in BASE]
perm_nodes = None
for pi in itertools.permutations(range(7)):
    if all(CART[pi[i]][pi[j]] == C7[i][j] for i in range(7) for j in range(7)):
        perm_nodes = pi; break
assert perm_nodes is not None, "Cartan matrices do not align"
BETA = [BASE[perm_nodes[i]] for i in range(7)]     # data's node i -> our simple root
def label_of(r): return tuple(dot4(r, b) for b in BETA)
root_of_vert = {}
for r in B56:
    lab = label_of(r)
    assert lab in vidx, "label not in the sealed vertex set"
    root_of_vert[vidx[lab]] = r
bij = (len(root_of_vert) == 56)
mask_of_vert = {k: rmask[ridx[r]] for k, r in root_of_vert.items()}
vert_of_mask = {m: k for k, m in mask_of_vert.items()}
BOARD = sorted(mask_of_vert.values())
board_ok = (len(set(BOARD)) == 56 and all(qvals[u] == 1 and Bform(u, ALPHA) == 1 for u in BOARD)
            and set(BOARD) == {u for u in NONSING if Bform(u, ALPHA) == 1})
edge_ok = True
for u, i, w in EDGES:
    ru, rw = root_of_vert[u], root_of_vert[w]
    edge_ok &= (tuple(a - b for a, b in zip(ru, rw)) == BETA[i])
check("AB1a", "IDENTIFICATION: the 56 E8 roots r with <r,alpha> = 1 match the "
      "56 sealed vertices BIJECTIVELY by Dynkin label (E7 base built in "
      "alpha-perp from a generic functional, Cartan matrix aligned to the "
      "sealed C7 by node permutation %s); every one of the 84 crystal edges "
      "of colour i is r_u - r_w = beta_i; the 56 masks are exactly the "
      "nonsingular u with B(u,v) = 1 -- THE BOARD IS THE 56-ORBIT"
      % (perm_nodes,), bij and board_ok and edge_ok)
iota_ok = all(mask_of_vert[IOTA[k]] == mask_of_vert[k] ^ ALPHA for k in range(56))
iota_neg = all(tuple(-x for x in verts[k]) == verts[IOTA[k]] for k in range(56))
check("AB1b", "THE CHIRALITY BIT: the sealed IOTA is w -> -w on labels and, "
      "under the match, u -> u + v on masks -- iota = the transvection t_v "
      "of the shadow's defining vector (Dickson 1: outside Omega, exactly "
      "as SM-015 saw it vanish in the Clifford quotient)", iota_ok and iota_neg)
def perm_on_board(vperm):
    return {mask_of_vert[k]: mask_of_vert[vperm[k]] for k in range(56)}
PSI_M = perm_on_board(PSI); PR_M = perm_on_board(PR); IOTA_M = perm_on_board(IOTA)
def linear_extension(pm):
    """try to extend a permutation of the board to a linear map of V:
    pick 8 independent board vectors, define M, test on all 56 + isometry."""
    basis = []; imgs = []
    for u in BOARD:
        if f2_rank(basis + [u]) > len(basis):
            basis.append(u); imgs.append(pm[u])
        if len(basis) == 8: break
    if len(basis) < 8: return None
    # solve M basis_j = imgs_j : M = IMG * BASIS^-1
    Bm = tuple(basis); Im = tuple(imgs)
    Bi = f2_matinv(Bm)
    if Bi is None: return None
    M = mmul(Im, Bi)
    if any(mvec(M, u) != pm[u] for u in BOARD): return None
    if not is_isometry(M): return None
    return M
M_iota = linear_extension(IOTA_M)
M_psi = linear_extension(PSI_M)
M_pr = linear_extension(PR_M)
check("AB1c", "under the match: IOTA extends to the linear isometry t_v "
      "(Dickson %s); PSI and PR do NOT extend to any linear map of V "
      "consistent on the 56 -- Psi nonlinear, pr odd (SM-015/016), re-seen "
      "in the roof's coordinates" % (dickson(M_iota) if M_iota else "-"),
      M_iota is not None and M_iota == transvect(ALPHA) and M_psi is None
      and M_pr is None)
tick("stage 1 done")

# ======================================================================
banner("STAGE 2 -- AB2: the dictionary counts -- 1 + 63 + 56 ; 63 + 72 ; 28 ; 36")
# ======================================================================
PAULI = [u for u in NONSING if u != ALPHA and Bform(u, ALPHA) == 0]
SING_PERP = [x for x in SING if Bform(x, ALPHA) == 0]
SING_ODD = [x for x in SING if Bform(x, ALPHA) == 1]
PAIRS28 = sorted({frozenset((u, u ^ ALPHA)) for u in BOARD})
THETA36 = sorted({frozenset((x, x ^ ALPHA)) for x in SING_ODD})
coset_ok = all(qvals[x] == qvals[x ^ ALPHA] for x in range(256) if Bform(x, ALPHA) == 1)
check("AB2a", "COUNTS: nonsingular 120 = {v} + 63 Paulis (B(u,v)=0) + 56 board; "
      "singular 135 = 63 (B=0) + 72 (B=1); the coset {x : B(x,v)=1} has 128 "
      "vectors, q constant on each pair {x, x+v}: 56 nonsingular -> 28 odd "
      "forms (the bitangents = iota-pairs), 72 singular -> 36 even forms "
      "(the thetas) -- Stone Q's 64 phase points, in the roof's coordinates",
      len(PAULI) == 63 and len(BOARD) == 56 and len(SING_PERP) == 63
      and len(SING_ODD) == 72 and len(PAIRS28) == 28 and len(THETA36) == 36
      and coset_ok)
tick("stage 2 done")

# ======================================================================
banner("STAGE 3 -- AB3: THE STILL POINT ON THE BOARD")
# ======================================================================
Gmats_all = [mat_of_perm(p) for p in G_list]
Ggen_m = Gmats
def orbits_on(points, key=lambda x: x, act=None):
    pts = list(points); idx = {key(p): i for i, p in enumerate(pts)}
    seen = [False] * len(pts); sizes = []
    for i0 in range(len(pts)):
        if seen[i0]: continue
        orb = [i0]; seen[i0] = True; fr = [pts[i0]]
        while fr:
            x = fr.pop()
            for M in Ggen_m:
                y = act(M, x)
                j = idx[key(y)]
                if not seen[j]:
                    seen[j] = True; orb.append(j); fr.append(y)
        sizes.append(len(orb))
    return sorted(sizes, reverse=True)
act_vec = lambda M, x: mvec(M, x)
act_pair = lambda M, S: frozenset(mvec(M, x) for x in S)
o56 = orbits_on(BOARD, act=act_vec)
o28 = orbits_on(PAIRS28, key=lambda S: S, act=act_pair)
o36 = orbits_on(THETA36, key=lambda S: S, act=act_pair)
o63 = orbits_on(PAULI, act=act_vec)
o63s = orbits_on(SING_PERP, act=act_vec)
say("  G2(2) orbits: board 56 -> %s ; bitangents 28 -> %s ; thetas 36 -> %s ; "
    "Paulis 63 -> %s ; singular-perp 63 -> %s" % (o56, o28, o36, o63, o63s))
check("AB3a", "REGISTERED EXPECTATION: G2(2) is TRANSITIVE on the 28 bitangents "
      "(stabilizer order 12096/28 = 432) and on the 36 even thetas "
      "(stabilizer order 12096/36 = 336) and on the 63 Paulis (stabilizer "
      "192)", o28 == [28] and o36 == [36] and o63 == [63])
check("AB3b", "MEASURED: G2(2) on the board itself: orbits %s (stabilizer "
      "order%s %s)" % (o56, "s" if len(o56) > 1 else "",
                        [12096 // s for s in o56]), True)
tick("stage 3 done")

# ======================================================================
banner("STAGE 4 -- AB4: THETA <-> SEVEN")
# ======================================================================
invs = [g for g in G_list if pord(g) == 2]
thr = [g for g in G_list if pord(g) == 3]
copies = []; copy_gens = []
for a in invs:
    for b in thr:
        ab = pmul(a, b)
        if pord(ab) != 7 or pord(comm(a, b)) != 4: continue
        if any(a in L and b in L for L in copies): continue
        L = closure([a, b], cap=200)
        if len(L) != 168: continue
        copies.append(frozenset(L)); copy_gens.append((a, b))
assert len(copies) == 36
Gmat_of = {p: M for p, M in zip(G_list, Gmats_all)}
def fixes_theta(M, T): return frozenset(mvec(M, x) for x in T) == T
theta_stab = []
for T in THETA36:
    St = [p for p, M in zip(G_list, Gmats_all) if fixes_theta(M, T)]
    theta_stab.append(St)
stab_orders = sorted(set(len(S) for S in theta_stab))
def derived_set(S):
    Sset = set(S)
    gens = find_gens(S, len(S))
    Dg = derived_subgroup(gens, len(S) + 5) if False else None
    # direct: normal closure of commutators inside a small group
    Dset = set(closure([comm(a, b) for a in gens for b in gens if a != b], cap=len(S) + 5))
    changed = True
    while changed:
        changed = False
        extra = [pmul(pmul(g, d), pinv(g)) for g in gens for d in list(Dset)[:30]]
        D2 = closure(list(Dset)[:6] + extra, cap=len(S) + 5)
        if len(D2) > len(Dset): Dset = set(D2); changed = True
    return frozenset(Dset)
theta_to_copy = []
for St in theta_stab:
    Dd = derived_set(St)
    theta_to_copy.append(copies.index(Dd) if Dd in copies else -1)
bij_ok = (sorted(theta_to_copy) == list(range(36)))
fixed_per_copy = []
for L in copies:
    Lg = find_gens(sorted(L), 168)
    nfix = sum(1 for T in THETA36 if all(fixes_theta(Gmat_of[g], T) for g in Lg))
    fixed_per_copy.append(nfix)
check("AB4a", "REGISTERED EXPECTATION: every even theta's stabilizer in G2(2) "
      "has order 336 (= PGL(2,7)) whose derived subgroup is one of the 36 "
      "PSL(2,7)'s of SM-038, the map theta -> seven is a BIJECTION, and each "
      "PSL(2,7) fixes exactly ONE even theta: {36 thetas} <-> {36 sevens at "
      "the still point}", stab_orders == [336] and bij_ok
      and fixed_per_copy == [1] * 36,
      "stabilizer orders %s; fixed thetas per copy %s"
      % (stab_orders, sorted(set(fixed_per_copy))))
L0 = copies[0]; L0g = find_gens(sorted(L0), 168)
Ggen_m_saved = Ggen_m
Ggen_m = [Gmat_of[g] for g in L0g]
oL36 = orbits_on(THETA36, key=lambda S: S, act=act_pair)
oL28 = orbits_on(PAIRS28, key=lambda S: S, act=act_pair)
Ggen_m = Ggen_m_saved
check("AB4b", "the bridge copy on the 36 even thetas: orbits %s (SM-003's "
      "sealed fingerprint [1,7,7,21]) and on the 28 bitangents: %s "
      "(transitive, [28]) -- the fixed theta is its own" % (oL36, oL28),
      oL36 == [21, 7, 7, 1] and oL28 == [28])
tick("stage 4 done")

# ======================================================================
banner("STAGE 5 -- AB5: two intersections as data")
# ======================================================================
P0 = PAIRS28[0]
stabP = [p for p, M in zip(G_list, Gmats_all) if act_pair(M, P0) == P0]
check("AB5a", "|W(E6) cap G2(2)| = |Stab_G(one bitangent)| = %d (= 432 by "
      "transitivity on the 28): the bitangent stabilizer meets the still "
      "point in a group of order 432; profile %s"
      % (len(stabP), profile_of(stabP)), len(stabP) == 432)
Tp2C = [tau_p(M) for M in TpC]
oT2, memT2, trT2, baseT2 = make_bsgs_full([perm_of(M) for M in Tp2C], 120)
triple = [p for p in G_list if memT2(p)]
Ggen_m = [Gmat_of[g] for g in find_gens(triple, len(triple))]
o63_tr = orbits_on(PAULI, act=act_vec)
Ggen_m = Ggen_m_saved
fixed_pauli = o63_tr.count(1)
stabPa = None
if fixed_pauli:
    # find the fixed Pauli and compare stabilizers
    for x in PAULI:
        if all(mvec(Gmat_of[g], x) == x for g in triple[:50]) and all(mvec(Gmat_of[g], x) == x for g in triple):
            stabPa = [p for p, M in zip(G_list, Gmats_all) if mvec(M, x) == x]
            break
same = (stabPa is not None and set(stabPa) == set(triple))
check("AB5b", "THE 192 (SM-038's raw-turner triple intersection, recomputed: "
      "order %d): its orbits on the 63 Paulis are %s -- %s"
      % (len(triple), o63_tr,
         "it fixes exactly one Pauli and EQUALS the stabilizer in G2(2) of "
         "that Pauli: the raw turner's triangle meets at one point of the "
         "hexagon" if same else "it is NOT a Pauli stabilizer (recorded)"),
      len(triple) == 192 and same is not None)
tick("stage 5 done")

# ======================================================================
banner("STAGE 6 -- AB6: Psi against the roof's incidence on the board")
# ======================================================================
def ptype(u, w):
    s = u ^ w
    if s == ALPHA: return "v"
    return "P" if qvals[s] == 1 else "S"
PAIRS = [(u, w) for i, u in enumerate(BOARD) for w in BOARD[i + 1:]]
type_counts = Counter(ptype(u, w) for u, w in PAIRS)
def preserved(pm):
    return sum(1 for u, w in PAIRS if ptype(pm[u], pm[w]) == ptype(u, w)) / len(PAIRS)
def compose(pm, qm): return {u: pm[qm[u]] for u in BOARD}
PSI2 = compose(PSI_M, PSI_M); PSI3 = compose(PSI2, PSI_M)
PSI9 = PSI3
for _ in range(2): PSI9 = compose(PSI9, PSI3)
weyl = {u: mvec(Cmats[0], u) for u in BOARD}
scores = {"iota": preserved(IOTA_M), "Weyl (a C-bar generator)": preserved(weyl),
          "Psi": preserved(PSI_M), "Psi^2": preserved(PSI2), "Psi^3": preserved(PSI3),
          "Psi^9": preserved(PSI9), "pr": preserved(PR_M)}
random.seed(20260903 + 6)
rnd = []
for _ in range(200):
    perm = BOARD[:]; random.shuffle(perm)
    rnd.append(preserved(dict(zip(BOARD, perm))))
rmean = sum(rnd) / len(rnd); rmax = max(rnd)
say("  pair types on the board: %s of %d pairs" % (dict(type_counts), len(PAIRS)))
for k, s in scores.items(): say("    %-26s preserves %6.2f%% of pair types" % (k, 100 * s))
say("    %-26s mean %6.2f%%, max %6.2f%% over 200" % ("random permutations", 100 * rmean, 100 * rmax))
check("AB6a", "REGISTERED: iota and the Weyl element preserve 100%% of pair "
      "types (linear); Psi (%.1f%%) and pr (%.1f%%) preserve strictly less "
      "than 100%% and more than the random baseline (mean %.1f%%, max "
      "%.1f%%) -- the merkabit's gates are non-linear yet structured against "
      "the roof's own incidence; the numbers are the finding"
      % (100 * scores["Psi"], 100 * scores["pr"], 100 * rmean, 100 * rmax),
      scores["iota"] == 1.0 and scores["Weyl (a C-bar generator)"] == 1.0
      and scores["Psi"] < 1.0 and scores["pr"] < 1.0
      and scores["Psi"] > rmax and scores["pr"] > rmax)
json.dump({"node_perm": list(perm_nodes), "orbits": {"56": o56, "28": o28, "36": o36, "63": o63},
           "theta_stab_orders": stab_orders, "fixed_per_copy": fixed_per_copy,
           "scores": scores, "random_mean": rmean, "random_max": rmax,
           "triple192_orbits63": o63_tr, "we6_cap_g": len(stabP)},
          open(os.path.join(CACHE_AB, "witnesses_ab.json"), "w"), indent=1)
banner("VERDICT")
say("""  The board is the 56-orbit of the vector shadow; the chirality bit is
  the transvection t_v; the bitangents and thetas are the phase points of
  Stone Q read mod v.  The still point acts on all of it: transitive on
  the 28 and the 36 with the stabilizers registered, the 36 thetas in
  bijection with its 36 sevens, each seven fixing its own theta.  Psi and
  pr do not extend linearly, and their scores against the roof's
  incidence are recorded above.""")
say("")
say("RESULT: %d checks passed, %d failed%s" % (PASS, FAIL,
    ("  FAILED: %s" % FAILED) if FAILED else ""))
tick("done")
LOG.close()
