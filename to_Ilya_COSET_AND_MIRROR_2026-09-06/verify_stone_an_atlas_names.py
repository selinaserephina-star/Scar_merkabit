# -*- coding: utf-8 -*-
r"""verify_stone_an_atlas_names.py -- STONE AN: THE ATLAS NAMES

Brief: BRIEF_STONE_AN_ATLAS_NAMES.md (lock BRIEF_STONE_AN_LOCK.sha256,
re-verified as check AN0).

The published character table of O8+(2).3 (GAP CTblLib 1.3.11,
data/ctoorth2.tbl; origin: ATLAS of finite groups), header blocks cited
verbatim in _stone_an_cache/, against our fourteen classes (SM-047..051):
the count, the (order, centralizer) multiset, the power maps against our
fibre data, the two twenty-fours told apart, the names.

Machinery: the cited headers; verify_stone_aa_roofclock.py lines 71-696
VERBATIM and the SM-045/047/048/050/051 helpers for three computations.
DISCIPLINE: compute, never assert; cited data quoted with source and
version; registered expectations resolvable INVERTED at equal prominence;
exact arithmetic; no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_an_atlas_names.py
"""
import itertools, json, os, sys, time, random, hashlib, re
from collections import Counter
from fractions import Fraction
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_an_atlas_names.log", "w", encoding="utf-8")
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
CACHE_AN = "_stone_an_cache"; os.makedirs(CACHE_AN, exist_ok=True)
random.seed(20260903)

say("=" * 78); say("STONE AN -- THE ATLAS NAMES (the published table of O8+(2).3 against our fourteen classes)"); say("=" * 78)
BRIEF_AN = "BRIEF_STONE_AN_ATLAS_NAMES.md"; LOCK_AN = open("BRIEF_STONE_AN_LOCK.sha256").read().strip()
sha_an = hashlib.sha256(open(BRIEF_AN, "rb").read()).hexdigest()
check("AN0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AN_LOCK.sha256" % BRIEF_AN, sha_an == LOCK_AN, sha_an[:16] + "...")

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
pass  # [AN] AA's np.save of phi360.npy REMOVED
tick("stage 2 done")


# =====================================================================
# VERBATIM helpers from SM-045 / SM-047 / SM-048 / SM-050 / SM-051 verifiers
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


# =====================================================================
# THE CITED DATA (headers of the tables "O8+(2)" and "O8+(2).3", CTblLib 1.3.11, data/ctoorth2.tbl)
# =====================================================================
banner("AN-data -- the cited headers, parsed")
NL = chr(10)
def parse_header(path):
    s = open(path, encoding="utf-8").read()
    head = s.split(NL + NL + "ALF(")[0]
    i = head.index('"' + NL + "]," + NL + "[") + 5        # the pattern is 6 characters; +5 lands on the opening bracket of the centralizer list
    rest = head[i:]
    j = rest.index("]," + NL + "[")
    cents = [int(x) for x in rest[1:j].replace(NL, "").split(",")]
    pm = rest[j + 3:].strip()
    while pm.endswith(","): pm = pm[:-1].strip()
    assert pm.startswith("[") and pm.endswith("]"), pm[-20:]
    pm_txt = pm[1:-1].replace(NL, "")
    parts = []; depth = 0; cur = ""
    for ch in pm_txt:
        if ch == "[": depth += 1
        if ch == "]": depth -= 1
        if ch == "," and depth == 0: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur); maps = {}
    for idx, p in enumerate(parts, start=1):
        p = p.strip()
        if p.startswith("["): maps[idx] = [int(x) for x in p[1:-1].split(",")]
    f = re.search(r'ALF\("O8\+\(2\)","O8\+\(2\)\.3",\[([0-9,\s]+)\]', s)
    fus = [int(x) for x in re.sub(r"\s", "", f.group(1)).split(",")] if f else None
    return cents, maps, fus, hashlib.sha256(open(path, "rb").read()).hexdigest()
