# -*- coding: utf-8 -*-
r"""verify_stone_av_d5_anomaly.py -- STONE AV: THE D5 ANOMALY ON THE 4-CUBE

Brief: BRIEF_STONE_AV_D5_ANOMALY.md (lock BRIEF_STONE_AV_LOCK.sha256, re-verified as AV0).
AV1 the D5 half-spin and the B4 spinor are one clock (same poset, same rowmotion, W(B4) < W(D5)); AV2 the survivors
against the clock's two orbits; AV3 the half-turn anomaly lives on the 4-cube (B4: I_4 = 8 vs C_4 = 4, same extras);
AV4 not F2-affine, not a near-miss of linearity (altitudes); AV5 GUESS: specific to the 4-cube (B5: I_k = C_k; B3: half-turn
linear); AV6 GUESS: I_4 dihedral of order 8, conjugation by R^4 inverts the extras; AV7 [obs] D6 half-spin contrast.
Machinery: the e-coordinate board machine of _explore_d5_probes_2026-09-10.py VERBATIM (weights as vectors).
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_av_d5_anomaly.py
"""
import os, sys, time, json, hashlib, itertools
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_av_d5_anomaly.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AV -- THE D5 ANOMALY ON THE 4-CUBE"); say("=" * 78)
BRIEF = "BRIEF_STONE_AV_D5_ANOMALY.md"; LOCK = open("BRIEF_STONE_AV_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AV0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AV_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- e-coordinate board machine, VERBATIM from _explore_d5_probes_2026-09-10.py
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
def comp(p, q): return tuple(p[q[i]] for i in range(len(p)))
def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def ppow(p, e):
    x = tuple(range(len(p)))
    for _ in range(e): x = comp(p, x)
    return x
def closure(gens):
    e = tuple(range(len(gens[0]))); seen = {e}; fr = [e]
    while fr:
        nxt = []
        for g in fr:
            for s in gens:
                h = comp(s, g)
                if h not in seen: seen.add(h); nxt.append(h)
        fr = nxt
    return seen
def orbits(p):
    seen = set(); out = []
    for a in range(len(p)):
        if a in seen: continue
        o = []; x = a
        while x not in seen: seen.add(x); o.append(x); x = p[x]
        out.append(o)
    return out
def ctype(p): return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(len(o) for o in orbits(p)).items(), reverse=True))
def signed_perm(g, W, n):
    V = np.array([[float(x) for x in w] for w in W]); GV = np.array([[float(x) for x in W[g[i]]] for i in range(len(W))])
    A, *_ = np.linalg.lstsq(V, GV, rcond=None); A = np.rint(A.T).astype(int)
    return tuple("%se%d" % ("+" if A[i][j] > 0 else "-", j + 1) for i in range(n) for j in range(n) if A[i][j] != 0)
e = lambda i, n: tuple(Fraction(int(j == i)) for j in range(n))
# ---------------------------------------------------------------- boards
def D_half(n):  # even sign patterns; roots e_i - e_{i+1}, e_{n-1} + e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [tuple(x + y for x, y in zip(e(n - 2, n), e(n - 1, n)))]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n) if signs.count(-1) % 2 == 0]
    return board(w, roots)
def B_spin(n):  # all sign patterns; roots e_i - e_{i+1}, e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [e(n - 1, n)]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n)]
    return board(w, roots)
def IC(R, Wset, k):
    Rk = ppow(R, k); Rki = pinv(Rk)
    I = {g for g in Wset if comp(comp(Rki, g), Rk) in Wset}; C = {g for g in Wset if comp(g, Rk) == comp(Rk, g)}
    return I, C
W5, idx5, S5, R5, P5, leq5 = D_half(5); WD5 = closure(S5)
W4, idx4, S4, R4, P4, leq4 = B_spin(4); WB4 = closure(S4)
tick("D5 half-spin and B4 spinor built; |W(D5)| = %d, |W(B4)| = %d" % (len(WD5), len(WB4)))

