# -*- coding: utf-8 -*-
r"""verify_stone_ax_c_equals_t.py -- STONE AX: C = T -- THE REVERSER AS A CONSTRAINT ON THE GRAMMAR

Brief: BRIEF_STONE_AX_C_EQUALS_T.md (lock BRIEF_STONE_AX_LOCK.sha256, re-verified as AX0).
AX1 reversers of R inside W form the coset w0.C_W(R) (counts on the 38 boards with |W| <= 400,000; the four large
boards cited from SM-058/SM-059, E7 re-measured on the 56); AX2 conjugation by w0 induces the diagram automorphism on the
simple reflections on all 42 boards -- central exactly where -1 in W; on the 56: iota central, w0(E6) induces sigma_6 on
the six E6 reflections and (GUESS) does not commute with the seventh; AX3 GUESS: the bridge copy's normaliser in W(E7)
is 2 x PGL(2,7) (order 672, centraliser <iota>), so W(E7) realises the outer automorphism of PSL(2,7) by a Weyl element c;
AX4 c is not iota, does not commute with Psi, does not reverse Psi -- C != T on the grammar; AX5 the permutation
character of P on the 28 iota-pairs = chi1 + 2 chi6 + chi7 + chi8 (SM-013 seen on the pairs); AX6 [obs] the class of c.
Machinery: Stone AQ's Minuscule class VERBATIM; Stone AT's numpy enumeration VERBATIM; the AP board block VERBATIM;
Stone AS's W(E7) enumeration VERBATIM; Stone AU's w0(E6) VERBATIM.  scar56_data.json and _stone_ap_cache/witnesses_ap.json
READ-ONLY (declared dependencies).  Own cache _stone_ax_cache/witnesses_ax.json.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_ax_c_equals_t.py
"""
import os, sys, time, json, hashlib, itertools, math
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ax_c_equals_t.log", "w", encoding="utf-8")
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
W_CAP = 400000

say("=" * 78); say("STONE AX -- C = T: THE REVERSER AS A CONSTRAINT ON THE GRAMMAR"); say("=" * 78)
BRIEF = "BRIEF_STONE_AX_C_EQUALS_T.md"; LOCK = open("BRIEF_STONE_AX_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AX0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AX_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- the AQ machine, VERBATIM
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices")
end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
note("Minuscule machine loaded verbatim from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16]))
# ---------------------------------------------------------------- Stone AT's numpy enumeration, VERBATIM
def enumerate_W_np(M):
    N = M.N; gens = [np.array(s, dtype=np.uint8) for s in M.S]
    ident = np.arange(N, dtype=np.uint8); seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
    while len(frontier):
        cand = np.concatenate([frontier[:, g] for g in gens], axis=0); keep = []
        for row in cand:
            b = row.tobytes()
            if b not in seen: seen.add(b); keep.append(row)
        frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, N), dtype=np.uint8)
        if len(frontier): layers.append(frontier)
    return np.concatenate(layers, axis=0), seen