def orders_from(maps, n):
    def order(c):
        best = None
        for a in range(13):
            for b in range(7):
                for cc in range(3):
                    for d in range(2):
                        x = c
                        for _ in range(a): x = maps[2][x - 1]
                        for _ in range(b): x = maps[3][x - 1]
                        for _ in range(cc): x = maps[5][x - 1]
                        for _ in range(d): x = maps[7][x - 1]
                        if x == 1:
                            o = 2 ** a * 3 ** b * 5 ** cc * 7 ** d
                            if best is None or o < best: best = o
        return best
    return [order(c) for c in range(1, n + 1)]
def pw(maps, c, k):
    x = c
    for p in (2, 3, 5, 7):
        while k % p == 0: x = maps[p][x - 1]; k //= p
    return x
def letter_names(orders):
    names = []; cnt = {}
    for o in orders:
        cnt[o] = cnt.get(o, 0) + 1; names.append("%d%s" % (o, chr(ord('A') + cnt[o] - 1)))
    return names
PATH_G = os.path.join(CACHE_AN, "O8+(2)_ctbllib-1.3.11_header_and_fusion.txt")
PATH_G3 = os.path.join(CACHE_AN, "O8+(2).3_ctbllib-1.3.11_ctoorth2_header.txt")
cG, mG, fus, shaG = parse_header(PATH_G); cG3, mG3, _, shaG3 = parse_header(PATH_G3)
oG = orders_from(mG, len(cG)); oG3 = orders_from(mG3, len(cG3))
nG = letter_names(oG)
say("  cited: O8+(2) header sha256 %s (%d classes); O8+(2).3 header sha256 %s (%d classes)" % (shaG[:16], len(cG), shaG3[:16], len(cG3)))
say("  O8+(2) ATLAS-rule names: %s" % nG)
say("  O8+(2).3 classes (index, order, centralizer): %s" % [(i + 1, oG3[i], cG3[i]) for i in range(len(cG3))])

banner("AN1 -- the count: 53 / 55 classes, 13 fused triples, 14 fixed classes, 14 outer classes per coset")
img = Counter(fus); triples = [k for k, v in img.items() if v == 3]; fixed = [k for k, v in img.items() if v == 1]
fixed_names = [nG[i] for i in range(len(fus)) if img[fus[i]] == 1]
n_inner = max(fus); n_outer = len(cG3) - n_inner
say("  fusion O8+(2) -> O8+(2).3: %d triples, %d fixed classes; inner classes of G.3: %d; outer: %d" % (len(triples), len(fixed), n_inner, n_outer))
say("  triality-fixed classes of O8+(2): %s" % fixed_names)
f = len(fixed)
check("AN1a", "[P cited] O8+(2) has 53 classes, O8+(2).3 has 55; the fusion fuses exactly 13 triples and fixes 14 classes; 27 inner + 28 outer = 55, i.e. 14 classes "
      "per outer coset (Brauer's permutation lemma) = our census; the fixed classes are 1A, 2A, 2E, 3D, 3E, 4A, 4B, 4F, 6G, 6N, 7A, 8A, 8B, 12D",
      len(cG) == 53 and len(cG3) == 55 and len(triples) == 13 and f == 14 and n_inner == 27 and n_outer == 28 and
      fixed_names == ["1A", "2A", "2E", "3D", "3E", "4A", "4B", "4F", "6G", "6N", "7A", "8A", "8B", "12D"], "f = %d" % f)

banner("AN2 -- the multiset of (order, centralizer) over the outer classes against ours")
outer = list(range(n_inner + 1, len(cG3) + 1))
pairs_ok = all(oG3[c - 1] == oG3[c] and cG3[c - 1] == cG3[c] for c in outer[::2])
pub = sorted((oG3[c - 1], cG3[c - 1]) for c in outer[::2])
OURS = {18: [6], 24: [8, 8], 21: [7], 12: [32, 4, 48, 96], 9: [18], 6: [192, 24, 48], 3: [12096, 216]}
ours = sorted((o, 3 * c) for o, L in OURS.items() for c in L)
say("  published outer (order, |C_{G.3}|): %s" % pub); say("  ours (order, 3|C_Omega|):          %s" % ours)
check("AN2a", "REGISTERED: the 28 outer classes are 14 inverse pairs with equal order and centralizer, and the multiset of (order, centralizer) over the 14 EQUALS "
      "ours (order, 3|C_Omega|) exactly: {(3,36288),(3,648),(6,576),(6,144),(6,72),(9,54),(12,288),(12,144),(12,96),(12,12),(18,18),(21,21),(24,24),(24,24)}",
      pairs_ok and pub == ours and len(pub) == 14)