banner("AV1 -- one clock on two boards")
match = {i: idx4[w[:4]] for i, w in enumerate(W5)}; inv_match = {v: k for k, v in match.items()}
R5_on_B4 = tuple(match[R5[inv_match[j]]] for j in range(16))
WB4_on_D5 = {tuple(inv_match[g[match[i]]] for i in range(16)) for g in WB4}
check("AV1", "the D5 half-spin and the B4 spinor have 10-element posets, the same rowmotion (type 8^2) under the identification, and W(B4) transported is a subgroup of W(D5) of order 384",
      len(P5) == 10 and len(P4) == 10 and sorted(match.values()) == list(range(16)) and R5_on_B4 == R4 and ctype(R5) == "8^2" and WB4_on_D5 <= WD5 and len(WB4) == 384 and len(WD5) == 1920)

banner("AV2 -- the survivors against the two orbits (D5 board)")
O = orbits(R5); orb_of = {x: i for i, o in enumerate(O) for x in o}
def action(g): return "preserves" if all(orb_of[g[x]] == orb_of[x] for x in range(16)) else ("swaps" if all(orb_of[g[x]] != orb_of[x] for x in range(16)) else "mixes")
w0 = tuple(idx5[tuple(-x for x in w[:4]) + (w[4],)] for w in W5)
I3, C3 = IC(R5, WD5, 3); I4, C4 = IC(R5, WD5, 4); I5, C5 = IC(R5, WD5, 5)
ident = tuple(range(16))
z3 = [g for g in I3 if g != ident]
extras4 = [g for g in I4 if g not in C4]
sp3 = [signed_perm(g, W5, 5) for g in z3]; sp4 = sorted(signed_perm(g, W5, 5) for g in extras4)
exp_z3 = ("+e3", "+e5", "+e1", "+e4", "+e2")
check("AV2a", "the clock has two free 8-orbits; w0 = -(e1..e4) preserves both and reverses R; the lag-3 survivor is the coordinate permutation (e1 e3)(e2 e5) and it MIXES the orbits",
      [len(o) for o in O] == [8, 8] and action(w0) == "preserves" and comp(comp(w0, R5), w0) == pinv(R5) and w0 in WD5
      and len(I3) == 2 and len(C3) == 1 and sp3 == [exp_z3] and action(z3[0]) == "mixes", (sp3, [action(g) for g in z3]))
check("AV2b", "|I_4| = 8, |C_4| = 4; all eight half-turn survivors preserve the orbits; the four extras are two signed 4-cycles on e1,e4,e2,e3 and two involutions, all fixing or negating e5",
      len(I4) == 8 and len(C4) == 4 and all(action(g) == "preserves" for g in I4) and len(extras4) == 4
      and sorted(ctype(g) for g in extras4) == ["2^8", "2^8", "4^4", "4^4"] and all(sp[4] in ("+e5", "-e5") for sp in sp4), sp4)
check("AV2c", "the lag-5 survivor set has order 2 and is the R^2-conjugate of the lag-3 one (I_5 = R^-2 I_3 R^2)", len(I5) == 2 and {comp(comp(pinv(ppow(R5, 2)), g), ppow(R5, 2)) for g in I3} == I5)

banner("AV3 -- the half-turn anomaly lives on the 4-cube (B4 board)")
sizesB = {k: (len(a), len(b)) for k, (a, b) in ((k, IC(R4, WB4, k)) for k in range(1, 8))}
I4B, C4B = IC(R4, WB4, 4)
extras4B = sorted(signed_perm(g, W4, 4) for g in I4B if g not in C4B)
extras4_restricted = sorted(tuple(x for x in sp if not x.endswith("e5")) for sp in sp4)
check("AV3", "on B4: I_k = C_k = {1} for k = 1, 2, 3 (and 5, 6, 7), |I_4| = 8 against |C_4| = 4, and the four extras are the D5 extras restricted to four coordinates",
      all(sizesB[k] == (1, 1) for k in (1, 2, 3, 5, 6, 7)) and sizesB[4] == (8, 4) and extras4B == extras4_restricted, (sizesB, extras4B))

banner("AV4 -- what it is not: F2-affine, or nearly linear")
def sign_pattern(v): return tuple(0 if x > 0 else 1 for x in v)
def is_affine(perm, pats, idx):
    def add(*ps): return tuple(sum(c) % 2 for c in zip(*ps))
    for a in range(len(pats)):
        for b in range(a, len(pats)):
            for c in range(b, len(pats)):
                s = add(pats[a], pats[b], pats[c])
                if s not in idx: return False
                if add(pats[perm[a]], pats[perm[b]], pats[perm[c]]) != pats[perm[idx[s]]]: return False
    return True
