# -*- coding: utf-8 -*-
r"""verify_stone_bd_halfturn_criterion.py -- STONE BD: THE HALF-TURN CRITERION (why the 4-cube, in one sentence)

Brief: BRIEF_STONE_BD_HALFTURN_CRITERION.md (lock BRIEF_STONE_BD_LOCK.sha256, re-verified as BD0).
Lemma BD-A: c = w^-1 R^m is an involution iff R^m w R^m = w^-1 (for an involution w: iff w commutes with R^m).
Lemma BD-B: if w commutes with R^m then w, c, R^m pairwise commute and, for g in W, any two of {g ~ w, g ~ R^m, g ~ c}
imply the third; with Lemma B (SM-063), I_m cap Stab_W(Fix c) = C_W(c) and its extras are C_W(c) \ C_W(w).
Bars: BD1 B4 (w = -tau in C_4, c^2 = 1, extras = C_W(c) \ C_W(w)); BD2 B8 (w not in C_8, c^2 != 1, GUESS Stab_W(Fix c) = {+-1});
BD3 B3 inside W(B3) (GUESS: nearest w in C_3, c^2 = 1, extras = C_W(c) \ C_W(w)); BD4 B5, B6, B7 (GUESS: no nearest w in C_m,
C_W(c) subset of C_m); BD5 the criterion on six boards (anomaly iff some nearest Weyl element commutes with the half-turn;
BD5b nearest unique up to the antipode); BD6 the lemmas as computations on every nearest w.

Machinery: Stone BC's board machine and affine (pi, v) engine VERBATIM (verify_stone_bc_b8_halfturn.py: board, B_spin,
rebase, all_perm_arrays, is_B_linear, enum_transport, enum_commute, g_arr, mode_count_rows, best_agreement, names);
NEW here: all_nearest (every (pi, v) attaining the best agreement) and enum_stab (the set stabilizer of Y in W).
DISCIPLINE: compute, never assert; registered guesses resolvable INVERTED at equal prominence; no registry/git writes.
Not RH/GRH.  Rule 3.
Run:  python -X utf8 verify_stone_bd_halfturn_criterion.py
"""
import os, sys, time, json, hashlib, itertools
from fractions import Fraction
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_bd_halfturn_criterion.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.write(s + "\n"); LOG.flush()
RESULTS = []
def check(tag, claim, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    say("[%s] %s: %s%s" % ("PASS" if ok else "FAIL", tag, claim, ("  -> " + str(detail)) if detail else ""))
    return bool(ok)
def guess(tag, claim, ok, detail=""):
    r = check(tag, "REGISTERED GUESS: " + claim, ok, detail)
    if not r: say("  [INVERTED] %s -- recorded at equal prominence." % tag)
    return r
def banner(t): say("\n" + "-" * 78); say(t); say("-" * 78)
def note(t): say("  " + t)
def tick(lbl): say("[t=%6.1fs] %s" % (time.time() - T0, lbl))
WIT = {}

say("=" * 78); say("STONE BD -- THE HALF-TURN CRITERION"); say("=" * 78)
BRIEF = "BRIEF_STONE_BD_HALFTURN_CRITERION.md"; LOCK = open("BRIEF_STONE_BD_LOCK.sha256").read().split()[0]
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("BD0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_BD_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
WIT["brief_sha"] = sha

# ============================================================================ board machine, VERBATIM (Stone BC <- Stone AV)
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
def orbits(p):
    seen = set(); out = []
    for a in range(len(p)):
        if a in seen: continue
        o = []; x = a
        while x not in seen: seen.add(x); o.append(x); x = p[x]
        out.append(o)
    return out
def ctype(p): return " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(len(o) for o in orbits(p)).items(), reverse=True))
e = lambda i, n: tuple(Fraction(int(j == i)) for j in range(n))
def B_spin(n):  # all sign patterns; roots e_i - e_{i+1}, e_n
    roots = [tuple(x - y for x, y in zip(e(i, n), e(i + 1, n))) for i in range(n - 1)] + [e(n - 1, n)]
    w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=n)]
    return board(w, roots)