banner("AN3 -- the published power maps against our fibre data")
def inner_by(o, cent): return [c for c in range(1, n_inner + 1) if oG3[c - 1] == o and cG3[c - 1] == cent]
HEART = inner_by(3, 5832); C2A = inner_by(2, 331776); C2E = inner_by(2, 9216)
TURN = [c for c in outer if oG3[c - 1] == 3 and cG3[c - 1] == 36288]; C648 = [c for c in outer if oG3[c - 1] == 3 and cG3[c - 1] == 648]
say("  reference classes: heart(3, 5832) = %s [3D]; 2A(331776) = %s; 2E(9216) = %s; turn(3, 36288) = %s; Phi.g672-class(3, 648) = %s" % (HEART, C2A, C2E, TURN, C648))
def oc(c): return (oG3[c - 1], cG3[c - 1])
def rep(o, cent): return next(c for c in outer[::2] if oc(c) == (o, cent))
e18 = rep(18, 18); e21 = rep(21, 21); e9 = rep(9, 54)
r12 = {cent: rep(12, cent) for cent in (288, 144, 96, 12)}; r6 = {cent: rep(6, cent) for cent in (576, 144, 72)}; r24 = [c for c in outer[::2] if oc(c) == (24, 24)]
checks = {
 "18: e^6 -> heart": pw(mG3, e18, 6) in HEART, "18: e^9 -> 2A": pw(mG3, e18, 9) in C2A, "18: e^2 -> (9,54)": oc(pw(mG3, e18, 2)) == (9, 54),
 "18: e^3 -> inner (6,648)": oc(pw(mG3, e18, 3)) == (6, 648) and pw(mG3, e18, 3) <= n_inner,
 "21: e^7 -> turn": pw(mG3, e21, 7) in TURN, "21: e^3 -> (7,21)": oc(pw(mG3, e21, 3)) == (7, 21),
 "24: e^12 -> 2A (both)": all(pw(mG3, c, 12) in C2A for c in r24),
 "12/288,144,96: e^6 -> 2A": all(pw(mG3, r12[k], 6) in C2A for k in (288, 144, 96)), "12/12: e^6 -> 2E": pw(mG3, r12[12], 6) in C2E,
 "9: e^3 -> heart": pw(mG3, e9, 3) in HEART,
 "6/576: e^3 -> 2A": pw(mG3, r6[576], 3) in C2A, "6/144: e^3 -> 2E": pw(mG3, r6[144], 3) in C2E, "6/72: e^3 -> 2E": pw(mG3, r6[72], 3) in C2E,
 "6/576: e^2 -> turn": oc(pw(mG3, r6[576], 2)) == (3, 36288), "6/144: e^2 -> turn": oc(pw(mG3, r6[144], 2)) == (3, 36288),
 "6/72: e^2 -> (3,648)": oc(pw(mG3, r6[72], 2)) == (3, 648),
}
for k, v in checks.items(): say("  %-28s %s" % (k, v))
check("AN3a", "REGISTERED: every published power-map entry that our stones recorded agrees -- eighteen: sixth power the heart (5832 = 3*1944), ninth power 2A "
      "(331776 = 3*110592, our 1,575-class); twenty-fours: twelfth powers 2A; twelves 288/144/96: sixth powers 2A, the 12: 2E (9216 = 3*3072, our 56,700-class); "
      "nine: cube the heart; sixes 576/144/72: cubes 2A/2E/2E; seven-beat clock: seventh power the turn, cube the (7,21) class", all(checks.values()))

