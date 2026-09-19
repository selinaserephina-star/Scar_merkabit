# -*- coding: utf-8 -*-
r"""verify_stone_bf_why_four.py -- STONE BF: WHY FOUR -- THE COMMUTATION THEOREM

Brief: BRIEF_STONE_BF_WHY_FOUR.md (lock BRIEF_STONE_BF_LOCK.sha256, re-verified as BF0).  The proofs are in the brief;
this verifier re-checks every statement as a computation on the actual clocks (Stone BE's combinatorial rowmotion on the
shifted staircase, verbatim, validated there against the sealed B4/B8 clocks).
BF1 Lemma BF-A (rowmotion in excess coordinates) equals the clock on every weight, n = 4..12;
BF2 Prop. BF-B (the orbit of lambda in closed form; ranks 0,n,n-1,n-1,...,1,1; the +-n/2 shift for even n), n = 3..16;
BF3 Prop. BF-C (w_n preserves O1 as the two reflections i -> 2-i (even), i -> -i (odd); commutes with H there), even n = 4..16;
BF4 Prop. BF-E (H(e_2) and H({3,n}) in closed form), even n = 6..16;
BF5 Theorem BF (w_n commutes with R^n iff n = 4; e_2 the witness), even n = 4..16;
BF6 [obs, guess] R^3(e_p) = -e_{n-1-p} and the closed form of H(e_p), n = 4..16;
BF7 [obs, guess] odd n: the SM-068 nearest element's analogue does not commute, n = 5, 7, 9, 11.
DISCIPLINE: compute, never assert; registered guesses (BF6, BF7 only) resolvable INVERTED; no registry/git writes.  Rule 3.
Run:  python -X utf8 verify_stone_bf_why_four.py
"""
import os, sys, time, json, hashlib
from collections import Counter
import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
LOG = open("verify_stone_bf_why_four.log", "w", encoding="utf-8")
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

say("=" * 78); say("STONE BF -- WHY FOUR: THE COMMUTATION THEOREM"); say("=" * 78)
BRIEF = "BRIEF_STONE_BF_WHY_FOUR.md"; LOCK = open("BRIEF_STONE_BF_LOCK.sha256").read().split()[0]
sha = hashlib.sha256(open(BRIEF, "rb").read()).hexdigest()
check("BF0", "the brief is sha-locked: sha256(%s) equals BRIEF_STONE_BF_LOCK.sha256" % BRIEF, sha == LOCK, sha[:16] + "...")
WIT["brief_sha"] = sha

# ============================================================================ Stone BE's combinatorial clock, VERBATIM
def staircase_rowmotion(n):
    cells = [(k, c) for k in range(1, n + 1) for c in range(k, n + 1)]; idx = {cl: i for i, cl in enumerate(cells)}; M = len(cells)
    lower = [([idx[(k, c + 1)]] if c + 1 <= n else []) + ([idx[(k - 1, c - 1)]] if k >= 2 else []) for (k, c) in cells]
    DC = np.zeros((M, M), dtype=np.int64)
    for i in sorted(range(M), key=lambda i: (n - cells[i][1]) + (cells[i][0] - 1)):
        DC[i, i] = 1
        for j in lower[i]: DC[i] |= DC[j]
    N = 1 << n
    plus = [[p + 1 for p in range(n) if not (x >> p) & 1] for x in range(N)]
    I = np.zeros((N, M), dtype=bool)
    for i, (k, c) in enumerate(cells):
        ck = np.array([pl[k - 1] if len(pl) >= k else n + 1 for pl in plus]); I[:, i] = ck <= c
    cond = ~I
    for i in range(M):
        for j in lower[i]: cond[:, i] &= I[:, j]
    RI = (cond.astype(np.int64) @ DC) > 0
    out = np.full(N, (1 << n) - 1, dtype=np.int64)
    for k in range(1, n + 1):
        rowcells = [idx[(k, c)] for c in range(k, n + 1)]; sub = RI[:, rowcells]; has = sub.any(1); ck = k + sub.argmax(1)
        out[has] &= ~(1 << (ck[has] - 1))
    assert sorted(out.tolist()) == list(range(N)), "rowmotion is not a bijection"
    return out
def perm_pow(p, k):
    x = np.arange(len(p))
    for _ in range(k): x = p[x]
    return x
def perm_inv(p):
    r = np.empty_like(p); r[p] = np.arange(len(p)); return r

