# -*- coding: utf-8 -*-
r"""verify_stone_ai_class18.py -- STONE AI: THE CLASS OF THE EIGHTEEN, AND THE HEART'S CENTRALIZER

Brief: BRIEF_STONE_AI_CLASS_OF_THE_EIGHTEEN.md (lock BRIEF_STONE_AI_LOCK.sha256,
re-verified as check AI0).

Question: what is the centralizer of the heart x = (Phi.c-bar)^6, and are
the order-18 elements of the twisted coset one class?  Lever: e, e' with
e^6 = e'^6 = x are conjugate only by elements of C_Omega(x) (1944
elements); and the <Omega,Phi>-class of a twisted e is its Omega-class.

BARS: AI0a replay + class(x) with transversal; AI1 C_Omega(x) of order
1944 by Schreier generators, full centralizer 5832; AI2 C_Omega(e) = <e^3>
of order 6, class 29,030,400 = 1/6 of the coset; AI3 300 sampled order-18
twisted elements all conjugate to Phi.c-bar (exact, per element); AI4
[obs] order-24 centralizers if their cubes' classes fit the cap.

Machinery: verify_stone_aa_roofclock.py lines 71-696 VERBATIM; the
helpers of verify_stone_ag_seven_nines.py VERBATIM; sealed caches
READ-ONLY.  DISCIPLINE: compute, never assert; registered expectations
resolvable INVERTED at equal prominence; exact arithmetic; no registry/
git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ai_class18.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ai_class18.log", "w", encoding="utf-8")
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
CACHE_AI = "_stone_ai_cache"; os.makedirs(CACHE_AI, exist_ok=True)
random.seed(20260903)

say("=" * 78); say("STONE AI -- THE CLASS OF THE EIGHTEEN, AND THE HEART'S CENTRALIZER"); say("=" * 78)
BRIEF_AI = "BRIEF_STONE_AI_CLASS_OF_THE_EIGHTEEN.md"; LOCK_AI = open("BRIEF_STONE_AI_LOCK.sha256").read().strip()
sha_ai = hashlib.sha256(open(BRIEF_AI, "rb").read()).hexdigest()
check("AI0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AI_LOCK.sha256" % BRIEF_AI, sha_ai == LOCK_AI, sha_ai[:16] + "...")

# =====================================================================
# VERBATIM from verify_stone_aa_roofclock.py, lines 71-696 (STAGE 0-2 of SM-039); checks relabelled REPLAY-AA*, np.save removed
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
pass  # [AI] AA's np.save of phi360.npy REMOVED: the sealed cache is read, never written
tick("stage 2 done")


# =====================================================================
# VERBATIM helpers from verify_stone_ag_seven_nines.py (SM-045)
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

# =====================================================================
# STONE AI stages
# =====================================================================
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

banner("AI0a -- replay: the class of the heart, with a transversal")
PHI_cached = tuple(int(v) for v in np.load(os.path.join(CACHE_AA, "phi360.npy")))
c240 = pident(240)
for s in S240: c240 = pmul(c240, s)
cbar = M2_of(c240); ec = pmul(PHI, P360(cbar)); e = A(ec); x = A(ppow(ec, 6))
ALPHA_R = SIMPLE[0]; ALPHA = rmask[ridx[ALPHA_R]]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi7 = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi7[i]] for i in range(7)]
def refl240(b): return tuple(ridx[tuple(r[t] - dot4(r, b) * b[t] for t in range(8))] for r in roots)
def coxeter240(nodes):
    p = pident(240)
    for i in nodes: p = pmul(p, refl240(BETA[i]))
    return p
def mpow(M, k):
    R = tuple(1 << j for j in range(8)); B = M
    while k:
        if k & 1: R = mmul(R, B)
        B = mmul(B, B); k >>= 1
    return R
cb7 = M2_of(coxeter240(range(7))); cb6 = M2_of(coxeter240([0, 1, 2, 3, 4, 5]))
y7 = A(P360(mpow(cb7, 6))); y6 = A(P360(mpow(cb6, 4)))
t1 = time.time(); TX = conj_class_T(x, CAP)
tick("class of x with transversal: %d elements (%.1fs)" % (len(TX), time.time() - t1))
tr_ok = all(np.array_equal(aconj(TX[k], x), np.frombuffer(k, dtype=np.uint16)) for k in random.sample(list(TX), 500))
check("AI0a", "Phi equals the sealed cache; class(x) has 89,600 elements with a transversal (u_y x u_y^-1 = y checked on 500 random y); c-bar7^6 and c-bar6^4 in it",
      PHI == PHI_cached and len(TX) == 89600 and tr_ok and y7.tobytes() in TX and y6.tobytes() in TX)

banner("AI1 -- the centralizer of the heart by Schreier generators")
keys = list(TX); random.seed(20260905)
sgens = []
for _ in range(400):
    k = random.choice(keys); yv = np.frombuffer(k, dtype=np.uint16); u = TX[k]
    j = random.randrange(26); g, gi = GA[j], GAi[j]
    gy = g[yv[gi]]; ugy = TX[gy.tobytes()]
    sg = amul(ainv(ugy), amul(g, u))          # u_{gy}^-1 g u_y
    assert np.array_equal(aconj(sg, x), x)
    if not np.array_equal(sg, IDENT): sgens.append(sg)
CX = closure_np(sgens[:60], cap=20000)
if CX is not None and len(CX) < 1944:
    CX = closure_np(sgens, cap=20000)
tick("centralizer closure from %d Schreier generators: %s elements" % (len(sgens), len(CX) if CX else "cap"))
cent_ok = all(np.array_equal(aconj(h, x), x) for h in CX)
check("AI1a", "REGISTERED: C_Omega(x) has order EXACTLY 1944 = 2^3 * 3^5 (Schreier generators closed; |Omega| / |class| = %d) and every element commutes with x"
      % (174182400 // len(TX)), len(CX) == 1944 and cent_ok and 174182400 // len(TX) == 1944)
CXkeys = set(h.tobytes() for h in CX)
e_cent = np.array_equal(aconj(e, x), x)
cos = [amul(e, h) for h in CX]; cos2 = [amul(e, c) for c in cos]
full_keys = CXkeys | set(c.tobytes() for c in cos) | set(c.tobytes() for c in cos2)
check("AI1b", "REGISTERED: e = Phi.c-bar centralizes x (its sixth power) and lies outside Omega; C_full(x) = C_Omega(x) u e C_Omega(x) u e^2 C_Omega(x) has order 5832",
      e_cent and (not memO(ec)) and len(full_keys) == 5832)
ordc = Counter(aorder(h) for h in CX)
centre = [h for h in CX if all(np.array_equal(amul(h, g), amul(g, h)) for g in sgens[:60])]
centre = [h for h in centre if all(np.array_equal(amul(h, g), amul(g, h)) for g in CX)]
fixV = [i for i in range(120) if x[i] == i]
orbs = []; seen = set()
for i in fixV:
    if i in seen: continue
    o = set(int(h[i]) for h in CX); seen |= o; orbs.append(len(o))
note("[obs] element-order census of C_Omega(x): %s; centre of order %d; orbits of C_Omega(x) on the 3 fixed nonsingular vectors of x on V: %s"
     % (dict(sorted(ordc.items())), len(centre), sorted(orbs, reverse=True)))
xk = x.tobytes(); note("[obs] x in the centre: %s; elements of order 3 in the centre: %d" % (xk in set(h.tobytes() for h in centre), sum(1 for h in centre if aorder(h) == 3)))

banner("AI2 -- the centralizer of the eighteen")
Ce = [h for h in CX if np.array_equal(aconj(h, e), e)]
e3 = A(ppow(ec, 3)); pw = closure_np([e3], cap=100)
check("AI2a", "REGISTERED: C_Omega(e) = {h in C_Omega(x) : h e h^-1 = e} has order 6 and equals <e^3>; the class of e has 174,182,400 / 6 = 29,030,400 elements = 1/6 of the coset",
      len(Ce) == 6 and set(h.tobytes() for h in Ce) == set(h.tobytes() for h in pw), "|C_Omega(e)| = %d" % len(Ce))

banner("AI3 -- one class: 300 sampled order-18 twisted elements, each tested exactly")
random.seed(20260905)
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)
CXlist = CX; CXinv = [ainv(h) for h in CX]
got = 0; conj_n = 0; fibre_fail = 0; tries = 0; types = Counter()
while got < 300 and tries < 300000:
    tries += 1
    g = pool[random.randrange(80)]
    for _ in range(3): g = pmul(pool[random.randrange(80)], g)
    ep = pmul(PHI, g); ct = cycle_type(ep)
    if order_ct(ct) != 18: continue
    got += 1; types[ct] += 1
    ea = A(ep); xp = A(ppow(ep, 6)); k = xp.tobytes()
    if k not in TX: fibre_fail += 1; continue
    u = TX[k]; epp = aconj(ainv(u), ea, u)            # u^-1 e' u  -> sixth power x
    assert np.array_equal(aconj(IDENT, x), x) and np.array_equal(amul(epp, amul(epp, amul(epp, amul(epp, amul(epp, epp))))), x)
    if any(np.array_equal(aconj(h, epp, hi), e) for h, hi in zip(CXlist, CXinv)): conj_n += 1
say("  %d order-18 twisted elements (%d tries), types %s; sixth powers in class(x): %d; conjugate to Phi.c-bar (exact): %d"
    % (got, tries, {str(dict(Counter(k))): v for k, v in types.items()}, got - fibre_fail, conj_n))
frac = got / tries
note("[obs] sampled order-18 density %.4f vs 1/6 = 0.1667; if a second class existed with density d, 300/300 in one class has probability (1 - 6d)^300: "
     "d = 0.01 -> %.2e" % (frac, (1 - 0.06) ** 300))
check("AI3a", "REGISTERED: all 300 sampled order-18 twisted elements are conjugate to Phi.c-bar (per element: sixth power in class(x), transported to the fibre over x, "
      "conjugated by C_Omega(x)) -- one class of density exactly 1/6 to the precision of the sample", got == 300 and conj_n == 300 and fibre_fail == 0)

banner("AI4 -- [obs] the order-24 twisted elements' centralizers, if their cubes' classes fit the cap")
reps24 = {}; tries = 0
while len(reps24) < 2 and tries < 100000:
    tries += 1
    g = pool[random.randrange(80)]
    for _ in range(3): g = pmul(pool[random.randrange(80)], g)
    ep = pmul(PHI, g); ct = cycle_type(ep)
    if order_ct(ct) == 24 and ct not in reps24: reps24[ct] = ep
for ct, ep in reps24.items():
    ea = A(ep); e3_ = A(ppow(ep, 3))
    T3 = conj_class_T(e3_, CAP)
    if T3 is None:
        note("[obs] type %s: the class of e^3 (order 8) exceeds the cap %d -- centralizer not computed" % (dict(Counter(ct)), CAP)); continue
    keys3 = list(T3); sg = []
    for _ in range(400):
        k = random.choice(keys3); yv = np.frombuffer(k, dtype=np.uint16); u = T3[k]
        j = random.randrange(26); g, gi = GA[j], GAi[j]
        gy = g[yv[gi]]; s_ = amul(ainv(T3[gy.tobytes()]), amul(g, u))
        if not np.array_equal(s_, IDENT): sg.append(s_)
    C3 = closure_np(sg, cap=200000)
    if C3 is None: note("[obs] type %s: centralizer closure over cap" % (dict(Counter(ct)),)); continue
    Ce24 = [h for h in C3 if np.array_equal(aconj(h, ea), ea)]
    note("[obs] type %s: |class(e^3)| = %d, |C_Omega(e^3)| = %d, |C_Omega(e)| = %d -> class of e has %d elements = %.4f of the coset (sampled ~0.125 each)"
         % (dict(Counter(ct)), len(T3), len(C3), len(Ce24), 174182400 // len(Ce24), 1.0 / len(Ce24)))

json.dump({"brief_sha": sha_ai, "class_x": len(TX), "cent_x": len(CX), "cent_x_orders": {str(k): v for k, v in ordc.items()}, "centre": len(centre),
           "cent_e": len(Ce), "sample18": {"n": got, "conjugate": conj_n}}, open(os.path.join(CACHE_AI, "witnesses_ai.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
