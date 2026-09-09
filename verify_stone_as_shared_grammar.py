# -*- coding: utf-8 -*-
r"""verify_stone_as_shared_grammar.py -- STONE AS: THE SHARED GRAMMAR -- how much symmetry survives k ticks

Brief: BRIEF_STONE_AS_SHARED_GRAMMAR.md (lock BRIEF_STONE_AS_LOCK.sha256, re-verified as check AS0).

W = W(E7) on the 56 states is the board's grammar; the clock Psi is not in it and commutes with nothing in it.
After k ticks the grammar is W_k = Psi^k W Psi^-k.  This stone computes W ∩ W_k EXACTLY for k = 1..9 (and 17) by
enumerating all 2,903,040 elements of W and testing each conjugate for linearity (= W-membership, [P]); and it
settles what the clock and the mirror generate with W.

BARS: AS0 lock; AS1 the enumeration (2,903,040, all linear; 63 reflections one class; iota in W; Psi, pr not);
AS2 <W,Psi> = A56, |<W,pr>| = 2^28 |Sp6(2)|, <W,Psi,pr> = S56; AS3 pr = w.t (t = the pole swap), <W,pr> = the
sign-flip group 2^28 : Sp6(2); AS4 REGISTERED GUESS: W ∩ W_k = {1} for k != 9 and {1, iota} for k = 9;
AS5 no reflection survives any tick; AS6 no bridge-copy involution survives any tick; AS7 [obs] near-survivors.

Machinery: board block VERBATIM from verify_stone_ap_clock_centralizer.py; numpy BFS enumeration; vectorized tests;
sympy Schreier-Sims.  scar56_data.json READ-ONLY.  Own cache _stone_as_cache/witnesses_as.json.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes.  Not RH/GRH.  Rule 3.
Run:  python -X utf8 verify_stone_as_shared_grammar.py
"""
import itertools, json, os, sys, time, hashlib, math
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_as_shared_grammar.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE AS -- THE SHARED GRAMMAR (W(E7) against its clock-conjugates)"); say("=" * 78)
BRIEF = "BRIEF_STONE_AS_SHARED_GRAMMAR.md"; LOCK = open("BRIEF_STONE_AS_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("AS0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_AS_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")

# ---------------------------------------------------------------- the board, VERBATIM (loaded from the sealed AP verifier)
AP = "verify_stone_ap_clock_centralizer.py"; apsrc = open(AP, encoding="utf-8").read()
fence = "# " + "=" * 69
blk = apsrc.split(fence)[2]; blk = blk[blk.index("\n") + 1:]
exec(compile(blk, AP, "exec"))
note("board block loaded verbatim from %s (sha256 %s)" % (AP, hashlib.sha256(apsrc.encode("utf-8")).hexdigest()[:16]))
PR = D["PR"]
TYPEMAT = np.full((56, 56), -1, dtype=np.int8)
for k, l in PAIRS:
    t = {"P": 0, "S": 1, "v": 2}[ptype(k, l)]; TYPEMAT[k, l] = t; TYPEMAT[l, k] = t
def compose(p, q): return [p[q[k]] for k in range(56)]
def pinv(p):
    r = [0] * 56
    for i, x in enumerate(p): r[x] = i
    return r
def ppow(p, e):
    x = list(range(56))
    for _ in range(e): x = compose(p, x)
    return x
def islinear(p): return all(ptype(p[k], p[l]) == ptype(k, l) for k, l in PAIRS)
def linear_mask(H, chunk=16384):
    """H: (m,56) uint8 array of permutations -> boolean mask of those preserving every pair type."""
    out = np.zeros(len(H), dtype=bool)
    for i in range(0, len(H), chunk):
        B = H[i:i + chunk]
        TB = TYPEMAT[B[:, :, None], B[:, None, :]]
        out[i:i + chunk] = np.all(TB == TYPEMAT[None, :, :], axis=(1, 2))
    return out
IOTA_A = np.array(IOTA, dtype=np.uint8); PSI_A = np.array(PSI, dtype=np.uint8)

# ---------------------------------------------------------------- AS1 enumerate W
banner("AS1 -- enumerating W(E7) on the 56 by breadth-first closure")
gens = [np.array(s, dtype=np.uint8) for s in S7]
ident = np.arange(56, dtype=np.uint8)
seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
while len(frontier):
    cand = np.concatenate([frontier[:, g] for g in gens], axis=0)   # (g o s)(x) = g[s[x]]  -> rows frontier[:, s]
    keep = []
    for row in cand:
        b = row.tobytes()
        if b not in seen: seen.add(b); keep.append(row)
    frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, 56), dtype=np.uint8)
    if len(frontier): layers.append(frontier)
    tick("layer %d: %d new, %d total" % (len(layers) - 1, len(frontier), len(seen)))
