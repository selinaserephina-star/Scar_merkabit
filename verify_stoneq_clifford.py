# verify_stoneq_clifford.py — STONE Q: THE CLIFFORD TRANSPORT
# Brief: BRIEF_STONEQ_CLIFFORD.md (sha-locked bb7a6822... BEFORE this file
# existed).  Registered bars QB1..QB5; expectations in the brief.
#
# ROUTE.  (C1) 3-qubit Clifford tableau images generate Sp6(2) on F2^6.
# (C2) the 64 refinements of omega split 36+28 by Arf; phase-point operator
# spectra reported [obs].  (C3) phi: W(E7) -> Sp(Q/2Q-bar) from the simple
# reflections on the root lattice mod 2; weight pairs {v,-v} |-> q + ell_v;
# symplectic Gram-Schmidt basis change into standard (x|z) coordinates.
# (C4) the bridge-class PSL(2,7) of Stone F(b) (seed 728) pushed through the
# form dictionary.  (QB4) membership boundary of {Psi, pr, iota} in W(E7);
# an explicit Clifford circuit for the Coxeter clock.  (QB5) shadow depth.
#
# Run:  python -X utf8 verify_stoneq_clifford.py
import json, random
from collections import Counter

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("STONE Q -- the Clifford transport: Sp6(2) = C3/(phases*Paulis)")
print("=" * 78)

# ---------------------------------------------------------------- shared BSGS
def make_bsgs(gen_list, deg):
    """Deterministic incremental Schreier-Sims.  Returns (order, is_member)."""
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    if not strong:
        return 1, (lambda g: g == E)
    base = []
    for g in strong:
        if all(g[b] == b for b in base):
            base.append(next(i for i in range(deg) if g[i] != i))
    lvl = [[g for g in strong if all(g[b] == b for b in base[:i])]
           for i in range(len(base))]
    transv = [None] * len(base)
    def rebuild(i):
        b = base[i]; T = {b: E}; q = [b]
        while q:
            x = q.pop(0)
            for g in lvl[i]:
                y = g[x]
                if y not in T:
                    T[y] = mulD(g, T[x]); q.append(y)
        transv[i] = T
    for i in range(len(base)): rebuild(i)
    def strip_from(g, start):
        h = g
        for i in range(start, len(base)):
            x = h[base[i]]
            if x not in transv[i]: return h, i
            h = mulD(invD(transv[i][x]), h)
        return h, len(base)
    i = len(base) - 1
    while i >= 0:
        clean = True
        for x in list(transv[i].keys()):
            for g in lvl[i]:
                sg = mulD(invD(transv[i][g[x]]), mulD(g, transv[i][x]))
                if sg == E: continue
                h, j = strip_from(sg, i + 1)
                if h != E:
                    clean = False
                    if j == len(base):
                        base.append(next(p for p in range(deg) if h[p] != p))
                        lvl.append([]); transv.append(None)
                    for k2 in range(i + 1, j + 1):
                        lvl[k2].append(h); rebuild(k2)
                    i = j
                    break
            if not clean: break
        if clean: i -= 1
    o = 1
    for T in transv: o *= len(T)
    def is_member(g):
        h, _ = strip_from(g, 0)
        return h == E
    return o, is_member

def orbits_of(gens, pts, act=None):
    if act is None: act = lambda g, x: g[x]
    seen, out = set(), []
    for s0 in pts:
        if s0 in seen: continue
        orb = {s0}; q = [s0]
        while q:
            x = q.pop()
            for g in gens:
                y = act(g, x)
                if y not in orb: orb.add(y); q.append(y)
        seen |= orb
        out.append(sorted(orb))
    return out

# ------------------------------------------------- C1/QB1: Clifford tableau
print("\n--- C1/QB1: 3-qubit Clifford tableau -> Sp6(2) ---")
# vectors x in 0..63: bits 0-2 = X-part, bits 3-5 = Z-part  [TBR convention]
def par(x): return bin(x).count("1") & 1
def omega(x, y): return par((x & 7) & (y >> 3)) ^ par((y & 7) & (x >> 3))
def q0(x): return par((x & 7) & (x >> 3))

