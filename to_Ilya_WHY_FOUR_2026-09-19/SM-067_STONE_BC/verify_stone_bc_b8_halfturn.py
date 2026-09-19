# -*- coding: utf-8 -*-
r"""verify_stone_bc_b8_halfturn.py -- STONE BC: DOES THE 4-CUBE ANOMALY RECUR ON THE 8-CUBE?

Brief: BRIEF_STONE_BC_B8_HALFTURN.md (lock BRIEF_STONE_BC_LOCK.sha256, re-verified as BC0).
BC1 orbit structure of R on the B8 spinor (guess: 16 free orbits of 16); BC2 O1 = the full-height orbit, half-turn shift
+-4, no Weyl u reproduces it (Lemma BB-B, m = 4); BC3 MAIN GUESS: at least one other orbit carries the half-turn as a Weyl
element (BC3b: exactly 2, swapped by w0 = -1); BC4 |C_8|, |I_8| exact, Lemma-B prediction I_8 = C_W(c), extras listed
(guess ratio 2); BC5 I_k = C_k for k != 8 on B8; BC6 D9 half-spin by containment, affine fit and (disclosed tightening)
full enumeration; BC7 B6, B7 clean at every lag; BC8 [P+C] what distinguishes the carrying orbits.

Machinery: the e-coordinate board machine of verify_stone_av_d5_anomaly.py VERBATIM (board, B_spin, D_half, closure,
IC, comp, pinv, ppow, orbits, ctype) for the boards and the B4/B5 engine cross-check; the Minuscule class and cartan_D /
inverse_frac of verify_stone_aq_rush_shi_defect.py VERBATIM for the D9 omega_9 cross-check (AV1's pattern);
reproducing_us / linear_span / affine_linear_part of verify_stone_bb_halfturn_fullheight.py generalised from 4 to n
bits.  NEW HERE: the affine (pi, v) engine -- W(B_n) = F2^n x| S_n acting on the 2^n sign patterns as x -> pi(x) ^ v,
and W(D_{n+1}) on the same 2^n patterns (the even code, parity bit dropped) -- W is never materialised as tuples
(brief sec 3 step 2).  Membership of a transport f = R^-k g R^k in W is tested by its values at 0 and the n unit vectors
(cheap, vectorised over all v for a block of pi) and then, for the survivors, on all 2^n points; a candidate failing the
cheap test fails the full 2^n-point check a fortiori, so this is the brief's 40,320 x 256 x 256-point test.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED at equal prominence; no registry/git writes.
Not RH/GRH.  Rule 3: "clock", "half-turn", "grammar" are labels for permutations and subgroups.
Run:  python -X utf8 verify_stone_bc_b8_halfturn.py
"""
import os, sys, time, json, hashlib, itertools, math
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_bc_b8_halfturn.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def guess(tag, claim, ok, detail=""):
    r = check(tag, "REGISTERED GUESS: " + claim, ok, detail)
    if not r: say("  [INVERTED] %s -- recorded at equal prominence." % tag)
    return r
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))
WIT = {}

say("=" * 78); say("STONE BC -- DOES THE 4-CUBE ANOMALY RECUR ON THE 8-CUBE?"); say("=" * 78)
BRIEF = "BRIEF_STONE_BC_B8_HALFTURN.md"; LOCK = open("BRIEF_STONE_BC_LOCK.sha256").read().split()[0]
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("BC0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_BC_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
WIT["brief_sha"] = sha

# ============================================================================ e-coordinate board machine, VERBATIM from
# verify_stone_av_d5_anomaly.py (itself verbatim from _explore_d5_probes_2026-09-10.py)
H = Fraction(1, 2)
def ip(a, b): return sum(x * y for x, y in zip(a, b))
def refl(w, a): return tuple(x - 2 * ip(w, a) / ip(a, a) * y for x, y in zip(w, a))
def label(w, a): return 2 * ip(w, a) / ip(a, a)
def board(weights, roots):
    W = sorted(set(weights)); idx = {w: i for i, w in enumerate(W)}; N = len(W)
    S = [tuple(idx[refl(w, a)] for w in W) for a in roots]
    down = [[] for _ in range(N)]
    for i, w in enumerate(W):
        for a in roots:
            if label(w, a) == 1: down[i].append(idx[tuple(x - y for x, y in zip(w, a))])
    below = [set() for _ in range(N)]
    height = lambda w: ip(w, tuple(Fraction(97 - 7 * j) for j in range(len(w))))   # generic functional
    for i in sorted(range(N), key=lambda i: height(W[i])):
        for b in down[i]: below[i] |= {b} | below[b]
    leq = lambda a, b: a == b or a in below[b]
    bottom = [i for i in range(N) if not down[i]]; assert len(bottom) == 1; bottom = bottom[0]
    P = [i for i in range(N) if len(down[i]) == 1]
    R = []
    for x in range(N):
        Sx = [p for p in P if not leq(p, x)]
        if not Sx: R.append(bottom); continue
        mins = [p for p in Sx if not any(q != p and leq(q, p) for q in Sx)]
        ub = [y for y in range(N) if all(leq(p, y) for p in mins)]
        join = [y for y in ub if not any(z != y and leq(z, y) for z in ub)]
        assert len(join) == 1; R.append(join[0])
    assert sorted(R) == list(range(N))
    return W, idx, S, tuple(R), P, leq
def comp(p, q): return tuple(p[q[i]] for i in range(len(p)))
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def ppow(p, e):
    x = tuple(range(len(p)))
    for _ in range(e): x = comp(p, x)
    return x
def closure(gens):
    e = tuple(range(len(gens[0]))); seen = {e}; fr = [e]
    while fr:
        nxt = []
        for g in fr:
            for s in gens:
                h = comp(s, g)
                if h not in seen: seen.add(h); nxt.append(h)
        fr = nxt
    return seen
def orbits(p):
    seen = set(); out = []
    for a in range(len(p)):
        if a in seen: continue
        o = []; x = a
        while x not in seen: seen.add(x); o.append(x); x = p[x]
        out.append(o)
    return out
def ctype(p): return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(len(o) for o in orbits(p)).items(), reverse=True))
e = lambda i, n: tuple(Fraction(int(j == i)) for j in range(n))
def D_half(n):  # even sign patterns; roots e_i - e_{i+1}, e_{n-1} + e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [tuple(x + y for x, y in zip(e(n - 2, n), e(n - 1, n)))]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n) if signs.count(-1) % 2 == 0]
    return board(w, roots)
def B_spin(n):  # all sign patterns; roots e_i - e_{i+1}, e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [e(n - 1, n)]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n)]
    return board(w, roots)
def IC(R, Wset, k):
    Rk = ppow(R, k); Rki = pinv(Rk)
    I = {g for g in Wset if comp(comp(Rki, g), Rk) in Wset}; C = {g for g in Wset if comp(g, Rk) == comp(Rk, g)}
    return I, C

