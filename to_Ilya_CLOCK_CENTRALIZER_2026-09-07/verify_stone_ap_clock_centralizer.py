# -*- coding: utf-8 -*-
r"""verify_stone_ap_clock_centralizer.py -- STONE AP: THE CLOCK'S LINEAR CENTRALIZER

Brief: BRIEF_STONE_AP_CLOCK_CENTRALIZER.md (lock BRIEF_STONE_AP_LOCK.sha256, re-verified as check AP0).

Question: IB asks for a canonical (2,3,7) pair (a,b) of one of the still point's 36 PSL(2,7) copies so he can
test whether the clock Psi fixes exactly one of the three C2's of his V4.  The house answers without a choice:
every such C2 is an element of W(E7) on the 56 (SM-013 lift; SM-040 board), so the question is whether ANY
element of W(E7) commutes with Psi.  Compute C_S56(Psi) in full (69,984), intersect with W(E7); instantiate
his test on a bridge copy built here for every (2,3,7) pair; settle his D vs dL bookkeeping.

BARS: AP0 lock; AP1 the board (pair type = sign of inner product; iota and the seven reflections linear,
traces -7 and 5); AP2 the centralizer (69,984 explicit, all commute, 231 involutions); AP3 REGISTERED:
C_S56(Psi) meets W(E7) in {1}; AP4 a bridge copy (order 168, orbits [28,28], fixed points 56/8/2/4/0/0,
traces 7/-1/1/-1/0/0 = chi7); AP5 his test for all 336 pairs: 0 of 3 C2's Psi-normalized, every pair;
AP6 D = lost - created equals c_nt(G) - c_nt(H) on every step, D(A4,V4) = 0; AP7 REGISTERED GUESS: best
pair-type agreement among the 231 = 1432/1540 with maximizers of type 2^27 1^2 (resolvable INVERTED).

Machinery: scar56_data.json READ-ONLY; the E8/E7/pair-type replay VERBATIM from
verify_stone_af_three_eighteens.py (= verify_stone_ac_parity_rule.py 55-108); closure by BFS; classes by
brute force; own cache _stone_ap_cache/witnesses_ap.json.

DISCIPLINE: compute, never assert; registered expectations resolvable INVERTED at equal prominence; exact
arithmetic; sealed caches READ-ONLY; no registry/git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ap_clock_centralizer.py
"""
import itertools, json, os, sys, time, random, hashlib
from collections import Counter
from fractions import Fraction
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LOG = open("verify_stone_ap_clock_centralizer.log", "w", encoding="utf-8")
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
random.seed(20260907)

say("=" * 78); say("STONE AP -- THE CLOCK'S LINEAR CENTRALIZER (IB's Psi-marker test answered without a choice)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AP_CLOCK_CENTRALIZER.md"; LOCK = open("BRIEF_STONE_AP_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AP0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AP_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
jsha = hashlib.sha256(open("scar56_data.json", "rb").read()).hexdigest()
note("scar56_data.json sha256 %s (READ-ONLY)" % jsha[:16])

# =====================================================================
# VERBATIM from verify_stone_af_three_eighteens.py (= verify_stone_ac_parity_rule.py, lines 55-108)
# =====================================================================
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=8):
    if signs.count(-1) % 2 == 0: roots.append(tuple(signs))
ridx = {r: k for k, r in enumerate(roots)}
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
SIMPLE = [(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0),(0,-2,2,0,0,0,0,0),
          (0,0,-2,2,0,0,0,0),(0,0,0,-2,2,0,0,0),(0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0)]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
Gm = np.array(GRAM, dtype=np.int64); Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
coords = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64); coords.append([int(x) for x in Ginv @ d])
rmask = [int(sum((coords[k][i] & 1) << i for i in range(8))) for k in range(240)]
qvals = []
for m in range(256):
    cv = np.array([(m >> i) & 1 for i in range(8)], dtype=np.int64); qvals.append(((int(cv @ Gm @ cv)) // 2) % 2)
def Bform(x, y): return qvals[x ^ y] ^ qvals[x] ^ qvals[y]
ALPHA_R = SIMPLE[0]; ALPHA = rmask[ridx[ALPHA_R]]
D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]; vidx = {v: k for k, v in enumerate(verts)}
PSI, IOTA, COMP, EDGES = D["PSI"], D["IOTA"], D["COMP"], D["EDGES"]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]; B56 = [r for r in roots if dot4(r, ALPHA_R) == 1]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi[i]] for i in range(7)]; BETAM = [rmask[ridx[b]] for b in BETA]
root_of = {}
for r in B56: root_of[vidx[tuple(dot4(r, b) for b in BETA)]] = r
assert len(root_of) == 56
mask = {k: rmask[ridx[root_of[k]]] for k in range(56)}
def ptype(k, l):
    s = mask[k] ^ mask[l]
    if s == ALPHA: return "v"
    return "P" if qvals[s] == 1 else "S"
