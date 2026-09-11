# -*- coding: utf-8 -*-
r"""verify_stone_ba_clifford_hierarchy.py -- STONE BA: THE CLOCK'S CLIFFORD HIERARCHY

Brief: BRIEF_STONE_BA_CLIFFORD_HIERARCHY.md (lock BRIEF_STONE_BA_LOCK.sha256, re-verified as BA0).
The hierarchy at lag k: P_1 = W, P_{j+1} = {g in P_j : R^-k g R^k in P_j}.  Lemma F: P_j is the intersection of the first j
clock-conjugates of W; the core is the largest subgroup of W normalised by R^k.  Lemma G: P_3 = P_2 iff a reverser normalises I_k.
BA1 Lemma F; BA2 Lemma G; BA3 REGISTERED depth <= 2 everywhere except the D5 half-spins at lags 3, 5 (depth 3, trivial core), with
the cores named; BA4 REGISTERED the core is not W-normal, and Core_{<W,R>}(W) on D3, D4, B3; BA5 [obs] tables; BA6 [I] reading.

Machinery: Stone AQ's Minuscule and Stone AT's numpy BFS VERBATIM (41 boards; E7 cited from SM-057, not run);
Stone AV's e-coordinate machine VERBATIM (B3, B4, B5 spinors). Membership by row bytes only.
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED; no registry/git writes. Not RH/GRH. Rule 3.
Run:  python -X utf8 verify_stone_ba_clifford_hierarchy.py
"""
import itertools, json, os, sys, time, hashlib
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_ba_clifford_hierarchy.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE BA -- THE CLOCK'S CLIFFORD HIERARCHY"); say("=" * 78)
BRIEF = "BRIEF_STONE_BA_CLIFFORD_HIERARCHY.md"; LOCK = open("BRIEF_STONE_BA_LOCK.sha256").read().strip()
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("BA0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_BA_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
CACHE["brief_sha"] = sha

AQ = "verify_stone_aq_rush_shi_defect.py"; aqsrc = open(AQ, encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
exec(compile(aqsrc[start:end], AQ, "exec"))
AT = "verify_stone_at_grammar_family.py"; atsrc = open(AT, encoding="utf-8").read()
a0 = atsrc.index("def enumerate_W_np(M):"); a1 = atsrc.index("def cyc(p):")
exec(compile(atsrc[a0:a1], AT, "exec"))
AV = "verify_stone_av_d5_anomaly.py"; avsrc = open(AV, encoding="utf-8").read()
s0 = avsrc.index("# ---------------------------------------------------------------- e-coordinate board machine"); s1 = avsrc.index("W5, idx5, S5, R5, P5, leq5 = D_half(5)")
exec(compile(avsrc[s0:s1], AV, "exec"))
note("Minuscule from %s (%s); BFS from %s (%s); boards from %s (%s)" % (AQ, hashlib.sha256(aqsrc.encode()).hexdigest()[:16], AT, hashlib.sha256(atsrc.encode()).hexdigest()[:16], AV, hashlib.sha256(avsrc.encode()).hexdigest()[:16]))
class Shim:
    def __init__(self, N, S): self.N, self.S = N, S
def member_mask(Hrows, Wbytes): return np.fromiter((row.tobytes() in Wbytes for row in Hrows), dtype=bool, count=len(Hrows))
def commutes(G, x): return np.all(G[:, x] == x[G], axis=1)
def conj_rows(G, Ginv, x):
    """rows g^-1 x g for every g in G"""
    return np.take_along_axis(Ginv, x[G], axis=1)
def bytes_of(rows): return {r.tobytes() for r in rows}
def bfs(gens, N):
    ident = np.arange(N, dtype=np.uint8); seen = {ident.tobytes()}; layers = [ident[None, :]]; frontier = ident[None, :]
    while len(frontier):
        cand = np.concatenate([frontier[:, g] for g in gens], axis=0); keep = []
        for row in cand:
            b = row.tobytes()
            if b not in seen: seen.add(b); keep.append(row)
        frontier = np.array(keep, dtype=np.uint8) if keep else np.zeros((0, N), dtype=np.uint8)
        if len(frontier): layers.append(frontier)
    return np.concatenate(layers, axis=0), seen

CASES = [("A", n, k) for n in range(2, 8) for k in range(1, n + 1)] + [("D", n, k) for n in range(4, 8) for k in (1, n - 1, n)] + [("E", 6, 1), ("E", 6, 6)]
BOARDS = []
for fam, n, k in CASES:
    M = Minuscule(fam, n, k); G, Wbytes = enumerate_W_np(M)
    vector = (fam == "D" and (k == 1 or (n == 4 and k in (3, 4)))) or (fam, n, k) == ("A", 3, 2)
    kind = "chain" if M.chain else ("vector" if vector else ("D5half" if (fam, n) == ("D", 5) and k in (4, 5) else "rich"))
    BOARDS.append(dict(name="%s%d w%d" % (fam, n, k), G=G, Wbytes=Wbytes, R=np.array(M.R, dtype=np.uint8), h=coxeter_number(fam, n), N=M.N, S=[np.array(s, dtype=np.uint8) for s in M.S], kind=kind, W=M.W))
for nn in (3, 4, 5):
    Wl, idx, S, R, P, leq = B_spin(nn); N = 2 ** nn; G, Wbytes = enumerate_W_np(Shim(N, S))
    BOARDS.append(dict(name="B%d spinor" % nn, G=G, Wbytes=Wbytes, R=np.array(R, dtype=np.uint8), h=2 * nn, N=N, S=[np.array(s, dtype=np.uint8) for s in S], kind=("B4" if nn == 4 else ("B3" if nn == 3 else "rich")), W=Wl))
tick("%d boards enumerated" % len(BOARDS))

banner("the hierarchy, board by board (BA1, BA2 checked inline; BA3/BA4 gathered)")
okF = True; okG = True; TABLE = []; CHAINS = {}
for B in BOARDS:
    G, Wbytes, R, h, N, name = B["G"], B["Wbytes"], B["R"], B["h"], B["N"], B["name"]; Wn = len(G)
    Ginv = np.empty_like(G)
    for i in range(Wn): Ginv[i, G[i]] = np.arange(N, dtype=np.uint8)
    Rinv = inv_arr(R)
    rev_mask = np.all(G[:, R] == Rinv[G], axis=1); nrev = int(rev_mask.sum()); r = G[np.nonzero(rev_mask)[0][0]]; rinv = Ginv[np.nonzero(rev_mask)[0][0]]
    nC1 = int(commutes(G, R).sum())
    for kk in range(1, h):
        Pk = pow_arr(R, kk); Pki = inv_arr(Pk)
        m = 1
        x = Pk.copy()
        while not np.array_equal(x, np.arange(N, dtype=np.uint8)): x = Pk[x]; m += 1      # order of R^k
        # the chain by the definition
        levels = [np.ones(Wn, dtype=bool)]; Pb = Wbytes
        while True:
            T = Pki[G[:, Pk]]
            nxt = levels[-1] & member_mask(T, Pb)
            if np.array_equal(nxt, levels[-1]): break
            levels.append(nxt); Pb = bytes_of(G[nxt])
        depth = len(levels); core = levels[-1]
        # Lemma F: partial intersections of the clock-conjugates
        inter = np.ones(Wn, dtype=bool); okF_here = True; Pik = np.arange(N, dtype=np.uint8); Piki = Pik.copy()
        for j in range(1, min(depth, len(levels)) + 1):
            if j > 1:
                Pik = Pk[Pik]; Piki = inv_arr(Pik)
                inter &= member_mask(Piki[G[:, Pik]], Wbytes)
            okF_here &= np.array_equal(inter, levels[j - 1])
        full = np.ones(Wn, dtype=bool); Pik = np.arange(N, dtype=np.uint8)
        for i in range(m):
            if i: Pik = Pk[Pik]
            full &= member_mask(inv_arr(Pik)[G[:, Pik]], Wbytes)
        coreb = bytes_of(G[core]); core_norm = bytes_of(Pki[G[core][:, Pk]]) == coreb
        okF_here &= np.array_equal(full, core) and core_norm
        okF &= okF_here
        # Lemma G
        I = levels[1] if depth >= 2 else levels[0]; Ib = bytes_of(G[I])
        r_norm = bytes_of(rinv[G[I][:, r]]) == Ib
        stops = (depth <= 2)
        okG_here = (stops == r_norm); okG &= okG_here
        nI = int(I.sum()); nC = int(commutes(G, Pk).sum()); nC2 = int(commutes(G, pow_arr(R, 2 * kk)).sum())
        # normality of the core in W
        normal = all(bytes_of(inv_arr(s)[G[core][:, s]]) == coreb for s in B["S"]) if (2 < int(core.sum()) < Wn) else None
        TABLE.append(dict(board=name, kind=B["kind"], k=kk, W=Wn, depth=depth, sizes=[int(l.sum()) for l in levels], nI=nI, nC=nC, nC2=nC2, core=int(core.sum()), core_eq_C2k=bool(np.array_equal(core, commutes(G, pow_arr(R, 2 * kk)))), core_eq_I=bool(np.array_equal(core, I)), core_eq_C=bool(np.array_equal(core, commutes(G, Pk))), r_norm=r_norm, core_normal_in_W=normal, lemmaF=okF_here, lemmaG=okG_here))
        if name in ("B4 spinor", "D5 w4") and kk in (3, 4, 5):   # first run: signed_perm applied to the D5 board's fundamental-weight coordinates (nonsense printout, instrumentation only), FIRSTRUN log kept; D5 now by cycle type
            CHAINS[(name, kk)] = [[(str(signed_perm(tuple(int(x) for x in g), B["W"], 4)) if name == "B4 spinor" else ctype(tuple(int(x) for x in g))) for g in G[l]] for l in levels[1:]]
    B["nrev"] = nrev; B["nC1"] = nC1
    rows = [t for t in TABLE if t["board"] == name]
    note("%-11s |W|=%7d h=%2d reversers %d (|C_W(R)| = %d): depth by lag %s; core sizes %s" % (name, Wn, h, nrev, nC1, [t["depth"] for t in rows], [t["core"] for t in rows]))
    tick(name)
check("BA1", "[Lemma F] on every board and lag the chain equals the run of partial intersections of the clock-conjugates of W, and the core is normalised by R^k and equals the intersection over the whole <R^k>-orbit", okF)
check("BA2", "[Lemma G] on every board and lag, P_3 = P_2 if and only if a reverser in W normalises I_k", okG)
check("BA2b", "[SM-062 re-seen] the reversers number |C_W(R)| on every enumerated board", all(B["nrev"] == B["nC1"] for B in BOARDS))

banner("BA3 -- REGISTERED: depth and cores")
def expected(t):
    if t["nI"] == t["W"]: return 1, "W"
    if t["kind"] == "D5half" and t["k"] in (3, 5): return 3, "1"
    if t["kind"] == "vector": return 2, "C2k"
    return 2, "I"
bad = []
for t in TABLE:
    d, c = expected(t)
    okc = {"W": t["core"] == t["W"], "1": t["core"] == 1, "C2k": t["core_eq_C2k"], "I": t["core_eq_I"]}[c]
    if t["depth"] != d or not okc: bad.append((t["board"], t["k"], t["depth"], d, t["core"], c))
check("BA3", "REGISTERED: depth <= 2 everywhere except the D5 half-spins at lags 3 and 5 (depth 3, trivial core); depth 1 exactly where I_k = W; cores: W on chains, C_W(R^2k) on the vectors, I_k elsewhere (= C_W(R^k) on rich boards; the order-8 I_4 on B4 and the D5 half-spins)",
      not bad, ("all %d (board, lag) pairs" % len(TABLE)) if not bad else "INVERTED: %s" % bad[:12])
d3 = [(t["board"], t["k"], t["sizes"]) for t in TABLE if t["depth"] >= 3]
note("depth-3 chains: %s" % d3)
CACHE["table"] = TABLE

banner("BA4 -- REGISTERED: the core is not W-normal; the core of W in <W,R>")
nn_rows = [t for t in TABLE if t["core_normal_in_W"] is not None]
normal_ones = [(t["board"], t["k"], t["core"]) for t in nn_rows if t["core_normal_in_W"]]
check("BA4a", "REGISTERED: wherever 2 < |core| < |W| the core is not a normal subgroup of W", not normal_ones, ("%d cores tested, none normal" % len(nn_rows)) if not normal_ones else "INVERTED: normal at %s" % normal_ones[:10])
CORES = {}
for name in ("A3 w2", "D4 w1", "B3 spinor"):
    B = next(b for b in BOARDS if b["name"] == name); G, Wbytes, R, N = B["G"], B["Wbytes"], B["R"], B["N"]
    Gbig, _ = bfs(B["S"] + [R], N); nbig = len(Gbig)
    Gbiginv = np.empty_like(Gbig)
    for i in range(nbig): Gbiginv[i, Gbig[i]] = np.arange(N, dtype=np.uint8)
    core_big = [w for w in G if np.all(member_mask(np.take_along_axis(Gbiginv, w[Gbig], axis=1), Wbytes))]
    Pinf1 = next(t for t in TABLE if t["board"] == name and t["k"] == 1)["core"]
    CORES[name] = dict(order_WR=nbig, core_in_WR=len(core_big), P_inf_1=Pinf1)
    note("%s: |<W,R>| = %d; Core_<W,R>(W) has order %d; P_inf(1) has order %d" % (name, nbig, len(core_big), Pinf1))
check("BA4b", "REGISTERED: on the D3 and D4 vector boards the core of W in <W,R> is trivial, hence strictly smaller than P_inf(1); B3 recorded",
      CORES["A3 w2"]["core_in_WR"] == 1 and CORES["D4 w1"]["core_in_WR"] == 1 and CORES["A3 w2"]["P_inf_1"] > 1 and CORES["D4 w1"]["P_inf_1"] > 1, CORES)
CACHE["cores_in_WR"] = CORES

banner("BA5 -- [obs] the 4-cube's and the D5 half-spin's chains, element by element")
for (name, kk), lv in CHAINS.items():
    note("%s lag %d: %s" % (name, kk, " > ".join("{%d: %s}" % (len(l), "; ".join(l)) for l in lv)))
CACHE["chains"] = {"%s k=%d" % (n_, k_): v for (n_, k_), v in CHAINS.items()}
note("the 56 (SM-057, not re-run): I_k = 1 for k != 9 and I_9 = {1, iota} with iota central, so depth 2 everywhere and the core is trivial except {1, iota} at the half-turn.")

banner("BA6 -- [I] the reading, recorded as a reading")
note("the Pauli group of the analogy is the core, the largest subgroup of W the clock normalises. Trivial (or +-1) on every rich board and the 56: the clock is beyond every level. C_W(R^2k) on the vectors, the dihedral I_4 on the 4-cube: there the clock is a level-three gate for that group, and W contains it without normalising it.")

os.makedirs("_stone_ba_cache", exist_ok=True)
json.dump(CACHE, open("_stone_ba_cache/witnesses_ba.json", "w", encoding="utf-8"), indent=1, default=str)
npass = sum(1 for _, ok in RESULTS if ok); nfail = len(RESULTS) - npass
say("\n" + "=" * 78); say("SUMMARY: %d PASS, %d FAIL of %d checks" % (npass, nfail, len(RESULTS)))
for tag, ok in RESULTS:
    if not ok: say("  FAIL: %s" % tag)
tick("done"); LOG.close()