# ============================================================================ Minuscule machine, VERBATIM from
# verify_stone_aq_rush_shi_defect.py (cartan_D, inverse_frac, class Minuscule; W_CAP as there)
W_CAP = 400000
def cartan_A(n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        C[i][i] = 2
        if i+1 < n: C[i][i+1] = C[i+1][i] = -1
    return C
def cartan_D(n):
    C = [[0]*n for _ in range(n)]
    for i in range(n): C[i][i] = 2
    for i in range(n-2): C[i][i+1] = C[i+1][i] = -1
    C[n-3][n-1] = C[n-1][n-3] = -1
    return C
def cartan_E(n):  # Bourbaki: chain 1-3-4-5-...-n, node 2 attached to 4
    C = [[0]*n for _ in range(n)]
    for i in range(n): C[i][i] = 2
    chain = [0] + list(range(2, n))
    for a, b in zip(chain, chain[1:]): C[a][b] = C[b][a] = -1
    C[1][3] = C[3][1] = -1
    return C
def inverse_frac(C):
    n = len(C); A = [[Fraction(C[i][j]) for j in range(n)] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0); A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]; A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]; A[r] = [x - f*y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]
class Minuscule:
    def __init__(self, fam, n, k):
        self.fam, self.n, self.k = fam, n, k
        C = {"A": cartan_A, "D": cartan_D, "E": cartan_E}[fam](n); self.C = C; r = n
        self.Cinv = inverse_frac(C)
        lam = tuple(int(i == k-1) for i in range(r))
        # orbit
        orbit = {lam}; frontier = [lam]
        while frontier:
            nxt = []
            for w in frontier:
                for i in range(r):
                    if w[i] != 0:
                        v = tuple(w[j] - w[i]*C[i][j] for j in range(r))
                        if v not in orbit: orbit.add(v); nxt.append(v)
            frontier = nxt
        self.W = sorted(orbit, reverse=True); self.idx = {w: i for i, w in enumerate(self.W)}; N = len(self.W); self.N = N
        assert all(all(x in (-1, 0, 1) for x in w) for w in self.W), "not minuscule"
        # simple reflections as permutations
        self.S = []
        for i in range(r):
            self.S.append(tuple(self.idx[tuple(w[j] - w[i]*C[i][j] for j in range(r))] for w in self.W))
        # inner products
        def ip(a, b): return sum(Fraction(a[i]) * self.Cinv[i][j] * b[j] for i in range(r) for j in range(r))
        self.IP = [[ip(a, b) for b in self.W] for a in self.W]
        # lattice: down-edges w -> w - alpha_i when label_i = 1
        self.down = [[] for _ in range(N)]
        for a, w in enumerate(self.W):
            for i in range(r):
                if w[i] == 1: self.down[a].append(self.idx[tuple(w[j] - C[i][j] for j in range(r))])
        below = [set() for _ in range(N)]  # strict
        order = sorted(range(N), key=lambda a: sum(self.W[a][i] * sum(self.Cinv[i][j] for j in range(r)) for i in range(r)))  # by height
        for a in order:
            for b in self.down[a]: below[a] |= {b} | below[b]
        # first run: this matrix was stored transposed (b <= a) and read as a <= b -- instrumentation, fixed; FIRSTRUN log kept
        self.leq = [[(a == b) or (a in below[b]) for b in range(N)] for a in range(N)]   # leq[a][b]  <=>  a <= b
        self.top = self.idx[lam]; self.bottom = next(a for a in range(N) if not self.down[a])
        assert sum(1 for a in range(N) if not self.down[a]) == 1
        # join-irreducibles
        self.P = [a for a in range(N) if len(self.down[a]) == 1]
        self.chain = all(self.leq[a][b] or self.leq[b][a] for a in self.P for b in self.P)
        # rowmotion
        R = []
        for x in range(N):
            Sx = [p for p in self.P if not self.leq[p][x]]
            if not Sx: R.append(self.bottom); continue
            mins = [p for p in Sx if not any(q != p and self.leq[q][p] for q in Sx)]
            ub = [y for y in range(N) if all(self.leq[p][y] for p in mins)]
            join = [y for y in ub if not any(z != y and self.leq[z][y] for z in ub)]
            assert len(join) == 1, "join not unique"
            R.append(join[0])
        assert sorted(R) == list(range(N)), "rowmotion not a bijection"
        self.R = tuple(R)
    def compose(self, p, q): return tuple(p[q[i]] for i in range(self.N))
    def cyc(self, p):
        seen = set(); c = []
        for a in range(self.N):
            if a in seen: continue
            o = 0; x = a
            while x not in seen: seen.add(x); o += 1; x = p[x]
            c.append(o)
        return tuple(sorted(c, reverse=True))
    def order(self, p):
        e = tuple(range(self.N)); x = p; n = 1
        while x != e: x = self.compose(p, x); n += 1
        return n

# ============================================================================ NEW: bit-pattern boards and the affine engine
PC = np.array([bin(i).count("1") for i in range(1 << 11)], dtype=np.int64)       # popcount table
def bits_of(w): return sum(1 << i for i, s in enumerate(w) if s < 0)                # bit i set iff coordinate i negative
def rebase(Wl, R, n):
    """rowmotion of a board (weights = sign patterns) as a permutation of the 2^n patterns of the FIRST n coordinates."""
    N = 1 << n; Rb = np.full(N, -1, dtype=np.int64)
    for i, w in enumerate(Wl): Rb[bits_of(w[:n])] = bits_of(Wl[R[i]][:n])
    assert sorted(Rb.tolist()) == list(range(N)); return Rb
def perm_pow(p, k):
    x = np.arange(len(p));
    for _ in range(k): x = p[x]
    return x
def perm_inv(p):
    r = np.empty_like(p); r[p] = np.arange(len(p)); return r
def cyc_type(p): return ctype(tuple(int(x) for x in p))
def perm_orbits(p): return orbits(tuple(int(x) for x in p))

def all_perm_arrays(n, nb, chunk=20000):
    """for every pi in S_n (lexicographic): the array x -> pi(x) on the 2^nb bit patterns.  When n == nb + 1 the n-th
       coordinate is the parity bit of the even code (W(D_{nb+1}) on the B_nb board) and is dropped again after pi."""
    PI = np.array(list(itertools.permutations(range(n))), dtype=np.int64)
    X = np.arange(1 << nb, dtype=np.int64)
    X9 = X | ((PC[X] & 1) << nb) if n == nb + 1 else X
    out = np.empty((len(PI), len(X)), dtype=np.uint8 if nb <= 8 else np.int64)
    mask = (1 << nb) - 1
    for s in range(0, len(PI), chunk):
        blk = np.zeros((min(chunk, len(PI) - s), len(X)), dtype=np.int64)
        for i in range(n): blk |= ((X9 >> i) & 1)[None, :] << PI[s:s + chunk, i][:, None]
        out[s:s + chunk] = blk & mask
    return PI, out
