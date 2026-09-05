# -*- coding: utf-8 -*-
r"""verify_stone_am_coset_complete.py -- STONE AM: THE COSET COMPLETE

Brief: BRIEF_STONE_AM_COSET_COMPLETE.md (lock BRIEF_STONE_AM_LOCK.sha256,
re-verified as check AM0).

Question: the remaining twisted orders 9, 6, 3 of the coset Omega.Phi,
classified exactly; the census must close: all class densities sum to 1.

BARS: AM1 order 9 (fibre over the heart): one class of 1/18; AM2 order 6
(involution fibre): classes and densities, measured; AM3 order 3: the
class of Phi.g56 = 806,400, Phi.g672 in it, 40 samples all in it, none
turns; AM4 the sum of all densities = 1 exactly; AM5 [obs] the table.

Machinery: verify_stone_aa_roofclock.py lines 71-696 VERBATIM; helpers of
SM-045/047/048/050 VERBATIM; sealed caches READ-ONLY.  DISCIPLINE:
compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; no registry/git writes.  Not RH/GRH.
Rule 3.

Run:  python -X utf8 verify_stone_am_coset_complete.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from fractions import Fraction
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_am_coset_complete.log", "w", encoding="utf-8")
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
CACHE_AM = "_stone_am_cache"; os.makedirs(CACHE_AM, exist_ok=True)
random.seed(20260903)

say("=" * 78); say("STONE AM -- THE COSET COMPLETE"); say("=" * 78)
BRIEF_AM = "BRIEF_STONE_AM_COSET_COMPLETE.md"; LOCK_AM = open("BRIEF_STONE_AM_LOCK.sha256").read().strip()
sha_am = hashlib.sha256(open(BRIEF_AM, "rb").read()).hexdigest()
check("AM0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AM_LOCK.sha256" % BRIEF_AM, sha_am == LOCK_AM, sha_am[:16] + "...")

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
pass  # [AM] AA's np.save of phi360.npy REMOVED
tick("stage 2 done")


# =====================================================================
# VERBATIM helpers from SM-045 / SM-047 / SM-048 / SM-050 verifiers
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

def schreier_centralizer(T, n_gen=600, cap=400000):
    keys = list(T); sg = []
    for _ in range(n_gen):
        k = random.choice(keys); yv = np.frombuffer(k, dtype=np.uint16); u = T[k]
        j = random.randrange(26); g, gi = GA[j], GAi[j]
        gy = g[yv[gi]]; s_ = amul(ainv(T[gy.tobytes()]), amul(g, u))
        if not np.array_equal(s_, IDENT): sg.append(s_)
    return closure_np(sg, cap=cap)
def sample_twisted(pool, want_order, n, tries_max=400000, by_type=False):
    out = []; tries = 0
    while len(out) < n and tries < tries_max:
        tries += 1
        g = pool[random.randrange(len(pool))]
        for _ in range(3): g = pmul(pool[random.randrange(len(pool))], g)
        ep = pmul(PHI, g); ct = cycle_type(ep)
        if order_ct(ct) == want_order: out.append((A(ep), ct))
    return out, tries


# =====================================================================
# STONE AM stages
# =====================================================================
OMEGA = 174182400
def classify_by_fibre(samples, power_k, T_of_rep, C_of_rep, rep):
    """samples: list of (array, ct) of one type; power_k: the power used as fibre; returns #conjugate to rep."""
    Cinv = [ainv(h) for h in C_of_rep]; same = 0; others = []
    for ea, ct in samples:
        zp = ea.copy()
        for _ in range(power_k - 1): zp = amul(ea, zp)
        k = zp.tobytes()
        if k not in T_of_rep: others.append(ea); continue
        u = T_of_rep[k]; epp = aconj(ainv(u), ea, u)
        if any(np.array_equal(aconj(h, epp, hi), rep) for h, hi in zip(C_of_rep, Cinv)): same += 1
        else: others.append(ea)
    return same, others
