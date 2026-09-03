# -*- coding: utf-8 -*-
r"""verify_stone_aa_roofclock.py -- STONE AA: THE ROOF CLOCK, FIRST MEASUREMENT

Brief: BRIEF_STONE_AA_ROOFCLOCK.md (lock BRIEF_STONE_AA_LOCK.sha256,
re-verified as check AA0:
0759ad94bdd8d1ed80d4f73d9b55b21a45793221c88b2d813c6fe68bc6954194).

Question: the two-register model's empty cell -- the roof's dynamics.  The
turn tau'' (SM-038: exact order 3, fixed set G2(2)) is realized as a
permutation Phi of the 360 = 3 x 120 nonsingular points of the three
8-dimensional modules V, S+, S- on which the roof acts, so that <Omega,
Phi> = O8+(2):3 is an explicit permutation group; then the first
measurements a clock would have to satisfy.

ROUTE (declared; bars AA1-AA6):
  AA1  rho- and Q- (odd half-spin; unique plus-type form); the three
       120-orbits; BSGS of P(Omega) on 360 points.
  AA2  Phi: T''^-1 on V, the exact intertwiner L (rho+ -> rho- o tau''^2)
       on S+, T'' L^-1 on S-; Phi^3 = id; Phi P(g) Phi^-1 = P(tau''^2 g)
       on all generators; |<P(Omega), Phi>| = 3 |Omega|.
  AA3  the three block point-stabilizers are the three shadows.
  AA4  G2(2) commutes with Phi and is the pointwise stabilizer of one
       Phi-orbit {v, Phi v, Phi^2 v}.
  AA5  the twisted coset Omega.Phi sampled: order distribution, maximal
       order + cycle types; Phi.g7 (order 21, registered) and Phi.c-bar
       (Coxeter image) recorded.
  AA6  the bridge PSL(2,7) of the still point on v-perp: Brauer character
       (7,1,0) (= chi7 mod 2 = 1+chi6 mod 2, honestly) and the Lagrangian
       split of v-perp/<v> into two invariant totally isotropic 3-spaces.

MACHINERY: Stone X replay and the BSGS/sift code are VERBATIM from
verify_stone_z_stillpoint.py (SM-038), which took them verbatim from
Stone X / Schur-pin / lift-law; y (the normalizing intertwiner) and G are
RECOMPUTED here from the sealed caches (7 s) and cross-checked against
_stone_z_cache/.  Sealed caches READ-ONLY; own cache _stone_aa_cache/.
No registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_aa_roofclock.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_aa_roofclock.log", "w", encoding="utf-8")
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
CACHE_Z = "_stone_z_cache"; CACHE_AA = "_stone_aa_cache"
os.makedirs(CACHE_AA, exist_ok=True)
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
check("AA0", "the brief is sha-locked: sha256(%s) equals the value in "
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
check("AA0a", "REPLAY cross-check: tau on the 26 generators and T+ "
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
check("AA0b", "SM-038 replayed: |G| = 12096 (exhaustive sift%s); y unique "
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
check("AA1a", "Q- (the rho-(Omega)-invariant quadratic form on S-) is "
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
check("AA1b", "P(Omega) on the 360 points: the three blocks are three orbits "
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
check("AA2a", "T'' = y^-1 s1-bar T+ intertwines: tau''(g) = T'' rho+(g) "
      "T''^-1 on all 26 generators; the intertwiner L: S+ -> S- with "
      "L rho+(g) = rho-(tau''^2 g) L exists and is UNIQUE (space dim %d, "
      "%d invertible solution)" % (len(NL), len(Ls)),
      tpp_ok and len(NL) == 1 and len(Ls) == 1)
Lm = Ls[0]; Li = f2_matinv(Lm)
L_iso = all(QM[mvec(Lm, x)] == QP[x] for x in range(256))
check("AA2b", "L carries Q+ to Q- on all 256 spinors (an isometry "
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
check("AA2c", "REGISTERED EXPECTATION CONFIRMED: Phi is a permutation of the "
      "360 points of EXACT order 3 (V -> S+ -> S- -> V) and "
      "Phi P(g) Phi^-1 = P(tau''^2(g)) for ALL 26 generators exactly -- "
      "the turn acts on states with footprint tau''^2 = tau''^-1",
      phi3 and conj_ok)
oOP, memOP, trOP, baseOP = make_bsgs_full(PG + [PHI], 360)
check("AA2d", "Phi is not in P(Omega) (membership strip) and |<P(Omega), "
      "Phi>| = 522,547,200 = 3 |O8+(2)|: O8+(2):3 as an explicit "
      "permutation group on 360 points", (not memO(PHI))
      and oOP == 3 * 174182400, "order %d" % oOP)
np.save(os.path.join(CACHE_AA, "phi360.npy"), np.array(PHI, dtype=np.uint16))
tick("stage 2 done")

# ======================================================================
banner("STAGE 3 -- AA3: the three block point-stabilizers are the three shadows")
# ======================================================================
v0 = V_IDX[ALPHA]; v1 = PHI[v0]; v2 = PHI[v1]
PC = [P360(M) for M in Cmats]
oPC, memPC, _, _ = make_bsgs_full(PC, 360)
stab_v0 = all(p[v0] == v0 for p in PC)
T2C = [tau_pp(tau_pp(M)) for M in Cmats]      # Phi C Phi^-1 = P(tau''^2 C)
T1C = [tau_pp(M) for M in Cmats]
stab_v1 = all(P360(M)[v1] == v1 for M in T2C)
stab_v2 = all(P360(M)[v2] == v2 for M in T1C)
check("AA3a", "Stab(v) in P(Omega) is C-bar: C-bar fixes v, has order "
      "1,451,520 = |Omega|/120 (orbit-stabilizer on the V-block); "
      "tau''^2(C-bar) fixes Phi(v) and tau''(C-bar) fixes Phi^2(v) -- the "
      "point stabilizers of the three blocks are the three shadows, and "
      "Phi cycles them (block by block, as the identity of AA2c predicts)",
      stab_v0 and oPC == 1451520 and stab_v1 and stab_v2)
tick("stage 3 done")

# ======================================================================
banner("STAGE 4 -- AA4: THE STILL POINT IN THE STATE SPACE")
# ======================================================================
PGm = [P360(M) for M in Gmats]
commutes = all(pmul(PHI, p) == pmul(p, PHI) for p in PGm)
fixes3 = all(p[v0] == v0 and p[v1] == v1 and p[v2] == v2 for p in PGm)
orb_v1_C = len(orbit_of(v1, PC))
check("AA4a", "REGISTERED EXPECTATION CONFIRMED: G2(2) COMMUTES with Phi on "
      "all 360 points (generators; hence the whole group) and fixes v, "
      "Phi(v), Phi^2(v); C-bar is transitive on the S+-block (orbit of "
      "Phi(v) has size %d), so |Stab_C-bar(Phi v)| = 12096 = |G| and "
      "G = the pointwise stabilizer in Omega of the Phi-orbit "
      "{v, Phi v, Phi^2 v}: a vector, a spinor, a co-spinor, one of each"
      % orb_v1_C, commutes and fixes3 and orb_v1_C == 120)
tick("stage 4 done")

# ======================================================================
banner("STAGE 5 -- AA5: the twisted coset Omega.Phi -- orders and cycle types")
# ======================================================================
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
pool = []
for _ in range(80):
    w = pident(360)
    for _ in range(random.randrange(6, 16)):
        w = pmul(PG[random.randrange(26)], w)
    pool.append(w)
NS5 = 30000
hist = Counter(); maxo = 0; max_cts = Counter()
t1 = time.time()
for _ in range(NS5):
    g = pool[random.randrange(80)]
    for _ in range(3): g = pmul(pool[random.randrange(80)], g)
    e = pmul(PHI, g)
    ct = cycle_type(e); o = order_ct(ct)
    hist[o] += 1
    if o > maxo: maxo = o; max_cts = Counter()
    if o == maxo: max_cts[ct] += 1
tick("%d twisted elements sampled (%.1fs)" % (NS5, time.time() - t1))
say("  element orders in the coset Omega.Phi (sample of %d):" % NS5)
for o in sorted(hist): say("    order %3d : %6d  (%.2f%%)" % (o, hist[o], 100.0 * hist[o] / NS5))
say("  maximal order found: %d; its cycle types on the 360 points:" % maxo)
for ct, n in max_cts.most_common(4):
    say("    %s  x%d" % (dict(Counter(ct)), n))
check("AA5a", "MEASUREMENT (tagged [obs]): the twisted coset's element "
      "orders are all multiples of 3 (%s) and the maximal order found "
      "among %d samples is %d, cycle types above -- the roof's number "
      "against 18 at E7 and 6 at D4" % (sorted(hist), NS5, maxo),
      all(o % 3 == 0 for o in hist) and maxo > 3)
g7p = next(g for g in G_list if pord(g) == 7)
g7m = mat_of_perm(g7p); P7 = P360(g7m)
e21 = pmul(PHI, P7); ct21 = cycle_type(e21)
check("AA5b", "REGISTERED EXPECTATION CONFIRMED: Phi . g7 (g7 in G2(2) of "
      "order 7, commuting with Phi) has order 21 -- the seven-beat clock "
      "composed with the turn; cycle type on 360: %s"
      % dict(Counter(ct21)), order_ct(ct21) == 21
      and pmul(PHI, P7) == pmul(P7, PHI))
c240 = pident(240)
for s in S240: c240 = pmul(c240, s)
cbar = M2_of(c240)
oc = pord(perm_of(cbar))
Pc = P360(cbar); ec = pmul(PHI, Pc); ctc = cycle_type(ec)
oc_tw = order_ct(ctc)
check("AA5c", "MEASUREMENT: the standard Coxeter element of W(E8) (product "
      "of the 8 simple reflections) has image c-bar of order %d in Omega "
      "(= h(E8)/2 = 15 expected); Phi . c-bar has order %d with cycle "
      "type %s -- recorded against h(E8) = 30" % (oc, oc_tw, dict(Counter(ctc))),
      oc == 15)
json.dump({"orders_hist": {str(k): v for k, v in hist.items()},
           "max_order": maxo, "max_cycle_types": [[list(k), v] for k, v in max_cts.items()],
           "phi_g7_ct": list(ct21), "phi_cox_order": oc_tw, "phi_cox_ct": list(ctc)},
          open(os.path.join(CACHE_AA, "coset_sample.json"), "w"))
tick("stage 5 done")

# ======================================================================
banner("STAGE 6 -- AA6: the bridge seven at the still point, on v-perp")
# ======================================================================
invs = [g for g in G_list if pord(g) == 2]
thr = [g for g in G_list if pord(g) == 3]
pair = None
for a in invs:
    for b in thr:
        ab = pmul(a, b)
        if pord(ab) == 7 and pord(comm(a, b)) == 4 \
           and len(closure([a, b], cap=200)) == 168:
            pair = (a, b); break
    if pair: break
a, b = pair
Am, Bm = mat_of_perm(a), mat_of_perm(b); ABm = mmul(Am, Bm)
frow = sum(Bform(1 << j, ALPHA) << j for j in range(8))
VPERP = f2_nullspace([frow], 8)              # 7 basis masks of v-perp
assert len(VPERP) == 7 and ALPHA in {x for x in range(256) if Bform(x, ALPHA) == 0}
def coords7(x):
    for bits in range(128):
        y = 0
        for k in range(7):
            if (bits >> k) & 1: y ^= VPERP[k]
        if y == x: return bits
    raise ValueError("not in v-perp")
def mat7(M):
    return tuple(coords7(mvec(M, e)) for e in VPERP)
def mat7_mul(A, B): return tuple(mvec(A, c) for c in B)
def mat7_add(A, B): return tuple(x ^ y for x, y in zip(A, B))
I7 = tuple(1 << i for i in range(7))
def mat7_kernel(A):
    rows = []
    for i in range(7):
        r = 0
        for j in range(7):
            if (A[j] >> i) & 1: r |= 1 << j
        rows.append(r)
    return f2_nullspace(rows, 7)
def to_mask(c):
    y = 0
    for k in range(7):
        if (c >> k) & 1: y ^= VPERP[k]
    return y
A7, B7, G7 = mat7(Am), mat7(Bm), mat7(ABm)
assert mat7_mul(A7, A7) == I7
m1_3 = len(mat7_kernel(mat7_add(B7, I7)))
m1_7 = len(mat7_kernel(mat7_add(G7, I7)))
G7_2 = mat7_mul(G7, G7); G7_3 = mat7_mul(G7_2, G7)
K1 = mat7_kernel(mat7_add(mat7_add(G7_3, G7), I7))          # x^3+x+1
K2 = mat7_kernel(mat7_add(mat7_add(G7_3, G7_2), I7))        # x^3+x^2+1
br3 = m1_3 - (7 - m1_3) // 2
br7 = m1_7 - len(K1) // 3            # a = b = dim/3, b7 + b7bar = -1
check("AA6a", "Brauer character of the bridge PSL(2,7) on v-perp (7-dim): "
      "(7, %d, %d) at element orders (1, 3, 7) -- = chi7 mod 2 = 1 + 3 + "
      "3-bar; stated honestly: 1 + chi6 (the Fano seven) has the SAME "
      "2-modular character, so the character cannot separate the sevens "
      "(kernel dims: 1-eigenspaces %d / %d; cubic kernels %d / %d)"
      % (br3, br7, m1_3, m1_7, len(K1), len(K2)),
      br3 == 1 and br7 == 0 and len(K1) == 3 and len(K2) == 3)
def span7(basis):
    S = set()
    for bits in range(2 ** len(basis)):
        y = 0
        for k in range(len(basis)):
            if (bits >> k) & 1: y ^= basis[k]
        S.add(y)
    return S
vc = coords7(ALPHA)
U1 = span7(K1); U2 = span7(K2)
U1v = span7(K1 + [vc]); U2v = span7(K2 + [vc])
inv1 = all(mvec(A7, x) in U1v for x in U1) and all(mvec(B7, x) in U1v for x in U1)
inv2 = all(mvec(A7, x) in U2v for x in U2) and all(mvec(B7, x) in U2v for x in U2)
iso1 = all(Bform(to_mask(x), to_mask(y)) == 0 for x in U1 for y in U1)
iso2 = all(Bform(to_mask(x), to_mask(y)) == 0 for x in U2 for y in U2)
sum_ok = len(span7(K1 + K2 + [vc])) == 128
check("AA6b", "REGISTERED EXPECTATION CONFIRMED -- THE LAGRANGIAN SPLIT: "
      "modulo v, the two cubic kernels U, U' (3-dim each) are both "
      "PSL(2,7)-invariant, both totally isotropic for B, and v-perp = "
      "U + U' + <v>: the still point's seven acts on the 6-dim symplectic "
      "quotient as diag(M, M^-T) on a Lagrangian pair -- SM-028's "
      "Lagrangian embedding recovered at the still point",
      inv1 and inv2 and iso1 and iso2 and sum_ok)
tick("stage 6 done")

banner("VERDICT")
say("""  The turn now acts on states: Phi, order three on 360 points, cycling
  vectors -> spinors -> co-spinors with footprint tau''^-1, and
  <Omega, Phi> = O8+(2):3 explicit.  The three shadows are the three
  block stabilizers; the still point is the joint stabilizer of one
  Phi-orbit.  The twisted coset's orders are measured above (tagged
  [obs]); the seven-beat clock composed with the turn has order 21.  The
  bridge seven on v-perp is chi7 mod 2 and splits Lagrangian.""")
say("")
say("RESULT: %d checks passed, %d failed%s" % (PASS, FAIL,
    ("  FAILED: %s" % FAILED) if FAILED else ""))
tick("done")
LOG.close()
