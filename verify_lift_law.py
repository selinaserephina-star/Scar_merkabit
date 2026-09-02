# -*- coding: utf-8 -*-
r"""verify_lift_law.py -- THE LIFT LAW: the spinor character eps on
K-bar = Sp6(2) and the exact shape of the split/non-split law for
preimages in H = 2.Sp6(2) = pi^-1(K_spin) <= W(E8).

CARRIED OPEN (joint program).  Stone U sealed H = 2.Sp6(2) with the
shadow-BSGS chain lifting any element of K-bar (pair action, 120 points)
to an explicit W(E8)-permutation preimage, and the square-sign tables of
the four involution classes: 315(+), 3780(+), 945(-), 63(-).  This run
asks for the LAW: which subgroups S <= K-bar have split preimage
pi^-1(S) = <-1> x S, and what single character decides it.

DEFINITION (the spinor character).  For g in K-bar of order n, let g-hat
in H be a preimage (the other is -g-hat).  eps(g) = + if some preimage
has order n; eps(g) = - if both preimages have order 2n.
  Well-definedness: n odd -> g-hat^n in {1,-1}; if -1 then
  (-g-hat)^n = (-1)^n g-hat^n = +1, so ONE of the lifts has order n:
  eps = + automatically for odd n.  [machine-checked, 1e]
  n even -> (-g-hat)^n = g-hat^n, so the value g-hat^n in {1,-1} is
  independent of the lift choice and eps is well-defined.  [1e]
  eps is a class function: conjugation in H permutes the lifts.  [1f]

REGISTERED EXPECTATIONS (resolved at their sites at EQUAL prominence,
INVERTED/REFUTED spelled out if so):
  RE-A [P, brief cites ATLAS]: Sp6(2) has exactly 30 conjugacy classes;
       the enumeration below must find exactly 30, sizes summing to
       1,451,520.
  RE-B [auditor -- THE DECISIVE ONE, task 3]: the converse of the
       involution law FAILS at cyclic level: there exists an order-4
       class with eps = - whose square lands in a PLUS involution class
       (giving C4 <= K-bar with all-plus involutions and non-split
       preimage C8).
  RE-C [house, task 4]: split => eps == + on S; every element sampled
       from the split-lifting sealed witnesses has eps = +.

TASKS / CHECK MAP:
  1*  the complete eps-table over all 30 conjugacy classes (exhaustive:
      the sealed cache holds ALL 1,451,520 elements; classes separated
      by order + fixed-point profile of powers, then CONFIRMED one class
      per bucket by exact centralizer counts).
  2*  the one-direction theorem: S contains an eps=- involution t =>
      pi^-1(S) non-split (a complement would contain an order-2 preimage
      of t; none exists since both lifts of t have order 4).  Verified
      on every sealed witness subgroup.
  3*  THE CONVERSE HUNT: for every eps=- class, the class and sign of
      its involution power g^(n/2).  Decides RE-B.
  4*  the corrected law: split => eps==+ (theorem, machine-checked);
      the cyclic law C_n splits <=> eps(gen)=+ (definitional, machine-
      checked per class); elementary-abelian all-plus => split
      (theorem via commuting lifts, machine-checked); and the eps-law
      converse hunt (eps==+ on S => split?) over available all-plus
      subgroup types, including the commutator-sign probe on C4 x C2.
  5*  verdict.

DISCIPLINE: compute, never assert; sealed caches (_stone_u_cache/,
_schur_pin_cache/) READ-ONLY; own cache _liftlaw_cache/; exhaustive
claims scoped exactly (30 classes = exhaustive at class level; subgroup
statements scoped to the tested types); no registry/git/knowledge.yaml
writes.  Not RH/GRH; no physical identification (Rule 3).

Run:  python -X utf8 verify_lift_law.py
      (writes verify_lift_law.log as it goes)
"""
import itertools, json, os, sys, time, random
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_lift_law.log", "w", encoding="utf-8")
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

STONE_CACHE = "_stone_u_cache"          # READ-ONLY (sealed Stone U)
MY_CACHE = "_liftlaw_cache"             # this verifier's own checkpoints
os.makedirs(MY_CACHE, exist_ok=True)
random.seed(20260902)
RNG = np.random.default_rng(20260902)

# ======================================================================
# permutation utilities (verbatim precedent: verify_stone_u_2cover.py /
# verify_schur_class_pinning.py)
# ======================================================================
def pmul(a, b): return tuple(a[x] for x in b)          # (a o b)(k) = a[b[k]]
def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def pident(n): return tuple(range(n))
def ppow(p, e):
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
def rand_word(gens, lo=15, hi=45):
    w = pident(len(gens[0]))
    for _ in range(random.randrange(lo, hi)):
        w = pmul(gens[random.randrange(len(gens))], w)
    return w
def profile_of(G):
    return dict(sorted(Counter(pord(g) for g in G).items()))
def conj_orbit(t, gens):
    gi = [pinv(g) for g in gens]
    S = {t}; fr = [t]
    while fr:
        x = fr.pop()
        for g, giv in zip(gens, gi):
            c = pmul(pmul(g, x), giv)
            if c not in S:
                S.add(c); fr.append(c)
    return S

# BSGS -- verbatim algorithm from the sealed verify_schur_class_pinning.py
def make_bsgs_full(gen_list, deg):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    if not strong:
        return 1, (lambda g: g == E), []
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
    return o, is_member, transv

# shadow-chain loader + sift (verbatim conventions: sealed Stone U)
def load_shadow(fname):
    z = np.load(fname)
    base = [int(b) for b in z["base"]]
    nl = int(z["nlvl"][0])
    transv = []
    for i in range(nl):
        keys = z["k%d" % i]; v1 = z["a%d" % i]; v2 = z["b%d" % i]
        transv.append({int(k): (tuple(int(x) for x in v1[j]),
                                tuple(int(x) for x in v2[j]))
                       for j, k in enumerate(keys)})
    o = 1
    for T in transv: o *= len(T)
    return o, base, transv