aff = {}
for n in (4, 5, 6):
    Wn, idxn, Sn, Rn, Pn, _ = D_half(n); pats = [sign_pattern(w) for w in Wn]; pidx = {p: i for i, p in enumerate(pats)}
    h = 2 * n - 2; aff[n] = [j for j in range(1, h) if is_affine(ppow(Rn, j), pats, pidx)]
alts = {}
for k in range(1, 8):
    Rk = ppow(R5, k); alts[k] = min(sum(1 for i in range(16) if g[i] != Rk[i]) for g in WD5)
check("AV4", "no power of the D5 (or D6) clock is affine over F2 on the even code; D4's half-turn is; altitudes of R^k against W(D5) are 10,10,7,8,7,10,10",
      aff[5] == [] and aff[6] == [] and aff[4] == [3] and [alts[k] for k in range(1, 8)] == [10, 10, 7, 8, 7, 10, 10], (aff, alts))
tick("AV4 done")

banner("AV5 -- REGISTERED GUESS: specific to the 4-cube (B5 and B3)")
W5b, idx5b, S5b, R5b, P5b, _ = B_spin(5); WB5 = closure(S5b)
sizes5 = {k: (len(a), len(b)) for k, (a, b) in ((k, IC(R5b, WB5, k)) for k in range(1, 10))}
W3b, idx3b, S3b, R3b, P3b, _ = B_spin(3); WB3 = closure(S3b)
I3_3, C3_3 = IC(R3b, WB3, 3)
ok5 = all(a == b for a, b in sizes5.values()) and len(WB5) == 3840 and ctype(R5b) == "10^3 2^1" and len(I3_3) == len(WB3) and ppow(R3b, 3) in WB3
check("AV5", "REGISTERED GUESS: on the B5 spinor (32, |W| = 3840, h = 10) I_k = C_k for every k; on the B3 spinor (8) the half-turn R^3 is a Weyl element and I_3 = W",
      ok5, "B5 sizes %s; B3 |I_3| = %d of %d" % (sizes5, len(I3_3), len(WB3)))
if not ok5: say("  [INVERTED] recorded at equal prominence.")
tick("AV5 done")

banner("AV6 -- REGISTERED GUESS: the structure of I_4 on the 4-cube")
Rk = ppow(R4, 4); Rki = pinv(Rk)
gI = list(I4B); orders = Counter(next(j for j in range(1, 9) if ppow(g, j) == tuple(range(16))) for g in gI)
nonab = any(comp(a, b) != comp(b, a) for a in gI for b in gI)
four = [g for g in I4B if g not in C4B and orders and ctype(g) == "4^4"]
gen = closure(list(C4B) + [four[0]]) if four else set()
inverts = all(comp(comp(Rki, g), Rk) == pinv(g) for g in I4B if g not in C4B)
ok6 = orders == Counter({1: 1, 2: 5, 4: 2}) and nonab and gen == I4B and inverts
check("AV6", "REGISTERED GUESS: I_4 on the 4-cube is dihedral of order 8 (five involutions, two elements of order 4, non-abelian), generated by C_4 and one signed 4-cycle, and R^-4 g R^4 = g^-1 for every extra g",
      ok6, "orders %s, nonabelian %s, generated %s, inverts %s" % (dict(orders), nonab, gen == I4B, inverts))
if not ok6: say("  [INVERTED] recorded at equal prominence.")

