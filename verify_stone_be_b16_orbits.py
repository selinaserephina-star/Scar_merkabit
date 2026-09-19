# -*- coding: utf-8 -*-
r"""verify_stone_be_b16_orbits.py -- STONE BE: THE 16-CUBE AT THE ORBIT LEVEL

Brief: BRIEF_STONE_BE_B16_ORBITS.md (lock BRIEF_STONE_BE_LOCK.sha256, re-verified as BE0).
BE1 the combinatorial rowmotion on the shifted staircase delta_n reproduces the sealed clocks of B4 and B8 (validation);
BE2 B16: 2048 free orbits of 32; BE3 O1 full-height, shift +-8, no u (Lemma BB-B, m = 8); BE4 MAIN: exactly two carrying
orbits, both by w = -(e2 e3)(e4 e5)...(e14 e15), e16 fixed, each preserved by -1, the band {7,8,9}; BE4b every orbit spans;
BE5 w not in C_W(R^16), c not an involution, Stab_W(Fix c) = <-1, w>, C_W(c) = {+-1}, hence I_16 cap Stab_W(Fix c) = {+-1}
(Lemma B); BE6 C_W(R^16) = {+-1}; BE7 [obs] |Fix c| and c's cycle type.  |I_16| is NOT computed and not claimed.

Machinery: Stone AV's e-coordinate board machine and Stone BC's rebase VERBATIM (for the validation only); NEW here:
rowmotion on J(delta_n) by bitsets over the n(n+1)/2 cells; the column method (a coordinate permutation matching given
vector pairs = a bijection between equal columns); backtracking searches for the set stabilizer of Y and for
centralizers in W(B16) = F2^16 x| S16, each leaf verified on all 65,536 points.  W(B16) is never enumerated.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED at equal prominence; no registry/git writes.
Not RH/GRH.  Rule 3.
Run:  python -X utf8 verify_stone_be_b16_orbits.py
"""
import os, sys, time, json, hashlib, itertools, math
from fractions import Fraction
from collections import Counter, defaultdict
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_be_b16_orbits.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE BE -- THE 16-CUBE AT THE ORBIT LEVEL"); say("=" * 78)
BRIEF = "BRIEF_STONE_BE_B16_ORBITS.md"; LOCK = open("BRIEF_STONE_BE_LOCK.sha256").read().split()[0]
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("BE0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_BE_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
WIT["brief_sha"] = sha

# ============================================================================ AV board machine + BC rebase, VERBATIM (validation only)
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
e = lambda i, n: tuple(Fraction(int(j == i)) for j in range(n))
def B_spin(n):  # all sign patterns; roots e_i - e_{i+1}, e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [e(n - 1, n)]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n)]
    return board(w, roots)
def bits_of(w): return sum(1 << i for i, s in enumerate(w) if s < 0)
def rebase(Wl, R, n):
    N = 1 << n; Rb = np.full(N, -1, dtype=np.int64)
    for i, w in enumerate(Wl): Rb[bits_of(w[:n])] = bits_of(Wl[R[i]][:n])
    assert sorted(Rb.tolist()) == list(range(N)); return Rb
def perm_pow(p, k):
    x = np.arange(len(p))
    for _ in range(k): x = p[x]
    return x
def perm_inv(p):
    r = np.empty_like(p); r[p] = np.arange(len(p)); return r
def cycle_lengths(p):
    N = len(p); seen = np.zeros(N, bool); out = []; p = np.asarray(p)
    for a in range(N):
        if seen[a]: continue
        L = 0; x = a
        while not seen[x]: seen[x] = True; L += 1; x = int(p[x])
        out.append(L)
    return out
def cyc_type_from_lengths(ls): return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(ls).items(), reverse=True))
def perm_orbits(p):
    N = len(p); seen = np.zeros(N, bool); out = []
    for a in range(N):
        if seen[a]: continue
        o = []; x = a
        while not seen[x]: seen[x] = True; o.append(x); x = int(p[x])
        out.append(o)
    return out