# ---------------------------------------------------------------- Stone AU's helpers, VERBATIM
def diagram_aut(fam, n):
    if fam == "A": return {i: n - 1 - i for i in range(n)}
    if fam == "D": return {**{i: i for i in range(n - 2)}, n - 2: n - 1, n - 1: n - 2}
    if fam == "E" and n == 6: return {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
    return {i: i for i in range(n)}
def tcomp(p, q): return tuple(p[q[i]] for i in range(len(p)))
def tinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def tpow(p, e):
    x = tuple(range(len(p)))
    for _ in range(e): x = tcomp(p, x)
    return x

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
banner("AX1 -- reversers = w0 . C_W(R) on the family;  AX2 -- the automorphism the reverser induces")
TABLE = []; ok1 = True; bad1 = []; ok2 = True; bad2 = []; okc = True; badc = []; oka = True; bada = []
obs_antipode = []
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); r = n; h = coxeter_number(fam, n); Wn = weyl_order(fam, n)
    minus_in_W = (fam == "D" and n % 2 == 0) or (fam == "E" and n == 7)
    sig = diagram_aut(fam, n) if not minus_in_W else {i: i for i in range(r)}; inv_sig = {v: u for u, v in sig.items()}
    w0 = tuple(M.idx[tuple(-w[inv_sig[j]] for j in range(r))] for w in M.W)
    R = tuple(M.R); Rinv = tinv(R)
    # AX2: conjugation by w0 on the simple reflections
    induced = [M.S.index(tcomp(tcomp(w0, M.S[i]), w0)) if tcomp(tcomp(w0, M.S[i]), w0) in M.S else None for i in range(r)]
    sigma_ok = induced == [sig[i] for i in range(r)]
    central = all(tcomp(w0, s) == tcomp(s, w0) for s in M.S)
    ok2 &= sigma_ok; okc &= (central == minus_in_W)
    if not sigma_ok: bad2.append((fam, n, k, induced))
    if central != minus_in_W: badc.append((fam, n, k, central))
    # antipode
    lam = M.W[M.top]; selfdual = tuple(-x for x in lam) in M.idx
    IO = tuple(M.idx[tuple(-x for x in w)] for w in M.W) if selfdual else None
    anti_is_w0 = (IO == w0) if selfdual else None
    if selfdual:
        if anti_is_w0 != minus_in_W: oka = False; bada.append((fam, n, k, anti_is_w0))
        if not minus_in_W:
            obs_antipode.append((fam, n, k, tcomp(tcomp(IO, R), IO) == Rinv, M.isometry(list(IO))))
    # AX1: counts
    if Wn <= W_CAP:
        G, Wb = enumerate_W_np(M); assert len(G) == Wn
        Ra = np.array(R, dtype=np.uint8); Ria = np.array(Rinv, dtype=np.uint8)
        rev = np.all(G[:, Ra] == Ria[G], axis=1); cen = np.all(G[:, Ra] == Ra[G], axis=1)
        nrev, ncen = int(rev.sum()), int(cen.sum())
        w0_in = np.array(w0, dtype=np.uint8).tobytes() in Wb
        w0rev = tcomp(tcomp(w0, R), w0) == Rinv
        good = (nrev == ncen) and w0_in and w0rev and (not selfdual or ((np.array(IO, dtype=np.uint8).tobytes() in Wb) == minus_in_W))
        ok1 &= good
        if not good: bad1.append((fam, n, k, nrev, ncen))
        TABLE.append([fam, n, k, Wn, h, nrev, ncen, minus_in_W, central, sigma_ok, selfdual, anti_is_w0])
        tick("%s%d w%d: |W| = %d, h = %d; reversers %d, |C_W(R)| = %d; central %s; sigma %s" % (fam, n, k, Wn, h, nrev, ncen, central, [sig[i] for i in range(r)]))
    else:
        w0_in = M.isometry(list(w0)); w0rev = tcomp(tcomp(w0, R), w0) == Rinv
        ok1 &= (w0_in and w0rev)
        TABLE.append([fam, n, k, Wn, h, "cited", "cited", minus_in_W, central, sigma_ok, selfdual, anti_is_w0])
        tick("%s%d w%d: |W| = %d > cap (counts cited from SM-058/059); w0 in W by isometry %s, reverses %s; central %s; sigma %s" % (fam, n, k, Wn, w0_in, w0rev, central, [sig[i] for i in range(r)]))
