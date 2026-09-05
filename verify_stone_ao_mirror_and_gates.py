# -*- coding: utf-8 -*-
r"""verify_stone_ao_mirror_and_gates.py -- STONE AO: THE MIRROR AND THE GATES

Brief: BRIEF_STONE_AO_MIRROR_AND_GATES.md (lock BRIEF_STONE_AO_LOCK.sha256,
re-verified as check AO0).

The mirror pr measured against everything exact on the board: the sheets
(node-6 coweight), the poset order, the toggles, iota, sigma = -w0(E6), the
clock and its powers; and what the three gates generate.

BARS: AO1 sheets (pr swaps the sheets, fixes the poles); AO2 pr vs the
linear involutions + the parity identity for pr; AO3 |<Psi,pr>| = 56!,
<Psi,iota> = D18, the diameter bound; AO4 the relations; AO5 pr on the
lattice, iota an antiautomorphism; AO6 pr vs the sheet clock.

Machinery: scar56_data.json READ-ONLY; verify_stone_ac_parity_rule.py
lines 55-108 and 111-146 VERBATIM (check calls re-issued); sympy
Schreier-Sims.  DISCIPLINE: compute, never assert; registered expectations
resolvable INVERTED at equal prominence; exact arithmetic; no registry/git
writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_ao_mirror_and_gates.py
"""
import itertools, json, os, sys, time, random, hashlib, functools
from collections import Counter
from fractions import Fraction
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ao_mirror_and_gates.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))
CACHE = "_stone_ao_cache"; os.makedirs(CACHE, exist_ok=True)