def fibre_class(e, power_k, cap_c=400000):
    """the class data of a twisted e through its k-th power p: class(p) with transversal, C(p), C(e)."""
    p = e.copy()
    for _ in range(power_k - 1): p = amul(e, p)
    T = conj_class_T(p, CAP)
    if T is None: return None
    C = schreier_centralizer(T, cap=cap_c)
    if C is None: return None
    Ce = [h for h in C if np.array_equal(aconj(h, e), e)]
    return dict(T=T, C=C, Ce=Ce, p=p)
def conj_class_keys(z, cap):
    z = A(z); orb = {z.tobytes()}; fr = [z]
    while fr:
        a = fr.pop()
        for g, gi in zip(GA, GAi):
            b = g[a[gi]]; k = b.tobytes()
            if k not in orb:
                orb.add(k); fr.append(b)
                if len(orb) > cap: return None
    return orb

banner("AM0a -- replay: the still point on 360; the heart's class and centralizer")
PHI_cached = tuple(int(v) for v in np.load(os.path.join(CACHE_AA, "phi360.npy")))
PHIa = A(PHI); PHIai = ainv(PHIa)
G_set120 = set(G_list)
random.seed(20260905)
while True:
    gens120 = [G_list[random.randrange(len(G_list))] for _ in range(4)]
    if len(closure(gens120, cap=13000)) == 12096: break
gens360 = [A(P360(mat_of_perm(g))) for g in gens120]
G360 = closure_np(gens360, cap=13000)
c240 = pident(240)
for s in S240: c240 = pmul(c240, s)
ec = pmul(PHI, P360(M2_of(c240))); e18 = A(ec); x = A(ppow(ec, 6))
t1 = time.time(); TX = conj_class_T(x, CAP); CX = schreier_centralizer(TX, cap=20000); CXinv = [ainv(h) for h in CX]
check("AM0a", "Phi equals the sealed cache; G2(2) on 360 (12,096); class(x) = 89,600 with transversal; C_Omega(x) = 1944",
      PHI == PHI_cached and len(G360) == 12096 and len(TX) == 89600 and len(CX) == 1944)
DENS = {18: [Fraction(1, 6)], 24: [Fraction(1, 8), Fraction(1, 8)], 21: [Fraction(1, 7)], 12: [Fraction(1, 32), Fraction(1, 4), Fraction(1, 48), Fraction(1, 96)]}
CENTS = {18: [6], 24: [8, 8], 21: [7], 12: [32, 4, 48, 96]}

random.seed(20260907)
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)

banner("AM1 -- order 9 through the heart")
S9, tries9 = sample_twisted(pool, 9, 150)
types9 = Counter(ct for _, ct in S9)
say("  150 order-9 twisted elements (%d tries; density %.4f vs 1/18 = 0.0556): types %s" % (tries9, 150 / tries9, {str(dict(Counter(k))): v for k, v in types9.items()}))
cubes_in = sum(1 for ea, _ in S9 if amul(ea, amul(ea, ea)).tobytes() in TX)
e9inv = ainv(amul(e18, e18))                      # (Phi.c-bar)^-2, a twisted element of order 9
DENS[9] = []; CENTS[9] = []; conj9 = Counter(); reps9 = []
for ct in types9:
    lst = [(ea, c) for ea, c in S9 if c == ct]; remaining = lst; kclass = 0
    while remaining and kclass < 4:
        rep = remaining[0][0]
        rp = amul(rep, amul(rep, rep)); k = rp.tobytes()
        if k not in TX: note("order-9 type %s: a representative's cube is NOT in the heart's class -- fibre unavailable" % str(dict(Counter(ct)))); break
        u = TX[k]; rep_t = aconj(ainv(u), rep, u)            # cube -> x
        Ce = [h for h in CX if np.array_equal(aconj(h, rep_t), rep_t)]
        same, others = classify_by_fibre(remaining, 3, TX, CX, rep_t)
        DENS[9].append(Fraction(1, len(Ce))); CENTS[9].append(len(Ce)); kclass += 1
        in_it = any(np.array_equal(aconj(h, aconj(ainv(TX[amul(e9inv, amul(e9inv, e9inv)).tobytes()]), e9inv, TX[amul(e9inv, amul(e9inv, e9inv)).tobytes()]), hi), rep_t) for h, hi in zip(CX, CXinv)) if amul(e9inv, amul(e9inv, e9inv)).tobytes() in TX else False
        tick("order-9 type %s, class %d: |C_Omega(e)| = %d -> density 1/%d; %d of %d samples; (Phi.c-bar)^-2 in it: %s" % (str(dict(Counter(ct))), kclass, len(Ce), len(Ce), same, len(remaining), in_it))
        conj9[(str(dict(Counter(ct))), kclass)] = same
        remaining = [(ea, ct) for ea in others]