def is_B_linear(Li, nb):        # Li (..., nb): images of the unit vectors; a coordinate permutation?
    pw = (Li != 0) & ((Li & (Li - 1)) == 0)
    return pw.all(-1) & (np.bitwise_or.reduce(Li, axis=-1) == (1 << nb) - 1)
def lift(y, nb): return y | ((PC[y] & 1) << nb)
def is_D_linear(Li, nb):        # the lifted images are weight-2 vectors sharing one coordinate, the others distinct
    L9 = lift(Li, nb)
    return (PC[L9] == 2).all(-1) & (np.bitwise_and.reduce(L9, axis=-1) != 0) & (PC[np.bitwise_or.reduce(L9, axis=-1)] == nb + 1)
def enum_transport(PERMS, Rk, Rki, test, nb, block=512):
    """all (pi_index, v) with R^-k g R^k in the target group (test), g = (pi, v): x -> PERMS[pi][x] ^ v."""
    N = 1 << nb; cols = np.array([0] + [1 << i for i in range(nb)]); V = np.arange(N); X = np.arange(N); found = []
    for s in range(0, len(PERMS), block):
        P = PERMS[s:s + block].astype(np.int64)
        F = Rki[P[:, Rk[cols]][:, None, :] ^ V[None, :, None]]              # (B, N, nb+1): f at 0 and the unit vectors
        f0 = F[..., 0]; Li = F[..., 1:] ^ f0[..., None]
        for bi, v in zip(*np.nonzero(test(Li, nb))):
            p = P[bi]; ff = Rki[p[Rk[X]] ^ v]; L = np.zeros(N, dtype=np.int64)
            for i in range(nb): L ^= ((X >> i) & 1) * int(Li[bi, v, i])
            if np.array_equal(ff, L ^ int(f0[bi, v])): found.append((s + int(bi), int(v)))
    return found
def enum_commute(PERMS, c, nb, block=512):
    """all (pi_index, v) with g c = c g."""
    N = 1 << nb; cols = np.array([0] + [1 << i for i in range(nb)]); V = np.arange(N); found = []
    for s in range(0, len(PERMS), block):
        P = PERMS[s:s + block].astype(np.int64)
        left = P[:, c[cols]][:, None, :] ^ V[None, :, None]; right = c[P[:, cols][:, None, :] ^ V[None, :, None]]
        for bi, v in zip(*np.nonzero((left == right).all(-1))):
            p = P[bi]
            if np.array_equal(p[c] ^ v, c[p ^ v]): found.append((s + int(bi), int(v)))
    return found
def g_arr(PERMS, g): return PERMS[g[0]].astype(np.int64) ^ g[1]
def mode_count_rows(D):
    """per row of D: the multiplicity of the most frequent value."""
    B, m = D.shape; S = np.sort(D, axis=1); flat = S.ravel()
    boundary = np.ones(B * m + 1, dtype=bool); boundary[1:-1] = flat[1:] != flat[:-1]; boundary[np.arange(0, B * m, m)] = True
    starts = np.flatnonzero(boundary); lens = np.diff(starts); row = starts[:-1] // m
    first = np.flatnonzero(np.r_[True, row[1:] != row[:-1]])
    return np.maximum.reduceat(lens, first)
def best_agreement(PERMS, target, pts=None, block=4096):
    """max over (pi, v) of #{x in pts : pi(x) ^ v == target[x]}; returns (max, number of (pi, v) attaining it)."""
    pts = np.arange(len(target)) if pts is None else np.asarray(pts); T = target[pts].astype(np.int64); best = 0; nbest = 0
    for s in range(0, len(PERMS), block):
        D = PERMS[s:s + block][:, pts].astype(np.int64) ^ T[None, :]; mc = mode_count_rows(D); m = int(mc.max())
        if m > best: best, nbest = m, 0
        if m == best:
            for r in np.flatnonzero(mc == m): nbest += sum(1 for _, c in Counter(D[r].tolist()).items() if c == m)
    return best, nbest
def weyl_agreeing(PERMS, target, pts):
    """all (pi, v) with pi(x) ^ v == target[x] for every x in pts (v pinned by pts[0])."""
    pts = np.asarray(pts); T = target[pts].astype(np.int64)
    D = PERMS[:, pts].astype(np.int64) ^ T[None, :]
    rows = np.flatnonzero((D == D[:, :1]).all(1))
    return [(int(r), int(D[r, 0])) for r in rows]
# ---- Stone BB helpers, generalised to nb bits
def reproducing_us(O, shift, nb):
    U = np.arange(1 << nb); O = np.asarray(O)
    ok = (PC[U][:, None] - 2 * PC[U[:, None] & O[None, :]] == shift[O][None, :]).all(1)
    return [int(u) for u in U[ok]]
def f2_rank(vecs):
    basis = []
    for v in vecs:
        v = int(v)
        for b in basis: v = min(v, v ^ b)
        if v: basis.append(v)
    return len(basis)
def affine_dim(pts): return f2_rank([int(p) ^ int(pts[0]) for p in pts])
def affine_linear_part(O, f, nb):
    """the linear part of the affine extension of f|O (base O[0]); (consistent, determined, is_perm, L or None)."""
    base = int(O[0]); fb = int(f[base]); known = {}
    for x in O:
        d = int(x) ^ base; im = int(f[x]) ^ fb
        if d in known and known[d] != im: return (False, False, False, None)
        known[d] = im
    changed = True
    while changed:
        changed = False
        for d1, i1 in list(known.items()):
            for d2, i2 in list(known.items()):
                d = d1 ^ d2; im = i1 ^ i2
                if d in known:
                    if known[d] != im: return (False, False, False, None)
                else: known[d] = im; changed = True
    if len(known) < (1 << nb): return (True, False, False, None)
    L = [known[1 << i] for i in range(nb)]
    is_perm = all(l and (l & (l - 1)) == 0 for l in L) and len(set(L)) == nb
    return (True, True, is_perm, L)
# ---- names
def sp_name(pi, v, n):  # e_i -> +-e_{pi(i)}, the sign negative iff v has bit pi(i)
    return tuple(("-" if (v >> pi[i]) & 1 else "+") + "e%d" % (pi[i] + 1) for i in range(n))
def cycle_name(pi, v, n):
    seen = set(); parts = []
    for i in range(n):
        if i in seen: continue
        chain = []; s, j = 1, i
        while True:
            chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); seen.add(j)
            s = s * (-1 if (v >> pi[j]) & 1 else 1); j = pi[j]
            if j == i: chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); break
        if len(chain) == 2 and chain[0] == chain[1]: continue           # fixed +e_i
        parts.append("(" + " -> ".join(chain) + ")")
    return " ".join(parts) if parts else "1"