# ============================================================================ NEW: rowmotion on J(delta_n) by bitsets
def staircase_rowmotion(n):
    """rowmotion on the ideals of the shifted staircase delta_n, returned as a permutation of the 2^n sign patterns
       (bit i set iff coordinate i+1 negative); cells (k, c), 1 <= k <= c <= n, colour c; (k, c) covers (k, c+1) and (k-1, c-1);
       the ideal of the pattern with plus signs at c_1 < ... < c_r is {(k, c) : k <= r, c >= c_k}."""
    cells = [(k, c) for k in range(1, n + 1) for c in range(k, n + 1)]; idx = {cl: i for i, cl in enumerate(cells)}; M = len(cells)
    lower = [([idx[(k, c + 1)]] if c + 1 <= n else []) + ([idx[(k - 1, c - 1)]] if k >= 2 else []) for (k, c) in cells]
    DC = np.zeros((M, M), dtype=np.int64)
    for i in sorted(range(M), key=lambda i: (n - cells[i][1]) + (cells[i][0] - 1)):      # lower covers first
        DC[i, i] = 1
        for j in lower[i]: DC[i] |= DC[j]
    N = 1 << n; X = np.arange(N)
    # ideals: r(x) = number of plus signs; c_k(x) = position (1-based) of the k-th plus sign
    plus = [[p + 1 for p in range(n) if not (x >> p) & 1] for x in range(N)]
    I = np.zeros((N, M), dtype=bool)
    for i, (k, c) in enumerate(cells):
        ck = np.array([pl[k - 1] if len(pl) >= k else n + 1 for pl in plus]); I[:, i] = ck <= c
    # minimal elements of the complement: not in I, all lower covers in I
    cond = ~I
    for i in range(M):
        for j in lower[i]: cond[:, i] &= I[:, j]
    RI = (cond.astype(np.int64) @ DC) > 0                                            # the ideal generated by min(P \ I)
    # back to sign patterns: row k's threshold c_k = first cell of row k in RI
    out = np.full(N, (1 << n) - 1, dtype=np.int64)
    for k in range(1, n + 1):
        rowcells = [idx[(k, c)] for c in range(k, n + 1)]; sub = RI[:, rowcells]; has = sub.any(1); ck = k + sub.argmax(1)
        out[has] &= ~(1 << (ck[has] - 1))
    assert sorted(out.tolist()) == list(range(N)), "rowmotion is not a bijection"
    return out, M

# ============================================================================ NEW: the column method
def perms_matching(pairs, n):
    """all coordinate permutations pi with pi(a) = b for every (a, b) in pairs: the bijections between equal columns.
       returns (count, groups) where groups = list of (source columns, target columns) with equal column value."""
    colA = [sum(((a >> j) & 1) << p for p, (a, b) in enumerate(pairs)) for j in range(n)]
    colB = [sum(((b >> j) & 1) << p for p, (a, b) in enumerate(pairs)) for j in range(n)]
    gA = defaultdict(list); gB = defaultdict(list)
    for j in range(n): gA[colA[j]].append(j); gB[colB[j]].append(j)
    if sorted(map(len, gA.values())) != sorted(map(len, gB.values())) or set(gA) != set(gB) or any(len(gA[v]) != len(gB[v]) for v in gA): return 0, []
    groups = [(gA[v], gB[v]) for v in gA]
    return math.prod(math.factorial(len(s)) for s, t in groups), groups
def enumerate_perms(groups, n, cap=100000):
    """expand the bijection products (at most cap of them)."""
    out = []
    for choice in itertools.product(*[itertools.permutations(t) for s, t in groups]):
        pi = [None] * n
        for (s, t), tt in zip(groups, choice):
            for a, b in zip(s, tt): pi[a] = b
        out.append(tuple(pi))
        if len(out) >= cap: break
    return out
def apply_pi(pi, x, n): return sum(((x >> j) & 1) << pi[j] for j in range(n))
def apply_pi_arr(pi, X, n):
    out = np.zeros_like(X)
    for j in range(n): out |= ((X >> j) & 1) << pi[j]
    return out
