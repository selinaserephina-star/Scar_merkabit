# -*- coding: utf-8 -*-
r"""verify_stone_at_grammar_family.py -- STONE AT: THE SHARED GRAMMAR ACROSS THE MINUSCULE FAMILY

Brief: BRIEF_STONE_AT_GRAMMAR_FAMILY.md (lock BRIEF_STONE_AT_LOCK.sha256, re-verified as AT0);
amendment AMENDMENT_STONE_AT_2026-09-09.md (lock AMENDMENT_STONE_AT_LOCK.sha256, re-verified as AT0b).

For every one of SM-055's 42 minuscule cases and every k = 1..h-1: I_k = {g in W : R^-k g R^k in W} (the grammar two
instants share) and C_k = C_W(R^k).  AT1 C_k ⊆ I_k [P]; AT2 REGISTERED GUESS I_k = C_k as sets everywhere; AT3 REGISTERED
predicted table of the common order; AT4 the antipode (as written; amended AT4b); AT5 [obs] named survivors.

Machinery: Minuscule class of verify_stone_aq_rush_shi_defect.py VERBATIM; numpy BFS enumeration of W for every case;
membership by row-bytes set (|W| <= 400,000) or by the isometry mask (E7, [P] as in Stones AP/AS).
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_at_grammar_family.py
"""
import itertools, json, os, sys, time, hashlib, math
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_at_grammar_family.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AT -- THE SHARED GRAMMAR ACROSS THE MINUSCULE FAMILY (I_k against C_W(R^k))"); say("=" * 78)
BRIEF = "BRIEF_STONE_AT_GRAMMAR_FAMILY.md"; LOCK = open("BRIEF_STONE_AT_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AT0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AT_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
AMEND = "AMENDMENT_STONE_AT_2026-09-09.md"; ALOCK = open("AMENDMENT_STONE_AT_LOCK.sha256").read().strip()
asha = hashlib.sha256(open(AMEND, "rb").read()).hexdigest()
check("AT0b", "the amendment is sha-locked before the run: sha256(%s) equals AMENDMENT_STONE_AT_LOCK.sha256" % AMEND, asha == ALOCK, asha[:16] + "...")

# ---------------------------------------------------------------- the AQ machine, VERBATIM
AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices")
end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
note("Minuscule machine loaded verbatim from %s (sha256 %s)" % (AQ, hashlib.sha256(aqsrc.encode("utf-8")).hexdigest()[:16]))

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
def typemat(M):
    vals = sorted({M.IP[a][b] for a in range(M.N) for b in range(M.N)}); code = {v: i for i, v in enumerate(vals)}
    T = np.zeros((M.N, M.N), dtype=np.int8)
    for a in range(M.N):
        for b in range(M.N): T[a, b] = code[M.IP[a][b]]
    return T
def iso_mask(H, T, chunk=16384):
    out = np.zeros(len(H), dtype=bool)
    for i in range(0, len(H), chunk):
        B = H[i:i + chunk]; out[i:i + chunk] = np.all(T[B[:, :, None], B[:, None, :]] == T[None, :, :], axis=(1, 2))
    return out
def pow_arr(p, k):
    x = np.arange(len(p), dtype=np.uint8)
    for _ in range(k): x = p[x]
    return x
def inv_arr(p):
    r = np.empty_like(p); r[p] = np.arange(len(p), dtype=np.uint8); return r
def cyc(p):
    seen_ = set(); c = []
    for a in range(len(p)):
        if a in seen_: continue
        x = a; L = 0
        while x not in seen_: seen_.add(x); L += 1; x = int(p[x])
        c.append(L)
    return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(c).items(), reverse=True))

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6), ("E", 7, 7)]
def predicted(fam, n, k, h, kk, Wn, chain, vector):
    if chain: return Wn
    if vector: return Wn if kk == n - 1 else 2
    if h % 2 == 1: return 1
    if kk != h // 2: return 1
    minus_in_W = (fam == "D" and n % 2 == 0) or (fam == "E" and n == 7)
    return 2 if minus_in_W else 1

