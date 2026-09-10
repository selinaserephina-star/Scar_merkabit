# -*- coding: utf-8 -*-
r"""verify_stone_ay_d5_by_hand.py -- STONE AY: THE D5 ANOMALY BY HAND -- THE HALF-TURN IS A WEYL ELEMENT ON ONE ORBIT

Brief: BRIEF_STONE_AY_D5_BY_HAND.md (lock BRIEF_STONE_AY_LOCK.sha256, re-verified as AY0).
Lemma A: I_k = union over w in W of C_W(R^k w^-1).  Lemma B: if Fix(R^k w^-1) has trivial pointwise stabilizer in W,
then I_k restricted to its stabilizer is C_W(R^k w^-1) and the transport g -> R^-k g R^k is conjugation by w.
On the 4-cube: R^4 = -tau on the clock orbit O2, O2 determines Weyl elements, I_4 = C_W((-tau) R^4) of order 8.
AY1 Lemma A numerically (B4, D5); AY2 the hand clock; AY3 the agreement sets; AY4 Lemma B on the 4-cube; AY5 Stab(O1)
and I_4 by the list; AY6 the transport = tau-conjugation; AY7 the swappers; AY8 the binary phases; AY9 D5 lag 3 (and 4, 5);
AY10 the family: one correction suffices (REGISTERED GUESS); AY11 [obs] by hand, no computation.

Machinery: Stone AV's e-coordinate board machine VERBATIM; Stone AQ's Minuscule class and Stone AT's numpy BFS VERBATIM;
the anomalous-lag list from _stone_at_cache/table_at.json.  Membership by row bytes only (no isometry criterion).
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_ay_d5_by_hand.py
"""
import itertools, json, os, sys, time, hashlib
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ay_d5_by_hand.log", "w", encoding="utf-8")
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
CACHE = {}

say("=" * 78); say("STONE AY -- THE D5 ANOMALY BY HAND (the half-turn is a Weyl element on one orbit)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AY_D5_BY_HAND.md"; LOCK = open("BRIEF_STONE_AY_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AY0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AY_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
CACHE["brief_sha"] = sha

# ---------------------------------------------------------------- Stone AV's e-coordinate board machine, VERBATIM
AV = "verify_stone_av_d5_anomaly.py"; avsrc = open(AV, encoding="utf-8").read()
s0 = avsrc.index("# ---------------------------------------------------------------- e-coordinate board machine")
s1 = avsrc.index("W5, idx5, S5, R5, P5, leq5 = D_half(5)")
exec(compile(avsrc[s0:s1], AV, "exec"))
note("board machine loaded verbatim from %s (sha256 %s)" % (AV, hashlib.sha256(avsrc.encode("utf-8")).hexdigest()[:16]))

# ---------------------------------------------------------------- the 4-cube
W4, idx4, S4, R4, P4, leq4 = B_spin(4); WB4 = closure(S4)
W5, idx5, S5, R5, P5, leq5 = D_half(5); WD5 = closure(S5)
tick("B4 spinor (|W| = %d) and D5 half-spin (|W| = %d) built" % (len(WB4), len(WD5)))
ID = tuple(range(16))
def negset(w): return frozenset(i + 1 for i, x in enumerate(w) if x < 0)
SS = [negset(w) for w in W4]; idxS = {s: i for i, s in enumerate(SS)}
def fs(*a): return frozenset(a)
def sname(s): return "{" + ",".join(str(i) for i in sorted(s)) + "}" if s else "{}"
def aff(pi, v):
    """x -> pi x + v on the 16 sign patterns as bit vectors (bit i = 1 iff coordinate i negative); pi: dict i -> pi(i)."""
    out = []
    for w in W4:
        bits = {j + 1: (1 if w[j] < 0 else 0) for j in range(4)}
        nb = {pi.get(j, j): bits[j] for j in range(1, 5)}
        for j in range(1, 5): nb[j] ^= int(v[j - 1])
        out.append(idxS[frozenset(j for j in range(1, 5) if nb[j])])
    return tuple(out)
def cyc_dict(*cycles):
    pi = {}
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]): pi[a] = b
    return pi
def fixed(g): return frozenset(x for x in range(len(g)) if g[x] == x)
def cent(Wset, x): return {g for g in Wset if comp(g, x) == comp(x, g)}
def conj(a, g): return comp(comp(pinv(a), g), a)          # a^-1 g a
neg = aff({}, "1111"); tau = aff(cyc_dict((2, 3)), "0001"); negtau = aff(cyc_dict((2, 3)), "1110")
R4h = ppow(R4, 4)
I4, C4 = IC(R4, WB4, 4)
note("machine: |I_4| = %d, |C_4| = %d; tau in W: %s; C_4 == {1, -1, tau, -tau}: %s" % (len(I4), len(C4), tau in WB4, C4 == {ID, neg, tau, negtau}))

banner("AY2 -- the hand clock (REGISTERED: as written)")
REG1 = [fs(), fs(4), fs(3), fs(2, 4), fs(1, 3), fs(1, 2, 4), fs(1, 2, 3), fs(1, 2, 3, 4)]
REG2 = [fs(1), fs(3, 4), fs(2), fs(1, 4), fs(2, 3), fs(1, 3, 4), fs(1, 2), fs(2, 3, 4)]
def orbit_from(R, s):
    x = idxS[s]; seq = []
    for _ in range(8): seq.append(SS[x]); x = R[x]
    return seq