# ============================================================================ NEW: Lemma BF-A as a function; coordinates
def minus_set(x, n): return tuple(p + 1 for p in range(n) if (x >> p) & 1)
def from_minus(S, n): return sum(1 << (p - 1) for p in S)
def excess(x, n):
    plus = [p + 1 for p in range(n) if not (x >> p) & 1]; return tuple(c - (k + 1) for k, c in enumerate(plus))
def from_excess(d, n):
    plus = [dk + k + 1 for k, dk in enumerate(d)]; return from_minus(set(range(1, n + 1)) - set(plus), n)
def R_excess(d, n):
    """Lemma BF-A: rowmotion on excess sequences."""
    r = len(d); G = [k for k in range(1, r + 1) if d[k - 1] > (d[k - 2] if k >= 2 else 0)]
    cap = (n - r - 1) if (r == 0 or d[r - 1] < n - r) else None
    out = []
    for kp in range(1, r + 2):
        cands = [d[k - 1] - 1 for k in G if k >= kp] + ([cap] if (cap is not None and kp <= r + 1) else [])
        if not cands: break
        out.append(min(cands))
    return tuple(out)
def w_even(n, x_arr):
    """w_n = -(e2 e3)(e4 e5)...(e_{n-2} e_{n-1}), e_n fixed (n even): pi = (2 3)(4 5)..., v = [n-1]."""
    pi = list(range(n))
    for k in range(1, n - 1, 2): pi[k], pi[k + 1] = pi[k + 1], pi[k]
    out = np.zeros_like(x_arr)
    for j in range(n): out |= ((x_arr >> j) & 1) << pi[j]
    return out ^ ((1 << (n - 1)) - 1)
def w_odd(n, x_arr):
    """the SM-068 shape for odd n: pi = (2 3)(4 5)...(n-3 n-2), v = [n] (as found on B5, B7)."""
    pi = list(range(n))
    for k in range(1, n - 2, 2): pi[k], pi[k + 1] = pi[k + 1], pi[k]
    out = np.zeros_like(x_arr)
    for j in range(n): out |= ((x_arr >> j) & 1) << pi[j]
    return out ^ ((1 << n) - 1)

CLOCK = {}
for n in range(3, 17):
    CLOCK[n] = staircase_rowmotion(n)
tick("clocks built for n = 3..16")

# ============================================================================ BF1 -- Lemma BF-A against the clock
banner("BF1 -- Lemma BF-A (rowmotion in excess coordinates) against the clock, every weight, n = 4..12")
ok1 = True; det1 = {}
for n in range(4, 13):
    R = CLOCK[n]; N = 1 << n; bad = 0
    for x in range(N):
        d = excess(x, n); assert from_excess(d, n) == x
        if from_excess(R_excess(d, n), n) != int(R[x]): bad += 1
    det1[n] = bad; ok1 &= bad == 0
check("BF1", "Lemma BF-A reproduces the clock on all 2^n weights for n = 4..12 (%d weights in all)" % sum(1 << n for n in range(4, 13)), ok1, "mismatches per n: %s" % det1)
tick("BF1 done")

# ============================================================================ BF2 -- Prop. BF-B
banner("BF2 -- Prop. BF-B: the orbit of lambda in closed form, n = 3..16")
def lam_orbit(n):
    R = CLOCK[n]; o = [0]; x = 0
    for _ in range(2 * n - 1): x = int(R[x]); o.append(x)
    return o