TABLE = []; ok1 = True; ok2 = True; ok3 = True; bad2 = []; bad3 = []; named = []
EQ = {}; HALF = {}; MODELS = {}; MEMB = {}   # post-reveal bookkeeping (added after the first sealed run; see AT2b/AT2c/AT3c)
at4_as_written = []; at4b = []
banner("the computation, case by case")
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); N = M.N; h = coxeter_number(fam, n)
    G, Wbytes = enumerate_W_np(M); Wn = len(G)
    assert Wn == weyl_order(fam, n), (fam, n, k, Wn)
    R = np.array(M.R, dtype=np.uint8)
    vector = (fam == "D" and (k == 1 or (n == 4 and k in (3, 4)))) or (fam, n, k) == ("A", 3, 2)
    big = Wn > W_CAP; T = typemat(M) if big else None
    IOTA = None
    lam = M.W[M.top]; neg = tuple(-x for x in lam)
    if neg in M.idx:   # self-dual: the antipode is a permutation of the weights
        IOTA = np.array([M.idx[tuple(-x for x in w)] for w in M.W], dtype=np.uint8)
    sizes = {}; sizesC = {}
    for kk in range(1, h):
        Pk = pow_arr(R, kk); Pki = inv_arr(Pk)
        H = Pki[G[:, Pk]]                                   # R^-k g R^k
        Cmask = np.all(G[:, Pk] == Pk[G], axis=1)           # g R^k = R^k g
        if big:
            pre = np.all(H[:, IOTA] == IOTA[H], axis=1)     # necessary (iota central in W(E7))
            idx = np.nonzero(pre)[0]; Imask = np.zeros(Wn, dtype=bool); Imask[idx] = iso_mask(H[idx], T) if len(idx) else False
        else:
            Imask = np.fromiter((row.tobytes() in Wbytes for row in H), dtype=bool, count=Wn)
        nI, nC = int(Imask.sum()), int(Cmask.sum()); sizes[kk] = nI; sizesC[kk] = nC
        EQ.setdefault((fam, n, k), {})[kk] = bool(np.array_equal(Imask, Cmask))
        if h % 2 == 0 and kk == h // 2: HALF[(fam, n, k)] = G[np.nonzero(Imask)[0]]
        if not np.all(Cmask <= Imask): ok1 = False
        if not np.array_equal(Imask, Cmask): ok2 = False; bad2.append((fam, n, k, kk, nI, nC))
        pred = predicted(fam, n, k, h, kk, Wn, M.chain, vector)
        if nI != pred: ok3 = False; bad3.append((fam, n, k, kk, nI, pred))
        if 1 < nI < Wn:
            els = G[np.nonzero(Imask)[0]]
            desc = []
            for g in els:
                if np.array_equal(g, np.arange(N, dtype=np.uint8)): continue
                ispow = next((j for j in range(1, h) if np.array_equal(g, pow_arr(R, j))), None)
                isanti = IOTA is not None and np.array_equal(g, IOTA)
                central = all(np.array_equal(g[np.array(s)], np.array(s, dtype=np.uint8)[g]) for s in M.S)   # first run: tuple used as a fancy index (instrumentation), log kept
                desc.append((cyc(g), ispow, isanti, central))
            named.append(((fam, n, k), kk, desc))
    # AT4 as written / AT4b
    minus_in_W = (IOTA is not None) and (IOTA.tobytes() in Wbytes if not big else bool(iso_mask(IOTA[None, :], T)[0]))
    if IOTA is not None:
        conj = IOTA[R[IOTA]]; anti_ok = np.array_equal(conj, inv_arr(R))
    else:
        anti_ok = None
    at4_as_written.append(((fam, n, k), minus_in_W, IOTA is not None, anti_ok))
    TABLE.append(dict(fam=fam, n=n, k=k, N=N, h=h, W=Wn, chain=M.chain, vector=vector, sizes=sizes, sizesC=sizesC, minus_in_W=minus_in_W, selfdual=IOTA is not None))
    MODELS[(fam, n, k)] = M; MEMB[(fam, n, k)] = (None if big else Wbytes, T)
    tick("%s%d w%d: |W| = %d, h = %d; |I_k| = %s" % (fam, n, k, Wn, h, [sizes[kk] for kk in range(1, h)]))

banner("AT1 -- C_W(R^k) ⊆ I_k everywhere; |C_1| agrees with SM-055")
c1 = {(r["fam"], r["n"], r["k"]): r["sizesC"][1] for r in TABLE}
exp1 = {key: (v["W"] if v["chain"] else (2 if v["vector"] else 1)) for key, v in ((k_, r) for k_, r in zip(c1.keys(), TABLE))}
check("AT1", "C_W(R^k) ⊆ I_k for every case and k; |C_W(R)| = |W| on chains, 2 on the D_n vector representations, 1 elsewhere (SM-055)",
      ok1 and all(c1[key] == exp1[key] for key in c1), [(key, c1[key], exp1[key]) for key in c1 if c1[key] != exp1[key]])