seq1 = orbit_from(R4, fs()); seq2 = orbit_from(R4, fs(1))
rev1 = [REG1[0]] + REG1[1:][::-1]; rev2 = [REG2[0]] + REG2[1:][::-1]
if seq1 == REG1 and seq2 == REG2: direction = "as written"; Rh = R4
elif seq1 == rev1 and seq2 == rev2: direction = "INVERSE (the machine's R is the hand's R^-1; phases read backwards)"; Rh = pinv(R4)
else: direction = "NEITHER"; Rh = R4
check("AY2", "the machine's rowmotion on the B4 board is the two registered 8-cycles, as written (not reversed)", direction == "as written",
      direction + "; O1: " + " -> ".join(sname(s) for s in seq1) + "; O2: " + " -> ".join(sname(s) for s in seq2))
O1 = frozenset(idxS[s] for s in REG1); O2 = frozenset(idxS[s] for s in REG2)
orbs = [frozenset(o) for o in orbits(R4)]
check("AY2b", "O1 (from {}) and O2 (from {1}) are exactly the two free clock orbits", set(orbs) == {O1, O2} and len(O1) == 8 and len(O2) == 8)
CACHE["clock_direction"] = direction; CACHE["O1"] = [sname(s) for s in seq1]; CACHE["O2"] = [sname(s) for s in seq2]

banner("AY3 -- H1: the agreement sets of R^4 with the Weyl elements (REGISTERED)")
Y = {g: fixed(comp(pinv(g), R4h)) for g in WB4}          # {x : R^4 x = g x}
dist = {g: 16 - len(Y[g]) for g in WB4}; dmin = min(dist.values()); nearest = [g for g in WB4 if dist[g] == dmin]
maxO1 = max(len(Y[g] & O1) for g in WB4); allO2 = [g for g in WB4 if O2 <= Y[g]]
check("AY3", "R^4 agrees with -tau exactly on O2; -tau is the unique nearest Weyl element (distance 8); no other Weyl element agrees on all of O2; none agrees on all of O1",
      Y[negtau] == O2 and dmin == 8 and nearest == [negtau] and allO2 == [negtau] and maxO1 < 8,
      "|Y(-tau)| = %d, min distance %d attained by %d element(s), agree-on-all-O2: %d, max agreement on O1: %d of 8" % (len(Y[negtau]), dmin, len(nearest), len(allO2), maxO1))
hist = Counter(len(Y[g]) for g in WB4)
note("agreement-size histogram over W(B4): " + ", ".join("%d:%d" % (k, v) for k, v in sorted(hist.items())))
CACHE["agreement_hist_B4_k4"] = {str(k): v for k, v in sorted(hist.items())}

banner("AY4 -- H2/H3: Lemma B on the 4-cube")
pstab = [g for g in WB4 if all(g[x] == x for x in O2)]
c = comp(negtau, R4h)
CWc = cent(WB4, c)
check("AY4a", "the pointwise stabilizer of O2 in W(B4) is trivial (O2 determines Weyl elements)", pstab == [ID], "%d element(s)" % len(pstab))
check("AY4b", "c = (-tau) R^4 fixes exactly O2, equals R^4 (-tau), and I_4 = C_W(c)", fixed(c) == O2 and c == comp(R4h, negtau) and CWc == I4,
      "|Fix c| = %d, |C_W(c)| = %d, |I_4| = %d, c type %s" % (len(fixed(c)), len(CWc), len(I4), ctype(c)))

banner("AY5 -- H4: Stab_W(O1) and I_4 by the hand list (REGISTERED)")
pid = {}; p1234 = cyc_dict((1, 2), (3, 4)); p23 = cyc_dict((2, 3)); p1342 = cyc_dict((1, 3, 4, 2)); p14 = cyc_dict((1, 4)); p1243 = cyc_dict((1, 2, 4, 3))
p1423 = cyc_dict((1, 4), (2, 3)); p1324 = cyc_dict((1, 3), (2, 4))
LIST16 = [(pi, v) for pis, vs in [((pid, p1234), ("0000", "1111")), ((p23, p1342), ("0001", "1110")), ((p14, p1243), ("0010", "1101")), ((p1423, p1324), ("0101", "1010"))]
          for pi in pis for v in vs]
els16 = [aff(pi, v) for pi, v in LIST16]
stab1 = {g for g in WB4 if frozenset(g[x] for x in O1) == O1}
Vpis = (pid, p23, p14, p1423)
els8 = [aff(pi, v) for pi, v in LIST16 if pi in Vpis]
check("AY5a", "Stab_W(O1) is exactly the sixteen listed affine maps", stab1 == set(els16) and len(els16) == 16 and len(set(els16)) == 16, "|Stab_W(O1)| = %d" % len(stab1))
check("AY5b", "I_4 is exactly the eight with pi in V = {1,(14),(23),(14)(23)}; C_4 = C_W(c) meet C_W(tau)", I4 == set(els8) and C4 == (CWc & cent(WB4, tau)))
E1 = aff(p14, "0010"); E4 = aff(p14, "1101"); E2 = aff(p1423, "0101"); E3 = aff(p1423, "1010")
check("AY5c", "the four extras are E1, E4, E2, E3 as named; in Stone AV's coordinates: (e1<->e4,-e3), (e1<->-e4,-e2), the signed 4-cycle, its inverse",
      set(I4) - set(C4) == {E1, E2, E3, E4}, "; ".join(str(signed_perm(g, W4, 4)) for g in (E1, E4, E2, E3)))
