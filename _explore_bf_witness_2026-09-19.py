# -*- coding: utf-8 -*-
"""_explore_bf_witness_2026-09-19.py -- FREE EXPLORATION (not sealed): where does w_n = -(e2 e3)(e4 e5)...(e_{n-2} e_{n-1})
(e_n fixed) fail to commute with the half-turn H = R^n on the B_n spinor, for even n?  Uses Stone BE's combinatorial
rowmotion (verbatim).  Prints, per n: |{x : wHx != Hwx}|, the lowest-rank witnesses, and checks the closed form of O1."""
import numpy as np, itertools, sys
from collections import Counter

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
    return out
def perm_pow(p, k):
    x = np.arange(len(p))
    for _ in range(k): x = p[x]
    return x
def sset(x, n): return tuple(p + 1 for p in range(n) if (x >> p) & 1)   # minus positions, 1-based
def w_n(n):
    """pi = (2 3)(4 5)...(n-2 n-1), v = positions 1..n-1 negated (even n)."""
    pi = list(range(n))
    for k in range(1, n - 1, 2): pi[k], pi[k + 1] = pi[k + 1], pi[k]     # 0-based: swap (1,2),(3,4),...
    v = (1 << (n - 1)) - 1
    X = np.arange(1 << n); out = np.zeros_like(X)
    for j in range(n): out |= ((X >> j) & 1) << pi[j]
    return out ^ v
for n in [4, 6, 8, 10, 12]:
    N = 1 << n; R = staircase_rowmotion(n); H = perm_pow(R, n); w = w_n(n); PC = np.array([bin(i).count("1") for i in range(N)])
    # closed form of O1
    lam_orbit = [0]; x = 0
    for _ in range(2 * n - 1): x = int(R[x]); lam_orbit.append(x)
    ok = True
    for j in range(0, n // 2 + 1):
        E = set(range(n - 2 * j + 2, n + 1, 2)) if j >= 1 else None
        pred_even = tuple(sorted(set(range(1, n + 1)) - E)) if j >= 1 else ()
        ok &= sset(lam_orbit[2 * j], n) == pred_even
        if 2 * j + 1 < 2 * n and j < n // 2:
            F = set(range(n - 2 * j + 1, n, 2)); pred_odd = tuple(sorted(set(range(1, n + 1)) - F)); ok &= sset(lam_orbit[2 * j + 1], n) == pred_odd
    bad = np.flatnonzero(w[H] != H[w]); ranks = Counter(PC[bad].tolist())
    print("n=%2d  |N| = %5d of %5d  O1 closed form ok=%s  w in C(H): %s  rank dist of N: %s" % (n, len(bad), N, ok, len(bad) == 0, dict(sorted(ranks.items()))))
    if len(bad):
        low = sorted(bad, key=lambda x: (PC[x], x))[:6]
        for x in low:
            print("     witness x=%-22s rank %d: Hx=%s  wx=%s  w(Hx)=%s  H(wx)=%s" % (sset(x, n), PC[x], sset(H[x], n), sset(w[x], n), sset(w[H[x]], n), sset(H[w[x]], n)))
        # is e_1 (minus at position 1 only) a witness? and single-minus points in general
        for p in range(1, n + 1):
            x = 1 << (p - 1)
            if w[H[x]] != H[w[x]]: print("     single-minus witness at position %d: x=%s Hx=%s H(wx)=%s w(Hx)=%s" % (p, sset(x, n), sset(H[x], n), sset(H[w[x]], n), sset(w[H[x]], n)))
    # commutation on O1
    print("     commute on O1: %s" % all(w[H[x]] == H[w[x]] for x in lam_orbit))

# ---- second pass: the orbit of e_p in minus-set and d-sequence form; R^3(e_p) = -e_{n-1-p}?; H(e_p) closed form
def dseq(x, n):
    plus = [p + 1 for p in range(n) if not (x >> p) & 1]
    return tuple(c - (k + 1) for k, c in enumerate(plus))
def Hpred(p, n):
    m = p - 1 if p <= n // 2 else n - p
    s = {1, 2} | set(range(4, 2 * m + 1, 2)) | set(range(2 * m + 3 if p <= n // 2 else 2 * m + 1, n, 2))
    return tuple(sorted(s))
print("\n==== orbits of e_p ====")
for n in [6, 8, 10, 12, 14]:
    N = 1 << n; R = staircase_rowmotion(n); H = perm_pow(R, n); PC = np.array([bin(i).count("1") for i in range(N)])
    r3 = all(int(perm_pow(R, 3)[1 << (p - 1)]) == (N - 1) ^ (1 << (n - 2 - p)) for p in range(1, n - 1))
    hp = all(sset(H[1 << (p - 1)], n) == Hpred(p, n) for p in range(2, n - 1))
    print("n=%2d  R^3(e_p) = -e_{n-1-p} for p=1..n-2: %s   H(e_p) closed form for p=2..n-2: %s" % (n, r3, hp))
    if n in (8, 12):
        x = 2  # e_2
        for j in range(2 * n):
            print("   R^%2d e_2 = %-28s d=%s  rank %d" % (j, sset(x, n), dseq(x, n), PC[x])); x = int(R[x])

# ---- third pass: the orbit of {3, n} (w(e_2) = -{3,n}) up to the half-turn, in d-form
print("\n==== orbits of {3, n} ====")
for n in [8, 10, 12, 14]:
    N = 1 << n; R = staircase_rowmotion(n); PC = np.array([bin(i).count("1") for i in range(N)])
    x = (1 << 2) | (1 << (n - 1))
    for j in range(n + 1):
        print("   n=%2d R^%2d {3,n} = %-30s d=%s" % (n, j, sset(x, n), dseq(x, n))); x = int(R[x])
    Hx = perm_pow(R, n)[(1 << 2) | (1 << (n - 1))]
    print("   n=%2d  2 in H({3,n}): %s ; H({3,n}) = %s" % (n, bool((Hx >> 1) & 1), sset(Hx, n)))