G = np.concatenate(layers, axis=0); NW = len(G)
check("AS1a", "W has exactly 2,903,040 elements on the 56", NW == 2903040, NW)
lin_all = linear_mask(G)
check("AS1b", "every element of W preserves every pair type (the isometry criterion is consistent)", bool(lin_all.all()), int(lin_all.sum()))
refls = set(tuple(int(x) for x in s) for s in S7); changed = True
while changed:
    changed = False
    for r in list(refls):
        for g in S7:
            c = tuple(compose(compose(list(g), list(r)), pinv(list(g))))
            if c not in refls: refls.add(c); changed = True
check("AS1c", "the 63 reflections form one W-class; iota in W; Psi and pr not in W",
      len(refls) == 63 and islinear(IOTA) and not islinear(PSI) and not islinear(PR), len(refls))
tick("AS1 done")

# ---------------------------------------------------------------- AS2 / AS3 the generated groups
banner("AS2/AS3 -- what the clock and the mirror generate with W; the mirror as a Weyl element times a pair flip")
from sympy.combinatorics import Permutation, PermutationGroup
Wg = [Permutation(list(s)) for s in S7]
def sign(p):
    seen_ = set(); s = 0
    for a in range(56):
        if a in seen_: continue
        x = a; L = 0
        while x not in seen_: seen_.add(x); L += 1; x = p[x]
        s += L - 1
    return (-1) ** s
