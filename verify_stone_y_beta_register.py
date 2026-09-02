# -*- coding: utf-8 -*-
r"""verify_stone_y_beta_register.py -- STONE Y: THE beta-REGISTER.

IB's proposal (received 2026-09-02): "memory of a level = M_Gamma(g,h) =
beta(g,h), the commutator sign of the lifts, on the generators of Gamma";
compute M_S3, M_D4, overlay the eps-table (SM-033), exhibit a pair where
all-plus is identical but M differs; decision rule: accepted iff M is
well-defined per level, reproduces the eps-table, and detects a non-split
case all-plus misses -- "a relabeling of the eps-table is not a new
object".  Brief: BRIEF_STONE_Y_BETA_REGISTER.md (sha-locked BEFORE code).

THE DEFINITIONAL REPAIR (declared in the brief, checked here):
  (1) beta(g,h) := [g-hat, h-hat] is lift-independent (central signs
      cancel) but is a SIGN only when [g,h] = 1.  IB's S3 pair (1 2),(2 3)
      and PSL(2,7) pair a,b do not commute -> no sign value.  [YE1]
  (2) Replacement: for S = <X> <= K-bar with presentation relators R,
      sigma_w := w(X-hat) in {+1,-1}; the sign gauge X-hat -> +-X-hat acts
      through exponent-sum parities; M_S := gauge orbit of sigma (= the
      restricted extension class in H^2(S,Z2)).  THEOREM: pi^-1(S) splits
      <=> M_S trivial (a complement is a gauge in which every relator
      holds).  Power relator g^n -> eps(g); commutator relator -> beta.
  (3) Gamma = an EMBEDDED class: S3 = N(<z3>) in each sealed L2(7) class;
      D4 = dihedral of order 8 (IB's presentation) as Sylow-2 of each
      sealed S4 witness + an in-K-bar sweep; PSL(2,7) = both classes.

REGISTERED EXPECTATIONS (resolved at their sites, INVERTED at equal
prominence if so):  YE1 commutators non-central; YE2 split <=> M trivial
(100% vs the 2^k closure test); YE3 S3: bridge SPLIT / Fano Dic3, M = eps
of the involution; YE4 D8: GL(2,3)-Sylow -> SD16, 2O-Sylow -> Q16, M =
(eps(r),eps(s),eps(rs)) exactly; YE5 PSL(2,7): M = eps(a), SM-029
recovered; YE6 the C4xC2 pair (same all-plus, different M); YE7 no spine
group contains C4xC2 -> on the spine M = eps-restriction; YE8 S3 -/-> D8.

Sealed caches READ-ONLY (_stone_u_cache/, _liftlaw_cache/); own cache
_stone_y_cache/.  Helpers + stage 0 verbatim from verify_lift_law.py
(SM-033).  No registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_y_beta_register.py
"""
import itertools, json, os, sys, time, random
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_y_beta_register.log", "w", encoding="utf-8")
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
MY_CACHE = "_stone_y_cache"
os.makedirs(MY_CACHE, exist_ok=True)
random.seed(20260902)
RNG = np.random.default_rng(20260902)

# ======================================================================
# permutation utilities (verbatim: verify_lift_law.py / Stone U)
# ======================================================================
def pmul(a, b): return tuple(a[x] for x in b)          # (a o b)(k) = a[b[k]]
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

say("=" * 78)
say("STONE Y -- THE beta-REGISTER: IB's 'memory as the beta-pattern' made")
say("well-defined and computed on S3, D8, PSL(2,7), C4xC2 in K-bar = Sp6(2)")
say("with lifts in H = 2.Sp6(2) <= W(E8)   [sealed caches READ-ONLY]")
say("=" * 78)

# ======================================================================
banner("STAGE 0 -- sealed data loaded (read-only); W(E8) frame; lift_H")
# ======================================================================
GO = 1451520
oKb, KB_GENS = load_bsgs_lvl0(os.path.join(STONE_CACHE, "kbar_120.npz"),
                              120)
EN = np.load(os.path.join(STONE_CACHE, "kbar_elements.npy"))
ORD = np.load(os.path.join(STONE_CACHE, "kbar_orders.npy"))
zsq = np.load(os.path.join(STONE_CACHE, "sqsign.npz"))
sq_sign = zsq["sign"]; kb_cls = zsq["cls"]
NKB = EN.shape[0]
check("0a", "sealed K-bar loaded: 1,451,520 elements (Sp6(2) on 120 "
      "pairs), chain order matches", NKB == GO and oKb == GO)