W2 = {k: tuple(2*x - a for x, a in zip(root_of[k], ALPHA_R)) for k in range(56)}
ipmap = Counter((ptype(k, l), sum(a*b for a, b in zip(W2[k], W2[l]))) for k in range(56) for l in range(56) if k != l)
PAIRS = [(k, l) for k in range(56) for l in range(k + 1, 56)]
def compose(p, q): return [p[q[k]] for k in range(56)]
def ppow(p, e):
    x = list(range(56))
    for _ in range(e): x = compose(p, x)
    return x
def score(p): return sum(1 for k, l in PAIRS if ptype(p[k], p[l]) == ptype(k, l)) / len(PAIRS)
# (AF2 verbatim) the seven simple reflections on the board
def refl(r, b): c = dot4(r, b); return tuple(x - c * y for x, y in zip(r, b))
vert_of_root = {root_of[k]: k for k in range(56)}
S7 = [[vert_of_root[refl(root_of[k], b)] for k in range(56)] for b in BETA]
assert all(sorted(s) == list(range(56)) for s in S7)
# =====================================================================

# ---------------------------------------------------------------- helpers (own)
IDP = list(range(56))
def cyc(p):
    seen = set(); c = []
    for k in range(len(p)):
        if k in seen: continue
        o = 0; x = k
        while x not in seen: seen.add(x); o += 1; x = p[x]
        c.append(o)
    return tuple(sorted(c, reverse=True))
def ctype(p):
    c = Counter(cyc(p)); return " ".join("%d^%d" % (l, m) for l, m in sorted(c.items(), reverse=True))