PC = np.array([bin(i).count("1") for i in range(1 << 11)], dtype=np.int64)
def bits_of(w): return sum(1 << i for i, s in enumerate(w) if s < 0)
def rebase(Wl, R, n):
    N = 1 << n; Rb = np.full(N, -1, dtype=np.int64)
    for i, w in enumerate(Wl): Rb[bits_of(w[:n])] = bits_of(Wl[R[i]][:n])
    assert sorted(Rb.tolist()) == list(range(N)); return Rb
def perm_pow(p, k):
    x = np.arange(len(p))
    for _ in range(k): x = p[x]
    return x
def perm_inv(p):
    r = np.empty_like(p); r[p] = np.arange(len(p)); return r
def cyc_type(p): return ctype(tuple(int(x) for x in p))
def all_perm_arrays(n, nb, chunk=20000):
    PI = np.array(list(itertools.permutations(range(n))), dtype=np.int64)
    X = np.arange(1 << nb, dtype=np.int64)
    X9 = X | ((PC[X] & 1) << nb) if n == nb + 1 else X
    out = np.empty((len(PI), len(X)), dtype=np.uint8 if nb <= 8 else np.int64)
    mask = (1 << nb) - 1
    for s in range(0, len(PI), chunk):
        blk = np.zeros((min(chunk, len(PI) - s), len(X)), dtype=np.int64)
        for i in range(n): blk |= ((X9 >> i) & 1)[None, :] << PI[s:s + chunk, i][:, None]
        out[s:s + chunk] = blk & mask
    return PI, out
def is_B_linear(Li, nb):
    pw = (Li != 0) & ((Li & (Li - 1)) == 0)
    return pw.all(-1) & (np.bitwise_or.reduce(Li, axis=-1) == (1 << nb) - 1)
def enum_transport(PERMS, Rk, Rki, test, nb, block=512):
    N = 1 << nb; cols = np.array([0] + [1 << i for i in range(nb)]); V = np.arange(N); X = np.arange(N); found = []
    for s in range(0, len(PERMS), block):
        P = PERMS[s:s + block].astype(np.int64)
        F = Rki[P[:, Rk[cols]][:, None, :] ^ V[None, :, None]]
        f0 = F[..., 0]; Li = F[..., 1:] ^ f0[..., None]
        for bi, v in zip(*np.nonzero(test(Li, nb))):
            p = P[bi]; ff = Rki[p[Rk[X]] ^ v]; L = np.zeros(N, dtype=np.int64)
            for i in range(nb): L ^= ((X >> i) & 1) * int(Li[bi, v, i])
            if np.array_equal(ff, L ^ int(f0[bi, v])): found.append((s + int(bi), int(v)))
    return found
def enum_commute(PERMS, c, nb, block=512):
    N = 1 << nb; cols = np.array([0] + [1 << i for i in range(nb)]); V = np.arange(N); found = []
    for s in range(0, len(PERMS), block):
        P = PERMS[s:s + block].astype(np.int64)
        left = P[:, c[cols]][:, None, :] ^ V[None, :, None]; right = c[P[:, cols][:, None, :] ^ V[None, :, None]]
        for bi, v in zip(*np.nonzero((left == right).all(-1))):
            p = P[bi]
            if np.array_equal(p[c] ^ v, c[p ^ v]): found.append((s + int(bi), int(v)))
    return found
def g_arr(PERMS, g): return PERMS[g[0]].astype(np.int64) ^ g[1]
def mode_count_rows(D):
    B, m = D.shape; S = np.sort(D, axis=1); flat = S.ravel()
    boundary = np.ones(B * m + 1, dtype=bool); boundary[1:-1] = flat[1:] != flat[:-1]; boundary[np.arange(0, B * m, m)] = True
    starts = np.flatnonzero(boundary); lens = np.diff(starts); row = starts[:-1] // m
    first = np.flatnonzero(np.r_[True, row[1:] != row[:-1]])
    return np.maximum.reduceat(lens, first)