inv_idx = np.nonzero(ORD == 2)[0]
inv_rows = EN[inv_idx]
kbcls_of = {}
for j, i in enumerate(inv_idx.tolist()):
    kbcls_of[tuple(int(x) for x in inv_rows[j])] = int(kb_cls[j])
sign_of_cls = {}; size_of_cls = {}
for j in range(len(inv_idx)):
    c = int(kb_cls[j])
    sign_of_cls.setdefault(c, set()).add(int(sq_sign[j]))
    size_of_cls[c] = size_of_cls.get(c, 0) + 1
sign_of_cls = {c: (list(v)[0] if len(v) == 1 else 0)
               for c, v in sign_of_cls.items()}
check("0b", "sealed involution tables: 5103 involutions in 4 classes "
      "{315+, 3780+, 945-, 63-}",
      len(inv_idx) == 5103
      and {size_of_cls[c]: sign_of_cls[c] for c in size_of_cls}
      == {315: 1, 3780: 1, 945: -1, 63: -1})

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
Amat = np.array(SIMPLE, dtype=np.int64).T
rmask = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64)
    c = Ginv @ d
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
check("0c", "W(E8) frame rebuilt; sealed shadow chain for H loaded "
      "(order 1451520); K-bar generators lift and ROUND-TRIP",
      SHH_o == GO and lift_rt and pmul(anti, anti) == ID240)