banner("AT2 -- REGISTERED GUESS: I_k = C_W(R^k) as sets, every case, every k")
check("AT2", "I_k equals C_W(R^k) as a set for all 42 cases and all k = 1..h-1 (E7: k = 1..17 on the full enumeration)", ok2, bad2[:12])
if not ok2: say("  [INVERTED] recorded at equal prominence.")
banner("AT3 -- REGISTERED GUESS: the predicted table")
check("AT3", "|I_k| as predicted: |W| on chains; on D_n vectors |W| at k = n-1 and 2 elsewhere; otherwise 1 except 2 at k = h/2 when -1 in W", ok3, bad3[:12])
if not ok3: say("  [INVERTED] recorded at equal prominence.")
e7 = next(r for r in TABLE if r["fam"] == "E" and r["n"] == 7)
check("AT3b", "E7: SM-057's intersections re-derived (1 for k != 9, 2 at k = 9)", all(e7["sizes"][kk] == (2 if kk == 9 else 1) for kk in range(1, 18)), e7["sizes"])
banner("AT2b/AT2c/AT3c -- POST-REVEAL, labelled (after the sealed run showed the guess true exactly where no power of R is linear)")
rich = [key for key in EQ if not MODELS[key].chain and not any(v == TABLE[[ (r["fam"], r["n"], r["k"]) for r in TABLE].index(key)]["W"] for v in TABLE[[ (r["fam"], r["n"], r["k"]) for r in TABLE].index(key)]["sizes"].values())]
eq_rich = {key: all(EQ[key].values()) for key in rich}
exceptions = [key for key, v in eq_rich.items() if not v]
check("AT2b", "POST-REVEAL: I_k = C_W(R^k) for every k in every case where no power of R is a Weyl element, EXCEPT the D5 half-spins "
      "(the 12 chains and the 7 vector-representation cases have a linear power and I_k ⊋ C_W(R^k) there)",
      all(v for key, v in eq_rich.items() if key not in (("D", 5, 4), ("D", 5, 5))) and set(exceptions) == {("D", 5, 4), ("D", 5, 5)}
      and all(not all(EQ[key].values()) for key in EQ if key not in rich),
      "rich cases %d, exceptions %s" % (len(rich), exceptions))