def weyl_agreeing_on(O, f, n):
    """all (pi, v) in W with pi(x) ^ v == f[x] for every x in O (list); via the column method on the differences."""
    x0 = int(O[0]); pairs = [(int(x) ^ x0, int(f[x]) ^ int(f[x0])) for x in O[1:]]
    cnt, groups = perms_matching(pairs, n)
    if cnt == 0: return 0, []
    # every pi of the family agrees with f on O once v = f(x0) ^ pi(x0) (the pairs force the linear part); verified anyway when enumerated
    sols = []
    for pi in enumerate_perms(groups, n, cap=1000):
        v = int(f[x0]) ^ apply_pi(pi, x0, n)
        assert all(apply_pi(pi, int(x), n) ^ v == int(f[x]) for x in O), "column method inconsistent"
        sols.append((pi, v))
    return cnt, sols

# ============================================================================ NEW: backtracking searches in W(B_n)
def set_stabilizer(Y, n, PC):
    """all (pi, v) with pi(Y) ^ v == Y as sets.  v filtered by the rank histogram, pi by projection-multiset backtracking."""
    Y = np.array(sorted(int(y) for y in Y), dtype=np.int64); N = 1 << n; V = np.arange(N, dtype=np.int64)
    hist = np.sort(PC[Y]); cand = [int(v) for v in V[(np.sort(PC[Y[None, :] ^ V[:, None]], axis=1) == hist[None, :]).all(1)]]
    sols = []; Yset = set(Y.tolist())
    bitsY = [(Y >> j) & 1 for j in range(n)]
    for v in cand:
        Yv = Y ^ v; bitsYv = [(Yv >> j) & 1 for j in range(n)]
        # backtracking: assign pi(j) = t; keep projections projS (of Y on assigned source coords) and projT (of Yv on assigned targets)
        def rec(j, used, projS, projT, pi):
            if j == n:
                img = apply_pi_arr(pi, Y, n) ^ v
                if set(img.tolist()) == Yset: sols.append((tuple(pi), v))
                return
            for t in range(n):
                if used & (1 << t): continue
                pS = projS | (bitsY[j] << j); pT = projT | (bitsYv[t] << j)
                if np.array_equal(np.sort(pS), np.sort(pT)):
                    pi.append(t); rec(j + 1, used | (1 << t), pS, pT, pi); pi.pop()
        rec(0, 0, np.zeros(len(Y), np.int64), np.zeros(len(Y), np.int64), [])
    return sols, len(cand)
def centralizer_search(c, n, PC, N):
    """all (pi, v) in W(B_n) commuting with the permutation c of the 2^n patterns, by pair-propagation backtracking:
       g(0) = v pins g on the c-orbit of 0; each assignment pi(j) = t pins g(e_j) and hence g on the c-orbit of e_j."""
    V = np.arange(N, dtype=np.int64); ci = perm_inv(c)
    def orbit_pairs(x, y, v):
        """g(x) = y forces g(c^i x) = c^i y along the c-orbit of x; recorded as column-method pairs (c^i x, c^i y ^ v), i.e. pi(a) = b.
           FIRST RUN: the pairs were recorded as (a, g(a)) without removing v, so the column test rejected every g with v != 0
           (-1 among them); instrumentation, fixed; _FIRSTRUN.log kept."""
        out = []; a, b = x, y
        for _ in range(N):
            out.append((a, b ^ v)); a, b = int(c[a]), int(c[b])
            if a == x: break
        return out
    z0 = int(c[0]); cand = [int(v) for v in V[PC[c[V] ^ V] == PC[z0]]] if True else []
    sols = []; unit = [1 << j for j in range(n)]
    def consistent(pairs, pi, used):
        # assigned coordinates: bits must match; unassigned: column multisets must match
        colA = [0] * n; colB = [0] * n
        for p, (a, b) in enumerate(pairs):
            for j in range(n):
                colA[j] |= ((a >> j) & 1) << p; colB[j] |= ((b >> j) & 1) << p
        for j, t in enumerate(pi):
            if colA[j] != colB[t]: return False
        rest_s = sorted(colA[j] for j in range(len(pi), n)); rest_t = sorted(colB[t] for t in range(n) if not used & (1 << t))
        return rest_s == rest_t
    for v in cand:
        base = orbit_pairs(0, v, v)
        if not consistent(base, [], 0): continue
        def rec(j, used, pi, pairs):
            if j == n:
                g = apply_pi_arr(pi, V, n) ^ v
                if np.array_equal(g[c], c[g]): sols.append((tuple(pi), v))
                return
            for t in range(n):
                if used & (1 << t): continue
                newpairs = pairs + orbit_pairs(unit[j], unit[t] ^ v, v)
                if consistent(newpairs, pi + [t], used | (1 << t)): rec(j + 1, used | (1 << t), pi + [t], newpairs)
        rec(0, 0, [], base)
    return sols, len(cand)