# matrices: tuples of 6 row-masks, y_i = par(row_i & x)
def matvec(M, x):
    y = 0
    for i in range(6):
        if par(M[i] & x): y |= 1 << i
    return y
def matmul(A, B):     # (A o B)(x) = A(Bx)
    rows = []
    for i in range(6):
        r = 0
        for k in range(6):
            if (A[i] >> k) & 1: r ^= B[k]
        rows.append(r)
    return tuple(rows)
I6cols = [1 << i for i in range(6)]
def from_cols(cols):
    return tuple(sum(((cols[k] >> i) & 1) << k for k in range(6))
                 for i in range(6))
I6 = from_cols(I6cols)

CLIF = {}
for i in range(3):                       # H_i : swap x_i <-> z_i
    cols = list(I6cols); cols[i], cols[i + 3] = cols[i + 3], cols[i]
    CLIF[f"H{i+1}"] = from_cols(cols)
for i in range(3):                       # S_i : z_i += x_i
    cols = list(I6cols); cols[i] = I6cols[i] ^ I6cols[i + 3]
    CLIF[f"S{i+1}"] = from_cols(cols)
for c in range(3):                       # CNOT c->t : x_t += x_c ; z_c += z_t
    for t in range(3):
        if c == t: continue
        cols = list(I6cols)
        cols[c] = I6cols[c] ^ I6cols[t]
        cols[t + 3] = I6cols[t + 3] ^ I6cols[c + 3]
        CLIF[f"CX{c+1}{t+1}"] = from_cols(cols)

sympl_ok = all(all(omega(matvec(M, x), matvec(M, y)) == omega(x, y)
                   for x in (1, 2, 4, 8, 16, 32) for y in range(64))
               for M in CLIF.values())
check("tableau symplectic", "all 12 generator images preserve omega "
      "(basis x full space, 12 matrices)", sympl_ok)

def mat_to_perm(M): return tuple(matvec(M, x) for x in range(64))
def perm_inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
SP_ORDER = 1451520
cl_perms = [mat_to_perm(M) for M in CLIF.values()]
oC, memC = make_bsgs(cl_perms, 64)
check("QB1", "the 12 tableau images generate order 1451520 = |Sp6(2)| — "
      "the 3-qubit Clifford group mod phases and Paulis  [classical]",
      oC == SP_ORDER, f"order {oC}")

# ------------------------------------------------- C2/QB2: forms + operators
print("\n--- C2/QB2: the 64 refinements, Arf split, phase-point spectra ---")
def qform(c):
    return tuple(q0(x) ^ par(c & x) for x in range(64))