def sp_name(pi, v, n): return tuple(("-" if (v >> pi[i]) & 1 else "+") + "e%d" % (pi[i] + 1) for i in range(n))
def cycle_name(pi, v, n):
    seen = set(); parts = []
    for i in range(n):
        if i in seen: continue
        chain = []; s, j = 1, i
        while True:
            chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); seen.add(j)
            s = s * (-1 if (v >> pi[j]) & 1 else 1); j = pi[j]
            if j == i: chain.append(("" if s > 0 else "-") + "e%d" % (j + 1)); break
        if len(chain) == 2 and chain[0] == chain[1]: continue
        parts.append("(" + " -> ".join(chain) + ")")
    return " ".join(parts) if parts else "1"
def name_B(PI, g, n): return cycle_name(tuple(int(t) for t in PI[g[0]]), g[1], n)
def f2_rank(vecs):
    basis = []
    for v in vecs:
        v = int(v)
        for b in basis: v = min(v, v ^ b)
        if v: basis.append(v)
    return len(basis)
def affine_dim(pts): return f2_rank([int(p) ^ int(pts[0]) for p in pts])

# ============================================================================ NEW: all nearest Weyl elements; set stabilizer
def all_nearest(PERMS, target, block=4096):
    """every (pi, v) maximising #{x : pi(x) ^ v == target[x]} over the whole board; returns (best, list)."""
    T = target.astype(np.int64); best = -1; out = []
    for s in range(0, len(PERMS), block):
        D = PERMS[s:s + block].astype(np.int64) ^ T[None, :]; mc = mode_count_rows(D); m = int(mc.max())
        if m > best: best, out = m, []
        if m == best:
            for r in np.flatnonzero(mc == m):
                for v, cnt in Counter(D[r].tolist()).items():
                    if cnt == m: out.append((s + int(r), int(v)))
    return best, sorted(out)
def enum_stab(PERMS, Y, nb, block=512):
    """all (pi, v) with g(Y) = Y as a set."""
    Y = np.asarray(sorted(int(y) for y in Y)); N = 1 << nb; V = np.arange(N); found = []
    for s in range(0, len(PERMS), block):
        P = PERMS[s:s + block].astype(np.int64)
        img = np.sort(P[:, Y][:, None, :] ^ V[None, :, None], axis=-1)              # (B, N, |Y|)
        for bi, v in zip(*np.nonzero((img == Y[None, None, :]).all(-1))): found.append((s + int(bi), int(v)))
    return found

# ============================================================================ the six boards
boards = {}
for n in range(3, 9):
    Wn, idxn, Sn, Rnt, Pn, _ = B_spin(n); Rb = rebase(Wn, Rnt, n); PI, PERMS = all_perm_arrays(n, n)
    boards[n] = dict(Rb=Rb, PI=PI, PERMS=PERMS, h=2 * n, type=cyc_type(Rb))
    tick("B%d: |W| = %d, R type %s" % (n, len(PI) * (1 << n), boards[n]["type"]))