def cycle_name(pi, v, n):
    seen = set(); parts = []
    for i in range(n):
        if i in seen: continue
        chain = []; s, j = 1, i
        while True:
            chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); seen.add(j)
            s = s * (-1 if (v >> pi[j]) & 1 else 1); j = pi[j]
            if j == i: chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); break
        if len(chain) == 2 and chain[0] == chain[1]: continue
        parts.append("(" + " -> ".join(chain) + ")")
    return " ".join(parts) if parts else "1"
def f2_rank(vecs):
    basis = []
    for v in vecs:
        v = int(v)
        for b in basis: v = min(v, v ^ b)
        if v: basis.append(v)
    return len(basis)
def affine_dim(pts): return f2_rank([int(p) ^ int(pts[0]) for p in pts])

# ============================================================================ BE1 -- validation of the combinatorial clock
banner("BE1 -- the combinatorial rowmotion on delta_n against the sealed clocks (B4, B8)")
ok1 = True; detail1 = {}
for n in (4, 8):
    Rc, M = staircase_rowmotion(n); Wn, idxn, Sn, Rnt, Pn, _ = B_spin(n); Rb = rebase(Wn, Rnt, n)
    detail1[n] = (bool(np.array_equal(Rc, Rb)), M, len(Pn)); ok1 &= detail1[n][0] and M == len(Pn)
t1 = time.time(); R16, M16 = staircase_rowmotion(16); t_build = time.time() - t1
h16 = next(k for k in range(1, 64) if np.array_equal(perm_pow(R16, k), np.arange(1 << 16)))
check("BE1", "the combinatorial rowmotion on J(delta_n) equals Stone AV's clock (as rebased in Stone BC) on B4 and B8, with |P| = 10 and 36; on delta_16 it is a permutation of the 65,536 patterns of order 32 with |P| = 136",
      ok1 and M16 == 136 and h16 == 32, "%s; B16 built in %.1fs, order %d" % (detail1, t_build, h16))
N = 1 << 16; n = 16; PC = np.array([bin(i).count("1") for i in range(N)], dtype=np.int64); X = np.arange(N, dtype=np.int64)
ONES = N - 1; w0 = X ^ ONES
assert np.array_equal(w0[R16[w0]], perm_inv(R16)), "w0 = -1 reverses R"
R8h = perm_pow(R16, 16); assert np.array_equal(R8h[R8h], X)   # the half-turn R^16 is an involution
tick("clock built and validated")

# ============================================================================ BE2 -- orbits
banner("BE2 -- the orbits of R on B16")
ORB = perm_orbits(R16); ORB.sort(key=min); orb_of = np.empty(N, dtype=np.int64)
for i, o in enumerate(ORB): orb_of[o] = i
ct = cyc_type_from_lengths([len(o) for o in ORB])
guess("BE2", "R acts freely on the 65,536 weights: 2,048 orbits of 32", ct == "32^2048", "type %s" % ct)
tick("orbits done")

# ============================================================================ BE3 -- O1
banner("BE3 -- O1: the full-height orbit, shift +-8, no u")
rank = PC; HT = R8h; shift = rank[HT] - rank
O1 = ORB[0]; assert O1[0] == 0
ranks1 = [int(rank[x]) for x in O1]; exp_f = [0] + [r for r in range(1, 16) for _ in (0, 1)] + [16]; exp_b = [0] + exp_f[1:][::-1]
def reproducing_us(O, chunk=8192):
    O = np.asarray(O, dtype=np.int64); target = shift[O]; found = []
    for s in range(0, N, chunk):
        U = X[s:s + chunk]
        ok = (PC[U][:, None] - 2 * PC[U[:, None] & O[None, :]] == target[None, :]).all(1)
        found.extend(int(u) for u in U[ok])
    return found