banner("AV2c-b / AV5b / AV6b -- POST-REVEAL, labelled")
R3 = ppow(R5, 3); R3i = pinv(R3)
check("AV2c-b", "POST-REVEAL: I_5 = I_{-3} = R^-3 I_3 R^3 (the brief's AV2c wrote R^2 for R^3 -- the auditor's slip)", {comp(comp(R3i, g), R3) for g in I3} == I5)
WD4_on_B3 = None
W4h, idx4h, S4h, R4h, P4h, _ = D_half(4); WD4 = closure(S4h)
m3 = {i: idx3b[w[:3]] for i, w in enumerate(W4h)}; inv3 = {v: k for k, v in m3.items()}
R4h_on_B3 = tuple(m3[R4h[inv3[j]]] for j in range(8))
WB3_on_D4 = {tuple(inv3[g[m3[i]]] for i in range(8)) for g in WB3}
C3_3 = {g for g in WB3 if comp(g, ppow(R3b, 3)) == comp(ppow(R3b, 3), g)}
check("AV5b", "POST-REVEAL: the B3 spinor is the D4 half-spin with the same rowmotion; its half-turn is a Weyl element of W(D4) (192) but NOT of W(B3) (48); |I_3| = 16 = |C_W(B3)(R^3)| -- the B5 clause of AV5 holds (I_k = C_k for all k, 2 at the half-turn)",
      R4h_on_B3 == R3b and WB3_on_D4 <= WD4 and ppow(R4h, 3) in WD4 and ppow(R3b, 3) not in WB3 and len(I3_3) == 16 and len(C3_3) == 16 and all(a == b for a, b in sizes5.values()),
      "|C_W(B3)(R^3)| = %d" % len(C3_3))
def name4(g): return signed_perm(g, W4, 4)
mapping = {name4(g): name4(comp(comp(Rki, g), Rk)) for g in I4B if g not in C4B}
extras_set = {name4(g) for g in I4B if g not in C4B}; cent_set = {name4(g) for g in C4B}
into_extras = all(v in extras_set for v in mapping.values())
check("AV6b", "POST-REVEAL: conjugation by R^4 permutes the four extras among themselves (never into the centralizer), but does not invert them: the map is recorded",
      into_extras and not all(comp(comp(Rki, g), Rk) == pinv(g) for g in I4B if g not in C4B), mapping)
banner("AV5c / AV8 -- POST-REVEAL, labelled: the overgroup mechanism")
check("AV5c", "POST-REVEAL: on B3 the shared grammar at the half-turn (16) exceeds the centralizer (8) because R^3 is a Weyl element of the OVERGROUP W(D4) of W(B3): a second board with the anomaly, with its mechanism visible",
      len(I3_3) == 16 and len(C3_3) == 8 and ppow(R4h, 3) in WD4 and WB3_on_D4 <= WD4)
from sympy.combinatorics import Permutation, PermutationGroup
def order_with(Wgens, extra): return PermutationGroup([Permutation(list(g)) for g in Wgens] + [Permutation(list(extra))]).order()
import math
o4 = order_with(S5, ppow(R5, 4)); o3 = order_with(S5, ppow(R5, 3)); o1 = order_with(S5, R5)
W6x, _, S6x, R6x, _, _ = D_half(6); o6 = order_with(S6x, ppow(R6x, 5))
note("[obs] AV8: |<W(D5), R^4>| = %d (= 16!/2? %s; = AGL(4,2) = 322560? %s); |<W(D5), R^3>| = %d; |<W(D5), R>| = %d (16!/2 = %d); D6 half-spin: |<W(D6), R^5>| = %d (32!/2 = %d)"
     % (o4, o4 == math.factorial(16) // 2, o4 == 322560, o3, o1, math.factorial(16) // 2, o6, math.factorial(32) // 2))
banner("AV7 -- [obs] the D6 half-spin at its half-turn, for contrast")
W6, idx6, S6, R6, P6, _ = D_half(6); WD6 = closure(S6); I5_6, C5_6 = IC(R6, WD6, 5)
O6 = orbits(R6); orb6 = {x: i for i, o in enumerate(O6) for x in o}
def action6(g):
    kinds = {(orb6[x], orb6[g[x]]) for x in range(32)}
    return "preserves" if all(a == b for a, b in kinds) else "moves orbits"
note("D6 half-spin: R type %s; |I_5| = %d = |C_5| = %d; survivors: %s" % (ctype(R6), len(I5_6), len(C5_6), [(ctype(g), action6(g), signed_perm(g, W6, 6)) for g in I5_6 if g != tuple(range(32))]))
tick("AV7 done")

json.dump({"brief_sha": sha, "D5_sizes": {k: (len(a), len(b)) for k, (a, b) in ((k, IC(R5, WD5, k)) for k in range(1, 8))}, "B4_sizes": sizesB, "B5_sizes": sizes5,
           "extras4": sp4, "z3": sp3, "affine": aff, "altitudes": alts}, open(os.path.join("_stone_av_cache", "witnesses_av.json"), "w"), indent=1, default=str)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