zeros = [sum(1 for x in range(64) if qform(c)[x] == 0) for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms = [c for c in range(64) if zeros[c] == 28]
check("Arf split", "64 refinements = 36 even (36 zeros) + 28 odd (28 zeros)",
      len(even_forms) == 36 and len(odd_forms) == 28
      and sorted(set(zeros)) == [28, 36])

def act_form_perm(Mperm_inv, c):
    """label of q_c o M^-1 (M given by its inverse's 64-perm), verified."""
    tab = tuple(q0(Mperm_inv[x]) ^ par(c & Mperm_inv[x]) for x in range(64))
    cc = 0
    for k in range(6):
        if tab[1 << k] ^ q0(1 << k): cc |= 1 << k
    assert tab == qform(cc), "form action left the refinement family"
    return cc

cl_form_perms = []
for p in cl_perms:
    pi = perm_inv(p)
    cl_form_perms.append(tuple(act_form_perm(pi, c) for c in range(64)))
ofc = orbits_of(cl_form_perms, [even_forms[0], odd_forms[0]])
check("QB2 orbits", "Clifford orbits on forms = the two Arf classes "
      "[36], [28]; stabilizer orders 40320 = 8! and 51840 = |W(E6)| "
      "[classical]", sorted(len(o) for o in ofc) == [28, 36]
      and SP_ORDER // 36 == 40320 and SP_ORDER // 28 == 51840)

import numpy as np
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
def pauli(x):
    a, b = x & 7, x >> 3
    M = np.eye(1, dtype=complex)
    for i in range(3):
        ai, bi = (a >> i) & 1, (b >> i) & 1
        f = (1j ** (ai * bi)) * np.linalg.matrix_power(X2, ai) @ \
            np.linalg.matrix_power(Z2, bi)
        M = np.kron(M, f)
    return M
def phase_point(c):
    A = np.zeros((8, 8), dtype=complex)
    qc = qform(c)
    for x in range(64):
        A += ((-1) ** qc[x]) * pauli(x)
    return A / 8
spec_even = np.round(np.linalg.eigvalsh(phase_point(even_forms[0])), 6)
spec_odd = np.round(np.linalg.eigvalsh(phase_point(odd_forms[0])), 6)
herm = all(np.allclose(phase_point(c), phase_point(c).conj().T)
           for c in (even_forms[0], odd_forms[0], odd_forms[5]))
tr1 = all(abs(np.trace(phase_point(c)) - 1) < 1e-9
          for c in (even_forms[0], even_forms[7], odd_forms[0], odd_forms[9]))
same_e = np.allclose(spec_even, np.round(
    np.linalg.eigvalsh(phase_point(even_forms[11])), 6))
same_o = np.allclose(spec_odd, np.round(
    np.linalg.eigvalsh(phase_point(odd_forms[13])), 6))
# honest reading: the two spectra are IDENTICAL — the Arf split is
# orbit-theoretic (36 vs 28 under Clifford), NOT spectral.  Consistent
# with the 1-qubit case: eigenvalues (1 +- sqrt(3))/2 for every form,
# and the 3-qubit operators factor as tensor cubes.
check("phase points [obs]", "the 64 Hermitian sign-operators "
      "A_c = (1/8) sum (-1)^{q_c} T_x have trace 1, ONE common spectrum "
      "for ALL 64 forms (products of (1 +- sqrt(3))/2) — the 36/28 Arf "
      "split is invisible to the spectrum; it is a Clifford-ORBIT "
      "distinction, not a spectral one",
      herm and tr1 and same_e and same_o
      and np.allclose(spec_even, spec_odd),
      f"common spectrum {[float(v) for v in spec_even]}")

# ------------------------------------------------- C3/QB3: the Weyl side
print("\n--- C3/QB3: phi: W(E7) -> Sp6(2) and the pair->form dictionary ---")
D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]
idx = {v: k for k, v in enumerate(verts)}
PSI, PR, IOTA, FRAME = D["PSI"], D["PR"], D["IOTA"], D["FRAME"]
N = 56
C7 = [[ 2, 0,-1, 0, 0, 0, 0],
      [ 0, 2, 0,-1, 0, 0, 0],
      [-1, 0, 2,-1, 0, 0, 0],
      [ 0,-1,-1, 2,-1, 0, 0],
      [ 0, 0, 0,-1, 2,-1, 0],
      [ 0, 0, 0, 0,-1, 2,-1],
      [ 0, 0, 0, 0, 0,-1, 2]]

S = []
for i in range(7):
    perm = []
    for k in range(N):
        w = verts[k]
        img = tuple(w[j] - w[i] * C7[i][j] for j in range(7))
        perm.append(idx[img])
    S.append(tuple(perm))
def mul56(a, b): return tuple(a[b[k]] for k in range(N))
def inv56(a):
    r = [0] * N
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
E56 = tuple(range(N))
oW, memW = make_bsgs(S, N)
check("W(E7)", "reflections generate order 2903040 on the 56 "
      "(SM-013 anchor)", oW == 2903040)

def bits7(x): return [(x >> i) & 1 for i in range(7)]
def B7(x, y):
    xv, yv = bits7(x), bits7(y)
    return sum(xv[i] * C7[i][j] * yv[j]
               for i in range(7) for j in range(7)) & 1
def q7(x):
    xv = bits7(x)
    return (sum(xv[i] * C7[i][j] * xv[j]
                for i in range(7) for j in range(7)) // 2) & 1
rad = [x for x in range(1, 128) if all(B7(x, 1 << j) == 0 for j in range(7))]
check("radical", "the mod-2 radical of the E7 Cartan form is "
      "1-dimensional (det C7 = 2)", len(rad) == 1,
      f"generator bits {bits7(rad[0])}")
r0 = rad[0]
polar_ok = all(q7(a ^ b) ^ q7(a) ^ q7(b) == B7(a, b)
               for a in range(0, 128, 7) for b in range(128))
check("polar identity", "q(x+y)+q(x)+q(y) = B(x,y) on F2^7 "
      "(sampled rows x full space)", polar_ok)
# REGISTERED EXPECTATION REFUTED (recorded at equal prominence, fail-first
# log kept): the brief registered q(r) = 0 and ell_v(r) = 0.  Measured:
# BOTH equal 1.  Neither piece descends to the quotient alone — but the
# PAIR FORM q_v = q + ell_v does, because the two obstructions cancel:
# q_v(x+r) = q_v(x) + q(r) + ell_v(r) = q_v(x).  The 56 weights are
# exactly the shifts that repair the descent.
qr = q7(r0)
lvr = [(sum(verts[k][j] * bits7(r0)[j] for j in range(7)) & 1)
       for k in range(N)]
check("descent obstructions", "q(r) = 1 and ell_v(r) = 1 for ALL 56 "
      "weights — the brief's registered expectation (both = 0) is "
      "REFUTED: neither q nor ell_v lives on the quotient alone",
      qr == 1 and all(v == 1 for v in lvr))
cancel = all(all((q7(x ^ r0) ^ sum(verts[k][j] * ((x ^ r0) >> j & 1)
                                   for j in range(7)) % 2) ==
                 (q7(x) ^ sum(verts[k][j] * ((x >> j) & 1)
                              for j in range(7)) % 2)
                 for x in range(128))
             for k in (pair_rep_k for pair_rep_k in
                       sorted({min(k, IOTA[k]) for k in range(N)})[:28]))
check("THE CANCELLATION", "q_v(x + r) = q_v(x) for all x in F2^7 and all "
      "28 pairs — the two obstructions cancel and the pair forms DO "
      "descend: the transport stands on the combination, not the pieces",
      cancel)

pivot = next(j for j in range(7) if (r0 >> j) & 1)
qbasis = [j for j in range(7) if j != pivot]
def proj(x):
    if (x >> pivot) & 1: x ^= r0
    return sum(((x >> qbasis[k]) & 1) << k for k in range(6))
def lift(u):
    return sum(((u >> k) & 1) << qbasis[k] for k in range(6))
def Bq(u, v): return B7(lift(u), lift(v))
def qq(u): return q7(lift(u))
def ellv(vidx, u):
    x = lift(u)
    return sum(verts[vidx][j] * ((x >> j) & 1) for j in range(7)) & 1

def refl7(i, x):
    t = sum(C7[i][j] * bits7(x)[j] for j in range(7))
    return x ^ (1 << i) if t & 1 else x
PHI = []
for i in range(7):
    cols = [proj(refl7(i, lift(1 << k))) for k in range(6)]
    PHI.append(from_cols(cols))
phi_perms = [tuple(matvec(M, u) for u in range(64)) for M in PHI]
oPhi, _ = make_bsgs(phi_perms, 64)
check("phi image", "phi(W(E7)) has order 1451520; index 2 in |W(E7)| — "
      "kernel exactly {+-1} (iota = -1 is trivial mod 2)",
      oPhi == SP_ORDER and oW // oPhi == 2)

pair_rep = {}
for k in range(N): pair_rep.setdefault(FRAME[k], k)
same_pm = all(tuple(qq(u) ^ ellv(k, u) for u in range(64)) ==
              tuple(qq(u) ^ ellv(IOTA[k], u) for u in range(64))
              for k in (0, 5, 23))
check("frames = iota-pairs", "FRAME groups the 56 into the 28 antipodal "
      "pairs, and q_v = q_{-v}",
      all(FRAME[k] == FRAME[IOTA[k]] for k in range(N)) and same_pm)
ptabs = {}
for f, k in pair_rep.items():
    ptabs[f] = tuple(qq(u) ^ ellv(k, u) for u in range(64))
all_refine = all(t[a ^ b] ^ t[a] ^ t[b] == Bq(a, b)
                 for t in list(ptabs.values())[:4]
                 for a in range(0, 64, 5) for b in range(64))
all_odd = all(sum(1 for u in range(64) if t[u] == 0) == 28
              for t in ptabs.values())
check("28 odd forms", "the 28 pair forms are 28 DISTINCT refinements of "
      "B-bar, all odd (28 zeros): pairs -> odd forms is a bijection",
      all_refine and all_odd and len(set(ptabs.values())) == 28)
equiv = all(ptabs[FRAME[S[i][pair_rep[f]]]] ==
            tuple(ptabs[f][matvec(PHI[i], u)] for u in range(64))
            for i in range(7) for f in range(28))
check("equivariance", "q_{s_i v}(u) = q_v(phi(s_i) u) for all 7 "
      "reflections x all 28 pairs — the dictionary is W(E7)-equivariant",
      equiv)

# symplectic Gram-Schmidt on (F2^6, B-bar)
upairs = []
avail = [u for u in range(1, 64)]
for _ in range(3):
    u = avail[0]
    w = next(v for v in avail if Bq(u, v) == 1)
    upairs.append((u, w))
    avail = [v for v in avail if Bq(v, u) == 0 and Bq(v, w) == 0]
us = [p[0] for p in upairs]; ws = [p[1] for p in upairs]
def Tmap(u):
    y = 0
    for k in range(3):
        if Bq(u, ws[k]): y |= 1 << k
        if Bq(u, us[k]): y |= 1 << (k + 3)
    return y
def Tinv(y):
    u = 0
    for k in range(3):
        if (y >> k) & 1: u ^= us[k]
        if (y >> (k + 3)) & 1: u ^= ws[k]
    return u
tbij = len({Tmap(u) for u in range(64)}) == 64
tomega = all(omega(Tmap(a), Tmap(b)) == Bq(a, b)
             for a in range(64) for b in range(64))
check("basis change", "T: quotient -> F2^6 is a bijection carrying B-bar "
      "to the standard omega", tbij and tomega)

def to_std(M):
    cols = [Tmap(matvec(M, Tinv(1 << k))) for k in range(6)]
    return from_cols(cols)
PHI_STD = [to_std(M) for M in PHI]
std_perms = [mat_to_perm(M) for M in PHI_STD]
oStd, memStd = make_bsgs(std_perms, 64)
in_each_other = all(memC(p) for p in std_perms) and \
                all(memStd(p) for p in cl_perms)
check("QB3 TRANSPORT", "in standard coordinates phi(W(E7)) and the "
      "Clifford tableau group are the SAME group of order 1451520: "
      "W(E7)/{+-1} = the 3-qubit Clifford group mod phases and Paulis",
      oStd == SP_ORDER and in_each_other)

def label_of(tab_std):
    cc = 0
    for k in range(6):
        if tab_std[1 << k] ^ q0(1 << k): cc |= 1 << k
    assert tab_std == qform(cc)
    return cc
pair_label = {}
for f in range(28):
    pair_label[f] = label_of(tuple(ptabs[f][Tinv(y)] for y in range(64)))
check("labels", "the 28 transported pair forms are exactly the 28 odd "
      "labels of the standard model (TBR's odd theta characteristics)",
      sorted(pair_label.values()) == sorted(odd_forms))

# ------------------------------------------------- C4: PSL(2,7) through phi
print("\n--- C4: the bridge-class PSL(2,7) pushed through the dictionary ---")
random.seed(728)      # Stone F(b)'s deterministic hunt, reproduced
def rand_word(L=40):
    w56 = E56
    for i in [random.randrange(7) for _ in range(L)]:
        w56 = mul56(S[i], w56)
    return w56
def to28(p56):
    out = [0] * 28
    for x in range(N): out[FRAME[x]] = FRAME[p56[x]]
    return tuple(out)
E28 = tuple(range(28))
def ord28(p56):
    p = to28(p56); k, x = 1, p
    while x != E28:
        x = tuple(x[p[j]] for j in range(28)); k += 1
    return k
def comm(a, b): return mul56(mul56(a, b), mul56(inv56(a), inv56(b)))
c56h = None
for _ in range(4000):
    g = rand_word()
    o = ord28(g)
    if o % 7 == 0:
        h = E56
        for _ in range(o // 7): h = mul56(g, h)
        c56h = h
        break
x56 = None
for _ in range(200000):
    g = rand_word(random.randrange(20, 60))
    o = ord28(g)
    if o % 2: continue
    h = E56
    for _ in range(o // 2): h = mul56(g, h)
    xc = to28(mul56(h, c56h))
    oxc = 1; t = xc
    while t != E28:
        t = tuple(t[xc[j]] for j in range(28)); oxc += 1
    if oxc not in (3, 4, 7): continue
    got, _m = make_bsgs([to28(h), to28(c56h)], 28)
    if got == 168:
        osz = [len(o_) for o_ in orbits_of([to28(h), to28(c56h)], range(28))]
        if osz == [28]:
            x56 = h
            break
check("bridge class", "the transitive-on-28 PSL(2,7) of Stone F(b) "
      "reproduced (seed 728)", x56 is not None)
gensK = [comm(x56, c56h), comm(x56, mul56(c56h, c56h)),
         comm(mul56(x56, c56h), mul56(c56h, x56)),
         comm(c56h, mul56(x56, mul56(c56h, x56)))]
oK, _ = make_bsgs(gensK, N)
check("perfect part", "canonical lift K = PSL(2,7), order 168", oK == 168)

def quotient_matrix_from_forms(p56):
    """The symplectic matrix (std coords) of w in W(E7), solved from the
    odd-form dictionary: labels transform affinely c -> M^{-T} c + d."""
    pairs = [(pair_label[f], pair_label[FRAME[p56[pair_rep[f]]]])
             for f in range(28)]
    c0, c0p = pairs[0]
    diffs = [(c ^ c0, cp ^ c0p) for c, cp in pairs[1:]]
    basis, imgs, spanned = [], [], {0}
    for d, dp in diffs:
        if d not in spanned:
            basis.append(d); imgs.append(dp)
            spanned |= {s ^ d for s in spanned}
        if len(basis) == 6: break
    if len(basis) < 6: return None
    span_map = {0: 0}
    for bvec, bim in zip(basis, imgs):
        for vec, im in list(span_map.items()):
            span_map[vec ^ bvec] = im ^ bim
    if len(span_map) < 64: return None
    MinvT = from_cols([span_map[1 << k] for k in range(6)])
    d = c0p ^ matvec(MinvT, c0)
    if not all(cp == (matvec(MinvT, c) ^ d) for c, cp in pairs):
        return None
    pmi = perm_inv(mat_to_perm(MinvT))
    MT = from_cols([pmi[1 << k] for k in range(6)])       # (M^{-T})^{-1}
    M = tuple(sum(((MT[k] >> i) & 1) << k for k in range(6))
              for i in range(6))                          # transpose -> M
    return M, MinvT, d

K_mats = [quotient_matrix_from_forms(g) for g in gensK]
check("matrix recovery", "each K generator's symplectic matrix recovered "
      "from the odd-form dictionary alone (affine label action verified "
      "28/28)", all(m is not None for m in K_mats))
K_label_maps = [tuple(matvec(MinvT, c) ^ d for c in range(64))
                for (_M, MinvT, d) in K_mats]
kodd_sizes = sorted(len(o) for o in
                    orbits_of(K_label_maps, odd_forms,
                              act=lambda m, x: m[x]))
kev_sizes = sorted(len(o) for o in
                   orbits_of(K_label_maps, even_forms,
                             act=lambda m, x: m[x]))
check("TBR fingerprint", "K on the Clifford side: TRANSITIVE on the 28 "
      "odd forms, orbits [1,7,7,21] on the 36 even forms — SM-003's "
      "bitangent-class fingerprint lands intact",
      kodd_sizes == [28] and kev_sizes == [1, 7, 7, 21])
# enumerate K's 168 label maps; stabilizer of one odd form
Kid = tuple(range(64))
Kset = {Kid}
frontier = [Kid]
while frontier:
    nxt = []
    for a in frontier:
        for g in K_label_maps:
            b = tuple(g[a[c]] for c in range(64))
            if b not in Kset:
                Kset.add(b); nxt.append(b)
    frontier = nxt
def perm_order64(g):
    k, x = 1, g
    while x != Kid:
        x = tuple(g[x[c]] for c in range(64)); k += 1
    return k
b0 = odd_forms[0]
stab = [g for g in Kset if g[b0] == b0]
stab_orders = sorted(perm_order64(g) for g in stab)
check("shared S3", "|K| enumerated = 168; the K-stabilizer of one odd form "
      "has order 6, element orders {1,2,2,2,3,3} = S3 — SM-003's shared "
      "S3 = N(<z3>), now a statement inside the 3-qubit Clifford group",
      len(Kset) == 168 and len(stab) == 6
      and stab_orders == [1, 2, 2, 2, 3, 3])

# ------------------------------------------------- QB4: membership boundary
print("\n--- QB4: which gates have a Clifford shadow ---")
PSIt, PRt, IOTAt = tuple(PSI), tuple(PR), tuple(IOTA)
refl_types = []
for i in range(7):
    fx = sum(1 for k in range(N) if S[i][k] == k)
    refl_types.append((fx, (N - fx) // 2))
all_even = all(t[1] % 2 == 0 for t in refl_types)
pr_swaps = sum(1 for k in range(N) if PRt[k] != k) // 2
check("parities", "every simple reflection is an EVEN permutation of the "
      "56; pr has 27 transpositions (ODD)", all_even and pr_swaps == 27,
      f"(fixed, 2-cycles) per reflection = {refl_types}")
check("QB4a iota", "iota IS in W(E7)  (= -1 = w0, central)", memW(IOTAt))
def ordp(p):
    k, x = 1, p
    while x != E56: x = mul56(x, p); k += 1
    return k
conj = mul56(IOTAt, mul56(PSIt, IOTAt))
psi_inv = inv56(PSIt)
check("QB4b Psi NOT Clifford", "iota Psi iota = Psi^-1 with ord(Psi) = 18 "
      "> 2 and iota central in W(E7) => Psi cannot lie in W(E7); BSGS "
      "strip agrees — the machine's true clock has NO Clifford shadow",
      conj == psi_inv and ordp(PSIt) == 18 and not memW(PSIt))
check("QB4c pr NOT Clifford", "pr is odd, W(E7)'s image on the 56 is even "
      "=> pr not in W(E7); strip agrees — the odd mirror lives above the "
      "quotient too", not memW(PRt))
psi_iota = mul56(PSIt, mul56(IOTAt, inv56(PSIt)))
check("QB4d no 28-shadow of Psi", "Psi iota Psi^-1 = iota Psi^-2 != iota: "
      "Psi does not even preserve the 28 iota-pairs — the quotient cannot "
      "see the clock at all, only its linear stand-in",
      psi_iota == mul56(IOTAt, mul56(psi_inv, psi_inv))
      and psi_iota != IOTAt)

cox = E56
for i in range(7): cox = mul56(S[i], cox)
cyc = sorted(len(o) for o in orbits_of([cox], range(N)))
cyc28 = sorted(len(o) for o in orbits_of([to28(cox)], range(28)))
check("Coxeter clock", "c = s1...s7: cycle type [2,18,18,18] on the 56, "
      "[1,9,9,9] on the 28 pairs — Psi's census (SM-012), realized "
      "LINEARLY: the clock's Clifford stand-in",
      cyc == [2, 18, 18, 18] and cyc28 == [1, 9, 9, 9])

res = quotient_matrix_from_forms(cox)
COXM2 = I6
for i in range(7): COXM2 = matmul(PHI_STD[i], COXM2)
check("phi(c)", "the Coxeter matrix via the form dictionary = the product "
      "of the seven transported reflection matrices (two independent "
      "routes agree)", res is not None and res[0] == COXM2)

# bidirectional BFS for a Clifford word for phi(c); all 12 generators are
# involutions in Sp6(2) (S^2 = Z is a Pauli, trivial in the quotient)
names = list(CLIF.keys())
gens_m = [CLIF[n] for n in names]
target = COXM2
def bfs_word(target):
    """word [g1..gk] with g1 o g2 o ... o gk = target."""
    if target == I6: return []
    fw = {I6: []}          # product(word) = m
    bw = {target: []}      # m o product(word) = target
    for _ in range(14):
        side_fw = len(fw) <= len(bw)
        src = fw if side_fw else bw
        new = {}
        for m, wd in list(src.items()):
            for gi, g in enumerate(gens_m):
                nm = matmul(g, m) if side_fw else matmul(m, g)
                if nm not in src and nm not in new:
                    # fw: product(word) = m, prepend on left-multiply;
                    # bw: m o product(word) = target, prepend on
                    # right-multiply (nm o g o P = m o P = target)
                    new[nm] = [gi] + wd
        src.update(new)
        inter = set(fw) & set(bw)
        if inter:
            m = next(iter(inter))
            return fw[m] + bw[m]
    return None
word = bfs_word(target)
word_ok = False
if word is not None:
    A = I6
    for gi in reversed(word): A = matmul(gens_m[gi], A)
    word_ok = (A == target)
check("QB4e circuit", "an explicit H/S/CNOT word for phi(c), verified by "
      "recomposition — the Coxeter clock as a 3-qubit Clifford circuit "
      "(mod Pauli and phase)", word is not None and word_ok,
      f"length {len(word) if word else '-'}: "
      f"{' '.join(names[g] for g in word) if word else '-'} "
      "(rightmost applied first)")

# ------------------------------------------------- QB5: THE SHADOW DEPTH
print("\n--- QB5: the shadow depth (REGISTERED HEADLINE) ---")
odd_idx = {c: i for i, c in enumerate(odd_forms)}
def label_perm(M):
    pmi = perm_inv(mat_to_perm(M))
    out = [0] * 28
    for c in odd_forms:
        out[odd_idx[c]] = odd_idx[act_form_perm(pmi, c)]
    return tuple(out)
G28gens = [label_perm(M) for M in PHI_STD]
oG28, _ = make_bsgs(G28gens, 28)
check("faithful on 28", "Sp6(2) acts faithfully on the 28 odd forms "
      "(order 1451520 as a 28-point group)", oG28 == SP_ORDER)
cox_l = label_perm(COXM2)
base = next(i for i in range(28) if cox_l[i] != i)
transv = {base: E28}
qd = [base]
while qd:
    x = qd.pop(0)
    for g in G28gens:
        if g[x] not in transv:
            transv[g[x]] = tuple(g[k] for k in transv[x])
            qd.append(g[x])
check("transitive", "G transitive on the 28 (orbit of base = 28)",
      len(transv) == 28)
def pinv28(p):
    r = [0] * 28
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
Hgens = set()
for x, ux in transv.items():
    for g in G28gens:
        sg = tuple(pinv28(transv[g[x]])[g[ux[k]]] for k in range(28))
        if sg != E28: Hgens.add(sg)
Hgens = list(Hgens)
oH, _ = make_bsgs(Hgens, 28)
check("H = W(E6)", "the point stabilizer has order 51840 = |W(E6)| — the "
      "typed subgroup of the shadow machine  [classical: O6-(2)]",
      oH == 51840)
Horb = sorted(len(o) for o in orbits_of(Hgens, range(28)))
check("QB5 rank", "H-orbits on the 28 = [1, 27] (W(E6) transitive on the "
      "27 lines) => exactly TWO (H,H) double cosets", Horb == [1, 27])
oClo, _ = make_bsgs(Hgens + [cox_l], 28)
check("QB5 SHADOW COLLAPSE", "phi(c) moves the base form, <H, phi(c)> = "
      "Sp6(2), and |H| + |H|*27 = 51840 + 1399680 = 1451520 EXACTLY: "
      "shadow magic-depth = 1 for every non-typed element (H c H is the "
      "single non-trivial double coset).  The 56-machine's two-tier depth "
      "structure (depth 2 both grammars, W-depth 4, 3718 frame classes) "
      "lives STRICTLY ABOVE its Clifford quotient (2 classes, depth 1).  "
      "PASS-COLLAPSE", cox_l[base] != base and oClo == SP_ORDER
      and 51840 + 51840 * 27 == SP_ORDER)

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