def name_B(PI, g, n): return cycle_name(tuple(int(t) for t in PI[g[0]]), g[1], n)
def name_D(PI9, g, nb):   # v on the even code: the 9th bit is the parity of the 8 given
    v9 = g[1] | ((PC[g[1]] & 1) << nb); return cycle_name(tuple(int(t) for t in PI9[g[0]]), int(v9), nb + 1)
def elem_orders(PERMS, S):
    out = Counter()
    for g in S:
        a = g_arr(PERMS, g); x = a.copy(); o = 1
        while not np.array_equal(x, np.arange(len(a))): x = a[x]; o += 1
        out[o] += 1
    return out
def lag_table(PERMS, Rb, testI, nb, lags):
    out = {}
    for k in lags:
        Rk = perm_pow(Rb, k); Rki = perm_inv(Rk)
        I = set(enum_transport(PERMS, Rk, Rki, testI, nb)); C = set(enum_commute(PERMS, Rk, nb))
        out[k] = (I, C)
    return out

# ============================================================================ boards
banner("BOARDS -- B8 spinor (256), D9 half-spin (256, cross-check), B6 (64), B7 (128), B4 (16), B5 (32)")
W8, idx8, S8, R8t, P8, _ = B_spin(8); Rb8 = rebase(W8, R8t, 8)
tick("B8 spinor built: |P| = %d, rowmotion type %s" % (len(P8), cyc_type(Rb8)))
W9, idx9, S9, R9t, P9, _ = D_half(9); Rb9 = rebase(W9, R9t, 8)
tick("D9 half-spin built (AV machine): |P| = %d" % len(P9))
M9 = Minuscule("D", 9, 9)
def d_labels_to_signs(w):
    n = len(w); s = [0] * n; s[n - 2] = w[n - 2] + w[n - 1]; s[n - 1] = w[n - 1] - w[n - 2]
    for i in range(n - 3, -1, -1): s[i] = s[i + 1] + 2 * w[i]
    return tuple(s)
signs9 = [d_labels_to_signs(w) for w in M9.W]
assert all(all(x in (1, -1) for x in s) for s in signs9) and all(s.count(-1) % 2 == 0 for s in signs9)
RbM = np.full(256, -1, dtype=np.int64)
for i, s in enumerate(signs9): RbM[bits_of(s[:8])] = bits_of(signs9[M9.R[i]][:8])
tick("D9 omega_9 built (AQ Minuscule machine): N = %d, |P| = %d" % (M9.N, len(M9.P)))
check("BC1-x", "one clock on three builds: the B8 spinor rowmotion (AV machine), the D9 half-spin rowmotion (AV machine, 9th coordinate dropped) and D9 omega_9 (AQ Minuscule machine from the Cartan matrix, labels -> signs) are the same permutation of the 256 sign patterns; |P| = 36 = |delta_8|",
      np.array_equal(Rb8, Rb9) and np.array_equal(Rb8, RbM) and len(P8) == 36 and len(P9) == 36 and len(M9.P) == 36)
PI8, PERMS8 = all_perm_arrays(8, 8); tick("W(B8) as (pi, v): %d pi x 256 v = %d elements" % (len(PI8), len(PI8) * 256))
PI9, PERMS9 = all_perm_arrays(9, 8); tick("W(D9) as (pi, v): %d pi x 256 v = %d elements" % (len(PI9), len(PI9) * 256))
assert len(PI8) * 256 == 10321920 and len(PI9) * 256 == 92897280
# W(B8) inside W(D9): pi in S_9 fixing the 9th letter
S9_index = {tuple(int(t) for t in PI9[i]): i for i in range(len(PI9))}
def B_in_D(g): return (S9_index[tuple(int(t) for t in PI8[g[0]]) + (8,)], g[1])
assert all(np.array_equal(g_arr(PERMS8, g), g_arr(PERMS9, B_in_D(g))) for g in [(0, 0), (5, 77), (40319, 255), (12345, 1)])

# ---- engine check against Stone AV's materialised IC on B4 and B5 (not a bar of the brief; the engine's own test)
banner("ENGINE CHECK -- the affine engine against Stone AV's materialised W on B4 (384) and B5 (3840)")
def as_tuple(Wl, idx, n, PERMS, g):
    a = g_arr(PERMS, g); out = []
    for w in Wl:
        y = int(a[bits_of(w)]); out.append(idx[tuple(-H if (y >> i) & 1 else H for i in range(n))])
    return tuple(out)
eng_ok = True
for n in (4, 5):
    Wn, idxn, Sn, Rnt, Pn, _ = B_spin(n); WB = closure(Sn); Rbn = rebase(Wn, Rnt, n); PIn, PERMSn = all_perm_arrays(n, n)
    if n == 4: Rb_B4, PI_B4, PERMS_B4 = Rbn, PIn, PERMSn
    for k in range(1, 2 * n):
        I, C = IC(Rnt, WB, k); Rk = perm_pow(Rbn, k); Rki = perm_inv(Rk)
        Ie = {as_tuple(Wn, idxn, n, PERMSn, g) for g in enum_transport(PERMSn, Rk, Rki, is_B_linear, n)}
        Ce = {as_tuple(Wn, idxn, n, PERMSn, g) for g in enum_commute(PERMSn, Rk, n)}
        eng_ok &= (Ie == I and Ce == C)
    note("B%d: I_k and C_k agree with AV's materialised sets at every lag: %s" % (n, eng_ok))
# W(D5) on the B4 board against AV's closure of D_half(5)
W5d, idx5d, S5d, R5dt, _, _ = D_half(5); WD5 = closure(S5d); Rb4 = rebase(W5d, R5dt, 4); PI5, PERMS5 = all_perm_arrays(5, 4)
def as_tuple_D(g):
    a = g_arr(PERMS5, g); out = []
    for w in W5d:
        y = int(a[bits_of(w[:4])]); y9 = y | ((PC[y] & 1) << 4)
        out.append(idx5d[tuple(-H if (y9 >> i) & 1 else H for i in range(5))])
    return tuple(out)
d_ok = True
for k in range(1, 8):
    I, C = IC(R5dt, WD5, k); Rk = perm_pow(Rb4, k); Rki = perm_inv(Rk)
    Ie = {as_tuple_D(g) for g in enum_transport(PERMS5, Rk, Rki, is_D_linear, 4)}; Ce = {as_tuple_D(g) for g in enum_commute(PERMS5, Rk, 4)}
    d_ok &= (Ie == I and Ce == C)