def analyse(n, w, tagname):
    """everything the brief asks about one Weyl element w = (pi, v) on B_n at the half-turn."""
    B = boards[n]; PERMS, PI, Rb = B["PERMS"], B["PI"], B["Rb"]; m = n; Rm = perm_pow(Rb, m); N = 1 << n
    wa = g_arr(PERMS, w); wi = perm_inv(wa); c = wi[Rm]; Y = [int(x) for x in np.flatnonzero(c == np.arange(N))]
    d = dict(board=n, w=name_B(PI, w, n), w_inv=bool(np.array_equal(wa[wa], np.arange(N))), agree=len(Y), Y_affdim=affine_dim(Y) if Y else -1,
             c_type=cyc_type(c), c_inv=bool(np.array_equal(c[c], np.arange(N))), RwR_eq_winv=bool(np.array_equal(Rm[wa[Rm]], wi)),
             w_in_Cm=bool(np.array_equal(wa[Rm], Rm[wa])))
    CWc = set(enum_commute(PERMS, c, n)); CWw = set(enum_commute(PERMS, wa, n)); Cm = B["Cm"]; Im = B["Im"]; StabY = set(enum_stab(PERMS, Y, n))
    d.update(CWc=len(CWc), CWw=len(CWw), StabY=len(StabY), Cm=len(Cm), Im=len(Im),
             CWc_in_StabY=CWc <= StabY, Im_in_StabY=Im <= StabY,
             lemmaB=(Im & StabY) == CWc if d["Y_affdim"] == n else None,
             two_imply_third=((CWw & Cm) <= CWc) and ((CWw & CWc) <= Cm) and ((CWc & Cm) <= CWw),
             extras_eq=((Im & StabY) - Cm) == (CWc - CWw), CWc_in_Cm=CWc <= Cm, CWc_names=sorted(name_B(PI, g, n) for g in CWc) if len(CWc) <= 16 else len(CWc))
    say("  [%s] B%d w = %-52s  agree %3d/%3d (Y affdim %d)  c: type %-22s c^2=1:%-5s R^m w R^m = w^-1:%-5s w in C_m:%-5s |C_W(c)|=%-3d |C_W(w)|=%-3d |Stab(Y)|=%-3d |C_m|=%-3d |I_m|=%-3d"
        % (tagname, n, d["w"], d["agree"], N, d["Y_affdim"], d["c_type"], d["c_inv"], d["RwR_eq_winv"], d["w_in_Cm"], d["CWc"], d["CWw"], d["StabY"], d["Cm"], d["Im"]))
    note("      Lemma B (I_m cap Stab Y = C_W(c)): %s; C_W(c) <= Stab(Y): %s; I_m <= Stab(Y): %s; two-imply-third: %s; extras (I_m cap Stab Y) \\ C_m == C_W(c) \\ C_W(w): %s; C_W(c) <= C_m: %s"
         % (d["lemmaB"], d["CWc_in_StabY"], d["Im_in_StabY"], d["two_imply_third"], d["extras_eq"], d["CWc_in_Cm"]))
    return d

banner("C_m, I_m and the nearest Weyl elements to the half-turn on B3..B8")
for n in range(3, 9):
    B = boards[n]; Rm = perm_pow(B["Rb"], n); Rmi = perm_inv(Rm); assert np.array_equal(Rm, Rmi)
    B["Cm"] = set(enum_commute(B["PERMS"], Rm, n)); B["Im"] = set(enum_transport(B["PERMS"], Rm, Rmi, is_B_linear, n))
    B["best"], B["nearest"] = all_nearest(B["PERMS"], Rm)
    w0 = (int(np.flatnonzero((B["PI"] == np.arange(n)).all(1))[0]), (1 << n) - 1)
    B["nearest_names"] = [name_B(B["PI"], g, n) for g in B["nearest"]]
    anti = {(g[0], g[1] ^ ((1 << n) - 1)) for g in B["nearest"]}
    B["nearest_antipode_closed"] = anti == set(B["nearest"])
    say("  B%d: |C_m| = %d, |I_m| = %d (%s); nearest Weyl elements to R^%d: best agreement %d/%d, %d element(s): %s; closed under w -> -w: %s"
        % (n, len(B["Cm"]), len(B["Im"]), "ANOMALOUS" if len(B["Im"]) > len(B["Cm"]) else "clean", n, B["best"], 1 << n, len(B["nearest"]),
           B["nearest_names"] if len(B["nearest"]) <= 8 else str(len(B["nearest"])) + " elements", B["nearest_antipode_closed"]))
tick("centralizers, shared grammars and nearest elements done")