GW = PermutationGroup(Wg); G1 = PermutationGroup(Wg + [Permutation(list(PSI))]); G2 = PermutationGroup(Wg + [Permutation(list(PR))]); G3 = PermutationGroup(Wg + [Permutation(list(PSI)), Permutation(list(PR))])
o1, o2, o3 = G1.order(), G2.order(), G3.order()
check("AS2a", "Psi, iota and the reflections are even; <W, Psi> = A56 (order 56!/2)",
      sign(PSI) == 1 and sign(IOTA) == 1 and sign(S7[0]) == 1 and o1 == math.factorial(56) // 2)
check("AS2b", "|<W, pr>| = 2^28 * |Sp6(2)| = 2^37 * 3^4 * 5 * 7", o2 == 2 ** 28 * 1451520, o2)
check("AS2c", "pr is odd and <W, Psi, pr> = S56", sign(PR) == -1 and o3 == math.factorial(56))
tick("generated groups done")
poles = [k for k in range(56) if PR[k] == k]
t = list(range(56)); t[poles[0]], t[poles[1]] = poles[1], poles[0]
w = compose(PR, t)
pairs = sorted({frozenset((k, IOTA[k])) for k in range(56)}); pidx = {p: i for i, p in enumerate(pairs)}
def block_perm(p): return [pidx[frozenset(p[k] for k in pairs[i])] for i in range(28)]
Wblock = PermutationGroup([Permutation(block_perm(list(s))) for s in S7])
orbit1 = Wblock.orbit(0)
flips_in = all(G2.contains(Permutation([ (IOTA[k] if k in pr_ else k) for k in range(56)])) for pr_ in [set(p) for p in pairs])
check("AS3a", "pr fixes exactly the two poles, which form an iota-pair; w = pr o (pole swap) is a Weyl element (SM-016's nu(pr) = 2 re-seen)",
      len(poles) == 2 and IOTA[poles[0]] == poles[1] and islinear(w) and not islinear(PR))
check("AS3b", "W is transitive on the 28 iota-pairs, its image there has order |Sp6(2)| = 1,451,520 (kernel <iota>); every single pair-flip lies in <W, pr>",
      len(orbit1) == 28 and Wblock.order() == 1451520 and flips_in, "|image| = %d" % Wblock.order())
check("AS3c", "hence <W, pr> = (2^28 pair-flips) . W with (2^28) ∩ W = <iota>: order 2^28 * |W| / 2, as measured",
      o2 == 2 ** 28 * NW // 2)
tick("AS3 done")

# ---------------------------------------------------------------- AS4 the intersections
banner("AS4 -- REGISTERED GUESS: W ∩ Psi^k W Psi^-k = {1} for k != 9, {1, iota} for k = 9")
IOTA_bytes = IOTA_A.tobytes(); ID_bytes = ident.tobytes()
inter = {}; near = {}
for k in list(range(1, 10)) + [17]:
    Pk = np.array(ppow(PSI, k), dtype=np.uint8); Pki = np.array(pinv(list(Pk)), dtype=np.uint8)
    H = Pki[G[:, Pk]]                                      # h = Psi^-k o g o Psi^k
    comm = np.all(H[:, IOTA_A] == IOTA_A[H], axis=1)       # cheap necessary test: h commutes with iota
    idx = np.nonzero(comm)[0]; near[k] = int(len(idx))
    lin = linear_mask(H[idx]) if len(idx) else np.zeros(0, dtype=bool)
    surv = idx[lin]
    inter[k] = sorted(G[i].tobytes() for i in surv)
    names = ["1" if b == ID_bytes else ("iota" if b == IOTA_bytes else "other") for b in inter[k]]
    tick("k = %2d: near-survivors %8d, survivors %d  %s" % (k, near[k], len(surv), Counter(names)))
ok4 = all(inter[k] == [ID_bytes] for k in range(1, 9)) and inter[9] == sorted([ID_bytes, IOTA_bytes])
check("AS4", "REGISTERED GUESS: |W ∩ W_k| = 1 for k = 1..8 and W ∩ W_9 = {1, iota}", ok4, {k: len(v) for k, v in inter.items()})
if not ok4: say("  [INVERTED] recorded at equal prominence: %s" % {k: Counter("1" if b == ID_bytes else ("iota" if b == IOTA_bytes else "other") for b in v) for k, v in inter.items()})
check("AS4b", "k and 18-k give intersections of equal order (checked k = 1, 17)", len(inter[1]) == len(inter[17]))

# ---------------------------------------------------------------- AS5 reflections, AS6 markers
banner("AS5/AS6 -- the reflections and the bridge copy's involutions under every tick")
R_list = [list(r) for r in refls]
surv5 = {k: sum(1 for r in R_list if islinear(compose(compose(ppow(PSI, k), r), pinv(ppow(PSI, k))))) for k in range(1, 18)}
check("AS5", "no reflection of W is linear after conjugation by Psi^k, k = 1..17", all(v == 0 for v in surv5.values()), surv5)
wit = json.load(open(os.path.join("_stone_ap_cache", "witnesses_ap.json")))
a0, b0 = wit["bridge_pair_a"], wit["bridge_pair_b"]
def closure(gs, cap=200):
    e = list(range(56)); seen_ = {tuple(e)}; fr = [e]
    while fr:
        nxt = []
        for g in fr:
            for s in gs:
                h = compose(s, g); th = tuple(h)
                if th not in seen_:
                    seen_.add(th); nxt.append(h)
                    if len(seen_) > cap: return None
        fr = nxt
    return [list(x) for x in seen_]
Hb = closure([a0, b0]); invs = [h for h in Hb if h != list(range(56)) and compose(h, h) == list(range(56))]
surv6 = {k: sum(1 for z in invs if islinear(compose(compose(ppow(PSI, k), z), pinv(ppow(PSI, k))))) for k in range(1, 18)}
check("AS6", "the bridge copy has order 168 with 21 involutions, and none is linear after conjugation by Psi^k, k = 1..17",
      len(Hb) == 168 and len(invs) == 21 and all(v == 0 for v in surv6.values()), surv6)
note("[obs] AS7 near-survivor profile (elements of W whose Psi^k-conjugate still commutes with iota): %s" % near)

json.dump({"brief_sha": sha, "W_order": NW, "orders": {"W,Psi": str(o1), "W,pr": str(o2), "W,Psi,pr": str(o3)}, "poles": poles,
           "intersections": {k: len(v) for k, v in inter.items()}, "near": near, "refl_survivors": surv5, "marker_survivors": surv6},
          open(os.path.join("_stone_as_cache", "witnesses_as.json"), "w"), indent=1)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED: " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
