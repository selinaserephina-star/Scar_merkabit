# -*- coding: utf-8 -*-
r"""verify_stone_ad_forced_narrowing.py -- STONE AD: THE FORCED-NARROWING TABLE

Brief: BRIEF_STONE_AD_FORCED_NARROWING.md (lock BRIEF_STONE_AD_LOCK.sha256, re-verified as check AD0).

Question: IB's table (PROMPT "Subgroup Diversity Along the Descent" +
ADDENDUM "Forced Narrowing as the Compression Mechanism", 2026-09-02;
repeated 2026-09-03): per spine level L7..L1 = PSL(2,7), C6xC2, A5, S4,
A4, C2, {e}: #subgroups, #conjugacy classes, #maximal, #normal; then his
two decision rules applied mechanically.  L6 = C6xC2 as his prompt says;
alternative L6 labels NOT tested here.

BARS: AD1 the seven groups from raw generators; AD2 the SM-026 census
reproduced (179/10/59/30/10/2/1; 15/10/9/11/5/2/1); AD3 maximal counts
22/4/21/8/5/1/0 with class breakdown; AD4 normal counts 2/10/2/4/3/2/1;
AD5a his diversity rule; AD5b his forced-narrowing rule; AD6 [obs].

Machinery: the SM-026 engine VERBATIM (lines 40-483 of
verify_blind_engine.py); pure Python; no caches.

DISCIPLINE: compute, never assert; registered expectations resolvable
INVERTED at equal prominence; exact arithmetic; sealed caches READ-ONLY;
no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ad_forced_narrowing.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from itertools import product as iproduct
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_ad_forced_narrowing.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AD -- THE FORCED-NARROWING TABLE (IB's subgroup-diversity prompt + addendum)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AD_FORCED_NARROWING.md"; LOCK = open("BRIEF_STONE_AD_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AD0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AD_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

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
# STONE AD stages
# =====================================================================
banner("AD1 -- the seven spine groups from raw generators (verbatim SM-026)")
G_PSL = Group.from_gens(*psl27_gens())
G_C6C2 = Group.from_gens(*direct_gens([(cyclic_perm(6)), (cyclic_perm(2))]))
G_A5 = Group.from_gens([(1, 2, 3, 4, 0), (1, 2, 0, 3, 4)], 5)
G_S4 = Group.from_gens([(1, 2, 3, 0), (1, 0, 2, 3)], 4)
G_A4 = Group.from_gens([(1, 2, 0, 3), (1, 0, 3, 2)], 4)
G_C2 = Group.from_gens([(1, 0)], 2)
G_E = Group.from_perms({(0,)})
LEVELS = [(7, "PSL(2,7)", G_PSL), (6, "C6xC2", G_C6C2), (5, "A5", G_A5), (4, "S4", G_S4),
          (3, "A4", G_A4), (2, "C2", G_C2), (1, "{e}", G_E)]
orders = [G.k for _, _, G in LEVELS]
nm6, ok6 = identify(G_C6C2)
check("AD1", "orders 168/12/60/24/12/2/1 from raw generators; the order-12 abelian input is C6xC2 by explicit isomorphism",
      orders == [168, 12, 60, 24, 12, 2, 1] and nm6 == "C6xC2" and ok6, "orders %s, L6 = %s" % (orders, nm6))
has6 = any(o == 6 for o in G_C6C2.order); has6psl = any(o == 6 for o in G_PSL.order)
check("AD1b", "the spine groups are NOT nested as subgroups: C6xC2 has an element of order 6 and PSL(2,7) has none, so "
      "'lost subgroups' below is a count difference, not a loss", has6 and not has6psl)

banner("AD2-AD4 -- the table: subgroups, classes, maximal, normal")
TABLE = []
for lev, name, G in LEVELS:
    subs = G.all_subgroups()
    classes = G.subgroup_conj_classes()
    proper = [s for s in subs if len(s) < G.k]
    maximal = [s for s in proper if not any(len(t) > len(s) and len(t) % len(s) == 0 and s < t for t in proper)]
    normal = [rep for rep, orb in classes if len(orb) == 1 and G.is_normal(rep)]
    # class breakdown of the maximal subgroups by iso type
    maxset = set(maximal); brk = Counter()
    for rep, orb in classes:
        if rep in maxset:
            tname, ver = identify(subgroup_group(G, rep))
            assert ver, (name, tname)
            brk[(len(rep), tname, len(orb))] += 1
    brk_s = ", ".join("%s x%d" % (t, n) for (o, t, n), c in sorted(brk.items()))
    TABLE.append((lev, name, G.k, len(subs), len(classes), len(maximal), len(normal), brk_s))
say("  level | |G|  | #subgroups | #conj classes | #maximal | #normal | maximal classes (type x conjugates)")
for row in TABLE:
    say("  %5d | %-4d | %10d | %13d | %8d | %7d | %s" % (row[0], row[2], row[3], row[4], row[5], row[6], row[7]))
NS = [r[3] for r in TABLE]; NC = [r[4] for r in TABLE]; NM = [r[5] for r in TABLE]; NN = [r[6] for r in TABLE]
check("AD2", "REGISTERED: the SM-026 census reproduced: #subgroups 179/10/59/30/10/2/1, #conj classes 15/10/9/11/5/2/1",
      NS == [179, 10, 59, 30, 10, 2, 1] and NC == [15, 10, 9, 11, 5, 2, 1], "%s ; %s" % (NS, NC))
check("AD3", "REGISTERED EXPECTATION: maximal subgroup counts 22/4/21/8/5/1/0 (breakdown above)",
      NM == [22, 4, 21, 8, 5, 1, 0], NM)
check("AD4", "REGISTERED EXPECTATION: normal subgroup counts 2/10/2/4/3/2/1", NN == [2, 10, 2, 4, 3, 2, 1], NN)

banner("AD5 -- his two decision rules, applied mechanically")
mono_s = all(NS[i] > NS[i + 1] for i in range(6)); mono_c = all(NC[i] > NC[i + 1] for i in range(6))
ups_s = [(TABLE[i][0], TABLE[i + 1][0], NS[i], NS[i + 1]) for i in range(6) if NS[i + 1] > NS[i]]
ups_c = [(TABLE[i][0], TABLE[i + 1][0], NC[i], NC[i + 1]) for i in range(6) if NC[i + 1] > NC[i]]
note("subgroup count increases at: %s ; class count increases at: %s" % (ups_s, ups_c))
check("AD5a", "REGISTERED: his diversity rule -- NEITHER column is monotone decreasing (subgroups up at 6->5, classes up at 5->4): "
      "'diversity narrowing' NOT SUPPORTED as stated, by his own rule",
      (not mono_s) and (not mono_c) and ups_s == [(6, 5, 10, 59)] and ups_c == [(5, 4, 9, 11)])
DIFF = [NS[i] - NS[i + 1] for i in range(6)]
MAG = [24, 128, 4, -2, 4, 9]          # his transition magnitudes, as given [I]
TR = ["7->6", "6->5", "5->4", "4->3", "3->2", "2->1"]
say("  transition | #subgroups(n) - #subgroups(n-1) | his magnitude [I]")
for t, d, m in zip(TR, DIFF, MAG): say("  %-10s | %31d | %d" % (t, d, m))
i_maxd = DIFF.index(max(DIFF)); i_maxm = MAG.index(max(MAG))
i_mind = DIFF.index(min(DIFF)); i_minm = MAG.index(min(m for m in MAG if m > 0)); i_rev = MAG.index(min(MAG))
note("largest difference at %s (%d); his largest magnitude at %s (%d)" % (TR[i_maxd], DIFF[i_maxd], TR[i_maxm], MAG[i_maxm]))
note("smallest difference at %s (%d); his smallest magnitude at %s (%d); his reversing transition %s (%d)"
     % (TR[i_mind], DIFF[i_mind], TR[i_minm], MAG[i_minm], TR[i_rev], MAG[i_rev]))
clause1 = (i_maxd == i_maxm); clause2 = (i_mind in (i_minm, i_rev))
check("AD5b", "REGISTERED: his forced-narrowing rule -- clause 1 (largest loss at largest compression) %s, clause 2 (smallest loss at "
      "smallest-or-reversing transition) %s: both fail -> the mechanism is REFUTED by his own rule (not 'ambiguous')"
      % ("holds" if clause1 else "fails", "holds" if clause2 else "fails"),
      DIFF == [169, -49, 29, 20, 8, 1] and (not clause1) and (not clause2))

banner("AD6 -- [obs] only")
def ranks(v):
    s = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]: j += 1
        for k in range(i, j + 1): r[s[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
rd, rm = ranks(DIFF), ranks(MAG); n = 6
md, mm = sum(rd) / n, sum(rm) / n
rho = sum((a - md) * (b - mm) for a, b in zip(rd, rm)) / (sum((a - md) ** 2 for a in rd) * sum((b - mm) ** 2 for b in rm)) ** 0.5
note("[obs] maximal column %s monotone; normal column %s monotone" % ("IS" if all(NM[i] > NM[i+1] for i in range(6)) else "NOT",
     "IS" if all(NN[i] > NN[i+1] for i in range(6)) else "NOT"))
note("[obs] Spearman rank correlation (average ranks, 6 points) between count difference and his magnitude: %.3f" % rho)
json.dump({"table": TABLE, "diff": DIFF, "mag": MAG, "spearman": rho}, open("_stone_ad_cache/table.json", "w"), indent=1)

banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done")
LOG.close()