# ============================================================================ BD1 -- B4 with w = -tau
banner("BD1 -- B4, w = -tau")
PI4 = boards[4]["PI"]; w_tau = next(g for g in boards[4]["nearest"] if name_B(PI4, g, 4) == "(e1 -> -e1) (e2 -> -e3 -> e2)")
d1 = analyse(4, w_tau, "BD1")
O2_4 = [o for o in orbits(tuple(int(x) for x in boards[4]["Rb"])) if 0 not in o][0]
guess("BD1", "B4 with w = -tau: w in C_4, c^2 = 1, |Stab_W(O2)| = 16, I_4 <= Stab_W(O2), I_4 = C_W(c) of order 8, and the four extras are C_W(c) \\ C_W(w)",
      d1["w_in_Cm"] and d1["c_inv"] and sorted(set(range(16)) - set(O2_4)) == sorted(set(range(16)) - set(O2_4)) and d1["agree"] == 8 and set(np.flatnonzero(perm_inv(g_arr(boards[4]["PERMS"], w_tau))[perm_pow(boards[4]["Rb"], 4)] == np.arange(16)).tolist()) == set(O2_4)
      and d1["StabY"] == 16 and d1["Im_in_StabY"] and d1["lemmaB"] and d1["CWc"] == 8 and d1["Im"] == 8 and d1["Cm"] == 4 and d1["extras_eq"] and d1["two_imply_third"],
      "C_W(c) = %s" % d1["CWc_names"])
WIT["BD1"] = d1

# ============================================================================ BD2 -- B8 with the carrying w
banner("BD2 -- B8, w = -(e2 e3)(e4 e5)(e6 e7)")
PI8 = boards[8]["PI"]; w8 = next(g for g in boards[8]["nearest"] if name_B(PI8, g, 8) == "(e1 -> -e1) (e2 -> -e3 -> e2) (e4 -> -e5 -> e4) (e6 -> -e7 -> e6)")
d2 = analyse(8, w8, "BD2")
check("BD2a", "B8: w is an involution not in C_8, hence (Lemma BD-A) c^2 != 1; R^8 w R^8 != w^-1; C_W(c) = {+-1} = C_8 = I_8; Lemma B holds",
      d2["w_inv"] and not d2["w_in_Cm"] and not d2["c_inv"] and not d2["RwR_eq_winv"] and d2["CWc"] == 2 and d2["Cm"] == 2 and d2["Im"] == 2 and d2["lemmaB"])
guess("BD2", "B8: Stab_W(Fix c) = {+-1} -- the 52-point agreement set has no Weyl symmetry beyond the antipode", d2["StabY"] == 2, "|Stab_W(Y)| = %d" % d2["StabY"])
StabY8 = sorted(enum_stab(boards[8]["PERMS"], [int(x) for x in np.flatnonzero(perm_inv(g_arr(boards[8]["PERMS"], w8))[perm_pow(boards[8]["Rb"], 8)] == np.arange(256))], 8))
names8 = [name_B(PI8, g, 8) for g in StabY8]
note("POST-REVEAL [C]: Stab_W(Y) on B8 = {%s}; its two elements beyond +-1 lie in I_8: %s, commute with c: %s (Lemma B: they are the elements of Stab(Y) outside C_W(c), hence outside I_8)"
     % ("; ".join(names8), [g in boards[8]["Im"] for g in StabY8], [g in set(enum_commute(boards[8]["PERMS"], perm_inv(g_arr(boards[8]["PERMS"], w8))[perm_pow(boards[8]["Rb"], 8)], 8)) for g in StabY8]))
WIT["BD2"] = d2; WIT["StabY8"] = names8

# ============================================================================ BD3 -- B3 inside W(B3)
banner("BD3 -- B3 inside W(B3) (R^3 is Weyl in W(D4), not in W(B3))")
d3s = [analyse(3, g, "BD3") for g in boards[3]["nearest"]]
ok3 = any(d["Y_affdim"] == 3 and d["lemmaB"] and d["w_in_Cm"] and d["c_inv"] and d["extras_eq"] and d["Im_in_StabY"] for d in d3s)
guess("BD3", "B3: a nearest Weyl element w in W(B3) to R^3 has a spanning agreement set, Lemma B applies, w in C_3, c^2 = 1, and the eight extras are C_W(c) \\ C_W(w)",
      ok3 and boards[3]["Im"].__len__() == 16 and len(boards[3]["Cm"]) == 8,
      "nearest: %s; per element (agree, w in C_3, c^2=1, |C_W(c)|, extras_eq, Lemma B): %s" % (boards[3]["nearest_names"], [(d["agree"], d["w_in_Cm"], d["c_inv"], d["CWc"], d["extras_eq"], d["lemmaB"]) for d in d3s]))
