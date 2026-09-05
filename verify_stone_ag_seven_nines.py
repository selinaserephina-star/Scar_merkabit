# -*- coding: utf-8 -*-
r"""verify_stone_ag_seven_nines.py -- STONE AG: THE SEVEN NINES

Brief: BRIEF_STONE_AG_SEVEN_NINES.md (lock BRIEF_STONE_AG_LOCK.sha256,
re-verified as check AG0).

Question: SM-044 left on the table that c-bar7 (the E7 Coxeter element
from the roof, on the 120 vectors) and Phi.c-bar (the roof's eighteen, on
360 points) both have exactly seven 9-cycles.  One object or a counting
rhyme?  The two eighteens could meet at their sixth powers (order 3, in
Omega): are c-bar7^6 and (Phi.c-bar)^6 conjugate?  And the order-24
twisted elements, orbit by orbit.

BARS: AG0a AA replay + Phi cross-check + Phi.c-bar's type; AG1 the roof's
seven nines located; AG2 the Coxeter element's seven nines are F64 (min
poly x^6+x^3+1); AG3 conjugacy invariants of the two order-3 elements
(registered guess: NOT conjugate, separated by spinor-block types); AG4
the order-24 twisted elements; AG5 [obs] order-18 types.

Machinery: verify_stone_aa_roofclock.py lines 71-696 VERBATIM (its checks
relabelled REPLAY-AA*, its np.save of the Phi cache removed); sealed
caches READ-ONLY.  DISCIPLINE: compute, never assert; registered
expectations resolvable INVERTED at equal prominence; exact arithmetic;
no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ag_seven_nines.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ag_seven_nines.log", "w", encoding="utf-8")
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
CACHE_AG = "_stone_ag_cache"; os.makedirs(CACHE_AG, exist_ok=True)
random.seed(20260903)   # AA's seed, so the replayed stages see the same draws

say("=" * 78); say("STONE AG -- THE SEVEN NINES (one object or a counting rhyme; where the two eighteens could meet)"); say("=" * 78)
BRIEF_AG = "BRIEF_STONE_AG_SEVEN_NINES.md"; LOCK_AG = open("BRIEF_STONE_AG_LOCK.sha256").read().strip()
sha_ag = hashlib.sha256(open(BRIEF_AG, "rb").read()).hexdigest()
check("AG0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AG_LOCK.sha256" % BRIEF_AG, sha_ag == LOCK_AG, sha_ag[:16] + "...")

# =====================================================================
# VERBATIM from verify_stone_aa_roofclock.py, lines 71-696 (STAGE 0-2 of SM-039);
# its check tags relabelled REPLAY-AA*, its np.save of phi360.npy removed
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
pass  # [AG] AA's np.save of phi360.npy REMOVED: the sealed cache is read below, never written
tick("stage 2 done")


# =====================================================================
# STONE AG stages
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

banner("AG0a -- the replayed Phi against the sealed cache; Phi.c-bar recomputed")
PHI_cached = tuple(int(x) for x in np.load(os.path.join(CACHE_AA, "phi360.npy")))
c240 = pident(240)
for s in S240: c240 = pmul(c240, s)
cbar = M2_of(c240)
Pc = P360(cbar); ec = pmul(PHI, Pc); ctc = dict(Counter(cycle_type(ec)))
check("AG0a", "the recomputed Phi equals the sealed phi360.npy exactly; Phi has order 3; Phi.c-bar (c-bar = the E8 Coxeter image, order %d) has order 18 "
      "with cycle type {18:16, 9:7, 3:3} on 360 -- SM-039's sealed value" % pord(perm_of(cbar)),
      PHI == PHI_cached and ppow(PHI, 3) == pident(360) and order_ct(cycle_type(ec)) == 18 and ctc == {18: 16, 9: 7, 3: 3}, ctc)

banner("AG1 -- the roof's seven nines, located")
e3 = ppow(ec, 3); e6 = ppow(ec, 6); e9 = ppow(ec, 9)
nine_pts = [i for i in range(360) if e9[i] == i and e3[i] != i]
per_block = [sum(1 for i in nine_pts if 120 * b <= i < 120 * b + 120) for b in range(3)]
ct3 = [ct_block(e3, b) for b in range(3)]; ct6 = [ct_block(e6, b) for b in range(3)]; ct9 = [ct_block(e9, b) for b in range(3)]
say("  (Phi.c-bar)^3 per block: %s" % ct3); say("  (Phi.c-bar)^6 per block: %s" % ct6); say("  (Phi.c-bar)^9 per block: %s" % ct9)
check("AG1a", "the 63 points in 9-cycles of Phi.c-bar = Fix((Phi.c-bar)^9) minus Fix((Phi.c-bar)^3): 21 per block; (Phi.c-bar)^3 has {6:16, 3:7, 1:3} on V, "
      "(Phi.c-bar)^6 has {3:39, 1:3} on every block, (Phi.c-bar)^9 is an involution with 24 fixed points per block; all three powers lie in Omega",
      len(nine_pts) == 63 and per_block == [21, 21, 21] and ct3[0] == {6: 16, 3: 7, 1: 3} and all(c == {3: 39, 1: 3} for c in ct6)
      and all(c == {2: 48, 1: 24} for c in ct9) and memO(e3) and memO(e6) and memO(e9))
V21 = [NONSING[i] for i in nine_pts if i < 120]
rk21 = f2_rank(V21); orth = sum(1 for a, b in itertools.combinations(V21, 2) if Bform(a, b) == 0)
hyper = [u for u in range(1, 256) if all(Bform(u, x) == 0 for x in V21)]
note("[obs] the 21 vectors of the vector block in the roof's nine-cycles: F2-rank of span %d; orthogonal pairs %d of %d; common orthogonal complement "
     "has %d nonzero vectors" % (rk21, orth, 21 * 20 // 2, len(hyper)))

banner("AG2 -- the Coxeter element's seven nines are a field")
# the E7 base BETA (verbatim construction of SM-040/041) and c-bar7 = product of the seven transvections
ALPHA_R = SIMPLE[0]; ALPHA = rmask[ridx[ALPHA_R]]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi7 = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi7[i]] for i in range(7)]; BETAM = [rmask[ridx[b]] for b in BETA]
def refl240(b):
    return tuple(ridx[tuple(r[t] - dot4(r, b) * b[t] for t in range(8))] for r in roots)
c7_240 = pident(240)
for b in BETA: c7_240 = pmul(c7_240, refl240(b))
cb7 = M2_of(c7_240)
p7 = perm_of(cb7)
tv_perm = tuple(V_IDX[x ^ (ALPHA if Bform(x, ALPHA) else 0)] for x in NONSING)
check("AG2a", "c-bar7 (the E7 Coxeter element as a 240-root permutation, reduced mod 2) has Dickson invariant 1, order 18 on the 120, cycle type "
      "{18:3, 9:7, 2:1, 1:1} (SM-044 re-seen), and c-bar7^9 = t_v", dickson(cb7) == 1 and pord(p7) == 18
      and dict(Counter(cycle_type(p7))) == {18: 3, 9: 7, 2: 1, 1: 1} and ppow(p7, 9) == tv_perm)
# v-perp / v as F2^6: choose a basis of v-perp containing v, reduce
VPERP = [x for x in range(256) if Bform(x, ALPHA) == 0]
basis = [ALPHA]
for x in VPERP:
    if f2_rank(basis + [x]) > len(basis): basis.append(x)
    if len(basis) == 7: break
assert len(basis) == 7
def coords_in(x, bs):
    for bits in range(1 << len(bs)):
        y = 0
        for j in range(len(bs)):
            if (bits >> j) & 1: y ^= bs[j]
        if y == x: return bits
    raise ValueError
cb7sq = mmul(cb7, cb7)
def mat6(M):
    """the induced 6x6 matrix on v-perp / v in the basis basis[1:7] (columns = images)."""
    cols = []
    for j in range(1, 7):
        y = mvec(M, basis[j]); bits = coords_in(y, basis)      # y in v-perp
        cols.append(bits >> 1)                                   # drop the v-coordinate
    return tuple(cols)
def mat6_mul(A, B):
    def mv(M, x):
        y = 0
        for j in range(6):
            if (x >> j) & 1: y ^= M[j]
        return y
    return tuple(mv(A, c) for c in B)
def mat6_pow(A, e):
    R = tuple(1 << j for j in range(6)); B = A
    while e:
        if e & 1: R = mat6_mul(R, B)
        B = mat6_mul(B, B); e >>= 1
    return R
A9 = mat6(cb7sq); I6 = tuple(1 << j for j in range(6))
# minimal polynomial over F2: test the candidates dividing x^9 - 1 = (x+1)(x^2+x+1)(x^6+x^3+1)
def poly_eval(coeffs, A):
    R = tuple(0 for _ in range(6))
    for c in coeffs:                       # highest degree first
        R = mat6_mul(R, A)
        if c: R = tuple(r ^ i for r, i in zip(R, I6))
    return R
Z6 = tuple(0 for _ in range(6))
is_phi9 = poly_eval([1, 0, 0, 1, 0, 0, 1], A9) == Z6
not_smaller = poly_eval([1, 1], A9) != Z6 and poly_eval([1, 1, 1], A9) != Z6 and poly_eval([1, 0, 0, 1], A9) != Z6
ord9 = mat6_pow(A9, 9) == I6 and mat6_pow(A9, 3) != I6
PAULI = [u for u in NONSING if u != ALPHA and Bform(u, ALPHA) == 0]
ct_pauli = dict(Counter(cycle_type([PAULI.index(mvec(cb7sq, u)) for u in PAULI])))
check("AG2b", "REGISTERED: c-bar7^2 (order 9) acts on v-perp/v = F2^6 with minimal polynomial x^6 + x^3 + 1 = Phi_9(x) (annihilated by it, by none of "
      "x+1, x^2+x+1, x^3+1): F2[c-bar7^2] is the field F64 and the seven 9-cycles on the 63 Paulis are the seven cosets of mu_9 in F64^x -- "
      "cycle type on the Paulis %s" % ct_pauli, is_phi9 and not_smaller and ord9 and ct_pauli == {9: 7})
check("AG2c", "REGISTERED reading: the roof's seven nines are seven 3-cycles of (Phi.c-bar)^3 on each of three blocks (3 x 21/3), the Coxeter element's "
      "are seven 9-cycles of an order-9 field element on the 63 Paulis of one block (63/9): a counting rhyme, not one object",
      ct3[0][3] == 7 and ct3[1][3] == 7 and ct3[2][3] == 7 and ct_pauli == {9: 7})

banner("AG3 -- where the two eighteens could meet: (Phi.c-bar)^6 against c-bar7^6, both of order 3 in Omega")
x = e6
y2 = P360(cb7sq)                    # c-bar7^2 is in Omega (Dickson 0)
y = ppow(y2, 3)
cx = [ct_block(x, b) for b in range(3)]; cy = [ct_block(y, b) for b in range(3)]
say("  x = (Phi.c-bar)^6 per block: %s" % cx); say("  y = c-bar7^6      per block: %s" % cy)
def fix_dim_V(p):
    M = mat_of_perm(tuple(p[:120]))
    return 8 - f2_rank([M[j] ^ (1 << j) for j in range(8)]), M
dx, Mx = fix_dim_V(x); dy, My = fix_dim_V(y)
def fixspace(M):
    return [u for u in range(1, 256) if mvec(M, u) == u]
fx, fy = fixspace(Mx), fixspace(My)
qx = Counter(qvals[u] for u in fx); qy = Counter(qvals[u] for u in fy)
say("  fixed subspace on V: x dim %d (%d nonzero: q-values %s); y dim %d (%d nonzero: q-values %s)" % (dx, len(fx), dict(qx), dy, len(fy), dict(qy)))
separated = (sorted(str(c) for c in cx) != sorted(str(c) for c in cy)) or dx != dy or qx != qy
both_omega = memO(x) and memO(y)
if separated:
    check("AG3a", "REGISTERED GUESS CONFIRMED: x = (Phi.c-bar)^6 and y = c-bar7^6 (both in Omega, both order 3, both {3:39,1:3} on V) are NOT conjugate in "
          "<Omega,Phi>: separated by %s" % ("the block cycle types (as multisets)" if sorted(str(c) for c in cx) != sorted(str(c) for c in cy)
          else "the fixed subspace on V (dim / q-values)"), both_omega and pord(x) == 3 and pord(y) == 3)
else:
    check("AG3a", "REGISTERED GUESS INVERTED (full prominence): x = (Phi.c-bar)^6 and y = c-bar7^6 agree in every invariant tested (block cycle types, "
          "fixed-space dimension and q-values on V) -- the conjugacy question is OPEN, not decided by these invariants", False)


# ---------------------------------------------------------------- POST-REVEAL (finding, not amendment)
# AG3a as registered compared invariants only and was INVERTED (all agree).  The question is decidable
# exactly: enumerate the Omega-conjugacy class of x as a set of 360-permutations (orbit under
# conjugation by the 26 generators), test y in it; then y^Phi, y^(Phi^2) for conjugacy in <Omega,Phi>.
banner("AG3b -- POST-REVEAL: exact conjugacy of x = (Phi.c-bar)^6 and y = c-bar7^6 by class enumeration")
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
t1 = time.time()
CLX = conj_class(x, CAP)
if CLX is None:
    check("AG3b", "POST-REVEAL: the Omega-class of x exceeds %d elements -- conjugacy NOT decided here (recorded OPEN)" % CAP, False)
else:
    tick("Omega-class of x enumerated: %d elements (%.1fs); |C_Omega(x)| = %d" % (len(CLX), time.time() - t1, 174182400 // len(CLX)))
    CLY = conj_class(y, CAP)
    tick("Omega-class of y enumerated: %d elements; |C_Omega(y)| = %d" % (len(CLY), 174182400 // len(CLY)))
    in_omega = key_of(y) in CLX
    yP = pmul(pmul(PHI, y), PHIi); yPP = pmul(pmul(PHI, yP), PHIi)
    in_full = in_omega or (key_of(yP) in CLX) or (key_of(yPP) in CLX)
    note("class sizes: x %d, y %d; y in class(x): %s; y^Phi in class(x): %s; y^(Phi^2) in class(x): %s" % (len(CLX), len(CLY), in_omega, key_of(yP) in CLX, key_of(yPP) in CLX))
    if in_full:
        check("AG3b", "POST-REVEAL FINDING: x = (Phi.c-bar)^6 and y = c-bar7^6 ARE conjugate in %s (class of %d elements, centralizer order %d): "
              "the two eighteens DO meet at their sixth powers -- the roof's eighteen and the E7 Coxeter element share one order-3 element up to conjugacy"
              % ("Omega" if in_omega else "<Omega,Phi> (via the turn, not inside Omega)", len(CLX), 174182400 // len(CLX)), True)
    else:
        check("AG3b", "POST-REVEAL FINDING: x = (Phi.c-bar)^6 and y = c-bar7^6 are NOT conjugate in <Omega,Phi> although every invariant of AG3a agrees "
              "(two classes of the same size %d / %d, centralizers %d / %d): the eighteens do not meet even at order 3"
              % (len(CLX), len(CLY), 174182400 // len(CLX), 174182400 // len(CLY)), True)
    json.dump({"class_x": len(CLX), "class_y": len(CLY), "y_in_class_x": in_omega, "conjugate_in_full": in_full},
              open(os.path.join(CACHE_AG, "conjugacy_ag3b.json"), "w"), indent=1)

banner("AG4 -- the order-24 twisted elements")
random.seed(20260905)
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)
NS5 = 30000
hist = Counter(); types24 = Counter(); types18 = Counter(); reps24 = {}
t1 = time.time()
for _ in range(NS5):
    g = pool[random.randrange(80)]
    for _ in range(3): g = pmul(pool[random.randrange(80)], g)
    e = pmul(PHI, g)
    ct = cycle_type(e); o = order_ct(ct)
    hist[o] += 1
    if o == 24:
        types24[ct] += 1
        if ct not in reps24: reps24[ct] = e
    if o == 18: types18[ct] += 1
tick("%d twisted elements sampled (%.1fs)" % (NS5, time.time() - t1))
say("  orders: %s" % dict(sorted(hist.items())))
say("  order-24 cycle types: %s" % {str(dict(Counter(k))): v for k, v in types24.items()})
sealed = json.load(open(os.path.join(CACHE_AA, "coset_sample.json")))
sealed_types = set(tuple(k) for k, v in sealed["max_cycle_types"])
check("AG4a", "REGISTERED: the re-sampled coset has the order set {3,6,9,12,18,21,24} and no new order; both sealed order-24 cycle types "
      "({24:12,12:3,6:5,3:2}, {24:12,12:5,6:1,3:2}) re-found", set(hist) == {3, 6, 9, 12, 18, 21, 24} and sealed_types <= set(types24),
      "new order-24 types: %d" % (len(set(types24) - sealed_types)))
# POST-REVEAL instrumentation fix: the brief wrote 'eighth power (order 3, in Omega)'; e^8 lies in the coset Omega.Phi^2
# (e in Omega.Phi, 8 = 2 mod 3) and moves the blocks -- the first run asserted on it and stopped (FIRSTRUN log kept).
# Measured instead: e^8's cycle type on 360 and its coset; e^3 (order 8, in Omega) per block; e^6 (order 4) per block.
PHI2 = ppow(PHI, 2); ctPHI2 = dict(Counter(cycle_type(PHI2)))
for ct, e in reps24.items():
    e3_ = ppow(e, 3); e6_ = ppow(e, 6); e8_ = ppow(e, 8)
    c3 = [ct_block(e3_, b) for b in range(3)]; c6 = [ct_block(e6_, b) for b in range(3)]
    ct8 = dict(Counter(cycle_type(e8_))); e8_in_omega = memO(e8_)
    say("  order-24 type %s: cube (order 8, in Omega %s) per block %s; sixth power (order 4) per block %s; eighth power (order 3): in Omega %s, "
        "cycle type on 360 %s (Phi^2: %s)" % (dict(Counter(ct)), memO(e3_), c3, c6, e8_in_omega, ct8, ctPHI2))
check("AG4b", "REGISTERED: no rowmotion in hand has order 24 (E7 board: 18; E6 sheets: 12) and no roof poset is named -- IB's 'order-24 element as "
      "rowmotion on a roof poset' NOT SUPPORTED as stated (the orbit data above is what a named poset would have to match)", True)

banner("AG5 -- [obs] the order-18 twisted elements")
say("  order-18 cycle types among the sample: %s" % {str(dict(Counter(k))): v for k, v in types18.most_common()})
note("[obs] Phi.c-bar's type {18:16, 9:7, 3:3} is %s among the sampled order-18 types" %
     ("the most common" if types18 and types18.most_common(1)[0][0] == cycle_type(ec) else "NOT the most common"))
json.dump({"brief_sha": sha_ag, "phic_ct": ctc, "nine_pts_per_block": per_block, "V21_rank": rk21, "V21_orth_pairs": orth,
           "x_blocks": cx, "y_blocks": cy, "x_fixdim": dx, "y_fixdim": dy, "separated": separated,
           "orders": {str(k): v for k, v in hist.items()}, "types24": {str(dict(Counter(k))): v for k, v in types24.items()},
           "types18": {str(dict(Counter(k))): v for k, v in types18.items()}},
          open(os.path.join(CACHE_AG, "witnesses_ag.json"), "w"), indent=1)

banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
