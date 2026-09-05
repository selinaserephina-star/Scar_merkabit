# -*- coding: utf-8 -*-
r"""verify_stone_ac_parity_rule.py -- STONE AC: THE PARITY RULE OF THE CLOCK

Brief: BRIEF_STONE_AC_PARITY_RULE.md (lock BRIEF_STONE_AC_LOCK.sha256,
re-verified as check AC0: 16349cbd805cab4f7ff3416c0386401f730ccc8bc44d5f1de279c8259e901722).

Why does the merkabit's clock keep 65% of the roof's pair incidence on the
board (SM-040 AB6) and its cube 51%?  The pair type is the sign of the E7
inner product; a pair keeps its type iff B(u,d') + B(d,u') + B(d,d') = 0
with d = u + Psi u; and d is the XOR of the simple roots the clock toggles.
THE RULE: type flips iff  t1 + t2 + t3  is odd, where t1 = #toggled colours
of u at which u' has an edge, t2 symmetric, t3 = #Dynkin-adjacent pairs
between the two toggle multisets.

BARS: AC1 PSI = rowmotion (downset of min complement) on the 27-element
join-irreducible poset, exactly; AC2 d = XOR of toggled roots, antipodal
steps = singleton toggles (registered); AC3 THE PARITY RULE exact, cells,
65.06% recovered; AC4 the profile Psi^k reproduced; AC5 the E6 control:
sheets = J(P6), Psi6 order 12 orbits [12,12,3], rule exact, registered
guess: E6 keeps >= 65%; AC6 [obs] cells.

Machinery: scar56_data.json (SM-005) READ-ONLY; the E8-root replay and
label matching of SM-040 verbatim.  No registry/git writes.  Not RH/GRH.
Rule 3.

Run:  python -X utf8 verify_stone_ac_parity_rule.py
"""
import itertools, json, os, time, hashlib, functools
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ac_parity_rule.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.write(s + "\n"); LOG.flush()
PASS = 0; FAIL = 0; FAILED = []
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else: FAIL += 1; FAILED.append(tag)
    say(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
CACHE = "_stone_ac_cache"; os.makedirs(CACHE, exist_ok=True)

say("=" * 78); say("STONE AC -- THE PARITY RULE OF THE CLOCK"); say("=" * 78)
BRIEF = "BRIEF_STONE_AC_PARITY_RULE.md"; LOCK = "16349cbd805cab4f7ff3416c0386401f730ccc8bc44d5f1de279c8259e901722"
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AC0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AC_LOCK.sha256" % BRIEF,
      sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- E8 replay (verbatim SM-040)
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
check("AC0a", "the pair type IS the sign of the E7 inner product: P <-> <w,w'> = +1/2 (1512 ordered "
      "pairs), S <-> -1/2 (1512), v <-> -3/2 (56) -- Psi's AB6 score is its Gosset-graph preservation",
      dict(ipmap) == {("P", 8): 1512, ("S", -8): 1512, ("v", -24): 56})
PAIRS = [(k, l) for k in range(56) for l in range(k + 1, 56)]
def compose(p, q): return [p[q[k]] for k in range(56)]
def ppow(p, e):
    x = list(range(56))
    for _ in range(e): x = compose(p, x)
    return x
def score(p): return sum(1 for k, l in PAIRS if ptype(p[k], p[l]) == ptype(k, l)) / len(PAIRS)

# ---------------------------------------------------------------- AC1: the poset and rowmotion
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
check("AC1a", "the sealed crystal lattice has one top, one bottom, 27 join-irreducibles (the E7 "
      "minuscule poset), and its 56 ideals are the 56 states (distinct)",
      sum(1 for k in range(56) if not above[k]) == 1 and sum(1 for k in range(56) if not below[k]) == 1
      and len(JI) == 27 and len(set(ideals.values())) == 56)
check("AC1b", "REGISTERED EXPECTATION: the sealed PSI equals rowmotion R(I) = downset(min(P \\ I)) on "
      "the ideals EXACTLY (and not its inverse) -- the convention is pinned",
      R == PSI and Rinv != PSI)

# ---------------------------------------------------------------- AC2: delta = XOR of toggled roots
banner("AC2 -- delta(u) = XOR of the toggled simple roots; the antipodal steps")
def toggles(k, P, ideals_, rmap):
    I, J = ideals_[k], ideals_[rmap[k]]
    return sorted(colour[p] for p in I ^ J)
TOG = {k: toggles(k, JI, ideals, PSI) for k in range(56)}
delta = {k: mask[k] ^ mask[PSI[k]] for k in range(56)}
xor_ok = all(delta[k] == functools.reduce(lambda a, b: a ^ b, (BETAM[c] for c in TOG[k]), 0) for k in range(56))
sizes = Counter(len(t) for t in TOG.values())
check("AC2a", "delta(u) = u + Psi(u) equals the XOR of the toggled simple-root masks for ALL 56 states; "
      "toggle-multiset sizes %s" % dict(sorted(sizes.items())), xor_ok)
anti = sorted(k for k in range(56) if ptype(k, PSI[k]) == "v")
single = sorted(k for k in range(56) if len(TOG[k]) == 1)
check("AC2b", "REGISTERED EXPECTATION: the 8 antipodal steps (Psi u = iota u) are exactly the 8 "
      "singleton toggles -- %s" % ("CONFIRMED" if anti == single else "INVERTED: antipodal %s vs singleton %s" % (anti, single)),
      anti == single and len(anti) == 8)
steps = Counter(ptype(k, PSI[k]) for k in range(56))
note("step types (u, Psi u): %s -- the clock almost always moves to a -1/2 neighbour" % dict(steps))

# ---------------------------------------------------------------- AC3: THE PARITY RULE
banner("AC3 -- THE PARITY RULE: kept iff t1 + t2 + t3 even")
def active(k, c): return abs(verts[k][c]) % 2          # |label_c(u)| = 1 iff u has a colour-c edge
def t_cross(tog_k, l): return sum(active(l, c) for c in tog_k) % 2
def t_dyn(tog_k, tog_l, C): return sum(C[c][cp] for c in tog_k for cp in tog_l) % 2
def rule_table(perm, TOGm, C, pairs, typef):
    cells = Counter(); exc = 0; kept_n = 0; nonv = 0
    for k, l in pairs:
        if typef(k, l) == "v" or typef(perm[k], perm[l]) == "v": continue
        nonv += 1
        a, b, c = t_cross(TOGm[k], l), t_cross(TOGm[l], k), t_dyn(TOGm[k], TOGm[l], C)
        kept = typef(perm[k], perm[l]) == typef(k, l)
        kept_n += kept
        cells[((a, b, c), kept)] += 1
        if ((a ^ b ^ c) == 0) != kept: exc += 1
    return cells, exc, kept_n, nonv
cells, exc, kept_n, nonv = rule_table(PSI, TOG, C7, PAIRS, ptype)
say("  parity cell (t1,t2,t3) : kept? : count")
for key in sorted(cells): say("    %s : %s : %d" % (key[0], key[1], cells[key]))
v_pairs = sum(1 for k, l in PAIRS if ptype(k, l) == "v")
v_kept = sum(1 for k, l in PAIRS if ptype(k, l) == "v" and ptype(PSI[k], PSI[l]) == "v")
total_kept = kept_n + v_kept
check("AC3a", "REGISTERED EXPECTATION CONFIRMED: on all %d non-antipodal pairs the type is kept iff "
      "t1 + t2 + t3 is EVEN -- %d exceptions; with the %d antipodal pairs (%d kept) the count %d/1540 = "
      "%.4f recovers SM-040's 65.06%%" % (nonv, exc, v_pairs, v_kept, total_kept, total_kept / 1540),
      exc == 0 and abs(total_kept / 1540 - 0.6506) < 5e-4)
m1 = sum(t_cross(TOG[k], l) for k, l in PAIRS) / len(PAIRS)
m3 = sum(t_dyn(TOG[k], TOG[l], C7) for k, l in PAIRS) / len(PAIRS)
dom = max(((key, n) for key, n in cells.items() if key[1]), key=lambda t: t[1])
note("[obs] marginals: t1 odd on %.3f of pairs, t3 odd on %.3f; the dominant kept cell is %s with %d pairs"
     % (m1, m3, dom[0][0], dom[1]))

# ---------------------------------------------------------------- AC4: the profile
banner("AC4 -- the profile Psi^k reproduced by the iterated rule")
prof_ok = True; prof = []
for kk in range(1, 18):
    Pk = ppow(PSI, kk)
    TOGk = {}
    for k in range(56):
        t = []; x = k
        for _ in range(kk):
            t += TOG[x]; x = PSI[x]
        TOGk[k] = t
    ok_delta = all((mask[k] ^ mask[Pk[k]]) == functools.reduce(lambda a, b: a ^ b, (BETAM[c] for c in TOGk[k]), 0) for k in range(56))
    c_k, exc_k, kept_k, nonv_k = rule_table(Pk, TOGk, C7, PAIRS, ptype)
    sc = score(Pk); prof.append((kk, sc, exc_k))
    prof_ok &= ok_delta and exc_k == 0
say("  k : preservation : exceptions to the iterated rule")
for kk, sc, e in prof: say("   %2d : %.4f : %d" % (kk, sc, e))
check("AC4a", "for every k = 1..17 the k-fold toggle multiset gives delta_k exactly and the parity rule "
      "is exact (0 exceptions); the sealed profile is reproduced (65.1 / 54.7 / 51.3 / ... / 61.6 at 9)",
      prof_ok and abs(prof[0][1] - 0.6506) < 5e-4 and abs(prof[8][1] - 0.6156) < 5e-4 and abs(prof[2][1] - 0.5130) < 5e-4)

# ---------------------------------------------------------------- AC5: the E6 control
banner("AC5 -- THE E6 CONTROL: the 27-sheets as J(P6), Psi6, the same rule")
sheets = [sorted(k for k in range(56) if COMP[k] == s) for s in (0, 1)]
C6 = [[C7[i][j] for j in range(6)] for i in range(6)]
res6 = []
for si, S in enumerate(sheets):
    Sset = set(S)
    bel = {k: {w for w in below[k] if w in Sset and col[(k, w)] != 6} for k in S}
    @functools.lru_cache(None)
    def down6(u):
        s = {u}
        for w in bel[u]: s |= down6(w)
        return frozenset(s)
    JI6 = [k for k in S if len(bel[k]) == 1]
    ideals6 = {k: frozenset(j for j in JI6 if j in down6(k)) for k in S}
    colour6 = {j: col[(j, next(iter(bel[j])))] for j in JI6}
    def leq6(j, jp): return j in down6(jp)
    def rowmo6(I):
        comp = [p for p in JI6 if p not in I]
        mins = [p for p in comp if not any(leq6(q, p) and q != p for q in comp)]
        return frozenset(p for p in JI6 if any(leq6(p, m) for m in mins))
    i2v6 = {I: k for k, I in ideals6.items()}
    R6 = {k: i2v6[rowmo6(ideals6[k])] for k in S}
    # order and orbits
    seen = set(); orbs = []
    for k in S:
        if k in seen: continue
        o = [k]; x = R6[k]
        while x != k: o.append(x); x = R6[x]
        seen |= set(o); orbs.append(len(o))
    order6 = functools.reduce(lambda a, b: a * b // __import__("math").gcd(a, b), orbs, 1)
    TOG6 = {k: sorted(colour6[p] for p in ideals6[k] ^ ideals6[R6[k]]) for k in S}
    pairs6 = [(k, l) for i, k in enumerate(S) for l in S[i + 1:]]
    tcount = Counter(ptype(k, l) for k, l in pairs6)
    R6p = {k: R6[k] for k in S}
    def typef6(k, l): return ptype(k, l)
    xor6 = all((mask[k] ^ mask[R6[k]]) == functools.reduce(lambda a, b: a ^ b, (BETAM[c] for c in TOG6[k]), 0) for k in S)
    c6, exc6, kept6, nonv6 = rule_table(R6p, TOG6, C6, pairs6, typef6)
    frac6 = kept6 / len(pairs6)
    res6.append(dict(sheet=si, nJI=len(JI6), order=order6, orbits=sorted(orbs, reverse=True),
                     types=dict(tcount), xor=xor6, exc=exc6, frac=frac6, colours=dict(Counter(colour6.values()))))
    say("  sheet %d: |P6| = %d, Psi6 order %d, orbits %s, pair types %s, delta=XOR %s, rule exceptions %d, "
        "Schlaefli preservation %.4f" % (si, len(JI6), order6, sorted(orbs, reverse=True), dict(tcount), xor6, exc6, frac6))
check("AC5a", "REGISTERED: each 27-sheet (colour 6 deleted, SM-005) is J(P6) with |P6| = 16; its rowmotion "
      "Psi6 has order 12 with orbits [12,12,3] (the sealed MC values); the sheet's pair types are the "
      "Schlaefli adjacency (216 P / 135 S, no antipodes)",
      all(r["nJI"] == 16 and r["order"] == 12 and r["orbits"] == [12, 12, 3]
          and r["types"] == {"P": 216, "S": 135} for r in res6))
check("AC5b", "the same parity rule with the E6 Dynkin diagram is EXACT for Psi6 on both sheets "
      "(delta = XOR of toggled roots; 0 exceptions)",
      all(r["xor"] and r["exc"] == 0 for r in res6))
f6 = [r["frac"] for r in res6]
if all(f >= 0.6506 for f in f6):
    check("AC5c", "REGISTERED GUESS CONFIRMED: the E6 clock keeps %s of its sheet's Schlaefli incidence, "
          "at least the E7 clock's 65.06%%" % ["%.4f" % f for f in f6], True)
else:
    check("AC5c", "REGISTERED GUESS INVERTED (full prominence): the E6 clock keeps %s of its sheet's "
          "Schlaefli incidence -- LESS than the E7 clock's 65.06%%; smaller toggle sets do not mean fewer "
          "flips" % ["%.4f" % f for f in f6], False)

json.dump({"toggle_sizes": dict(sizes), "cells": {str(k): v for k, v in cells.items()}, "profile": prof,
           "e6": res6, "node_perm": list(pi)}, open(os.path.join(CACHE, "witnesses_ac.json"), "w"), indent=1)
banner("VERDICT")
say("""  The clock is rowmotion on the 27-element minuscule poset, exactly as
  sealed.  It flips the roof's incidence between two states iff the number
  of its toggled colours active on the other state, plus the same the
  other way, plus the Dynkin adjacencies between the two toggle sets, is
  odd.  The 65% is that count; the profile is the same rule iterated;
  the E6 sheets obey it with their own diagram.""")
say(""); say("RESULT: %d checks passed, %d failed%s" % (PASS, FAIL, ("  FAILED: %s" % FAILED) if FAILED else ""))
say("[t=%6.1fs] done" % (time.time() - T0)); LOG.close()