def diagram_aut(fam, n):
    if fam == "A": return {i: n - 1 - i for i in range(n)}
    if fam == "D": return {**{i: i for i in range(n - 2)}, n - 2: n - 1, n - 1: n - 2}
    if fam == "E" and n == 6: return {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
    return {i: i for i in range(n)}
w0rows = []
for key, M in MODELS.items():
    fam, n, k = key; h = coxeter_number(fam, n)
    minus_in_W = (fam == "D" and n % 2 == 0) or (fam == "E" and n == 7) or (fam == "A" and n == 1)
    sig = diagram_aut(fam, n) if not minus_in_W else {i: i for i in range(n)}
    w0 = np.array([M.idx[tuple(-w[i] for i in range(n)) if minus_in_W else tuple(-w[{v: u for u, v in sig.items()}[j]] for j in range(n))] for w in M.W], dtype=np.uint8) if False else None
    # w0 acts on weights as -sigma: (w0 w)_j = -w_{sigma^-1(j)}; for minus_in_W sigma = id
    inv_sig = {v: u for u, v in sig.items()}
    w0 = np.array([M.idx[tuple(-w[inv_sig[j]] for j in range(n))] for w in M.W], dtype=np.uint8)
    R = np.array(M.R, dtype=np.uint8); Rinv = inv_arr(R)
    Wb, T = MEMB[key]
    inW = (w0.tobytes() in Wb) if Wb is not None else bool(iso_mask(w0[None, :], T)[0])
    top_to_bottom = int(w0[M.top]) == M.bottom
    reverses = np.array_equal(w0[R[w0]], Rinv)
    half = None
    if h % 2 == 0:
        Rm = pow_arr(R, h // 2); commutes = np.array_equal(w0[Rm], Rm[w0])
        S = HALF[key]; half = (len(S) == 2 and any(np.array_equal(g, w0) for g in S))
    else:
        commutes = None
    w0rows.append((key, inW, top_to_bottom, reverses, commutes, half))
check("AT2c", "POST-REVEAL: in every case the longest element w0 (acting as -sigma, sigma the diagram automorphism when -1 is not in W) lies in W, "
      "sends the top to the bottom, and REVERSES rowmotion: w0 R w0 = R^-1; hence w0 commutes with R^(h/2) whenever h is even",
      all(inW and t2b and rev and (c is None or c) for (_, inW, t2b, rev, c, _) in w0rows), [key for (key, inW, t2b, rev, c, _) in w0rows if not (inW and t2b and rev and (c is None or c))])
rich_even = [key for key in rich if coxeter_number(key[0], key[1]) % 2 == 0 and key not in (("D", 5, 4), ("D", 5, 5), ("D", 6, 5), ("D", 6, 6))]
check("AT2d", "POST-REVEAL: on every rich board with h even except the D5 and D6 half-spins, the half-turn survivors are exactly {1, w0} "
      "(E7's iota generalizes to the longest element); D6 half-spins: 4 survivors including w0 = -1; D5 half-spins: 8 survivors including w0",
      all(half for (key, _, _, _, _, half) in w0rows if key in rich_even)
      and all(len(HALF[key]) == 4 and any(np.array_equal(g, np.array([MODELS[key].idx[tuple(-x for x in w)] for w in MODELS[key].W], dtype=np.uint8)) for g in HALF[key]) for key in (("D", 6, 5), ("D", 6, 6)))
      and all(len(HALF[key]) == 8 for key in (("D", 5, 4), ("D", 5, 5))),
      "rich even cases with {1, w0}: %d" % sum(1 for (key, _, _, _, _, half) in w0rows if key in rich_even and half))
note("[obs] AT3c: on the D_n vector representations |I_k| depends on gcd(k, n-1): D5 (n-1 = 4): gcd 1 -> 8, 2 -> 32, 4 -> |W|; D6 (5): gcd 1 -> 10, 5 -> |W|; "
     "D7 (6): gcd 1 -> 12, 2 -> 72, 3 -> 384, 6 -> |W|; D4 (3): gcd 1 -> 6, 3 -> |W|; while |C_W(R^k)| there is 2 at gcd 1 and grows with the gcd (2, 8/10/12, 16, 32/72/384, ...)")
banner("AT4 -- the antipode, as written in the brief, and as amended")
as_written_ok = all((minus or not perm) for (_, minus, perm, _) in at4_as_written)   # brief: -1 not in W  =>  antipode not a permutation
check("AT4", "AS WRITTEN: on boards with -1 not in W the antipode is not a permutation of the weights",
      as_written_ok, [key for (key, minus, perm, _) in at4_as_written if perm and not minus])
selfdual_pred = {key: ((key[0] == "A" and 2 * key[2] == key[1] + 1) or (key[0] == "D" and (key[2] == 1 or key[1] % 2 == 0)) or (key[0] == "E" and key[1] == 7)) for (key, _, _, _) in at4_as_written}
check("AT4b", "AMENDED: the antipode is a permutation iff lambda is self-dual (A_n omega_{(n+1)/2}; D_n omega_1; D_n half-spins n even; E7); whenever it is, "
      "iota R iota = R^-1; and it lies in W iff -1 in W (D_n n even, E7)",
      all(perm == selfdual_pred[key] for (key, _, perm, _) in at4_as_written) and all(anti for (_, _, perm, anti) in at4_as_written if perm)
      and all(minus == ((key[0] == "D" and key[1] % 2 == 0) or key[0] == "E" and key[1] == 7) for (key, minus, _, _) in at4_as_written),
      [(key, minus, perm, anti) for (key, minus, perm, anti) in at4_as_written if perm])
banner("AT5 -- [obs] the non-trivial proper survivors, named")
for key, kk, desc in named:
    note("%s%d w%d, k = %d: %s" % (key[0], key[1], key[2], kk, desc))
json.dump({"brief_sha": sha, "amend_sha": asha, "table": TABLE, "named": [[list(k_), kk, d] for k_, kk, d in named]}, open(os.path.join("_stone_at_cache", "table_at.json"), "w"), indent=1, default=str)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