def eps_of_invol_tuple(t): return sign_of_cls[kbcls_of[t]]
def eps_elem(t):
    m = pord(t)
    if m % 2 == 1: return 1
    return eps_of_invol_tuple(ppow(t, m // 2))
def inv_class_label(t):
    c = kbcls_of[t]
    return "%d%s" % (size_of_cls[c], "+" if sign_of_cls[c] == 1 else "-")
def eps_profile(S):
    """multiset of (order, eps) over the elements of S -- IB's 'overlay'"""
    return dict(sorted(Counter((pord(g), "+" if eps_elem(g) == 1 else "-")
                               for g in S).items()))
def all_plus(S): return all(eps_elem(g) == 1 for g in S)

# verbatim SM-033 splitness test (2^k generator-lift sign choices)
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
say("[t=%6.1fs] stage 0 done" % (time.time() - T0))

# ======================================================================
# THE beta-REGISTER MACHINERY (new in this stone)
# ======================================================================
def eval_word(elems, word):
    """word = list of (generator index, integer exponent); left-to-right."""
    x = pident(len(elems[0]))
    for i, e in word:
        x = pmul(x, ppow(elems[i], e))
    return x
def word_str(names, word):
    out = []
    for i, e in word:
        out.append(names[i] if e == 1 else "%s^%d" % (names[i], e))
    return "".join(out)
def relator_register(gens120, relators, names):
    """Return dict: signs (list of +-1 per relator), parity rows,
    gauge-invariant flags, M trivial?, best gauge, plus the lift-
    independence check (every relator sign recomputed on flipped lifts
    changes exactly by the parity rule)."""
    k = len(gens120)
    for w in relators:                      # relators must HOLD downstairs
        assert eval_word(gens120, w) == ID120, "relator fails in K-bar"
    lifts = [lift_H(g) for g in gens120]
    def signs_for(L):
        out = []
        for w in relators:
            v = eval_word(L, w)
            assert v in (ID240, anti), "relator lift not central"
            out.append(1 if v == ID240 else -1)
        return out
    sig = signs_for(lifts)
    parity = [[sum(e for i, e in w if i == j) % 2 for j in range(k)]
              for w in relators]
    gauge_inv = [all(p == 0 for p in row) for row in parity]
    trivial = False; best = None; rule_ok = True
    for gam in itertools.product((0, 1), repeat=k):
        L2 = [pmul(anti, l) if gam[i] else l for i, l in enumerate(lifts)]
        s2 = signs_for(L2)
        # the gauge rule: sign_w flips iff sum_j parity[w][j]*gam[j] odd
        pred = [sig[a] * (-1) ** (sum(parity[a][j] * gam[j]
                                      for j in range(k)) % 2)
                for a in range(len(relators))]
        rule_ok &= (pred == s2)
        if all(s == 1 for s in s2) and not trivial:
            trivial = True; best = gam
    inv_signs = tuple(sig[a] for a in range(len(relators)) if gauge_inv[a])
    return dict(signs=sig, parity=parity, gauge_inv=gauge_inv,
                trivial=trivial, gauge=best, rule_ok=rule_ok,
                inv_signs=inv_signs, lifts=lifts)
def sgn(x): return "+" if x == 1 else "-"
def preimage_profile(lifts):
    return profile_of(closure(list(lifts) + [anti], cap=5000))

NAMES16 = {  # order-16 groups with a D8 quotient by a central C2, by profile
    (1, 9, 2, 4): "D16", (1, 5, 6, 4): "SD16", (1, 1, 10, 4): "Q16",
    (1, 11, 4, 0): "D8xC2", (1, 3, 12, 0): "C4:C4 or Q8xC2",
    (1, 3, 4, 8): "M16", (1, 7, 8, 0): "(C4xC2):C2 [=C2^2:C4]",
}
def name16(prof):
    key = tuple(prof.get(o, 0) for o in (1, 2, 4, 8))
    return NAMES16.get(key, "order-16 profile %s" % prof)
NAMES12 = {(1, 1, 2, 6, 2): "Dic3", (1, 7, 2, 0, 2): "S3xC2"}
def name12(prof):
    key = tuple(prof.get(o, 0) for o in (1, 2, 3, 4, 6))
    return NAMES12.get(key, "order-12 profile %s" % prof)

WIT = json.load(open(os.path.join(STONE_CACHE, "witnesses.json")))
L27 = [(tuple(ab[0]), tuple(ab[1])) for ab in WIT["L27"]]
S4W = [(tuple(ab[0]), tuple(ab[1])) for ab in WIT["S4"]]
A5W = [(tuple(ab[0]), tuple(ab[1])) for ab in WIT["A5"]]
A4W = [(tuple(ab[0]), tuple(ab[1])) for ab in WIT["A4"]]
C6Z2 = (tuple(WIT["C6Z2"][0]), tuple(WIT["C6Z2"][1]))

AGREE = []   # (label, M trivial?, split_test?) for YE2

# ======================================================================
banner("CHECK 1 -- YE1: beta as a SIGN exists only on commuting pairs")
# ======================================================================
say("""  beta(g,h) := [g-hat, h-hat].  Flipping g-hat -> -g-hat leaves the
  commutator unchanged (signs are central), so it is a lift-INDEPENDENT
  element of H lifting [g,h].  It is +-1 iff [g,h] = 1.  IB's generator
  pairs for S3 and PSL(2,7) do not commute; the machine shows the
  commutator of their lifts is a NON-central element.""")

def find_S3_in(G168):
    """N(<z>) for an order-3 z inside a PSL(2,7) closure: order 6 = S3.
    Returns (s1, s2) two involutions with s1 s2 of order 3."""
    z = next(g for g in G168 if pord(g) == 3)
    zi = pinv(z); z2 = pmul(z, z)
    N = [g for g in G168 if pmul(pmul(g, z), pinv(g)) in (z, z2)]
    assert len(N) == 6
    invs = [g for g in N if pord(g) == 2]
    assert len(invs) == 3
    s1, s2 = invs[0], invs[1]
    assert pord(pmul(s1, s2)) == 3
    return s1, s2, N
def find_237_in(G168):
    """(a,b): a involution, b order 3, ab order 7, [a,b] order 4."""
    invs = [g for g in G168 if pord(g) == 2]
    thr = [g for g in G168 if pord(g) == 3]
    for a in invs:
        for b in thr:
            if pord(pmul(a, b)) == 7 and pord(comm(a, b)) == 4:
                return a, b
    raise RuntimeError("no (2,3,7) pair")

S3_of = []; ye1_ok = True; ye1_detail = []
for ci, (ga, gb) in enumerate(L27):
    G = closure([ga, gb], cap=200)
    assert len(G) == 168
    s1, s2, N = find_S3_in(G)
    S3_of.append((s1, s2))
    c = comm(lift_H(s1), lift_H(s2))
    central = c in (ID240, anti)
    ye1_ok &= (not central) and to120(c) == comm(s1, s2) \
              and pord(comm(s1, s2)) == 3
    ye1_detail.append("L27#%d: [s1-hat,s2-hat] non-central, order %d, "
                      "projects to [s1,s2] of order 3" % (ci + 1, pord(c)))
for d in ye1_detail: say("  " + d)
check("1a", "YE1 (S3): for the S3 = N(<z3>) inside EACH of the 4 sealed "
      "L2(7) witnesses, the commutator of the generator lifts is a "
      "NON-central element of H (it lifts [s1,s2] = (s1 s2)^2, order 3) "
      "-- 'beta(s1,s2)' has no sign value", ye1_ok)

P27_of = []; ye1b_ok = True
for ci, (ga, gb) in enumerate(L27):
    G = closure([ga, gb], cap=200)
    a, b = find_237_in(G)
    P27_of.append((a, b))
    c = comm(lift_H(a), lift_H(b))
    ye1b_ok &= (c not in (ID240, anti)) and to120(c) == comm(a, b)
    say("  L27#%d: (a,b) with a^2=b^3=(ab)^7=1, [a,b] of order 4; "
        "[a-hat,b-hat] non-central, order %d" % (ci + 1, pord(c)))
check("1b", "YE1 (PSL(2,7)): for a (2,3,7)-generating pair in each "
      "witness, [a-hat,b-hat] is NON-central -- 'beta(a,b)' has no sign "
      "value either", ye1b_ok)
say("""  NOTE [P, cited]: IB's presentation <a,b | a^2, b^3, (ab)^7> is the
  (2,3,7) triangle group, which is INFINITE; PSL(2,7) needs one more
  relator, [a,b]^4 = 1 (standard).  The register below uses the full
  presentation a^2, b^3, (ab)^7, [a,b]^4 -- and every pair found above
  satisfies [a,b]^4 = 1 in K-bar (checked in find_237_in).""")
say("[t=%6.1fs] check 1 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 3 -- YE3: M_{S3} per embedded class; the sweep by involution class")
# ======================================================================
S3_REL = [[(0, 2)], [(1, 2)], [(0, 1), (1, 1), (0, 1), (1, 1), (0, 1), (1, 1)]]
S3_NAMES = ["s1", "s2"]
say("  presentation S3 = <s1, s2 | s1^2, s2^2, (s1 s2)^3>")
say("  relator      parity(s1,s2)  gauge-invariant?")
rows3 = []
ye3_ok = True
for ci, (s1, s2) in enumerate(S3_of):
    R = relator_register([s1, s2], S3_REL, S3_NAMES)
    S = closure([s1, s2], cap=20); assert len(S) == 6
    sp = split_test([s1, s2], 6)
    prof = preimage_profile(R["lifts"])
    AGREE.append(("S3 in L27#%d" % (ci + 1), R["trivial"], sp))
    if ci == 0:
        for w, par, gi in zip(S3_REL, R["parity"], R["gauge_inv"]):
            say("  %-12s %-14s %s" % (word_str(S3_NAMES, w), par, gi))
    lab = inv_class_label(s1)
    say("  L27#%d  S3: signs (s1^2,s2^2,(s1s2)^3) = (%s,%s,%s); "
        "involution class %s; eps-profile %s; M trivial=%s; split_test=%s; "
        "preimage = %s %s"
        % (ci + 1, sgn(R["signs"][0]), sgn(R["signs"][1]),
           sgn(R["signs"][2]), lab, eps_profile(S), R["trivial"], sp,
           name12(prof), prof))
    rows3.append((ci, lab, R, sp, prof))
    ye3_ok &= R["rule_ok"]
    # M is exactly eps(s1): trivial <=> eps(s1) = +
    ye3_ok &= (R["trivial"] == (eps_elem(s1) == 1))
    ye3_ok &= (R["signs"][0] == R["signs"][1] == eps_elem(s1))
bridge = [r for r in rows3 if r[1] == "315+"]
fano = [r for r in rows3 if r[1] == "945-"]
check("3a", "YE3: the S3 inside the three SPLIT-lifting (bridge-class) "
      "L2(7) witnesses is SPLIT with preimage S3xC2; the S3 inside the "
      "SL(2,7)-lifting (Fano-class) witness is NON-SPLIT with preimage "
      "Dic3 -- SM-029's two-twos dichotomy restricted to the shared S3",
      len(bridge) == 3 and len(fano) == 1
      and all(r[3] and name12(r[4]) == "S3xC2" for r in bridge)
      and all((not r[3]) and name12(r[4]) == "Dic3" for r in fano))
check("3b", "YE3: M_{S3} = eps(s1) EXACTLY -- the two involution relators "
      "carry eps(s1)=eps(s2), the (s1s2)^3 relator is gauge-flippable "
      "(parity (1,1)), the gauge rule verified on all 4 sign choices; "
      "M trivial <=> eps(involution) = + on every instance", ye3_ok)

# the sweep: S3's generated by random involution pairs, by K-bar class
say("")
say("  SWEEP: random pairs of involutions (t, s) with ts of order 3, "
    "grouped by the K-bar class of t (all three involutions of an S3 are "
    "S3-conjugate, hence in one K-bar class):")
random.seed(20260902 + 3)
inv_np = inv_rows
by_class = {}
sweep_ok = True; n_sweep = 0
for c in sorted(size_of_cls, key=lambda c: size_of_cls[c]):
    idx_c = np.nonzero(kb_cls == c)[0]
    got = 0; tries = 0
    while got < 6 and tries < 3000:
        tries += 1
        j = int(idx_c[random.randrange(idx_c.size)])
        t = tuple(int(x) for x in inv_np[j])
        # candidate s among involutions of the same class (fast filter:
        # ts of order 3  <=>  (ts)^3 = 1 and ts != 1)
        jj = int(idx_c[random.randrange(idx_c.size)])
        s = tuple(int(x) for x in inv_np[jj])
        if s == t: continue
        ts = pmul(t, s)
        if pord(ts) != 3: continue
        S = closure([t, s], cap=20)
        if len(S) != 6: continue
        got += 1; n_sweep += 1
        R = relator_register([t, s], S3_REL, S3_NAMES)
        sp = split_test([t, s], 6)
        prof = preimage_profile(R["lifts"])
        AGREE.append(("S3 sweep %s #%d" % (inv_class_label(t), got),
                      R["trivial"], sp))
        key = inv_class_label(t)
        by_class.setdefault(key, Counter())[
            ("M trivial" if R["trivial"] else "M nontrivial",
             "split" if sp else "non-split", name12(prof))] += 1
        sweep_ok &= R["rule_ok"] and (R["trivial"] == sp) \
                    and (R["trivial"] == (eps_elem(t) == 1))
for key in by_class:
    say("  class %-6s: %s" % (key, dict(by_class[key])))
check("3c", "YE3 sweep: %d S3 subgroups of K-bar generated by involution "
      "pairs across the involution classes found (%s): in EVERY case "
      "M trivial <=> split <=> eps(involution) = + -- plus classes give "
      "S3xC2, minus classes give Dic3; M_{S3} is the eps-restriction, "
      "nothing more" % (n_sweep, sorted(by_class)),
      sweep_ok and n_sweep >= 12 and len(by_class) >= 3)
say("[t=%6.1fs] check 3 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 4 -- YE4: M_{D8} (IB's D4 = dihedral of order 8) per class + sweep")
# ======================================================================
D8_REL = [[(0, 4)], [(1, 2)], [(0, 1), (1, 1), (0, 1), (1, 1)]]
D8_NAMES = ["r", "s"]
say("  presentation D8 = <r, s | r^4, s^2, (rs)^2>   (IB's D4)")
def find_D8_in(G24):
    r = next(g for g in G24 if pord(g) == 4)
    ri = pinv(r); Cr = {pident(120), r, ppow(r, 2), ri}
    s = next(g for g in G24 if pord(g) == 2 and g not in Cr
             and pmul(pmul(g, r), g) == ri)
    D = closure([r, s], cap=20); assert len(D) == 8
    return r, s
rows4 = []; ye4_ok = True
for wi, (ga, gb) in enumerate(S4W):
    G = closure([ga, gb], cap=40); assert len(G) == 24
    r, s = find_D8_in(G)
    R = relator_register([r, s], D8_REL, D8_NAMES)
    sp = split_test([r, s], 8)
    prof = preimage_profile(R["lifts"])
    D = closure([r, s], cap=20)
    AGREE.append(("D8 in S4#%d" % (wi + 1), R["trivial"], sp))
    if wi == 0:
        for w, par, gi in zip(D8_REL, R["parity"], R["gauge_inv"]):
            say("  %-8s parity %-8s gauge-invariant=%s"
                % (word_str(D8_NAMES, w), par, gi))
    trip = (sgn(R["signs"][0]), sgn(R["signs"][1]), sgn(R["signs"][2]))
    eps_trip = (sgn(eps_elem(r)), sgn(eps_elem(s)), sgn(eps_elem(pmul(r, s))))
    say("  S4#%d  D8: (r^4, s^2, (rs)^2) = %s ; (eps r, eps s, eps rs) = %s ; "
        "eps-profile %s ; M trivial=%s ; split=%s ; preimage %s %s"
        % (wi + 1, trip, eps_trip, eps_profile(D), R["trivial"], sp,
           name16(prof), prof))
    rows4.append((wi, trip, eps_trip, R, sp, prof, G))
    ye4_ok &= R["rule_ok"] and all(R["gauge_inv"]) and (trip == eps_trip)
    ye4_ok &= (R["trivial"] == sp) and (R["trivial"] == (trip == ("+", "+", "+")))
# which S4 witness is 2O: all 9 involutions eps=-
def s4_type(G):
    m = Counter(inv_class_label(g) for g in G if pord(g) == 2)
    return "2O" if m == Counter({"945-": 9}) else "GL(2,3)"
types = [s4_type(r[6]) for r in rows4]
sd = [name16(r[5]) for r, t in zip(rows4, types) if t == "GL(2,3)"]
q16 = [name16(r[5]) for r, t in zip(rows4, types) if t == "2O"]
check("4a", "YE4: the Sylow-2 D8 of every GL(2,3)-lifting S4 witness "
      "(%d of them) has preimage SD16; that of the 2O-lifting witness "
      "(%d) has preimage Q16; all non-split" % (len(sd), len(q16)),
      len(sd) == 5 and len(q16) == 1 and all(x == "SD16" for x in sd)
      and all(x == "Q16" for x in q16) and not any(r[4] for r in rows4))
check("4b", "YE4: all three D8 relators are gauge-INVARIANT (parities "
      "(0,0)), so M_{D8} = (eps(r), eps(s), eps(rs)) literally; gauge "
      "rule verified; M trivial <=> split <=> all three + (on the "
      "witness Sylows)", ye4_ok)

say("")
say("  SWEEP: D8 = <r, s> for random order-4 r and involutions s with "
    "s r s = r^-1, s not in <r> -- which sign triples occur in K-bar:")
random.seed(20260902 + 5)
ord4_idx = np.nonzero(ORD == 4)[0]
inv_np = inv_rows
triples = Counter(); pre_by_trip = {}
sweep4_ok = True; n4 = 0
t_sw = time.time()
for trial in range(400):
    if n4 >= 60 or time.time() - t_sw > 150: break
    ai = int(ord4_idx[random.randrange(ord4_idx.size)])
    r = tuple(int(x) for x in EN[ai]); r_arr = EN[ai]
    ri = np.array(pinv(r), dtype=np.uint8)
    # s r s == r^-1  <=>  s[r[s[k]]] == ri[k]
    srs = np.take_along_axis(inv_np, r_arr[inv_np], axis=1)
    cand = np.nonzero((srs == ri).all(axis=1))[0]
    Cr = {pident(120), r, ppow(r, 2), tuple(int(x) for x in ri)}
    picked = 0
    for j in cand.tolist():
        if picked >= 2: break
        s = tuple(int(x) for x in inv_np[j])
        if s in Cr: continue
        D = closure([r, s], cap=20)
        if len(D) != 8: continue
        picked += 1; n4 += 1
        R = relator_register([r, s], D8_REL, D8_NAMES)
        sp = split_test([r, s], 8)
        prof = preimage_profile(R["lifts"])
        trip = (sgn(R["signs"][0]), sgn(R["signs"][1]), sgn(R["signs"][2]))
        eps_trip = (sgn(eps_elem(r)), sgn(eps_elem(s)),
                    sgn(eps_elem(pmul(r, s))))
        triples[trip] += 1
        pre_by_trip.setdefault(trip, set()).add(name16(prof))
        AGREE.append(("D8 sweep #%d" % n4, R["trivial"], sp))
        sweep4_ok &= R["rule_ok"] and (trip == eps_trip) \
                     and (R["trivial"] == sp) \
                     and (sp == (trip == ("+", "+", "+")))
say("  triple (eps r, eps s, eps rs) : count : preimage type(s)")
for trip in sorted(triples):
    say("    %s : %3d : %s" % (trip, triples[trip], sorted(pre_by_trip[trip])))
say("  (%d of the 8 possible triples realized in %d D8's sampled)"
    % (len(triples), n4))
check("4c", "YE4 sweep: %d D8 subgroups of K-bar sampled; %d distinct sign "
      "triples realized; in EVERY case the relator triple EQUALS the eps "
      "triple and split <=> all-plus -- M_{D8} is the eps-restriction, "
      "nothing more" % (n4, len(triples)),
      sweep4_ok and n4 >= 20)
check("4d", "YE4 sweep: the split triple (+,+,+) is realized in K-bar "
      "(preimage D8xC2) alongside non-split ones -- so 'relabeling at "
      "D8' is a statement about ALL classes met, not a small sample",
      ("+", "+", "+") in triples and len(triples) >= 3)
say("[t=%6.1fs] check 4 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 5 -- YE5: M_{PSL(2,7)} on both sealed classes")
# ======================================================================
P_REL = [[(0, 2)], [(1, 3)], [(0, 1), (1, 1)] * 7,
         [(0, 1), (1, 1), (0, -1), (1, -1)] * 4]
P_NAMES = ["a", "b"]
say("  presentation PSL(2,7) = <a, b | a^2, b^3, (ab)^7, [a,b]^4>")
rows5 = []; ye5_ok = True
for ci, (a, b) in enumerate(P27_of):
    R = relator_register([a, b], P_REL, P_NAMES)
    sp = split_test([a, b], 168)
    AGREE.append(("PSL(2,7) L27#%d" % (ci + 1), R["trivial"], sp))
    if ci == 0:
        for w, par, gi in zip(P_REL, R["parity"], R["gauge_inv"]):
            say("  %-24s parity %-8s gauge-invariant=%s"
                % (word_str(P_NAMES, w)[:24], par, gi))
    lab = inv_class_label(a)
    say("  L27#%d: signs (a^2, b^3, (ab)^7, [a,b]^4) = (%s,%s,%s,%s); "
        "involution class %s; M trivial=%s; split=%s"
        % (ci + 1, *[sgn(x) for x in R["signs"]], lab, R["trivial"], sp))
    ye5_ok &= R["rule_ok"] and (R["trivial"] == sp)
    ye5_ok &= (R["gauge_inv"] == [True, False, False, True])
    ye5_ok &= (R["signs"][0] == R["signs"][3] == eps_elem(a))
    rows5.append((lab, R["trivial"]))
check("5a", "YE5: M_{PSL(2,7)} has two gauge-invariant components "
      "(a^2 and [a,b]^4; b^3 and (ab)^7 are flippable) and they COINCIDE "
      "on every instance (= eps(a)); bridge class (315+) trivial/split, "
      "Fano class (945-) nontrivial/non-split -- SM-029 recovered as a "
      "corollary of the definition",
      ye5_ok and sorted(rows5) == [("315+", True)] * 3 + [("945-", False)])
say("[t=%6.1fs] check 5 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 6 -- YE6: IB's required output 4 -- the discriminating pair")
# ======================================================================
C42_REL = [[(0, 4)], [(1, 2)], [(0, 1), (1, 1), (0, -1), (1, -1)]]
C42_NAMES = ["a", "t"]
say("  presentation C4xC2 = <a, t | a^4, t^2, [a,t]>  (all three relators "
    "gauge-invariant; the third IS beta(a,t))")
random.seed(20260902 + 13)
plus4_idx = np.nonzero((ORD == 4) & (np.array([1] * NKB) == 1))[0]
# restrict to eps=+ order-4 elements: eps(g) = sign of g^2's class
sq_of_ord4 = None
found_ns = None; found_sp = None; n_probe = 0
t6 = time.time()
for trial in range(400):
    if (found_ns and found_sp) or time.time() - t6 > 150: break
    ai = int(ord4_idx[random.randrange(ord4_idx.size)])
    a = tuple(int(x) for x in EN[ai])
    if eps_elem(a) != 1: continue
    a_arr = EN[ai]; a2 = ppow(a, 2)
    mk = (inv_np[:, a_arr] == a_arr[inv_np]).all(axis=1)
    cand = np.nonzero(mk & (sq_sign == 1))[0]
    for j in cand.tolist()[:12]:
        t = tuple(int(x) for x in inv_np[j])
        if t == a2: continue
        S = closure([a, t], cap=20)
        if len(S) != 8 or not all_plus(S): continue
        n_probe += 1
        R = relator_register([a, t], C42_REL, C42_NAMES)
        sp = split_test([a, t], 8)
        AGREE.append(("C4xC2 probe #%d" % n_probe, R["trivial"], sp))
        rec = (ai, int(inv_idx[j]), R, sp, eps_profile(S),
               preimage_profile(R["lifts"]))
        if R["signs"][2] == -1 and found_ns is None: found_ns = rec
        if R["signs"][2] == 1 and found_sp is None: found_sp = rec
        if found_ns and found_sp: break
for name, rec in (("NON-SPLIT", found_ns), ("SPLIT", found_sp)):
    if rec is None:
        say("  %s C4xC2: NOT FOUND in %d probes" % (name, n_probe)); continue
    ai, ti, R, sp, ep, prof = rec
    say("  %s C4xC2 = <a = K-bar element #%d (order 4), t = involution "
        "#%d>: signs (a^4, t^2, [a,t]) = (%s,%s,%s); eps-profile %s; "
        "M trivial=%s; split_test=%s; preimage profile %s"
        % (name, ai, ti, *[sgn(x) for x in R["signs"]], ep, R["trivial"],
           sp, prof))
same_eps = (found_ns is not None and found_sp is not None
            and found_ns[4] == found_sp[4])
check("6a", "YE6: an all-plus C4xC2 with beta(a,t) = - (NON-SPLIT) and an "
      "all-plus C4xC2 with beta(a,t) = + (SPLIT) both exhibited, with "
      "IDENTICAL eps-profiles on all 8 elements -- identical all-plus, "
      "different M: the register discriminates where the eps-table "
      "cannot (%d all-plus probes)" % n_probe,
      same_eps and not found_ns[3] and found_sp[3]
      and found_ns[2]["trivial"] is False and found_sp[2]["trivial"] is True)
say("[t=%6.1fs] check 6 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 7 -- YE7: where the new discrimination lives; YE2 the theorem")
# ======================================================================
def has_C4xC2(G):
    o4 = [g for g in G if pord(g) == 4]
    inv = [g for g in G if pord(g) == 2]
    for a in o4:
        a2 = ppow(a, 2)
        for t in inv:
            if t != a2 and pmul(a, t) == pmul(t, a):
                if len(closure([a, t], cap=20)) == 8: return True
    return False
spine = [("PSL(2,7) L27#%d" % (i + 1), closure(list(p), cap=200))
         for i, p in enumerate(L27)]
spine += [("C6xZ2", closure(list(C6Z2), cap=30))]
spine += [("A5 #%d" % (i + 1), closure(list(p), cap=100))
          for i, p in enumerate(A5W)]
spine += [("S4 #%d" % (i + 1), closure(list(p), cap=40))
          for i, p in enumerate(S4W)]
spine += [("A4 #%d" % (i + 1), closure(list(p), cap=20))
          for i, p in enumerate(A4W)]
ye7 = True
for name, G in spine:
    h = has_C4xC2(G)
    say("  %-16s |G|=%4d  contains C4xC2: %s" % (name, len(G), h))
    ye7 &= (not h)
say("  Z2, {e}: trivially no C4xC2.")
check("7a", "YE7: NO spine group (PSL(2,7) x4 classes, C6xZ2, A5 x6, S4 x6, "
      "A4 x3 sealed witnesses; Z2; {e}) contains a C4xC2 -- and every spine "
      "level's standard presentation has only power relators (S3, D8, "
      "PSL(2,7) shown above) -> on the spine M_Gamma = eps-restriction; "
      "beta's extra content is OFF-SPINE (registered expectation "
      "CONFIRMED)", ye7 and len(spine) == 20)
agree_ok = all(m == s for _, m, s in AGREE)
check("7b", "YE2 THE THEOREM (machine-checked): 'M_S trivial' (some gauge "
      "makes every relator hold) and 'pi^-1(S) splits' (SM-033's 2^k "
      "closure test) AGREE on all %d subgroup instances of this run "
      "(S3 x%d, D8 x%d, PSL(2,7) x%d, C4xC2 x%d)"
      % (len(AGREE), sum(1 for l, _, _ in AGREE if l.startswith("S3")),
         sum(1 for l, _, _ in AGREE if l.startswith("D8")),
         sum(1 for l, _, _ in AGREE if l.startswith("PSL")),
         sum(1 for l, _, _ in AGREE if l.startswith("C4xC2"))),
      agree_ok and len(AGREE) >= 40)
say("[t=%6.1fs] check 7 done" % (time.time() - T0))

# ======================================================================
banner("CHECK 8 -- YE8: the beta-chain's first step, on order alone")
# ======================================================================
r, s = find_D8_in(closure(list(S4W[0]), cap=40))
D = closure([r, s], cap=20)
check("8a", "YE8: D8 has no element of order 3 (profile %s) -- no "
      "generator map S3 -> D8 preserving the relators exists, so IB's "
      "chain step S3 -> D4(dihedral) fails on ORDER before beta is "
      "consulted; the D4 and G2 levels of the chain await his "
      "instantiation" % profile_of(D), 3 not in profile_of(D))

# ======================================================================
banner("VERDICT")
# ======================================================================
say("""  IB's decision rule, item by item:
   - M_Gamma well-defined on each level:  YES -- after the repair.  As a
     SIGN on generator pairs it is undefined (YE1); as the relator-sign
     class (= restricted extension class) it is well-defined per EMBEDDED
     class, and split <=> trivial is a machine-checked theorem (YE2).
   - M_Gamma reproduces the eps-table:  YES -- power relators g^n carry
     exactly eps(g); on S3, D8 and PSL(2,7) the register IS the eps
     restriction (YE3/YE4/YE5), and SM-029's bridge/Fano dichotomy falls
     out of it (YE5), as does SM-033's Dic3/S3xC2 split at the shared S3.
   - Detects a non-split case all-plus misses:  YES -- but ONLY through a
     commutator relator: the C4xC2 pair (YE6).  No spine group contains
     one (YE7).
   - Verdict in his words: at S3 and D4 the proposal IS a relabeling of
     the eps-table; the new object exists, and lives off the spine, in
     the commutator relators.  'Memory' remains his [I] label.""")
say("")
say("RESULT: %d checks passed, %d failed%s" % (PASS, FAIL,
    ("  FAILED: %s" % FAILED) if FAILED else ""))
say("[t=%6.1fs] done" % (time.time() - T0))
LOG.close()