u1 = reproducing_us(O1); sh1 = sorted(set(int(shift[x]) for x in O1)); span1 = f2_rank(O1)
guess("BE3", "O1 is the full-height orbit (ranks 0,1,1,...,15,15,16 around the clock), R^16 shifts every rank on it by exactly +-8, O1 spans F2^16, and no u reproduces its shift (Lemma BB-B, m = 8)",
      ranks1 in (exp_f, exp_b) and sh1 == [-8, 8] and span1 == 16 and u1 == [], "ranks in R-order %s; shifts %s; span %d; u: %s" % (ranks1, sh1, span1, u1))
tick("BE3 done")

# ============================================================================ BE4 -- every orbit: band, shifts, u's, carrying
banner("BE4 -- every orbit: rank band, half-turn shifts, reproducing u's, carrying (column method)")
t1 = time.time(); info = []
for i, O in enumerate(ORB):
    rk = [int(rank[x]) for x in O]; sh = Counter(int(shift[x]) for x in O)
    cnt, sols = weyl_agreeing_on(O, HT, n)
    info.append(dict(orbit=i + 1, min=int(min(O)), rmin=min(rk), rmax=max(rk), shifts=dict(sorted(sh.items())), affdim=affine_dim(O),
                     n_pi=cnt, carrying=len(sols) > 0, weyl=[(list(p), v) for p, v in sols], names=[cycle_name(p, v, n) for p, v in sols],
                     w0_image=int(orb_of[int(w0[O[0]])]) + 1))
t_col = time.time() - t1
band = [d for d in info if d["rmin"] >= 7 and d["rmax"] <= 9]; carrying = [d for d in info if d["carrying"]]
# reproducing u's only where they could matter and for the record: band orbits + a sample; then all orbits (vectorised, ~1 min)
t1 = time.time(); nus = []
for d, O in zip(info, ORB): d["n_u"] = len(reproducing_us(O)); nus.append(d["n_u"])
t_u = time.time() - t1
say("  orbit  min    ranks   affdim  shifts                       #u  carrying  w0->   w")
for d in info:
    if d["carrying"] or d["rmin"] >= 6 or d["orbit"] <= 3:
        say("  O%-5d %5d  %2d..%-2d  %2d      %-28s %2d  %-5s     O%-5d %s" % (d["orbit"], d["min"], d["rmin"], d["rmax"], d["affdim"], d["shifts"], d["n_u"], d["carrying"], d["w0_image"], "; ".join(d["names"])))
note("(only the carrying orbits, the orbits with ranks >= 6 throughout, and O1..O3 are printed; all 2048 are in the witnesses file)")
exp_w = "(e1 -> -e1) " + " ".join("(e%d -> -e%d -> e%d)" % (k, k + 1, k) for k in range(2, 16, 2))
same_w = len(carrying) > 0 and all(d["names"] == carrying[0]["names"] for d in carrying) and len(carrying[0]["names"]) == 1
band_iff = all(((d["rmin"] >= 7 and d["rmax"] <= 9) == d["carrying"]) for d in info)
shift1_iff = all((set(d["shifts"]) <= {1, -1}) == d["carrying"] for d in info)
guess("BE4", "exactly two orbits carry the half-turn as a Weyl element, both by the same w = -(e2 e3)(e4 e5)...(e14 e15) with e16 fixed; each is preserved by -1; carrying <=> ranks in {7,8,9} <=> all shifts +-1",
      len(carrying) == 2 and same_w and carrying[0]["names"][0] == exp_w and all(d["w0_image"] == d["orbit"] for d in carrying) and band_iff and shift1_iff,
      "carrying orbits %s; w = %s; -1 maps them to %s; band iff carrying %s; shifts +-1 iff carrying %s; column method %.1fs, u-survey %.1fs"
      % ([d["orbit"] for d in carrying], carrying[0]["names"] if carrying else None, [d["w0_image"] for d in carrying], band_iff, shift1_iff, t_col, t_u))