note("D5 (W(D5) = 1920 as (pi in S5, v in F2^4) on the B4 board): I_k, C_k agree with AV's sets at every lag: %s" % d_ok)
check("BC-engine", "the affine (pi, v) engine reproduces Stone AV's materialised I_k and C_k as sets on B4 (all 7 lags, |I_4| = 8, |C_4| = 4), B5 (all 9 lags) and the D5 half-spin (all 7 lags, I_3 = I_5 = 2, I_4 = 8)", eng_ok and d_ok)
tick("engine check done")

# ============================================================================ BC1 -- orbit structure
banner("BC1 -- orbit structure of R on the B8 spinor")
ORB = perm_orbits(Rb8); ORB.sort(key=lambda o: min(o)); assert ORB[0][0] == 0
orb_of = {x: i for i, o in enumerate(ORB) for x in o}
h = next(k for k in range(1, 100) if np.array_equal(perm_pow(Rb8, k), np.arange(256)))
guess("BC1", "R acts freely on the 256 weights of the B8 spinor: 16 orbits of size 16 (h = 16)",
      cyc_type(Rb8) == "16^16" and h == 16, "type %s, order %d" % (cyc_type(Rb8), h))
WIT["B8_orbits"] = [[int(x) for x in o] for o in ORB]
R8 = perm_pow(Rb8, 8); rank = PC[np.arange(256)]; shift8 = rank[R8] - rank
w0 = np.arange(256) ^ 255
assert np.array_equal(w0[Rb8[w0]], perm_inv(Rb8)), "w0 = -1 reverses R"

# ============================================================================ BC2 -- O1, the full-height orbit
banner("BC2 -- O1 (the orbit of lambda): ranks around the clock, the +-4 shift, no Weyl u")
O1 = ORB[0]; ranks1 = [int(rank[x]) for x in O1]
exp_ranks = [0] + [r for r in range(1, 8) for _ in (0, 1)] + [8]
sh1 = sorted(set(int(shift8[x]) for x in O1))
u1 = reproducing_us(O1, shift8, 8)
span1 = f2_rank(O1)
exp_bwd = [0] + exp_ranks[1:][::-1]
guess("BC2", "O1 is the full-height orbit, ranks 0,1,1,2,2,...,7,7,8 around the clock from lambda (read in either direction); R^8 shifts every rank on it by exactly +-4; O1 spans F2^8; no u in F2^8 reproduces its shift (Lemma BB-B, m = 4: R^8|O1 is not Weyl)",
      ranks1 in (exp_ranks, exp_bwd) and sh1 == [-4, 4] and span1 == 8 and u1 == [],
      "ranks in R-order %s; shifts %s; span %d; reproducing u: %s" % (ranks1, sh1, span1, u1))
note("POST-REVEAL, labelled: the FIRST RUN scored the literal list in R-order (0,1,1,...,7,7,8) and FAILED on orientation alone (_FIRSTRUN.log kept): in R-order the ranks read 0,8,7,7,...,1,1 --")
check("BC2-orient", "POST-REVEAL [C]: on the AV machine R(lambda) = w0.lambda on B4 and on B8 (the paper's sec 7.6 Lemma (a)), and R^-1(lambda) has rank 1; Stone BB's O1 list (0,1,1,2,2,3,3,4) is therefore in R^-1 order, and the phrase 'rowmotion sends w0.lambda straight to lambda' (BB5; MATH v2 Thm 6.2 proof) is R^-1's reading -- nothing in Theorem BB depends on it (the half-turn is its own inverse)",
      int(Rb_B4[0]) == 15 and int(Rb8[0]) == 255 and PC[perm_inv(Rb_B4)[0]] == 1 and PC[perm_inv(Rb8)[0]] == 1)
note("Lemma BB-B engine at n = 8: lambda's shift is %+d, pinning wt(u) = 4; every weight-4 u has odd overlap with some x in O1: %s"
     % (shift8[0], all(any(PC[x & u] % 2 == 1 for x in O1) for u in range(256) if PC[u] == 4)))
tick("BC2 done")

# ============================================================================ BC3 -- every orbit against the half-turn
banner("BC3 -- for every orbit: the u's reproducing its half-turn rank-shift, the nearest Weyl element, the affine extension")
orbinfo = []
for i, O in enumerate(ORB):
    us = reproducing_us(O, shift8, 8); agree, nagree = best_agreement(PERMS8, R8, O)
    ws = weyl_agreeing(PERMS8, R8, O) if agree == 16 else []
    cons, det, isp, L = affine_linear_part(O, R8, 8)
    rk = sorted(int(rank[x]) for x in O); sh = Counter(int(shift8[x]) for x in O)
    orbinfo.append(dict(orbit=i + 1, min=int(min(O)), has_lambda=0 in O, has_w0lambda=255 in O, ranks=(rk[0], rk[-1]), rank_multiset=rk,
                        affine_dim=affine_dim(O), linear_dim=f2_rank(O), shifts=dict(sorted(sh.items())), us=us, best_agreement=agree,
                        n_best=nagree, carrying=(agree == 16), weyl=[(int(p), int(v)) for p, v in ws],
                        weyl_names=[name_B(PI8, g, 8) for g in ws], affine_consistent=cons, linear_part_determined=det, linear_part_is_perm=isp,
                        w0_image=orb_of[int(w0[O[0]])] + 1))
    d = orbinfo[-1]
    say("  O%-2d min=%3d lambda=%d w0lambda=%d ranks %d..%d affdim %d shifts %-28s |u|=%d best agreement %2d/16 (x%d) carrying=%s%s"
        % (d["orbit"], d["min"], d["has_lambda"], d["has_w0lambda"], d["ranks"][0], d["ranks"][1], d["affine_dim"], d["shifts"], len(us), agree, nagree, d["carrying"],
           ("  w = " + "; ".join(d["weyl_names"])) if ws else ""))
carrying = [d for d in orbinfo if d["carrying"]]
WIT["orbits"] = orbinfo
guess("BC3", "at least one R-orbit O != O1 carries the half-turn as a Weyl element (some (pi, v) agrees with R^8 on all 16 points of O)",
      len(carrying) >= 1 and all(not d["has_lambda"] for d in carrying), "carrying orbits: %s" % [d["orbit"] for d in carrying])
guess("BC3b", "(low confidence) the number of carrying orbits is exactly 2, and w0 = -1 exchanges them",
      len(carrying) == 2 and {d["w0_image"] for d in carrying} == {d["orbit"] for d in carrying} and carrying[0]["w0_image"] != carrying[0]["orbit"],
      "count %d; w0 maps carrying orbits to %s" % (len(carrying), [d["w0_image"] for d in carrying]))