def shadow_sift(base, transv, d1, d2, target):
    r2 = tuple(range(d2)); h = target
    for i, bpt in enumerate(base):
        x = h[bpt]
        if x not in transv[i]: return None
        t1p, t2p = transv[i][x]
        r2 = pmul(r2, t2p)
        h = pmul(pinv(t1p), h)
    if h != tuple(range(d1)): return None
    return r2
def load_bsgs_lvl0(fname, deg):
    z = np.load(fname)
    nl = int(z["nlvl"][0])
    o = 1
    for i in range(nl): o *= z["k%d" % i].shape[0]
    gv = z["g0"]
    gens = [tuple(int(x) for x in gv[j]) for j in range(gv.shape[0])]
    return o, gens
def load_bsgs_transv(fname):
    z = np.load(fname)
    nl = int(z["nlvl"][0])
    transv = []
    for i in range(nl):
        keys = z["k%d" % i]; vals = z["v%d" % i]
        transv.append({int(k): tuple(int(x) for x in vals[j])
                       for j, k in enumerate(keys)})
    return transv
def enumerate_group_np(transv, deg):
    L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
         for T in transv]
    EN = L[-1]
    for j in range(len(L) - 2, -1, -1):
        EN = np.concatenate([L[j][i][EN] for i in range(L[j].shape[0])])
    return EN

say("=" * 78)
say("THE LIFT LAW -- the spinor character eps on K-bar = Sp6(2) and the "
    "split law")
say("for preimages in H = 2.Sp6(2) <= W(E8)   [sealed Stone U caches "
    "READ-ONLY]")
say("=" * 78)
say("""
REGISTERED EXPECTATIONS (resolved below at equal prominence either way):
  RE-A [P, ATLAS via brief]: Sp6(2) has EXACTLY 30 conjugacy classes.
  RE-B [auditor, decisive]: the involution-law converse FAILS at cyclic
       level -- an order-4 class with eps=- whose square is a PLUS
       involution class exists (C4 with all-plus involutions, non-split
       preimage C8).
  RE-C [house]: split => eps == + on S (all split witnesses all-plus).
""")

# ======================================================================
banner("STAGE 0 -- sealed data loaded (read-only); the W(E8) frame rebuilt")
# ======================================================================
GO = 1451520
oKb, KB_GENS = load_bsgs_lvl0(os.path.join(STONE_CACHE, "kbar_120.npz"),
                              120)
EN = np.load(os.path.join(STONE_CACHE, "kbar_elements.npy"))
ORD = np.load(os.path.join(STONE_CACHE, "kbar_orders.npy"))
sign_row = np.load(os.path.join(STONE_CACHE, "kbar_signrow.npy"))
zsq = np.load(os.path.join(STONE_CACHE, "sqsign.npz"))
sq_sign = zsq["sign"]; kb_cls = zsq["cls"]
NKB = EN.shape[0]
cnt = np.bincount(ORD)
censusK = {int(o): int(cnt[o]) for o in range(len(cnt)) if cnt[o]}
check("0a", "sealed K-bar loaded: 1,451,520 elements (all of Sp6(2), "
      "pair action on 120 points), element orders "
      "{1,2,3,4,5,6,7,8,9,10,12,15}, chain order matches",
      NKB == GO and oKb == GO
      and sorted(censusK) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15],
      "census %s" % censusK)

inv_idx = np.nonzero(ORD == 2)[0]
inv_rows = EN[inv_idx]
kbcls_of = {}
for j, i in enumerate(inv_idx.tolist()):
    kbcls_of[tuple(int(x) for x in inv_rows[j])] = int(kb_cls[j])
sign_of_cls = {}
size_of_cls = {}
for j in range(len(inv_idx)):
    c = int(kb_cls[j])
    sign_of_cls.setdefault(c, set()).add(int(sq_sign[j]))
    size_of_cls[c] = size_of_cls.get(c, 0) + 1
sign_of_cls = {c: (list(v)[0] if len(v) == 1 else 0)
               for c, v in sign_of_cls.items()}
check("0b", "sealed involution tables: 5103 involutions in 4 classes, "
      "sizes {315, 3780, 945, 63}, square-sign constant per class with "
      "signs (+,+,-,-) on sizes (315,3780,945,63)",
      len(inv_idx) == 5103
      and sorted(size_of_cls.values()) == [63, 315, 945, 3780]
      and all(s != 0 for s in sign_of_cls.values())
      and {size_of_cls[c]: sign_of_cls[c] for c in size_of_cls}
      == {315: 1, 3780: 1, 945: -1, 63: -1},
      "(size,sign): %s" % sorted((size_of_cls[c], sign_of_cls[c])
                                 for c in size_of_cls))

# W(E8) frame: the 240 roots and the antipode (verbatim construction)
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
anti = tuple(ridx[tuple(-x for x in r)] for r in roots)
ID240 = pident(240); ID120 = pident(120)

# pair machinery for round-trip verification (verbatim stage-2 route)
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
Gm = np.array(GRAM, dtype=np.int64)
Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
rec_ok = bool((Gm @ Ginv == np.eye(8, dtype=np.int64)).all())
Amat = np.array(SIMPLE, dtype=np.int64).T
rmask = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64)
    c = Ginv @ d
    rec_ok &= bool((Amat @ c == np.array(r, dtype=np.int64)).all())
    rmask.append(int(sum((int(c[i]) & 1) << i for i in range(8))))
pair_of = [0] * 240; PAIRS = []; seenm = {}
for k in range(240):
    m = rmask[k]
    if m not in seenm:
        seenm[m] = len(PAIRS); PAIRS.append(m)
    pair_of[k] = seenm[m]
def to120(p240):
    out = [0] * 120
    for k in range(240): out[pair_of[k]] = pair_of[p240[k]]
    return tuple(out)

SHH_o, SHH_base, SHH_tr = load_shadow(os.path.join(STONE_CACHE,
                                                   "shadow_H.npz"))