guess("BE4b", "every orbit affinely spans F2^16 (so the Weyl element agreeing on a carrying orbit is unique)", all(d["affdim"] == 16 for d in info),
      "affine dimensions: %s" % dict(sorted(Counter(d["affdim"] for d in info).items())))
note("u-survey: orbits with a reproducing u: %d (%s); orbits in the band: %d" % (sum(1 for d in info if d["n_u"] > 0), [d["orbit"] for d in info if d["n_u"] > 0][:10], len(band)))
# POST-REVEAL, labelled: the parts of BE4 that hold, stated separately
w0map = {d["orbit"]: d["w0_image"] for d in carrying}
check("BE4c", "POST-REVEAL [C]: on B16 the carrying orbits number %d (B4: 1, B8: 2), ALL carried by the same w = -(e2 e3)(e4 e5)...(e14 e15) with e16 fixed; carrying <=> ranks in {7,8,9} <=> every half-turn shift is +-1 <=> some u reproduces the shift, on all 2048 orbits; every carrying orbit affinely spans; -1 fixes %d of them and swaps %d pairs"
      % (len(carrying), sum(1 for a, b in w0map.items() if a == b), sum(1 for a, b in w0map.items() if a < b)),
      len(carrying) > 0 and same_w and carrying[0]["names"][0] == exp_w and band_iff and shift1_iff and all((d["n_u"] > 0) == d["carrying"] for d in info) and all(d["affdim"] == 16 for d in carrying),
      "-1 on the carrying orbits: fixed %s, swapped %s" % ([a for a, b in w0map.items() if a == b], sorted((a, b) for a, b in w0map.items() if a < b)))
WIT["carrying_orbits"] = [d["orbit"] for d in carrying]; WIT["w0_on_carrying"] = w0map
WIT["orbits"] = info
tick("BE4 done")

# ============================================================================ BE5 -- the criterion's negative case on B16
banner("BE5 -- w, the correction c, Fix(c), Stab_W(Fix c), C_W(c), Lemma B")
if carrying:
    pi_w, v_w = carrying[0]["weyl"][0]; pi_w = tuple(pi_w); wa = apply_pi_arr(pi_w, X, n) ^ v_w; wi = perm_inv(wa); c = wi[HT]
    Y = [int(x) for x in np.flatnonzero(c == X)]; c_inv = bool(np.array_equal(c[c], X)); w_in_C = bool(np.array_equal(wa[HT], HT[wa]))
    RwR = bool(np.array_equal(HT[wa[HT]], wi)); ctype = cyc_type_from_lengths(cycle_lengths(c)); Ydim = affine_dim(Y)
    t1 = time.time(); stab, ncand = set_stabilizer(Y, n, PC); t_stab = time.time() - t1
    CWc = [g for g in stab if np.array_equal((apply_pi_arr(g[0], X, n) ^ g[1])[c], c[apply_pi_arr(g[0], X, n) ^ g[1]])]
    stab_names = sorted(cycle_name(p, v, n) for p, v in stab); CWc_names = sorted(cycle_name(p, v, n) for p, v in CWc)
    note("w = %s; w involution: %s; w in C_W(R^16): %s; R^16 w R^16 = w^-1: %s; c = w^-1 R^16: type %s, involution %s; |Fix c| = %d (affine dim %d)"
         % (carrying[0]["names"][0], bool(np.array_equal(wa[wa], X)), w_in_C, RwR, ctype, c_inv, len(Y), Ydim))
    note("Stab_W(Fix c) (%d v-candidates after the rank-histogram filter, %.1fs): %d elements: %s" % (ncand, t_stab, len(stab), stab_names))
    note("C_W(c) = %d elements: %s" % (len(CWc), CWc_names))
    exp_stab = sorted(["1", cycle_name(tuple(range(n)), ONES, n), carrying[0]["names"][0], cycle_name(pi_w, v_w ^ ONES, n)])
    guess("BE5", "w does not commute with R^16 (so c is not an involution, Lemma BD-A), Fix(c) affinely spans, Stab_W(Fix c) = <-1, w> of order 4, C_W(c) = {+-1}, hence by Lemma B I_16 cap Stab_W(Fix c) = {+-1}",
          (not w_in_C) and (not c_inv) and Ydim == 16 and stab_names == exp_stab and CWc_names == sorted(["1", cycle_name(tuple(range(n)), ONES, n)]),
          "|Stab| = %d, |C_W(c)| = %d" % (len(stab), len(CWc)))
    WIT["BE5"] = dict(w=carrying[0]["names"][0], w_in_C=w_in_C, c_type=ctype, c_inv=c_inv, FixY=len(Y), Ydim=Ydim, stab=stab_names, CWc=CWc_names, t_stab=t_stab, ncand=ncand)
    check("BE7", "[obs] |Fix c| = %d of 65,536 (%.2f%%; B4: 8/16 = 50%%, B8: 52/256 = 20.3%%); Fix c = the %d carrying orbits (%d points) + %d further points; c has cycle type %s" % (len(Y), 100.0 * len(Y) / N, len(carrying), 32 * len(carrying), len(Y) - 32 * len(carrying), ctype), True)
