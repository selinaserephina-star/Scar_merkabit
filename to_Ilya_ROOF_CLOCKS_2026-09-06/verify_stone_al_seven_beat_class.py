# -*- coding: utf-8 -*-
r"""verify_stone_al_seven_beat_class.py -- STONE AL: THE SEVEN-BEAT CLOCK'S CLASS, AND THE TURN'S CENTRALIZER

Brief: BRIEF_STONE_AL_SEVEN_BEAT_CLASS.md (lock BRIEF_STONE_AL_LOCK.sha256,
re-verified as check AL0).

Lever: (Phi.g7)^7 = Phi, so the fibre over Phi is C_Omega(Phi) = the
still point (made exact here by the class count 14,400).  Then the
order-21 class, and the order-12 elements via the involution fibre.

BARS: AL1 class of Phi = 14,400, C_Omega(Phi) = G2(2) as a set; AL2
C_Omega(Phi.g7) = <g7>, class 1/7; AL3 300 order-21 samples conjugated
exactly; AL4 order-12 types and classes; AL5 [obs].

Machinery: verify_stone_aa_roofclock.py lines 71-696 VERBATIM; helpers of
SM-045/047/048 VERBATIM; sealed caches READ-ONLY.  DISCIPLINE: compute,
never assert; registered expectations resolvable INVERTED at equal
prominence; exact arithmetic; no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_al_seven_beat_class.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_al_seven_beat_class.log", "w", encoding="utf-8")
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
CACHE_AL = "_stone_al_cache"; os.makedirs(CACHE_AL, exist_ok=True)
random.seed(20260903)

say("=" * 78); say("STONE AL -- THE SEVEN-BEAT CLOCK'S CLASS, AND THE TURN'S CENTRALIZER"); say("=" * 78)
BRIEF_AL = "BRIEF_STONE_AL_SEVEN_BEAT_CLASS.md"; LOCK_AL = open("BRIEF_STONE_AL_LOCK.sha256").read().strip()
sha_al = hashlib.sha256(open(BRIEF_AL, "rb").read()).hexdigest()
check("AL0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AL_LOCK.sha256" % BRIEF_AL, sha_al == LOCK_AL, sha_al[:16] + "...")

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
pass  # [AL] AA's np.save of phi360.npy REMOVED
tick("stage 2 done")


# =====================================================================
# VERBATIM helpers from SM-045 / SM-047 / SM-048 verifiers
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

# =====================================================================
# STONE AL stages
# =====================================================================
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

banner("AL0a -- replay: the still point on 360 points")
PHI_cached = tuple(int(v) for v in np.load(os.path.join(CACHE_AA, "phi360.npy")))
PHIa = A(PHI); PHIai = ainv(PHIa)
G_set120 = set(G_list)
random.seed(20260905)
while True:
    gens120 = [G_list[random.randrange(len(G_list))] for _ in range(4)]
    if len(closure(gens120, cap=13000)) == 12096: break
gens360 = [A(P360(mat_of_perm(g))) for g in gens120]
G360 = closure_np(gens360, cap=13000); G360keys = set(g.tobytes() for g in G360)
check("AL0a", "Phi equals the sealed cache; G2(2) on 360 points: 12,096 elements whose vector parts are the sealed G_list",
      PHI == PHI_cached and len(G360) == 12096 and set(tuple(int(v) for v in g[:120]) for g in G360) == G_set120)

banner("AL1 -- the turn's centralizer is the still point, exactly")
t1 = time.time(); TPHI = conj_class_T(PHIa, CAP)
tick("Omega-class of Phi: %d elements (%.1fs)" % (len(TPHI), time.time() - t1))
CPHI = schreier_centralizer(TPHI)
CPHIkeys = set(h.tobytes() for h in CPHI)
check("AL1a", "REGISTERED: the Omega-class of Phi has EXACTLY 14,400 = |Omega|/|G2(2)| elements and its Schreier-closed centralizer C_Omega(Phi) EQUALS the "
      "still point G2(2) as a set of 12,096 permutations -- SM-038's Fix(tau'') = G2(2), now exact", len(TPHI) == 14400 and CPHIkeys == G360keys,
      "|C_Omega(Phi)| = %d" % len(CPHI))

banner("AL2 -- the seven-beat clock's centralizer and class")
G7 = [g for g in G360 if aorder(g) == 7]
cls7 = gclasses(G7, gens360)
g7 = G7[0]; e21 = amul(PHIa, g7)
C21 = [h for h in G360 if np.array_equal(aconj(h, e21), e21)]
pw7 = closure_np([g7], cap=10)
check("AL2a", "REGISTERED: G2(2)'s 1,728 elements of order 7 form ONE G2(2)-class; C_Omega(Phi.g7) = {h in G2(2): h g7 h^-1 = g7} = <g7> of order 7; the class of "
      "Phi.g7 has 174,182,400/7 = 24,883,200 elements = 1/7 of the coset (sampled 14.27 %)",
      len(G7) == 1728 and len(cls7) == 1 and cls7[0][1] == 1728 and aorder(e21) == 21 and len(C21) == 7 and set(h.tobytes() for h in C21) == set(h.tobytes() for h in pw7),
      "|C| = %d" % len(C21))

banner("AL3 -- one class: 300 sampled order-21 twisted elements, each tested exactly through the fibre over Phi")
random.seed(20260906)
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)
S21, tries = sample_twisted(pool, 21, 300)
Ginv = [ainv(g) for g in G360]
in_phi = 0; conj_n = 0
for ea, ct in S21:
    z = ea.copy()
    for _ in range(6): z = amul(ea, z)                 # e^7
    k = z.tobytes()
    if k not in TPHI: continue
    in_phi += 1
    u = TPHI[k]; epp = aconj(ainv(u), ea, u)           # seventh power -> Phi
    if any(np.array_equal(aconj(h, epp, hi), e21) for h, hi in zip(G360, Ginv)): conj_n += 1
say("  %d order-21 twisted elements (%d tries; density %.4f vs 1/7 = 0.1429); seventh powers in class(Phi): %d; conjugate to Phi.g7: %d" % (len(S21), tries, len(S21) / tries, in_phi, conj_n))
check("AL3a", "REGISTERED: all 300 sampled order-21 twisted elements have seventh power in the class of Phi and are conjugate to Phi.g7 (exact, via the still point) "
      "-- one class of density exactly 1/7 to the precision of the sample", len(S21) == 300 and in_phi == 300 and conj_n == 300)

banner("AL4 -- the order-12 twisted elements: types, centralizers, classes")
S12, tries12 = sample_twisted(pool, 12, 200)
types12 = Counter(ct for _, ct in S12)
say("  200 order-12 twisted elements (%d tries; density %.4f): cycle types %s" % (tries12, 200 / tries12, {str(dict(Counter(k))): v for k, v in types12.items()}))
# the still point's order-12 twisted elements: Phi.g4 and Phi.g12
sp_types = Counter()
for g in G360:
    og = aorder(g)
    if og in (4, 12):
        sp_types[(og, cycle_type([int(v) for v in amul(PHIa, g)]))] += 1
say("  from the still point: %s" % {("Phi.g%d %s" % (o, dict(Counter(k)))): v for (o, k), v in sp_types.items()})
sp_set = set(k for (o, k) in sp_types)
check("AL4a", "REGISTERED GUESS: the sampled order-12 cycle types are exactly those realised from the still point by Phi.g4 and Phi.g12" if set(types12) == sp_set else
      "REGISTERED GUESS INVERTED: the sampled order-12 types (%d) differ from the still point's (%d): sample-only %d, still-point-only %d"
      % (len(types12), len(sp_set), len(set(types12) - sp_set), len(sp_set - set(types12))), set(types12) == sp_set)
RES12 = {}; OTHERS = {}
for ct in types12:
    name = str(dict(Counter(ct)))
    e = next(ea for ea, c in S12 if c == ct)
    z = e.copy()
    for _ in range(5): z = amul(e, z)                   # e^6, an involution in Omega
    assert aorder(z) == 2 and memO(tuple(int(v) for v in z))
    t1 = time.time(); TZ = conj_class_T(z, CAP)
    if TZ is None:
        note("type %s: class of e^6 exceeds the cap -- not computed" % name); RES12[name] = None; continue
    CZ = schreier_centralizer(TZ, cap=400000)
    if CZ is None:
        note("type %s: class of e^6 has %d elements, centralizer %d -- closure over cap, not computed" % (name, len(TZ), 174182400 // len(TZ))); RES12[name] = None; continue
    CZinv = [ainv(h) for h in CZ]
    Ce = [h for h in CZ if np.array_equal(aconj(h, e), e)]
    same = 0; n_t = 0
    for ea, c in S12:
        if c != ct: continue
        n_t += 1
        zp = ea.copy()
        for _ in range(5): zp = amul(ea, zp)
        k = zp.tobytes()
        if k not in TZ: continue
        u = TZ[k]; epp = aconj(ainv(u), ea, u)
        if any(np.array_equal(aconj(h, epp, hi), e) for h, hi in zip(CZ, CZinv)): same += 1
        else: OTHERS.setdefault(name, []).append(ea)
    RES12[name] = dict(class6=len(TZ), cent6=len(CZ), cent=len(Ce), density=1.0 / len(Ce), n=n_t, same=same)
    tick("type %s: |class(e^6)| = %d, |C(e^6)| = %d, |C_Omega(e)| = %d -> class density 1/%d; sampled of this type %d, conjugate to the representative %d"
         % (name, len(TZ), len(CZ), len(Ce), len(Ce), n_t, same))
done = [v for v in RES12.values() if v is not None]
one_each = all(v["same"] == v["n"] for v in done) and len(done) == len(RES12)
dsum = sum(v["density"] for v in done)
check("AL4b", "REGISTERED GUESS: one class per order-12 type (every sampled element conjugate to its type's representative) and the class densities sum to the "
      "sampled 31.5 %% within error (sum = %.4f, sampled %.4f)" % (dsum, 200 / tries12), one_each and abs(dsum - 200 / tries12) < 0.03)


# ---------------- POST-REVEAL (finding, not amendment): the type whose sample was not one class -- a second representative
banner("AL4c -- POST-REVEAL: the split type, second representative")
RES12c = {}
for name, lst in OTHERS.items():
    rep2 = lst[0]; z2 = rep2.copy()
    for _ in range(5): z2 = amul(rep2, z2)
    T2 = conj_class_T(z2, CAP)
    if T2 is None: note("type %s: second representative's e^6 class over cap" % name); continue
    C2 = schreier_centralizer(T2, cap=400000)
    if C2 is None: note("type %s: second centralizer closure over cap" % name); continue
    C2inv = [ainv(h) for h in C2]
    Ce2 = [h for h in C2 if np.array_equal(aconj(h, rep2), rep2)]
    same2 = 1
    for ea in lst[1:]:
        zp = ea.copy()
        for _ in range(5): zp = amul(ea, zp)
        k = zp.tobytes()
        if k not in T2: continue
        u = T2[k]; epp = aconj(ainv(u), ea, u)
        if any(np.array_equal(aconj(h, epp, hi), rep2) for h, hi in zip(C2, C2inv)): same2 += 1
    RES12c[name] = dict(class6=len(T2), cent6=len(C2), cent=len(Ce2), density=1.0 / len(Ce2), n=len(lst), same=same2)
    tick("type %s: second representative: |class(e^6)| = %d, |C_Omega(e)| = %d -> density 1/%d; of the %d non-conjugate samples, %d conjugate to it"
         % (name, len(T2), len(Ce2), len(Ce2), len(lst), same2))
    d_first = RES12[name]["density"]
    check("AL4c", "POST-REVEAL FINDING: the type %s is exactly TWO classes on the sample (densities 1/%d and 1/%d, together %.4f; sampled type density %.4f)"
          % (name, int(round(1 / d_first)), len(Ce2), d_first + 1.0 / len(Ce2), RES12[name]["n"] / tries12) if same2 == len(lst) else
          "POST-REVEAL: the type %s has MORE than two classes on the sample (%d of %d non-conjugate samples match the second representative)" % (name, same2, len(lst)),
          same2 == len(lst))
dsum_all = sum(v["density"] for v in RES12.values() if v) + sum(v["density"] for v in RES12c.values())
note("[obs] order-12 class densities in hand: %s; sum %.4f (SM-039 sampled 0.3153, this stone 0.2833)"
     % ({n: "1/%d" % int(round(1 / v["density"])) for n, v in RES12.items() if v} | {n + " (2nd)": "1/%d" % int(round(1 / v["density"])) for n, v in RES12c.items()}, dsum_all))
banner("AL5 -- [obs] the twisted coset accounted")
S3, tries3 = sample_twisted(pool, 3, 40, tries_max=200000)
t3 = Counter(ct for _, ct in S3)
note("[obs] sampled order-3 twisted elements: %d in %d tries (%.4f); cycle types %s; Phi's class has 14,400 elements = %.5f of the coset"
     % (len(S3), tries3, len(S3) / tries3 if tries3 else 0, {str(dict(Counter(k))): v for k, v in t3.items()}, 14400 / 174182400))
acc = 1/6 + 1/4 + 1/7 + dsum_all
note("[obs] densities in hand: 18 -> 1/6, 24 -> 1/4, 21 -> 1/7, 12 -> %.4f; total %.4f; remainder for orders 9, 6, 3: %.4f (SM-039 sampled 9: 0.0554, 6: 0.0673, 3: 0.0047 = 0.1274)" % (dsum, acc, 1 - acc))
json.dump({"brief_sha": sha_al, "class_phi": len(TPHI), "cent_phi": len(CPHI), "cent_21": len(C21), "sample21": {"n": len(S21), "conj": conj_n},
           "types12": {str(dict(Counter(k))): v for k, v in types12.items()}, "res12": RES12, "res12c": RES12c, "acc": acc}, open(os.path.join(CACHE_AL, "witnesses_al.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