note("agreement with a Weyl element per orbit: %s" % [d["best_agreement"] for d in orbinfo])
note("u's reproducing the shift, per orbit (count): %s; affine extension is Weyl (linear part a permutation): %s"
     % ([len(d["us"]) for d in orbinfo], [d["linear_part_is_perm"] for d in orbinfo]))
tick("BC3 done")

# ============================================================================ BC4 -- C_8, I_8, Lemma B
banner("BC4 -- |C_8|, |I_8| by enumeration; the Lemma-B prediction; the extras")
R8i = perm_inv(R8)
t1 = time.time(); C8 = set(enum_commute(PERMS8, R8, 8)); t_c = time.time() - t1
t1 = time.time(); I8 = set(enum_transport(PERMS8, R8, R8i, is_B_linear, 8)); t_i = time.time() - t1
tick("|C_8| = %d (%.1fs), |I_8| = %d (%.1fs) over 10,321,920 elements" % (len(C8), t_c, len(I8), t_i))
assert C8 <= I8, "C_k subset of I_k always"
extras = sorted(I8 - C8)
# Lemma B from each carrying orbit
pred = {}; lemmaB_ok = True
for d in carrying:
    for wg in d["weyl"]:
        wa = g_arr(PERMS8, wg); c = perm_inv(wa)[R8]                                 # c = w^-1 R^8, identity on O
        Y = [int(x) for x in np.flatnonzero(c == np.arange(256))]
        stabY_trivial = affine_dim(Y) == 8
        CWc = set(enum_commute(PERMS8, c, 8))
        # Lemma B: I_8 cap Stab_W(Y) = C_W(c), transport = conjugation by w there
        Yset = set(Y); stabY = {g for g in I8 if {int(t) for t in g_arr(PERMS8, g)[Y]} == Yset}
        conj_ok = all(np.array_equal(R8i[g_arr(PERMS8, g)[R8]], perm_inv(wa)[g_arr(PERMS8, g)[wa]]) for g in CWc)
        lemmaB_ok &= (stabY_trivial and stabY == CWc and conj_ok and CWc <= I8)
        pred[(d["orbit"], wg)] = CWc
        note("O%d, w = %s: c = w^-1 R^8 has Fix(c) of size %d (affine dim %d, %s), cycle type %s; |C_W(c)| = %d; I_8 cap Stab(Y) = C_W(c): %s; transport = conj by w on it: %s"
             % (d["orbit"], name_B(PI8, wg, 8), len(Y), affine_dim(Y), "pointwise stabilizer trivial" if stabY_trivial else "NOT spanning", cyc_type(c), len(CWc), stabY == CWc, conj_ok))
union_pred = set().union(*pred.values()) if pred else set()
check("BC4a", "Lemma B holds at n = 8 from every carrying orbit: Fix(c) has trivial pointwise stabilizer, I_8 cap Stab_W(Fix c) = C_W(c), and the transport there is conjugation by w", lemmaB_ok and bool(pred))
guess("BC4", "|I_8| > |C_8|, I_8 is exactly the Lemma-B prediction C_W(c) from a carrying orbit, and |I_8| / |C_8| = 2",
      len(I8) > len(C8) and any(I8 == P for P in pred.values()) and len(I8) == 2 * len(C8),
      "|I_8| = %d, |C_8| = %d, ratio %s; I_8 == C_W(c) for some carrying orbit: %s; I_8 == union of the predictions: %s"
      % (len(I8), len(C8), Fraction(len(I8), len(C8)) if C8 else None, any(I8 == P for P in pred.values()), I8 == union_pred))