else:
    check("BE5", "no carrying orbit found -- BE5 not applicable", False); check("BE7", "not applicable", False)
tick("BE5 done")

# ============================================================================ BE6 -- C_W(R^16)
banner("BE6 -- C_W(R^16) by pair-propagation backtracking")
t1 = time.time(); C16, ncand16 = centralizer_search(HT, n, PC, N); t_c16 = time.time() - t1
C16_names = sorted(cycle_name(p, v, n) for p, v in C16)
guess("BE6", "C_W(R^16) = {+-1}", C16_names == sorted(["1", cycle_name(tuple(range(n)), ONES, n)]), "%d elements (%d v-candidates, %.1fs): %s" % (len(C16), ncand16, t_c16, C16_names))
WIT["C16"] = C16_names; WIT["t_c16"] = t_c16
# cross-check of the search engine on B8 (where Stone BC enumerated): C_W(R^8) = {+-1} and the B8 stabilizer of the 52-point set = <-1, w> (SM-068)
R8c, _ = staircase_rowmotion(8); PC8 = np.array([bin(i).count("1") for i in range(256)], dtype=np.int64); H8 = perm_pow(R8c, 8)
C8s, _ = centralizer_search(H8, 8, PC8, 256)
O8 = perm_orbits(R8c); car8 = [O for O in O8 if weyl_agreeing_on(O, H8, 8)[1]]
pi8, v8 = weyl_agreeing_on(car8[0], H8, 8)[1][0]; wa8 = apply_pi_arr(pi8, np.arange(256), 8) ^ v8; c8 = perm_inv(wa8)[H8]; Y8 = [int(x) for x in np.flatnonzero(c8 == np.arange(256))]
stab8, _ = set_stabilizer(Y8, 8, PC8); CWc8 = [g for g in stab8 if np.array_equal((apply_pi_arr(g[0], np.arange(256), 8) ^ g[1])[c8], c8[apply_pi_arr(g[0], np.arange(256), 8) ^ g[1]])]
check("BE6-engine", "the backtracking searches reproduce Stone BC/BD's enumerated answers on B8: C_W(R^8) = {+-1}, |Stab_W(Fix c)| = 4, C_W(c) = {+-1}, two carrying orbits with w = -(e2 e3)(e4 e5)(e6 e7)",
      len(C8s) == 2 and len(stab8) == 4 and len(CWc8) == 2 and len(car8) == 2 and cycle_name(pi8, v8, 8) == "(e1 -> -e1) (e2 -> -e3 -> e2) (e4 -> -e5 -> e4) (e6 -> -e7 -> e6)")
tick("BE6 done")

# ============================================================================ witnesses, verdict
os.makedirs("_stone_be_cache", exist_ok=True)
def _default(o):
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    if isinstance(o, (set, tuple)): return list(o)
    return str(o)
json.dump({str(k): v for k, v in WIT.items()}, open(os.path.join("_stone_be_cache", "witnesses_be.json"), "w"), indent=1, default=_default)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED (registered guesses INVERTED unless a bug is shown): " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
