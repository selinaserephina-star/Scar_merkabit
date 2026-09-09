# free exploration (NOT sealed): the D5 half-spin anomaly of Stone AT.
# The 2^(n-1) half-spin weights of D_n are the even sign patterns of length n = F2^(n-1) (translate by even vectors, permute coords).
# Is rowmotion AFFINE over F2 on this space?  Which powers are?  What are the extra survivors as signed permutations?
import os, itertools
from fractions import Fraction
from collections import Counter
import numpy as np
os.chdir(r"C:\Users\selin\OneDrive\Desktop\Scar_merkabit")
aqsrc = open("verify_stone_aq_rush_shi_defect.py", encoding="utf-8").read()
start = aqsrc.index("# ---------------------------------------------------------------- Cartan matrices"); end = aqsrc.index("# ---------------------------------------------------------------- the cases")
W_CAP = 400000
exec(compile(aqsrc[start:end], "aq", "exec"))
def tcomp(p, q): return tuple(p[q[i]] for i in range(len(p)))
def tinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def tpow(p, e):
    x = tuple(range(len(p)))
    for _ in range(e): x = tcomp(p, x)
    return x
def spin_vectors(M, n):
    # recover the +-1/2 coordinates of each half-spin weight from its Dynkin labels: w = sum_i label_i * omega_i, omega in e-coords
    # fundamental coweights of D_n in e-coordinates: omega_i = e_1+..+e_i (i <= n-2), omega_{n-1} = (e_1+..+e_{n-1} - e_n)/2, omega_n = (e_1+..+e_n)/2
    om = []
    for i in range(1, n - 1): om.append([Fraction(1) if j < i else Fraction(0) for j in range(n)])
    om.append([Fraction(1, 2)] * (n - 1) + [Fraction(-1, 2)]); om.append([Fraction(1, 2)] * n)
    vecs = []
    for w in M.W:
        v = [sum(w[i] * om[i][j] for i in range(n)) for j in range(n)]
        vecs.append(tuple(v))
    return vecs
def sign_pattern(v): return tuple(0 if x > 0 else 1 for x in v)   # +1/2 -> 0, -1/2 -> 1
def is_affine(perm, pats, idx):
    # perm on indices; affine over F2 iff perm(x)+perm(y)+perm(z) = perm(x+y+z) for all x,y,z  (as sign patterns)
    n = len(pats[0])
    def add(*ps): return tuple(sum(c) % 2 for c in zip(*ps))
    for a in range(len(pats)):
        for b in range(a, len(pats)):
            for c in range(b, len(pats)):
                s = add(pats[a], pats[b], pats[c])
                if s not in idx: return False
                if add(pats[perm[a]], pats[perm[b]], pats[perm[c]]) != pats[perm[idx[s]]]: return False
    return True
for n, k in [(4, 4), (5, 5), (6, 6), (7, 7)]:
    M = Minuscule("D", n, k); h = coxeter_number("D", n)
    vecs = spin_vectors(M, n); pats = [sign_pattern(v) for v in vecs]; idx = {p: i for i, p in enumerate(pats)}
    assert len(idx) == M.N and all(sum(p) % 2 == 0 for p in pats), "not the even code"
    R = tuple(M.R)
    aff = [j for j in range(1, h) if is_affine(tpow(R, j), pats, idx)]
    print("D%d half-spin: N = %d = F2^%d; rowmotion affine over F2 for powers j in %s (of 1..%d)" % (n, M.N, n - 1, aff, h - 1))
    if n == 5:
        Ws = M.enumerate_W()
        # the anomalous survivors at k = 3, 4, 5 and the centralizers, as signed permutations
        for kk in (3, 4):
            Rk = tpow(R, kk); Rki = tinv(Rk)
            I = [g for g in Ws if tcomp(tcomp(Rki, g), Rk) in Ws]
            C = [g for g in Ws if tcomp(g, Rk) == tcomp(Rk, g)]
            print("  k = %d: |I| = %d, |C| = %d" % (kk, len(I), len(C)))
            for g in I:
                if g == tuple(range(M.N)): continue
                # linear map on e-coords: find signed permutation: image of e_i read from the action on vectors
                # g(v) = vecs[g[idx]]; solve for the matrix via the vectors (they span R^5)
                V = np.array([[float(x) for x in v] for v in vecs]); GV = np.array([[float(x) for x in vecs[g[i]]] for i in range(M.N)])
                A, *_ = np.linalg.lstsq(V, GV, rcond=None); A = np.rint(A.T).astype(int)   # g(v) = A v
                sp = ["%se%d" % ("+" if A[i][j] > 0 else "-", j + 1) for i in range(n) for j in range(n) if A[i][j] != 0]
                conj = tcomp(tcomp(Rki, g), Rk)
                print("     %s  commutes with R^k: %s  (R^-k g R^k = itself: %s); signed perm e_i -> %s" % (
                    " ".join("%d^%d" % (l, m) for l, m in sorted(Counter(M.cyc(list(g))).items(), reverse=True)), g in C, conj == g, sp))