say("=" * 78); say("STONE AO -- THE MIRROR AND THE GATES"); say("=" * 78)
BRIEF = "BRIEF_STONE_AO_MIRROR_AND_GATES.md"; LOCK = open("BRIEF_STONE_AO_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AO0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AO_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# =====================================================================
# VERBATIM from verify_stone_ac_parity_rule.py, lines 55-108 (E8 replay, label matching, pair type; check call removed, re-issued as AO0a)
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

check("AO0a", "the pair type IS the sign of the E7 inner product (SM-041 AC0a re-seen)", dict(ipmap) == {("P", 8): 1512, ("S", -8): 1512, ("v", -24): 56})

# =====================================================================
# VERBATIM from verify_stone_ac_parity_rule.py, lines 111-146 (the poset, rowmotion, the toggles; check calls removed, re-issued as AO0b)
# =====================================================================
banner("AC1 -- the minuscule poset from the crystal; PSI = rowmotion, exactly")
below = {k: set() for k in range(56)}; above = {k: set() for k in range(56)}; col = {}
for u, i, w in EDGES:
    below[u].add(w); above[w].add(u); col[(u, w)] = i
@functools.lru_cache(None)
def down(u):
    s = {u}
    for w in below[u]: s |= down(w)
    return frozenset(s)
JI = [k for k in range(56) if len(below[k]) == 1]
ideals = {k: frozenset(j for j in JI if j in down(k)) for k in range(56)}
colour = {j: col[(j, next(iter(below[j])))] for j in JI}
def leq(j, jp): return j in down(jp)
def rowmo(I, P):
    comp = [p for p in P if p not in I]
    mins = [p for p in comp if not any(leq(q, p) and q != p for q in comp)]
    return frozenset(p for p in P if any(leq(p, m) for m in mins))
i2v = {I: k for k, I in ideals.items()}
R = [i2v[rowmo(ideals[k], JI)] for k in range(56)]
Rinv = [0] * 56
for k in range(56): Rinv[R[k]] = k

# ---------------------------------------------------------------- AC2: delta = XOR of toggled roots
banner("AC2 -- delta(u) = XOR of the toggled simple roots; the antipodal steps")
def toggles(k, P, ideals_, rmap):
    I, J = ideals_[k], ideals_[rmap[k]]
    return sorted(colour[p] for p in I ^ J)
TOG = {k: toggles(k, JI, ideals, PSI) for k in range(56)}
delta = {k: mask[k] ^ mask[PSI[k]] for k in range(56)}

check("AO0b", "the crystal lattice has one top, one bottom, 27 join-irreducibles, 56 distinct ideals, and PSI = rowmotion exactly (SM-041 AC1 re-seen)",
      sum(1 for k in range(56) if not above[k]) == 1 and sum(1 for k in range(56) if not below[k]) == 1 and len(JI) == 27
      and len(set(ideals.values())) == 56 and R == PSI and Rinv != PSI)
PR = D["PR"]
def cyc(p):
    seen = set(); c = []
    for k in range(56):
        if k in seen: continue
        o = 0; x = k
        while x not in seen: seen.add(x); o += 1; x = p[x]
        c.append(o)
    return sorted(c, reverse=True)
def porder(p):
    x = list(range(56)); n = 0
    while True:
        x = compose(p, x); n += 1
        if x == list(range(56)): return n
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
IDN = list(range(56))

banner("AO1 -- the sheets: the node-6 coweight; pr swaps the sheets and fixes the poles")
Cinv = np.linalg.inv(np.array(C7, dtype=float))
cw = [Fraction(round(2 * sum(Cinv[6][j] * verts[k][j] for j in range(7))), 2) for k in range(56)]
dist = Counter(cw)
top = [k for k in range(56) if not above[k]][0]; bot = [k for k in range(56) if not below[k]][0]
prT = Counter((cw[k], cw[PR[k]]) for k in range(56)); ioT = Counter((cw[k], cw[IOTA[k]]) for k in range(56)); psT = Counter((cw[k], cw[PSI[k]]) for k in range(56))
say("  coweight-6 values: %s; top %d has %s, bottom %d has %s" % ({str(k): v for k, v in dist.items()}, top, cw[top], bot, cw[bot]))
say("  pr on sheets: %s" % {str(k): v for k, v in prT.items()}); say("  iota on sheets: %s" % {str(k): v for k, v in ioT.items()})
say("  [obs] Psi on sheets: %s" % {str(k): v for k, v in psT.items()})
h = Fraction(1, 2); t = Fraction(3, 2)
check("AO1a", "REGISTERED: the coweight takes +-3/2 once each (the top and bottom of the lattice) and +-1/2 twenty-seven times each; pr SWAPS the two 27-sheets and FIXES "
      "both poles (its only fixed points); iota swaps the sheets and swaps the poles",
      dist == Counter({h: 27, -h: 27, t: 1, -t: 1}) and {cw[top], cw[bot]} == {t, -t} and prT[(h, -h)] == 27 and prT[(-h, h)] == 27 and prT[(t, t)] == 1 and prT[(-t, -t)] == 1
      and [k for k in range(56) if PR[k] == k] == sorted([top, bot]) and ioT[(t, -t)] == 1 and ioT[(-t, t)] == 1 and ioT[(h, -h)] == 27)

banner("AO2 -- pr against the linear involutions; the parity identity for pr")
def refl(r, b): c = dot4(r, b); return tuple(x - c * y for x, y in zip(r, b))
vert_of_root = {root_of[k]: k for k in range(56)}
S7 = [[vert_of_root[refl(root_of[k], b)] for k in range(56)] for b in BETA]
c6 = IDN[:]
for i in range(6): c6 = compose(S7[i], c6)
w0 = ppow(c6, 6); sig = compose(IOTA, w0)
agree = lambda p, q: sum(1 for k in range(56) if p[k] == q[k])
pi = compose(PR, IOTA)
say("  pr: order %d, cycle type %s; pr*iota: order %d, fixed %d; agreement pr/iota %d, pr/sigma %d, pr/w0 %d; w0(E6) order %d fixed %d"
    % (porder(PR), dict(Counter(cyc(PR))), porder(pi), sum(1 for k in range(56) if pi[k] == k), agree(PR, IOTA), agree(PR, sig), agree(PR, w0), porder(w0), sum(1 for k in range(56) if w0[k] == k)))
check("AO2a", "REGISTERED: pr is an involution of cycle type 2^27 1^2 commuting with iota; pr*iota has 6 fixed points; pr agrees with iota on 6 states, with sigma = -w0(E6) on 14, "
      "with w0 on 2 -- the mirror is none of the linear involutions",
      porder(PR) == 2 and Counter(cyc(PR)) == Counter({2: 27, 1: 2}) and compose(PR, IOTA) == compose(IOTA, PR) and sum(1 for k in range(56) if pi[k] == k) == 6
      and agree(PR, IOTA) == 6 and agree(PR, sig) == 14 and agree(PR, w0) == 2)
# the parity identity for an arbitrary board permutation
def flips_by_identity(perm):
    d = {k: mask[k] ^ mask[perm[k]] for k in range(56)}
    exc = 0; kept = 0; cells = Counter()
    for k, l in PAIRS:
        if ptype(k, l) == "v" or ptype(perm[k], perm[l]) == "v":
            kept += (ptype(perm[k], perm[l]) == ptype(k, l)); continue
        pred_flip = (Bform(d[k], mask[l]) ^ Bform(mask[k], d[l]) ^ Bform(d[k], d[l])) == 1
        real_flip = ptype(perm[k], perm[l]) != ptype(k, l)
        if pred_flip != real_flip: exc += 1
        kept += (not real_flip)
    return exc, kept
exc_pr, kept_pr = flips_by_identity(PR)
TOGPR = {k: sorted(colour[p] for p in ideals[k] ^ ideals[PR[k]]) for k in range(56)}
sizes = Counter(len(v) for v in TOGPR.values())
say("  pr: parity identity exceptions %d; kept %d/1540 = %.4f (SM-040: 92.99 %%); toggle-multiset sizes %s" % (exc_pr, kept_pr, kept_pr / 1540, dict(sorted(sizes.items()))))
check("AO2b", "REGISTERED: the parity identity B(du,u')+B(u,du')+B(du,du') = flip holds for pr with ZERO exceptions (it is bilinear, hence holds for every board permutation) "
      "and the kept count recovers SM-040's 92.99 %", exc_pr == 0 and abs(kept_pr / 1540 - 0.9299) < 0.0005)

banner("AO3 -- the gates generate everything")
from sympy.combinatorics import Permutation, PermutationGroup
from math import factorial, log, ceil
oPI = PermutationGroup([Permutation(PSI), Permutation(IOTA)]).order()
oPRI = PermutationGroup([Permutation(PR), Permutation(IOTA)]).order()
t1 = time.time(); oPP = PermutationGroup([Permutation(PSI), Permutation(PR)]).order(); tick("Schreier-Sims for <Psi, pr> (%.1fs)" % (time.time() - t1))
oALL = PermutationGroup([Permutation(PSI), Permutation(IOTA), Permutation(PR)]).order()
say("  |<Psi,iota>| = %d; |<pr,iota>| = %d; |<Psi,pr>| = %d; 56! = %d; |<Psi,iota,pr>| = 56!: %s" % (oPI, oPRI, oPP, factorial(56), oALL == factorial(56)))
dbound = ceil(log(factorial(56) / 2, 3))
check("AO3a", "REGISTERED: <Psi,iota> has order 36 (dihedral, iota Psi iota = Psi^-1), <pr,iota> = C2 x C2, and |<Psi,pr>| = 56! -- the clock and the mirror generate the full "
      "symmetric group of the board; <Psi,iota,pr> = S56",
      oPI == 36 and compose(IOTA, compose(PSI, IOTA)) == pinv(PSI) and oPRI == 4 and oPP == factorial(56) and oALL == factorial(56))
check("AO3b", "[P] the Cayley graph of S56 on {Psi, Psi^-1, iota, pr} has diameter >= ceil(log_3(56!/2)) = %d (at most 2*3^d - 1 elements within distance d): the inherited "
      "'exact Cayley diameter (conj. 91-95)' cannot be this graph's -- flagged for the crystal lane, not refuted" % dbound, dbound == 157)

banner("AO4 -- the relations of the mirror with the clock")
orders = {k: porder(compose(PR, ppow(PSI, k))) for k in range(1, 18)}
say("  orders m_k of pr.Psi^k: %s" % orders)
# shortest reduced word in {Psi, Psi^-1, pr} equal to the identity, other than Psi^18 and pr^2 (and their rotations)
PSIi = pinv(PSI); G = {"P": PSI, "p": PSIi, "r": PR}
def reduced(w):
    for a, b in zip(w, w[1:]):
        if (a, b) in (("P", "p"), ("p", "P"), ("r", "r")): return False
    return True
found = None
for L in range(2, 17):
    for w in itertools.product("Ppr", repeat=L):
        if not reduced(w): continue
        if set(w) <= {"P"} or set(w) <= {"p"}: continue
        x = IDN[:]
        for g in w: x = compose(G[g], x)
        if x == IDN: found = "".join(w); break
    if found: break
say("  shortest reduced identity word using pr (length <= 16): %s (length %s)" % (found, len(found) if found else None))
check("AO4a", "REGISTERED: the table of orders m_k of pr.Psi^k (k = 1..17) is printed; m_4 = %d answers the inherited 'shortest pr/Psi^4 relation' as stated: (pr Psi^4)^%d = 1; "
      "the shortest reduced identity word involving pr up to length 16 is %s" % (orders[4], orders[4], found), all(v >= 2 for v in orders.values()))

banner("AO5 -- pr on the lattice; iota an antiautomorphism; the colour toggles")
comp = [(k, l) for k in range(56) for l in range(56) if k != l and ideals[k] < ideals[l]]
def order_stats(perm):
    pres = rev = nei = 0
    for k, l in comp:
        a, b = ideals[perm[k]], ideals[perm[l]]
        if a < b: pres += 1
        elif b < a: rev += 1
        else: nei += 1
    return pres, rev, nei
si = order_stats(IOTA); sp = order_stats(PR); sP = order_stats(PSI)
say("  comparable pairs of ideals: %d; iota (pres, rev, neither) = %s; pr = %s; [obs] Psi = %s" % (len(comp), si, sp, sP))
check("AO5a", "REGISTERED: iota reverses EVERY comparable pair (an antiautomorphism of J(P)); pr is neither order-preserving nor order-reversing (counts printed)",
      si[1] == len(comp) and sp[0] > 0 and sp[1] > 0)
def colour_toggle(c):
    elems = sorted([p for p in JI if colour[p] == c], key=lambda p: -len(down(p)))   # top to bottom
    def tog(I, p):
        if p in I:
            return I - {p} if not any(p in down(q) and q != p and q in I for q in JI) else I
        return I | {p} if all(q in I for q in JI if q != p and q in down(p)) else I
    perm = []
    for k in range(56):
        I = ideals[k]
        for p in elems: I = tog(I, p)
        perm.append(i2v[I])
    return perm
TC = {c: colour_toggle(c) for c in range(7)}
comm_pr = [c for c in range(7) if compose(TC[c], PR) == compose(PR, TC[c])]
comm_io = [c for c in range(7) if compose(TC[c], IOTA) == compose(IOTA, TC[c])]
say("  [obs] colour toggles T_c (orders %s) commuting with pr: %s; with iota: %s" % ({c: porder(TC[c]) for c in range(7)}, comm_pr, comm_io))

banner("AO6 -- pr and the sheet clock Psi6")
# Psi6: rowmotion of each 27-sheet as J(P6) -- the sheets and their posets built EXACTLY as in SM-041 AC5 (lines 214-229 of the AC verifier), the poles fixed
sheets = [sorted(k for k in range(56) if COMP[k] == s) for s in (0, 1)]
PSI6 = IDN[:]
for si_, S in enumerate(sheets):
    Sset = set(S)
    bel = {k: {w for w in below[k] if w in Sset and col[(k, w)] != 6} for k in S}
    @functools.lru_cache(None)
    def down6(u):
        s = {u}
        for w in bel[u]: s |= down6(w)
        return frozenset(s)
    JI6 = [k for k in S if len(bel[k]) == 1]
    ideals6 = {k: frozenset(j for j in JI6 if j in down6(k)) for k in S}
    def leq6(j, jp): return j in down6(jp)
    def rowmo6(I):
        comp_ = [p for p in JI6 if p not in I]
        mins = [p for p in comp_ if not any(leq6(q, p) and q != p for q in comp_)]
        return frozenset(p for p in JI6 if any(leq6(p, m) for m in mins))
    i2v6 = {I: k for k, I in ideals6.items()}
    for k in S: PSI6[k] = i2v6[rowmo6(ideals6[k])]
sheet_cw = {si_: set(cw[k] for k in S) for si_, S in enumerate(sheets)}
say("  sheets by COMP: sizes %s, coweight values %s" % ([len(S) for S in sheets], {k: [str(x) for x in v] for k, v in sheet_cw.items()}))
ok6 = sorted(PSI6) == IDN and all(len(S) == 27 for S in sheets) and all(len(v) == 1 for v in sheet_cw.values())
o6 = porder(PSI6) if ok6 else None
conjP = compose(PR, compose(PSI6, PR)) if ok6 else None
norm = [k for k in range(o6) if conjP == ppow(PSI6, k)] if ok6 else []
say("  Psi6 well-defined on the sheets: %s; order %s; cycle type %s; pr Psi6 pr = Psi6^k for k in %s; order of pr.Psi6 = %s"
    % (ok6, o6, dict(Counter(cyc(PSI6))) if ok6 else None, norm, porder(compose(PR, PSI6)) if ok6 else None))
if ok6 and not norm:
    check("AO6a", "REGISTERED GUESS: pr does NOT normalize <Psi6> (pr Psi6 pr is no power of Psi6)", True)
elif ok6:
    check("AO6a", "REGISTERED GUESS INVERTED (full prominence): pr Psi6 pr = Psi6^%s -- the mirror normalizes the sheet clock" % norm, False)
else:
    check("AO6a", "Psi6 could not be defined sheetwise on the sealed ideals (the colour-6 elements do not split as expected) -- recorded, no claim", False)

# ---------------- POST-REVEAL (finding, not amendment): AO6a inverted -- pr COMMUTES with the sheet clock.  A map commuting with rowmotion on each sheet
# and swapping the sheets is what an order-isomorphism between the two sheet lattices J(P6) would do.  Tested directly here.
banner("AO6b -- POST-REVEAL: is pr an order-isomorphism between the two sheets' ideal lattices?")
IDEALS6 = {}; JI6s = {}; COL6 = {}
for si_, S in enumerate(sheets):
    Sset = set(S)
    bel = {k: {w for w in below[k] if w in Sset and col[(k, w)] != 6} for k in S}
    @functools.lru_cache(None)
    def d6(u):
        s = {u}
        for w in bel[u]: s |= d6(w)
        return frozenset(s)
    JI6 = [k for k in S if len(bel[k]) == 1]; JI6s[si_] = JI6
    for j in JI6: COL6[j] = col[(j, next(iter(bel[j])))]
    for k in S: IDEALS6[k] = frozenset(j for j in JI6 if j in d6(k))
def within_stats(perm, src_sheet):
    S = sheets[src_sheet]; pres = rev = nei = tot = 0
    for k in S:
        for l in S:
            if k != l and IDEALS6[k] < IDEALS6[l]:
                tot += 1; a, b = IDEALS6[perm[k]], IDEALS6[perm[l]]
                if a < b: pres += 1
                elif b < a: rev += 1
                else: nei += 1
    return pres, rev, nei, tot
w0s = within_stats(PR, 0); w1s = within_stats(PR, 1)
sizes_ok = all(len(IDEALS6[k]) == len(IDEALS6[PR[k]]) for k in sheets[0] + sheets[1])
tri = all(sorted(COL6[p] for p in IDEALS6[k]) == sorted(COL6[p] for p in IDEALS6[PR[k]]) for k in sheets[0] + sheets[1])
say("  pr on the within-sheet ideal order: sheet 0 -> 1 (pres, rev, neither, total) = %s; sheet 1 -> 0 = %s; ideal sizes preserved: %s; colour multisets of ideals preserved: %s"
    % (w0s, w1s, sizes_ok, tri))
iso = w0s[0] == w0s[3] and w1s[0] == w1s[3]
check("AO6b", "POST-REVEAL FINDING: pr is an ORDER-ISOMORPHISM between the two sheets' ideal lattices J(P6) (every within-sheet comparable pair preserved, both directions, "
      "ideal sizes preserved) -- the mirror is the natural identification of the two E6 sheets, which is why it commutes with the sheet clock; its 'neither' pairs on the "
      "full lattice are all cross-sheet" if iso else
      "POST-REVEAL: pr is NOT an order-isomorphism of the sheet lattices (counts above) although it commutes with the sheet clock -- recorded, open", iso)
# the induced map on the sheet posets themselves (join-irreducibles): colours preserved?
if iso:
    jmap = {}
    for j in JI6s[0]:
        img = IDEALS6[PR[j]]                       # image ideal of the principal ideal of j; its top element is the image of j
        tops = [q for q in img if not any(q != r and q in IDEALS6[r] and r in img for r in JI6s[1])]
        jmap[j] = tops
    col_pres = sum(1 for j in JI6s[0] if len(jmap[j]) == 1 and COL6[jmap[j][0]] == COL6[j])
    note("[obs] induced map on the 16 join-irreducibles of sheet 0: %d of 16 principal ideals map to principal ideals; colours preserved on %d of them (colour map %s)"
         % (sum(1 for j in JI6s[0] if len(jmap[j]) == 1), col_pres, Counter((COL6[j], COL6[jmap[j][0]]) for j in JI6s[0] if len(jmap[j]) == 1)))

json.dump({"brief_sha": sha, "sheets": {str(k): v for k, v in dist.items()}, "pr_type": dict(Counter(cyc(PR))), "orders_prPsik": orders, "shortest_word": found,
           "group_orders": {"Psi_iota": oPI, "pr_iota": oPRI, "Psi_pr": str(oPP), "all_is_S56": oALL == factorial(56)}, "diam_bound": dbound,
           "order_stats": {"iota": si, "pr": sp, "Psi": sP}, "toggle_sizes_pr": dict(sizes), "kept_pr": kept_pr, "psi6_order": o6, "pr_normalizes_psi6": norm},
          open(os.path.join(CACHE, "witnesses_ao.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