check("AX1", "on the 38 boards with |W| <= 400,000 the number of reversers of R in W equals |C_W(R)|, w0 among them; on the 4 large boards w0 in W and reverses (counts cited)", ok1, bad1)
n_unique = sum(1 for t in TABLE if t[5] == 1)
n_enum = sum(1 for t in TABLE if t[5] != "cited")
note("[C] the reverser is unique on %d of the %d enumerated boards (those with C_W(R) = 1) -- plus E7 (SM-059 AU5), re-measured below" % (n_unique, n_enum))
note("[note] the brief wrote '38 boards' and 'four large boards (D8 x3, E7)': a slip of the auditor -- D8 is not in the family and only E7 exceeds the cap; %d boards enumerated, 1 cited" % n_enum)
check("AX2a", "on all 42 boards w0 s_i w0 = s_sigma(i) for every simple reflection, sigma the diagram automorphism (identity where -1 in W)", ok2, bad2)
check("AX2b", "w0 is central in W exactly on the 10 boards where -1 in W (D4, D6, D8 x3, E7)", okc and sum(1 for t in TABLE if t[8]) == 10, badc or sum(1 for t in TABLE if t[8]))
# post-reveal (added after the first sealed run, kept as _FIRSTRUN.log): the brief's "10" counted D8, which is not among the 42 boards
# (the family is A2..A7, D4..D7, E6, E7); the boards with -1 in W are D4 x3, D6 x3, E7 = 7.  AX2b stays FAIL as written.
central_boards = [f"{t[0]}{t[1]} w{t[2]}" for t in TABLE if t[8]]
check("AX2b-b (post-reveal)", "w0 is central in W exactly on the 7 boards of the family where -1 in W (D4 w1/w3/w4, D6 w1/w5/w6, E7 w7) and nowhere else", okc and len(central_boards) == 7, central_boards)
check("AX2c", "on every self-dual board the reverser w0 equals the antipode of the weights exactly when -1 in W", oka, bada)
note("[obs, beyond the brief] self-dual boards with -1 NOT in W (antipode a permutation of the weights but not w0): (board, antipode reverses R, antipode in W by isometry) = %s" % [(f"{a}{b} w{c}", d, e) for a, b, c, d, e in obs_antipode])
note("[obs, beyond the brief] on those five boards the antipode is an isometry of the weight configuration (trivially) but NOT in W: the isometry criterion equals W-membership only where Aut of the configuration is W itself -- true on E7 (SM-054 [P]) and wherever -1 in W or the board is not self-dual; the sealed stones AQ/AR/AU use the criterion on E7 alone (checked: every other board was enumerated), so nothing sealed depends on it")
tick("family done")

# ---------------------------------------------------------------- the 56-board, AP block VERBATIM
AP = "verify_stone_ap_clock_centralizer.py"; apsrc = open(AP, encoding="utf-8").read(); fence = "# " + "=" * 69
blk = apsrc.split(fence)[2]; blk = blk[blk.index("\n") + 1:]; exec(compile(blk, AP, "exec"))
note("board block loaded verbatim from %s (sha256 %s); scar56_data.json sha256 %s" % (AP, hashlib.sha256(apsrc.encode("utf-8")).hexdigest()[:16], hashlib.sha256(open("scar56_data.json", "rb").read()).hexdigest()[:16]))
PR = D["PR"]
def comp(p, q): return [p[q[k]] for k in range(56)]
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def islin(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
def cyc(p):
    seen_ = set(); c = []
    for a in range(56):
        if a in seen_: continue
        x = a; L = 0
        while x not in seen_: seen_.add(x); L += 1; x = p[x]
        c.append(L)
    return sorted(c, reverse=True)
def ctype(p): return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(cyc(p)).items(), reverse=True))
def porder(p):
    x = list(range(56)); n_ = 0
    while True:
        x = comp(p, x); n_ += 1
        if x == list(range(56)): return n_
def fixed(p): return sum(1 for k in range(56) if p[k] == k)
def closure(gens, cap=2000):
    gens = [tuple(g) for g in gens]; e = tuple(range(56)); seen = {e}; frontier = [e]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = tuple(s[g[i]] for i in range(56))
                if h not in seen:
                    seen.add(h); nxt.append(h)
                    if len(seen) > cap: return None
        frontier = nxt
    return seen