ok2 = True; det2 = {}
for n in range(3, 17):
    o = lam_orbit(n); full = set(range(1, n + 1)); okn = True
    for j in range(1, n // 2 + 1): okn &= minus_set(o[2 * j], n) == tuple(sorted(full - set(range(n - 2 * j + 2, n + 1, 2))))
    for j in range(0, (n - 1) // 2 + 1): okn &= minus_set(o[2 * j + 1], n) == tuple(sorted(full - set(range(n - 2 * j + 1, n, 2))))
    ranks = [bin(x).count("1") for x in o]
    exp = [0] + [n - (i // 2) for i in range(1, n + 2)] + [((2 * n - i) + 1) // 2 for i in range(n + 2, 2 * n)]
    okn &= ranks == exp
    # antipode identity R^{-k} lambda = -R^{k+1} lambda
    okn &= all(o[(-k) % (2 * n)] == ((1 << n) - 1) ^ o[(k + 1) % (2 * n)] for k in range(2 * n))
    if n % 2 == 0:
        H = perm_pow(CLOCK[n], n); okn &= all(bin(int(H[x])).count("1") - bin(x).count("1") in (n // 2, -n // 2) for x in o)
    det2[n] = okn; ok2 &= okn
check("BF2", "Prop. BF-B: R^{2j} lambda and R^{2j+1} lambda as stated, the rank sequence 0,n,n-1,n-1,...,1,1, the antipode identity R^-k lambda = -R^{k+1} lambda, and (even n) the half-turn shift exactly +-n/2 on the orbit of lambda -- n = 3..16", ok2, det2)
tick("BF2 done")

# ============================================================================ BF3 -- Prop. BF-C
banner("BF3 -- Prop. BF-C: w_n on the orbit of lambda (even n)")
ok3 = True; det3 = {}
for n in range(4, 17, 2):
    o = lam_orbit(n); pos = {x: i for i, x in enumerate(o)}; X = np.arange(1 << n); w = w_even(n, X); H = perm_pow(CLOCK[n], n)
    okn = all(int(w[x]) in pos for x in o)
    if okn:
        okn &= all(pos[int(w[o[i]])] == ((2 - i) % (2 * n) if i % 2 == 0 else (-i) % (2 * n)) for i in range(2 * n))
    okn &= all(int(w[H[x]]) == int(H[w[x]]) for x in o)
    det3[n] = okn; ok3 &= okn
check("BF3", "Prop. BF-C: w_n preserves the orbit of lambda, acting as i -> 2-i on even and i -> -i on odd clock positions, and commutes with R^n on it -- even n = 4..16", ok3, det3)
tick("BF3 done")

# ============================================================================ BF4 -- Prop. BF-E
banner("BF4 -- Prop. BF-E: H(e_2) and H({3,n}) in closed form (even n >= 6)")
ok4 = True; det4 = {}
for n in range(6, 17, 2):
    H = perm_pow(CLOCK[n], n)
    He2 = minus_set(int(H[from_minus({2}, n)]), n); exp_e2 = tuple(sorted({1, 2} | set(range(5, n, 2))))
    H3n = minus_set(int(H[from_minus({3, n}, n)]), n)
    exp_3n = (1, 2, 3, 5, 6) if n == 6 else tuple(sorted(set(range(1, n + 1)) - ({4, 6} | set(range(7, n, 2)))))
    okn = He2 == exp_e2 and H3n == exp_3n and 2 in H3n and 3 not in He2
    det4[n] = (okn, He2, H3n); ok4 &= okn
    # the excess trail of the proof: R^{2j} e_2 and R^{2j+1} e_2, R^{2j+1}{3,n}, R^{2j+2}{3,n}
    R = CLOCK[n]; x = from_minus({2}, n); trail_ok = True
    for j in range(2, n // 2):
        trail_ok &= excess(int(perm_pow(R, 2 * j)[x]), n) == tuple([n - 1 - 2 * j] + list(range(n - 2 * j + 2, n - j + 1)))
        trail_ok &= excess(int(perm_pow(R, 2 * j + 1)[x]), n) == tuple([n - 2 - 2 * j] + list(range(n - 2 * j + 1, n - j)))
    trail_ok &= excess(int(H[x]), n) == tuple([2, 2] + list(range(3, n // 2 + 1)))
    y = from_minus({3, n}, n)
    if n >= 8:
        for j in range(2, n // 2 - 1):
            trail_ok &= excess(int(perm_pow(R, 2 * j + 1)[y]), n) == tuple([n - 3 - 2 * j] + list(range(n - 2 * j + 2, n - j + 1)))
            trail_ok &= excess(int(perm_pow(R, 2 * j + 2)[y]), n) == tuple([n - 4 - 2 * j] + list(range(n - 2 * j + 1, n - j)))
        trail_ok &= excess(int(perm_pow(R, n - 1)[y]), n) == tuple([4, 4] + list(range(5, n // 2 + 2)))
        trail_ok &= excess(int(H[y]), n) == tuple([3, 4, 4] + list(range(5, n // 2 + 1)))
    trail_ok &= excess(int(perm_pow(R, 3)[x]), n) == (n - 4,) and excess(int(perm_pow(R, 4)[x]), n) == (n - 5, n - 2)
    trail_ok &= int(R[y]) == from_minus({4}, n)
    ok4 &= trail_ok; det4[n] = det4[n] + (trail_ok,)
check("BF4", "Prop. BF-E: H(e_2) = {1,2} u {5,7,...,n-1} and H({3,n}) = [n] \\ {4,6,7,9,...,n-1} (n >= 8; {1,2,3,5,6} at n = 6), with every excess sequence of the two inductions as the proof states -- even n = 6..16",
      ok4, {n: v[0] and v[3] for n, v in det4.items()})
for n in (6, 8, 16): note("n = %d: H(e_2) = %s; H({3,n}) = %s" % (n, det4[n][1], det4[n][2]))
tick("BF4 done")

# ============================================================================ BF5 -- Theorem BF
banner("BF5 -- Theorem BF: w_n commutes with R^n iff n = 4 (even n = 4..16); e_2 the witness")
ok5 = True; det5 = {}
for n in range(4, 17, 2):
    X = np.arange(1 << n); w = w_even(n, X); H = perm_pow(CLOCK[n], n); comm = bool(np.array_equal(w[H], H[w]))
    e2 = from_minus({2}, n); wHe2 = minus_set(int(w[H[e2]]), n); Hwe2 = minus_set(int(H[w[e2]]), n)
    witness = (2 in wHe2) and (2 not in Hwe2)
    nbad = int((w[H] != H[w]).sum())
    det5[n] = (comm, witness, nbad); ok5 &= (comm == (n == 4)) and (witness == (n != 4))
check("BF5", "Theorem BF: w_4 = -tau commutes with R^4; for even n = 6..16 it does not, and e_2 witnesses it (2 in w(H e_2), 2 not in H(w e_2))", ok5,
      {n: "commutes=%s witness=%s |{x: wHx != Hwx}|=%d" % v for n, v in det5.items()})
note("the non-commuting set is empty at n = 4 and grows: %s" % {n: v[2] for n, v in det5.items()})
WIT["BF5"] = det5
tick("BF5 done")

# ============================================================================ BF6 -- [obs] R^3(e_p), H(e_p)
banner("BF6 -- [obs, registered guess] R^3(e_p) = -e_{n-1-p}; the closed form of H(e_p)")
def Hpred(p, n):
    m = p - 1 if p <= n // 2 else n - p
    return tuple(sorted({1, 2} | set(range(4, 2 * m + 1, 2)) | set(range(2 * m + 3 if p <= n // 2 else 2 * m + 1, n, 2))))
ok6 = True; det6 = {}
for n in range(4, 17, 2):
    R = CLOCK[n]; H = perm_pow(R, n); N = 1 << n; R3 = perm_pow(R, 3)
    r3 = all(int(R3[from_minus({p}, n)]) == (N - 1) ^ from_minus({n - 1 - p}, n) for p in range(1, n - 1))
    hp = all(minus_set(int(H[from_minus({p}, n)]), n) == Hpred(p, n) for p in range(2, n - 1))
    det6[n] = (r3, hp); ok6 &= r3 and hp
guess("BF6", "R^3(e_p) = -e_{n-1-p} for 1 <= p <= n-2, and H(e_p) = {1,2} u {4,...,2m} u {2m'+1,...,n-1} (m = p-1, m' = p for p <= n/2; m = m' = n-p for p >= n/2), for 2 <= p <= n-2 -- even n = 4..16 (seen to 14 in the exploration; n = 16 the new instance)", ok6, det6)
tick("BF6 done")

# ============================================================================ BF7 -- [obs] odd n
banner("BF7 -- [obs, registered guess] odd n: the SM-068 shape does not commute with R^n (n = 5, 7, 9, 11, 13, 15)")
det7 = {}
for n in range(5, 16, 2):
    X = np.arange(1 << n); w = w_odd(n, X); H = perm_pow(CLOCK[n], n); det7[n] = int((w[H] != H[w]).sum())
guess("BF7", "for odd n = 5..15 the element -(e2 e3)(e4 e5)...(e_{n-3} e_{n-2}) with e_{n-1}, e_n negated (SM-068's nearest element on B5, B7) does not commute with R^n", all(v > 0 for v in det7.values()), "non-commuting points: %s" % det7)
tick("BF7 done")

os.makedirs("_stone_bf_cache", exist_ok=True)
json.dump({str(k): v for k, v in WIT.items()}, open(os.path.join("_stone_bf_cache", "witnesses_bf.json"), "w"), indent=1, default=str)
banner("VERDICT")
npass = sum(1 for t_, ok in RESULTS if ok); nfail = [t_ for t_, ok in RESULTS if not ok]
say("RESULT: %d checks passed, %d failed%s" % (npass, len(nfail), ("  FAILED (registered guesses INVERTED unless a bug is shown): " + str(nfail)) if nfail else ""))
tick("done"); LOG.close()
