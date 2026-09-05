# -*- coding: utf-8 -*-
r"""verify_stone_af_three_eighteens.py -- STONE AF: THE THREE EIGHTEENS

Brief: BRIEF_STONE_AF_THREE_EIGHTEENS.md (lock BRIEF_STONE_AF_LOCK.sha256,
re-verified as check AF0).

Question: three objects carry 18 = h(E7): the merkabit's clock Psi
(SM-041: rowmotion on the E7 minuscule poset), the E7 Coxeter element c7
on the 56 weights, and the roof's Phi.c-bar (SM-039).  Which are the same
object; does the roof's one have any rowmotion in it?  First bar: IB's
PROMPT "What exactly does Psi remember?" -- per-type survival.

BARS: AF0a type = sign of the E7 inner product; AF1 per-type survival
table (v 1/28, P 504/756, S 497/756 at k=1; all v kept at k=9, P=S=460);
AF2 64 Coxeter elements, all [18,18,18,2], c^9 = iota, Psi not in W(E7);
AF3 max agreement Psi vs Coxeter = 14/56; AF4 c-bar7 outside Omega
(Dickson 1), cycle type {1:1, 2:1, 18:3, 9:7} on the 120; AF5 the coset
argument + orbit structures from the sealed SM-039 log: "Phi.c-bar is
rowmotion on a roof poset" NOT SUPPORTED as stated.

Machinery: scar56_data.json READ-ONLY; the E8 replay / label matching /
pair type VERBATIM from verify_stone_ac_parity_rule.py lines 55-108
(its check call re-issued as AF0a); the sealed SM-039 log read for cycle
types.  DISCIPLINE: compute, never assert; registered expectations
resolvable INVERTED at equal prominence; exact arithmetic; no registry/
git writes.  Not RH/GRH.  Rule 3.

Run:  python -X utf8 verify_stone_af_three_eighteens.py
"""
import itertools, json, os, sys, time, random, hashlib, re
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_af_three_eighteens.log", "w", encoding="utf-8")
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
CACHE = "_stone_af_cache"; os.makedirs(CACHE, exist_ok=True)