NORM7 = sum(sum(a * a for a in W2[k]) for k in range(56))
def trace7(p): return Fraction(7 * sum(sum(a * b for a, b in zip(W2[p[k]], W2[k])) for k in range(56)), NORM7)
# Stone AU's sheet coordinates and w0(E6), VERBATIM
labels = {k: tuple(verts[k]) for k in range(56)}
C7inv = [[Fraction(x) for x in row] for row in np.linalg.inv(np.array(C7, dtype=float)).round(6).tolist()]
def cow6(k): return sum(C7inv[6][j] * labels[k][j] for j in range(7))
sheet = {k: cow6(k) for k in range(56)}; poles = [k for k in range(56) if abs(sheet[k]) == Fraction(3, 2)]
sig6 = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
by_sheet = {}
for k in range(56): by_sheet.setdefault(sheet[k], {})[labels[k][:6]] = k
w0e6 = [k if k in poles else by_sheet[sheet[k]][tuple(-labels[k][:6][sig6[j]] for j in range(6))] for k in range(56)]

banner("AX2 on the 56 -- iota central; w0(E6) induces sigma_6 on the E6 reflections; GUESS: it moves the seventh")
S7l = [list(s) for s in S7]
iota_central = all(comp(IOTA, s) == comp(s, IOTA) for s in S7l)
ind6 = []
for i in range(6):
    c_ = comp(comp(w0e6, S7l[i]), w0e6); ind6.append(S7l.index(c_) if c_ in S7l else None)
seventh_commutes = comp(w0e6, S7l[6]) == comp(S7l[6], w0e6)
c7 = comp(comp(w0e6, S7l[6]), w0e6)
check("AX2d", "on the 56: iota s_i iota = s_i for all seven simple reflections (iota central, SM-013)", iota_central)
check("AX2e", "w0(E6) s_i w0(E6) = s_sigma6(i) for the six E6 nodes (sigma6: 0<->5, 2<->4)", ind6 == [sig6[i] for i in range(6)], ind6)
check("AX2f", "REGISTERED GUESS: w0(E6) does NOT commute with the seventh reflection s_6", not seventh_commutes,
      "w0(E6) s_6 w0(E6) is %s (moves %d points; s_6 moves the poles: %s)" % ("a simple reflection" if c7 in S7l else "not a simple reflection", 56 - fixed(c7), [S7l[6][p] for p in poles]))
note("[obs] w0(E6) s_6 w0(E6) is a reflection of W(E7)? linear %s, cycle type %s, trace on the seven %s" % (islin(c7), ctype(c7), trace7(c7)))

# ---------------------------------------------------------------- Stone AS's enumeration of W(E7) on the 56, VERBATIM
banner("AX3 -- the bridge copy's normaliser in W(E7): REGISTERED GUESS 2 x PGL(2,7)")
wit = json.load(open(os.path.join("_stone_ap_cache", "witnesses_ap.json")))
a, b = wit["bridge_pair_a"], wit["bridge_pair_b"]
Pset = closure([a, b], cap=400)
fp_by_order = {}
for g in Pset: fp_by_order.setdefault(porder(list(g)), set()).add(fixed(list(g)))
check("AX3a", "the cached bridge pair generates a group of order 168 with fixed points 56/8/2/0/0 by element order 1/2/3/4/7 (SM-054 AP4 re-seen)",
      len(Pset) == 168 and fp_by_order == {1: {56}, 2: {8}, 3: {2}, 4: {0}, 7: {0}}, fp_by_order)
gens = [np.array(s, dtype=np.uint8) for s in S7]
ident = np.arange(56, dtype=np.uint8)
seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
while len(frontier):
    cand = np.concatenate([frontier[:, g] for g in gens], axis=0)   # (g o s)(x) = g[s[x]]  -> rows frontier[:, s]
    keep = []
    for row in cand:
        b_ = row.tobytes()
        if b_ not in seen: seen.add(b_); keep.append(row)
    frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, 56), dtype=np.uint8)
    if len(frontier): layers.append(frontier)
