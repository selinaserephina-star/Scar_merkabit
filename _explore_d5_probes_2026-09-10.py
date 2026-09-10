# free exploration (NOT sealed): D5 anomaly probes.
# (1) the clock's two free 8-orbits on the D5 half-spin; which survivors preserve / swap them.
# (2) the B4 spinor on the same 16 sign patterns: same poset? same rowmotion? W(B4) = 384; its I_k and C_k.
# Both boards built in e-coordinates from scratch (vectors, reflections, covers, rowmotion), no Cartan-label machine.
import os, itertools
from fractions import Fraction
from collections import Counter
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
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

# ---- D5 half-spin: even sign patterns of length 5
e = lambda i, n: tuple(Fraction(int(j == i)) for j in range(n))
D5_roots = [tuple(x - y for x, y in zip(e(i, 5), e(i + 1, 5))) for i in range(4)] + [tuple(x + y for x, y in zip(e(3, 5), e(4, 5)))]
D5_w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=5) if signs.count(-1) % 2 == 0]
W5, idx5, S5, R5, P5, leq5 = board(D5_w, D5_roots)
WD5 = closure(S5); print("D5 half-spin: N =", len(W5), " |W| =", len(WD5), " R type", ctype(R5), " |P| =", len(P5))
O = orbits(R5); print("R-orbits:", [len(o) for o in O])
orb_of = {x: i for i, o in enumerate(O) for x in o}
def orbit_action(g): return "preserves" if all(orb_of[g[x]] == orb_of[x] for x in range(16)) else ("swaps" if all(orb_of[g[x]] != orb_of[x] for x in range(16)) else "mixes")
def signed_perm(g, W, n):
    # recover the linear map from its action on the spanning weights (rational least squares by hand: use a basis of weights)
    import numpy as np
    V = np.array([[float(x) for x in w] for w in W]); GV = np.array([[float(x) for x in W[g[i]]] for i in range(len(W))])
    A, *_ = np.linalg.lstsq(V, GV, rcond=None); A = np.rint(A.T).astype(int)
    return ["%se%d" % ("+" if A[i][j] > 0 else "-", j + 1) for i in range(n) for j in range(n) if A[i][j] != 0]
w0 = tuple(idx5[tuple(-x for x in w[:4]) + (w[4],)] for w in W5)   # w0(D5) = -1 on e1..e4, +1 on e5
print("w0 = -(e1..e4):", orbit_action(w0), "the two orbits; in W:", w0 in WD5, " reverses R:", comp(comp(w0, R5), w0) == pinv(R5))
for k in (1, 2, 3, 4):
    Rk = ppow(R5, k); Rki = pinv(Rk)
    I = [g for g in WD5 if comp(comp(Rki, g), Rk) in WD5]; C = [g for g in WD5 if comp(g, Rk) == comp(Rk, g)]
    print("k = %d: |I| = %d |C| = %d" % (k, len(I), len(C)))
    for g in I:
        if g == tuple(range(16)): continue
        print("    %-9s %-9s %s  %s" % (ctype(g), orbit_action(g), "centralizer" if g in C else "extra      ", signed_perm(g, W5, 5)))
# ---- B4 spinor: all sign patterns of length 4; roots e_i - e_{i+1}, e_4
B4_roots = [tuple(x - y for x, y in zip(e(i, 4), e(i + 1, 4))) for i in range(3)] + [e(3, 4)]
B4_w = [tuple(H * s for s in signs) for signs in itertools.product((1, -1), repeat=4)]
W4, idx4, S4, R4, P4, leq4 = board(B4_w, B4_roots)
WB4 = closure(S4); print("\nB4 spinor: N =", len(W4), " |W| =", len(WB4), " R type", ctype(R4), " |P| =", len(P4))
# identify the two boards: D5 pattern -> first four coordinates
match = {i: idx4[w[:4]] for i, w in enumerate(W5)}
assert sorted(match.values()) == list(range(16))
R5_on_B4 = tuple(match[R5[[k for k, v in match.items() if v == j][0]]] for j in range(16))
print("D5 rowmotion transported to the B4 labelling equals B4 rowmotion:", R5_on_B4 == R4, " (or its inverse:", R5_on_B4 == pinv(R4), ")")
# W(B4) inside W(D5)?  transport W(B4) to D5 labelling
inv_match = {v: k for k, v in match.items()}
WB4_on_D5 = {tuple(inv_match[g[match[i]]] for i in range(16)) for g in WB4}
print("W(B4) transported into the D5 board lies inside W(D5):", WB4_on_D5 <= WD5, " |intersection| =", len(WB4_on_D5 & WD5))
for k in (1, 2, 3, 4):
    Rk = ppow(R4, k); Rki = pinv(Rk)
    I = [g for g in WB4 if comp(comp(Rki, g), Rk) in WB4]; C = [g for g in WB4 if comp(g, Rk) == comp(Rk, g)]
    print("B4 k = %d: |I| = %d |C| = %d  extra: %s" % (k, len(I), len(C), [ctype(g) + " " + str(signed_perm(g, W4, 4)) for g in I if g not in C]))

# ---- altitude of each clock power against W(B4) and W(D5); nearest elements
print("\naltitude nu(R^k) = min Hamming distance to a Weyl element (B4 board / D5 board):")
for k in range(1, 8):
    Rk4 = ppow(R4, k); Rk5 = ppow(R5, k)
    d4 = min(sum(1 for i in range(16) if g[i] != Rk4[i]) for g in WB4); d5 = min(sum(1 for i in range(16) if g[i] != Rk5[i]) for g in WD5)
    near5 = [g for g in WD5 if sum(1 for i in range(16) if g[i] != Rk5[i]) == d5]
    print("  k = %d: nu_B4 = %2d  nu_D5 = %2d  (#nearest in W(D5): %d%s)" % (k, d4, d5, len(near5), ("; e.g. " + str(signed_perm(near5[0], W5, 5))) if d5 <= 4 else ""))
# the same for E6 (27) and D6 spinor for comparison would need those boards; here: the correction R^4 = w . c, c = w^-1 R^4 on the D5 board
Rk5 = ppow(R5, 4); near = [g for g in WD5 if sum(1 for i in range(16) if g[i] != Rk5[i]) == min(sum(1 for i in range(16) if g[i] != Rk5[i]) for g in WD5)]
for g in near[:3]:
    c = comp(pinv(g), Rk5); print("  R^4 = w . c with w =", signed_perm(g, W5, 5), " c type", ctype(c), " c moves", sum(1 for i in range(16) if c[i] != i), "points; c in W:", c in WD5)