CACHE["stab_O1"] = [signed_perm(g, W4, 4) for g in els16]; CACHE["I4"] = [signed_perm(g, W4, 4) for g in els8]

banner("AY6 -- H5: the transport on I_4 is conjugation by tau")
tr = lambda g: conj(R4h, g)
comm = comp(comp(comp(pinv(E1), pinv(R4h)), E1), R4h)
check("AY6a", "for every g in I_4: R^-4 g R^4 = tau g tau", all(tr(g) == conj(tau, g) for g in I4))
check("AY6b", "E1 <-> E4 and E2 <-> E3 = E2^-1 under the transport (Stone AV's AV6b map); E2^2 = -1; [E1, R^4] = E1 E4 = -1",
      tr(E1) == E4 and tr(E4) == E1 and tr(E2) == E3 and tr(E3) == E2 and comp(E2, E3) == ID and comp(E2, E2) == neg and comm == neg and comp(E1, E4) == neg)

banner("AY7 -- H6: the orbit swappers")
stabpart = {g for g in WB4 if frozenset(g[x] for x in O1) in (O1, O2)}
swappers = {g for g in stabpart if frozenset(g[x] for x in O1) == O2}
sw = aff(p23, "1000")
check("AY7", "Stab_W({O1,O2}) has order 32; (e2 e3)(-e1) swaps the orbits; no element of I_4 swaps them",
      len(stabpart) == 32 and sw in swappers and not (I4 & swappers), "|Stab| = %d, |swappers| = %d, (e2e3)(-e1) = %s" % (len(stabpart), len(swappers), signed_perm(sw, W4, 4)))

banner("AY8 -- H7: the binary phases (REGISTERED)")
def phases(R, start):
    ph = {}; x = idxS[start]
    for p in range(8): ph[x] = p; x = R[x]
    return ph
ph1 = phases(Rh, fs()); ph2 = phases(Rh, fs(1))
def is_xor(g, ph, t): return all(ph[g[x]] == (ph[x] ^ t) for x in ph)
def xor_of(g, ph): return [t for t in range(8) if is_xor(g, ph, t)]
rows = [("-1", neg, 7, 7), ("tau", tau, 1, 3), ("R^4", R4h, 4, 4)]
okp = all(xor_of(g, ph1) == [t1] and xor_of(g, ph2) == [t2] for _, g, t1, t2 in rows)
extras_not = all(xor_of(g, ph1) == [] and xor_of(g, ph2) == [] for g in (E1, E2, E3, E4))
check("AY8", "-1 = XOR 111 on both orbits; tau = XOR 001 on O1 and XOR 011 on O2; R^4 = XOR 100 on both; the four extras are phase translations on neither orbit",
      okp and extras_not, "; ".join("%s: O1 %s O2 %s" % (nm, xor_of(g, ph1), xor_of(g, ph2)) for nm, g, _, _ in rows) + "; extras on O1: " + str([xor_of(g, ph1) for g in (E1, E2, E3, E4)]))
note("C_4 on O1 = translations {%s}; on O2 = {%s}" % (",".join(format(xor_of(g, ph1)[0], "03b") for g in (ID, neg, tau, negtau)), ",".join(format(xor_of(g, ph2)[0], "03b") for g in (ID, neg, tau, negtau))))

banner("AY1 -- Lemma A numerically: I_k = union_w C_W(R^k w^-1) on B4 and D5, all lags")
def lemmaA(Wset, R, N, label_):
    G = np.array(sorted(Wset), dtype=np.uint8); Wb = {row.tobytes() for row in G}; Wn = len(G)
    Ginv = np.empty_like(G)
    for i in range(Wn): Ginv[i, G[i]] = np.arange(N, dtype=np.uint8)
    Rn = np.array(R, dtype=np.uint8); ok = True; out = {}
    for k in range(1, 8):
        Pk = Rn.copy()
        for _ in range(k - 1): Pk = Rn[Pk]
        Pki = np.empty_like(Pk); Pki[Pk] = np.arange(N, dtype=np.uint8)
        Imask = np.fromiter(((Pki[g[Pk]]).tobytes() in Wb for g in G), dtype=bool, count=Wn)
        union = np.zeros(Wn, dtype=bool)
        for i in range(Wn):
            x = Pk[Ginv[i]]                                    # R^k w^-1
            union |= np.all(G[:, x] == x[G], axis=1)
        eq = bool(np.array_equal(union, Imask)); ok &= eq; out[k] = (int(Imask.sum()), int(union.sum()), eq)
    note("%s: " % label_ + "; ".join("k=%d |I|=%d |union|=%d %s" % (k, a, b, "=" if e_ else "!=") for k, (a, b, e_) in out.items()))
    return ok