G = np.concatenate(layers, axis=0); NW = len(G); del layers
check("AX3b", "W(E7) enumerated on the 56: 2,903,040 elements (SM-057 AS1)", NW == 2903040, NW)
tick("W(E7) enumerated")
# vectorised conjugation with exact verification
rng = np.random.default_rng(20260910); RV = rng.integers(1, 2**40, size=56, dtype=np.int64)   # 56 * 255 * 2^40 < 2^63: no overflow
def hrows(A): return (A.astype(np.int64) * RV[None, :]).sum(axis=1)
Ph = np.array(sorted(set(int(x) for x in hrows(np.array(sorted(Pset), dtype=np.uint8)))), dtype=np.int64)
Pbytes = {np.array(g, dtype=np.uint8).tobytes() for g in Pset}
aA = np.array(a, dtype=np.uint8); bA = np.array(b, dtype=np.uint8)
Nmask = np.zeros(NW, dtype=bool); Cmask = np.zeros(NW, dtype=bool); CH = 400000
for i in range(0, NW, CH):
    B = G[i:i + CH]; Binv = np.empty_like(B); np.put_along_axis(Binv, B, np.broadcast_to(ident, B.shape), axis=1)
    ca = np.take_along_axis(B[:, aA], Binv, axis=1); cb = np.take_along_axis(B[:, bA], Binv, axis=1)   # g a g^-1, g b g^-1
    Nmask[i:i + CH] = np.isin(hrows(ca), Ph) & np.isin(hrows(cb), Ph)
    Cmask[i:i + CH] = np.all(ca == aA[None, :], axis=1) & np.all(cb == bA[None, :], axis=1)
    del B, Binv, ca, cb
Ncand = [tuple(int(x) for x in G[j]) for j in np.nonzero(Nmask)[0]]
def conj(g, x): return tuple(g[x[pinv(list(g))[i]]] for i in range(56))
Nset = {g for g in Ncand if np.array(conj(g, a), dtype=np.uint8).tobytes() in Pbytes and np.array(conj(g, b), dtype=np.uint8).tobytes() in Pbytes}   # exact
Cset = {tuple(int(x) for x in G[j]) for j in np.nonzero(Cmask)[0]}
tick("normaliser and centraliser found: candidates %d, exact |N| = %d, |C| = %d" % (len(Ncand), len(Nset), len(Cset)))
IOTA_t = tuple(IOTA); ID_t = tuple(range(56))
PC = {tuple(p[c_[i]] for i in range(56)) for p in Pset for c_ in Cset}
outer = sorted(Nset - PC, key=lambda g: (porder(list(g)), -fixed(list(g))))
guess3 = (len(Cset) == 2 and Cset == {ID_t, IOTA_t} and len(Nset) == 672 and len(outer) == 336)
check("AX3c", "REGISTERED GUESS: C_W(E7)(P) = <iota> (order 2), |N_W(E7)(P)| = 672, N/C = PGL(2,7): the outer automorphism is realised by Weyl elements",
      guess3, "|C| = %d, |N| = %d, |N \\ P.C| = %d, C = %s" % (len(Cset), len(Nset), len(outer), sorted(ctype(list(g)) for g in Cset)))
if not guess3: say("  [INVERTED] recorded at equal prominence: |C| = %d (types %s), |N| = %d, image order |N|/|C| = %s" % (len(Cset), Counter(ctype(list(g)) for g in Cset), len(Nset), Fraction(len(Nset), len(Cset))))
# identify an outer element and verify it swaps the two 7-classes
a7 = next(g for g in Pset if porder(list(g)) == 7); cls7 = {conj(p, a7) for p in Pset}
if outer:
    c = list(outer[0])
    is_outer = tuple(conj(tuple(c), a7)) not in cls7
    check("AX3d", "a chosen normalising element c outside P.C carries a 7-element to the OTHER 7-class (the outer automorphism, Ilya's C on PSL(2,7))",
          is_outer, "c: order %d, cycle type %s, fixed %d" % (porder(c), ctype(c), fixed(c)))
    inv_types = Counter(ctype(list(g)) for g in outer if porder(list(g)) == 2)
    check("AX3e", "the outer coset contains involutions of type 2^24 1^8 (8 fixed points; the guess from x -> 1/x on the projective line)",
          "2^24 1^8" in inv_types, dict(inv_types))