check("AM1a", "REGISTERED: every sampled order-9 twisted element has its cube in the heart's class; REGISTERED GUESS: ONE class of density 1/18 (centralizer 18), all 150 "
      "samples conjugate to the representative, (Phi.c-bar)^-2 among them", cubes_in == 150 and len(DENS[9]) == 1 and DENS[9][0] == Fraction(1, 18) and sum(conj9.values()) == 150,
      "cubes in class(x): %d/150; classes found %s" % (cubes_in, ["1/%d" % c for c in CENTS[9]]))

banner("AM2 -- order 6 through the involution")
S6, tries6 = sample_twisted(pool, 6, 150)
types6 = Counter(ct for _, ct in S6)
say("  150 order-6 twisted elements (%d tries; density %.4f): types %s" % (tries6, 150 / tries6, {str(dict(Counter(k))): v for k, v in types6.items()}))
DENS[6] = []; CENTS[6] = []; assigned6 = 0
for ct in types6:
    lst = [(ea, c) for ea, c in S6 if c == ct]; remaining = lst; kclass = 0
    while remaining and kclass < 4:
        rep = remaining[0][0]
        fc = fibre_class(rep, 3)
        if fc is None: note("order-6 type %s: fibre over e^3 exceeds a cap -- not classified" % str(dict(Counter(ct)))); break
        same, others = classify_by_fibre(remaining, 3, fc["T"], fc["C"], rep)
        DENS[6].append(Fraction(1, len(fc["Ce"]))); CENTS[6].append(len(fc["Ce"])); kclass += 1; assigned6 += same
        tick("order-6 type %s, class %d: |class(e^3)| = %d, |C(e^3)| = %d, |C_Omega(e)| = %d -> density 1/%d; %d of %d samples"
             % (str(dict(Counter(ct))), kclass, len(fc["T"]), len(fc["C"]), len(fc["Ce"]), len(fc["Ce"]), same, len(remaining)))
        remaining = [(ea, ct) for ea in others]
d6 = sum(DENS[6])
check("AM2a", "MEASURED: the order-6 twisted elements: %d classes found with densities %s (sum %s = %.4f; sampled %.4f); all 150 samples assigned"
      % (len(DENS[6]), ["1/%d" % c for c in CENTS[6]], d6, float(d6), 150 / tries6), assigned6 == 150)

banner("AM3 -- order 3: the turn's class, the still point's twisted 3-elements, the samples")
G3 = [g for g in G360 if aorder(g) == 3]
cls3 = gclasses(G3, gens360)
g56 = next(rep for rep, n in cls3 if n == 56); g672 = next(rep for rep, n in cls3 if n == 672)
e56 = amul(PHIa, g56); e672 = amul(PHIa, g672)
t1 = time.time(); K56 = conj_class_keys(e56, 1_000_000)
tick("class of Phi.g56: %s elements (%.1fs)" % (len(K56) if K56 else "> 1,000,000", time.time() - t1))
TPHI = conj_class_keys(PHIa, 20000)
in672 = (e672.tobytes() in K56) if K56 else None
if K56 is not None and not in672:
    t1 = time.time(); K672 = conj_class_keys(e672, 1_000_000)
    tick("class of Phi.g672: %s elements (%.1fs)" % (len(K672) if K672 else "> 1,000,000", time.time() - t1))