okA = lemmaA(WB4, R4, 16, "B4") and lemmaA(WD5, R5, 16, "D5")
check("AY1", "Lemma A holds numerically on B4 and D5 at every lag k = 1..7", okA)
tick("Lemma A checked")

banner("AY9 -- D5 half-spin: lag 3 (REGISTERED), lag 5, lag 4")
def sp5(images):
    """signed permutation of R^5 by images e_i -> eps e_sigma(i); images: dict i -> (sigma(i), eps); as a permutation of the D5 weights."""
    out = []
    for w in W5:
        v = [None] * 5
        for i in range(5):
            j, eps = images.get(i + 1, (i + 1, 1)); v[j - 1] = eps * w[i]
        out.append(idx5[tuple(v)])
    return tuple(out)
p_surv = sp5({1: (3, 1), 3: (1, 1), 2: (5, 1), 5: (2, 1)})
ID16 = tuple(range(16)); WD5s = sorted(WD5)
res9 = {}; WK = {}
for k in (3, 5):
    Rk = ppow(R5, k); Ik, Ck = IC(R5, WD5, k)
    Yk = {g: fixed(comp(pinv(g), Rk)) for g in WD5}; dk = {g: 16 - len(Yk[g]) for g in WD5}; dmn = min(dk.values()); near = [g for g in WD5 if dk[g] == dmn]
    wk = near[0]; ck = comp(Rk, pinv(wk)); Yw = fixed(ck); ps = [g for g in WD5 if all(g[x] == x for x in Yw)]
    Cc = cent(WD5, ck)
    carriers = [w for w in WD5 if comp(p_surv, comp(Rk, pinv(w))) == comp(comp(Rk, pinv(w)), p_surv)]
    transport_ok = conj(Rk, p_surv) == conj(wk, p_surv)
    WK[k] = wk
    res9[k] = dict(nI=len(Ik), nC=len(Ck), dmin=dmn, nnear=len(near), w=signed_perm(wk, W5, 5), Ysize=len(Yw), pstab=len(ps), p_in_Cc=(p_surv in Cc), Cc=len(Cc), Ik_eq_Cc=(Ik == Cc), ncarriers=len(carriers), transport=transport_ok, Ik=[signed_perm(g, W5, 5) for g in Ik])
    note("k=%d: |I|=%d |C|=%d; nearest distance %d attained by %d; w_k = %s; |Y| = %d, pointwise stabilizer %d; p in C_W(c): %s (|C_W(c)| = %d); I_k == C_W(c): %s; #w carrying p: %d; transport of p = conj by w_k: %s"
         % (k, len(Ik), len(Ck), dmn, len(near), res9[k]["w"], len(Yw), len(ps), p_surv in Cc, len(Cc), Ik == Cc, len(carriers), transport_ok))
r3 = res9[3]
check("AY9", "REGISTERED GUESS: on D5 at lag 3 the nearest Weyl element is unique (distance 7), its agreement set (9 points) determines Weyl elements, the survivor (e1 e3)(e2 e5) commutes with the correction, I_3 = C_W(R^3 w^-1) = {1, p}, and p's transport is conjugation by w",
      p_surv in WD5 and r3["nnear"] == 1 and r3["dmin"] == 7 and r3["Ysize"] == 9 and r3["pstab"] == 1 and r3["p_in_Cc"] and r3["Ik_eq_Cc"] and r3["nI"] == 2 and r3["transport"],
      "p in W(D5): %s; %s" % (p_surv in WD5, {k_: v_ for k_, v_ in r3.items() if k_ != "Ik"}))
r5 = res9[5]
check("AY9b", "the same at lag 5 (SM-059's reversal)", r5["nnear"] == 1 and r5["dmin"] == 7 and r5["Ysize"] == 9 and r5["pstab"] == 1 and r5["p_in_Cc"] and r5["Ik_eq_Cc"] and r5["transport"], {k_: v_ for k_, v_ in r5.items() if k_ != "Ik"})
w4 = sp5({1: (1, -1), 2: (3, -1), 3: (2, -1), 4: (4, 1), 5: (5, -1)})
R54 = ppow(R5, 4); I54, C54 = IC(R5, WD5, 4); c54 = comp(R54, pinv(w4)); Y54 = fixed(c54)
O2_D5 = frozenset(i for i, w in enumerate(W5) if negset(w[:4]) in set(REG2))
ps54 = [g for g in WD5 if all(g[x] == x for x in Y54)]
check("AY9c", "lag 4 on D5 with w = (-e1,-e3,-e2,+e4,-e5): the correction fixes exactly the D5 image of O2, that set determines W(D5), and I_4 = C_W(correction) of order 8",
      w4 in WD5 and Y54 == O2_D5 and ps54 == [ID16] and cent(WD5, c54) == I54 and len(I54) == 8, "|Fix| = %d, pointwise stabilizer %d, |C_W(c)| = %d, |I_4| = %d" % (len(Y54), len(ps54), len(cent(WD5, c54)), len(I54)))
CACHE["D5"] = {str(k): {k_: v_ for k_, v_ in v.items()} for k, v in res9.items()}
tick("D5 done")