else:
    c = None; check("AX3d", "an outer element exists", False, "none: the normaliser induces only inner automorphisms")

banner("AX4 -- C != T on the grammar")
check("AX4a", "iota commutes with every element of P (induces the identity automorphism on the flavour group)", all(comp(IOTA, list(g)) == comp(list(g), IOTA) for g in Pset))
if c is not None:
    PSIl = list(PSI); PSIinv = pinv(PSIl); cPc = comp(comp(c, PSIl), pinv(c))
    keptF = sum(1 for x in range(56) if cPc[x] == PSIl[x]); keptB = sum(1 for x in range(56) if cPc[x] == PSIinv[x])
    check("AX4b", "c is not iota, c is linear, c does not commute with Psi (SM-054) and does not reverse Psi (SM-059): the flavour C and the board's T are different elements",
          c != list(IOTA) and islin(c) and cPc != PSIl and cPc != PSIinv, "#{x: cPsic^-1 x = Psi x} = %d, #{x: = Psi^-1 x} = %d" % (keptF, keptB))
    o1 = closure([a, b, c], cap=1000); o2 = closure([a, b, c, IOTA], cap=2000)
    check("AX4c", "|<P, c>| = 336 (PGL(2,7)) and |<P, c, iota>| = 672", o1 is not None and len(o1) == 336 and o2 is not None and len(o2) == 672,
          (len(o1) if o1 else ">1000", len(o2) if o2 else ">2000"))
    same = all(g in Nset for g in o2) if o2 else False
    note("[C] <P, c, iota> equals N: %s" % (o2 is not None and set(o2) == Nset))
    # the reverser of Psi inside N: only iota (AU5 re-measured over N)
    revN = [g for g in Nset if comp(comp(list(g), PSIl), pinv(list(g))) == PSIinv]; cenN = [g for g in Nset if comp(list(g), PSIl) == comp(PSIl, list(g))]
    check("AX4d", "inside N the only reverser of Psi is iota and the only element commuting with Psi is 1 (SM-059 AU5, SM-054 AP3 re-measured on the 672)",
          revN == [IOTA_t] and cenN == [ID_t], (len(revN), len(cenN)))
# E7 reversers over all of W, re-measured in the 56 coordinates
PSI_A = np.array(PSI, dtype=np.uint8); PSIi_A = np.array(pinv(list(PSI)), dtype=np.uint8)
nrevW = 0; ncenW = 0
for i in range(0, NW, CH):
    B = G[i:i + CH]; nrevW += int(np.all(B[:, PSI_A] == PSIi_A[B], axis=1).sum()); ncenW += int(np.all(B[:, PSI_A] == PSI_A[B], axis=1).sum())
check("AX1-E7", "on the 56 the number of reversers of Psi in W(E7) is 1 (= |C_W(Psi)| = 1): the coset statement on the large board, re-measured", nrevW == 1 and ncenW == 1, (nrevW, ncenW))

banner("AX5 -- what C has to act on: the pairs")
pairs = sorted({frozenset((k, IOTA[k])) for k in range(56)}); pidx = {p: i for i, p in enumerate(pairs)}
def block_perm(p): return [pidx[frozenset(p[k] for k in pairs[i])] for i in range(28)]
fp28 = {}
for g in Pset: fp28.setdefault(porder(list(g)), set()).add(sum(1 for i in range(28) if block_perm(list(g))[i] == i))
check("AX5a", "P acts on the 28 iota-pairs with fixed points 28/4/1/0/0 by element order 1/2/3/4/7 (transitive, SM-013)", fp28 == {1: {28}, 2: {4}, 3: {1}, 4: {0}, 7: {0}}, fp28)
# PSL(2,7) character table, classes 1A 2A 3A 4A 7A 7B, sizes 1 21 56 42 24 24
alpha = complex(-0.5, math.sqrt(7) / 2)
CT = {"chi1": [1, 1, 1, 1, 1, 1], "chi3": [3, -1, 0, 1, alpha, alpha.conjugate()], "chi3bar": [3, -1, 0, 1, alpha.conjugate(), alpha],
      "chi6": [6, 2, 0, 0, -1, -1], "chi7": [7, -1, 1, -1, 0, 0], "chi8": [8, 0, -1, 0, 1, 1]}
