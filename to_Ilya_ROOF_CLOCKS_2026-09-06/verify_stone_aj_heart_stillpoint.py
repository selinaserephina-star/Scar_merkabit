# -*- coding: utf-8 -*-
r"""verify_stone_aj_heart_stillpoint.py -- STONE AJ: THE HEART AT THE STILL POINT

Brief: BRIEF_STONE_AJ_HEART_AT_STILLPOINT.md (lock BRIEF_STONE_AJ_LOCK.sha256,
re-verified as check AJ0).

Question: can the roof clock be turned out of the still point?  (No: the
still point commutes with the turn and has no order 9.)  Where do the
heart x = (Phi.c-bar)^6 and the cube (Phi.c-bar)^3 sit relative to G2(2)?
Does the vector shadow turn into an eighteen?

BARS: AJ1 Phi commutes with all 12096, twisted orders {3,6,12,21,24}, the
3024 Phi.g8 of order 24 and their types; AJ2 the heart meets G2(2) in the
class of 56, not the 672; AJ3 an order-6 element of G2(2) conjugate to
(Phi.c-bar)^3; AJ4 Phi.C-bar contains eighteens; AJ5 [obs].

Machinery: verify_stone_aa_roofclock.py lines 71-696 VERBATIM; helpers of
verify_stone_ag_seven_nines.py and verify_stone_ai_class18.py VERBATIM;
sealed caches READ-ONLY.  DISCIPLINE: compute, never assert; registered
expectations resolvable INVERTED at equal prominence; exact arithmetic;
no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_aj_heart_stillpoint.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_aj_heart_stillpoint.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))

CACHE_U = "_stone_u_cache"; CACHE_V = "_stone_v_cache"
CACHE_X = "_stone_x_cache"; CACHE_L = "_liftlaw_cache"
CACHE_Z = "_stone_z_cache"; CACHE_AA = "_stone_aa_cache"
CACHE_AJ = "_stone_aj_cache"; os.makedirs(CACHE_AJ, exist_ok=True)
random.seed(20260903)

say("=" * 78); say("STONE AJ -- THE HEART AT THE STILL POINT"); say("=" * 78)
BRIEF_AJ = "BRIEF_STONE_AJ_HEART_AT_STILLPOINT.md"; LOCK_AJ = open("BRIEF_STONE_AJ_LOCK.sha256").read().strip()
sha_aj = hashlib.sha256(open(BRIEF_AJ, "rb").read()).hexdigest()
check("AJ0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AJ_LOCK.sha256" % BRIEF_AJ, sha_aj == LOCK_AJ, sha_aj[:16] + "...")

# =====================================================================
# VERBATIM from verify_stone_aa_roofclock.py, lines 71-696; checks relabelled REPLAY-AA*, np.save removed
# =====================================================================
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
say("STONE AA -- THE ROOF CLOCK, FIRST MEASUREMENT")
say("the turn tau'' realized on the 360 nonsingular points of V, S+, S-;")
say("<Omega, Phi> = O8+(2):3 explicit; first measurements   [caches READ-ONLY]")
say("=" * 78)

# ======================================================================
banner("STAGE 0 -- AA0: brief lock; Stone X + SM-038 machinery replayed VERBATIM")
# ======================================================================
BRIEF = "BRIEF_STONE_AA_ROOFCLOCK.md"
LOCK = "0759ad94bdd8d1ed80d4f73d9b55b21a45793221c88b2d813c6fe68bc6954194"
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("REPLAY-AA0", "the brief is sha-locked: sha256(%s) equals the value in "
      "BRIEF_STONE_AA_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

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
check("REPLAY-AA0a", "REPLAY cross-check: tau on the 26 generators and T+ "
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
check("REPLAY-AA0b", "SM-038 replayed: |G| = 12096 (exhaustive sift%s); y unique "
      "and equal to the sealed y_cols; tau'' fixes G's generators; "
      "tau''^3 = id on all 26 generators"
      % (", identical to the cached G_rows" if same_G else ""),
      len(G_list) == 12096 and (same_G in (True, None))
      and list(Ym) == ZJ["y_cols"]
      and all(tau_pp(M) == M for M in Gmats) and ord3 and oC == 1451520)
tick("stage 0 done")

# ======================================================================
banner("STAGE 1 -- AA1: rho-, Q-, the three 120-point blocks, P(Omega) on 360")
# ======================================================================
ODD = [S for S in range(16) if bin(S).count("1") % 2 == 1]
OPOS = {S: i for i, S in enumerate(ODD)}
ODD_MASK = sum(1 << S for S in ODD)
def sminus_of(P):
    cols = []
    for S in ODD:
        c = P[S]
        if c & ~ODD_MASK: return None
        cols.append(sum(((c >> T) & 1) << OPOS[T] for T in ODD))
    return tuple(cols)
_RHO_MEMO = {}
def rho_pm(M):
    """(rho+(M), rho-(M)) via the transvection decomposition (memoized)."""
    got = _RHO_MEMO.get(M)
    if got is not None: return got
    P = rho_full(decompose(M))
    sp, sm = splus_of(P), sminus_of(P)
    assert sp is not None and sm is not None
    _RHO_MEMO[M] = (sp, sm)
    return sp, sm
RHOM = [rho_pm(M)[1] for M in OMEGA_GENS]
rowsQ = []
for M in RHOM:
    for x in range(256):
        y = mvec(M, x)
        r = 0
        for t, (i, j) in enumerate(mon):
            if (((x >> i) & (x >> j)) ^ ((y >> i) & (y >> j))) & 1:
                r |= 1 << t
        if r: rowsQ.append(r)
NSM = f2_nullspace(rowsQ, 36)
cQM = NSM[0] if NSM else 0
QM = []
for x in range(256):
    v = 0
    for t, (i, j) in enumerate(mon):
        if (cQM >> t) & 1 and ((x >> i) & 1) and ((x >> j) & 1): v ^= 1
    QM.append(v)
SP_NS = [x for x in range(256) if QP[x] == 1]
SM_NS = [x for x in range(256) if QM[x] == 1]
check("REPLAY-AA1a", "Q- (the rho-(Omega)-invariant quadratic form on S-) is "
      "UNIQUE (nullspace dim 1) and PLUS-TYPE: 120 nonsingular spinors, "
      "as Q+ on S+ and q on V", len(NSM) == 1 and len(SP_NS) == 120
      and len(SM_NS) == 120 and len(NONSING) == 120)
V_IDX = {m: i for i, m in enumerate(NONSING)}
SP_IDX = {m: 120 + i for i, m in enumerate(SP_NS)}
SM_IDX = {m: 240 + i for i, m in enumerate(SM_NS)}
def P360(M):
    sp, sm = rho_pm(M)
    return tuple([V_IDX[mvec(M, x)] for x in NONSING]
                 + [SP_IDX[mvec(sp, x)] for x in SP_NS]
                 + [SM_IDX[mvec(sm, x)] for x in SM_NS])
PG = [P360(M) for M in OMEGA_GENS]
def orbit_of(pt, perms):
    orb = {pt}; fr = [pt]
    while fr:
        x = fr.pop()
        for p in perms:
            y = p[x]
            if y not in orb:
                orb.add(y); fr.append(y)
    return orb
orbs = [len(orbit_of(pt, PG)) for pt in (0, 120, 240)]
oO, memO, trO, baseO = make_bsgs_full(PG, 360)
check("REPLAY-AA1b", "P(Omega) on the 360 points: the three blocks are three orbits "
      "of size 120 each; BSGS order 174,182,400 = |O8+(2)| (faithful)",
      orbs == [120, 120, 120] and oO == 174182400)
tick("stage 1 done (BSGS on 360 points)")

# ======================================================================
banner("STAGE 2 -- AA2: THE TURN ON STATES -- Phi, order 3, footprint tau''^2")
# ======================================================================
TPP = mmul(Yi, mmul(W0m, TP)); TPPi = f2_matinv(TPP)     # T'': S+ -> V
tpp_ok = all(mmul(TPP, mmul(rho_pm(M)[0], TPPi)) == tau_pp(M)
             for M in OMEGA_GENS)
T2 = [tau_pp(tau_pp(M)) for M in OMEGA_GENS]                # tau''^2(g)
pairsL = [(rho_pm(M)[0], rho_pm(N)[1]) for M, N in zip(OMEGA_GENS, T2)]
NL = intertwiner_space(pairsL)
Ls = []
for bits in range(1, 2 ** len(NL)):
    v = 0
    for k in range(len(NL)):
        if (bits >> k) & 1: v ^= NL[k]
    Lm = mat_from_bits(v)
    if f2_matinv(Lm) is None: continue
    if all(mmul(Lm, A) == mmul(B, Lm) for A, B in pairsL): Ls.append(Lm)
check("REPLAY-AA2a", "T'' = y^-1 s1-bar T+ intertwines: tau''(g) = T'' rho+(g) "
      "T''^-1 on all 26 generators; the intertwiner L: S+ -> S- with "
      "L rho+(g) = rho-(tau''^2 g) L exists and is UNIQUE (space dim %d, "
      "%d invertible solution)" % (len(NL), len(Ls)),
      tpp_ok and len(NL) == 1 and len(Ls) == 1)
Lm = Ls[0]; Li = f2_matinv(Lm)
L_iso = all(QM[mvec(Lm, x)] == QP[x] for x in range(256))
check("REPLAY-AA2b", "L carries Q+ to Q- on all 256 spinors (an isometry "
      "(S+,Q+) -> (S-,Q-)): the twisted spin module is the other "
      "half-spin module, with its form", L_iso)
PHI = [0] * 360
for i, x in enumerate(NONSING): PHI[i] = SP_IDX[mvec(TPPi, x)]
for i, x in enumerate(SP_NS): PHI[120 + i] = SM_IDX[mvec(Lm, x)]
for i, x in enumerate(SM_NS): PHI[240 + i] = V_IDX[mvec(TPP, mvec(Li, x))]
PHI = tuple(PHI); PHIi = pinv(PHI)
phi3 = (ppow(PHI, 3) == pident(360)) and PHI != pident(360)
conj_ok = all(pmul(pmul(PHI, P360(M)), PHIi) == P360(N)
              for M, N in zip(OMEGA_GENS, T2))
check("REPLAY-AA2c", "REGISTERED EXPECTATION CONFIRMED: Phi is a permutation of the "
      "360 points of EXACT order 3 (V -> S+ -> S- -> V) and "
      "Phi P(g) Phi^-1 = P(tau''^2(g)) for ALL 26 generators exactly -- "
      "the turn acts on states with footprint tau''^2 = tau''^-1",
      phi3 and conj_ok)
oOP, memOP, trOP, baseOP = make_bsgs_full(PG + [PHI], 360)
check("REPLAY-AA2d", "Phi is not in P(Omega) (membership strip) and |<P(Omega), "
      "Phi>| = 522,547,200 = 3 |O8+(2)|: O8+(2):3 as an explicit "
      "permutation group on 360 points", (not memO(PHI))
      and oOP == 3 * 174182400, "order %d" % oOP)
pass  # [AJ] AA's np.save of phi360.npy REMOVED
tick("stage 2 done")


# =====================================================================
# VERBATIM helpers from verify_stone_ag_seven_nines.py (SM-045) and verify_stone_ai_class18.py (SM-047)
# =====================================================================
def cycle_type(p):
    n = len(p); seen = [False] * n; ct = []
    for i in range(n):
        if seen[i]: continue
        j = i; k = 0
        while not seen[j]:
            seen[j] = True; j = p[j]; k += 1
        ct.append(k)
    return tuple(sorted(ct, reverse=True))
def lcm(a, b): return a * b // gcd(a, b)
def order_ct(ct):
    o = 1
    for k in set(ct): o = lcm(o, k)
    return o
def ct_block(p, b):
    """cycle type of the permutation restricted to block b (0: V, 1: S+, 2: S-); p must preserve the block."""
    idx = list(range(120 * b, 120 * b + 120)); assert all(120 * b <= p[i] < 120 * b + 120 for i in idx)
    sub = [p[i] - 120 * b for i in idx]
    return dict(Counter(cycle_type(sub)))


CAP = 1_500_000
GA = [np.array(g, dtype=np.uint16) for g in PG]; GAi = [np.array(pinv(g), dtype=np.uint16) for g in PG]
def key_of(z): return np.asarray(z, dtype=np.uint16).tobytes()
def conj_class(z, cap):
    """the Omega-conjugacy class of z as a set of byte-keys (orbit under conjugation by the 26 generators; numpy)."""
    z = np.array(z, dtype=np.uint16); orb = {key_of(z)}; fr = [z]
    while fr:
        a = fr.pop()
        for g, gi in zip(GA, GAi):
            b = g[a[gi]]                       # (g a g^-1)[i] = g[a[g^-1[i]]]
            k = b.tobytes()
            if k not in orb:
                orb.add(k); fr.append(b)
                if len(orb) > cap: return None
    return orb

IDENT = np.arange(360, dtype=np.uint16)
def A(p): return np.asarray(p, dtype=np.uint16)
def ainv(a):
    r = np.empty_like(a); r[a] = np.arange(len(a), dtype=np.uint16); return r
def amul(a, b): return a[b]                       # (a b)[i] = a[b[i]]  (apply b then a)
def aconj(g, a, gi=None):                          # g a g^-1
    if gi is None: gi = ainv(g)
    return g[a[gi]]
def conj_class_T(z, cap):
    """Omega-class of z with a transversal: dict key(y) -> u_y (array) with u_y z u_y^-1 = y."""
    z = A(z); T = {z.tobytes(): IDENT.copy()}; fr = [(z, IDENT.copy())]
    while fr:
        a, u = fr.pop()
        for g, gi in zip(GA, GAi):
            b = g[a[gi]]; k = b.tobytes()
            if k not in T:
                ub = g[u]; T[k] = ub; fr.append((b, ub))
                if len(T) > cap: return None
    return T
def closure_np(gens, cap=200000):
    S = {IDENT.tobytes(): IDENT.copy()}; fr = [IDENT.copy()]
    while fr:
        a = fr.pop()
        for g in gens:
            b = a[g]; k = b.tobytes()
            if k not in S:
                S[k] = b; fr.append(b)
                if len(S) > cap: return None
    return list(S.values())
def aorder(a):
    b = a.copy(); n = 1
    while not np.array_equal(b, IDENT): b = a[b]; n += 1
    return n


# =====================================================================
# STONE AJ stages
# =====================================================================
banner("AJ0a -- replay: the still point on 360 points; the heart's class with transversal; its centralizer")
PHI_cached = tuple(int(v) for v in np.load(os.path.join(CACHE_AA, "phi360.npy")))
c240 = pident(240)
for s in S240: c240 = pmul(c240, s)
cbar = M2_of(c240); ec = pmul(PHI, P360(cbar)); e = A(ec); x = A(ppow(ec, 6)); e3 = A(ppow(ec, 3))
PHIa = A(PHI); PHIai = ainv(PHIa)
# G2(2) on 360: closure from a few generators of G_list (the sealed 12096 on the vector block)
G_set120 = set(G_list)
random.seed(20260905)
while True:
    gens120 = [G_list[random.randrange(len(G_list))] for _ in range(4)]
    if len(closure(gens120, cap=13000)) == 12096: break
gens360 = [A(P360(mat_of_perm(g))) for g in gens120]
G360 = closure_np(gens360, cap=13000)
G360_by120 = {tuple(int(v) for v in g[:120]): g for g in G360}
check("AJ0a", "Phi equals the sealed cache; G2(2) lifted to 360 points: 12,096 distinct permutations whose vector-block parts are exactly the sealed G_list",
      PHI == PHI_cached and len(G360) == 12096 and set(G360_by120) == G_set120)
t1 = time.time(); TX = conj_class_T(x, CAP); tick("class(x) with transversal: %d (%.1fs)" % (len(TX), time.time() - t1))
keys = list(TX); sgens = []
for _ in range(400):
    k = random.choice(keys); yv = np.frombuffer(k, dtype=np.uint16); u = TX[k]
    j = random.randrange(26); g, gi = GA[j], GAi[j]
    gy = g[yv[gi]]; sg = amul(ainv(TX[gy.tobytes()]), amul(g, u))
    if not np.array_equal(sg, IDENT): sgens.append(sg)
CX = closure_np(sgens, cap=20000); CXinv = [ainv(h) for h in CX]
check("AJ0b", "class(x) has 89,600 elements and C_Omega(x) has order 1944 (SM-047 re-derived)", len(TX) == 89600 and len(CX) == 1944)

banner("AJ1 -- the still point commutes with the turn; its twisted orders; the order-24 elements Phi.g8")
comm_all = all(np.array_equal(amul(PHIa, g), amul(g, PHIa)) for g in G360)
ordG = Counter(); ordPhiG = Counter(); types24 = Counter(); ord8_types = {}
for g in G360:
    og = aorder(g); ordG[og] += 1
    pg = amul(PHIa, g); ct = cycle_type([int(v) for v in pg]); o = order_ct(ct); ordPhiG[o] += 1
    if o == 24:
        types24[ct] += 1
say("  orders in G2(2): %s" % dict(sorted(ordG.items())))
say("  orders of Phi.g over G2(2): %s" % dict(sorted(ordPhiG.items())))
say("  cycle types on 360 of the Phi.g of order 24: %s" % {str(dict(Counter(k))): v for k, v in types24.items()})
lcm_ok = all(ordPhiG[o] == sum(v for k, v in ordG.items() if (3 * k // gcd(3, k)) == o) for o in ordPhiG)
sealed = json.load(open(os.path.join(CACHE_AA, "coset_sample.json")))
sealed_types = set(tuple(k) for k, v in sealed["max_cycle_types"])
check("AJ1a", "REGISTERED: Phi P(g) = P(g) Phi for ALL 12,096 g; the orders of Phi.g are exactly lcm(3, ord g): {3, 6, 12, 21, 24} with the census "
      "multiplicities (3: 729, 6: 2835, 12: 3780, 21: 1728, 24: 3024) -- NO eighteen: by SM-047's one class, Phi.c-bar is conjugate to no Phi.g with g at "
      "the still point; the maximal twisted order 24 IS at the still point (all 3,024 elements of order 8)",
      comm_all and lcm_ok and set(ordPhiG) == {3, 6, 12, 21, 24} and ordPhiG[24] == 3024 and 18 not in ordPhiG)
both = sealed_types <= set(types24)
check("AJ1b", "REGISTERED GUESS: both sealed order-24 cycle types appear among the Phi.g8" if both else
      "REGISTERED GUESS INVERTED: only %s of the two sealed order-24 types appears among the Phi.g8" % len(sealed_types & set(types24)), both,
      "types found: %d, in numbers %s" % (len(types24), sorted(types24.values())))

banner("AJ2 -- the heart at the still point: the 728 elements of order 3 of G2(2) against class(x)")
G3 = [g for g in G360 if aorder(g) == 3]
# G2(2)-conjugacy classes of its order-3 elements
def gclasses(elems, gens):
    keys = set(g.tobytes() for g in elems); seen = set(); classes = []
    ginv = [ainv(g) for g in gens]
    for g in elems:
        if g.tobytes() in seen: continue
        orb = {g.tobytes()}; fr = [g]
        while fr:
            a = fr.pop()
            for h, hi in zip(gens, ginv):
                b = h[a[hi]]; k = b.tobytes()
                if k not in orb: orb.add(k); fr.append(b)
        seen |= orb; classes.append((g, len(orb)))
    return classes
cls3 = gclasses(G3, gens360)
inx = {}
for rep, n in cls3:
    inx[n] = rep.tobytes() in TX
    M = mat_of_perm(tuple(int(v) for v in rep[:120])); fd = 8 - f2_rank([M[j] ^ (1 << j) for j in range(8)])
    note("order-3 class of G2(2) of size %d: fixed dim on V %d, block cycle types %s, in class(x): %s" % (n, fd, [ct_block([int(v) for v in rep], b) for b in range(3)], inx[n]))
n_in = sum(1 for g in G3 if g.tobytes() in TX)
check("AJ2a", "REGISTERED GUESS: the order-3 elements of G2(2) form two G2(2)-classes of sizes 56 and 672; exactly the class of 56 lies in class(x) "
      "(56 elements of the still point are hearts), the class of 672 does not", sorted(n for _, n in cls3) == [56, 672] and inx.get(56) is True and inx.get(672) is False and n_in == 56,
      "in class(x): %d of 728" % n_in)
if inx.get(56):
    rep56 = next(rep for rep, n in cls3 if n == 56)
    # centralizer in G2(2) of that heart
    c56 = sum(1 for g in G360 if np.array_equal(aconj(g, rep56), rep56))
    note("[obs] |C_{G2(2)}(heart)| = %d (= 12096/56 = %d)" % (c56, 12096 // 56))

banner("AJ3 -- the cube of the eighteen at the still point: order-6 elements of G2(2) with square in class(x)")
G6 = [g for g in G360 if aorder(g) == 6]
cands = [g for g in G6 if amul(g, g).tobytes() in TX]
note("order-6 elements of G2(2): %d; with square in class(x): %d" % (len(G6), len(cands)))
found = 0; found_types = Counter()
for g in cands:
    k = amul(g, g).tobytes(); u = TX[k]; gg = aconj(ainv(u), g, u)          # u^-1 g u : square = x
    assert np.array_equal(amul(gg, gg), x)
    if any(np.array_equal(aconj(h, gg, hi), e3) for h, hi in zip(CX, CXinv)):
        found += 1; found_types[str([ct_block([int(v) for v in g], b) for b in range(3)])] += 1
say("  candidates conjugate to (Phi.c-bar)^3: %d of %d" % (found, len(cands)))
check("AJ3a", "REGISTERED GUESS: at least one element of order 6 of G2(2) is conjugate in Omega to (Phi.c-bar)^3 -- the eighteen's cube is at the still point" if found
      else "REGISTERED GUESS INVERTED: no element of order 6 of G2(2) is conjugate to (Phi.c-bar)^3 -- the eighteen's cube is NOT at the still point", found > 0,
      "conjugate: %d; block types of the candidates: %s" % (found, {str(k): v for k, v in Counter(str([ct_block([int(v) for v in g], b) for b in range(3)]) for g in cands).items()}))

banner("AJ4 -- the vector shadow turns into an eighteen")
gz = np.load(os.path.join(CACHE_U, "stab_derived_gens.npz"))["g"]
Cg120 = [tuple(int(v) for v in gz[j]) for j in range(gz.shape[0])]
Cg360 = [A(P360(M2_of(g) if len(g) == 240 else mat_of_perm(g))) for g in Cg120]   # the sealed generators are 240-root permutations (Stone Z reduces them with M2_of); first run passed them to mat_of_perm and stopped -- FIRSTRUN log kept
random.seed(20260906)
poolC = []
for _ in range(60):
    w = IDENT.copy()
    for _ in range(random.randrange(8, 20)): w = amul(Cg360[random.randrange(len(Cg360))], w)
    poolC.append(w)
histC = Counter(); e18 = None
for _ in range(3000):
    g = poolC[random.randrange(60)]
    for _ in range(3): g = amul(poolC[random.randrange(60)], g)
    assert g[V_IDX[ALPHA]] == V_IDX[ALPHA]
    pg = amul(PHIa, g); o = order_ct(cycle_type([int(v) for v in pg])); histC[o] += 1
    if o == 18 and e18 is None: e18 = g
say("  orders of Phi.g for 3000 random g in C-bar = Stab(v): %s" % dict(sorted(histC.items())))
check("AJ4a", "REGISTERED: Phi.C-bar contains elements of order 18 (found %d of 3000): by the one class, the clock's class meets Phi.C-bar -- the eighteen can be "
      "turned out of the vector shadow though not out of the still point" % histC[18], histC[18] > 0)
ALPHA_R = SIMPLE[0]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi7 = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi7[i]] for i in range(7)]
def refl240(b): return tuple(ridx[tuple(r[t] - dot4(r, b) * b[t] for t in range(8))] for r in roots)
c7_240 = pident(240)
for i in range(7): c7_240 = pmul(c7_240, refl240(BETA[i]))
cb7 = M2_of(c7_240); cb7sq = mmul(cb7, cb7)
P72 = A(P360(cb7sq)); P76 = amul(P72, amul(P72, P72))
o2 = order_ct(cycle_type([int(v) for v in amul(PHIa, P72)])); o6 = order_ct(cycle_type([int(v) for v in amul(PHIa, P76)]))
note("[obs] Phi.c-bar7^2 has order %d; Phi.c-bar7^6 (= Phi.y) has order %d" % (o2, o6))

json.dump({"brief_sha": sha_aj, "ordG": {str(k): v for k, v in ordG.items()}, "ordPhiG": {str(k): v for k, v in ordPhiG.items()},
           "types24": {str(dict(Counter(k))): v for k, v in types24.items()}, "order3_classes": [n for _, n in cls3], "hearts_in_G2": n_in,
           "order6_conj_to_cube": found, "histC": {str(k): v for k, v in histC.items()}}, open(os.path.join(CACHE_AJ, "witnesses_aj.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
