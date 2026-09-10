# -*- coding: utf-8 -*-
r"""verify_stone_az_doubled_clock.py -- STONE AZ: THE DOUBLED CLOCK -- the vector boards' shared grammar is C_W(R^{2k})

Brief: BRIEF_STONE_AZ_DOUBLED_CLOCK.md (lock BRIEF_STONE_AZ_LOCK.sha256, re-verified as AZ0).
Lemma C: an involution centralizing W and reversing R gives I_k <= C_W(R^{2k}).  Lemma D: on the D_n vector boards
equality, since the transport commutes with the antipode (so lies in W(B_n)) and has even sign (so lies in W(D_n)).
Lemma E: a transport can change the signed cycle type only by trading two negative j-cycles for one positive 2j-cycle.
AZ1 Lemma C on eleven boards; AZ2 Lemma D on D_3..D_7; AZ3 Lemma E and the inner/non-inner counts (REGISTERED);
AZ4 D_3 by hand; AZ5 the inner half (REGISTERED); AZ6 [obs] the groups; AZ7 [obs] one line.

Machinery: Stone AV's e-coordinate board machine VERBATIM + a four-line vector-board builder (new, printed);
Stone AQ's Minuscule and Stone AT's numpy BFS VERBATIM. Membership by row bytes only.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_az_doubled_clock.py
"""
import itertools, json, os, sys, time, hashlib, inspect
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_az_doubled_clock.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AZ -- THE DOUBLED CLOCK (the vector boards' shared grammar is the centralizer of R^{2k})"); say("=" * 78)
BRIEF = "BRIEF_STONE_AZ_DOUBLED_CLOCK.md"; LOCK = open("BRIEF_STONE_AZ_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AZ0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AZ_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
CACHE["brief_sha"] = sha

# ---------------------------------------------------------------- Stone AV's e-coordinate board machine, VERBATIM
AV = "verify_stone_av_d5_anomaly.py"; avsrc = open(AV, encoding="utf-8").read()
s0 = avsrc.index("# ---------------------------------------------------------------- e-coordinate board machine")
s1 = avsrc.index("W5, idx5, S5, R5, P5, leq5 = D_half(5)")
exec(compile(avsrc[s0:s1], AV, "exec"))
note("board machine loaded verbatim from %s (sha256 %s)" % (AV, hashlib.sha256(avsrc.encode("utf-8")).hexdigest()[:16]))
# ---------------------------------------------------------------- the one new machine: the D_n vector board in e-coordinates
def D_vec(n):  # weights +-e_i; roots e_i - e_{i+1}, e_{n-1} + e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [tuple(x + y for x, y in zip(e(n - 2, n), e(n - 1, n)))]
    w = [e(i, n) for i in range(n)] + [tuple(-x for x in e(i, n)) for i in range(n)]
    return board(w, roots)
note("new machine (four lines):\n" + inspect.getsource(D_vec))
# ---------------------------------------------------------------- Stone AQ's Minuscule and Stone AT's BFS, VERBATIM
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
AT = "verify_stone_at_grammar_family.py"; atsrc = open(AT, encoding="utf-8").read()
a0 = atsrc.index("def enumerate_W_np(M):"); a1 = atsrc.index("def cyc(p):")
exec(compile(atsrc[a0:a1], AT, "exec"))
note("Minuscule from %s (sha256 %s); BFS from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16], AT, hashlib.sha256(atsrc.encode("utf-8")).hexdigest()[:16]))
class Shim:  # what enumerate_W_np needs from a board built in e-coordinates
    def __init__(self, N, S): self.N, self.S = N, S
def perm_sign(p):
    """sign of a permutation given as an array"""
    seen = np.zeros(len(p), dtype=bool); cycles = 0
    for a in range(len(p)):
        if seen[a]: continue
        cycles += 1; x = a
        while not seen[x]: seen[x] = True; x = int(p[x])
    return 1 if (len(p) - cycles) % 2 == 0 else -1
def commutes(G, x): return np.all(G[:, x] == x[G], axis=1)
def member_mask(Hrows, Wbytes): return np.fromiter((row.tobytes() in Wbytes for row in Hrows), dtype=bool, count=len(Hrows))

banner("AZ1 -- Lemma C: I_k <= C_W(R^{2k}) wherever an involution centralizes W and reverses R")
BOARDS_C = [("A", 3, 2), ("A", 5, 3), ("A", 7, 4), ("D", 4, 1), ("D", 4, 3), ("D", 4, 4), ("D", 5, 1), ("D", 6, 1), ("D", 6, 5), ("D", 6, 6), ("D", 7, 1)]
okC = True; rowsC = []
for fam, n, k in BOARDS_C:
    M = Minuscule(fam, n, k); N = M.N; G, Wbytes = enumerate_W_np(M); Wn = len(G); R = np.array(M.R, dtype=np.uint8); h = coxeter_number(fam, n)
    lam = M.W[M.top]; assert tuple(-x for x in lam) in M.idx, "not self-dual"
    IOTA = np.array([M.idx[tuple(-x for x in w)] for w in M.W], dtype=np.uint8)
    iota_in_W = IOTA.tobytes() in Wbytes
    central = bool(np.all(G[:, IOTA] == IOTA[G])); reverses = bool(np.array_equal(IOTA[R[IOTA]], inv_arr(R)))
    incl = True; sizes = []
    for kk in range(1, h):
        Pk = pow_arr(R, kk); Pki = inv_arr(Pk); Imask = member_mask(Pki[G[:, Pk]], Wbytes); C2 = commutes(G, pow_arr(R, 2 * kk))
        incl &= bool(np.all(Imask <= C2)); sizes.append((int(Imask.sum()), int(C2.sum())))
    okC &= central and reverses and incl
    rowsC.append(dict(board="%s%d w%d" % (fam, n, k), W=Wn, iota_in_W=iota_in_W, central=central, reverses=reverses, inclusion=incl, sizes=sizes))
    note("%s%d w%d |W|=%6d: antipode in W %-5s centralizes W %-5s reverses R %-5s  I_k <= C_W(R^2k) at every lag: %s  (|I_k|,|C_2k|): %s" % (fam, n, k, Wn, iota_in_W, central, reverses, incl, sizes))
    tick("%s%d w%d done" % (fam, n, k))
W4, idx4, S4, R4, P4, leq4 = B_spin(4); WB4 = closure(S4)
G4 = np.array(sorted(WB4), dtype=np.uint8); Wb4 = {r.tobytes() for r in G4}; R4a = np.array(R4, dtype=np.uint8)
IOTA4 = np.array([idx4[tuple(-x for x in w)] for w in W4], dtype=np.uint8)
c4 = bool(np.all(G4[:, IOTA4] == IOTA4[G4])); r4 = bool(np.array_equal(IOTA4[R4a[IOTA4]], inv_arr(R4a))); incl4 = True; s4 = []
for kk in range(1, 8):
    Pk = pow_arr(R4a, kk); Pki = inv_arr(Pk); Imask = member_mask(Pki[G4[:, Pk]], Wb4); C2 = commutes(G4, pow_arr(R4a, 2 * kk)); incl4 &= bool(np.all(Imask <= C2)); s4.append((int(Imask.sum()), int(C2.sum())))
okC &= c4 and r4 and incl4
note("B4 spinor |W|=384: antipode in W True centralizes W %s reverses R %s  inclusion %s  (|I_k|,|C_2k|): %s" % (c4, r4, incl4, s4))
check("AZ1", "on the eleven boards with a W-central reverser (ten of the 42 + the B4 spinor) the antipode centralizes W, reverses R, and I_k <= C_W(R^{2k}) at every lag", okC)
CACHE["lemmaC"] = rowsC + [dict(board="B4 spinor", central=c4, reverses=r4, inclusion=incl4, sizes=s4)]

banner("AZ2 -- Lemma D: on the D_n vector boards I_k = C_W(R^{2k}) as sets (n = 3..7)")
TAB = {(r["fam"], r["n"], r["k"]): r for r in json.load(open("_stone_at_cache/table_at.json", encoding="utf-8"))["table"]}
VEC = {}
okD = True; okTab = True
for n in range(3, 8):
    Wl, idx, S, R, P, leq = D_vec(n); N = 2 * n; G, Wbytes = enumerate_W_np(Shim(N, S)); Wn = len(G); Ra = np.array(R, dtype=np.uint8); h = 2 * n - 2
    assert Wn == 2 ** (n - 1) * np.math.factorial(n) if hasattr(np, "math") else True
    IOTA = np.array([idx[tuple(-x for x in w)] for w in Wl], dtype=np.uint8)
    assert bool(np.all(G[:, IOTA] == IOTA[G])) and np.array_equal(IOTA[Ra[IOTA]], inv_arr(Ra))
    ei = [idx[e(i, n)] for i in range(n)]; mei = [idx[tuple(-x for x in e(i, n))] for i in range(n)]
    pos = {}
    for i in range(n): pos[ei[i]] = (i, 1); pos[mei[i]] = (i, -1)
    def signed(g, ei=ei, pos=pos, n=n):   # first run: late-bound closure read the last board's coordinates (instrumentation), FIRSTRUN log kept
        """signed cycle type of a Weyl element given as a permutation of the 2n weights"""
        sig = {};
        for i in range(n):
            j, s = pos[int(g[ei[i]])]; sig[i] = (j, s)
        seen = set(); typ = []
        for i in range(n):
            if i in seen: continue
            L = 0; sgn = 1; x = i
            while x not in seen: seen.add(x); L += 1; j, s = sig[x]; sgn *= s; x = j
            typ.append((L, sgn))
        return tuple(sorted(typ, reverse=True))
    key = ("A", 3, 2) if n == 3 else ("D", n, 1); row = TAB[key]
    per = {}
    for kk in range(1, h):
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Hm = Pki[G[:, Pk]]; Imask = member_mask(Hm, Wbytes); C2 = commutes(G, pow_arr(Ra, 2 * kk)); Ck = commutes(G, Pk)
        eq = bool(np.array_equal(Imask, C2)); okD &= eq
        okTab &= (int(Imask.sum()) == row["sizes"][str(kk)] and int(Ck.sum()) == row["sizesC"][str(kk)])
        idxC = np.nonzero(C2)[0]; sample = idxC if len(idxC) <= 2000 else idxC[np.linspace(0, len(idxC) - 1, 2000).astype(int)]
        inB = bool(np.all(np.all(Hm[sample][:, IOTA] == IOTA[Hm[sample]], axis=1))); even = all(perm_sign(Hm[i]) == 1 for i in sample)
        per[kk] = dict(nI=int(Imask.sum()), nC=int(Ck.sum()), nC2=int(C2.sum()), equal=eq, transport_in_pairing_stabilizer=inB, transport_even=even, sampled=(len(sample) < len(idxC)))
        okD &= inB and even
    VEC[n] = dict(Wl=Wl, idx=idx, G=G, Wbytes=Wbytes, R=Ra, h=h, IOTA=IOTA, signed=signed, per=per, N=N)
    note("D%d vector (N=%d, |W|=%d, h=%d): " % (n, N, Wn, h) + "; ".join("k=%d |I|=%d |C_k|=%d |C_2k|=%d %s" % (kk, v["nI"], v["nC"], v["nC2"], "=" if v["equal"] else "!=") for kk, v in per.items()))
    tick("D%d vector done" % n)
check("AZ2", "on D_3..D_7 (vector boards) I_k = C_W(R^{2k}) as sets at every lag; every transport of C_W(R^{2k}) lies in the pairing stabilizer and is even (sampled where |C| > 2000)", okD)
check("AZ2b", "[P] the orders reproduce SM-058's table (|I_k| and |C_k|) on D_3 = A3w2, D_4, D_5, D_6, D_7", okTab)
CACHE["lemmaD"] = {str(n): VEC[n]["per"] for n in VEC}

banner("AZ3 -- Lemma E: what a transport changes; inner iff same signed type (REGISTERED counts)")
EXPECT_NONINNER = {3: {1: 2, 3: 2}, 5: {1: 4, 3: 4, 5: 4, 7: 4, 2: 18, 6: 18}, 7: {1: 6, 5: 6, 7: 6, 11: 6, 3: 252, 9: 252, 2: 0, 4: 0, 8: 0, 10: 0}, 4: {1: 0, 2: 0, 4: 0, 5: 0}, 6: {k: 0 for k in (1, 2, 3, 4, 6, 7, 8, 9)}}
def trade_ok(tg, th):
    """th - tg is a sum of trades: two negative j-cycles <-> one positive 2j-cycle"""
    cg, ch = Counter(tg), Counter(th); d = {key: ch[key] - cg[key] for key in set(cg) | set(ch)}
    for (L, s), v in d.items():
        if v == 0: continue
        if s == -1:
            if v % 2: return False
            if d.get((2 * L, 1), 0) != -v // 2: return False
        else:
            if L % 2: return False
            if d.get((L // 2, -1), 0) != -2 * v: return False
    return True
okE = True; okCount = True; okIff = True; TRADES = {}; INNER = {}
for n in range(3, 8):
    V = VEC[n]; G, Wbytes, Ra, h, signed, N = V["G"], V["Wbytes"], V["R"], V["h"], V["signed"], V["N"]
    for kk in range(1, h):
        if V["per"][kk]["nI"] == len(G): continue        # the half-turn: R^{h/2} in W, the transport is conjugation by it (SM-056); skipped
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Imask = member_mask(Pki[G[:, Pk]], Wbytes); Ig = G[np.nonzero(Imask)[0]]
        js = Counter(); n_non = 0; inner_set = []; noninner_set = []; iff_ok = True; type_ok = True
        for g in Ig:
            hh = Pki[g[Pk]]; tg, th = signed(g), signed(hh)
            if ctype(tuple(int(x) for x in g)) != ctype(tuple(int(x) for x in hh)) or perm_sign(g) != perm_sign(hh): type_ok = False
            same = (tg == th)
            if not same:
                if not trade_ok(tg, th): type_ok = False
                for (L, s), v in (Counter(th) - Counter(tg)).items():
                    if s == 1: js[L // 2] += 1
                for (L, s), v in (Counter(tg) - Counter(th)).items():
                    if s == 1: js[L // 2] += 1
            inner = bool(np.any(np.all(g[G] == G[:, hh], axis=1)))
            if inner != same: iff_ok = False
            if inner: inner_set.append(g)
            else: noninner_set.append(g); n_non += 1
        okE &= type_ok; okIff &= iff_ok
        exp = EXPECT_NONINNER[n].get(kk); okCount &= (exp is not None and exp == n_non)
        TRADES[(n, kk)] = dict(nI=len(Ig), noninner=n_non, expected=exp, trades_j=dict(js), iff=iff_ok); INNER[(n, kk)] = (inner_set, noninner_set)
        note("D%d k=%2d |I|=%4d: non-inner %4d (Stone AY: %s); types/sign preserved and only trades: %s; inner <=> same signed type: %s; trades by j: %s" % (n, kk, len(Ig), n_non, exp, type_ok, iff_ok, dict(js)))
    tick("D%d transports classified" % n)
check("AZ3a", "[Lemma E] every transport keeps the unsigned cycle type and the sign, and changes the signed type only by trades (two negative j-cycles <-> one positive 2j-cycle)", okE)
check("AZ3b", "REGISTERED: g is W-inner if and only if g and its transport have the same signed cycle type (the split D_n classes never separate them)", okIff)
check("AZ3c", "REGISTERED: the non-inner counts reproduce Stone AY's on every board and lag", okCount, {("D%d" % n, kk): (v["noninner"], v["expected"]) for (n, kk), v in TRADES.items() if v["noninner"] != v["expected"]} or "all")
CACHE["trades"] = {"D%d k=%d" % (n, kk): v for (n, kk), v in TRADES.items()}

banner("AZ4 -- D3 by hand")
V = VEC[3]; Wl, idx, G, Ra = V["Wl"], V["idx"], V["G"], V["R"]
def sp(images, n=3):
    out = []
    for w in Wl:
        v = [None] * n
        for i in range(n):
            j, eps = images.get(i + 1, (i + 1, 1)); v[j - 1] = eps * w[i]
        out.append(idx[tuple(v)])
    return np.array(out, dtype=np.uint8)
ID3 = np.arange(6, dtype=np.uint8); s_minus = sp({1: (2, 1), 2: (1, 1)}); s_plus = sp({1: (2, -1), 2: (1, -1)}); dflip = sp({1: (1, -1), 2: (1 + 1, -1)})
R2 = pow_arr(Ra, 2); Pk = Ra; Pki = inv_arr(Ra)
I1 = {r.tobytes() for r in G[np.nonzero(member_mask(Pki[G[:, Pk]], V["Wbytes"]))[0]]}
tr = lambda g: Pki[g[Pk]]
check("AZ4", "D3: I_1 = {1, s_{e1-e2}, s_{e1+e2}, s_{e1-e2}s_{e1+e2}} = W(D2); R^2 = s_{e1+e2}; the transport swaps the reflection s_{e1-e2} and the double flip and fixes R^2",
      I1 == {ID3.tobytes(), s_minus.tobytes(), s_plus.tobytes(), dflip.tobytes()} and np.array_equal(R2, s_plus) and np.array_equal(tr(s_minus), dflip) and np.array_equal(tr(dflip), s_minus) and np.array_equal(tr(s_plus), s_plus)
      and np.array_equal(dflip, s_minus[s_plus]))

banner("AZ5 -- the inner half (REGISTERED) and the realising pair for n even")
from math import gcd
okHalf = True; okSub = True; okEven = True; SUBS = {}
for n in (3, 5, 7):
    V = VEC[n]; G, Ra, h, signed = V["G"], V["R"], V["h"], V["signed"]
    for kk in range(1, h):
        if gcd(kk, n - 1) != 1: continue
        inner_set, non = INNER[(n, kk)]; nI = len(inner_set) + len(non)
        okHalf &= (2 * len(inner_set) == nI)
        S_ = {tuple(int(x) for x in g) for g in inner_set}; closed = all(tuple(int(x) for x in np.array(a)[np.array(b)]) in S_ for a in S_ for b in S_)
        okSub &= closed
        Ck = G[np.nonzero(commutes(G, pow_arr(Ra, kk)))[0]]; Ck_in = all(tuple(int(x) for x in g) in S_ for g in Ck)
        # candidates: the inner half = elements fixing the pair {e_n, -e_n} pointwise? / = elements whose signed type has no negative 1-cycle? recorded
        fix_en = sum(1 for g in inner_set if g[V["idx"][e(n - 1, n)]] == V["idx"][e(n - 1, n)]); fix_en_non = sum(1 for g in non if g[V["idx"][e(n - 1, n)]] == V["idx"][e(n - 1, n)])
        SUBS[(n, kk)] = dict(nI=nI, inner=len(inner_set), subgroup=closed, contains_Ck=Ck_in, inner_types=sorted(Counter(signed(g) for g in inner_set).items()), noninner_types=sorted(Counter(signed(g) for g in non).items()), inner_fix_en=fix_en, noninner_fix_en=fix_en_non)
        note("D%d k=%d: |I|=%d inner %d (half: %s), inner set a subgroup: %s, contains C_W(R^k): %s; inner signed types %s; non-inner signed types %s; fixing e_n: inner %d / non-inner %d"
             % (n, kk, nI, len(inner_set), 2 * len(inner_set) == nI, closed, Ck_in, SUBS[(n, kk)]["inner_types"], SUBS[(n, kk)]["noninner_types"], fix_en, fix_en_non))
check("AZ5a", "REGISTERED: for n odd at every lag coprime to n-1 exactly half of I_k is W-inner and the inner half is a subgroup", okHalf and okSub, "half: %s, subgroup: %s" % (okHalf, okSub))
PAIRS = {}
for n in (4, 6):
    V = VEC[n]; G, Ra, h = V["G"], V["R"], V["h"]
    for kk in range(1, h):
        if V["per"][kk]["nI"] == len(G) or V["per"][kk]["nI"] == V["per"][kk]["nC"]: continue
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Imask = member_mask(Pki[G[:, Pk]], V["Wbytes"]); Ig = G[np.nonzero(Imask)[0]]
        m = np.ones(len(G), dtype=bool)
        for g in Ig: m &= np.all(g[G] == G[:, Pki[g[Pk]]], axis=1)
        sols = G[np.nonzero(m)[0]]; C2 = commutes(G, pow_arr(Ra, 2 * kk)); inC2 = all(bool(np.all(w[pow_arr(Ra, 2 * kk)] == pow_arr(Ra, 2 * kk)[w])) for w in sols)
        types = [V["signed"](w) for w in sols]; isw0 = [bool(np.array_equal(w, V["IOTA"])) for w in sols]
        okEven &= (len(sols) == 2 and inC2)
        PAIRS[(n, kk)] = dict(nsol=len(sols), in_C2k=inC2, types=types, contains_w0=any(isw0))
        note("D%d k=%d: |I|=%d realising Weyl elements: %d, all in C_W(R^2k): %s, signed types %s, one of them is w0 = -1: %s" % (n, kk, len(Ig), len(sols), inC2, types, any(isw0)))
check("AZ5b", "REGISTERED: for n even every element is inner, realised by exactly two Weyl elements, both in C_W(R^{2k})", okEven)
CACHE["inner_half"] = {"D%d k=%d" % (n, kk): {kk_: (str(v_) if not isinstance(v_, (int, bool)) else v_) for kk_, v_ in d.items()} for (n, kk), d in SUBS.items()}
CACHE["even_pairs"] = {"D%d k=%d" % (n, kk): {kk_: str(v_) for kk_, v_ in d.items()} for (n, kk), d in PAIRS.items()}

banner("POST-REVEAL (labelled, after the first sealed run): AZ5c, AZ5d")
# AZ5c [obs]: at lags coprime to n-1, is I_k = C_W(R^{2k}) dihedral of order 2(n-1) -- a cyclic subgroup <c> of order n-1 and n-1 involutions
# outside it -- with the inner half (n odd) equal to <c> and the transport swapping the two reflection classes?
def order_of(g):
    o = 1; x = g; e_ = tuple(range(len(g)))
    while x != e_: x = comp(g, x); o += 1
    return o
okDih = True; DIH = {}
for n in range(3, 8):
    V = VEC[n]; G, Ra, h, signed = V["G"], V["R"], V["h"], V["signed"]; Wbytes = V["Wbytes"]
    for kk in range(1, h):
        if gcd(kk, n - 1) != 1: continue
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Ig = G[np.nonzero(member_mask(Pki[G[:, Pk]], Wbytes))[0]]
        els = [tuple(int(x) for x in g) for g in Ig]; m = n - 1
        cyc_gens = [g for g in els if order_of(g) == m]
        ok = len(els) == 2 * m and bool(cyc_gens)
        if ok:
            c = cyc_gens[0]; Cc = {c}; x = c
            for _ in range(m - 1): x = comp(c, x); Cc.add(x)
            outside = [g for g in els if g not in Cc]
            ok = len(Cc) == m and all(order_of(g) == 2 for g in outside)
            # the transport on <c> and on the reflections
            tr = {g: tuple(int(x) for x in Pki[np.array(g, dtype=np.uint8)[Pk]]) for g in els}
            cyc_inner = all(tr[g] in Cc for g in Cc)
            # reflection classes of the dihedral group: conjugacy under <c> (two classes when m is even, one when m is odd)
            classes = []
            for g in outside:
                cls = {comp(comp(pinv(y), g), y) for y in Cc}
                if not any(cls == C_ for C_ in classes): classes.append(cls)
            swaps = all(any(tr[g] in C_ and g not in C_ for C_ in classes) for g in outside) if len(classes) == 2 else None
            keeps = all(any(tr[g] in C_ and g in C_ for C_ in classes) for g in outside)
            inner_set = {tuple(int(x) for x in g) for g in INNER[(n, kk)][0]} if (n, kk) in INNER else None
            DIH[(n, kk)] = dict(order=len(els), dihedral=ok, cyclic_part_inner=cyc_inner, reflection_classes=len(classes), transport_swaps_classes=swaps, transport_keeps_classes=keeps, inner_half_is_cyclic=(inner_set == Cc) if inner_set is not None else None, c_type=str(signed(np.array(c, dtype=np.uint8))))
            note("D%d k=%d: |I|=%d dihedral of order 2(n-1): %s; generator c of the cyclic half: %s; transport keeps <c>: %s; reflection classes under <c>: %d; transport swaps them: %s / keeps them: %s; inner half == <c>: %s"
                 % (n, kk, len(els), ok, DIH[(n, kk)]["c_type"], cyc_inner, len(classes), swaps, keeps, DIH[(n, kk)]["inner_half_is_cyclic"]))
        else:
            DIH[(n, kk)] = dict(order=len(els), dihedral=False); note("D%d k=%d: |I|=%d not dihedral of order 2(n-1) as tested" % (n, kk, len(els)))
        okDih &= ok
check("AZ5c", "POST-REVEAL [obs]: at every lag coprime to n-1 (n = 3..7) I_k is dihedral of order 2(n-1); the transport preserves its cyclic half; for n odd it swaps the two reflection classes (an outer automorphism) and the inner half is exactly the cyclic half; for n even there is one reflection class and the transport keeps it",
      okDih and all((d["transport_swaps_classes"] and d["inner_half_is_cyclic"]) if n % 2 else (d["reflection_classes"] == 1 and d["transport_keeps_classes"]) for (n, kk), d in DIH.items()))
# AZ5d [obs]: for n even, the two realising elements named
for n in (4, 6):
    V = VEC[n]; G, Ra, h = V["G"], V["R"], V["h"]
    for kk in range(1, h):
        if (n, kk) not in PAIRS: continue
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Ig = G[np.nonzero(member_mask(Pki[G[:, Pk]], V["Wbytes"]))[0]]
        m = np.ones(len(G), dtype=bool)
        for g in Ig: m &= np.all(g[G] == G[:, Pki[g[Pk]]], axis=1)
        sols = G[np.nonzero(m)[0]]
        names = [signed_perm(tuple(int(x) for x in w), V["Wl"], n) for w in sols]
        refl = [bool(np.array_equal(w[V["IOTA"]], V["IOTA"][w]) and V["signed"](w).count((2, 1)) == 1 and all(L == 1 for (L, s_) in V["signed"](w) if (L, s_) != (2, 1))) for w in sols]
        PAIRS[(n, kk)]["names"] = names
        note("D%d k=%d: the two realising Weyl elements: %s; a reflection among them: %s" % (n, kk, names, refl))
# AZ5c-b: the same with the canonical cyclic half -- the transport-stable one (for n = 3 the Klein group has three index-2 subgroups; only <R^2> = C_W(R) is transport-stable)
okDih2 = True; DIH2 = {}
for n in range(3, 8):
    V = VEC[n]; G, Ra, h = V["G"], V["R"], V["h"]; Wbytes = V["Wbytes"]
    for kk in range(1, h):
        if gcd(kk, n - 1) != 1: continue
        Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Ig = G[np.nonzero(member_mask(Pki[G[:, Pk]], Wbytes))[0]]
        els = [tuple(int(x) for x in g) for g in Ig]; m = n - 1
        tr = {g: tuple(int(x) for x in Pki[np.array(g, dtype=np.uint8)[Pk]]) for g in els}
        best = None
        for c in [g for g in els if order_of(g) == m]:
            Cc = {c}; x = c
            for _ in range(m - 1): x = comp(c, x); Cc.add(x)
            if all(tr[g] in Cc for g in Cc): best = (c, Cc); break
        if best is None: okDih2 = False; DIH2[(n, kk)] = dict(stable_cyclic_half=False); continue
        c, Cc = best; outside = [g for g in els if g not in Cc]
        classes = []
        for g in outside:
            cls = {comp(comp(pinv(y), g), y) for y in Cc}
            if not any(cls == C_ for C_ in classes): classes.append(cls)
        swaps = (len(classes) == 2) and all(any(tr[g] in C_ and g not in C_ for C_ in classes) for g in outside)
        keeps = all(any(tr[g] in C_ and g in C_ for C_ in classes) for g in outside)
        inner_set = {tuple(int(x) for x in g) for g in INNER[(n, kk)][0]}
        Rh2 = tuple(int(x) for x in pow_arr(Ra, h // 2)); c_is_R = (n == 3 and Cc == {tuple(range(6)), Rh2})
        DIH2[(n, kk)] = dict(order=len(els), stable_cyclic_half=True, reflection_classes=len(classes), swaps=swaps, keeps=keeps, inner_half_is_cyclic=(inner_set == Cc), c_type=str(V["signed"](np.array(c, dtype=np.uint8))))
        cond = (swaps and inner_set == Cc) if n % 2 else (len(classes) == 1 and keeps)
        okDih2 &= cond
        note("D%d k=%d: transport-stable cyclic half <c>, c of type %s; reflection classes %d; swaps %s / keeps %s; inner half == <c>: %s%s" % (n, kk, DIH2[(n, kk)]["c_type"], len(classes), swaps, keeps, inner_set == Cc, "  (n = 3: <c> = <R^2> = C_W(R))" if c_is_R else ""))
check("AZ5c-b", "POST-REVEAL [obs] with the transport-stable cyclic half: I_k at coprime lags is dihedral of order 2(n-1); n odd: the transport swaps the two reflection classes and the inner half is the cyclic half; n even: one reflection class, kept", okDih2)
# AZ5d-b [obs]: for n even the realising pair is {R^{h/2}, w0 R^{h/2}} -- by hand: on I_k = C_W(R^{2k}) the transport R^-k g R^k equals conjugation by any odd power
# R^{k(2j+1)}; for n even h/2 = n-1 is odd, so at odd k some odd multiple of k is h/2 mod h and R^{h/2} (a Weyl element, SM-056) does it; w0 = -1 is central.
okPair = True
for (n, kk), d in PAIRS.items():
    V = VEC[n]; Ra, h, IOTA = V["R"], V["h"], V["IOTA"]
    Rh2 = pow_arr(Ra, h // 2); w0Rh2 = IOTA[Rh2]
    Pk = pow_arr(Ra, kk); Pki = inv_arr(Pk); Ig = V["G"][np.nonzero(member_mask(Pki[V["G"][:, Pk]], V["Wbytes"]))[0]]
    m = np.ones(len(V["G"]), dtype=bool)
    for g in Ig: m &= np.all(g[V["G"]] == V["G"][:, Pki[g[Pk]]], axis=1)
    sols = {r.tobytes() for r in V["G"][np.nonzero(m)[0]]}
    ok = sols == {Rh2.tobytes(), w0Rh2.tobytes()}; okPair &= ok
    note("D%d k=%d: realising pair == {R^{h/2}, w0 R^{h/2}}: %s" % (n, kk, ok))
check("AZ5d", "POST-REVEAL [obs]: for n even (D4, D6) the two Weyl elements realising the transport are exactly the half-turn R^{h/2} and w0 R^{h/2} (the transport on C_W(R^{2k}) is conjugation by any odd power of R^k; for n even the half-turn is one and is a Weyl element)", okPair)
CACHE["dihedral_stable"] = {"D%d k=%d" % (n, kk): d for (n, kk), d in DIH2.items()}
CACHE["dihedral"] = {"D%d k=%d" % (n, kk): d for (n, kk), d in DIH.items()}
CACHE["even_pairs"] = {"D%d k=%d" % (n, kk): {kk_: str(v_) for kk_, v_ in d.items()} for (n, kk), d in PAIRS.items()}

banner("AZ6 -- [obs] the groups C_W(R^{2k}) on the vectors")
OBS = {}
for n in range(3, 8):
    V = VEC[n]; G, Ra, h = V["G"], V["R"], V["h"]
    for kk in range(1, h // 2 + 1):
        C2 = G[np.nonzero(commutes(G, pow_arr(Ra, 2 * kk)))[0]]
        if len(C2) > 2000: OBS[(n, kk)] = dict(order=len(C2), note="large"); continue
        els = [tuple(int(x) for x in g) for g in C2]; S_ = set(els)
        ab = all(comp(a, b) == comp(b, a) for a in els for b in els)
        orders = Counter()
        for g in els:
            o = 1; x = g
            while x != tuple(range(len(g))): x = comp(g, x); o += 1
            orders[o] += 1
        OBS[(n, kk)] = dict(order=len(els), abelian=ab, element_orders=dict(orders))
        note("D%d k=%d: C_W(R^2k) order %d, abelian %s, element orders %s" % (n, kk, len(els), ab, dict(orders)))
CACHE["groups"] = {"D%d k=%d" % (n, kk): v for (n, kk), v in OBS.items()}

banner("AZ7 -- [obs], one line")
note("the B3 spinor's lag-3 transports are conjugation by R^3 in W(D4) (SM-060 AV5c, SM-063 AY10d); -1 in W(B3), so Lemma C gives I_3 <= C_W(R^6) = W, vacuous. No computation.")

os.makedirs("_stone_az_cache", exist_ok=True)
json.dump(CACHE, open("_stone_az_cache/witnesses_az.json", "w", encoding="utf-8"), indent=1, default=str)
npass = sum(1 for _, ok in RESULTS if ok); nfail = len(RESULTS) - npass
say("\n" + "=" * 78); say("SUMMARY: %d PASS, %d FAIL of %d checks" % (npass, nfail, len(RESULTS)))
for tag, ok in RESULTS:
    if not ok: say("  FAIL: %s" % tag)
tick("done"); LOG.close()