SIZES = [1, 21, 56, 42, 24, 24]
census = Counter(porder(list(g)) for g in Pset)
pi28 = [28, 4, 1, 0, 0, 0]
mult = {nm: sum(SIZES[i] * pi28[i] * CT[nm][i].conjugate() if isinstance(CT[nm][i], complex) else SIZES[i] * pi28[i] * CT[nm][i] for i in range(6)) / 168 for nm in CT}
mult = {nm: (round(v.real, 9) if isinstance(v, complex) else v) for nm, v in mult.items()}
check("AX5b", "the permutation character on the pairs decomposes as chi1 + 2 chi6 + chi7 + chi8 -- no chi3, no chi3bar (SM-013's erratum seen on the pairs); census 1/21/56/42/48",
      mult == {"chi1": 1, "chi3": 0, "chi3bar": 0, "chi6": 2, "chi7": 1, "chi8": 1} and census == Counter({1: 1, 2: 21, 3: 56, 4: 42, 7: 48}), (mult, dict(census)))
check("AX5c", "iota is fixed-point-free of type 2^28 (swaps every pair) and c permutes the pairs (c normalises <iota>)", ctype(list(IOTA)) == "2^28" and (c is None or all(pidx.get(frozenset(c[k] for k in pairs[i])) is not None for i in range(28))))

banner("AX6 [obs] -- the class of c in W(E7)")
if c is not None:
    from sympy import Matrix, Rational
    cols = []; used = []
    for k in range(56):
        v = Matrix([Rational(x) for x in W2[k]])
        if Matrix.hstack(*(cols + [v])).rank() > len(cols): cols.append(v); used.append(k)
        if len(cols) == 7: break
    Bm = Matrix.hstack(*cols); Bg = Matrix.hstack(*[Matrix([Rational(x) for x in W2[c[k]]]) for k in used])
    A = Bg * (Bm.T * Bm).inv() * Bm.T
    assert (A * Bm - Bg).is_zero_matrix; detc = A.det()
    tr7 = trace7(c)
    note("c: order %d, cycle type %s, fixed points %d, trace on the seven %s, det on the seven %s (%s), linear %s" % (porder(c), ctype(c), fixed(c), tr7, detc, "in W+ = Sp6(2)" if detc == 1 else "in the iota-coset", islin(c)))
    note("outer coset: element orders %s; cycle types of its involutions %s" % (dict(Counter(porder(list(g)) for g in outer)), dict(Counter(ctype(list(g)) for g in outer if porder(list(g)) == 2))))
    ic = comp(IOTA, c)
    note("iota.c: order %d, cycle type %s, trace %s" % (porder(ic), ctype(ic), trace7(ic)))

os.makedirs("_stone_ax_cache", exist_ok=True)
json.dump({"brief_sha": sha, "ap_witness_sha256": hashlib.sha256(open(os.path.join("_stone_ap_cache", "witnesses_ap.json"), "rb").read()).hexdigest(),
           "scar56_sha256": hashlib.sha256(open("scar56_data.json", "rb").read()).hexdigest(),
           "family_table": TABLE, "N_order": len(Nset), "C_order": len(Cset), "C_types": sorted(ctype(list(g)) for g in Cset),
           "c": c, "w0e6": w0e6, "results": RESULTS}, open(os.path.join("_stone_ax_cache", "witnesses_ax.json"), "w"), indent=1, default=str)
banner("VERDICT")
npass = sum(1 for _, ok in RESULTS if ok); nfail = len(RESULTS) - npass
say("RESULT: %d checks passed, %d failed" % (npass, nfail))
for tag, ok in RESULTS:
    if not ok: say("  FAILED: %s" % tag)
tick("done")