# POST-REVEAL, labelled: the contrast with B4 by the same engine, the carrying element's u, and the nearest Weyl element
R4_B4 = perm_pow(Rb_B4, 4); O2_B4 = [o for o in perm_orbits(Rb_B4) if 0 not in o][0]; wB4 = weyl_agreeing(PERMS_B4, R4_B4, O2_B4)
assert len(wB4) == 1; wa4 = g_arr(PERMS_B4, wB4[0]); c4 = perm_inv(wa4)[R4_B4]; CWc4 = set(enum_commute(PERMS_B4, c4, 4))
note("B4 by the same engine: -tau = %s agrees with R^4 on O2; c = (-tau)^-1 R^4 has type %s, |C_W(c)| = %d (= |I_4|, SM-063)" % (name_B(PI_B4, wB4[0], 4), cyc_type(c4), len(CWc4)))
wg = carrying[0]["weyl"][0] if carrying else None
if wg is not None:
    pi_w = tuple(int(t) for t in PI8[wg[0]]); v_w = wg[1]; u_w = sum(((v_w >> pi_w[i]) & 1) << i for i in range(8))
    a8, n8 = best_agreement(PERMS8, R8)
    same_w = all(d["weyl"] == carrying[0]["weyl"] for d in carrying)
    note("the carrying element w = %s: v = %s (wt %d), u = pi^-1(v) = %s (wt %d); shift = %d - 2|x cap u| = +-1 iff |x cap u| in {%d, %d}; the SAME w carries every carrying orbit: %s"
         % (name_B(PI8, wg, 8), format(v_w, "08b")[::-1], PC[v_w], format(u_w, "08b")[::-1], PC[u_w], PC[u_w], (PC[u_w] - 1) // 2, (PC[u_w] + 1) // 2, same_w))
    note("nearest Weyl element to R^8 on the whole board: agreement %d/256 (altitude %d), attained by %d element(s); w's agreement set Fix(c) = %d points = the carrying orbits (%d) + %d more"
         % (a8, 256 - a8, n8, len(Y), 16 * len(carrying), len(Y) - 16 * len(carrying)))
    check("BC4b", "POST-REVEAL [C]: on B8 the carrying Weyl element is -(e2 e3)(e4 e5)(e6 e7) with e8 fixed -- the analogue of B4's -tau = -(e2 e3) with e4 fixed -- and it is the unique nearest Weyl element to R^8 (agreement 52 of 256); its correction c = w^-1 R^8 is NOT an involution (B4's is), and C_W(c) = {+-1}",
          name_B(PI8, wg, 8) == "(e1 -> -e1) (e2 -> -e3 -> e2) (e4 -> -e5 -> e4) (e6 -> -e7 -> e6)" and a8 == 52 and n8 == 1 and same_w
          and not np.array_equal(c[c], np.arange(256)) and cyc_type(c4) == "2^4 1^8" and len(CWc) == 2, "w = %s" % name_B(PI8, wg, 8))
    WIT["carrying_w"] = name_B(PI8, wg, 8); WIT["carrying_u"] = format(u_w, "08b")[::-1]; WIT["Fix_c"] = len(Y); WIT["c_type"] = cyc_type(c)
w0_orbit_map = {i + 1: orb_of[int(w0[o[0]])] + 1 for i, o in enumerate(ORB)}
note("w0 = -1 on the 16 orbits: fixes %s, swaps %s" % ([a for a, b in w0_orbit_map.items() if a == b], sorted({tuple(sorted((a, b))) for a, b in w0_orbit_map.items() if a != b})))
ordI = elem_orders(PERMS8, I8); ordC = elem_orders(PERMS8, C8)
ab = all(np.array_equal(g_arr(PERMS8, a)[g_arr(PERMS8, b)], g_arr(PERMS8, b)[g_arr(PERMS8, a)]) for a in I8 for b in I8)
note("I_8 element orders %s; C_8 element orders %s; I_8 abelian: %s" % (dict(sorted(ordI.items())), dict(sorted(ordC.items())), ab))
def orbit_action(g):
    a = g_arr(PERMS8, g); m = {orb_of[x]: orb_of[int(a[x])] for x in range(256)}
    if any(orb_of[int(a[x])] != m[orb_of[x]] for x in range(256)): return "mixes"
    return "preserves" if all(k == v for k, v in m.items()) else "permutes orbits " + str(sorted((k + 1, v + 1) for k, v in m.items() if k != v))
say("  C_8 (%d):" % len(C8))
for g in sorted(C8): say("    %-60s  [%s]" % (name_B(PI8, g, 8), orbit_action(g)))
say("  extras I_8 \\ C_8 (%d):" % len(extras))
for g in extras: say("    %-60s  transport -> %s  [%s]" % (name_B(PI8, g, 8), name_B(PI8, next(gg for gg in I8 if np.array_equal(g_arr(PERMS8, gg), R8i[g_arr(PERMS8, g)[R8]])), 8), orbit_action(g)))
WIT["C8"] = [name_B(PI8, g, 8) for g in sorted(C8)]; WIT["I8_extras"] = [name_B(PI8, g, 8) for g in extras]
WIT["sizes_B8_lag8"] = (len(I8), len(C8)); WIT["time_C8_I8"] = (t_c, t_i)
tick("BC4 done")

# ============================================================================ BC5 -- all lags on B8
banner("BC5 -- |I_k| vs |C_k| on B8 for k = 1..15")
t1 = time.time(); tab8 = lag_table(PERMS8, Rb8, is_B_linear, 8, [k for k in range(1, 16) if k != 8]); tab8[8] = (I8, C8); t_all = time.time() - t1
sizes8 = {k: (len(tab8[k][0]), len(tab8[k][1])) for k in range(1, 16)}
for k in range(1, 16): note("k = %2d  R^k type %-12s |I_k| = %4d  |C_k| = %4d  %s" % (k, cyc_type(perm_pow(Rb8, k)), sizes8[k][0], sizes8[k][1], "" if sizes8[k][0] == sizes8[k][1] else "<-- I_k != C_k"))
guess("BC5", "on B8, I_k = C_k as sets for every k != 8 (the anomaly is at the half-turn only)",
      all(tab8[k][0] == tab8[k][1] for k in range(1, 16) if k != 8), "sizes %s; wall %.0fs for the 14 other lags" % (sizes8, t_all))
WIT["sizes_B8"] = sizes8
tick("BC5 done")

# ============================================================================ BC6 -- D9
banner("BC6 -- the D9 half-spin: containment, the affine-fit method, then (disclosed tightening) full enumeration")
# (a) containment: the B8 extras and their transports are in W(B8) < W(D9), hence in I_8(D9)
inD = all(np.array_equal(R8i[g_arr(PERMS8, g)[R8]], g_arr(PERMS9, B_in_D(next(gg for gg in I8 if np.array_equal(g_arr(PERMS8, gg), R8i[g_arr(PERMS8, g)[R8]]))))) for g in I8)
check("BC6a", "containment: every element of I_8(B8) and its transport lie in W(B8) < W(D9), so I_8(B8) is contained in I_8(D9); for the B8 EXTRAS the statement is vacuous -- there are none (BC4). (The first run demanded extras and FAILED on that condition; _FIRSTRUN.log kept)", inD)
# (b) the affine-fit method: the nearest W(D9) element to R^k on the whole board, and to R^8 on each orbit
alt9 = {}; alt8 = {}
for k in range(1, 16):
    Rk = perm_pow(Rb8, k); a9, n9 = best_agreement(PERMS9, Rk); a8, n8 = best_agreement(PERMS8, Rk); alt9[k] = (256 - a9, n9); alt8[k] = (256 - a8, n8)
note("altitude of R^k (min disagreement over W, whole board) against W(D9): %s" % {k: v[0] for k, v in alt9.items()})
note("altitude of R^k against W(B8): %s" % {k: v[0] for k, v in alt8.items()})
fit9 = []
for i, O in enumerate(ORB):
    a9, n9 = best_agreement(PERMS9, R8, O); fit9.append(a9)
note("agreement of the nearest W(D9) element with R^8 per orbit: %s (against W(B8): %s)" % (fit9, [d["best_agreement"] for d in orbinfo]))
WIT["altitudes_D9"] = alt9; WIT["altitudes_B8"] = alt8; WIT["fit9_per_orbit"] = fit9
tick("BC6 affine fit done")
# (c) TIGHTENING, disclosed: with the (pi in S9, v) representation W(D9) IS enumerable (92,897,280 elements, cheap test then full
#     check); the brief asked for lemma-plus-sampling only.  Full I_k(D9), C_k(D9) at every lag.
t1 = time.time(); tab9 = lag_table(PERMS9, Rb8, is_D_linear, 8, range(1, 16)); t9 = time.time() - t1
sizes9 = {k: (len(tab9[k][0]), len(tab9[k][1])) for k in range(1, 16)}
for k in range(1, 16):
    I9, C9 = tab9[k]; ex = sorted(I9 - C9)
    note("D9 k = %2d  |I_k| = %4d  |C_k| = %4d  %s" % (k, len(I9), len(C9), "" if not ex else "<-- extras: " + "; ".join(name_D(PI9, g, 8) for g in ex[:8]) + (" ..." if len(ex) > 8 else "")))
extra_lags9 = [k for k in range(1, 16) if tab9[k][0] != tab9[k][1]]
coprime_extras = {k: sorted(tab9[k][0] - tab9[k][1]) for k in extra_lags9 if math.gcd(k, 16) == 1}
pure_perm = {k: [name_D(PI9, g, 8) for g in ex if g[1] == 0 and PI9[g[0]][8] != 8] for k, ex in coprime_extras.items()}
I8_9, C8_9 = tab9[8]
B8_extras_in_D9 = {B_in_D(g) for g in extras}
check("BC6c", "TIGHTENING [C, full enumeration of W(D9), %.0fs for 15 lags]: I_8(D9) contains the B8 extras; sizes at every lag recorded" % t9,
      B8_extras_in_D9 <= I8_9, "D9 sizes %s" % sizes9)
guess("BC6", "(low confidence) D9 carries at least one extra survivor at a lag coprime to 16 that is a pure coordinate permutation mixing the ninth axis in",
      any(pure_perm.values()), "lags with I_k != C_k on D9: %s; coprime-lag extras that are pure permutations moving e9: %s" % (extra_lags9, pure_perm))
note("C_8(D9) = I_8(D9) = {%s}" % ", ".join(name_D(PI9, g, 8) for g in sorted(I8_9)))
note("B8 extras (%d) inside I_8(D9) (%d): %s; I_8(D9) cap W(B8) = I_8(B8): %s" % (len(extras), len(I8_9), B8_extras_in_D9 <= I8_9,
     {g for g in I8_9 if PI9[g[0]][8] == 8} == {B_in_D(g) for g in I8}))
WIT["sizes_D9"] = sizes9; WIT["D9_extras"] = {k: [name_D(PI9, g, 8) for g in sorted(tab9[k][0] - tab9[k][1])] for k in extra_lags9}
tick("BC6 done")

# ============================================================================ BC7 -- B6, B7
banner("BC7 -- B6 (64, h = 12) and B7 (128, h = 14): |I_k| vs |C_k| at every lag")
res7 = {}
for n in (6, 7):
    Wn, idxn, Sn, Rnt, Pn, _ = B_spin(n); Rbn = rebase(Wn, Rnt, n); PIn, PERMSn = all_perm_arrays(n, n)
    tab = lag_table(PERMSn, Rbn, is_B_linear, n, range(1, 2 * n)); sz = {k: (len(tab[k][0]), len(tab[k][1])) for k in range(1, 2 * n)}
    clean = all(tab[k][0] == tab[k][1] for k in range(1, 2 * n)); res7[n] = (sz, clean, cyc_type(Rbn))
    note("B%d: R type %s; sizes %s; I_k = C_k at every lag: %s" % (n, cyc_type(Rbn), sz, clean))
guess("BC7", "on B6 and B7 (non-free clocks) I_k = C_k for every k -- the anomaly does not occur",
      res7[6][1] and res7[7][1], "B6 clean %s, B7 clean %s" % (res7[6][1], res7[7][1]))
for n in (6, 7):
    Wn, idxn, Sn, Rnt, Pn, _ = B_spin(n); Rbn = rebase(Wn, Rnt, n); PIn, PERMSn = all_perm_arrays(n, n)
    half = set(enum_commute(PERMSn, perm_pow(Rbn, n), n)); note("B%d half-turn survivors I_%d = C_%d = {%s}" % (n, n, n, ", ".join(name_B(PIn, g, n) for g in sorted(half))))
guess("BC7-law", "the brief's stated conjecture (sec 2, BC7): among the B_n spinors the shared grammar exceeds the centralizer at some lag iff n is a power of 2 (n >= 4) -- tested at its one new instance, n = 8",
      any(sizes8[k][0] > sizes8[k][1] for k in range(1, 16)), "B8: I_k = C_k at every lag (BC4, BC5); the 'if' direction fails at n = 8. Anomalous spinor boards among B3..B8: B4 (SM-060) and B3 by the overgroup W(D4) (SM-060) only")
WIT["sizes_B6"] = res7[6][0]; WIT["sizes_B7"] = res7[7][0]; WIT["types_B67"] = (res7[6][2], res7[7][2])
tick("BC7 done")

# ============================================================================ BC8 -- what distinguishes the carrying orbits
banner("BC8 [P + C] -- what distinguishes the carrying orbits (observation; promoted only if it proves)")
say("  orbit  lambda  ranks   affdim  |shift| multiset            #u  carrying  w0->")
for d in orbinfo:
    say("  O%-4d  %d       %d..%d    %d       %-26s %2d  %-5s     O%d" % (d["orbit"], d["has_lambda"], d["ranks"][0], d["ranks"][1], d["affine_dim"],
        dict(sorted(Counter(abs(k) for k, m in d["shifts"].items() for _ in range(m)).items())), len(d["us"]), d["carrying"], d["w0_image"]))
# candidate distinguishers, each tested on all 16 orbits
cand = {
    "carrying <=> some u reproduces the shift (rank-shift is necessary, not sufficient -- an observation)": all((len(d["us"]) > 0) == d["carrying"] for d in orbinfo),
    "carrying <=> affine extension of R^8|O has a permutation linear part (exact on affinely spanning orbits)": all(bool(d["linear_part_is_perm"]) == d["carrying"] for d in orbinfo),
    "carrying => all half-turn shifts have |shift| = 1 (as O2 on B4)": all(set(abs(k) for k in d["shifts"]) == {1} for d in carrying),
    "non-carrying => some |shift| >= 2": all(any(abs(k) >= 2 for k in d["shifts"]) for d in orbinfo if not d["carrying"]),
    "carrying orbits avoid ranks 0 and 8": all(d["ranks"][0] >= 1 and d["ranks"][1] <= 7 for d in carrying),
    "every orbit affinely spans F2^8": all(d["affine_dim"] == 8 for d in orbinfo),
    "|shift| = 1 on every point <=> carrying (both directions)": all((set(abs(k) for k in d["shifts"]) == {1}) == d["carrying"] for d in orbinfo),
    "carrying <=> the orbit's ranks lie in the middle band {n/2-1, n/2, n/2+1} = {3,4,5} (both directions)": all((d["ranks"][0] >= 3 and d["ranks"][1] <= 5) == d["carrying"] for d in orbinfo),
}
rk4 = {tuple(o): (int(min(PC[x] for x in o)), int(max(PC[x] for x in o))) for o in perm_orbits(Rb_B4)}
cand["the same band statement on B4: O2 (carrying) has ranks {1,2,3} = {n/2-1, n/2, n/2+1}, O1 has 0..4"] = sorted(rk4.values()) == [(0, 4), (1, 3)]
for k, v in cand.items(): note("%s: %s" % (k, v))
check("BC8", "[obs] the table of distinguishers is recorded for all 16 orbits; consistency: the enumeration's 'carrying' agrees with the affine-extension criterion (exact where the orbit affinely spans)",
      cand["carrying <=> affine extension of R^8|O has a permutation linear part (exact on affinely spanning orbits)"] or not all(d["affine_dim"] == 8 for d in orbinfo))
WIT["BC8_candidates"] = cand
tick("BC8 done")

# ============================================================================ witnesses, verdict
os.makedirs("_stone_bc_cache", exist_ok=True)
def _default(o):
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    if isinstance(o, (set, tuple)): return list(o)
    if isinstance(o, Fraction): return str(o)
    return str(o)
json.dump({str(k): v for k, v in WIT.items()}, open(os.path.join("_stone_bc_cache", "witnesses_bc.json"), "w"), indent=1, default=_default)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED (registered guesses INVERTED unless a bug is shown): " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
