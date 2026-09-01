# -*- coding: utf-8 -*-
r"""verify_schur_class_pinning.py -- WHICH PSL(2,7) CLASS LIFTS TO SL(2,7)?

ADOPTED joint work-item, building on the sealed Stone U run
(verify_stone_u_2cover.py, 59 PASS, cache _stone_u_cache/ READ-ONLY here)
and the sealed 28-point machinery (verify_envelope_normalizer.py = SM-024,
verify_ib_normalizer_mechanism.py, verify_stoneq_clifford.py).

QUESTION.  Stone U found the lift type of L2(7) inside H = 2.Sp6(2) is
CLASS-DEPENDENT: 3 found copies (involutions in K-bar class 1, size 315,
square-sign +) lift SPLIT to 2 x L2(7); 1 found copy (involutions in class
3, size 945, square-sign -) lifts to SL(2,7).  The 28-point model of
Sp6(2) knows TWO conjugacy classes of PSL(2,7): the bitangent-transitive
BRIDGE class (transitive on the 28 odd forms, stab S3, even orbits
[1,7,7,21]; IB's Lagrangian diag(M, (M^-1)^T) realizes it) and the
FANO-DOUBLED class (odd orbits [7,21], self-normalizing).  Which of the
two lifts to SL(2,7)?

METHOD (intrinsic invariants only -- never representation-specific data):
  1  28-model: G = Sp6(2) from the Clifford tableau; FULL enumeration on
     28 points; ALL involutions partitioned into conjugacy classes -->
     the four class sizes (expected {63, 315, 945, 3780}); bridge copy
     (IB's Lagrangian embedding, deterministic) and Fano copy (seeded
     hunt, SM-024's own loop) fingerprinted: G-class sizes of their
     involutions / order-3 / order-4 elements.
  2  Stone U model: the 4 cached L2(7) witnesses in K-bar; same intrinsic
     fingerprints (K-bar class sizes); lift types RE-COMPUTED through the
     cached shadow chain (closure with -1; unique involution + order 14
     <=> SL(2,7)).
  3  MATCH by fingerprint; caveat handled: fingerprint matching alone is
     forced only if same-fingerprint copies are conjugate, so
  4  DIRECT ROUTE (gold standard): an explicit isomorphism
     psi: K-bar -> G is CONSTRUCTED from the size-63 involution class
     (= the transvections): commutation on that class recovers the
     symplectic form, a hyperbolic basis chosen inside it labels the 63
     elements by the nonzero vectors of F2^6, and conjugation becomes a
     linear symplectic action.  psi is verified to be an isomorphism ONTO
     G (order 1451520, per-generator linearity => multiplicativity by
     uniqueness of linear extensions).  The SL(2,7)-lifting copy is
     pushed through psi and its orbit fingerprint on the 28 odd forms is
     READ OFF.  Canonicality of the class correspondence: Out(Sp6(2)) = 1
     [P cited, ATLAS], plus the computed fingerprint agreement.
  5  Cross-check: exhaustive normalizer scan in K-bar for one copy of
     each lift type (sealed SM-024: bridge N = PGL(2,7) index 2, Fano
     self-normalizing).
  6  Bonus (nearly free once psi exists): the cached A5 / S4 / A4
     witnesses transported to the 28-model, fingerprints paired with
     their (re-computed) lift types.

DISCIPLINE: compute, never assert; every exhaustive claim says over
what; the Stone U cache is READ-ONLY (own cache: _schur_pin_cache/);
no registry/git writes.  Not RH/GRH; no physical identification (Rule 3).

Run:  python -X utf8 verify_schur_class_pinning.py
      (writes verify_schur_class_pinning.log as it goes)
"""
import itertools, json, os, sys, time, random
from collections import Counter
from math import gcd
import numpy as np

T0 = time.time()
LOG = open("verify_schur_class_pinning.log", "w", encoding="utf-8")
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
MY_CACHE = "_schur_pin_cache"           # this verifier's own checkpoints
os.makedirs(MY_CACHE, exist_ok=True)

# ======================================================================
# permutation utilities (verbatim: verify_stone_u_2cover.py precedent)
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
def profile_of(G):
    return dict(sorted(Counter(pord(g) for g in G).items()))
def conj_orbit(t, gens):
    """conjugation orbit of t under the group generated by gens (= the
    full conjugacy class when gens generate the group t lives in)."""
    gi = [pinv(g) for g in gens]
    S = {t}; fr = [t]
    while fr:
        x = fr.pop()
        for g, giv in zip(gens, gi):
            c = pmul(pmul(g, x), giv)
            if c not in S:
                S.add(c); fr.append(c)
    return S
def orbits_of(gens, pts):
    seen, out = set(), []
    for s0 in pts:
        if s0 in seen: continue
        orb = {s0}; q = [s0]
        while q:
            x = q.pop()
            for g in gens:
                y = g[x]
                if y not in orb: orb.add(y); q.append(y)
        seen |= orb
        out.append(sorted(orb))
    return out
def perm_order(p):
    seen, o = set(), 1
    for s0 in range(len(p)):
        if s0 in seen: continue
        L, x = 1, p[s0]
        seen.add(s0)
        while x != s0:
            seen.add(x); x = p[x]; L += 1
        o = o * L // gcd(o, L)
    return o

# BSGS -- verbatim algorithm from the sealed verify_envelope_normalizer.py
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

def enumerate_group_np(transv, deg):
    L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
         for T in transv]
    EN = L[-1]
    for j in range(len(L) - 2, -1, -1):
        EN = np.concatenate([L[j][i][EN] for i in range(L[j].shape[0])])
    return EN

# shadow-chain loader + sift (verbatim conventions: verify_stone_u_2cover)
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
    """order + the level-0 strong generators (= the ORIGINAL generator
    list of the cached chain: incremental Schreier-Sims only ever appends
    new strong generators to levels >= 1)."""
    z = np.load(fname)
    nl = int(z["nlvl"][0])
    o = 1
    for i in range(nl): o *= z["k%d" % i].shape[0]
    gv = z["g0"]
    gens = [tuple(int(x) for x in gv[j]) for j in range(gv.shape[0])]
    return o, gens

# ======================================================================
# F2 6x6 matrix utilities (verbatim: verify_ib_normalizer_mechanism.py)
# ======================================================================
def par(x): return bin(x).count("1") & 1
def mulM(A, B):
    d = len(A); out = []
    for i in range(d):
        r = 0; a = A[i]
        for k in range(d):
            if (a >> k) & 1: r ^= B[k]
        out.append(r)
    return tuple(out)
def Tm(A):
    d = len(A)
    return tuple(sum(((A[j] >> i) & 1) << j for j in range(d))
                 for i in range(d))