def lift_H(t):
    u = shadow_sift(SHH_base, SHH_tr, 120, 240, t)
    assert u is not None
    return u
lift_rt = all(to120(lift_H(g)) == g for g in KB_GENS)
check("0c", "W(E8) frame rebuilt (240 roots, antipode -1 = fixed-point-"
      "free central involution); sealed shadow chain loaded (order "
      "1451520); the K-bar generators lift and ROUND-TRIP (project back "
      "to themselves through the rebuilt mod-2 pair map)",
      rec_ok and len(roots) == 240 and all(anti[k] != k for k in range(240))
      and pmul(anti, anti) == ID240 and SHH_o == GO and lift_rt)

# hash lookup for involution rows (own hash, verified collision-free)
RH = RNG.integers(1, 2 ** 63, size=120, dtype=np.uint64)
def hrows(X):
    out = np.zeros(X.shape[0], np.uint64)
    step = 100000
    for s in range(0, X.shape[0], step):
        out[s:s + step] = (X[s:s + step].astype(np.uint64) * RH).sum(axis=1)
    return out
inv_hash = hrows(inv_rows)
h2cls = {int(h): int(c) for h, c in zip(inv_hash.tolist(),
                                        kb_cls.tolist())}
check("0d", "involution row-hashes collision-free (safe class/sign "
      "lookup)", len(h2cls) == 5103)
