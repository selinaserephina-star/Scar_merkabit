# -*- coding: utf-8 -*-
r"""verify_stone_ae_his_chain.py -- STONE AE: HIS CHAIN IN THE HOUSE'S STILL POINT

Brief: BRIEF_STONE_AE_HIS_CHAIN_IN_OUR_G22.md (lock BRIEF_STONE_AE_LOCK.sha256, re-verified as check AE0).

Question: reproduce every number of IB's AXIS_SPIRAL_CHAIN_VERIFICATION.md
(GAP on PrimitiveGroup(63,2)) inside the house's OWN G2(2) -- the sealed
still point of SM-038, _stone_z_cache/G_rows.npy (12096 permutations of
the 120 nonsingular vectors; READ-ONLY; if absent run
verify_stone_z_stillpoint.py first, this run never regenerates it) -- and
test the line his script did not compute: do the two S4 classes of
PSL(2,7) fuse in G2(2)?

BARS: AE0a the model; AE1 his section 1 (36 copies, one class, N = 336, H
= PSL(2,7) by explicit iso); AE2 his section 2 (14 S4's, two H-classes of
7, N_H = S4, N_G = C2xS4 of order 48, G-class 252); AE2b REGISTERED: the
two H-classes FUSE in G (one G-class of 252 meets H in all 14) -- his
"504 copies / 2 classes" double-counts; AE3 his section 3 (A4, same);
AE4 his section 4 (Z2: N_A4 = C2xC2, N_S4 = N_H = D8, |N_G| = 192, class
21 in H / 63 in G; N_G(Z2) = the stabilizer of one Pauli = SM-040's 192);
AE5 the chain as containments; AE6 each S4 = the H-stabilizer of one
theta, the two H-classes <-> the two 7-orbits of [1,7,7,21].

Machinery: F2 / E8-mask replay VERBATIM from verify_stone_ab_merkabit.py;
perm helpers + closure VERBATIM from verify_stone_z_stillpoint.py; group
class + explicit-iso identifier VERBATIM from verify_blind_engine.py
(library extended by one model C2xS4 built with direct_gens).

DISCIPLINE: compute, never assert; registered expectations resolvable
INVERTED at equal prominence; exact arithmetic; sealed caches READ-ONLY;
no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ae_his_chain.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from itertools import product as iproduct
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_ae_his_chain.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))

say("=" * 78); say("STONE AE -- HIS CHAIN IN THE HOUSE'S STILL POINT (reciprocal audit of the axis-spiral package)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AE_HIS_CHAIN_IN_OUR_G22.md"; LOCK = open("BRIEF_STONE_AE_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AE0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AE_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# =====================================================================
# VERBATIM from verify_blind_engine.py (SM-026), lines 40-483
# =====================================================================
# permutation helpers
# ----------------------------------------------------------------------------
def pmul(p, q):                      # (p*q)(i) = p[q[i]]  (apply q, then p)
    return tuple(p[q[i]] for i in range(len(p)))

def pid(n):
    return tuple(range(n))

def closure_perms(gens, n):
    e = pid(n)
    elems = {e}
    frontier = [e]
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = pmul(a, g)
                if b not in elems:
                    elems.add(b)
                    new.append(b)
        frontier = new
    return elems

# ----------------------------------------------------------------------------
# table-based Group
# ----------------------------------------------------------------------------
class Group:
    def __init__(self, mul, e):
        self.k = len(mul)
        self.mul = mul
        self.e = e
        self.inv = [None] * self.k
        for i in range(self.k):
            for j in range(self.k):
                if mul[i][j] == e:
                    self.inv[i] = j
                    break
        self.order = []
        for i in range(self.k):
            o, x = 1, i
            while x != e:
                x = mul[x][i]
                o += 1
            self.order.append(o)
        self._gens = None
        self._fp = None
        self._subs = None

    @staticmethod
    def from_perms(perms):
        elems = sorted(perms)
        n = len(elems[0])
        e = pid(n)
        elems = [e] + [x for x in elems if x != e]
        idx = {x: i for i, x in enumerate(elems)}
        mul = [[idx[pmul(a, b)] for b in elems] for a in elems]
        return Group(mul, 0)

    @staticmethod
    def from_gens(gens, n):
        return Group.from_perms(closure_perms([tuple(g) for g in gens], n))

    def close(self, gens):
        elems = {self.e}
        frontier = [self.e]
        mul = self.mul
        while frontier:
            new = []
            for a in frontier:
                for g in gens:
                    b = mul[a][g]
                    if b not in elems:
                        elems.add(b)
                        new.append(b)
            frontier = new
        return elems

    def small_gens(self):
        if self._gens is not None:
            return self._gens
        gens = []
        cur = {self.e}
        for x in sorted(range(self.k), key=lambda i: -self.order[i]):
            if x not in cur:
                gens.append(x)
                cur = self.close(gens)
                if len(cur) == self.k:
                    break
        self._gens = gens
        return gens

    def conj(self, g, x):             # g x g^-1
        return self.mul[self.mul[g][x]][self.inv[g]]

    def is_abelian(self):
        m = self.mul
        for a in range(self.k):
            for b in range(a + 1, self.k):
                if m[a][b] != m[b][a]:
                    return False
        return True

    def center_size(self):
        m = self.mul
        c = 0
        for a in range(self.k):
            if all(m[a][b] == m[b][a] for b in range(self.k)):
                c += 1
        return c

    def conj_class_sizes(self):
        gens = self.small_gens()
        seen = [False] * self.k
        sizes = []
        for x in range(self.k):
            if seen[x]:
                continue
            orb = {x}
            fr = [x]
            while fr:
                nf = []
                for y in fr:
                    for g in gens:
                        z = self.conj(g, y)
                        if z not in orb:
                            orb.add(z)
                            nf.append(z)
                fr = nf
            for y in orb:
                seen[y] = True
            sizes.append(len(orb))
        return tuple(sorted(sizes))

    def derived_subgroup(self):
        m, iv = self.mul, self.inv
        comms = set()
        for a in range(self.k):
            for b in range(self.k):
                comms.add(m[m[iv[a]][iv[b]]][m[a][b]])
        return frozenset(self.close(list(comms)))

    def fingerprint(self):
        if self._fp is None:
            self._fp = (self.k,
                        tuple(sorted(self.order)),
                        self.is_abelian(),
                        self.center_size(),
                        self.conj_class_sizes(),
                        len(self.derived_subgroup()))
        return self._fp

    # -- full subgroup enumeration -------------------------------------------
    def all_subgroups(self):
        """Return dict frozenset(indices) -> generating list.  Complete:
        every subgroup is generated by cyclic subgroups; BFS from the trivial
        subgroup adding one cyclic generator at a time reaches all of them."""
        if self._subs is not None:
            return self._subs
        cyc = {}
        for x in range(self.k):
            s = frozenset(self.close([x]))
            if len(s) > 1 and s not in cyc:
                cyc[s] = x
        cyc_list = list(cyc.items())
        subs = {frozenset([self.e]): []}
        frontier = [(frozenset([self.e]), [])]
        while frontier:
            new = []
            for (s, gens) in frontier:
                for (cs, x) in cyc_list:
                    if x in s:
                        continue
                    g2 = gens + [x]
                    s2 = frozenset(self.close(g2))
                    if s2 not in subs:
                        subs[s2] = g2
                        new.append((s2, g2))
            frontier = new
        self._subs = subs
        return subs

    def subgroup_conj_classes(self):
        """List of (representative, orbit_set) over all subgroups."""
        subs = self.all_subgroups()
        gens = self.small_gens()
        classes = []
        seen = set()
        for s in sorted(subs, key=lambda t: (len(t), sorted(t))):
            if s in seen:
                continue
            orb = {s}
            fr = [s]
            while fr:
                nf = []
                for t in fr:
                    for g in gens:
                        tg = frozenset(self.conj(g, x) for x in t)
                        if tg not in orb:
                            orb.add(tg)
                            nf.append(tg)
                fr = nf
            seen |= orb
            classes.append((s, orb))
        return classes

    def is_normal(self, s):
        for g in self.small_gens():
            for x in s:
                if self.conj(g, x) not in s:
                    return False
        return True

def subgroup_group(G, s):
    loc = sorted(s)
    pos = {x: i for i, x in enumerate(loc)}
    mul = [[pos[G.mul[a][b]] for b in loc] for a in loc]
    return Group(mul, pos[G.e])

def quotient_group(G, N):
    """G/N for N normal (caller guarantees normality)."""
    coset_of = {}
    reps = []
    for x in range(G.k):
        if x in coset_of:
            continue
        cs = frozenset(G.mul[x][n] for n in N)
        ci = len(reps)
        reps.append(x)
        for y in cs:
            coset_of[y] = ci
    mul = [[coset_of[G.mul[reps[a]][reps[b]]] for b in range(len(reps))]
           for a in range(len(reps))]
    return Group(mul, coset_of[G.e])

# ----------------------------------------------------------------------------
# isomorphism testing (explicit generator-image backtracking)
# ----------------------------------------------------------------------------
def find_iso(A, B):
    """Return an explicit isomorphism dict A-index -> B-index, or None.
    Method: choose a small generating set of A; try every image tuple in B
    with matching element orders; propagate the map by BFS over A multiplying
    by generators; any conflict kills the candidate.  Conflict-free + total +
    injective  =>  isomorphism (hom property on (a, gen) pairs extends to all
    products by induction on word length)."""
    if A.k != B.k:
        return None
    if A.fingerprint() != B.fingerprint():
        return None
    gens = A.small_gens()
    if not gens:                      # trivial group
        return {A.e: B.e}
    cands = [[y for y in range(B.k) if B.order[y] == A.order[g]] for g in gens]
    for images in iproduct(*cands):
        phi = {A.e: B.e}
        frontier = [A.e]
        gi = list(zip(gens, images))
        ok = True
        while frontier and ok:
            new = []
            for a in frontier:
                b = phi[a]
                for (g, h) in gi:
                    a2 = A.mul[a][g]
                    b2 = B.mul[b][h]
                    if a2 in phi:
                        if phi[a2] != b2:
                            ok = False
                            break
                    else:
                        phi[a2] = b2
                        new.append(a2)
                if not ok:
                    break
            frontier = new
        if ok and len(phi) == A.k and len(set(phi.values())) == A.k:
            return phi
    return None

# ----------------------------------------------------------------------------
# reference constructions (library used ONLY to attach standard names to
# computed iso classes; each identification is verified by an explicit iso)
# ----------------------------------------------------------------------------
def cyclic_perm(n):
    if n == 1:
        return [pid(1)], 1
    return [tuple(list(range(1, n)) + [0])], n

def dihedral_gens(n):
    rot = tuple(list(range(1, n)) + [0])
    ref = tuple((n - i) % n for i in range(n))
    return [rot, ref], n

def direct_gens(parts):
    """parts: list of (gens, degree) -> gens of direct product on disjoint pts."""
    total = sum(d for _, d in parts)
    gens = []
    off = 0
    for (gs, d) in parts:
        for g in gs:
            p = list(range(total))
            for i in range(d):
                p[off + i] = off + g[i]
            gens.append(tuple(p))
        off += d
    return gens, total

def mat2perms(mats, p):
    """2x2 matrices over F_p acting on the p^2-1 nonzero column vectors."""
    vecs = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
    idx = {v: i for i, v in enumerate(vecs)}
    perms = []
    for M in mats:
        (a, b), (c, d) = M
        perms.append(tuple(idx[((a * v[0] + b * v[1]) % p,
                                (c * v[0] + d * v[1]) % p)] for v in vecs))
    return perms, len(vecs)

def affine_gens(p, mult):
    """x -> x+1 and x -> mult*x on F_p (Frobenius-type group)."""
    add = tuple((i + 1) % p for i in range(p))
    mu = tuple((mult * i) % p for i in range(p))
    return [add, mu], p

def dic3_gens():
    # a = (0 1 2), b = (1 2)(3 4 5 6):  b a b^-1 = a^-1, b^2 central of order 2
    a = (1, 2, 0, 3, 4, 5, 6)
    b = (0, 2, 1, 4, 5, 6, 3)
    return [a, b], 7

def psl27_gens():
    # Moebius maps on P1(F7) = {0..6, 7=inf}:  S: z->z+1,  T: z->-1/z
    S = (1, 2, 3, 4, 5, 6, 0, 7)
    T = (7, 6, 3, 2, 5, 4, 1, 0)
    return [S, T], 8

_LIB = None
def nonabelian_library():
    global _LIB
    if _LIB is not None:
        return _LIB
    lib = {}
    def add(name, gens, n):
        G = Group.from_gens(gens, n)
        lib.setdefault(G.k, []).append((name, G))
    add("S3", *dihedral_gens(3))
    add("D4", *dihedral_gens(4))                      # dihedral of order 8
    add("Q8", *mat2perms([(((0, 2), (1, 0))), ((1, 1), (1, 2))], 3))
    add("D5", *dihedral_gens(5))                      # dihedral of order 10
    g, n = cyclic_perm(3)
    a4 = [(1, 2, 0, 3), (1, 0, 3, 2)]
    add("A4", a4, 4)
    add("D6", *dihedral_gens(6))                      # order 12
    add("Dic3", *dic3_gens())                         # order 12
    add("D7", *dihedral_gens(7))                      # order 14
    add("F20", *affine_gens(5, 2))                    # order 20
    add("F21", *affine_gens(7, 2))                    # order 21
    add("S4", [(1, 2, 3, 0), (1, 0, 2, 3)], 4)
    add("SL(2,3)", *mat2perms([((1, 1), (0, 1)), ((0, 2), (1, 0))], 3))
    add("D12", *dihedral_gens(12))                    # order 24
    add("C2xA4", *direct_gens([([(1, 0)], 2), (a4, 4)]))
    add("A5", [(1, 2, 3, 4, 0), (1, 2, 0, 3, 4)], 5)
    add("PSL(2,7)", *psl27_gens())
    _LIB = lib
    return lib

# ----------------------------------------------------------------------------
# abelian structure from raw order statistics (then verified by explicit iso)
# ----------------------------------------------------------------------------
def factorize(n):
    fac = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac

def abelian_invariant_factors(H):
    """Invariant factors d1 >= d2 >= ... (each dividing the previous) computed
    purely from the multiset of element orders."""
    n = H.k
    if n == 1:
        return []
    fac = factorize(n)
    primary = {}
    for p, a in fac.items():
        e_prev = 0
        m = []
        for kk in range(1, a + 1):
            cnt = sum(1 for o in H.order if (p ** kk) % o == 0)
            e_k = 0
            c = cnt
            while c > 1:
                c //= p
                e_k += 1
            m.append(e_k - e_prev)
            e_prev = e_k
        lam = []
        top = m[0] if m else 0
        for i in range(1, top + 1):
            lam.append(sum(1 for mk in m if mk >= i))
        # lam is the partition (descending) of a
        primary[p] = sorted(lam, reverse=True)
    width = max(len(v) for v in primary.values())
    ds = []
    for j in range(width):
        d = 1
        for p, lam in primary.items():
            if j < len(lam):
                d *= p ** lam[j]
        ds.append(d)
    return ds

VERIFIED_ABELIAN = {}
def abelian_name_and_verify(H):
    ds = abelian_invariant_factors(H)
    if not ds:
        return "1", True
    name = "x".join("C%d" % d for d in ds)
    key = tuple(ds)
    if key in VERIFIED_ABELIAN:
        return name, VERIFIED_ABELIAN[key]
    parts = [(cyclic_perm(d)) for d in ds]
    gens, n = direct_gens(parts)
    model = Group.from_gens(gens, n)
    ok = find_iso(H, model) is not None
    VERIFIED_ABELIAN[key] = ok
    return name, ok

def identify(H, verify_log=None):
    """Name the iso type of table-group H.  Returns (name, verified_bool)."""
    if H.k == 1:
        return "1", True
    if H.is_abelian():
        return abelian_name_and_verify(H)
    for (nm, R) in nonabelian_library().get(H.k, []):
        if H.fingerprint() == R.fingerprint():
            if find_iso(H, R) is not None:
                return nm, True
    return ("NONAB%d[fp=%s]" % (H.k, str(H.fingerprint())[:60]), False)


# =====================================================================
# VERBATIM from verify_stone_z_stillpoint.py, lines 84-113 (perm helpers)
# =====================================================================
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

# =====================================================================
# VERBATIM from verify_stone_ab_merkabit.py: mvec (96-102), f2_rank (128-135),
# the E8-mask replay, qvals, NONSING, perm_of / mat_of_perm (257-320)
# =====================================================================
def mvec(M, x):
    y = 0
    while x:
        b = x & -x
        y ^= M[b.bit_length() - 1]
        x ^= b
    return y
def f2_rank(masks):
    basis = []
    for m in masks:
        for b in basis:
            m = min(m, m ^ b)
        if m:
            basis.append(m); basis.sort(reverse=True)
    return len(basis)
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

# =====================================================================
# STONE AE stages
# =====================================================================
CACHE_Z = "_stone_z_cache"; CACHE_AE = "_stone_ae_cache"; os.makedirs(CACHE_AE, exist_ok=True)
random.seed(20260905)
banner("AE0 -- the model: the house G2(2) on the 120 nonsingular vectors")
zf = os.path.join(CACHE_Z, "G_rows.npy")
assert os.path.exists(zf), "sealed cache absent: run verify_stone_z_stillpoint.py first (never regenerated here)"
G_rows = np.load(zf); gsha = hashlib.sha256(open(zf, "rb").read()).hexdigest()
note("G_rows.npy sha256 %s, shape %s" % (gsha, G_rows.shape))
n = G_rows.shape[0]
G_list = [tuple(int(x) for x in r) for r in G_rows]
G_set = set(G_list)
ident = tuple(range(120))
ALPHA = rmask[ridx[SIMPLE[0]]]; IV = NS_IDX[ALPHA]
closed = all(pmul(G_list[random.randrange(n)], G_list[random.randrange(n)]) in G_set for _ in range(2000))
fixes_v = bool((G_rows[:, IV] == IV).all())
check("AE0a", "G_rows: 12096 distinct permutations, identity present, closed under 2000 random products, every element fixes v",
      n == 12096 and len(G_set) == 12096 and ident in G_set and closed and fixes_v)
ORD = Counter(pord(g) for g in G_list)
note("element-order census of G: %s" % dict(sorted(ORD.items())))

banner("AE1 -- his section 1: PSL(2,7) copies at the still point")
invs = [g for g in G_list if pord(g) == 2]; thr = [g for g in G_list if pord(g) == 3]
copies = []; copy_gens = []
for a in invs:
    for b in thr:
        ab = pmul(a, b)
        if pord(ab) != 7: continue
        if pord(comm(a, b)) != 4: continue
        if any(a in L and b in L for L in copies): continue
        L = closure([a, b], cap=200)
        if len(L) != 168: continue
        copies.append(frozenset(L)); copy_gens.append((a, b))
tick("(2,3,7)+[a,b]^4 scan: %d copies" % len(copies))
# generators of G (random, verified by closure size)
while True:
    Ggens = [G_list[random.randrange(n)] for _ in range(3)]
    if len(closure(Ggens, cap=13000)) == 12096: break
def conj_set(L, g):
    gi = pinv(g)
    return frozenset(pmul(pmul(g, x), gi) for x in L)
orb = {copies[0]}; fr = [copies[0]]
while fr:
    X = fr.pop()
    for g in Ggens:
        Y = conj_set(X, g)
        if Y not in orb: orb.add(Y); fr.append(Y)
L0 = copies[0]; a0, b0 = copy_gens[0]
NL = [g for g in G_list if pmul(pmul(g, a0), pinv(g)) in L0 and pmul(pmul(g, b0), pinv(g)) in L0]
H = Group.from_perms(L0)
Helems = sorted(L0); Helems = [ident] + [x for x in Helems if x != ident]      # the from_perms element order
hname, hver = identify(H)
check("AE1", "REGISTERED: 36 copies of order 168, ONE G-class (orbit of the first copy has 36 members and contains all copies), "
      "|N_G(H)| = 336 = |PGL(2,7)|; H is PSL(2,7) by explicit isomorphism to the Moebius model -- his 'order-168 subgroup classes = 1'",
      len(copies) == 36 and len(orb) == 36 and all(L in orb for L in copies) and len(NL) == 336 and hname == "PSL(2,7)" and hver,
      "copies %d, orbit %d, |N_G| %d, H = %s" % (len(copies), len(orb), len(NL), hname))
N_H_set = frozenset(NL)

# ---- helpers on the big group (numpy, vectorised)
GINV = np.argsort(G_rows, axis=1).astype(np.uint8)          # ginv[r] = inverse permutation of row r
def conj_rows(s):
    """array n x 120: g s g^-1 for every row g."""
    s = np.asarray(s, dtype=np.uint8)
    return np.take_along_axis(G_rows, s[GINV], axis=1)
def rows_key(A): return [r.tobytes() for r in np.ascontiguousarray(A, dtype=np.uint8)]
def normalizer_in_G(S_set, gens):
    """rows g with g S g^-1 = S (tested on generators of S)."""
    keys = set(np.array(s, dtype=np.uint8).tobytes() for s in S_set)
    ok = np.ones(n, dtype=bool)
    for s in gens:
        ck = rows_key(conj_rows(s)); ok &= np.array([k in keys for k in ck])
    return [G_list[i] for i in np.nonzero(ok)[0]]
def G_orbit_of_subgroup(S_list):
    """the set of G-conjugates of S (as frozensets of bytes), vectorised."""
    conjs = [rows_key(conj_rows(s)) for s in S_list]        # list over s of lists over g
    return set(frozenset(conjs[j][i] for j in range(len(S_list))) for i in range(n))
def fs_bytes(S): return frozenset(np.array(s, dtype=np.uint8).tobytes() for s in S)
def sub_perms(idxset): return [Helems[i] for i in idxset]
def gens_of(S_list):
    """two generators of a subgroup given as perms (small search)."""
    for a in S_list:
        for b in S_list:
            if len(closure([a, b], cap=len(S_list) + 1)) == len(S_list): return [a, b]
    return list(S_list)
def normalizer_in(Sub_list, S_set):
    return [h for h in Sub_list if all(pmul(pmul(h, s), pinv(h)) in S_set for s in S_set)]
def ident_of(perms):
    return identify(Group.from_perms(set(perms)))
# library extension: C2 x S4 model (built with direct_gens, identified by explicit iso)
LIB = nonabelian_library()
_c2s4 = Group.from_gens(*direct_gens([([(1, 0)], 2), ([(1, 2, 3, 0), (1, 0, 2, 3)], 4)]))
LIB.setdefault(48, []).append(("C2xS4", _c2s4))

banner("AE2 -- his section 2: the S4's of H, their normalizers, and the fusion test")
subsH = H.all_subgroups(); classesH = H.subgroup_conj_classes()
S4_idx = [s for s in subsH if len(s) == 24]
S4_classes = [(rep, o) for rep, o in classesH if len(rep) == 24]
S4_types = [identify(subgroup_group(H, s)) for s in S4_idx]
note("|H| = %d: %d subgroups, %d classes; order-24 subgroups: %d in %d H-classes of sizes %s; types %s"
     % (H.k, len(subsH), len(classesH), len(S4_idx), len(S4_classes), [len(o) for _, o in S4_classes], Counter(t for t, v in S4_types)))
rowsS = []
for ci, (rep, o) in enumerate(S4_classes):
    for s in sorted(o, key=lambda t: sorted(t)):
        Sp = sub_perms(s); Sset = set(Sp); g2 = gens_of(Sp)
        NH = normalizer_in(Helems, Sset); NG = normalizer_in_G(Sset, g2)
        ngname, ngver = ident_of(NG)
        rowsS.append((ci, s, Sp, len(NH), len(NG), ngname, ngver))
ok2 = (len(S4_idx) == 14 and len(S4_classes) == 2 and all(len(o) == 7 for _, o in S4_classes)
       and all(t == "S4" and v for t, v in S4_types)
       and all(r[3] == 24 and r[4] == 48 and r[5] == "C2xS4" and r[6] for r in rowsS))
check("AE2", "REGISTERED: 14 S4's in H (explicit iso), two H-classes of 7; for every one N_H(S4) = S4 (24), N_G(S4) = C2xS4 (48, explicit iso), "
      "G-class length 12096/48 = 252 -- his section 2 line by line", ok2,
      "N_H orders %s, N_G orders %s, N_G types %s" % (sorted(set(r[3] for r in rowsS)), sorted(set(r[4] for r in rowsS)), sorted(set(r[5] for r in rowsS))))
# fusion
S_first = rowsS[0][2]
orbit1 = G_orbit_of_subgroup(S_first)
all14 = [fs_bytes(r[2]) for r in rowsS]
in_orbit = [fs in orbit1 for fs in all14]
class2_in = [in_orbit[i] for i, r in enumerate(rowsS) if r[0] == 1]
note("G-orbit of one S4 has %d members; of the 14 S4's of H, %d lie in it (class 1: %d/7, class 2: %d/7)"
     % (len(orbit1), sum(in_orbit), sum(in_orbit[:7]), sum(class2_in)))
fused = (len(orbit1) == 252 and all(in_orbit))
if fused:
    check("AE2b", "REGISTERED EXPECTATION CONFIRMED: the two H-classes of S4 are FUSED in G -- ONE G-class of 252 S4's contains all 14 S4's of H "
          "(N_G(H) = PGL(2,7) swaps the classes); his 'Total S4 copies = 504, Total S4 classes = 2' double-counts: the S4's of G meeting H are one class of 252", True)
else:
    check("AE2b", "REGISTERED EXPECTATION INVERTED (full prominence): the two H-classes of S4 stay DISTINCT in G -- his '504 copies / 2 classes' stands", False,
          "orbit %d, in-orbit %s" % (len(orbit1), in_orbit))
# does an element of N_G(H) \ H swap the two classes?  (the mechanism, measured)
outer = [g for g in NL if g not in L0]
sw = sum(1 for g in outer if fs_bytes(conj_set(set(S_first), g)) in set(fs_bytes(r[2]) for r in rowsS if r[0] == 1))
note("[measured] of the %d elements of N_G(H) outside H, %d conjugate a class-1 S4 into class 2" % (len(outer), sw))

banner("AE3 -- his section 3: the A4's")
rowsA = []
for r in rowsS:
    Sg = Group.from_perms(set(r[2])); Selems = sorted(set(r[2])); Selems = [ident] + [x for x in Selems if x != ident]
    subsS = Sg.all_subgroups(); A_idx = [s for s in subsS if len(s) == 12]
    assert len(A_idx) == 1
    Ap = [Selems[i] for i in A_idx[0]]; Aset = set(Ap); g2 = gens_of(Ap)
    aname, aver = ident_of(Ap)
    NS4 = normalizer_in(Selems, Aset); NH = normalizer_in(Helems, Aset); NG = normalizer_in_G(Aset, g2)
    ngname, ngver = ident_of(NG)
    rowsA.append((r[0], Ap, aname, aver, len(NS4), len(NH), len(NG), ngname, ngver))
ok3 = all(a[2] == "A4" and a[3] and a[4] == 24 and a[5] == 24 and a[6] == 48 and a[7] == "C2xS4" and a[8] for a in rowsA)
check("AE3", "REGISTERED: each S4 has exactly one A4 (explicit iso); N_S4(A4) = S4, N_H(A4) = S4 (24), N_G(A4) = C2xS4 (48), G-class 252 -- his section 3",
      ok3 and len(rowsA) == 14)
orbitA = G_orbit_of_subgroup(rowsA[0][1])
inA = [fs_bytes(a[1]) in orbitA for a in rowsA]
fusedA = (len(orbitA) == 252 and all(inA))
check("AE3b", "REGISTERED: the two H-classes of A4 FUSE in G (one G-class of 252 contains all 14)" if fusedA else
      "REGISTERED EXPECTATION INVERTED: the two H-classes of A4 stay distinct in G", fusedA, "orbit %d, in-orbit %d/14" % (len(orbitA), sum(inA)))

banner("AE4 -- his section 4: the Z2 in the fixed A4")
A0 = rowsA[0][1]; A0set = set(A0)
Ag = Group.from_perms(A0set); Aelems = sorted(A0set); Aelems = [ident] + [x for x in Aelems if x != ident]
A_invs = [x for x in A0 if pord(x) == 2]
A_cls = [(rep, o) for rep, o in Ag.subgroup_conj_classes() if len(rep) == 2]
z = A_invs[0]; Z = {ident, z}
S0 = rowsS[0][2]; S0elems = sorted(set(S0)); S0elems = [ident] + [x for x in S0elems if x != ident]
NA = normalizer_in(Aelems, Z); NS = normalizer_in(S0elems, Z); NH = normalizer_in(Helems, Z); NG = normalizer_in_G(Z, [z])
na, ns, nh, ng = ident_of(NA), ident_of(NS), ident_of(NH), None
cl_H = len(set(fs_bytes(conj_set(Z, h)) for h in Helems)); cl_G = 12096 // len(NG)
note("involutions in A4: %d, forming %d A4-class(es); N_A4 = %s (%d), N_S4 = %s (%d), N_H = %s (%d), |N_G| = %d; class length %d in H, %d in G"
     % (len(A_invs), len(A_cls), na[0], len(NA), ns[0], len(NS), nh[0], len(NH), len(NG), cl_H, cl_G))
ok4 = (len(A_invs) == 3 and len(A_cls) == 1 and na == ("C2xC2", True) and ns[0] == "D4" and ns[1] and nh[0] == "D4" and nh[1]
       and len(NA) == 4 and len(NS) == 8 and len(NH) == 8 and len(NG) == 192 and cl_H == 21 and cl_G == 63)
check("AE4", "REGISTERED: one A4-class of 3 involutions; N_A4(Z2) = C2xC2 (4), N_S4(Z2) = D8 (8), N_H(Z2) = D8 (8), |N_G(Z2)| = 192; "
      "class length 21 in H and 63 in G -- his section 4 (D8 = the engine's 'D4', dihedral of order 8)", ok4)
# the Pauli
PAULI_IDX = [NS_IDX[u] for u in NONSING if u != ALPHA and Bform(u, ALPHA) == 0]
BOARD_IDX = [NS_IDX[u] for u in NONSING if Bform(u, ALPHA) == 1]
fixedP = [i for i in PAULI_IDX if z[i] == i]
zclass = set(rows_key(conj_rows(z)))
tabZ = json.load(open(os.path.join(CACHE_Z, "witnesses_z.json")))["involution_table"]
note("z fixes %d of the 63 Paulis and %d of the 56 board points; its G-class has %d elements (SM-038 involution table rows: %s)"
     % (len(fixedP), sum(1 for i in BOARD_IDX if z[i] == i), len(zclass), [r[0] for r in tabZ]))
if len(fixedP) == 1:
    u = fixedP[0]
    stab_u = [G_list[i] for i in np.nonzero(G_rows[:, u] == u)[0]]
    same = (set(stab_u) == set(NG))
    check("AE4b", "REGISTERED: z is an inner involution (class of 63 = SM-038's 63-class); N_G(Z2) = C_G(z) fixes exactly ONE Pauli u and "
          "EQUALS Stab_G(u) (order %d) -- SM-040's 192 (AB3a/AB5b) read from his chain" % len(stab_u),
          len(zclass) == 63 and same and len(stab_u) == 192)
else:
    check("AE4b", "REGISTERED EXPECTATION INVERTED: z fixes %d Paulis, not one -- N_G(Z2) is not a single Pauli stabilizer" % len(fixedP), False)
ordN = Counter(pord(g) for g in NG)
note("[obs] element-order census of N_G(Z2) (his '(SL(2,3):C4):C2'): %s; centre size %d; derived subgroup order %d"
     % (dict(sorted(ordN.items())), Group.from_perms(set(NG)).center_size(), len(Group.from_perms(set(NG)).derived_subgroup())))

banner("AE5 -- the chain as containments in one model")
chain = [({ident}, 1), (Z, 2), (A0set, 12), (set(S0), 24), (set(L0), 168), (G_set, 12096)]
ok5 = all(len(c) == o for c, o in chain) and all(chain[i][0] < chain[i + 1][0] for i in range(5))
check("AE5", "{e} < Z2 < A4 < S4 < PSL(2,7) < G2(2) as actual subsets of one permutation group, orders 1, 2, 12, 24, 168, 12096; N_G({e}) = G", ok5)

banner("AE6 -- the chain meets the still point's geometry: S4 = the stabilizer of a theta")
SINGV = [x for x in range(1, 256) if qvals[x] == 0 and Bform(x, ALPHA) == 1]
THETAS = sorted({frozenset((x, x ^ ALPHA)) for x in SINGV}); TIDX = {t: i for i, t in enumerate(THETAS)}
def mat_of(p): return mat_of_perm(p)
def act_theta(M, t):
    x = next(iter(t)); y = mvec(M, x); return frozenset((y, y ^ ALPHA))
Hmats = {h: mat_of(h) for h in Helems}
assert all(is_isometry(M) and mvec(M, ALPHA) == ALPHA for M in Hmats.values())
def orbits_theta(perms):
    seen = set(); sizes = []
    for t in THETAS:
        if t in seen: continue
        o = {t}; fr = [t]
        while fr:
            x = fr.pop()
            for p in perms:
                y = act_theta(Hmats[p], x)
                if y not in o: o.add(y); fr.append(y)
        seen |= o; sizes.append(sorted(TIDX[x] for x in o))
    return sizes
Horb = orbits_theta([a0, b0])
note("H on the 36 thetas: orbit sizes %s" % sorted(len(o) for o in Horb))
sevens = [set(o) for o in Horb if len(o) == 7]
fixed_by = []
for r in rowsS:
    fx = [TIDX[t] for t in THETAS if all(act_theta(Hmats[s], t) == t for s in r[2])]
    fixed_by.append((r[0], fx))
c1 = sorted(f[1][0] for f in fixed_by if f[0] == 0 and len(f[1]) == 1)
c2 = sorted(f[1][0] for f in fixed_by if f[0] == 1 and len(f[1]) == 1)
ok6 = (len(SINGV) == 72 and len(THETAS) == 36 and sorted(len(o) for o in Horb) == [1, 7, 7, 21] and len(sevens) == 2
       and all(len(f[1]) == 1 for f in fixed_by)
       and ((set(c1) == sevens[0] and set(c2) == sevens[1]) or (set(c1) == sevens[1] and set(c2) == sevens[0])))
check("AE6", "REGISTERED: H has orbits [1,7,7,21] on the 36 even thetas; every S4 of H fixes exactly one theta; the seven S4's of one H-class "
      "fix the seven thetas of one 7-orbit and the other class the other 7-orbit -- his 'S4 = point stabilizer of the 7-point action', on the board",
      ok6, "fixed thetas: class 1 %s, class 2 %s" % (c1, c2))

# =====================================================================
# POST-REVEAL CHECKS (findings, not amendments; the first-run log is kept
# as verify_stone_ae_his_chain_FIRSTRUN.log).  AE4b as instrumented tested
# whether z itself fixes one Pauli (it fixes 15); the brief's sentence is
# about N_G(Z2).  AE6 as instrumented demanded exactly one fixed theta per
# S4, forgetting the theta of the size-1 orbit, fixed by all of H.
# =====================================================================
banner("AE4c -- POST-REVEAL: the 192 of his chain against SM-040's 192 (the Pauli stabilizer)")
fixN = [i for i in PAULI_IDX if all(g[i] == i for g in NG)]
note("Paulis fixed by ALL of N_G(Z2) = C_G(z): %d" % len(fixN))
u0 = PAULI_IDX[0]; stab0 = [G_list[i] for i in np.nonzero(G_rows[:, u0] == u0)[0]]
GN = Group.from_perms(set(NG)); GS = Group.from_perms(set(stab0))
fpN, fpS = GN.fingerprint(), GS.fingerprint()
note("fingerprint (order, element orders, abelian?, |centre|, conjugacy-class sizes, |derived|):")
note("  N_G(Z2) : %s" % (fpN,))
note("  Stab(u) : %s" % (fpS,))
NGelems = sorted(set(NG)); NGelems = [ident] + [x for x in NGelems if x != ident]
gensN = [NGelems[i] for i in GN.small_gens()]
stabkeys = set(np.array(x, dtype=np.uint8).tobytes() for x in stab0)
okc = np.ones(n, dtype=bool)
for sgen in gensN:
    ck = rows_key(conj_rows(sgen)); okc &= np.array([k in stabkeys for k in ck])
conjugate = bool(okc.any())
note("conjugating the %d generators of N_G(Z2) by every g in G: %d elements g carry N_G(Z2) into Stab(u)" % (len(gensN), int(okc.sum())))
if (not conjugate) and len(stab0) == 192:
    check("AE4c", "POST-REVEAL FINDING: N_G(Z2) = C_G(z) (order 192) is NOT conjugate to the stabilizer of a Pauli (order 192, SM-040's 192) -- "
          "the still point has two different 192's: his chain's (an involution centralizer, fingerprint %s) and the hexagon-point stabilizer "
          "(fingerprint %s); isomorphic: %s" % ("as above", "as above", "fingerprints agree" if fpN == fpS else "NO (fingerprints differ)"), True)
else:
    check("AE4c", "POST-REVEAL: N_G(Z2) IS conjugate to a Pauli stabilizer (the brief's AE4b holds after all, only z's own fixed set was misread)",
          conjugate and len(fixN) >= 1)

banner("AE6b -- POST-REVEAL: the H-fixed theta excluded")
one_idx = [TIDX[t] for t in THETAS if all(act_theta(Hmats[h], t) == t for h in (a0, b0))]
note("thetas fixed by all of H: %s (the size-1 orbit)" % one_idx)
fixed_by2 = [(ci, [x for x in fx if x not in one_idx]) for ci, fx in fixed_by]
d1 = sorted(f[1][0] for f in fixed_by2 if f[0] == 0 and len(f[1]) == 1)
d2 = sorted(f[1][0] for f in fixed_by2 if f[0] == 1 and len(f[1]) == 1)
ok6b = (len(one_idx) == 1 and all(len(f[1]) == 1 for f in fixed_by2) and len(sevens) == 2
        and ((set(d1) == sevens[0] and set(d2) == sevens[1]) or (set(d1) == sevens[1] and set(d2) == sevens[0])))
check("AE6b", "POST-REVEAL: every S4 of H fixes the H-fixed theta AND exactly one further theta; the seven S4's of one H-class fix the seven "
      "thetas of one 7-orbit, the other class the other 7-orbit -- his 'S4 = point stabilizer of the 7-point action', located on the board "
      "(AE6 as instrumented failed only by counting the H-fixed theta)", ok6b, "class 1 %s, class 2 %s" % (d1, d2))

json.dump({"G_rows_sha256": gsha, "copies": len(copies), "N_G_H": len(NL), "S4_orbit": len(orbit1), "A4_orbit": len(orbitA),
           "N_G_Z2": len(NG), "fixed_pauli_index": fixedP, "theta_orbits": sorted(len(o) for o in Horb),
           "brief_sha": sha}, open(os.path.join(CACHE_AE, "witnesses_ae.json"), "w"), indent=1)

banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done")
LOG.close()