banner("AY10 -- the family: one correction suffices (REGISTERED GUESS)")
def gens_of(elements):
    """greedy generating set of a small permutation group given as tuples"""
    els = sorted(elements); n = len(els[0]); gens = []; cl = {tuple(range(n))}
    for g in els:
        if g not in cl:
            gens.append(g); cl = closure(gens)
    return gens
def one_correction_tuple(Wset, R, k, I):
    """brute force over W (tuples): #w with w^-1 g w = R^-k g R^k for all g in I; returns (count, example)"""
    Rk = ppow(R, k); gens = gens_of(I) if len(I) < len(Wset) else None
    if gens is None: gens = gens_of(I)
    sols = [w for w in Wset if all(conj(w, g) == conj(Rk, g) for g in gens)]
    return len(sols), (sols[0] if sols else None), len(gens)
FAM = []
# B3 spinor at lag 3, B4 at lag 4, D5 at lags 3, 4, 5 (tuple machinery)
W3, idx3, S3, R3, P3, leq3 = B_spin(3); WB3 = closure(S3)
for label_, Wset, R, N, lags in [("B3 spinor", WB3, R3, 8, (3,)), ("B4 spinor", WB4, R4, 16, (4,)), ("D5 half-spin", WD5, R5, 16, (3, 4, 5))]:
    for k in lags:
        I, C = IC(R, Wset, k)
        if I == C: continue
        n_sol, ex, ng = one_correction_tuple(Wset, R, k, I)
        Rk = ppow(R, k)
        FAM.append(dict(board=label_, k=k, nI=len(I), nC=len(C), nW=len(Wset), n_sol=n_sol, gens=ng, example=(ctype(ex) if ex else None), ex_commutes_Rk=(ex is not None and comp(ex, Rk) == comp(Rk, ex))))
        note("%-14s k=%d |I|=%d |C|=%d |W|=%d: solutions w: %d (of |W|)%s" % (label_, k, len(I), len(C), len(Wset), n_sol, ("; example type %s, commutes with R^k: %s" % (ctype(ex), comp(ex, Rk) == comp(Rk, ex))) if ex else ""))