else: K672 = None
S3, tries3 = sample_twisted(pool, 3, 40, tries_max=300000)
n_turn = sum(1 for ea, _ in S3 if ea.tobytes() in TPHI); n56 = sum(1 for ea, _ in S3 if K56 and ea.tobytes() in K56)
n672 = sum(1 for ea, _ in S3 if K672 and ea.tobytes() in K672)
say("  %d order-3 twisted elements (%d tries; density %.5f): in the turn's class %d; in class(Phi.g56) %d; in class(Phi.g672) %d; types %s"
    % (len(S3), tries3, len(S3) / tries3, n_turn, n56, n672, {str(dict(Counter(c))): v for c, v in Counter(c for _, c in S3).items()}))
DENS[3] = [Fraction(1, 12096)] + ([Fraction(len(K56), OMEGA)] if K56 else []) + ([Fraction(len(K672), OMEGA)] if K672 else [])
CENTS[3] = [12096] + ([OMEGA // len(K56)] if K56 else []) + ([OMEGA // len(K672)] if K672 else [])
check("AM3a", "REGISTERED: the Omega-class of Phi.g56 has EXACTLY 806,400 = |Omega|/216 elements; Phi.g672 lies in it (guess); the 40 sampled order-3 twisted "
      "elements are none of them turns and all in the class of Phi.g56 -- two order-3 classes, densities 1/216 and 1/12,096",
      K56 is not None and len(K56) == 806400 and in672 is True and len(S3) == 40 and n_turn == 0 and n56 == 40,
      "|class(Phi.g56)| = %s; Phi.g672 in it: %s; samples: turn %d, g56-class %d, g672-class %d" % (len(K56) if K56 else None, in672, n_turn, n56, n672))


# ---------------- POST-REVEAL (finding, not amendment): the first run found |class(Phi.g56)| = 14,400 = |class(Phi)| and a census excess of exactly
# 1/12096 -- the arithmetic forces Phi.g56 to be a turn.  Tested directly here; the duplicate density removed from the census.
banner("AM3b -- POST-REVEAL: is Phi.g56 a turn?")
g56_is_turn = e56.tobytes() in TPHI
check("AM3b", "POST-REVEAL FINDING: Phi.g56 (g56 a heart at the still point, commuting with Phi) IS conjugate to Phi itself -- the class of 14,400 found in AM3a is the "
      "turn's own class; the order-3 twisted elements are TWO classes: the turn's (1/12,096) and Phi.g672's (806,400 = 1/216)" if g56_is_turn else
      "POST-REVEAL: Phi.g56 is NOT in the turn's class although the two classes have equal size 14,400 -- three order-3 classes stand", g56_is_turn)
if g56_is_turn:
    DENS[3] = [Fraction(1, 12096)] + ([Fraction(len(K672), OMEGA)] if K672 else []); CENTS[3] = [12096] + ([OMEGA // len(K672)] if K672 else [])
    note("census corrected: the class of Phi.g56 is the turn's class and is counted once")
banner("AM4 -- the census closes")
total = sum(sum(v) for v in DENS.values())
say("  class densities by order: %s" % {o: [str(d) for d in DENS[o]] for o in sorted(DENS)})
say("  sum = %s = %.6f" % (total, float(total)))
check("AM4a", "REGISTERED: the densities of all classes found (SM-047, 049, 050, this stone) sum to EXACTLY 1", total == 1,
      ("shortfall %s" % (1 - total)) if total < 1 else ("excess %s" % (total - 1)) if total > 1 else "exact")

banner("AM5 -- [obs] the roof's twisted class list, computed")
say("  order | classes | centralizer orders | share")
for o in sorted(DENS, reverse=True):
    say("  %5d | %7d | %s | %s" % (o, len(DENS[o]), CENTS[o], " + ".join(str(d) for d in DENS[o])))
say("  total classes in the coset: %d" % sum(len(v) for v in DENS.values()))
json.dump({"brief_sha": sha_am, "dens": {str(o): [str(d) for d in v] for o, v in DENS.items()}, "cents": {str(o): v for o, v in CENTS.items()},
           "total": str(total), "class56": len(K56) if K56 else None, "g672_in_56": in672, "types9": {str(dict(Counter(k))): v for k, v in types9.items()},
           "types6": {str(dict(Counter(k))): v for k, v in types6.items()}}, open(os.path.join(CACHE_AM, "witnesses_am.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
