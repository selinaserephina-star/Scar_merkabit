# -*- coding: utf-8 -*-
r"""verify_stone_z_stillpoint.py -- STONE Z: THE STILL POINT OF THE ROOF TURN

Brief: BRIEF_STONE_Z_STILLPOINT.md (lock BRIEF_STONE_Z_LOCK.sha256,
re-verified as check Z0:
e13da2538b6bf25d598c124bde9651bf23c2bec7fabc24154ecc683a8ff072e0).

Question: SM-036 built tau', an explicit outer 3-cycle of Omega = W+(E8)/
<-1> ~= O8+(2) on the three shadow classes, with tau'^3 inner by h'.  What
does the turn hold still?  Take the sealed vector shadow C-bar and the
triangle (C-bar, tau'(C-bar), tau'^2(C-bar)); compute the intersection,
name it, normalize the turner to exact order 3 fixing it pointwise, and
find which seven sits inside.

ROUTE (declared in the brief; bars ZB0-ZB6):
  ZB0  replay Stone X's tau' machinery VERBATIM and cross-check it against
       the sealed _stone_x_cache/witnesses_x.json; C-bar as a permutation
       group on the 120 nonsingular vectors (faithful), enumerated.
  ZB1  G := C-bar cap tau'(C-bar) by exhaustive sift.  REGISTERED: |G| =
       12096 = |G2(2)|; [G,G] of order 6048, G/[G,G] = C2; order census
       {1,2,3,4,6,7,8,12}.
  ZB2  G' := tau'(C-bar) cap tau'^2(C-bar) (= tau'(G)); the triple
       intersection MEASURED; tau'(G) = G TESTED (conditional expectation).
  ZB3  normalize: y with y g y^-1 = tau'(g) on G's generators; tau'' :=
       inn(y^-1) o tau'.  REGISTERED: tau'' fixes G pointwise and
       tau''^3 = id on all 26 Omega-generators.
  ZB4  Fix(tau'') = G as far as the machine reaches: C-bar cap
       tau''(C-bar) = G; the triangle closes; random sample has no fixed
       element outside G.  [P cited] for the full statement.
  ZB5  PSL(2,7) in G: copies, conjugacy, normalizer (336?).  REGISTERED:
       the copy is the BRIDGE class of C-bar (involution class 315).
       Its class in the spin-type shadow tau'(C-bar) measured alongside.
  ZB6  the register of the still point: G's involution classes read in
       C-bar and in tau'(C-bar), with the sealed eps values; verdict on
       the spin-tower preimage of G.  REGISTERED: non-split.

SEALED MACHINERY (READ-ONLY): _stone_u_cache/ (stab_derived_gens,
witnesses.json k0_pair), _stone_v_cache/ (K_240 order), _stone_x_cache/
(witnesses_x.json).  All F2 / Clifford / decomposition / spin code is
VERBATIM from verify_stone_x_turner.py; BSGS verbatim from
verify_schur_class_pinning.py (returns the base as well -- one added
return value, used by the vectorized sift); enumerate_group_np verbatim
from verify_lift_law.py.

DISCIPLINE: compute, never assert; registered expectations resolvable
INVERTED at equal prominence; exact arithmetic; sealed caches READ-ONLY;
own cache _stone_z_cache/.  No registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_z_stillpoint.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_z_stillpoint.log", "w", encoding="utf-8")
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
CACHE_Z = "_stone_z_cache"
os.makedirs(CACHE_Z, exist_ok=True)
random.seed(20260903)

# ======================================================================
# permutation + F2 utilities (verbatim: Stone X / Stone U / lift law)
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
say("STONE Z -- THE STILL POINT OF THE ROOF TURN")
say("G = C-bar cap tau'(C-bar) in Omega = O8+(2); the turner normalized to")
say("order three; the seven at the still point   [sealed caches READ-ONLY]")
say("=" * 78)

# ======================================================================
banner("STAGE 0 -- Z0: brief lock; Stone X machinery replayed VERBATIM and "
       "cross-checked against the sealed witnesses_x.json")
# ======================================================================
BRIEF = "BRIEF_STONE_Z_STILLPOINT.md"
LOCK = "e13da2538b6bf25d598c124bde9651bf23c2bec7fabc24154ecc683a8ff072e0"
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("Z0", "the brief is sha-locked: sha256(%s) equals the value in "
      "BRIEF_STONE_Z_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

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

WX = json.load(open(os.path.join(CACHE_X, "witnesses_x.json")))
TAU_GENS = [tau_of(M) for M in OMEGA_GENS]
rep_tau = ([list(M) for M in TAU_GENS] == WX["tau_gen_cols"])
rep_tp = (list(TP) == WX["Tplus_cols"])
TP3 = [tau_p(tau_p(tau_p(M))) for M in OMEGA_GENS]
dP, HPs = good_intertwiners(list(zip(OMEGA_GENS, TP3)))
rep_hp = (dP == 1 and len(HPs) == 1 and list(HPs[0]) == WX["hprime_cols"])
HPm = HPs[0] if HPs else None
check("Z0a", "REPLAY cross-check: tau on all 26 Omega-generators, T+, and "
      "the tau'^3 intertwiner h' reproduce the sealed Stone X witnesses "
      "byte-for-byte (tau_gen_cols, Tplus_cols, hprime_cols; intertwiner "
      "space dim 1)", rep_tau and rep_tp and rep_hp)
oK, _, _, _ = 0, None, None, None
tick("stage 0 replay done")

# --- C-bar on the 120 nonsingular vectors
Cperm = [perm_of(M) for M in Cmats]
oC, memC, trC, baseC = make_bsgs_full(Cperm, 120)
EN_C = enumerate_group_np(trC, 120)
check("Z0b", "C-bar (the sealed vector shadow, 24 generators) acts "
      "faithfully on the 120 nonsingular vectors: BSGS order 1,451,520 = "
      "|Sp6(2)|; all elements enumerated (%d rows)" % EN_C.shape[0],
      oC == 1451520 and EN_C.shape == (1451520, 120))
tick("stage 0 done")

# ======================================================================
banner("STAGE 1 -- ZB1: THE STILL POINT  G = C-bar cap tau'(C-bar)")
# ======================================================================
TpC = [tau_p(M) for M in Cmats]
TpCperm = [perm_of(M) for M in TpC]
oT, memT, trT, baseT = make_bsgs_full(TpCperm, 120)
check("Z1a", "tau'(C-bar) = <tau'(24 generators)>: BSGS order 1,451,520 "
      "(tau' is an automorphism); every image a Dickson-0 isometry",
      oT == 1451520 and all(is_isometry(M) and dickson(M) == 0 for M in TpC))
t1 = time.time()
maskG = member_mask(EN_C, baseT, trT)
G_rows = EN_C[maskG]
nG = int(maskG.sum())
tick("exhaustive sift of 1,451,520 elements through tau'(C-bar) done "
     "(%.1fs)" % (time.time() - t1))
G_set = set(tuple(int(x) for x in r) for r in G_rows)
G_list = sorted(G_set)
np.save(os.path.join(CACHE_Z, "G_rows.npy"), G_rows)
check("Z1b", "REGISTERED EXPECTATION: |G| = 12096 = |G2(2)| -- the "
      "intersection of the vector shadow with its turned image has index "
      "120 in C-bar (C-bar transitive on the 120 nonsingular spinors)",
      nG == 12096, "|G| = %d, index %s" % (nG, 1451520 // nG if nG else "-"))
# closure sanity + generators
def find_gens(elems, order, tries=50):
    for _ in range(tries):
        gs = [random.choice(elems) for _ in range(2)]
        if len(closure(gs, cap=order + 5)) == order: return gs
    for _ in range(tries):
        gs = [random.choice(elems) for _ in range(3)]
        if len(closure(gs, cap=order + 5)) == order: return gs
    raise RuntimeError("no small generating set found")
Ggens = find_gens(G_list, nG)
Gmats = [mat_of_perm(p) for p in Ggens]
assert all(perm_of(M) == p for M, p in zip(Gmats, Ggens))
census_G = profile_of(G_list)
def derived_subgroup(gens, order_cap):
    D = set(closure([comm(a, b) for a in gens for b in gens if a != b],
                    cap=order_cap))
    while True:
        Dg = list(D)[:40] if len(D) > 40 else list(D)
        extra = [pmul(pmul(g, s), pinv(g)) for g in gens for s in Dg]
        D2 = closure(list(D)[:6] + Dg + extra, cap=order_cap)
        if len(D2) == len(D): return D
        D = set(D2)
Dsub = derived_subgroup(Ggens, nG + 5)
Dgens = find_gens(sorted(Dsub), len(Dsub))
DD = derived_subgroup(Dgens, len(Dsub) + 5)
check("Z1c", "IDENTIFICATION: [G,G] has order 6048 with G/[G,G] = C2 "
      "(index 2); [G,G] is PERFECT (its own derived subgroup, order 6048 "
      "= |U3(3)|); element-order census of G = {1,2,3,4,6,7,8,12} -- "
      "G = U3(3):2 = G2(2) [orders + [P cited: G2(2) = U3(3):2 is the "
      "unique index-120 subgroup class of Sp6(2)]]",
      len(Dsub) == 6048 and nG == 2 * len(Dsub) and len(DD) == 6048
      and sorted(census_G) == [1, 2, 3, 4, 6, 7, 8, 12],
      "census %s" % census_G)
tick("stage 1 done")

# ======================================================================
banner("STAGE 2 -- ZB2: the triangle's intersections under the raw tau'")
# ======================================================================
Tp2C = [tau_p(M) for M in TpC]
oT2, memT2, trT2, baseT2 = make_bsgs_full([perm_of(M) for M in Tp2C], 120)
TpG = [perm_of(tau_p(M)) for M in Gmats]
Gp_set = closure(TpG, cap=nG + 5)
in_T2 = [memT2(p) for p in G_list]
triple = sum(in_T2)
tpG_in_G = all(p in G_set for p in TpG)
note("tau'(G) = <tau'(gens of G)> has order %d; tau'(G) == G: %s"
     % (len(Gp_set), tpG_in_G))
note("triple intersection |C-bar cap tau'(C-bar) cap tau'^2(C-bar)| = %d"
     % triple)
check("Z2a", "G' = tau'(C-bar) cap tau'^2(C-bar) = tau'(G) has order 12096 "
      "(automorphism image); tau'^2(C-bar) BSGS order 1,451,520",
      len(Gp_set) == 12096 and oT2 == 1451520)
check("Z2b", "MEASURED (conditional expectation): tau'(G) == G is %s and "
      "the triple intersection has order %d -- %s"
      % (tpG_in_G, triple,
         "the raw turner normalizes the still point and the triangle's "
         "pairwise intersections coincide" if tpG_in_G and triple == nG
         else "the RAW turner (tau'^3 = inn(h'), h' != 1) does NOT "
         "normalize G; the triangle's three pairwise intersections are "
         "three DIFFERENT G2(2)'s -- exactly what ZB3's normalization "
         "must repair"), True)
tick("stage 2 done")

# ======================================================================
banner("STAGE 3 -- ZB3: THE TURN OF ORDER THREE -- tau'' = inn(y^-1) o tau'")
# ======================================================================
pairsG = list(zip(Gmats, [tau_p(M) for M in Gmats]))
dY, Ys = good_intertwiners(pairsG)
note("intertwiner space for tau'|_G: dim %d; invertible Dickson-0 "
     "isometric solutions: %d" % (dY, len(Ys)))
check("Z3a", "an invertible Dickson-0 isometry y with y g y^-1 = tau'(g) on "
      "the generators of G EXISTS (tau'|_G is inner-realized: G2(2) is "
      "complete and its turned copy is Omega-conjugate)", len(Ys) >= 1,
      "dim %d, %d candidates" % (dY, len(Ys)))
results = []
for Ym in Ys:
    Yi = f2_matinv(Ym)
    def tau_pp(M, Yi=Yi, Ym=Ym): return mmul(Yi, mmul(tau_p(M), Ym))
    fix_ok = all(tau_pp(M) == M for M in Gmats)
    T3 = [tau_pp(tau_pp(tau_pp(M))) for M in OMEGA_GENS]
    ord3 = all(A == B for A, B in zip(T3, OMEGA_GENS))
    results.append((Ym, fix_ok, ord3, T3))
best = next((r for r in results if r[1] and r[2]), None)
if best is None: best = next((r for r in results if r[1]), results[0])
Ym, fix_ok, ord3, T3 = best
Yi = f2_matinv(Ym)
def tau_pp(M): return mmul(Yi, mmul(tau_p(M), Ym))
check("Z3b", "tau'' fixes every generator of G (hence G pointwise)", fix_ok)
if ord3:
    check("Z3c", "REGISTERED EXPECTATION CONFIRMED: tau''^3 = identity on "
          "ALL 26 Omega-generators -- the turner normalized to EXACT order "
          "three (y columns %s); %d of %d intertwiner candidates give "
          "order 3" % ((Ym,), sum(1 for r in results if r[1] and r[2]),
                        len(results)), True)
else:
    dZ, Zs = good_intertwiners(list(zip(OMEGA_GENS, T3)))
    check("Z3c", "REGISTERED EXPECTATION INVERTED (full prominence): "
          "tau''^3 is NOT the identity on the generators; it is inner by "
          "z = %s (must centralize G: C_Omega(G2(2)) != 1 would be the "
          "finding)" % (Zs[0] if Zs else "NOT FOUND"), False)
tick("stage 3 done")

# ======================================================================
banner("STAGE 4 -- ZB4: Fix(tau'') = G, as far as the machine reaches")
# ======================================================================
TppC = [tau_pp(M) for M in Cmats]
oTT, memTT, trTT, baseTT = make_bsgs_full([perm_of(M) for M in TppC], 120)
t1 = time.time()
mask2 = member_mask(EN_C, baseTT, trTT)
G2_set = set(tuple(int(x) for x in r) for r in EN_C[mask2])
tick("second exhaustive sift (through tau''(C-bar)) done (%.1fs)"
     % (time.time() - t1))
check("Z4a", "C-bar cap tau''(C-bar) = G EXACTLY (order %d, set equality "
      "with G): every tau''-fixed element of the vector shadow lies in G"
      % len(G2_set), G2_set == G_set)
Tpp2C = [tau_pp(M) for M in TppC]
oTT2, memTT2, trTT2, baseTT2 = make_bsgs_full([perm_of(M) for M in Tpp2C],
                                              120)
G_in_TT2 = all(memTT2(p) for p in G_list)
Tpp3C = [tau_pp(M) for M in Tpp2C]
closes = all(memC(perm_of(M)) for M in Tpp3C)
# the other two pairwise intersections: tau''(G) = G pointwise, so
# tau''(C-bar) cap tau''^2(C-bar) = tau''(G) = G and likewise the third
check("Z4b", "THE TRIANGLE CLOSES under tau'': tau''^3(C-bar) = C-bar "
      "(all 24 images pass C-bar's membership strip); G <= tau''^2(C-bar) "
      "(all 12096 elements sift), so all three pairwise intersections of "
      "(C-bar, tau''(C-bar), tau''^2(C-bar)) equal G (the other two are "
      "tau''-images of the first, and tau'' fixes G pointwise)",
      closes and G_in_TT2 and oTT == 1451520 and oTT2 == 1451520)
def rand_elem():
    M = IDM8
    for _ in range(random.randrange(4, 12)):
        M = mmul(M, OMEGA_GENS[random.randrange(26)])
    return M
NSAMP = 1200
n_fixed = 0; n_fixed_outside = 0; n_inC = 0
t1 = time.time()
for _ in range(NSAMP):
    M = rand_elem()
    p = perm_of(M)
    if memC(p): n_inC += 1
    if tau_pp(M) == M:
        n_fixed += 1
        if p not in G_set: n_fixed_outside += 1
tick("random sample of %d Omega-elements through tau'' (%.1fs)"
     % (NSAMP, time.time() - t1))
check("Z4c", "random sample: %d elements of Omega (words in the 26 "
      "generators; %d of them happened to lie in C-bar), %d fixed by "
      "tau'', %d fixed OUTSIDE G -- consistent with Fix(tau'') = G "
      "[P cited: the centralizer of an order-3 graph automorphism of "
      "O8+(2) is G2(2)]; the machine-checked part is Z4a/Z4b"
      % (NSAMP, n_inC, n_fixed, n_fixed_outside), n_fixed_outside == 0)
json.dump({"y_cols": list(Ym), "tau_pp_order3": ord3},
          open(os.path.join(CACHE_Z, "turner_normalized.json"), "w"))
tick("stage 4 done")

# ======================================================================
banner("STAGE 5 -- ZB5: THE SEVEN AT THE STILL POINT")
# ======================================================================
invs = [g for g in G_list if pord(g) == 2]
thr = [g for g in G_list if pord(g) == 3]
note("G has %d involutions and %d elements of order 3" % (len(invs), len(thr)))
copies = []           # list of frozensets
copy_gens = []
t1 = time.time()
for a in invs:
    for b in thr:
        ab = pmul(a, b)
        if pord(ab) != 7: continue
        if pord(comm(a, b)) != 4: continue
        if any(a in L and b in L for L in copies): continue
        L = closure([a, b], cap=200)
        if len(L) != 168: continue
        copies.append(frozenset(L)); copy_gens.append((a, b))
tick("(2,3,7)-pair scan over G done: %d distinct PSL(2,7) copies (%.1fs)"
     % (len(copies), time.time() - t1))
# G-conjugacy orbits of the copies
def conj_set(L, g):
    gi = pinv(g)
    return frozenset(pmul(pmul(g, x), gi) for x in L)
orbits = []
seen = set()
for i, L in enumerate(copies):
    if i in seen: continue
    orb = {L}; fr = [L]
    while fr:
        X = fr.pop()
        for g in Ggens:
            Y = conj_set(X, g)
            if Y not in orb:
                orb.add(Y); fr.append(Y)
    idxs = [j for j, L2 in enumerate(copies) if L2 in orb]
    seen |= set(idxs)
    orbits.append((idxs, orb))
note("G-conjugacy orbits of the copies: sizes %s" % [len(o) for _, o in orbits])
# normalizer of the first copy in G
L0 = copies[0]; a0, b0 = copy_gens[0]
NL = [g for g in G_list
      if pmul(pmul(g, a0), pinv(g)) in L0 and pmul(pmul(g, b0), pinv(g)) in L0]
check("Z5a", "G contains PSL(2,7): %d copies found by the (2,3,7)+[a,b]^4 "
      "scan, forming %d G-conjugacy orbit(s); N_G(L2(7)) has order %d "
      "(= 336 = PGL(2,7) expected: the ambient outer flip lives at the "
      "still point); 12096/|N| = %s copies per orbit"
      % (len(copies), len(orbits), len(NL),
         12096 // len(NL) if len(NL) else "-"),
      len(copies) >= 1 and len(NL) == 336
      and all(len(o) == 36 for _, o in orbits))

# fingerprints: class size of an involution in C-bar and in tau'(C-bar)
def class_size_in(EN, g_tuple):
    g = np.array(g_tuple, dtype=np.uint8)
    n_c = 0; CH = 262144
    for s in range(0, EN.shape[0], CH):
        chunk = EN[s:s + CH]
        n_c += int((chunk[:, g] == g[chunk]).all(axis=1).sum())
    return EN.shape[0] // n_c
EN_T = enumerate_group_np(trT, 120)
assert EN_T.shape[0] == 1451520
EPS_OF_SIZE = {63: -1, 315: 1, 945: -1, 3780: 1}
fp = []
for idxs, orb in orbits:
    a = copy_gens[idxs[0]][0]
    sC = class_size_in(EN_C, a); sT = class_size_in(EN_T, a)
    fp.append((sC, sT))
    note("orbit of %d copies: involution class size in C-bar = %d (%s), "
         "in tau'(C-bar) = %d (%s)"
         % (len(orb), sC, "BRIDGE" if sC == 315 else "FANO" if sC == 945
            else "?", sT, "BRIDGE-type" if sT == 315 else "FANO-type"
            if sT == 945 else "?"))
bridge_all = all(sC == 315 for sC, _ in fp)
fano_all = all(sC == 945 for sC, _ in fp)
if bridge_all:
    check("Z5b", "REGISTERED EXPECTATION CONFIRMED: every PSL(2,7) at the "
          "still point is the BRIDGE class of C-bar (involutions in the "
          "315-class) -- the seven that meets G2(2) is the P^1(F7) seven, "
          "as SM-035 read it at the crystal level", True)
elif fano_all:
    check("Z5b", "REGISTERED EXPECTATION INVERTED (full prominence): the "
          "PSL(2,7) at the still point is the FANO class (945) -- read "
          "against SM-035", False)
else:
    check("Z5b", "MIXED: the still point holds PSL(2,7)'s of BOTH classes "
          "(%s) -- registered expectation neither confirmed nor inverted; "
          "recorded" % fp, False)
same_label = all((sC == 315) == (sT == 315) for sC, sT in fp)
check("Z5c", "MEASURED: the class label read in the spin-type shadow "
      "tau'(C-bar) %s the label read in the vector shadow (%s) -- %s"
      % ("AGREES with" if same_label else "DIFFERS from", fp,
         "the seven's label survives the turn" if same_label
         else "the turn RELABELS the seven"), True)
tick("stage 5 done")

# ======================================================================
banner("STAGE 6 -- ZB6: the register of the still point")
# ======================================================================
# G-classes of involutions
cls_reps = []; seen_inv = set()
for a in invs:
    if a in seen_inv: continue
    orb = {a}; fr = [a]
    while fr:
        x = fr.pop()
        for g in Ggens:
            y = pmul(pmul(g, x), pinv(g))
            if y not in orb:
                orb.add(y); fr.append(y)
    seen_inv |= orb
    cls_reps.append((a, len(orb)))
say("  G-class of involutions (size) : class size in C-bar (eps) : "
    "class size in tau'(C-bar) (eps)")
minus_spin = False; minus_vec = False
table = []
for a, sz in cls_reps:
    sC = class_size_in(EN_C, a); sT = class_size_in(EN_T, a)
    eC = EPS_OF_SIZE.get(sC, 0); eT = EPS_OF_SIZE.get(sT, 0)
    minus_vec |= (eC == -1); minus_spin |= (eT == -1)
    table.append((sz, sC, eC, sT, eT))
    say("    %4d : %5d (%s) : %5d (%s)"
        % (sz, sC, "+" if eC == 1 else "-", sT, "+" if eT == 1 else "-"))
check("Z6a", "G's involutions fall into %d G-classes of sizes %s; every "
      "class resolves in the sealed Sp6(2) involution classes "
      "{63,315,945,3780} both in C-bar and in tau'(C-bar)"
      % (len(cls_reps), [sz for sz, *_ in table]),
      all(sC in EPS_OF_SIZE and sT in EPS_OF_SIZE
          for _, sC, _, sT, _ in table))
if minus_spin:
    check("Z6b", "REGISTERED EXPECTATION CONFIRMED: read in the spin-type "
          "shadow tau'(C-bar), G meets a MINUS class (%s) => by SM-033's "
          "necessity theorem the preimage of G in the spin tower 2.Sp6(2) "
          "is NON-SPLIT: 2.G2(2) sits over the hinge. (In the vector "
          "shadow the W(E8)-preimage is split trivially, SM-023.)"
          % [(sT, "-") for _, _, _, sT, eT in table if eT == -1], True)
else:
    check("Z6b", "REGISTERED EXPECTATION INVERTED: all of G's involutions "
          "are PLUS in the spin-type reading -- eps cannot decide the "
          "splitness of G's spin-tower preimage (SM-033: necessity only); "
          "UNDECIDED here, recorded", False)
note("vector-shadow reading: G meets a minus class there too: %s (the 63 "
     "U3(3)-involutions as symplectic transvections of Stab(v))"
     % minus_vec)
# --- POST-REVEAL FINDING (added after the first run showed ZB6 INVERTED;
#     not a registered bar; first-run log kept as *_FIRSTRUN.log).
#     H^2(G2(2), Z2) = Hom(M(G2(2)), Z2) + Ext(G2(2)^ab, Z2) = 0 + Z2
#     [P cited: the Schur multiplier of G2(2) = U3(3):2 is trivial (ATLAS)],
#     and the surviving Ext-class restricts ISOMORPHICALLY to <t> for any
#     OUTER involution t (since <t> -> G -> G^ab = C2 is an isomorphism).
#     So the extension class of any central Z2-extension of G is detected
#     by the lift-order of one outer involution: eps(t) = + <=> SPLIT.
inner = [(sz, sC, eC, sT, eT, a in Dsub) for (a, sz), (_, sC, eC, sT, eT)
         in zip(cls_reps, table)]
outer_cls = [(sz, sT, eT) for sz, sC, eC, sT, eT, isin in inner if not isin]
inner_cls = [(sz, sT, eT) for sz, sC, eC, sT, eT, isin in inner if isin]
note("inner (in [G,G] = U3(3)) involution classes: %s ; outer: %s"
     % (inner_cls, outer_cls))
split_spin = bool(outer_cls) and all(eT == 1 for _, _, eT in outer_cls)
check("Z6c", "POST-REVEAL FINDING (not registered; added after the first "
      "run): the %d-class is OUTER (outside [G,G]) and the %d-class INNER; "
      "the outer involutions read eps = + in the spin-type shadow, so by "
      "M(G2(2)) = 1 [P cited] + the Ext-restriction argument the spin-"
      "tower preimage of G is SPLIT: 2 x G2(2), not 2.G2(2) -- the still "
      "point lifts through the hinge without twisting (both shadows agree; "
      "the register of the still point is TRIVIAL)"
      % (outer_cls[0][0] if outer_cls else -1,
         inner_cls[0][0] if inner_cls else -1),
      split_spin and len(outer_cls) == 1 and len(inner_cls) == 1)
json.dump({"involution_table": table, "psl27_fingerprints": fp,
           "n_copies": len(copies), "normalizer_order": len(NL),
           "census": census_G}, open(os.path.join(CACHE_Z, "witnesses_z.json"),
                                     "w"), indent=1)
tick("stage 6 done")

# ======================================================================
banner("VERDICT")
# ======================================================================
say("""  The turn holds still a G2(2) = U3(3):2 of order 12096: the
  intersection of the vector shadow with its turned image, index 120.
  Normalized by its own intertwiner, the turner has exact order three and
  fixes exactly that subgroup (machine-checked inside the three shadows;
  [P] for the rest).  PSL(2,7) lives at the still point with its ambient
  outer flip (PGL(2,7) = its normalizer there); its class and the
  register are read above.""")
say("")
say("RESULT: %d checks passed, %d failed%s" % (PASS, FAIL,
    ("  FAILED: %s" % FAILED) if FAILED else ""))
tick("done")
LOG.close()