# the 42 (Minuscule VERBATIM from AQ; BFS VERBATIM from AT)
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
AT = "verify_stone_at_grammar_family.py"; atsrc = open(AT, encoding="utf-8").read()
a0 = atsrc.index("def enumerate_W_np(M):"); a1 = atsrc.index("def cyc(p):")
exec(compile(atsrc[a0:a1], AT, "exec"))
note("Minuscule machine from %s (sha256 %s); BFS from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16], AT, hashlib.sha256(atsrc.encode("utf-8")).hexdigest()[:16]))
TAB = json.load(open("_stone_at_cache/table_at.json", encoding="utf-8"))["table"]
todo = [(r["fam"], r["n"], r["k"], sorted(int(kk) for kk in r["sizes"] if r["sizes"][kk] != r["sizesC"][kk])) for r in TAB if r["sizes"] != r["sizesC"]]
note("anomalous boards from SM-058's table: %d boards, %d (board, lag) pairs" % (len(todo), sum(len(t[3]) for t in todo)))
repro_ok = True
for fam, n, k, lags in todo:
    M = Minuscule(fam, n, k); N = M.N; G, Wbytes = enumerate_W_np(M); Wn = len(G); R = np.array(M.R, dtype=np.uint8)
    tick("%s%d k=%d: |W| = %d, N = %d" % (fam, n, k, Wn, N))
    Sgens = [np.array(s, dtype=np.uint8) for s in M.S]
    for kk in lags:
        Pk = pow_arr(R, kk); Pki = inv_arr(Pk)
        Hm = Pki[G[:, Pk]]
        Imask = np.fromiter((row.tobytes() in Wbytes for row in Hm), dtype=bool, count=Wn)
        Cmask = np.all(G[:, Pk] == Pk[G], axis=1)
        nI, nC = int(Imask.sum()), int(Cmask.sum())
        row = next(r for r in TAB if (r["fam"], r["n"], r["k"]) == (fam, n, k))
        if (nI, nC) != (row["sizes"][str(kk)], row["sizesC"][str(kk)]): repro_ok = False
        if nI == Wn: gens = Sgens
        else: gens = [np.array(g, dtype=np.uint8) for g in gens_of([tuple(int(x) for x in g) for g in G[Imask]])]
        m = np.ones(Wn, dtype=bool)
        for g in gens:
            t = Pki[g[Pk]]
            m &= np.all(g[G] == G[:, t], axis=1)
        n_sol = int(m.sum()); ex = G[np.nonzero(m)[0][0]] if n_sol else None
        ex_c = bool(np.array_equal(ex[Pk], Pk[ex])) if ex is not None else None
        ex_pow = (next((j for j in range(1, 2 * N) if np.array_equal(ex, pow_arr(R, j))), None)) if ex is not None else None
        FAM.append(dict(board="%s%d w%d" % (fam, n, k), k=kk, nI=nI, nC=nC, nW=Wn, n_sol=n_sol, gens=len(gens), example=(ctype(tuple(int(x) for x in ex)) if ex is not None else None), ex_commutes_Rk=ex_c, ex_power_of_R=ex_pow))   # first run: AT's cyc lies outside the loaded slice (instrumentation), FIRSTRUN log kept
        note("  lag %2d: |I|=%6d |C|=%5d  solutions w: %6d%s" % (kk, nI, nC, n_sol, ("; example %s%s%s" % (ctype(tuple(int(x) for x in ex)), ", commutes with R^k" if ex_c else ", does NOT commute with R^k", (", = R^%d" % ex_pow) if ex_pow else "")) if ex is not None else "  -- NONE: two corrections needed"))
check("AY10a", "[P] SM-058's (|I_k|, |C_k|) reproduced on every anomalous board and lag from the AQ/AT machines", repro_ok)
bad = [f for f in FAM if f["n_sol"] == 0]
check("AY10", "REGISTERED GUESS: on every anomalous board and lag (the 42's chains, A3w2, D_n vectors, D5 half-spins; B3 lag 3; B4 lag 4) the transport on I_k is conjugation by a single Weyl element",
      not bad, ("all %d (board, lag) pairs" % len(FAM)) if not bad else ("INVERTED: first failure %s lag %d (|I|=%d, |C|=%d); %d failures of %d" % (bad[0]["board"], bad[0]["k"], bad[0]["nI"], bad[0]["nC"], len(bad), len(FAM))))
CACHE["family"] = FAM
tick("family done")

banner("POST-REVEAL (labelled, after the first sealed run): AY2-b, AY9b-b, AY10b")
check("AY2-b", "POST-REVEAL: the machine's rowmotion on the B4 board is exactly the inverse of the hand's two 8-cycles (the AV machine grows ideals from the lowest weight, the hand from the highest: dual lattices, inverse rowmotion); the phases of AY8 were read along the hand's direction",
      seq1 == rev1 and seq2 == rev2 and Rh == pinv(R4))
R53 = ppow(R5, 3); R55 = ppow(R5, 5); I55, _ = IC(R5, WD5, 5); p5 = next(g for g in I55 if g != ID16)
w5 = WK[5]; c5 = comp(R55, pinv(w5)); w3 = WK[3]
check("AY9b-b", "POST-REVEAL: the lag-5 survivor is the transport of p, R^-3 p R^3 = w_3^-1 p w_3 (the brief named p itself: the auditor's slip); with it, Lemma B holds at lag 5 with the nearest w_5: p_5 commutes with the correction, I_5 = C_W(R^5 w_5^-1), and p_5's transport is conjugation by w_5",
      p5 == conj(R53, p_surv) and p5 == conj(w3, p_surv) and p5 in cent(WD5, c5) and I55 == cent(WD5, c5) and conj(R55, p5) == conj(w5, p5),
      "p_5 = %s" % str(signed_perm(p5, W5, 5)))
CACHE["D5"]["5"]["survivor_p5"] = signed_perm(p5, W5, 5)
sols4 = [w for w in WB4 if all(conj(w, g) == conj(R4h, g) for g in I4)]
note("the four Weyl elements realising the transport on the 4-cube: " + "; ".join(str(signed_perm(w, W4, 4)) for w in sols4) + "  (the coset (-tau) C_W(I_4))")
CACHE["B4_transport_solutions"] = [signed_perm(w, W4, 4) for w in sols4]
def carriers(G, Ig, Pk, Pki):
    """M[w, j] = (w carries I-element j): g_j w = w t_j with t_j the transport of g_j"""
    Wn = len(G); M = np.zeros((Wn, len(Ig)), dtype=bool)
    for j, g in enumerate(Ig):
        t = Pki[g[Pk]]; M[:, j] = np.all(g[G] == G[:, t], axis=1)
    return M
def min_cover(M):
    """(uncarried, nmin, ndist, exact): elements of I carried by no w; then the exact minimum number of w's covering I (exact when <= 3)"""
    nI = M.shape[1]; full = (1 << nI) - 1
    uncarried = int((M.sum(axis=0) == 0).sum())
    if uncarried: return uncarried, None, None, True
    subs = set()
    for row in np.packbits(M, axis=1, bitorder="little"): subs.add(int.from_bytes(row.tobytes(), "little"))
    D = sorted(subs, key=lambda m: -bin(m).count("1"))
    if len(D) <= 3000: D = [d for d in D if not any(d != e_ and (d & e_) == d for e_ in D)]
    if any(d == full for d in D): return 0, 1, len(D), True
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            if D[i] | D[j] == full: return 0, 2, len(D), True
    if len(D) <= 120:
        for i in range(len(D)):
            for j in range(i + 1, len(D)):
                for l in range(j + 1, len(D)):
                    if D[i] | D[j] | D[l] == full: return 0, 3, len(D), True
    cov = 0; n = 0
    while cov != full:
        best = max(D, key=lambda d: bin(d & ~cov).count("1")); cov |= best; n += 1
    return 0, n, len(D), (n <= 3)
# Lemma A as written in the brief is WRONG in its second step: R^-k g R^k in W does not mean R^-k g R^k = w^-1 g w for a Weyl w.
# Only the inclusion union_w C_W(R^k w^-1) <= I_k is proved; equality holds exactly when every transport is W-conjugate to its element.
# Post-reveal: measured on every anomalous pair (the "uncarried" count); the first sealed run hung here (an impossible set cover), FIRSTRUN log kept.
COVER = []
fails = [f for f in FAM if f["n_sol"] == 0]
for f in fails:
    b = f["board"]; kk = f["k"]
    if b == "B3 spinor":
        G3 = np.array(sorted(WB3), dtype=np.uint8); Rn = np.array(R3, dtype=np.uint8); Pk = pow_arr(Rn, kk); Pki = inv_arr(Pk)
        I3s, _ = IC(R3, WB3, kk); Ig = [np.array(g, dtype=np.uint8) for g in sorted(I3s)]; G = G3
    else:
        fam, n, k = b[0], int(b[1]), int(b.split("w")[1]); M = Minuscule(fam, n, k); G, Wbytes = enumerate_W_np(M); Rn = np.array(M.R, dtype=np.uint8)
        Pk = pow_arr(Rn, kk); Pki = inv_arr(Pk); Hm = Pki[G[:, Pk]]
        Imask = np.fromiter((row.tobytes() in Wbytes for row in Hm), dtype=bool, count=len(G)); Ig = [g for g in G[Imask]]
    Mc = carriers(G, Ig, Pk, Pki)
    unc, nmin, ndist, exact = min_cover(Mc)
    COVER.append(dict(board=b, k=kk, nI=len(Ig), uncarried=unc, min_corrections=nmin, exact=exact, maximal_carried_subsets=ndist, max_carried=int(Mc.sum(axis=1).max())))
    if unc: note("%-14s lag %2d |I|=%4d: %d of %d elements have a transport that is NOT W-conjugate to them (the union of centralizers is a strict subset of I_k; no cover exists); the best single w carries %d" % (b, kk, len(Ig), unc, len(Ig), int(Mc.sum(axis=1).max())))
    else: note("%-14s lag %2d |I|=%4d: every transport is W-inner; corrections needed %d%s (%d maximal carried subsets; the best single w carries %d of %d)" % (b, kk, len(Ig), nmin, "" if exact else " (greedy bound)", ndist, int(Mc.sum(axis=1).max()), len(Ig)))
unc_pairs = [c_ for c_ in COVER if c_["uncarried"]]
check("AY1-b", "POST-REVEAL, the auditor's own error: Lemma A's proof is wrong as written (only the inclusion union <= I_k holds; equality needs every transport W-conjugate to its element). Measured: the equality holds on B4 and D5 (AY1) and FAILS on the B3 spinor at lag 3, where transports leave the W-conjugacy classes",
      any(c_["board"] == "B3 spinor" and c_["uncarried"] > 0 for c_ in COVER), "pairs with non-inner transports: %d of %d failing pairs: %s" % (len(unc_pairs), len(COVER), "; ".join("%s k=%d (%d of %d)" % (c_["board"], c_["k"], c_["uncarried"], c_["nI"]) for c_ in unc_pairs)))
inner_pairs = [c_ for c_ in COVER if not c_["uncarried"]]
# AY10c [obs], post-reveal: are the non-inner transports conjugation by the antipode (which is not a Weyl element on A3w2 and the odd D_n vectors)?
ANTI = []
for f in fails:
    b = f["board"]; kk = f["k"]
    if b == "B3 spinor": continue
    fam, n, k = b[0], int(b[1]), int(b.split("w")[1]); M = Minuscule(fam, n, k); G, Wbytes = enumerate_W_np(M); Rn = np.array(M.R, dtype=np.uint8)
    lam = M.W[M.top]
    if tuple(-x for x in lam) not in M.idx: continue
    IOTA = np.array([M.idx[tuple(-x for x in w)] for w in M.W], dtype=np.uint8); iota_in_W = IOTA.tobytes() in Wbytes
    Pk = pow_arr(Rn, kk); Pki = inv_arr(Pk); Hm = Pki[G[:, Pk]]
    Imask = np.fromiter((row.tobytes() in Wbytes for row in Hm), dtype=bool, count=len(G)); Ig = [g for g in G[Imask]]
    Mc = carriers(G, Ig, Pk, Pki); unc_idx = [j for j in range(len(Ig)) if Mc[:, j].sum() == 0]
    by_iota = sum(1 for j in unc_idx if np.array_equal(Pki[Ig[j][Pk]], IOTA[Ig[j][IOTA]]))
    ANTI.append(dict(board=b, k=kk, iota_in_W=bool(iota_in_W), uncarried=len(unc_idx), by_antipode=int(by_iota)))
    note("%-8s lag %2d: antipode in W: %s; of %d non-inner transports, %d equal conjugation by the antipode" % (b, kk, iota_in_W, len(unc_idx), by_iota))
check("AY10c", "POST-REVEAL [obs]: on A3w2 and the odd D_n vectors the antipode is not a Weyl element and every non-inner transport is conjugation by the antipode",
      bool(ANTI) and all((not a["iota_in_W"]) and a["by_antipode"] == a["uncarried"] for a in ANTI), "; ".join("%s k=%d %d/%d" % (a["board"], a["k"], a["by_antipode"], a["uncarried"]) for a in ANTI))
CACHE["antipode"] = ANTI
# AY10d [obs], post-reveal (after AY10c failed): are the non-inner transports inner in the OVERGROUP -- W(D4) for the B3 spinor (Stone AV's AV5c),
# and for A3w2 = the D3 vector and the odd D_n vectors the stabilizer of the antipodal pairing, W(B_n) = <W(D_n), one pair swap>?
def bfs_np(gens, N):
    ident = np.arange(N, dtype=np.uint8); seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
    while len(frontier):
        cand = np.concatenate([frontier[:, g] for g in gens], axis=0); keep = []
        for row in cand:
            b = row.tobytes()
            if b not in seen: seen.add(b); keep.append(row)
        frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, N), dtype=np.uint8)
        if len(frontier): layers.append(frontier)
    return np.concatenate(layers, axis=0)