say("=" * 78); say("STONE AF -- THE THREE EIGHTEENS (what Psi remembers; is the roof's 18 rowmotion?)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AF_THREE_EIGHTEENS.md"; LOCK = open("BRIEF_STONE_AF_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AF0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AF_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# =====================================================================
# VERBATIM from verify_stone_ac_parity_rule.py, lines 55-108 (check call removed, re-issued below as AF0a)
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

check("AF0a", "the pair type IS the sign of the E7 inner product: P <-> +1/2 (1512 ordered pairs), S <-> -1/2 (1512), v <-> -3/2 (56)",
      dict(ipmap) == {("P", 8): 1512, ("S", -8): 1512, ("v", -24): 56})

# ---------------------------------------------------------------- helpers
def cyc(p):
    seen = set(); c = []
    for k in range(len(p)):
        if k in seen: continue
        o = 0; x = k
        while x not in seen: seen.add(x); o += 1; x = p[x]
        c.append(o)
    return sorted(c, reverse=True)
def porder(p):
    x = list(range(len(p))); n = 0
    while True:
        x = [p[i] for i in x]; n += 1
        if x == list(range(len(p))): return n
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return r
TYPES = Counter(ptype(k, l) for k, l in PAIRS)

# =====================================================================
banner("AF1 -- his prompt: what exactly does Psi remember?  per-type survival under Psi^k")
# =====================================================================
say("  pair-type counts on the board: %s" % dict(TYPES))
random.seed(20260905)
acc = {T: 0.0 for T in "vPS"}; NR = 200
for _ in range(NR):
    p = list(range(56)); random.shuffle(p)
    M = Counter((ptype(k, l), ptype(p[k], p[l])) for k, l in PAIRS)
    for T in "vPS": acc[T] += M[(T, T)] / TYPES[T] / NR
say("  random baseline (%d permutations): v %.4f, P %.4f, S %.4f" % (NR, acc["v"], acc["P"], acc["S"]))
say("   k | overall | v kept | P kept | S kept |  transition counts (from v / P / S -> [v P S])")
ROWS = {}
for kk in range(1, 18):
    Pk = ppow(PSI, kk)
    M = Counter((ptype(k, l), ptype(Pk[k], Pk[l])) for k, l in PAIRS)
    kept = {T: M[(T, T)] for T in "vPS"}
    overall = sum(kept.values()) / len(PAIRS)
    ROWS[kk] = dict(kept=kept, M={a + b: M[(a, b)] for a in "vPS" for b in "vPS"}, overall=overall)
    say("  %2d | %.4f | %3d/28 | %3d/756 | %3d/756 |  v[%3d %3d %3d] P[%3d %3d %3d] S[%3d %3d %3d]"
        % (kk, overall, kept["v"], kept["P"], kept["S"], M[("v","v")], M[("v","P")], M[("v","S")],
           M[("P","v")], M[("P","P")], M[("P","S")], M[("S","v")], M[("S","P")], M[("S","S")]))
k1 = ROWS[1]["kept"]; k9 = ROWS[9]["kept"]
check("AF1a", "REGISTERED: at k = 1 the v-pairs kept are 1/28, P 504/756, S 497/756 (the 65.06 % is 1002/1540)",
      k1 == {"v": 1, "P": 504, "S": 497} and sum(k1.values()) == 1002)
fP, fS, fv = k1["P"] / 756, k1["S"] / 756, k1["v"] / 28
check("AF1b", "REGISTERED: NO type is privileged -- P and S survive within 2 points of each other (%.1f %% vs %.1f %%), v is destroyed "
      "(%.1f %%, random %.1f %%): his decision rule ('one type survives much better') is NOT met" % (100*fP, 100*fS, 100*fv, 100*acc["v"]),
      abs(fP - fS) < 0.02 and fv < 0.1 and fP > acc["P"] + 0.1 and fS > acc["S"] + 0.1)
P9 = ppow(PSI, 9)
comm9 = all(P9[IOTA[k]] == IOTA[P9[k]] for k in range(56))
check("AF1c", "REGISTERED: at k = 9 all 28 antipodal pairs are kept and P = S = 460/756 exactly; Psi^9 commutes with iota, is fixed-point-free, "
      "and is NOT iota", k9 == {"v": 28, "P": 460, "S": 460} and comm9 and all(P9[k] != k for k in range(56)) and P9 != IOTA)
note("[obs] where the v-pairs go at k = 1: to P %d, to S %d; the antipodal steps (Psi u = iota u) number %d"
     % (ROWS[1]["M"]["vP"], ROWS[1]["M"]["vS"], sum(1 for k in range(56) if PSI[k] == IOTA[k])))

# =====================================================================
banner("AF2 -- the E7 Coxeter element on the board: same orbit structure as Psi, ninth power = iota; Psi not in W(E7)")
# =====================================================================
def refl(r, b): c = dot4(r, b); return tuple(x - c * y for x, y in zip(r, b))
vert_of_root = {root_of[k]: k for k in range(56)}
S7 = [[vert_of_root[refl(root_of[k], b)] for k in range(56)] for b in BETA]
assert all(sorted(s) == list(range(56)) for s in S7)
COX = {}
for perm in itertools.permutations(range(7)):
    p = list(range(56))
    for i in perm: p = compose(S7[i], p)
    COX.setdefault(tuple(p), perm)
COXL = [list(c) for c in COX]
types = Counter(tuple(cyc(c)) for c in COXL); orders = Counter(porder(c) for c in COXL)
ninth = all(ppow(c, 9) == IOTA for c in COXL)
check("AF2a", "REGISTERED: the 7! orderings of the E7 simple reflections give exactly 64 distinct Coxeter elements, every one of order 18 with "
      "cycle type [18,18,18,2] on the board -- Psi's orbit structure %s -- and c^9 = iota for every one" % cyc(PSI),
      len(COXL) == 64 and orders == Counter({18: 64}) and types == Counter({(18, 18, 18, 2): 64}) and cyc(PSI) == [18, 18, 18, 2] and ninth,
      "distinct %d, orders %s, types %s" % (len(COXL), dict(orders), {k: v for k, v in types.items()}))
# Psi not in W(E7): the board masks span V; the linear map from a basis disagrees
def f2rank(ms):
    b = []
    for m in ms:
        for x in b: m = min(m, m ^ x)
        if m: b.append(m); b.sort(reverse=True)
    return len(b)
masks = [mask[k] for k in range(56)]
rk = f2rank(masks)
basis = []; bidx = []
for k in range(56):
    if f2rank([mask[j] for j in bidx] + [mask[k]]) > len(bidx): bidx.append(k)
    if len(bidx) == 8: break
# express every mask in the basis (solve over F2) and compare Psi with the induced linear map
Bm = [mask[k] for k in bidx]; Im = [mask[PSI[k]] for k in bidx]
def coords_in_basis(x):
    for bits in range(256):
        y = 0
        for j in range(8):
            if (bits >> j) & 1: y ^= Bm[j]
        if y == x: return bits
    return None
lin_ok = True
for k in range(56):
    bits = coords_in_basis(mask[k]); y = 0
    for j in range(8):
        if (bits >> j) & 1: y ^= Im[j]
    if y != mask[PSI[k]]: lin_ok = False; break
check("AF2b", "REGISTERED: the 56 board masks span V (F2-rank 8) and the linear map defined by Psi on a basis of 8 board points DISAGREES with Psi "
      "on the board -- Psi is not in W(E7) (SM-040's 'no linear extension', re-seen)", rk == 8 and not lin_ok)

# =====================================================================
banner("AF3 -- how far Psi is from a Coxeter element")
# =====================================================================
PSIinv = pinv(PSI)
agree = Counter(); best = (0, None)
for c in COXL:
    a = sum(1 for k in range(56) if c[k] == PSI[k]); ai = sum(1 for k in range(56) if c[k] == PSIinv[k])
    agree[a] += 1
    if a > best[0]: best = (a, c)
    if ai > best[0]: best = (ai, c)
say("  agreement (points of the board where Psi = c) over the 64 Coxeter elements: %s" % dict(sorted(agree.items())))
check("AF3a", "REGISTERED: the maximum agreement of Psi (or Psi^-1) with any Coxeter element is 14 of 56 points", best[0] == 14, "max %d" % best[0])
cb = best[1]; comp = compose(PSI, pinv(cb))
note("[obs] for a best c: Psi o c^-1 has cycle type %s, order %d, and type-score %.4f (Psi alone: %.4f; c alone: %.4f)"
     % (cyc(comp), porder(comp), score(comp), score(PSI), score(cb)))

# =====================================================================
banner("AF4 -- the E7 Coxeter element seen from the roof: c-bar7 on the 120 nonsingular vectors")
# =====================================================================
BETAM = [rmask[ridx[b]] for b in BETA]
def tv(x, b): return x ^ (b if Bform(x, b) else 0)
def cbar7(x):
    for i in reversed(range(7)): x = tv(x, BETAM[i])
    return x
NONSING = [m for m in range(256) if qvals[m] == 1]; NS_IDX = {m: i for i, m in enumerate(NONSING)}
pc = [NS_IDX[cbar7(m)] for m in NONSING]
Mcols = [cbar7(1 << j) for j in range(8)]
dick = f2rank([Mcols[j] ^ (1 << j) for j in range(8)]) & 1
lin_all = all(cbar7(x ^ y) == cbar7(x) ^ cbar7(y) for x in range(256) for y in range(0, 256, 37))
isom = all(qvals[cbar7(x)] == qvals[x] for x in range(256))
BOARDM = sorted(masks); PAULI = [u for u in NONSING if u != ALPHA and Bform(u, ALPHA) == 0]
pboard = {u: cbar7(u) for u in BOARDM}; ppauli = {u: cbar7(u) for u in PAULI}
def cyc_dict(d):
    seen = set(); c = []
    for k in d:
        if k in seen: continue
        o = 0; x = k
        while x not in seen: seen.add(x); o += 1; x = d[x]
        c.append(o)
    return Counter(c)
ct120 = Counter(cyc(pc)); ctB = cyc_dict(pboard); ctP = cyc_dict(ppauli)
say("  c-bar7: linear %s, isometry %s, fixes v %s, Dickson invariant %d; cycle type on 120: %s; on the 56 board: %s; on the 63 Paulis: %s"
    % (lin_all, isom, cbar7(ALPHA) == ALPHA, dick, dict(ct120), dict(ctB), dict(ctP)))
check("AF4a", "REGISTERED: c-bar7 (product of the seven transvections t_beta) is a q-isometry fixing v with Dickson invariant 1 -- OUTSIDE Omega, "
      "in the coset of iota = t_v", lin_all and isom and cbar7(ALPHA) == ALPHA and dick == 1)
check("AF4b", "REGISTERED: cycle type on the 120: one fixed point (v), one 2-cycle and three 18-cycles on the board, seven 9-cycles on the 63 Paulis",
      ct120 == Counter({1: 1, 2: 1, 18: 3, 9: 7}) and ctB == Counter({18: 3, 2: 1}) and ctP == Counter({9: 7}))
# the board action of c-bar7 equals c7 mod 2 (same permutation of the 56 as the real Coxeter element with the same ordering)
perm0 = COX[tuple(COXL[0])]
c_real = list(range(56))
for i in perm0: c_real = compose(S7[i], c_real)
def cbar_ordered(x, perm):
    for i in perm: x = tv(x, BETAM[i])      # c_real = S7[perm[-1]] o ... o S7[perm[0]]: perm[0] acts first (first run applied the reverse order; FIRSTRUN log kept)
    return x
same = all(cbar_ordered(mask[k], perm0) == mask[c_real[k]] for k in range(56))
check("AF4c", "the mod-2 image of a Coxeter element (same ordering) acts on the 56 masks exactly as the real Coxeter element acts on the 56 roots", same)

# =====================================================================
banner("AF5 -- the roof's 18 is not rowmotion: the coset argument + orbit structures from the sealed SM-039 log")
# =====================================================================
aa = open("verify_stone_aa_roofclock.log", encoding="utf-8").read()
m18 = re.search(r"Phi \. c-bar has order 18 with cycle type (\{[^}]*\})", aa)
m24 = re.search(r"maximal order found among \d+ samples is (\d+)", aa)
ct_phic = eval(m18.group(1)) if m18 else None
say("  from the sealed SM-039 log: Phi.c-bar cycle type on 360 = %s; maximal twisted order sampled = %s" % (ct_phic, m24.group(1) if m24 else None))
# rowmotion orbit structures in hand
row_E7 = Counter(cyc(PSI)); row_E6 = Counter({12: 2, 3: 1})   # SM-041 AC5a (sealed): each 27-sheet [12,12,3]
def matches(ct, deg):
    return ct is not None and sum(k * v for k, v in ct.items()) == deg
say("  rowmotion orbit structures in hand: E7 minuscule (56 ideals) %s; E6 minuscule sheet (27 ideals) %s" % (dict(row_E7), dict(row_E6)))
coset_ok = (dick == 1)   # c-bar7 in the involution coset; Phi.c-bar in the order-3 coset (SM-039: <Omega,Phi> = Omega:3)
no_match = (ct_phic is not None and Counter(ct_phic) != row_E7 and Counter(ct_phic) != row_E6 and sum(k*v for k, v in ct_phic.items()) == 360)
check("AF5a", "[P on computed inputs] c-bar7 lies in Omega.iota (Dickson 1) and Phi.c-bar in Omega.Phi (order-3 coset, SM-039); in Omega:S3 "
      "conjugation preserves the S3-class of the coset, a 3-cycle is not a transposition: the two eighteens of the roof are NOT conjugate", coset_ok)
check("AF5b", "REGISTERED: Phi.c-bar's sealed cycle type on 360 (%s) matches NO rowmotion orbit structure in hand ([18,18,18,2] on 56; [12,12,3] on 27) "
      "and no roof poset is named: under IB's own decision rule, 'Phi.c-bar (or an order-24 element) is rowmotion on a roof poset' is NOT SUPPORTED "
      "as stated; the only 18-clock that IS rowmotion is the merkabit's (SM-041)" % (ct_phic,), no_match)
json.dump({"brief_sha": sha, "per_type": {k: ROWS[k]["kept"] for k in ROWS}, "random_baseline": acc, "coxeter_count": len(COXL),
           "max_agreement": best[0], "cbar7_cycle_120": dict(ct120), "dickson": dick, "phic_cycle_360": ct_phic},
          open(os.path.join(CACHE, "witnesses_af.json"), "w"), indent=1)

banner("VERDICT")
say("""  Three eighteens, one number.  The merkabit's clock Psi is rowmotion and
  shares the E7 Coxeter element's orbit structure [18,18,18,2] -- and
  nothing else of it: it is not a Weyl element, it agrees with the best
  Coxeter element on 14 points of 56, and its ninth power is not the
  chirality bit (the Coxeter element's is).  Seen from the roof the
  Coxeter element sits in iota's coset, the turn's eighteen in the
  triality coset; they are not conjugate, and the roof's eighteen matches
  no rowmotion in hand.  What Psi remembers is not a type: P and S survive
  alike, antipodes die at once and come back whole at the ninth beat.""")
npass = sum(1 for t, ok in RESULTS if ok); nfail = [t for t, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