WIT["BD3"] = d3s
def spanning_survey(n):
    """over every w in W(B_n): the agreement set Fix(w^-1 R^m) with the half-turn; how many are affinely spanning, and the best agreement among those."""
    B = boards[n]; PERMS, Rb = B["PERMS"], B["Rb"]; Rm = perm_pow(Rb, n); N = 1 << n; X = np.arange(N); best_all = 0; n_span = 0; best_span = 0; best_span_w = []
    for s0 in range(0, len(PERMS), 256):
        P = PERMS[s0:s0 + 256].astype(np.int64)
        agree = (P[:, None, :] ^ np.arange(N)[None, :, None]) == Rm[None, None, :]          # (B, N, N): g(x) == R^m(x)
        cnt = agree.sum(-1); best_all = max(best_all, int(cnt.max()))
        for bi, v in zip(*np.nonzero(cnt >= n + 1)):                                            # a spanning set needs n+1 points
            Y = X[agree[bi, v]]
            if affine_dim(Y) == n:
                n_span += 1; a = int(cnt[bi, v])
                if a > best_span: best_span, best_span_w = a, []
                if a == best_span: best_span_w.append((s0 + int(bi), int(v)))
    return best_all, n_span, best_span, best_span_w
surv = {}
for n in range(3, 8):
    ba, ns, bs, bw = spanning_survey(n); surv[n] = (ba, ns, bs, [name_B(boards[n]["PI"], g, n) for g in bw][:4])
    note("POST-REVEAL [C] B%d: over all %d Weyl elements, best agreement with R^%d is %d/%d; %d elements have an affinely SPANNING agreement set (Lemma B applies), best among them %d/%d: %s"
         % (n, len(boards[n]["PI"]) * (1 << n), n, ba, 1 << n, ns, bs, 1 << n, surv[n][3] if ns else "none"))
check("BD3b", "POST-REVEAL [C]: within W(B3) NO Weyl element agrees with R^3 on an affinely spanning set (max agreement 4 of 8, on a 2-flat), so Lemma B and the sentence never apply on B3 -- the B3 anomaly is the overgroup's (SM-060 AV5c), not the 4-cube's; on B4 the spanning survey returns -tau as the best spanning element (8/16)",
      surv[3][1] == 0 and surv[3][0] == 4 and surv[4][2] == 8 and surv[4][3] == ["(e1 -> -e1) (e2 -> -e3 -> e2)"], {n: surv[n][:3] for n in surv})
WIT["spanning_survey"] = surv
tick("spanning survey done (B8 not surveyed: 10.3M elements)")

# ============================================================================ BD4 -- B5, B6, B7
banner("BD4 -- the clean boards B5, B6, B7")
d4 = {n: [analyse(n, g, "BD4") for g in boards[n]["nearest"]] for n in (5, 6, 7)}
ok4 = all(not d["w_in_Cm"] and d["CWc_in_Cm"] and (d["lemmaB"] in (True, None)) for n in (5, 6, 7) for d in d4[n])
guess("BD4", "B5, B6, B7: no nearest Weyl element to the half-turn commutes with it; C_W(w^-1 R^m) <= C_m for each; Lemma B's equality holds wherever the agreement set spans",
      ok4, {n: [(d["agree"], d["Y_affdim"], d["w_in_Cm"], d["c_inv"], d["CWc"], d["CWc_in_Cm"], d["lemmaB"]) for d in d4[n]] for n in (5, 6, 7)})
WIT["BD4"] = d4