banner("AN3b -- three entries our stones did not record, computed now")
PHI_cached = tuple(int(v) for v in np.load(os.path.join(CACHE_AA, "phi360.npy")))
PHIa = A(PHI)
c240 = pident(240)
for s_ in S240: c240 = pmul(c240, s_)
ec = pmul(PHI, P360(M2_of(c240))); E18 = A(ec); x = A(ppow(ec, 6)); e3 = A(ppow(ec, 3))
TX = conj_class_T(x, CAP); CX = schreier_centralizer(TX, cap=20000)
C_e3 = [h for h in CX if np.array_equal(aconj(h, e3), e3)]
check("AN3b", "REGISTERED: |C_Omega((Phi.c-bar)^3)| = 216 (the published inner class of order 6 and centralizer 648 = 3*216 that the eighteen cubes into) -- "
      "so the Omega-class of the cube has 806,400 elements, of which SM-048's 504 still-point elements are the part inside G2(2)",
      PHI == PHI_cached and len(CX) == 1944 and len(C_e3) == 216, "|C| = %d" % len(C_e3))
G_set120 = set(G_list); random.seed(20260905)
while True:
    gens120 = [G_list[random.randrange(len(G_list))] for _ in range(4)]
    if len(closure(gens120, cap=13000)) == 12096: break
gens360 = [A(P360(mat_of_perm(g))) for g in gens120]; G360 = closure_np(gens360, cap=13000)
G3 = [g for g in G360 if aorder(g) == 3]; cls3 = gclasses(G3, gens360)
g672 = next(r for r, n in cls3 if n == 672); e672 = amul(PHIa, g672)
TPHI = conj_class_keys(PHIa, 20000); t1 = time.time(); K672 = conj_class_keys(e672, 1_000_000); tick("class of Phi.g672: %d (%.1fs)" % (len(K672), time.time() - t1))
random.seed(20260907)
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)
S6, _ = sample_twisted(pool, 6, 150)
sq = Counter()
# POST-REVEAL instrumentation fix: e^2 of a twisted e lies in the OTHER coset Omega.Phi^2, whose classes are the inverses of ours
# (the first run tested e^2 against classes in Omega.Phi and found every square "elsewhere"; FIRSTRUN log kept).  e^4 = e^-2 lies in Omega.Phi.
for ea, ct in S6:
    e4 = amul(amul(ea, ea), amul(ea, ea)); k = e4.tobytes()
    where = "turn" if k in TPHI else ("g672-class" if k in K672 else "elsewhere")
    sq[(str(dict(Counter(ct))), where)] += 1
say("  squares of sampled order-6 twisted elements (tested through e^4 = e^-2, in the coset of Phi), by cycle type: %s" % dict(sq))
T48 = "{6: 48, 3: 24}"; T56 = "{6: 56, 3: 8}"
ok6 = (all(w == "turn" for (t, w) in sq if t == T48) and any(w == "turn" for (t, w) in sq if t == T56)
       and any(w == "g672-class" for (t, w) in sq if t == T56) and not any(w == "elsewhere" for _, w in sq))
check("AN3c", "REGISTERED: the squares of the 576-class {6:48,3:24} are all turns; the type {6:56,3:8} (the 144- and 72-classes of SM-051) squares partly to turns (the "
      "144-class) and partly into the class of Phi.g672 (the 72-class); no square lands elsewhere", ok6)

banner("AN4 -- the two twenty-fours told apart by their squares")
G8 = [g for g in G360 if aorder(g) == 8]; cls8 = gclasses(G8, gens360)
sq_pub = {c: oc(pw(mG3, c, 2)) for c in r24}
say("  published: %s" % {c: "24-class %d squares into %s" % (c, sq_pub[c]) for c in r24})
RES = {}
for rep_, n in cls8:
    e = amul(PHIa, rep_); ct = str(dict(Counter(cycle_type([int(v) for v in e])))); e2 = amul(e, e)
    ct2 = str(dict(Counter(cycle_type([int(v) for v in e2]))))
    z = e2.copy()
    for _ in range(5): z = amul(e2, z)
    T = conj_class_T(z, CAP); C = schreier_centralizer(T, cap=400000)
    Ce2 = [h for h in C if np.array_equal(aconj(h, e2), e2)]
    RES[ct] = dict(square_type=ct2, cent_sq=len(Ce2))
    tick("type %s: square has cycle type %s and |C_Omega(e^2)| = %d -> the order-12 class of density 1/%d, published centralizer %d" % (ct, ct2, len(Ce2), len(Ce2), 3 * len(Ce2)))