OVER = []
for f in fails:
    b = f["board"]; kk = f["k"]
    if b == "B3 spinor":
        G = np.array(sorted(WB3), dtype=np.uint8); Rn = np.array(R3, dtype=np.uint8); N = 8; Pk = pow_arr(Rn, kk); Pki = inv_arr(Pk)
        I3s, _ = IC(R3, WB3, kk); Ig = [np.array(g, dtype=np.uint8) for g in sorted(I3s)]
        Gover = bfs_np([np.array(g_, dtype=np.uint8) for g_ in S3] + [pow_arr(Rn, 3)], N); over_name = "<W(B3), R^3> (= W(D4) by Stone AV)"
    else:
        fam, n, k = b[0], int(b[1]), int(b.split("w")[1]); M = Minuscule(fam, n, k); G, Wbytes = enumerate_W_np(M); Rn = np.array(M.R, dtype=np.uint8); N = M.N
        Pk = pow_arr(Rn, kk); Pki = inv_arr(Pk); Hm = Pki[G[:, Pk]]
        Imask = np.fromiter((row.tobytes() in Wbytes for row in Hm), dtype=bool, count=len(G)); Ig = [g for g in G[Imask]]
        lam = M.W[M.top]; IOTA = np.array([M.idx[tuple(-x for x in w)] for w in M.W], dtype=np.uint8)
        swap = np.arange(N, dtype=np.uint8); swap[0], swap[IOTA[0]] = IOTA[0], 0          # one antipodal pair transposed
        Gover = bfs_np([np.array(s_, dtype=np.uint8) for s_ in M.S] + [swap], N); over_name = "<W, one antipodal swap> (the stabilizer of the pairing)"
    Mo = carriers(Gover, Ig, Pk, Pki); unc = int((Mo.sum(axis=0) == 0).sum())
    m = np.ones(len(Gover), dtype=bool)
    for j, g in enumerate(Ig):
        t = Pki[g[Pk]]; m &= np.all(g[Gover] == Gover[:, t], axis=1)
    OVER.append(dict(board=b, k=kk, overgroup=over_name, over_order=int(len(Gover)), W_order=int(len(G)), uncarried_in_overgroup=unc, single_u_in_overgroup=int(m.sum())))
    note("%-14s lag %2d: overgroup %s of order %d (= %d x |W|): elements of I_k not carried by any u: %d; single u realising the whole transport: %d" % (b, kk, over_name, len(Gover), len(Gover) // len(G), unc, int(m.sum())))
check("AY10d", "POST-REVEAL [obs]: every non-inner transport in the family is inner in the overgroup (W(D4) for B3; the pairing stabilizer W(B_n) for A3w2 and the odd D_n vectors), and there a single element realises the whole transport",
      bool(OVER) and all(o["uncarried_in_overgroup"] == 0 and o["single_u_in_overgroup"] > 0 for o in OVER), "; ".join("%s k=%d: %d uncarried, %d single u" % (o["board"], o["k"], o["uncarried_in_overgroup"], o["single_u_in_overgroup"]) for o in OVER))
CACHE["overgroup"] = OVER
check("AY10b", "POST-REVEAL [obs]: on every failing pair whose transports are all W-inner, exactly two corrections cover I_k", all(c_["min_corrections"] == 2 and c_["exact"] for c_ in inner_pairs),
      ("; ".join("%s k=%d: %d" % (c_["board"], c_["k"], c_["min_corrections"]) for c_ in inner_pairs)) if inner_pairs else "no such pair: every failure is a non-inner transport")
CACHE["cover"] = COVER
tick("post-reveal done")

banner("AY11 -- [obs], by hand")
note("the anomaly is already on B4, whose reverser -1 is central in W(B4); it is not tied to D5's non-central reverser (SM-062 section 7.11.4). No computation.")

os.makedirs("_stone_ay_cache", exist_ok=True)
json.dump(CACHE, open("_stone_ay_cache/witnesses_ay.json", "w", encoding="utf-8"), indent=1, default=str)
npass = sum(1 for _, ok in RESULTS if ok); nfail = len(RESULTS) - npass
say("\n" + "=" * 78); say("SUMMARY: %d PASS, %d FAIL of %d checks" % (npass, nfail, len(RESULTS)))
for tag, ok in RESULTS:
    if not ok: say("  FAIL: %s" % tag)
tick("done"); LOG.close()