# ============================================================================ BD5 -- the criterion across six boards
banner("BD5 -- the criterion: anomaly iff some nearest Weyl element commutes with the half-turn")
allw = {4: [d1] + [analyse(4, g, "BD5") for g in boards[4]["nearest"] if g != w_tau], 8: [d2] + [analyse(8, g, "BD5") for g in boards[8]["nearest"] if g != w8], 3: d3s, 5: d4[5], 6: d4[6], 7: d4[7]}
table = {}
for n in range(3, 9):
    anomalous = len(boards[n]["Im"]) > len(boards[n]["Cm"]); commutes = any(d["w_in_Cm"] for d in allw[n]); invol = any(d["c_inv"] for d in allw[n])
    table[n] = dict(anomalous=anomalous, some_nearest_commutes=commutes, some_c_involution=invol, Im=len(boards[n]["Im"]), Cm=len(boards[n]["Cm"]), n_nearest=len(boards[n]["nearest"]), best=boards[n]["best"])
    say("  B%d: |I_m| = %3d |C_m| = %3d anomalous=%-5s | nearest: %d element(s), agreement %d/%d, some commute with R^m: %-5s some c involution: %-5s"
        % (n, table[n]["Im"], table[n]["Cm"], anomalous, table[n]["n_nearest"], boards[n]["best"], 1 << n, commutes, invol))
guess("BD5", "on B3..B8: I_{h/2} exceeds C_{h/2} iff some nearest Weyl element to R^{h/2} commutes with R^{h/2}",
      all(t["anomalous"] == t["some_nearest_commutes"] for t in table.values()), {n: (t["anomalous"], t["some_nearest_commutes"]) for n, t in table.items()})
guess("BD5b", "on each of the six boards the nearest Weyl element is unique up to the antipode (the set is {w, -w})",
      all(boards[n]["n_nearest"] if False else len(boards[n]["nearest"]) == 2 and boards[n]["nearest_antipode_closed"] for n in range(3, 9)),
      {n: (len(boards[n]["nearest"]), boards[n]["nearest_antipode_closed"]) for n in range(3, 9)})
note("also: anomaly iff some correction is an involution: %s" % all(t["anomalous"] == t["some_c_involution"] for t in table.values()))
note("CAVEAT (post-reveal): on B3 the criterion holds as a marker only -- its nearest elements have non-spanning agreement sets, Lemma B does not apply, and the extras come from the overgroup W(D4) (BD3 INVERTED, BD3b); the explanatory chain nearest-w -> commutes -> c involution -> C_W(c) \\ C_W(w) is verified on B4 (positive) and on B5..B8 (negative: w does not commute, c is not an involution, C_W(c) = C_m)")
WIT["BD5"] = table

# ============================================================================ BD6 -- the lemmas as computations
banner("BD6 -- Lemmas BD-A and BD-B on every nearest (and carrying) w")
ds = [d for n in range(3, 9) for d in allw[n]]
bdA = all(d["c_inv"] == d["RwR_eq_winv"] for d in ds) and all((d["c_inv"] == d["w_in_Cm"]) for d in ds if d["w_inv"])
bdB = all(d["two_imply_third"] and d["extras_eq"] for d in ds if d["w_in_Cm"])
check("BD6", "Lemma BD-A (c^2 = 1 iff R^m w R^m = w^-1; for involutions iff w in C_m) and Lemma BD-B (two-imply-third; extras = C_W(c) \\ C_W(w)) hold as computations on all %d elements examined" % len(ds),
      bdA and bdB, "BD-A %s, BD-B %s; involutions among them: %d" % (bdA, bdB, sum(1 for d in ds if d["w_inv"])))

# ============================================================================ witnesses, verdict
os.makedirs("_stone_bd_cache", exist_ok=True)
def _default(o):
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    if isinstance(o, (set, tuple)): return list(o)
    return str(o)
json.dump({str(k): v for k, v in WIT.items()}, open(os.path.join("_stone_bd_cache", "witnesses_bd.json"), "w"), indent=1, default=_default)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED (registered guesses INVERTED unless a bug is shown): " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