A_ = "{24: 12, 12: 3, 6: 5, 3: 2}"; B_ = "{24: 12, 12: 5, 6: 1, 3: 2}"
okA = RES[A_]["cent_sq"] == 96 and RES[A_]["square_type"] == "{12: 24, 6: 6, 3: 12}"
okB = RES[B_]["cent_sq"] == 32 and RES[B_]["square_type"] == "{12: 24, 6: 10, 3: 4}"
check("AN4a", "REGISTERED: type A's square has cycle type {12:24, 6:6, 3:12} and Omega-centralizer 96 (the 1/96 class, published centralizer 288); type B's square has "
      "{12:24, 6:10, 3:4} and centralizer 32 (the 1/32 class, published 96) -- type A <-> the published 24-class squaring into the 288-class, type B <-> the one "
      "squaring into the 96-class", okA and okB and sorted(sq_pub.values()) == [(12, 96), (12, 288)])
c8 = [c for c in range(1, n_inner + 1) if oG3[c - 1] == 8]
check("AN4b", "[P cited] the cubes of the two 24-classes are the two inner order-8 classes (8A, 8B), each with centralizer 96 in G.3, so |C_Omega(g8)| = 32 and the "
      "Omega-class of g8 has 5,443,200 elements -- why SM-049 could not enumerate the cube's class", sorted(pw(mG3, c, 3) for c in r24) == c8 and all(cG3[c - 1] == 96 for c in c8))

banner("AN5 -- the names [obs]: inner by fusion, outer by the letter rule in table order")
inner_names = {}
for c in range(1, n_inner + 1):
    src_ = [nG[i] for i in range(len(fus)) if fus[i] == c]
    inner_names[c] = src_[0] if len(src_) == 1 else "%s(=%s)" % (src_[0], "/".join(src_))
gap_names = letter_names(oG3)
say("  inner classes of G.3 (index: O8+(2) name(s), order, |C_{G.3}|):")
for c in range(1, n_inner + 1): say("    %2d: %-14s %2d %8d" % (c, inner_names[c], oG3[c - 1], cG3[c - 1]))
say("  our fourteen classes with the published data (order, |C_Omega|, |C_{G.3}|, table index pair, GAP-style name, what it is):")
WHAT = {(3, 12096): "the turn Phi (and Phi.g56: the heart at the still point, turned)", (3, 216): "Phi.g672", (6, 192): "the 576-class", (6, 24): "the 72-class",
        (6, 48): "the 144-class", (9, 18): "(Phi.c-bar)^-2's class", (12, 32): "the 1/32 class", (12, 4): "the 1/4 class (not from the still point)", (12, 48): "the 1/48 class",
        (12, 96): "the 1/96 class (type A's square)", (18, 6): "Phi.c-bar, the roof's eighteen", (21, 7): "Phi.g7, the seven-beat clock",
        (24, 8): "Phi.g8, both types (squares into 288 / 96)"}
table = []
for o, L in sorted(OURS.items()):
    for cO in L:
        idx = [c for c in outer[::2] if oc(c) == (o, 3 * cO)]
        table.append((o, cO, 3 * cO, idx, [gap_names[c - 1] + "/" + gap_names[c] for c in idx], WHAT.get((o, cO), "")))
for row in table: say("    %s" % (row,))
c648 = [c for c in range(1, n_inner + 1) if oc(c) == (6, 648)]
say("  key inner classes: heart = O8+(2) 3D (1944 -> 5832 in G.3); E8/D4 hearts = 3A/3B/3C fused (77760); involution fibres: 2A (110592 -> 331776), 2E (3072 -> 9216); "
    "the eighteen's cube: the inner (6, 648) class = %s; the seven: 7A; the eights: 8A, 8B" % [inner_names[c] for c in c648])
json.dump({"brief_sha": sha_an, "cited_sha": {"O8+(2)": shaG, "O8+(2).3": shaG3}, "fixed_classes": fixed_names, "published_outer": pub, "ours": ours,
           "power_checks": checks, "C_e3": len(C_e3), "squares6": {str(k): v for k, v in sq.items()}, "twentyfours": RES, "table": [list(map(str, r)) for r in table],
           "inner_names": inner_names}, open(os.path.join(CACHE_AN, "witnesses_an.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