def eye(d): return tuple(1 << i for i in range(d))
def rankM(A):
    d = len(A); rows = list(A); r = 0
    for c in range(d):
        piv = next((i for i in range(r, d) if (rows[i] >> c) & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(d):
            if i != r and (rows[i] >> c) & 1: rows[i] ^= rows[r]
        r += 1
    return r
def matvec(M, x):
    y = 0
    for i in range(len(M)):
        if par(M[i] & x): y |= 1 << i
    return y
def from_cols(cols):
    n = len(cols)
    return tuple(sum(((cols[k] >> i) & 1) << k for k in range(n))
                 for i in range(n))
I6 = eye(6)
OMEGA = tuple([1 << (i + 3) for i in range(3)] + [1 << i for i in range(3)])
def is_symplectic(M):
    return mulM(Tm(M), mulM(OMEGA, M)) == OMEGA
def omega_pair(x, y): return par(matvec(OMEGA, y) & x)   # x^T Omega y

say("=" * 78)
say("SCHUR CLASS PINNING -- which PSL(2,7) class of Sp6(2) lifts to SL(2,7)"
    " in 2.Sp6(2)?")
say("=" * 78)
say("[t=%6.1fs] start" % (time.time() - T0))

# ======================================================================
banner("SECTION 1 -- 28-model: G = Sp6(2), full enumeration, involution "
       "classes")
# ======================================================================
# Clifford tableau generators (verbatim: verify_envelope_normalizer.py /
# Stone Q construction)
I6cols = [1 << i for i in range(6)]
CLIF = {}
for i in range(3):                       # H_i : swap x_i <-> z_i
    cols = list(I6cols); cols[i], cols[i + 3] = cols[i + 3], cols[i]
    CLIF[f"H{i+1}"] = from_cols(cols)
for i in range(3):                       # S_i : z_i += x_i
    cols = list(I6cols); cols[i] = I6cols[i] ^ I6cols[i + 3]
    CLIF[f"S{i+1}"] = from_cols(cols)
for c in range(3):                       # CNOT c->t
    for t in range(3):
        if c == t: continue
        cols = list(I6cols)
        cols[c] = I6cols[c] ^ I6cols[t]
        cols[t + 3] = I6cols[t + 3] ^ I6cols[c + 3]
        CLIF[f"CX{c+1}{t+1}"] = from_cols(cols)
def mat_to_perm64(M): return tuple(matvec(M, x) for x in range(64))
SP_ORDER = 1451520
cl_perms = [mat_to_perm64(M) for M in CLIF.values()]
oV, memV, TRV = make_bsgs_full(cl_perms, 64)
check("1a", "|G| = 1,451,520 = |Sp6(2)|: the 12 Clifford tableau matrices "
      "generate the full symplectic group on F2^6 (BSGS on the 64 "
      "vectors); all 12 preserve Omega",
      oV == SP_ORDER and all(is_symplectic(M) for M in CLIF.values()),
      "order %d" % oV)

# the 64 quadratic refinements, Arf split, form-label action (verbatim)
def q0(x): return par((x & 7) & (x >> 3))
def qform(c): return tuple(q0(x) ^ par(c & x) for x in range(64))
zeros = [sum(1 for x in range(64) if qform(c)[x] == 0) for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms = [c for c in range(64) if zeros[c] == 28]
def perm_inv64(p):
    r = [0] * 64
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def act_form_perm(Mperm_inv, c):
    tab = tuple(q0(Mperm_inv[x]) ^ par(c & Mperm_inv[x]) for x in range(64))
    cc = 0
    for k in range(6):
        if tab[1 << k] ^ q0(1 << k): cc |= 1 << k
    assert tab == qform(cc), "form action left the refinement family"
    return cc
def label_perm(M):
    pi = perm_inv64(mat_to_perm64(M))
    return tuple(act_form_perm(pi, c) for c in range(64))
odd_idx = {c: i for i, c in enumerate(odd_forms)}
def rest28(p64): return tuple(odd_idx[p64[c]] for c in odd_forms)
label_gens = [label_perm(M) for M in CLIF.values()]
G28gens = [rest28(p) for p in label_gens]
o28, memG28, TR28 = make_bsgs_full(G28gens, 28)
o64L, memG64L, TR64 = make_bsgs_full(label_gens, 64)
check("1b", "Arf split 36 even + 28 odd; G acts on the 28 odd forms "
      "FAITHFULLY and TRANSITIVELY (28-point BSGS order 1,451,520, first "
      "orbit 28); 64-label order agrees",
      len(even_forms) == 36 and len(odd_forms) == 28
      and o28 == SP_ORDER and o64L == SP_ORDER and len(TR28[0]) == 28)

# full enumeration on 28 points + element orders (cached)
EN_f = os.path.join(MY_CACHE, "en28.npy")
ORD_f = os.path.join(MY_CACHE, "ord28.npy")
FLAG_f = os.path.join(MY_CACHE, "flags.json")
FLAGS = json.load(open(FLAG_f)) if os.path.exists(FLAG_f) else {}
def flag_put(k, v):
    FLAGS[k] = v
    json.dump(FLAGS, open(FLAG_f, "w"))
if os.path.exists(EN_f):
    EN28 = np.load(EN_f)
    uniq_ok = bool(FLAGS.get("en28_unique"))
    say("  [cache] 28-model enumeration loaded")
else:
    EN28 = enumerate_group_np(TR28, 28)
    np.save(EN_f, EN28)
    uniq_ok = (np.unique(EN28, axis=0).shape[0] == EN28.shape[0])
    flag_put("en28_unique", bool(uniq_ok))
check("1c", "BSGS transversal products enumerate 1,451,520 DISTINCT "
      "elements of G on 28 points (uniqueness verified row-wise at first "
      "build, cached flag on resume)",
      EN28.shape == (SP_ORDER, 28) and uniq_ok)
ID28 = np.arange(28, dtype=np.uint8)
if os.path.exists(ORD_f):
    ORD28 = np.load(ORD_f)
    say("  [cache] 28-model order census loaded")
else:
    ORD28 = np.zeros(SP_ORDER, np.uint8)
    P = EN28.copy(); k = 1
    while True:
        mk = (P == ID28).all(axis=1) & (ORD28 == 0)
        ORD28[mk] = k
        if not (ORD28 == 0).any(): break
        k += 1
        assert k <= 40
        P = np.take_along_axis(EN28, P, axis=1)
    del P
    np.save(ORD_f, ORD28)
cnt28 = np.bincount(ORD28)
census28 = {int(o): int(cnt28[o]) for o in range(len(cnt28)) if cnt28[o]}
SP6_CENSUS = {1: 1, 2: 5103, 3: 16352, 4: 75600, 5: 48384, 6: 272160,
              7: 207360, 8: 181440, 9: 161280, 10: 145152, 12: 241920,
              15: 96768}
check("1d", "exhaustive element-order census of G = the Sp6(2) census "
      "(matches the sealed Stone U K-bar census line for line)",
      census28 == SP6_CENSUS, "%s" % census28)

# ALL involutions partitioned into conjugacy classes (intrinsic labels)
inv_rows28 = EN28[ORD28 == 2]
inv_tups28 = [tuple(int(x) for x in r) for r in inv_rows28]
inv_set28 = set(inv_tups28)
cls28_of = {}
cls28_sizes = []
for t in inv_tups28:
    if t in cls28_of: continue
    orb = conj_orbit(t, G28gens)
    cid = len(cls28_sizes)
    for x in orb:
        assert x in inv_set28
        cls28_of[x] = cid
    cls28_sizes.append(len(orb))
check("1e", "the 5103 involutions of G partition into EXACTLY 4 "
      "conjugacy classes (conjugation-orbit closure under the 12 "
      "generators, exhaustive over all involutions) with sizes "
      "{63, 315, 945, 3780}",
      len(cls28_of) == 5103 and sorted(cls28_sizes) == [63, 315, 945, 3780],
      "sizes in discovery order %s" % cls28_sizes)
def gclass_size_28(t):
    """intrinsic label of any element t of G (28-perm): its G-conjugacy
    class SIZE (involutions via the full partition, others via orbit)."""
    if t in cls28_of: return cls28_sizes[cls28_of[t]]
    return len(conj_orbit(t, G28gens))
say("[t=%6.1fs] section 1 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 2 -- 28-model: bridge copy (IB Lagrangian) and Fano copy "
       "(SM-024 hunt); intrinsic fingerprints")
# ======================================================================
# IB's Lagrangian embedding (verbatim: verify_ib_normalizer_mechanism.py)
I3 = eye(3)
GL32 = [tuple(rows) for rows in itertools.product(range(8), repeat=3)
        if rankM(tuple(rows)) == 3]
INV3 = {}
for M in GL32:
    for N in GL32:
        if mulM(M, N) == I3:
            INV3[M] = N; break
def phi(M):
    Mit = Tm(INV3[M])
    return tuple([M[i] for i in range(3)] + [Mit[i] << 3 for i in range(3)])
Hb_mats = [phi(M) for M in GL32]
PSL_CENSUS = {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}
cenHb = dict(sorted(Counter(
    perm_order(mat_to_perm64(g)) for g in Hb_mats).items()))
Hb28 = [rest28(label_perm(g)) for g in Hb_mats]
Hb28set = set(Hb28)
check("2a", "H_b = {diag(M,(M^-1)^T)} rebuilt: 168 distinct symplectic "
      "matrices, PSL(2,7) order census, faithful on the 28",
      len(set(Hb_mats)) == 168 and all(is_symplectic(g) for g in Hb_mats)
      and cenHb == PSL_CENSUS and len(Hb28set) == 168)
A3g = ((1 | 2), 2, 4); B3g = (4, 1, 2)
A6, B6 = phi(A3g), phi(B3g)
lpA, lpB = label_perm(A6), label_perm(B6)
odd_orb_b = sorted(len(t) for t in orbits_of(
    [rest28(lpA), rest28(lpB)], range(28)))
even_orb_b = sorted(len(t) for t in orbits_of([lpA, lpB], even_forms))
check("2b", "H_b has the BRIDGE-class fingerprint: transitive on the 28 "
      "odd forms, even-form orbits [1,7,7,21] (sealed SM-003/SM-024 / "
      "verify_ib_normalizer_mechanism fingerprint)",
      odd_orb_b == [28] and even_orb_b == [1, 7, 7, 21],
      "odd %s even %s" % (odd_orb_b, even_orb_b))
Hb_inv28 = [p for p in Hb28 if p != pident(28) and pmul(p, p) == pident(28)]
cls_b = sorted(set(cls28_of[p] for p in Hb_inv28))
S_b = cls28_sizes[cls_b[0]] if len(cls_b) == 1 else None
inv_mat_b = next(g for g in Hb_mats
                 if g != I6 and mulM(g, g) == I6)
rank_b = rankM(tuple(inv_mat_b[i] ^ I6[i] for i in range(6)))
# type a vs c for a rank-2 involution: <v, gv> = 0 for all v  <=> type a
type_a_b = all(omega_pair(x, matvec(inv_mat_b, x)) == 0 for x in range(64))
check("2c", "H_b's 21 involutions all lie in ONE G-class; its size is "
      "the intrinsic label S_b",
      len(Hb_inv28) == 21 and len(cls_b) == 1,
      "S_b = %s   [obs: rank(g-I) = %d, <v,gv>=0 for all v: %s]"
      % (S_b, rank_b, type_a_b))
Hb_o3 = [p for p in Hb28 if pord(p) == 3]
Hb_o4 = [p for p in Hb28 if pord(p) == 4]
orb3_b = conj_orbit(Hb_o3[0], G28gens)
orb4_b = conj_orbit(Hb_o4[0], G28gens)
check("2d", "H_b order-3 / order-4 fingerprints: all 56 order-3 elements "
      "in one G-class, all 42 order-4 elements in one G-class",
      all(p in orb3_b for p in Hb_o3) and all(p in orb4_b for p in Hb_o4),
      "sizes (|3-class|, |4-class|) = (%d, %d)" % (len(orb3_b),
                                                   len(orb4_b)))
FP_bridge = (S_b, len(orb3_b), len(orb4_b))

# --- the Fano copy: SM-024's own seeded hunt loop, replicated verbatim
E28t = pident(28); E64t = pident(64)
def mul28(a, b): return tuple(a[b[k]] for k in range(28))
def mul64(a, b): return tuple(a[b[k]] for k in range(64))
def inv28(a): return pinv(a)
def pow64(p, e):
    x = E64t
    for _ in range(e): x = mul64(p, x)
    return x
def close_group28(gens28):
    S = {E28t}; frontier = [E28t]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens28:
                b = mul28(g, a)
                if b not in S:
                    S.add(b); nxt.append(b)
        frontier = nxt
    return S
fano_cached = FLAGS.get("fano_gens")
hunted_H = None
if fano_cached:
    xK64 = tuple(fano_cached[0]); c64s = tuple(fano_cached[1])
    xK28, c28s = rest28(xK64), rest28(c64s)
    say("  [cache] Fano witness reloaded")
else:
    random.seed(20260831)               # the sealed SM-024 seed
    TLIST64 = [list(T.values()) for T in TR64]
    def rand_elem64():
        g = E64t
        for T in TLIST64:
            g = mul64(random.choice(T), g)
        return g
    c64s = None
    for _ in range(20000):
        g = rand_elem64()
        o = perm_order(rest28(g))
        if o % 7 == 0:
            c64s = pow64(g, o // 7)
            break
    c28s = rest28(c64s)
    ALLOWED = {1, 2, 3, 4, 7}
    foundH = foundK2 = None
    tries = 0
    while (foundH is None or foundK2 is None) and tries < 120000:
        tries += 1
        g = rand_elem64()
        r = rest28(g); o = perm_order(r)
        if o % 2: continue
        x64 = pow64(g, o // 2)
        x28 = rest28(x64)
        xc = mul28(x28, c28s)
        if perm_order(xc) not in (3, 4, 7): continue
        cm = mul28(mul28(x28, c28s), mul28(x28, inv28(c28s)))
        if perm_order(cm) not in ALLOWED: continue
        osz = sorted(len(t) for t in orbits_of([x28, c28s], range(28)))
        if osz == [28] and foundH is None:
            got, _, _ = make_bsgs_full([x28, c28s], 28)
            if got == 168:
                cen = Counter(perm_order(h)
                              for h in close_group28([x28, c28s]))
                if dict(cen) == PSL_CENSUS:
                    foundH = (x64, x28)
        elif osz == [7, 21] and foundK2 is None:
            got, _, _ = make_bsgs_full([x28, c28s], 28)
            if got == 168:
                cen = Counter(perm_order(h)
                              for h in close_group28([x28, c28s]))
                if dict(cen) == PSL_CENSUS:
                    foundK2 = (x64, x28)
    say("  hunt: %d tries (seed 20260831, SM-024's loop verbatim)" % tries)
    assert foundK2 is not None, "Fano hunt failed within budget"
    xK64, xK28 = foundK2
    flag_put("fano_gens", [list(xK64), list(c64s)])
    if foundH is not None:
        hunted_H = foundH
Hf168 = close_group28([xK28, c28s])
cenHf = dict(sorted(Counter(perm_order(h) for h in Hf168).items()))
odd_orb_f = sorted(len(t) for t in orbits_of([xK28, c28s], range(28)))
# xK64/c64s ARE 64-form-label perms (the hunt samples the label action)
even_orb_f = sorted(len(t) for t in orbits_of([xK64, c64s], even_forms))
check("2e", "the FANO-DOUBLED copy H_f found in the same G (order 168, "
      "PSL census) with odd orbits [7,21] and even orbits [1,7,28] "
      "(SM-024's contrast-class fingerprint)",
      len(Hf168) == 168 and cenHf == PSL_CENSUS
      and odd_orb_f == [7, 21] and even_orb_f == [1, 7, 28],
      "odd %s even %s" % (odd_orb_f, even_orb_f))
Hf_inv28 = [p for p in Hf168 if p != E28t and pmul(p, p) == E28t]
cls_f = sorted(set(cls28_of[p] for p in Hf_inv28))
S_f = cls28_sizes[cls_f[0]] if len(cls_f) == 1 else None
Hf_o3 = [p for p in Hf168 if pord(p) == 3]
Hf_o4 = [p for p in Hf168 if pord(p) == 4]
orb3_f = conj_orbit(next(iter(Hf_o3)), G28gens)
orb4_f = conj_orbit(next(iter(Hf_o4)), G28gens)
check("2f", "H_f's 21 involutions all in ONE G-class (size S_f); order-3 "
      "and order-4 elements each in one G-class",
      len(Hf_inv28) == 21 and len(cls_f) == 1
      and all(p in orb3_f for p in Hf_o3)
      and all(p in orb4_f for p in Hf_o4),
      "S_f = %s, (|3-class|, |4-class|) = (%d, %d)"
      % (S_f, len(orb3_f), len(orb4_f)))
FP_fano = (S_f, len(orb3_f), len(orb4_f))
check("2g", "SEPARATION in the 28-model: the bridge and Fano classes have "
      "DIFFERENT intrinsic involution-class sizes (and full fingerprints)",
      S_b != S_f and FP_bridge != FP_fano,
      "bridge (inv,3,4)-class sizes %s vs Fano %s" % (FP_bridge, FP_fano))
if hunted_H is not None:
    hH = close_group28([hunted_H[1], c28s])
    hinv = [p for p in hH if p != E28t and pmul(p, p) == E28t]
    same = sorted(set(cls28_of[p] for p in hinv)) == cls_b
    check("2h", "corroboration: the hunt's OWN transitive copy (found "
          "alongside H_f) has involutions in the SAME G-class as IB's "
          "Lagrangian H_b", same and len(hH) == 168)
say("[t=%6.1fs] section 2 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 3 -- Stone U model: the 4 cached L2(7) copies in K-bar; "
       "fingerprints + lift types RE-COMPUTED")
# ======================================================================
oKb, KB_GENS = load_bsgs_lvl0(os.path.join(STONE_CACHE, "kbar_120.npz"),
                              120)
ENkb = np.load(os.path.join(STONE_CACHE, "kbar_elements.npy"),
               mmap_mode="r")
ORDkb = np.load(os.path.join(STONE_CACHE, "kbar_orders.npy"))
zsq = np.load(os.path.join(STONE_CACHE, "sqsign.npz"))
sq_sign = zsq["sign"]; kb_cls = zsq["cls"]
inv_idx_kb = np.nonzero(ORDkb == 2)[0]
inv_rows_kb = np.array(ENkb[inv_idx_kb])
kb_cls_sizes = np.bincount(kb_cls)
cnt_kb = np.bincount(ORDkb)
census_kb = {int(o): int(cnt_kb[o]) for o in range(len(cnt_kb))
             if cnt_kb[o]}
check("3a", "sealed Stone U caches loaded: |K-bar| = 1,451,520 (chain "
      "product), level-0 generators regenerate it; element-order census "
      "IDENTICAL to the 28-model census (1d) -- the two models share the "
      "intrinsic Sp6(2) fingerprint",
      oKb == SP_ORDER and census_kb == census28 and len(KB_GENS) == 2
      and make_bsgs_full(KB_GENS, 120)[0] == SP_ORDER,
      "lvl-0 gens: %d" % len(KB_GENS))
kbcls_of = {}                # involution 120-tuple -> class id
for j, i in enumerate(inv_idx_kb.tolist()):
    kbcls_of[tuple(int(x) for x in inv_rows_kb[j])] = int(kb_cls[j])
sign_of_cls = {}
for j in range(len(inv_idx_kb)):
    sign_of_cls.setdefault(int(kb_cls[j]), set()).add(int(sq_sign[j]))
reverify = True
for cid in range(len(kb_cls_sizes)):
    rep = next(t for t, c in kbcls_of.items() if c == cid)
    orb = conj_orbit(rep, KB_GENS)
    reverify &= (len(orb) == int(kb_cls_sizes[cid])
                 and all(kbcls_of.get(x) == cid for x in orb))
check("3b", "K-bar involution classes RE-VERIFIED from scratch: each "
      "cached class is a single conjugation orbit under the K-bar "
      "generators, sizes {315, 3780, 945, 63}, square-signs constant "
      "per class (+, +, -, -)",
      reverify and sorted(kb_cls_sizes.tolist()) == [63, 315, 945, 3780]
      and all(len(v) == 1 for v in sign_of_cls.values()),
      "(size, sign) by class id: %s"
      % [(int(kb_cls_sizes[c]), sorted(sign_of_cls[c]))
         for c in range(len(kb_cls_sizes))])
def gclass_size_kb(t):
    if t in kbcls_of: return int(kb_cls_sizes[kbcls_of[t]])
    return len(conj_orbit(t, KB_GENS))

WIT = json.load(open(os.path.join(STONE_CACHE, "witnesses.json")))
L27W = WIT["L27"]
copies = []
for ci, ab in enumerate(L27W):
    a = tuple(ab[0]); b = tuple(ab[1])
    Gc = closure([a, b], cap=400)
    prof = profile_of(Gc)
    copies.append((a, b, Gc))
    assert len(Gc) == 168 and prof == PSL_CENSUS
distinct = len({frozenset(G) for (_, _, G) in copies}) == 4
copy_invcls = []
for ci, (a, b, Gc) in enumerate(copies):
    invs = [g for g in Gc if pord(g) == 2]
    cids = sorted(set(kbcls_of[g] for g in invs))
    copy_invcls.append((len(invs), cids,
                        int(kb_cls_sizes[cids[0]]) if len(cids) == 1
                        else None))
check("3c", "the 4 cached L2(7) witnesses re-closed (each 168, PSL "
      "census, pairwise distinct); each copy's 21 involutions lie in ONE "
      "K-bar class",
      distinct and all(n == 21 and len(c) == 1
                       for (n, c, s) in copy_invcls),
      "involution class sizes per copy: %s"
      % [s for (_, _, s) in copy_invcls])

# lift types re-computed: W(E8) roots + antipode + the cached shadow chain
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
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
SIMPLE = [
    (1, -1, -1, -1, -1, -1, -1, 1), (2, 2, 0, 0, 0, 0, 0, 0),
    (-2, 2, 0, 0, 0, 0, 0, 0), (0, -2, 2, 0, 0, 0, 0, 0),
    (0, 0, -2, 2, 0, 0, 0, 0), (0, 0, 0, -2, 2, 0, 0, 0),
    (0, 0, 0, 0, -2, 2, 0, 0), (0, 0, 0, 0, 0, -2, 2, 0)]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
Gm = np.array(GRAM, dtype=np.int64)
Ginv8 = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
assert (Gm @ Ginv8 == np.eye(8, dtype=np.int64)).all()
coords = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64)
    coords.append(Ginv8 @ d)
rmask = [int(sum((int(c[i]) & 1) << i for i in range(8))) for c in coords]
pair_of = [0] * 240; seenm = {}
for k in range(240):
    m = rmask[k]
    if m not in seenm: seenm[m] = len(seenm)
    pair_of[k] = seenm[m]
def to120(p240):
    out = [0] * 120
    for k in range(240): out[pair_of[k]] = pair_of[p240[k]]
    return tuple(out)
SHH_o, SHH_base, SHH_tr = load_shadow(os.path.join(STONE_CACHE,
                                                   "shadow_H.npz"))
def lift_H(t):
    u = shadow_sift(SHH_base, SHH_tr, 120, 240, t)
    assert u is not None and to120(u) == t
    return u
check("3d", "W(E8) frame rebuilt (240 roots, antipode -1 fixed-point-"
      "free); the cached H shadow chain loads with order 1,451,520 and "
      "sifts K-bar elements to lifts in H",
      len(roots) == 240 and all(anti[k] != k for k in range(240))
      and pmul(anti, anti) == pident(240) and SHH_o == SP_ORDER)

def split_double(prof):
    """element-order profile of Z2 x X from that of X (Stone U's helper)"""
    out = Counter()
    for o, c in prof.items():
        out[o] += c
        out[o * 2 // gcd(o, 2)] += c
    return dict(sorted(out.items()))
def mmul2(A, B, p):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e+b*g) % p, (a*f+b*h) % p, (c*e+d*g) % p, (c*f+d*h) % p)
def mord2(M, p):
    I = (1, 0, 0, 1); x = M; k = 1
    while x != I: x = mmul2(x, M, p); k += 1
    return k
SL27 = [(a, b, c, d) for a in range(7) for b in range(7)
        for c in range(7) for d in range(7) if (a*d - b*c) % 7 == 1]
prof_SL27 = dict(sorted(Counter(mord2(M, 7) for M in SL27).items()))
prof_2xL27 = split_double(PSL_CENSUS)
lift_types = []
for ci, (a, b, Gc) in enumerate(copies):
    la, lb = lift_H(a), lift_H(b)
    P = closure([la, lb, anti], cap=800)
    profP = profile_of(P)
    ninv = profP.get(2, 0)
    if profP == prof_SL27:
        typ = "SL(2,7)"
    elif profP == prof_2xL27:
        typ = "2 x L2(7)"
    else:
        typ = "UNRECOGNIZED %s" % profP
    lift_types.append(typ)
    say("  copy %d: involution class size %d (sign %s) -> preimage order "
        "%d, %d involution(s), 14 present: %s => %s"
        % (ci + 1, copy_invcls[ci][2],
           sorted(sign_of_cls[copy_invcls[ci][1][0]]), len(P), ninv,
           14 in profP, typ))
sl_copies = [i for i, t in enumerate(lift_types) if t == "SL(2,7)"]
sp_copies = [i for i, t in enumerate(lift_types) if t == "2 x L2(7)"]
check("3e", "lift types RE-COMPUTED through the shadow chain (closure "
      "with -1, census against explicit SL(2,7) / 2xL2(7) models): "
      "3 copies split, 1 copy SL(2,7) -- matching the sealed Stone U "
      "UB5a table", len(sl_copies) == 1 and len(sp_copies) == 3)
S_split = copy_invcls[sp_copies[0]][2]
S_schur = copy_invcls[sl_copies[0]][2]
check("3f", "in K-bar the lift type is PINNED to the involution class: "
      "ALL split copies have involutions in the SAME class (one size), "
      "the SL(2,7) copy in a DIFFERENT class",
      len({copy_invcls[i][2] for i in sp_copies}) == 1
      and S_schur != S_split,
      "split copies -> class size %d; SL(2,7) copy -> class size %d"
      % (S_split, S_schur))
# order-3 / order-4 fingerprints for one copy of each type
def fp_of_copy_kb(Gc):
    inv = next(g for g in Gc if pord(g) == 2)
    e3 = next(g for g in Gc if pord(g) == 3)
    e4 = next(g for g in Gc if pord(g) == 4)
    o3 = conj_orbit(e3, KB_GENS); o4 = conj_orbit(e4, KB_GENS)
    ok3 = all(g in o3 for g in Gc if pord(g) == 3)
    ok4 = all(g in o4 for g in Gc if pord(g) == 4)
    return (gclass_size_kb(inv), len(o3), len(o4)), ok3 and ok4
FP_kb_split, okA = fp_of_copy_kb(copies[sp_copies[0]][2])
FP_kb_schur, okB = fp_of_copy_kb(copies[sl_copies[0]][2])
check("3g", "K-bar (inv, order-3, order-4) class-size fingerprints "
      "computed for one copy of each lift type (each order's elements "
      "single-class per copy); the 4 copies form EXACTLY 2 fingerprint "
      "groups", okA and okB and FP_kb_split != FP_kb_schur,
      "split-type %s, SL(2,7)-type %s" % (FP_kb_split, FP_kb_schur))
say("[t=%6.1fs] section 3 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 4 -- the fingerprint MATCH (with its caveat)")
# ======================================================================
match_bridge_schur = (FP_bridge == FP_kb_schur and FP_fano == FP_kb_split)
match_bridge_split = (FP_bridge == FP_kb_split and FP_fano == FP_kb_schur)
check("4a", "the two 28-model fingerprints and the two K-bar fingerprints "
      "MATCH UP one-to-one (class sizes are isomorphism-invariant)",
      match_bridge_schur or match_bridge_split,
      "bridge %s / Fano %s  vs  K-bar split-type %s / SL(2,7)-type %s"
      % (FP_bridge, FP_fano, FP_kb_split, FP_kb_schur))
if match_bridge_schur:
    say("  fingerprint route says: BRIDGE class <-> SL(2,7)-lifting class.")
elif match_bridge_split:
    say("  fingerprint route says: BRIDGE class <-> SPLIT-lifting class; "
        "the FANO class is the SL(2,7) one.")
say("  CAVEAT (handled next): fingerprints alone force the matching only "
    "if same-fingerprint")
say("  copies are conjugate.  The DIRECT ROUTE below removes the caveat "
    "by explicit transport.")
say("[t=%6.1fs] section 4 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 5 -- DIRECT ROUTE: explicit isomorphism psi: K-bar -> G "
       "via the 63-class; transport the copies")
# ======================================================================
cid63 = next(c for c in range(len(kb_cls_sizes))
             if int(kb_cls_sizes[c]) == 63)
C63 = [t for t, c in kbcls_of.items() if c == cid63]
def commT(x, y): return 0 if pmul(x, y) == pmul(y, x) else 1
ok_prod = True
for i in range(63):
    for j in range(i + 1, 63):
        o = pord(pmul(C63[i], C63[j]))
        ok_prod &= (o == 2) if commT(C63[i], C63[j]) == 0 else (o == 3)
check("5a", "the size-63 involution class C63 of K-bar behaves as the "
      "TRANSVECTION class: for every distinct pair, the product has "
      "order 2 iff they commute and order 3 iff not (all 63x63 pairs)",
      ok_prod)
c1 = C63[0]
d1 = next(x for x in C63 if commT(c1, x))
perp12 = [x for x in C63 if commT(x, c1) == 0 and commT(x, d1) == 0]
c2 = perp12[0]
d2 = next(x for x in perp12 if commT(c2, x))
perp34 = [x for x in perp12
          if commT(x, c2) == 0 and commT(x, d2) == 0]
c3 = perp34[0]
d3 = next(x for x in perp34 if commT(c3, x))
CB = [c1, c2, c3]; DB = [d1, d2, d3]
hyp_ok = all(commT(CB[i], DB[j]) == (1 if i == j else 0)
             and commT(CB[i], CB[j]) == 0 and commT(DB[i], DB[j]) == 0
             for i in range(3) for j in range(3))
check("5b", "a hyperbolic (symplectic) basis found INSIDE C63 by "
      "commutation: pairs (c_i, d_i) with c_i,d_j commuting except "
      "exactly the i=j partners (|perp12| = 15, |perp34| = 3)",
      hyp_ok and len(perp12) == 15 and len(perp34) == 3)
ulab = {}
for x in C63:
    u = 0
    for i in range(3):
        if commT(x, DB[i]): u |= 1 << i          # e_i coefficient
        if commT(x, CB[i]): u |= 1 << (i + 3)    # f_i coefficient
    ulab[x] = u
lab_vals = sorted(ulab.values())
pair_ok = all(omega_pair(ulab[x], ulab[y]) == commT(x, y)
              for x in C63 for y in C63)
add_ok = all(ulab[pmul(pmul(x, y), x)] == (ulab[x] ^ ulab[y])
             for x in C63 for y in C63 if commT(x, y) == 1)
lab_of = {v: k for k, v in ulab.items()}
check("5c", "labels u: C63 -> F2^6\\{0} via commutation with the basis: "
      "BIJECTIVE onto the 63 nonzero vectors; Omega-pairing(u(x),u(y)) = "
      "commutation(x,y) for ALL pairs; transvection addition law "
      "u(xyx) = u(x)+u(y) on ALL non-commuting pairs",
      lab_vals == list(range(1, 64)) and pair_ok and add_ok
      and all(ulab[CB[i]] == 1 << i and ulab[DB[i]] == 1 << (i + 3)
              for i in range(3)))
C63set = set(C63)
def psi(g):
    """the matrix of conjugation-by-g on C63 in the u-labels; returns
    (matrix, linear_ok).  Uniqueness of the linear extension of a
    permutation of ALL 63 nonzero vectors makes g -> psi(g)
    automatically multiplicative wherever linear_ok holds."""
    gi = pinv(g)
    cols = []
    for j in range(6):
        x = CB[j] if j < 3 else DB[j - 3]
        cx = pmul(pmul(g, x), gi)
        if cx not in C63set: return None, False
        cols.append(ulab[cx])
    M = from_cols(cols)
    lin = all(matvec(M, ulab[x]) == ulab[pmul(pmul(g, x), gi)]
              for x in C63)
    return M, lin
Mg = []
psi_ok = True
for g in KB_GENS:
    M, lin = psi(g)
    psi_ok &= lin and M is not None and is_symplectic(M) \
        and memV(mat_to_perm64(M))
    Mg.append(M)
oPsi, _, _ = make_bsgs_full([mat_to_perm64(M) for M in Mg], 64)
check("5d", "psi on the two K-bar generators: conjugation on C63 is "
      "LINEAR in the labels (verified on all 63 points each), symplectic, "
      "and a member of G (BSGS strip); <psi(gens)> has order 1,451,520 "
      "= |K-bar| = |G|  =>  psi: K-bar -> G is an ISOMORPHISM ONTO G "
      "(kernel trivial by order; multiplicativity by uniqueness of "
      "linear extension, argued in the docstring)",
      psi_ok and oPsi == SP_ORDER, "order %d" % oPsi)

def transport_copy(Gc):
    """push a K-bar subgroup through psi; returns (mats, ok)"""
    mats = {}
    ok = True
    for g in Gc:
        M, lin = psi(g)
        ok &= lin and M is not None and is_symplectic(M)
        mats[g] = M
    # multiplicativity spot-verified exhaustively on the copy
    Glist = list(Gc)
    for i in range(0, len(Glist), 17):
        for j in range(0, len(Glist), 23):
            a, b = Glist[i], Glist[j]
            ok &= mulM(mats[a], mats[b]) == mats[pmul(a, b)]
    return mats, ok

aS, bS, GcS = copies[sl_copies[0]]
matsS, okS = transport_copy(GcS)
imgS = set(matsS.values())
img28S = [rest28(label_perm(M)) for M in imgS]
odd_S = sorted(len(t) for t in orbits_of(
    [rest28(label_perm(matsS[aS])), rest28(label_perm(matsS[bS]))],
    range(28)))
even_S = sorted(len(t) for t in orbits_of(
    [label_perm(matsS[aS]), label_perm(matsS[bS])], even_forms))
invS_cls = sorted(set(cls28_of[p] for p in img28S
                      if p != pident(28) and pmul(p, p) == pident(28)))
S_S = cls28_sizes[invS_cls[0]] if len(invS_cls) == 1 else None
check("5e", "the SL(2,7)-LIFTING copy transported through psi: 168 "
      "distinct symplectic images, multiplicative on the sampled grid, "
      "all members of G; its 28-model involution class size EQUALS the "
      "K-bar-side size (coherence)",
      okS and len(imgS) == 168 and len(set(img28S)) == 168
      and all(memV(mat_to_perm64(M)) for M in imgS)
      and len(invS_cls) == 1 and S_S == S_schur,
      "involution class size %s (K-bar side %d)" % (S_S, S_schur))
if odd_S == [28]:
    verdict_direct = "BRIDGE"
elif odd_S == [7, 21]:
    verdict_direct = "FANO"
else:
    verdict_direct = "UNRECOGNIZED %s" % odd_S
check("5f", "THE DIRECT READ-OFF: psi(SL(2,7)-lifting copy) has odd-form "
      "orbits %s and even-form orbits %s  =>  it is the %s class"
      % (odd_S, even_S, verdict_direct),
      verdict_direct in ("BRIDGE", "FANO"),
      "bridge = [28]/[1,7,7,21]; Fano = [7,21]/[1,7,28]")

aP, bP, GcP = copies[sp_copies[0]]
matsP, okP = transport_copy(GcP)
imgP = set(matsP.values())
img28P = [rest28(label_perm(M)) for M in imgP]
odd_P = sorted(len(t) for t in orbits_of(
    [rest28(label_perm(matsP[aP])), rest28(label_perm(matsP[bP]))],
    range(28)))
even_P = sorted(len(t) for t in orbits_of(
    [label_perm(matsP[aP]), label_perm(matsP[bP])], even_forms))
invP_cls = sorted(set(cls28_of[p] for p in img28P
                      if p != pident(28) and pmul(p, p) == pident(28)))
S_P = cls28_sizes[invP_cls[0]] if len(invP_cls) == 1 else None
verdict_split = ("BRIDGE" if odd_P == [28]
                 else "FANO" if odd_P == [7, 21]
                 else "UNRECOGNIZED %s" % odd_P)
check("5g", "contrast: psi(a SPLIT-lifting copy) has odd orbits %s / even "
      "orbits %s => the %s class; involution class size %s agrees with "
      "the K-bar side (%d); the two transported copies land in the TWO "
      "DIFFERENT classes"
      % (odd_P, even_P, verdict_split, S_P, S_split),
      okP and len(imgP) == 168 and len(invP_cls) == 1
      and S_P == S_split and verdict_split in ("BRIDGE", "FANO")
      and verdict_split != verdict_direct)
consistent_45 = ((verdict_direct == "BRIDGE" and match_bridge_schur)
                 or (verdict_direct == "FANO" and match_bridge_split))
check("5h", "the direct route and the fingerprint route AGREE",
      consistent_45,
      "direct: SL(2,7)-lifting class = %s" % verdict_direct)
say("  CANONICALITY NOTE: any two isomorphisms K-bar -> G differ by an "
    "automorphism of G;")
say("  Out(Sp6(2)) = 1 [P cited, ATLAS], so the class correspondence "
    "does not depend on the")
say("  choice of psi.  Belt-and-braces: the automorphism-invariant "
    "fingerprints (sections 2-4)")
say("  give the same matching, computed.")
say("[t=%6.1fs] section 5 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 6 -- normalizer cross-check (exhaustive scans in K-bar)")
# ======================================================================
# sealed SM-024 (verify_envelope_normalizer.log): bridge class has
# N_G = PGL(2,7), index 2; Fano class SELF-NORMALIZING, index 1.
norm_cached = FLAGS.get("norm_scan")
if norm_cached:
    nN_schur, nN_split = norm_cached
    say("  [cache] exhaustive normalizer scans reloaded")
else:
    rng = np.random.default_rng(20260901)
    Wc = rng.integers(1, 2 ** 63, size=120, dtype=np.uint64)
    def hkeys(X):
        return (X.astype(np.uint64) * Wc).sum(axis=1)
    def scan_normalizer(a, b, Gset):
        keys = np.array(sorted({int((np.array(g, np.uint64) * Wc).sum())
                                for g in Gset}), np.uint64)
        h1 = np.array(a, np.uint8); h2 = np.array(b, np.uint8)
        nfound = 0
        for s in range(0, SP_ORDER, 90000):
            chunk = np.array(ENkb[s:s + 90000])
            Ginv2 = np.argsort(chunk, axis=1)
            ok = None
            conjs = []
            for hn in (h1, h2):
                B = hn[Ginv2]
                conj = np.take_along_axis(chunk, B.astype(np.intp),
                                          axis=1)
                m = np.isin(hkeys(conj), keys)
                ok = m if ok is None else (ok & m)
                conjs.append(conj)
            for r in np.nonzero(ok)[0].tolist():
                t1 = tuple(int(v) for v in conjs[0][r])
                t2 = tuple(int(v) for v in conjs[1][r])
                if t1 in Gset and t2 in Gset:     # exact, no hash trust
                    nfound += 1
        return nfound
    nN_schur = scan_normalizer(aS, bS, frozenset(GcS))
    nN_split = scan_normalizer(aP, bP, frozenset(GcP))
    flag_put("norm_scan", [int(nN_schur), int(nN_split)])
check("6a", "EXHAUSTIVE normalizer scan over all 1,451,520 elements of "
      "K-bar (conjugate BOTH generators into the stored 168-set, hash "
      "prefilter + exact verification): the SL(2,7)-lifting copy has "
      "|N| = %d, the split-lifting copy has |N| = %d"
      % (nN_schur, nN_split),
      nN_schur in (168, 336) and nN_split in (168, 336)
      and nN_schur != nN_split,
      "[N:H] = %d vs %d" % (nN_schur // 168, nN_split // 168))
# sealed cross-references
norm_consistent = (
    (verdict_direct == "FANO" and nN_schur == 168 and nN_split == 336)
    or (verdict_direct == "BRIDGE" and nN_schur == 336
        and nN_split == 168))
check("6b", "normalizer indices MATCH the sealed SM-024 pattern for the "
      "classes the direct route assigned (bridge: N = PGL(2,7) index 2; "
      "Fano: self-normalizing index 1) -- and the cached Stone U "
      "PGL27_scan (|N| = 336 over split copy 1) agrees",
      norm_consistent and WIT["PGL27_scan"][0] == 336,
      "a THIRD independent intrinsic invariant confirms the matching")
say("[t=%6.1fs] section 6 done" % (time.time() - T0))

# ======================================================================
banner("SECTION 7 -- bonus (nearly free via psi): A5 / S4 / A4 witnesses "
       "transported; fingerprints paired with lift types")
# ======================================================================
def SL2p(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if (a*d - b*c) % p == 1]
prof_SL25 = dict(sorted(Counter(mord2(M, 5) for M in SL2p(5)).items()))
prof_SL23 = dict(sorted(Counter(mord2(M, 3) for M in SL2p(3)).items()))
GL23 = [(a, b, c, d) for a in range(3) for b in range(3)
        for c in range(3) for d in range(3) if (a*d - b*c) % 3 != 0]
prof_GL23 = dict(sorted(Counter(mord2(M, 3) for M in GL23).items()))
A5m = closure([(1, 2, 0, 3, 4), (1, 2, 3, 4, 0)])
S4m = closure([(1, 0, 2, 3), (1, 2, 3, 0)])
A4m = closure([(1, 2, 0, 3), (0, 2, 3, 1)])
prof_A5, prof_S4, prof_A4 = (profile_of(A5m), profile_of(S4m),
                             profile_of(A4m))
fam_models = {
    "A5": (prof_A5, 60, [("2I = SL(2,5)", prof_SL25),
                         ("A5 x Z2 (split)", split_double(prof_A5))]),
    "S4": (prof_S4, 24, [("GL(2,3) = 2.S4", prof_GL23),
                         ("2 x S4 (split)", split_double(prof_S4))]),
    "A4": (prof_A4, 12, [("2T = SL(2,3)", prof_SL23),
                         ("A4 x Z2 (split)", split_double(prof_A4))]),
}
bonus_ok = True
for fam in ("A5", "S4", "A4"):
    prof_ref, sz, models = fam_models[fam]
    say("  -- %s (witnesses cached by the sealed Stone U hunt) --" % fam)
    for ci, ab in enumerate(WIT[fam]):
        a = tuple(ab[0]); b = tuple(ab[1])
        Gc = closure([a, b], cap=4 * sz)
        if len(Gc) != sz or profile_of(Gc) != prof_ref:
            bonus_ok = False; continue
        # lift type (recomputed)
        P = closure([lift_H(a), lift_H(b), anti], cap=4 * sz + 10)
        profP = profile_of(P)
        typ = next((nm for nm, pr in models if profP == pr), None)
        if typ is None:
            typ = ("2O (order 48, unique involution) [obs census %s]"
                   % profP if len(P) == 48 and profP.get(2, 0) == 1
                   else "UNRECOGNIZED %s" % profP)
        # transport + fingerprint
        Ma, la = psi(a); Mb, lb2 = psi(b)
        if not (la and lb2):
            bonus_ok = False; continue
        odd_o = sorted(len(t) for t in orbits_of(
            [rest28(label_perm(Ma)), rest28(label_perm(Mb))], range(28)))
        inv_cls_sz = sorted({gclass_size_kb(g) for g in Gc
                             if pord(g) == 2})
        say("     copy %d: K-bar involution class size(s) %s; 28-odd "
            "orbits %s; preimage -> %s"
            % (ci + 1, inv_cls_sz, odd_o, typ))
check("7a", "every cached A5/S4/A4 witness re-closed with the right order "
      "and census, its lift type recomputed, and its 28-model orbit "
      "fingerprint computed via psi (table above; scoped to the copies "
      "the sealed Stone U hunts found)", bonus_ok)
say("[t=%6.1fs] section 7 done" % (time.time() - T0))

# ======================================================================
banner("VERDICT")
# ======================================================================
if verdict_direct == "FANO":
    say("""
  THE ANSWER (computed three independent ways -- direct transport,
  intrinsic fingerprints, normalizer indices):

  *  The bitangent-transitive BRIDGE class of PSL(2,7) (IB's Lagrangian
     diag(M,(M^-1)^T); transitive on the 28, stab S3, even orbits
     [1,7,7,21]; N = PGL(2,7)) has involutions in the Sp6(2) class of
     size %d (square-sign +): it lifts SPLIT, to 2 x L2(7).
     The bridge embedding is NOT the spinorial one.

  *  The FANO-DOUBLED class (odd orbits [7,21], even orbits [1,7,28],
     self-normalizing) has involutions in the class of size %d
     (square-sign -): IT is the class that lifts to SL(2,7) inside
     H = 2.Sp6(2).  The spinorial embedding is the Fano-doubled one.
""" % (S_b, S_f))
elif verdict_direct == "BRIDGE":
    say("""
  THE ANSWER: the BRIDGE class (involution class size %d) IS the
  SL(2,7)-lifting class; the Fano-doubled class (size %d) lifts split.
  The bitangent embedding is the spinorial one.
""" % (S_b, S_f))
else:
    say("  INCONCLUSIVE: the transported copy's fingerprint was not "
        "recognized -- see FAILs above.")
say("""  SCOPE.  Class sizes / fingerprints: exhaustive over all involutions
  (both models), all elements of the two subgroups per class, and the
  cited orders.  Lift types: decisive per copy (explicit preimage
  closures).  The isomorphism psi is explicit and verified onto G; the
  class correspondence is choice-independent because Out(Sp6(2)) = 1
  [P cited, ATLAS] AND because the automorphism-invariant fingerprints
  agree (computed).  Normalizer scans: exhaustive over all 1,451,520
  elements of K-bar, both copies.  No claim about L2(7) copies of
  K-bar beyond those the sealed hunts found, EXCEPT: the two 28-model
  classes are genuinely the two fingerprint types, and each found K-bar
  copy belongs to one of them by the transported class correspondence.
  Not RH/GRH; no physical identification (Rule 3).""")
say("=" * 78)
say("RESULT: %d checks passed, %d failed%s"
    % (PASS, FAIL, ("   FAILED: %s" % FAILED) if FAILED else ""))
say("total time %.1fs" % (time.time() - T0))
LOG.close()
sys.exit(0 if FAIL == 0 else 1)