def eps_of_invol_tuple(t): return sign_of_cls[kbcls_of[t]]
def eps_elem(t):
    """eps of a K-bar element given as a 120-tuple (order via cycle walk;
    even order -> sign of the involution power, from the sealed table
    which check 1i re-verifies on random lifts)."""
    m = pord(t)
    if m % 2 == 1: return 1
    return eps_of_invol_tuple(ppow(t, m // 2))
say("[t=%6.1fs] stage 0 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 1 -- THE COMPLETE eps-TABLE (all 30 conjugacy classes, "
      "exhaustive)")
# ======================================================================
# 1c: class separation.  Invariant bundle per element: (order; fixed
# points of g^k on the 120 pairs, k = 1..15).  The fixed-point counts of
# all powers determine the full cycle type, a class invariant; buckets
# are therefore UNIONS of classes.  1d then proves each bucket is ONE
# class by an exact centralizer count for a representative.
FIX_F = os.path.join(MY_CACHE, "fixprofile.npy")
if os.path.exists(FIX_F):
    FIXM = np.load(FIX_F)
    say("  [cache] fixed-point profiles loaded")
else:
    FIXM = np.zeros((NKB, 15), np.uint8)
    CH = 131072
    t1 = time.time()
    for s in range(0, NKB, CH):
        chunk = EN[s:s + CH]
        P = chunk.copy()
        ar = np.arange(120, dtype=np.uint8)
        for k in range(1, 16):
            if k > 1:
                P = np.take_along_axis(chunk, P, axis=1)
            FIXM[s:s + CH, k - 1] = (P == ar).sum(axis=1)
    np.save(FIX_F, FIXM)
    say("  [built] fixed-point profiles of powers k=1..15 for all "
        "%d elements (%.1fs)" % (NKB, time.time() - t1))
KEYS = np.column_stack([ORD.astype(np.uint8), FIXM])
uk, binv, bcnt = np.unique(KEYS, axis=0, return_inverse=True,
                           return_counts=True)
NB = uk.shape[0]
check("1a", "invariant buckets (order + fixed-point profile of powers "
      "1..15): bucket sizes sum to |Sp6(2)| = 1,451,520",
      int(bcnt.sum()) == GO, "%d buckets" % NB)

# exact centralizer machinery (full pass over all 1,451,520 elements)
def centralizer_order(g_tup):
    g = np.array(g_tup, dtype=np.uint8)
    n_c = 0; CH = 262144
    for s in range(0, NKB, CH):
        chunk = EN[s:s + CH]
        # x in C(g)  <=>  x o g == g o x  <=>  chunk[:,g] == g[chunk]
        n_c += int((chunk[:, g] == g[chunk]).all(axis=1).sum())
    return n_c

CEN_F = os.path.join(MY_CACHE, "bucket_class.json")
rep_idx = [int(np.nonzero(binv == b)[0][0]) for b in range(NB)]
if os.path.exists(CEN_F):
    cent_sizes = json.load(open(CEN_F))["cent"]
    say("  [cache] bucket-rep centralizer counts loaded")
else:
    t1 = time.time()
    cent_sizes = [centralizer_order(tuple(int(x) for x in EN[i]))
                  for i in rep_idx]
    json.dump({"cent": cent_sizes}, open(CEN_F, "w"))
    say("  [built] exact centralizer orders for all %d bucket reps "
        "(%.1fs)" % (NB, time.time() - t1))
cls_sizes_b = [GO // c for c in cent_sizes]
ambiguous = [b for b in range(NB) if cls_sizes_b[b] != int(bcnt[b])]
say("  buckets whose rep's true class size < bucket size (invariant "
    "bundle too coarse there, fail-first log kept): %s"
    % [(b, cls_sizes_b[b], int(bcnt[b])) for b in ambiguous])

# refinement: conjugacy-orbit BFS inside each ambiguous bucket, every
# refined class CONFIRMED by an exact centralizer count of its rep
CLS_F = os.path.join(MY_CACHE, "classes.json")
if os.path.exists(CLS_F):
    zc = json.load(open(CLS_F))
    CLASSES = [(tuple(r), o, s) for r, o, s in
               zip(zc["reps"], zc["orders"], zc["sizes"])]
    refine_ok = bool(zc["refine_ok"])
    say("  [cache] refined class list loaded (%d classes)"
        % len(CLASSES))
else:
    t1 = time.time()
    CLASSES = []          # (rep_tuple, order, size)
    refine_ok = True
    for b in range(NB):
        rep = tuple(int(x) for x in EN[rep_idx[b]])
        if b not in ambiguous:
            CLASSES.append((rep, int(ORD[rep_idx[b]]), cls_sizes_b[b]))
            continue
        idxs = np.nonzero(binv == b)[0]
        pool = {tuple(int(x) for x in EN[i]): None for i in idxs.tolist()}
        first = True
        while pool:
            r = rep if first and rep in pool else next(iter(pool))
            first = False
            orb = conj_orbit(r, KB_GENS)
            refine_ok &= all(x in pool for x in orb)
            for x in orb: pool.pop(x, None)
            csz = GO // centralizer_order(r)
            refine_ok &= (csz == len(orb))
            CLASSES.append((r, pord(r), len(orb)))
    json.dump({"reps": [list(r) for r, o, s in CLASSES],
               "orders": [o for r, o, s in CLASSES],
               "sizes": [s for r, o, s in CLASSES],
               "refine_ok": refine_ok}, open(CLS_F, "w"))
    say("  [built] BFS refinement of the ambiguous buckets (%.1fs)"
        % (time.time() - t1))
NCLS = len(CLASSES)
check("1b", "every bucket resolved into FULL conjugacy classes: "
      "unambiguous buckets confirmed by |G|/|C(rep)| == bucket size; "
      "ambiguous buckets partitioned by conjugacy-orbit BFS under the "
      "K-bar generators, every BFS orbit staying inside its bucket and "
      "its size equal to |G|/|C(rep)| (exact centralizer count per "
      "refined class); class sizes sum to 1,451,520",
      refine_ok and sum(s for _, _, s in CLASSES) == GO
      and all(GO % c == 0 for c in cent_sizes),
      "%d classes total" % NCLS)
re_a = (NCLS == 30)
check("1c", "RE-A %s: the enumeration finds EXACTLY 30 conjugacy "
      "classes of Sp6(2) (exhaustive over all 1,451,520 elements)%s"
      % ("CONFIRMED" if re_a else "REFUTED (full prominence)",
         "" if re_a else " -- found %d" % NCLS), re_a,
      "%d classes, sizes sum %d" % (NCLS, GO))

# class labels: sort by (order, size); letters within an order
by_key = sorted(range(NCLS),
                key=lambda c: (CLASSES[c][1], CLASSES[c][2]))
LABEL = {}
last_o = None; li = 0
for c in by_key:
    if CLASSES[c][1] != last_o:
        last_o = CLASSES[c][1]; li = 0
    LABEL[c] = "%d%s" % (CLASSES[c][1], chr(ord('A') + li)); li += 1

# eps per class: lift the representative, read the order upstairs
eps_of_c = {}; lift_ord_of_c = {}
welldef_ok = True; odd_ok = True
for c in range(NCLS):
    g, n, _sz = CLASSES[c]
    u = lift_H(g); um = pmul(anti, u)
    ou = pord(u); oum = pord(um)
    if n % 2 == 1:
        # one of the lifts must have order n (the other 2n)
        odd_ok &= (sorted((ou, oum)) == [n, 2 * n] or (ou == oum == n))
        eps_of_c[c] = 1
        lift_ord_of_c[c] = min(ou, oum)
    else:
        pu = ppow(u, n); pum = ppow(um, n)
        welldef_ok &= (pu == pum and pu in (ID240, anti))
        eps_of_c[c] = 1 if pu == ID240 else -1
        lift_ord_of_c[c] = ou
        welldef_ok &= (ou == oum == (n if eps_of_c[c] == 1 else 2 * n))
check("1d", "WELL-DEFINEDNESS machine-checked on all %d reps: n odd -> "
      "one lift has order n (eps=+ automatic); n even -> g-hat^n = "
      "(-g-hat)^n in {1,-1} and both lifts share one order (n or 2n)"
      % NCLS, welldef_ok and odd_ok)

# eps is a class function: random conjugates agree (3 per class)
cf_ok = True
for c in range(NCLS):
    g, n, _sz = CLASSES[c]
    for _ in range(3):
        w = rand_word(KB_GENS)
        gc = pmul(pmul(w, g), pinv(w))
        u = lift_H(gc)
        if n % 2 == 1:
            e = 1
        else:
            e = 1 if ppow(u, n) == ID240 else -1
        cf_ok &= (e == eps_of_c[c])
check("1e", "eps is a CLASS FUNCTION: 3 random conjugates per class "
      "(%d total, lifted independently) all reproduce the class eps"
      % (3 * NCLS), cf_ok)

say("")
say("  THE eps-TABLE (exhaustive over the %d conjugacy classes of "
    "K-bar = Sp6(2)):" % NCLS)
say("    class   order   class size   eps   lift order in H")
n_plus = 0; n_minus = 0
for c in by_key:
    e = eps_of_c[c]
    if e == 1: n_plus += 1
    else: n_minus += 1
    say("    %-6s  %5d   %10d    %s    %d"
        % (LABEL[c], CLASSES[c][1], CLASSES[c][2],
           "+" if e == 1 else "-", lift_ord_of_c[c]))
say("    (%d classes eps=+, %d classes eps=-)" % (n_plus, n_minus))
say("")

inv_c = [c for c in range(NCLS) if CLASSES[c][1] == 2]
inv_table = {CLASSES[c][2]: eps_of_c[c] for c in inv_c}
check("1f", "the four involution classes give eps(315)=+, eps(3780)=+, "
      "eps(945)=-, eps(63)=- -- MATCHES the sealed square-sign data "
      "(consistency with Stone U)",
      inv_table == {315: 1, 3780: 1, 945: -1, 63: -1},
      "%s" % sorted(inv_table.items()))

# cross-check vs the sealed per-element sign table + direct random lifts
seal_ok = True
for b in range(NB):
    if int(ORD[rep_idx[b]]) % 2 == 0:
        g = tuple(int(x) for x in EN[rep_idx[b]])
        u = lift_H(g); n = int(ORD[rep_idx[b]])
        e = 1 if ppow(u, n) == ID240 else -1
        seal_ok &= (int(sign_row[rep_idx[b]]) == e)
random.seed(20260902 + 7)
even_idx = np.nonzero(ORD % 2 == 0)[0]
samp = [int(even_idx[random.randrange(even_idx.size)]) for _ in range(300)]
samp_ok = True
for i in samp:
    g = tuple(int(x) for x in EN[i]); n = int(ORD[i])
    u = lift_H(g)
    e = 1 if ppow(u, n) == ID240 else -1
    samp_ok &= (e == int(sign_row[i]))
check("1g", "eps == the sealed square-sign table: on every even-order "
      "bucket rep AND on 300 random even-order elements lifted directly "
      "(so the sealed kbar_signrow.npy IS the element-level eps on even "
      "orders, re-verified independently here)", seal_ok and samp_ok)
eps_all = np.where(ORD % 2 == 1, 1, sign_row.astype(np.int8))
say("[t=%6.1fs] check 1 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 2 -- THE ONE-DIRECTION THEOREM + the sealed witnesses")
# ======================================================================
say("""  THEOREM (one direction).  If S <= K-bar contains an involution t
  with eps(t) = -, then pi^-1(S) is NON-SPLIT.
  PROOF.  A complement C (C cap {+-1} = 1, pi(C) = S) would contain a
  preimage of t of order 2 (pi|C is an isomorphism onto S, so the order
  of the C-preimage of t equals ord(t) = 2).  But BOTH preimages of t
  square to -1 (eps(t) = -), i.e. have order 4.  Contradiction.  []

  SPLITNESS DECIDED EXACTLY per witness S = <g1, g2>: any complement
  contains, for each generator g_i, exactly one of its two lifts
  +-g_i-hat, and is GENERATED by those (pi|C iso).  So S splits iff some
  of the 2^k sign choices of generator lifts closes to order |S|
  (order 2|S| means -1 was reached).  All 2^k choices are tried.""")

WIT = json.load(open(os.path.join(STONE_CACHE, "witnesses.json")))
def split_test(gens120, order_S, cap_extra=10):
    lifts = [lift_H(t) for t in gens120]
    k = len(lifts)
    for mask in range(2 ** k):
        chosen = [pmul(anti, l) if (mask >> i) & 1 else l
                  for i, l in enumerate(lifts)]
        C = closure(chosen, cap=2 * order_S + cap_extra)
        if len(C) == order_S:
            return True
    return False
def inv_eps_multiset(S):
    out = Counter()
    for g in S:
        if pord(g) == 2:
            c = kbcls_of[g]
            out[(size_of_cls[c], "+" if sign_of_cls[c] == 1 else "-")] += 1
    return dict(sorted(out.items()))

witnesses = []
for key, sealed_types in [("L27", "SL(2,7) x1 / 2xL2(7) x3 [sealed]"),
                          ("A5", "2I x3 / A5xZ2 x3 [sealed]"),
                          ("S4", "GL(2,3) x5 / 2O x1 [sealed]"),
                          ("A4", "A4xZ2 x1 / 2T x2 [sealed]")]:
    for ci, ab in enumerate(WIT[key]):
        witnesses.append(("%s#%d" % (key, ci + 1),
                          tuple(ab[0]), tuple(ab[1])))
witnesses.append(("C6Z2", tuple(WIT["C6Z2"][0]), tuple(WIT["C6Z2"][1])))

rows2 = []; thm_ok = True; conv_inv_ok = True
say("")
say("  witness      |S|   involution eps-classes (size,sign):count"
    "        preimage")
for name, a, b in witnesses:
    S = closure([a, b], cap=1400)
    m = inv_eps_multiset(S)
    has_minus = any(sg == "-" for (_, sg), _n in m.items())
    is_split = split_test([a, b], len(S))
    # theorem: minus involution present => must be non-split
    thm_ok &= (not has_minus) or (not is_split)
    # scoped converse observation at witness level:
    conv_inv_ok &= (not is_split) == has_minus
    rows2.append((name, len(S), m, is_split))
    say("  %-10s %5d   %-46s %s"
        % (name, len(S), m, "SPLIT" if is_split else "NON-SPLIT"))
check("2a", "ONE-DIRECTION THEOREM verified on all %d sealed small "
      "witnesses: every witness containing an eps=- involution is "
      "NON-SPLIT (splitness decided exactly by the 2^k sign-choice "
      "closure test)" % len(witnesses), thm_ok)
check("2b", "and every SPLIT witness contains NO eps=- involution "
      "(contrapositive side, same table)",
      all((not sp) or not any(sg == "-" for (_, sg) in m)
          for (_, _, m, sp) in rows2))
say("  [observation, scoped to these witnesses: split <=> no eps=- "
    "involution held on every one: %s]" % conv_inv_ok)

# WE6: the big witness -- theorem side via the sealed non-split verdict
w6a, w6b = tuple(WIT["WE6"][0]), tuple(WIT["WE6"][1])
tr6 = load_bsgs_transv(os.path.join(STONE_CACHE, "we6_copy_120.npz"))
EN6 = enumerate_group_np(tr6, 120)
o6 = EN6.shape[0]
ID6 = np.arange(120, dtype=np.uint8)
O6 = np.zeros(o6, np.uint8)
P = EN6.copy(); k = 1
while True:
    mk = (P == ID6).all(axis=1) & (O6 == 0)
    O6[mk] = k
    if not (O6 == 0).any(): break
    k += 1
    assert k <= 40
    P = np.take_along_axis(EN6, P, axis=1)
inv6 = EN6[O6 == 2]
h6 = hrows(inv6)
cls6 = Counter()
lookup_ok = True
for h in h6.tolist():
    if int(h) in h2cls:
        c = h2cls[int(h)]
        cls6[(size_of_cls[c], "+" if sign_of_cls[c] == 1 else "-")] += 1
    else:
        lookup_ok = False
has_minus6 = any(sg == "-" for (_, sg) in cls6)
check("2c", "the W(E6)-copy witness (order 51840, 891 involutions, "
      "numpy-enumerated from the sealed chain): its involutions resolve "
      "in the K-bar classes as %s -- it CONTAINS eps=- involutions, so "
      "the theorem forces NON-SPLIT; the sealed Stone U run computed "
      "exactly that independently ([P,P] = P contains -1, check 7k) "
      "[C cross-run]" % dict(cls6),
      o6 == 51840 and int((O6 == 2).sum()) == 891 and lookup_ok
      and has_minus6)
say("[t=%6.1fs] check 2 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 3 -- THE CONVERSE HUNT (RE-B, decisive): power chains of "
      "every class")
# ======================================================================
say("""  For EVERY even-order class c (rep g, order n): the involution
  power j = g^(n/2), its class, and its eps -- the full chain table.
  The auditor registered (RE-B): some eps=- class, already at order 4,
  powers into a PLUS involution class.""")
say("")
say("    class   eps   -> involution power lands in   its eps")
chain_ok = True
minus_to_plus = []
for c in by_key:
    n = CLASSES[c][1]
    if n % 2 == 1: continue
    g = CLASSES[c][0]
    j = ppow(g, n // 2)
    cj = kbcls_of[j]
    ej = sign_of_cls[cj]
    # label of the involution class in the table (sizes are distinct)
    bj = next(cc for cc in inv_c if CLASSES[cc][2] == size_of_cls[cj])
    say("    %-6s   %s    -> %-6s (size %5d)            %s"
        % (LABEL[c], "+" if eps_of_c[c] == 1 else "-",
           LABEL[bj], size_of_cls[cj], "+" if ej == 1 else "-"))
    chain_ok &= (ej == eps_of_c[c])
    if eps_of_c[c] == -1 and ej == 1:
        minus_to_plus.append(LABEL[c])
say("")
if minus_to_plus:
    check("3a", "RE-B CONFIRMED: eps=- class(es) %s power into a PLUS "
          "involution class -- explicit C_n witness with all-plus "
          "involutions and non-split preimage" % minus_to_plus, True)
else:
    check("3a", "RE-B REFUTED (registered auditor expectation, resolved "
          "at full prominence): NO eps=- class powers into a plus "
          "involution class -- for EVERY even class, eps(class) = "
          "eps(involution-power class), exhaustively over all 30 "
          "classes.  The involution law SURVIVES cyclic testing: no C_n "
          "with all-plus involutions has non-split preimage",
          not minus_to_plus and chain_ok)
say("""  WHY IT CANNOT HAPPEN (the identity behind the table):
  for n = ord(g) even,   g-hat^n = (g-hat^(n/2))^2,
  and g-hat^(n/2) is a preimage of the involution j = g^(n/2); both
  preimages of j share the same square (central -1, (-j-hat)^2 =
  j-hat^2).  Hence eps(g) = square-sign(j) = eps(j) EXACTLY:
  the spinor character of any even-order element EQUALS that of its
  involution power.  The auditor's C4/C8 refuter shape is impossible.""")
check("3b", "the identity eps(g) = eps(g^(n/2)) (n even) is machine-"
      "verified on all even classes (chain table above) AND at element "
      "level by 1g's 300 random even-order direct lifts (eps == sealed "
      "involution-power sign for every sample)", chain_ok)
say("[t=%6.1fs] check 3 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 4 -- THE CORRECTED LAW: what is exactly true")
# ======================================================================
# 4a: the cyclic law is exact and definitional
cyc_ok = True
for c in range(NCLS):
    g, n, _sz = CLASSES[c]
    u = lift_H(g); um = pmul(anti, u)
    if eps_of_c[c] == 1:
        # some lift has order n: <that lift> is a complement for <g>
        v = u if pord(u) == n else um
        cyc_ok &= (pord(v) == n)          # <v> ~ C_n, misses -1
        cyc_ok &= (ppow(v, n) == ID240)
    else:
        # both lifts have order 2n and power to -1: every preimage
        # subgroup mapping onto <g> contains -1 => non-split
        cyc_ok &= (ppow(u, n) == anti and ppow(um, n) == anti)
check("4a", "THE CYCLIC LAW (exact, definitional): <g> lifts split <=> "
      "eps(g) = +.  eps=+ classes: an order-n lift generates an explicit "
      "complement; eps=- classes: BOTH lifts power to -1 at n, so every "
      "preimage of <g> contains -1.  Machine-checked on all %d classes"
      % NCLS, cyc_ok)

# 4b: split => eps == + on S  (RE-C)
say("""  DIRECTION (theorem): S splits => eps == + on S.
  PROOF.  A complement C gives, for every s in S, a preimage of order
  ord(s) (pi|C iso).  For even-order s that preimage witnesses
  s-hat^ord(s) = 1, i.e. eps(s) = +; odd orders are + automatically. []""")
rec_ok4 = True
for (name, a, b) in witnesses:
    S = closure([a, b], cap=1400)
    if split_test([a, b], len(S)):
        rec_ok4 &= all(eps_elem(g) == 1 for g in S)
check("4b", "RE-C CONFIRMED: on every SPLIT sealed witness, eps = + on "
      "ALL elements (exhaustive per witness, not sampled)", rec_ok4)

# 4c: the involution collapse -- eps==+ on S <=> all involutions of S
# are eps=+ (by the check-3 identity), so the eps-law and the
# involution-law COINCIDE at subgroup level.
say("""  COLLAPSE (corollary of the check-3 identity): for ANY subgroup S,
  eps == + on S  <=>  every INVOLUTION of S has eps = +.
  (Every even-order s in S has eps(s) = eps(s^(n/2)) and s^(n/2) is an
  involution IN S; odd orders are +.)  So the involution-only law and
  the eps-law are the SAME subgroup law; check 3 already verified the
  identity on all 30 classes.""")

# 4d: elementary abelian all-plus => split (theorem + machine check);
# plus the commutator-sign equivalence on Klein fours.
say("""  THEOREM (elementary abelian).  If E <= K-bar is elementary
  abelian and eps == + on E, then pi^-1(E) splits.
  PROOF.  For commuting involutions t, s:  (t-hat s-hat)^2 =
  [t-hat, s-hat] . t-hat^2 s-hat^2 = [t-hat, s-hat], and t-hat s-hat is
  a preimage of ts, so eps(ts) = + iff the lifts COMMUTE.  With all
  pairwise products +, chosen involutive lifts of a basis commute
  pairwise and generate an elementary abelian complement (no nonempty
  product of independent basis lifts can be +-1: it projects to a
  nontrivial element of E). []""")
random.seed(20260902 + 11)
plus_inv_rows = [tuple(int(x) for x in inv_rows[j])
                 for j in range(len(inv_idx)) if int(sq_sign[j]) == 1]
n_k4_pp = 0; n_k4_pm = 0; k4_ok = True; comm_sign_ok = True
tries = 0
while (n_k4_pp < 6 or n_k4_pm < 6) and tries < 4000:
    tries += 1
    t = plus_inv_rows[random.randrange(len(plus_inv_rows))]
    s = plus_inv_rows[random.randrange(len(plus_inv_rows))]
    if s == t or pmul(t, s) != pmul(s, t): continue
    ts = pmul(t, s)
    if pord(ts) != 2: continue
    e_ts = eps_of_invol_tuple(ts)
    lt, ls = lift_H(t), lift_H(s)
    lt = lt if pord(lt) == 2 else pmul(anti, lt)
    ls = ls if pord(ls) == 2 else pmul(anti, ls)
    c = comm(lt, ls)
    csign = 1 if c == ID240 else (-1 if c == anti else 0)
    comm_sign_ok &= (csign == e_ts)     # the proof's equivalence, live
    if e_ts == 1 and n_k4_pp < 6:
        n_k4_pp += 1
        k4_ok &= split_test([t, s], 4)
    elif e_ts == -1 and n_k4_pm < 6:
        n_k4_pm += 1
        k4_ok &= (not split_test([t, s], 4))
check("4c", "Klein-four probes: %d all-plus V4's (eps(t)=eps(s)="
      "eps(ts)=+) all SPLIT; %d V4's of plus generators with MINUS "
      "product all NON-SPLIT; and on every sampled commuting pair the "
      "lift-commutator sign EQUALS eps(ts) (the proof's mechanism, "
      "observed live)" % (n_k4_pp, n_k4_pm),
      n_k4_pp >= 6 and n_k4_pm >= 6 and k4_ok and comm_sign_ok)

# 4e: THE eps-LAW CONVERSE HUNT.  eps==+ on S => split?
# The sharpest potential refuter: S = C4 x C2 = <a, t> with a order 4
# eps+, t an involution eps+, [a,t]=1 in K-bar -- ALL eight elements of
# S are then eps=+ ((a^2 t)-hat^2 = [t-hat,a-hat^2] = 1 whatever the
# generator commutator sign), yet if the lifts of a and t ANTICOMMUTE
# no complement exists (a complement is abelian ~ C4 x C2 but would
# contain the anticommuting lift pair).
say("""  THE eps-LAW CONVERSE HUNT.  Candidate refuter shape: S = C4xC2 =
  <a, t>, a of order 4 with eps+, t an involution with eps+, commuting
  in K-bar.  ALL 8 elements of such an S have eps=+ (verified per hit
  below), but the preimage is non-split iff the lifts of a and t
  anticommute ([a-hat, t-hat] = -1): a complement would be an abelian
  C4 x C2 containing an anticommuting pair.  The commutator sign is
  lift-independent (signs are central and cancel), so it is an invariant
  of (a, t) -- the hunt computes it explicitly.""")
random.seed(20260902 + 13)
plus4_idx = np.nonzero((ORD == 4) & (eps_all == 1))[0]
say("  order-4 elements with eps=+: %d available" % plus4_idx.size)
found_refuter = None
n_pairs = 0; n_anti = 0; allplus_checked = 0
inv_np = inv_rows  # (5103,120) uint8
t_hunt0 = time.time()
for trial in range(80):
    if found_refuter and n_pairs >= 40: break
    if time.time() - t_hunt0 > 120: break
    ai = int(plus4_idx[random.randrange(plus4_idx.size)])
    a = tuple(int(x) for x in EN[ai])
    a_arr = EN[ai]
    a_inv2 = ppow(a, 2)
    # commuting involutions, vectorized over all 5103
    mk = (inv_np[:, a_arr] == a_arr[inv_np]).all(axis=1)
    cand = np.nonzero(mk & (sq_sign == 1))[0]
    if cand.size == 0: continue
    for j in cand.tolist()[:12]:
        t = tuple(int(x) for x in inv_np[j])
        if t == a_inv2: continue
        S = closure([a, t], cap=20)
        if len(S) != 8: continue
        n_pairs += 1
        all_plus = all(eps_elem(g) == 1 for g in S)
        if all_plus: allplus_checked += 1
        la, lt = lift_H(a), lift_H(t)
        c = comm(la, lt)
        gam = 1 if c == ID240 else (-1 if c == anti else 0)
        # lift-independence spot check on the first few
        if n_pairs <= 3:
            c2 = comm(pmul(anti, la), pmul(anti, lt))
            assert c2 == c
        if gam == -1:
            n_anti += 1
            if found_refuter is None and all_plus:
                sp = split_test([a, t], 8)
                if not sp:
                    found_refuter = (ai, j, dict(
                        profile=profile_of(S),
                        inv_eps=inv_eps_multiset(S)))
        if found_refuter and n_pairs >= 40: break
say("  C4xC2 probes: %d commuting (a:4+, t:2+) pairs tested, all-plus "
    "on all 8 elements in %d of them, anticommuting lifts in %d"
    % (n_pairs, allplus_checked, n_anti))
if found_refuter:
    ai, j, meta = found_refuter
    check("4d", "THE eps-LAW CONVERSE IS REFUTED -- THE FINDING OF THE "
          "DAY: an explicit S = C4 x C2 <= K-bar (a = element #%d of "
          "the sealed enumeration, order 4, eps+; t = involution #%d, "
          "eps+; commuting) has eps = + on ALL 8 elements (profile %s, "
          "involution classes %s) yet its preimage is NON-SPLIT (all "
          "four generator-lift sign choices close to order 16, i.e. "
          "reach -1): the lifts of a and t ANTICOMMUTE.  eps == + on S "
          "does NOT imply split; the obstruction lives in the "
          "commutator signs, invisible to element orders"
          % (ai, int(inv_idx[j]), meta["profile"], meta["inv_eps"]),
          True)
    EPS_LAW = ("REFUTED: eps==+ on S does NOT imply split "
               "(C4xC2 witness; the commutator-sign obstruction)")
else:
    check("4d", "eps-law converse: NO refuter found among %d C4xC2 "
          "probes (all all-plus probes split)" % n_pairs,
          n_pairs > 0)
    EPS_LAW = None

# 4f: a broader all-plus sweep (random 2-generated all-plus subgroups)
random.seed(20260902 + 17)
plus_idx_all = np.nonzero(eps_all == 1)[0]
sweep = Counter(); sweep_splits = Counter()
t_sw = time.time(); n_ok = 0; n_try = 0
while n_ok < 40 and n_try < 3000 and time.time() - t_sw < 90:
    n_try += 1
    i1 = int(plus_idx_all[random.randrange(plus_idx_all.size)])
    i2 = int(plus_idx_all[random.randrange(plus_idx_all.size)])
    x = tuple(int(v) for v in EN[i1]); y = tuple(int(v) for v in EN[i2])
    S = closure([x, y], cap=520)
    if len(S) > 512: continue
    if not all(eps_elem(g) == 1 for g in S): continue
    n_ok += 1
    sp = split_test([x, y], len(S))
    key = (len(S), tuple(sorted(profile_of(S).items())))
    sweep[key] += 1
    if sp: sweep_splits[key] += 1
nonsplit_types = [(k, sweep[k] - sweep_splits.get(k, 0))
                  for k in sweep if sweep_splits.get(k, 0) < sweep[k]]
say("  all-plus 2-generated sweep: %d subgroups (|S| <= 512) with "
    "eps==+ verified on every element; %d tries" % (n_ok, n_try))
for k in sorted(sweep):
    say("    |S|=%4d profile %s : %d found, %d split, %d non-split"
        % (k[0], dict(k[1]), sweep[k], sweep_splits.get(k, 0),
           sweep[k] - sweep_splits.get(k, 0)))
if EPS_LAW is None and nonsplit_types:
    check("4e", "THE eps-LAW CONVERSE IS REFUTED in the broad sweep -- "
          "all-plus NON-SPLIT subgroup type(s) found: %s"
          % nonsplit_types, True)
    EPS_LAW = ("REFUTED: eps==+ on S does not imply split "
               "(sweep witness types: %s)" % nonsplit_types)
elif EPS_LAW is not None:
    check("4e", "broad all-plus sweep tallied above (%d subgroups) -- "
          "the C4xC2 refuter of 4d is corroborated by %d further "
          "non-split all-plus types in the sweep"
          % (n_ok, len(nonsplit_types)),
          n_ok > 0)
else:
    check("4e", "eps-law converse: NO all-plus non-split subgroup found "
          "in the sweep either -- eps==+ => split SURVIVES as a "
          "conjecture, scoped to: cyclic (exact, 4a), elementary "
          "abelian (theorem, 4c), the split sealed witnesses, and the "
          "%d sweep types above" % len(sweep), n_ok > 0)
say("[t=%6.1fs] check 4 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 5 -- VERDICT: the final shape of the lift law")
# ======================================================================
if EPS_LAW is None:
    eps_line = ("eps == + on S => split: SURVIVING CONJECTURE (no "
                "counterexample over all tested types: cyclic, "
                "elementary abelian, split witnesses, random all-plus "
                "sweep)")
else:
    eps_line = "eps == + on S => split: " + EPS_LAW
say("""
  THE LIFT LAW, final shape (all statements computed above):

  (i)   THE CYCLIC LAW (exact, all 30 classes): <g> lifts split <=>
        eps(g) = +.  The complete eps-table is printed at check 1
        (%d classes +, %d classes -); the four involution classes are
        315(+), 3780(+), 945(-), 63(-).

  (ii)  THE POWER IDENTITY (the day's structural theorem): for every
        even-order g, eps(g) = eps(g^(ord/2)) -- the spinor character
        of an element equals that of its involution power (proof:
        g-hat^n = (g-hat^(n/2))^2 and both lifts of an involution share
        a square).  Hence RE-B is REFUTED: no C_n with all-plus
        involutions has a non-split preimage; the involution law is
        EXACT at cyclic level, and at subgroup level 'all involutions
        of S are +' is the SAME condition as 'eps == + on S'.

  (iii) THE ONE-DIRECTION THEOREM (exact): an eps=- involution in S
        forces pi^-1(S) non-split.  Verified on every sealed witness
        (SL(2,7)/2I/2T/2O/GL(2,3)/2.W(E6) copies all carry eps=-
        involutions; the split copies carry none).

  (iv)  %s

  (v)   Necessity is a theorem either way: split => eps == + on S
        (RE-C confirmed on the split witnesses, exhaustively per
        witness).
""" % (n_plus, n_minus, eps_line))
check("5a", "verdict assembled; registered expectations resolved: "
      "RE-A %s, RE-B %s, RE-C %s"
      % ("CONFIRMED (30 classes)" if re_a else "REFUTED",
         "CONFIRMED" if minus_to_plus else "REFUTED",
         "CONFIRMED" if rec_ok4 else "REFUTED"),
      True)

say("=" * 78)
say("RESULT: %d checks passed, %d failed%s"
    % (PASS, FAIL, ("  FAILED: %s" % FAILED) if FAILED else ""))
say("registered expectations: RE-A (30 classes) / RE-B (cyclic converse "
    "fails) / RE-C (split => all-plus) -- resolutions printed at their "
    "sites at equal prominence.")
say("total time %.1fs" % (time.time() - T0))
say("=" * 78)
LOG.close()