def porder(p):
    x = IDP; n = 0
    while True:
        x = compose(p, x); n += 1
        if x == IDP: return n
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def fixed(p): return sum(1 for k in range(56) if p[k] == k)
def kept(p): return sum(1 for k, l in PAIRS if ptype(p[k], p[l]) == ptype(k, l))   # exact integer, out of 1540
def islinear(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
IP = {(k, l): sum(a*b for a, b in zip(W2[k], W2[l])) for k in range(56) for l in range(56)}
NORM = IP[(0, 0)]
def trace7(p): return Fraction(7 * sum(IP[(p[k], k)] for k in range(56)), 56 * NORM)   # exact
def closure(gens, cap):
    seen = {tuple(IDP)}; frontier = [IDP]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = compose(s, g); t = tuple(h)
                if t not in seen:
                    seen.add(t); nxt.append(h)
                    if len(seen) > cap: return None
        frontier = nxt
    return sorted(seen)
def conj_classes(G):
    Gs = [list(g) for g in G]; invs = {g: tuple(pinv(list(g))) for g in G}
    left = set(G); classes = []
    while left:
        x = next(iter(left)); cl = set()
        for g in Gs:
            cl.add(tuple(compose(compose(g, list(x)), list(invs[tuple(g)]))))
        left -= cl; classes.append(frozenset(cl))
    return classes
def subgroup(gens, cap=200): return closure(gens, cap)
def is_normal(H, G):
    Hs = set(H)
    return all(tuple(compose(compose(list(g), list(h)), pinv(list(g)))) in Hs for g in G for h in H)

# ---------------------------------------------------------------- AP1 the board
banner("AP1 -- the board: pair type = sign of inner product; iota and the seven reflections linear")
check("AP1a", "the pair type IS the sign of the E7 inner product: P <-> +1/2 (1512 ordered pairs), S <-> -1/2 (1512), v <-> -3/2 (56)",
      dict(ipmap) == {("P", 8): 1512, ("S", -8): 1512, ("v", -24): 56})
check("AP1b", "iota preserves every pair type and has trace -7 on the seven; each simple reflection preserves every pair type with trace 5",
      islinear(IOTA) and trace7(IOTA) == -7 and all(islinear(s) and trace7(s) == 5 for s in S7),
      "traces iota %s, reflections %s" % (trace7(IOTA), sorted({trace7(s) for s in S7})))
note("[P] a permutation of the 56 weights preserving every pairwise inner product extends to an isometry of the lattice they span;")
note("    Aut of the E7 lattice is W(E7) (which contains -1 = iota) -- so 'linear' below means: preserves every pair type.")
note("[P] trace on the seven: the 56 weights form one W-orbit spanning R^7, so sum_k w_k w_k^T is W-invariant = c.I and")
note("    tr(A) = 7 * sum_k <A w_k, w_k> / (56 |w|^2); validated on iota (-7) and the reflections (5) above.")

# ---------------------------------------------------------------- AP2 the centralizer
banner("AP2 -- the centralizer of Psi in S56, explicitly")
cycles = []; seen = set()
for k in range(56):
    if k in seen: continue
    c = []; x = k
    while x not in seen: seen.add(x); c.append(x); x = PSI[x]
    cycles.append(c)
big = [c for c in cycles if len(c) == 18]; two = [c for c in cycles if len(c) == 2]
check("AP2a", "Psi has cycle type [18,18,18,2] (SM-012)", cyc(PSI) == (18, 18, 18, 2) and len(big) == 3 and len(two) == 1)
def cent_elements():
    for sigma in itertools.permutations(range(3)):
        for shifts in itertools.product(range(18), repeat=3):
            for eps in (0, 1):
                p = [None] * 56
                for i in range(3):
                    for j in range(18):
                        p[big[i][j]] = big[sigma[i]][(j + shifts[i]) % 18]
                p[two[0][0]] = two[0][eps]; p[two[0][1]] = two[0][1 - eps]
                yield p
CENT = list(cent_elements())
distinct = len({tuple(p) for p in CENT})
allcomm = all(compose(p, PSI) == compose(PSI, p) for p in CENT)
INVS = [p for p in CENT if p != IDP and compose(p, p) == IDP]
check("AP2b", "the constructed centralizer has 18^3 * 3! * 2 = 69,984 distinct elements, every one commuting with Psi (= the whole "
      "centralizer, [P] |C(sigma)| = prod m_i! l_i^m_i)", distinct == 69984 and allcomm and len(CENT) == 69984, "distinct %d" % distinct)
check("AP2c", "its involutions number 231 = 15 + 3*72", len(INVS) == 231, len(INVS))
tick("centralizer built")

# ---------------------------------------------------------------- AP3 the answer
banner("AP3 -- REGISTERED: the centralizer meets W(E7) in the identity alone")
LIN = [p for p in CENT if islinear(p)]
lin_inv = [p for p in INVS if islinear(p)]
check("AP3a", "REGISTERED: exactly one of the 69,984 elements of C_S56(Psi) lies in W(E7), and it is the identity",
      len(LIN) == 1 and LIN[0] == IDP, "linear elements found: %d, orders %s" % (len(LIN), sorted(porder(p) for p in LIN)))
check("AP3b", "REGISTERED: 0 of the 231 involutions commuting with Psi is linear -- no C2 of W(E7) is normalized by the clock",
      len(lin_inv) == 0, len(lin_inv))
P9 = ppow(PSI, 9); IP9 = compose(IOTA, P9)
check("AP3c", "Psi^9 and iota*Psi^9 are involutions commuting with Psi and neither is linear (SM-016 re-seen: nu(Psi^9) > 0)",
      compose(P9, P9) == IDP and compose(P9, PSI) == compose(PSI, P9) and not islinear(P9) and not islinear(IP9),
      "kept pairs: Psi^9 %d/1540, iota*Psi^9 %d/1540" % (kept(P9), kept(IP9)))
tick("AP3 done")

# ---------------------------------------------------------------- AP7 the registered guess
banner("AP7 -- REGISTERED GUESS: the best linear agreement among the 231 is 1432/1540 with maximizers of pr's type 2^27 1^2")
K = [(kept(p), p) for p in INVS]
kmax = max(k for k, _ in K); maxers = [p for k, p in K if k == kmax]
mtypes = Counter(ctype(p) for p in maxers)
ok7 = (kmax == 1432 and all(cyc(p) == tuple([2]*27 + [1]*2) for p in maxers))
check("AP7", "REGISTERED GUESS: max kept = 1432/1540 (pr's 92.99 %%) and all maximizers have type 2^27 1^2",
      ok7, "max kept %d/1540 = %.4f; %d maximizers with types %s" % (kmax, kmax / 1540, len(maxers), dict(mtypes)))
if not ok7:
    say("  [INVERTED] recorded at equal prominence: the registered guess AP7 fails as stated; the numbers above stand as the finding.")
PR = D["PR"]
note("[obs] pr itself: kept %d/1540, type %s, commutes with Psi: %s" % (kept(PR), ctype(PR), compose(PR, PSI) == compose(PSI, PR)))
# POST-REVEAL, labelled: the single maximizer is a transposition.  Which one, and why 1432?
swap_axis = list(IDP); swap_axis[two[0][0]], swap_axis[two[0][1]] = two[0][1], two[0][0]
is_axis = len(maxers) == 1 and maxers[0] == swap_axis
changed = sum(1 for k, l in PAIRS if ptype(swap_axis[k], swap_axis[l]) != ptype(k, l))
check("AP7b", "POST-REVEAL: the unique maximizer is the transposition of Psi's 2-cycle (the clock's axis pair, SM-012), and its kept "
      "count 1540 - 108 = 1432 is forced for ANY transposition of an iota-pair (2*54 pairs touched, none preserved) -- pr's equal 1432 "
      "is a number repeated, not a structure repeated", is_axis and changed == 108 and 1540 - changed == 1432,
      "axis pair %s, pairs changed %d" % (two[0], changed))
note("[obs] the axis pair %s is an iota-pair: %s" % (two[0], IOTA[two[0][0]] == two[0][1]))
note("[obs] kept-pair histogram over the 231 involutions: %s" % sorted(Counter(k for k, _ in K).items(), reverse=True)[:8])

# ---------------------------------------------------------------- AP4 a bridge copy
banner("AP4 -- a bridge PSL(2,7) inside W(E7) on the 56 (SM-013 re-seen), by targeted (2,3,7) search")
def rand_elt(n=30):
    p = IDP
    for _ in range(n): p = compose(random.choice(S7), p)
    return p
T2 = tuple([2]*24 + [1]*8); T3 = tuple([3]*18 + [1]*2)
invs2, thr3 = [], []; spectrum = Counter(); nsamp = 0
def pairs_orbits(H):
    pairs = list({frozenset((k, IOTA[k])) for k in range(56)}); pidx = {p: i for i, p in enumerate(pairs)}
    parent = list(range(28))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for h in H:
        for p in pairs:
            q = frozenset(h[k] for k in p); a, b = find(pidx[p]), find(pidx[q])
            if a != b: parent[a] = b
    return sorted(Counter(find(i) for i in range(28)).values(), reverse=True)
def orbits56(H):
    parent = list(range(56))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for h in H:
        for k in range(56):
            a, b = find(k), find(h[k])
            if a != b: parent[a] = b
    return sorted(Counter(find(k) for k in range(56)).values(), reverse=True)
found = None; tried = 0
while found is None and nsamp < 300000:
    g = rand_elt(); nsamp += 1; ct = cyc(g)
    if ct[0] == 2 and ct[-1] in (1, 2): spectrum[fixed(g)] += 1
    if ct == T2 and g not in invs2: invs2.append(g)
    elif ct == T3 and g not in thr3: thr3.append(g)
    else: continue
    for a in invs2:
        for b in thr3:
            if porder(compose(a, b)) != 7: continue
            tried += 1
            H = closure([a, b], cap=170)
            if H is not None and len(H) == 168 and pairs_orbits(H) == [28]:
                found = (a, b, [list(h) for h in H]); break
        if found: break
check("AP4a", "a PSL(2,7) transitive on the 28 iota-pairs found inside W(E7) (order 168; (2,3,7) pairs tried %d; samples %d)" % (tried, nsamp),
      found is not None)
if found is None:
    say("RESULT: bridge copy not found within budget -- AP4/AP5/AP6 NOT RUN"); LOG.close(); sys.exit(1)
A0, B0, H = found
Hset = set(tuple(h) for h in H)
check("AP4b", "every element of the copy is linear (in W(E7)); orbits on the 56 are [28, 28] (SM-013's DQ-1)",
      all(islinear(h) for h in H) and orbits56(H) == [28, 28], orbits56(H))
CL = conj_classes([tuple(h) for h in H])
# first run: `sorted(Counter(...))` listed KEYS, collapsing the two order-7 classes -- instrumentation, fixed; FIRSTRUN log kept
census = sorted((len(c), porder(list(next(iter(c))))) for c in CL)
byclass = sorted(((porder(list(next(iter(c)))), len(c), fixed(list(next(iter(c)))), trace7(list(next(iter(c))))) for c in CL))
check("AP4c", "class census 1/21/56/42/24/24 (orders 1,2,3,4,7,7) -- PSL(2,7)", census == [(1, 1), (21, 2), (24, 7), (24, 7), (42, 4), (56, 3)], census)
fp = {(o, n): f for o, n, f, t in byclass}; tr = {(o, n): t for o, n, f, t in byclass}
check("AP4d", "REGISTERED (as written in the brief): fixed points on the 56 by class 56/8/2/4/0/0",
      fp == {(1, 1): 56, (2, 21): 8, (3, 56): 2, (4, 42): 4, (7, 24): 0}, fp)
check("AP4e", "REGISTERED: traces on the seven by class 7/-1/1/-1/0/0 = chi7 -- the seven restricts irreducibly to the bridge class",
      tr == {(1, 1): Fraction(7), (2, 21): Fraction(-1), (3, 56): Fraction(1), (4, 42): Fraction(-1), (7, 24): Fraction(0)}, tr)
# POST-REVEAL, labelled: the brief's '4' at the order-4 class was the auditor's arithmetic slip (it used chi7(4A) = +1 while the
# brief's own AP4e registers chi7(4A) = -1).  Evaluate SM-013's character from the classical table (SM-001) and compare.
# PSL(2,7) character table rows on classes 1A, 2A, 3A, 4A, 7A, 7B  [P, SM-001]:
CHI = {"chi1": (1, 1, 1, 1, 1, 1), "chi6": (6, 2, 0, 0, -1, -1), "chi7": (7, -1, 1, -1, 0, 0), "chi8": (8, 0, -1, 0, 1, 1)}
pred = tuple(2 * (CHI["chi1"][i] + 2 * CHI["chi6"][i] + CHI["chi7"][i] + CHI["chi8"][i]) for i in range(6))
meas = (fp[(1, 1)], fp[(2, 21)], fp[(3, 56)], fp[(4, 42)], fp[(7, 24)], fp[(7, 24)])
check("AP4d-b", "POST-REVEAL: 2(chi1+2chi6+chi7+chi8) evaluated from SM-001's table gives fixed points %s; measured %s -- SM-013's "
      "permutation character holds, the brief's '4' was a slip" % (pred, meas), pred == meas and pred == (56, 8, 2, 0, 0, 0))
note("[P] an order-4 element then has type 4^12 2^4 (its square fixes 8): measured %s" %
     ctype(list(next(iter([c for c in CL if len(c) == 42][0])))))
note("[obs] involution fixed-point spectrum of W(E7) on the 56, as sampled (fixed points: count): %s" % sorted(spectrum.items()))
tick("AP4 done")

# ---------------------------------------------------------------- AP5 his test for every pair
banner("AP5 -- his test, instantiated for every (2,3,7) pair of the copy")
Hl = [list(h) for h in H]
inv_H = [h for h in Hl if h != IDP and compose(h, h) == IDP]
thr_H = [h for h in Hl if porder(h) == 3]
gen_pairs = []
for a in inv_H:
    for b in thr_H:
        if porder(compose(a, b)) == 7 and closure([a, b], cap=170) is not None and len(closure([a, b], cap=170)) == 168:
            gen_pairs.append((a, b))
check("AP5a", "the copy has 21 involutions, 56 elements of order 3, and 336 (2,3,7)-generating pairs", len(inv_H) == 21 and len(thr_H) == 56 and len(gen_pairs) == 336,
      "%d / %d / %d" % (len(inv_H), len(thr_H), len(gen_pairs)))
V4_all = set()
for u in inv_H:
    for v in inv_H:
        if u != v and compose(u, v) == compose(v, u): V4_all.add(frozenset(tuple(x) for x in [IDP, u, v, compose(u, v)]))
V4_reached = set(); rows = Counter(); nfix_total = 0; chain_first = None
for A, B in gen_pairs:
    Bi = pinv(B)
    X = compose(compose(compose(A, B), A), Bi)
    Y = compose(compose(compose(compose(compose(compose(Bi, A), B), A), Bi), A), B)
    P = compose(X, X); Q = compose(X, Y)
    S4 = subgroup([X, Y]); A4 = subgroup([P, Q]); QPQi = compose(compose(Q, P), pinv(Q))
    V4 = subgroup([P, QPQi]); C2s = [P, QPQi, compose(compose(P, Q), compose(P, pinv(Q)))]
    okw = (S4 is not None and len(S4) == 24 and A4 is not None and len(A4) == 12 and is_normal(A4, S4)
           and V4 is not None and len(V4) == 4 and is_normal(V4, A4) and len({tuple(c) for c in C2s}) == 3
           and all(tuple(c) in set(V4) for c in C2s))
    A4s = [list(g) for g in A4]
    orbit = {tuple(compose(compose(g, P), pinv(g))) for g in A4s}
    normal = sum(1 for g in A4s if compose(compose(g, P), pinv(g)) == P)
    okc = orbit == {tuple(c) for c in C2s} and normal == 4
    nfix = sum(1 for c in C2s if compose(c, PSI) == compose(PSI, c))
    rows[(okw, okc, nfix)] += 1; nfix_total += nfix
    V4_reached.add(frozenset(V4))
    if chain_first is None: chain_first = (S4, A4, V4, C2s)
check("AP5b", "for all 336 pairs his words give S4 (24) > A4 (12, normal) > V4 (4, normal, three distinct C2's in it), the three C2's one "
      "A4-orbit with normalizer of order 4", rows == Counter({(True, True, 0): 336}) or all(k[0] and k[1] for k in rows), dict(rows))
check("AP5c", "the V4's reached are exactly the 14 V4 subgroups of the copy", len(V4_all) == 14 and V4_reached == V4_all,
      "%d reached of %d" % (len(V4_reached), len(V4_all)))
check("AP5d", "for EVERY pair, 0 of the 3 C2's is normalized by Psi (all 21 involutions of the copy fail) -- his test NOT SEALED, "
      "and by AP3 for every copy of the still point and every PSL(2,7) in W(E7)", nfix_total == 0 and all(k[2] == 0 for k in rows),
      "Psi-fixed C2's summed over 336 pairs: %d" % nfix_total)
tick("AP5 done")

# ---------------------------------------------------------------- AP6 his two channels
banner("AP6 -- his two channels D and dL on the chain, in the copy")
S4, A4, V4, C2s = chain_first
chain = [("PSL(2,7)", [tuple(h) for h in H]), ("S4", [tuple(x) for x in S4]), ("A4", [tuple(x) for x in A4]),
         ("V4", [tuple(x) for x in V4]), ("C2", [tuple(IDP), tuple(C2s[0])]), ("{e}", [tuple(IDP)])]
cls = {n: [c for c in conj_classes(G) if tuple(IDP) not in c] for n, G in chain}
cnt = [(n, len(cls[n])) for n, _ in chain]
check("AP6a", "nontrivial class counts along the chain 5, 4, 3, 3, 1, 0", [c for _, c in cnt] == [5, 4, 3, 3, 1, 0], cnt)
table = []
for (n1, G), (n2, Hh) in zip(chain, chain[1:]):
    Hs = set(Hh); lost = sum(1 for c in cls[n1] if not (c & Hs))
    created = sum(max(0, sum(1 for d in cls[n2] if d <= c) - 1) for c in cls[n1])
    table.append((n1, n2, lost, created, lost - created, len(cls[n1]) - len(cls[n2])))
for r in table: say("  %-9s -> %-5s  lost %d  created %d  D %d  c_nt diff %d" % r)
check("AP6b", "REGISTERED: (lost, created) = (2,1),(2,1),(2,2),(2,0),(1,0); D = 1,1,0,2,1 = c_nt(G) - c_nt(H) on every step "
      "(identically: c_nt(H) = c_nt(G) - lost + created)", [(r[2], r[3]) for r in table] == [(2,1),(2,1),(2,2),(2,0),(1,0)]
      and all(r[4] == r[5] for r in table) and [r[4] for r in table] == [1,1,0,2,1])
check("AP6c", "his D(A4,V4) = 2 ('new by splitting: none') is refuted: A4's involution class splits into V4's three, created = 2, D = 0",
      table[2][3] == 2 and table[2][4] == 0)
note("'lossless' is class-count only: |A4|/|V4| = 3, log2(3) = %.4f bits of order lost at that step (his own Level-5 number)" % np.log2(3))

json.dump({"brief_sha": sha, "scar56_sha256": jsha, "centralizer_order": distinct, "involutions": len(INVS), "linear_in_centralizer": len(LIN),
           "AP7_max_kept": kmax, "AP7_maximizer_types": dict(mtypes), "bridge_pair_a": A0, "bridge_pair_b": B0,
           "bridge_orbits56": orbits56(H), "V4_count": len(V4_all), "generating_pairs": len(gen_pairs), "psi_fixed_C2_total": nfix_total,
           "class_table": [list(r) for r in table], "involution_spectrum_sampled": sorted(spectrum.items())},
          open(os.path.join("_stone_ap_cache", "witnesses_ap.json"), "w"), indent=1)

banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done")
LOG.close()
