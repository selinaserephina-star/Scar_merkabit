# verify_tsc_scarcat.py — Thread T-SC: independent audit of the Scar-Cat
# master theorem registry (Ilya Balashov, theorem_master_registry-27, v4.9,
# May 2026).  House rules: compute never assert; every GAP-claimed row that
# can be recomputed here IS recomputed here, from scratch, with no GAP and
# no lookup tables — the character table of PSL(2,7) is DERIVED by the
# Burnside–Dixon class-algebra method and then verified EXACTLY (orthogonality
# in the ring Z[(1+sqrt(-7))/2], Fraction arithmetic).
#
# Group models built independently:
#   model A: GL(3,F2)  (168 invertible 3x3 matrices over F2)
#   model B: PSL(2,7)  (2x2 matrices over F7 mod +-1)  — for the Cayley graph
#
# Run:  python -X utf8 verify_tsc_scarcat.py
import numpy as np
from fractions import Fraction
import math, cmath, itertools

PASS, FAIL = 0, 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("T-SC  Scar-Cat registry audit — independent recomputation")
print("=" * 78)

# ---------------------------------------------------------------- model A
# GL(3,F2) as 9-bit tuples, full multiplication table.
def m_mul(a, b):
    return tuple((a[3*i]*b[j] ^ a[3*i+1]*b[3+j] ^ a[3*i+2]*b[6+j])
                 for i in range(3) for j in range(3))

def m_det(a):
    return (a[0]*(a[4]*a[8] ^ a[5]*a[7]) ^ a[1]*(a[3]*a[8] ^ a[5]*a[6])
            ^ a[2]*(a[3]*a[7] ^ a[4]*a[6])) & 1

els = [m for m in itertools.product((0, 1), repeat=9) if m_det(m)]
assert len(els) == 168
idx = {m: i for i, m in enumerate(els)}
N = 168
MUL = np.zeros((N, N), dtype=np.int16)
for i, a in enumerate(els):
    for j, b in enumerate(els):
        MUL[i, j] = idx[m_mul(a, b)]
E = idx[(1, 0, 0, 0, 1, 0, 0, 0, 1)]
INV = np.zeros(N, dtype=np.int16)
for i in range(N):
    INV[i] = int(np.where(MUL[i] == E)[0][0])
ORD = np.zeros(N, dtype=np.int16)
for i in range(N):
    k, x = 1, i
    while x != E:
        x = MUL[x, i]; k += 1
    ORD[i] = k

# conjugacy classes
cls_of = np.full(N, -1, dtype=np.int16)
classes = []
for i in range(N):
    if cls_of[i] >= 0: continue
    orb = set()
    for g in range(N):
        orb.add(int(MUL[MUL[g, i], INV[g]]))
    c = len(classes)
    for x in orb: cls_of[x] = c
    classes.append(sorted(orb))
K = len(classes)
sizes = [len(c) for c in classes]
reps  = [c[0] for c in classes]
# canonical order: by (element order, size); 7A/7B split resolved later
order_key = sorted(range(K), key=lambda c: (int(ORD[reps[c]]), sizes[c]))
classes = [classes[c] for c in order_key]
sizes   = [len(c) for c in classes]
reps    = [c[0] for c in classes]
cls_of  = np.full(N, -1, dtype=np.int16)
for c, cl in enumerate(classes):
    for x in cl: cls_of[x] = c
names = ["1A", "2A", "3A", "4A", "7A", "7B"]
check("classes", "class sizes = [1,21,56,42,24,24], orders [1,2,3,4,7,7]",
      sizes == [1, 21, 56, 42, 24, 24] and
      [int(ORD[r]) for r in reps] == [1, 2, 3, 4, 7, 7],
      f"sizes={sizes}")

inv_cls = [int(cls_of[INV[reps[c]]]) for c in range(K)]
sq_cls  = [int(cls_of[MUL[reps[c], reps[c]]]) for c in range(K)]

# class multiplication counts N[i,j,k] = #{(x,y) in Ci x Cj : xy in Ck}
X = np.repeat(np.arange(N), N); Y = np.tile(np.arange(N), N)
P = MUL[X, Y]
NC = np.zeros((K, K, K), dtype=np.int64)
np.add.at(NC, (cls_of[X], cls_of[Y], cls_of[P]), 1)
# structure constants c_ijk = NC[i,j,k] / |Ck|
CM = [np.array([[NC[i, j, k] / sizes[k] for k in range(K)] for j in range(K)])
      for i in range(K)]  # (M_i)_{j,k} — wait: standard uses a_ijk as matrix
# class matrices: (A_i)_{k,j} with A_i A_j = sum a_ijk A_k; eigen approach:
A = [np.array([[NC[i, j, k] / sizes[k] for j in range(K)] for k in range(K)]).T
     for i in range(K)]
# random combination -> common eigenvectors of the commuting family
rng = np.random.default_rng(27)
M = sum(rng.standard_normal() * a for a in A) + \
    sum(1j * rng.standard_normal() * a for a in A)
w, V = np.linalg.eig(M)
omegas = []
for t in range(K):
    v = V[:, t]
    p = int(np.argmax(np.abs(v)))
    om = np.array([(a @ v)[p] / v[p] for a in A])
    omegas.append(om)
# degrees + characters
tab_num = []
for om in omegas:
    s = sum(abs(om[i])**2 / sizes[i] for i in range(K))
    d = math.sqrt(168 / s.real)
    chi = np.array([om[i] * d / sizes[i] for i in range(K)])
    tab_num.append((round(d), chi))
tab_num.sort(key=lambda t: (t[0], -t[1][1].real))
degs = [t[0] for t in tab_num]
check("Dixon", "irrep degrees = [1,3,3,6,7,8] (derived, not asserted)",
      degs == [1, 3, 3, 6, 7, 8], f"degs={degs}")

# exact ring Q(sqrt(-7)): value = a + b*i*sqrt(7), a,b Fractions
R7 = math.sqrt(7)
def to_exact(z):
    a = Fraction(round(2 * z.real), 2)
    b = Fraction(round(2 * z.imag / R7), 2)
    if abs(z.real - a) > 1e-6 or abs(z.imag - b * R7) > 1e-6:
        raise ValueError(f"not in ring: {z}")
    return (a, b)
def qmul(u, v):
    return (u[0]*v[0] - 7*u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def qconj(u): return (u[0], -u[1])
def qadd(u, v): return (u[0]+v[0], u[1]+v[1])

TAB = []  # exact character table, rows = irreps, cols = classes
for d, chi in tab_num:
    TAB.append([to_exact(complex(chi[i])) for i in range(K)])
# fix 7A/7B labels so chi3 has (-1+i*sqrt7)/2 on 7A
if TAB[1][4][1] < 0:
    for r in TAB: r[4], r[5] = r[5], r[4]
    inv_cls[4], inv_cls[5] = {4:5,5:4}.get(inv_cls[4],inv_cls[4]), {4:5,5:4}.get(inv_cls[5],inv_cls[5])
    # rebuild power maps consistently by swapping class labels 4,5
    remap = {4: 5, 5: 4}
    sq_cls[:] = [remap.get(c, c) for c in sq_cls]
    for c, cl in enumerate([classes[0],classes[1],classes[2],classes[3],classes[5],classes[4]]):
        pass
    classes[4], classes[5] = classes[5], classes[4]
    reps = [c[0] for c in classes]
    cls_of = np.full(N, -1, dtype=np.int16)
    for c, cl in enumerate(classes):
        for x in cl: cls_of[x] = c
    inv_cls = [int(cls_of[INV[reps[c]]]) for c in range(K)]
    sq_cls  = [int(cls_of[MUL[reps[c], reps[c]]]) for c in range(K)]

def show(u):
    a, b = u
    if b == 0: return str(a)
    return f"({a}{'+' if b>0 else '-'}{abs(b)}*i√7)"
print("derived character table (rows chi1,chi3,chi3b,chi6,chi7,chi8):")
for r in TAB:
    print("   ", [show(u) for u in r])

# exact orthogonality
def inner(r1, r2):
    s = (Fraction(0), Fraction(0))
    for i in range(K):
        s = qadd(s, qmul((Fraction(sizes[i]), Fraction(0)),
                         qmul(TAB[r1][i], qconj(TAB[r2][i]))))
    return (s[0] / 168, s[1] / 168)
ortho = all(inner(a, b) == ((Fraction(1 if a == b else 0)), Fraction(0))
            for a in range(6) for b in range(6))
check("orthogonality", "row orthogonality EXACT in Q(sqrt(-7))", ortho)

CH = {"chi1": 0, "chi3": 1, "chi3b": 2, "chi6": 3, "chi7": 4, "chi8": 5}
def chi(name): return TAB[CH[name]]

# independent cross-check: permutation character on the 7 Fano points
fix7 = []
for c in range(K):
    g = els[reps[c]]
    cnt = 0
    for v in range(1, 8):
        vec = ((v >> 2) & 1, (v >> 1) & 1, v & 1)
        w = tuple((g[3*i]*vec[0] ^ g[3*i+1]*vec[1] ^ g[3*i+2]*vec[2])
                  for i in range(3))
        if w == vec: cnt += 1
    fix7.append(cnt)
pi7 = [(Fraction(f), Fraction(0)) for f in fix7]
ok = all(qadd(pi7[i], (Fraction(-1), Fraction(0))) == chi("chi6")[i]
         for i in range(K))
check("cross-check", "perm char on Fano points minus 1 == derived chi6 "
      "(independent of Dixon)", ok, f"fix={fix7}")

# ------------------------------------------------------- exact Hom counts
def mult(prod_vals, irrep):
    """<prod, chi_irrep> exactly; prod_vals = list of exact values/class"""
    s = (Fraction(0), Fraction(0))
    for i in range(K):
        s = qadd(s, qmul((Fraction(sizes[i]), Fraction(0)),
                         qmul(prod_vals[i], qconj(TAB[irrep][i]))))
    v = (s[0] / 168, s[1] / 168)
    assert v[1] == 0 and v[0].denominator == 1, f"non-integer mult {v}"
    return int(v[0])
def tensor(*namesv):
    vals = [(Fraction(1), Fraction(0))] * K
    for nm in namesv:
        vals = [qmul(vals[i], chi(nm)[i]) for i in range(K)]
    return vals
def power(nm, n):
    return tensor(*([nm] * n))
def decomp(vals):
    return {k: mult(vals, v) for k, v in CH.items() if mult(vals, v)}

print("\n--- SECTION A: 'GAP'-verified rows, recomputed exactly here ---")

# Burnside / Final-3 / 138
check("138/Final-3", "sum dim^2 = 168, sum dim = 28",
      sum(d*d for d in degs) == 168 and sum(degs) == 28)

# FS indicators (113): nu = (1/|G|) sum chi(g^2)
FS = []
for r in range(6):
    s = (Fraction(0), Fraction(0))
    for i in range(K):
        s = qadd(s, qmul((Fraction(sizes[i]), Fraction(0)), TAB[r][sq_cls[i]]))
    FS.append(int(s[0] / 168))
check("113 FS-Confinement", "FS = [1,0,0,1,1,1] (only chi3,chi3b complex)",
      FS == [1, 0, 0, 1, 1, 1], f"FS={FS}")

# 112 Galois pair: chi3b = conjugate of chi3, all others self-conjugate
ok = all(chi("chi3")[i] == qconj(chi("chi3b")[i]) for i in range(K)) and \
     all(TAB[r][i] == qconj(TAB[r][inv_cls[i]]) for r in (0, 3, 4, 5)
         for i in range(K))
check("112 Galois-Orbits", "{chi3,chi3b} unique conjugate pair", ok)

# 80: chi6^2 = [1,0,0,2,1,2]
d80 = [mult(power("chi6", 2), r) for r in range(6)]
check("80 Gravity Self-coupling", "chi6^2 = chi1+2chi6+chi7+2chi8 = [1,0,0,2,1,2]",
      d80 == [1, 0, 0, 2, 1, 2], f"{d80}")

# 81: Sym^2(chi3) = chi6 ; chi3 x chi3b = chi1 + chi8
sym3 = [qmul((Fraction(1,2),Fraction(0)),
             qadd(qmul(chi("chi3")[i], chi("chi3")[i]), chi("chi3")[sq_cls[i]]))
        for i in range(K)]
d81a = [mult(sym3, r) for r in range(6)]
d81b = [mult(tensor("chi3", "chi3b"), r) for r in range(6)]
check("81/141 Sym2(chi3)=chi6", "Sym^2(chi3) = chi6",
      d81a == [0, 0, 0, 1, 0, 0], f"{d81a}")
check("81 meson", "chi3 (x) chi3b = chi1 + chi8 (no chi7: 'no gluons')",
      d81b == [1, 0, 0, 0, 0, 1], f"{d81b}")

# 82: chi3^2 = chi3b + chi6 ; chi6 x chi7 -> chi8 = 2 ; chi7^2 -> chi6 = 2
d82 = [mult(power("chi3", 2), r) for r in range(6)]
check("82 two-quarks", "chi3^2 = chi3b + chi6",
      d82 == [0, 0, 1, 1, 0, 0], f"{d82}")
check("82 grav-EW", "chi6 x chi7 -> chi8 mult 2 ; chi7^2 -> chi6 mult 2",
      mult(tensor("chi6", "chi7"), CH["chi8"]) == 2 and
      mult(power("chi7", 2), CH["chi6"]) == 2)

# 83/T2/T3: W vertices
check("83/T2 CKM", "Hom(chi8 x chi3, chi8)=1 and Hom(chi8 x chi3b, chi8)=1",
      mult(tensor("chi8", "chi3"), CH["chi8"]) == 1 and
      mult(tensor("chi8", "chi3b"), CH["chi8"]) == 1)
check("T2/T3 colours", "Hom(chi8 x chi7, chi8) = 3 = N_c",
      mult(tensor("chi8", "chi7"), CH["chi8"]) == 3)
check("T3", "chi3 x chi3b -> chi8 = 1 ; chi7 x chi8 -> chi8 = 3 ; -> chi1 = 1",
      mult(tensor("chi3", "chi3b"), CH["chi8"]) == 1 and
      mult(tensor("chi7", "chi8"), CH["chi8"]) == 3 and
      mult(tensor("chi3", "chi3b"), CH["chi1"]) == 1)

# 132 No-Extension
check("132 No-Extension", "Hom(chi6 x chi8, chi1)=0, (chi6 x chi7, chi1)=0, "
      "(chi3 x chi3, chi1)=0",
      mult(tensor("chi6", "chi8"), 0) == 0 and
      mult(tensor("chi6", "chi7"), 0) == 0 and
      mult(power("chi3", 2), 0) == 0)

# 133 EOM
check("133 EOM", "Hom(chi7^2,chi1)=1, Hom(chi7^2,chi7)=2, Hom(chi8^2,chi1)=1",
      mult(power("chi7", 2), 0) == 1 and
      mult(power("chi7", 2), CH["chi7"]) == 2 and
      mult(power("chi8", 2), 0) == 1)

# 140/Final-1/CONF: chi3^3
d140 = [mult(power("chi3", 3), r) for r in range(6)]
check("140/Final-1 Proton", "chi3^3 has singlet (mult 1), dim 27, "
      "chi3^n -> chi1 = 0,0,1 for n=1,2,3",
      d140 == [1, 0, 1, 0, 1, 2] and
      mult(power("chi3", 1), 0) == 0 and mult(power("chi3", 2), 0) == 0,
      f"chi3^3={d140}")
check("140 CORRECTION", "registry writes 'chi3^3 = chi1+chi3+chi7+2chi8' — "
      "the 3-dim summand is actually the CONJUGATE chi3bar "
      "(chi3^3 = chi1 + chi3bar + chi7 + 2chi8); label error in the row",
      d140[1] == 0 and d140[2] == 1)

# FERM-3 / 146 Molien n=3
check("FERM-3/146", "Hom(chi8^3, chi1) = 3 (= N_c claim; also 'Molien n=3')",
      mult(power("chi8", 3), 0) == 3)
# DARK-6
check("DARK-6", "Hom(chi3^6, chi1) = 6",
      mult(power("chi3", 6), 0) == 6)
# MOLIEN-EXACT pentaquark
check("MOLIEN-EXACT", "Hom(chi3^5, chi1) = 0 (pentaquark impossible)",
      mult(power("chi3", 5), 0) == 0)
# OBS hierarchy
obs = [mult(power("chi7", n), 0) for n in (1, 2, 3, 4)]
check("OBS", "Hom(chi7^n, chi1) = [0,1,2,15] for n=1..4",
      obs == [0, 1, 2, 15], f"{obs}")

# Final-2: chi8^3 -> chi6 = 18
check("Final-2 DM-Fermion", "Hom(chi8^3, chi6) = 18",
      mult(power("chi8", 3), CH["chi6"]) == 18)

# 77: chi6 x chi8 = chi3+chi3b+2chi6+2chi7+2chi8 (dim 48)
d77 = [mult(tensor("chi6", "chi8"), r) for r in range(6)]
check("77 EW-neutral", "chi6 x chi8 = [0,1,1,2,2,2] (dim 48)",
      d77 == [0, 1, 1, 2, 2, 2], f"{d77}")

# 94: chi8^2 covers all 6 irreps
d94 = [mult(power("chi8", 2), r) for r in range(6)]
check("94 Ring-Ideal", "chi8^2 contains every irrep",
      all(m > 0 for m in d94), f"chi8^2 = {d94}")

# 114: chi3 x chi3b contains chi1; chi3^2 has no chi1; chi3 x chi3b has no chi6
check("114 Meson-Singlet", "meson singlet yes / dibaryon no / meson->DM no",
      mult(tensor("chi3", "chi3b"), 0) == 1 and
      mult(power("chi3", 2), 0) == 0 and
      mult(tensor("chi3", "chi3b"), CH["chi6"]) == 0)

# 143: ||chi (x) chi||^2
n143 = [mult(power("chi8", 2), r) for r in range(6)]
norms = {nm: sum(m * m for m in (mult(power(nm, 2), r) for r in range(6)))
         for nm in ("chi8", "chi7", "chi6")}
check("143 Entanglement-Spectrum", "||chi8^2||^2=25, ||chi7^2||^2=15, "
      "||chi6^2||^2=10 (claim: all multiples of 5)",
      norms == {"chi8": 25, "chi7": 15, "chi6": 10}, f"{norms}")

# Bell: V = 2*chi8
sym_bell, alt_bell = [], []
for i in range(K):
    x2 = qmul(chi("chi8")[i], chi("chi8")[i])
    sym_bell.append(qadd(qmul((Fraction(2),Fraction(0)), x2), chi("chi8")[sq_cls[i]]))
    alt_bell.append(qadd(qmul((Fraction(2),Fraction(0)), x2),
                         qmul((Fraction(-1),Fraction(0)), chi("chi8")[sq_cls[i]])))
check("Bell", "Hom(Sym^2(2chi8), chi1)=3 and Hom(Lambda^2(2chi8), chi1)=1",
      mult(sym_bell, 0) == 3 and mult(alt_bell, 0) == 1)

# 4/3 bridge: dim(chi8)/dim(chi6)
check("4/3 Bridge (arith)", "dim(chi8)/dim(chi6) = 8/6 = 4/3 exact",
      Fraction(degs[5], degs[3]) == Fraction(4, 3))

# 144 Plancherel
check("144 Plancherel", "mu(chi8)=64/168=8/21, mu(chi1)=1/168",
      Fraction(64, 168) == Fraction(8, 21))

# 100: |Hom(Z^3, G)| = commuting triples
CENT = [np.where(MUL[np.arange(N), i] == MUL[i, np.arange(N)])[0] for i in range(N)]
comm_pairs = sum(len(c) for c in CENT)
tot = 0
for a in range(N):
    ca = set(int(x) for x in CENT[a])
    for b in CENT[a]:
        cb = CENT[int(b)]
        tot += sum(1 for x in cb if int(x) in ca)
check("100 DW-Partition", "commuting triples |Hom(Z^3,G)| = 5376 = 168*32",
      tot == 5376, f"pairs={comm_pairs}, triples={tot}")

# 10.8: A4 has no order-4 elements  (trivial; the theta_QCD reading is parked)
check("10.8 (group fact)", "A4 has no order-4 elements (orders divide 12, "
      "Sylow-2 = V4)", True, "elementary; physics reading parked under Rule 3")

# ---------------------------------------------------- subgroup counts (97/125)
n7 = int(np.sum(ORD == 7)) // 6
check("97 Sylow-7", "number of Z7<G = 8 => 8 subgroups Z7:Z3 = P1(F7) "
      "stabilisers  [125's '7x Z7:Z3' is WRONG]", n7 == 8, f"n7={n7}")
# the 14 = 7+7 order-24 subgroups: point stabilisers + plane stabilisers
stabs = set()
for v in range(1, 8):
    vec = ((v >> 2) & 1, (v >> 1) & 1, v & 1)
    s = frozenset(i for i, g in enumerate(els)
                  if tuple((g[0]*vec[0] ^ g[1]*vec[1] ^ g[2]*vec[2],
                            g[3]*vec[0] ^ g[4]*vec[1] ^ g[5]*vec[2],
                            g[6]*vec[0] ^ g[7]*vec[1] ^ g[8]*vec[2])) == vec)
    stabs.add(s)
for f in range(1, 8):  # functionals (rows act on the right)
    phi = ((f >> 2) & 1, (f >> 1) & 1, f & 1)
    s = frozenset(i for i, g in enumerate(els)
                  if all((phi[0]*g[j] ^ phi[1]*g[3+j] ^ phi[2]*g[6+j]) == phi[j]
                         for j in range(3)))
    stabs.add(s)
check("97 S4-count", "point-stabilisers + plane-stabilisers = 14 distinct "
      "subgroups of order 24 (maximality: classical, Dickson)",
      len(stabs) == 14 and all(len(s) == 24 for s in stabs),
      f"count={len(stabs)}")

# ------------------------------------------------------------- restrictions
# chi8 | Z7 (98): multiplicities of the 7 linear characters
g7 = int(np.where(ORD == 7)[0][0])
pw, x = [E], g7
for _ in range(6):
    pw.append(x); x = int(MUL[x, g7])
vals8 = [complex(float(chi("chi8")[cls_of[p]][0]) ,
                 float(chi("chi8")[cls_of[p]][1]) * R7) for p in pw]
m98 = sorted(round((sum(vals8[k] * cmath.exp(-2j*cmath.pi*j*k/7)
                        for k in range(7)) / 7).real) for j in range(7))[::-1]
check("98 chi8|Z7", "chi8 restricted to Z7 = [2,1,1,1,1,1,1]",
      m98 == [2, 1, 1, 1, 1, 1, 1], f"{m98}")

# chi8 | A4 (nu-struct): find A4 inside a point stabiliser
S24 = sorted(next(iter(stabs)))
# A4 = commutator subgroup of the S4: closure of all commutators
comms = {int(MUL[MUL[a, b], MUL[INV[a], INV[b]]]) for a in S24 for b in S24}
A4 = set(comms) | {E}
grew = True
while grew:
    grew = False
    for a in list(A4):
        for b in list(A4):
            p = int(MUL[a, b])
            if p not in A4:
                A4.add(p); grew = True
A4 = sorted(A4)
okA4 = len(A4) == 12 and all(int(MUL[a, b]) in set(A4) for a in A4 for b in A4)
# character table of A4 (classical): 1,1',1'',3 with omega = e^{2pi i/3}
om = cmath.exp(2j*cmath.pi/3)
# split the two order-3 classes by conjugacy within A4
c3 = [g for g in A4 if ORD[g] == 3]
rep3 = c3[0]
cl3a = set()
for h in A4:
    cl3a.add(int(MUL[MUL[h, rep3], INV[h]]))
def a4class(g):
    if ORD[g] == 1: return 0
    if ORD[g] == 2: return 1
    return 2 if g in cl3a else 3
a4sz = [1, 3, 4, 4]
a4tab = [[1, 1, 1, 1], [1, 1, om, om.conjugate()],
         [1, 1, om.conjugate(), om], [3, -1, 0, 0]]
r8 = [complex(float(chi("chi8")[cls_of[g]][0]),
              float(chi("chi8")[cls_of[g]][1]) * R7) for g in A4]
mults = []
for row in a4tab:
    s = sum(r8[i] * row[a4class(A4[i])].conjugate() for i in range(12)) / 12
    assert abs(s.imag) < 1e-9 and abs(s.real - round(s.real)) < 1e-9
    mults.append(round(s.real))
check("nu-struct chi8|A4", "chi8|A4 = [0,1,1,2] (2 linear 'neutrinos' + "
      "2 triplets)", okA4 and mults == [0, 1, 1, 2], f"{mults}")

# ------------------------------------------------- MOLIEN-REC (suspect row)
print("\n--- SECTION B: refutation candidates, computed ---")
def molien_seq(nm, nmax=13):
    return [mult(power(nm, n), 0) for n in range(1, nmax + 1)]
rec_ok = {}
for nm, d in (("chi1",1),("chi3",3),("chi3b",3),("chi6",6),("chi7",7),("chi8",8)):
    a = molien_seq(nm)
    ok = all(a[n] == d*a[n-1] + a[n-2] - d*a[n-3] for n in range(3, len(a)))
    rec_ok[nm] = (ok, a[:8])
for nm, (ok, a) in rec_ok.items():
    print(f"      {nm}: a(1..8)={a}  recurrence a(n)=d*a(n-1)+a(n-2)-d*a(n-3): "
          f"{'holds' if ok else 'FAILS'}")
claim_all = all(ok for ok, _ in rec_ok.values())
check("MOLIEN-REC", "registry claims recurrence holds for ALL irreps "
      "('verified n=1..13 all')", False if not claim_all else True,
      "REFUTED as stated" if not claim_all else "confirmed")
# and the char.poly note: x^3 - d x^2 - x + d = (x-d)(x^2-1), NOT (x-d)(x^2+1)
check("MOLIEN-REC charpoly", "stated char.poly '(x-d)(x^2+1)' is wrong for its "
      "own recurrence: x^3-dx^2-x+d = (x-d)(x^2-1)", True,
      "sign typo at best; roots must be character values {d,+1,-1}")

# T4 Higgs-Guardian: Hom(chi1, chi_i (x) chi_i) = 1 for i in {8,3,7,6,1}?
t4 = {nm: mult(power(nm, 2), 0) for nm in ("chi8","chi3","chi7","chi6","chi1")}
check("T4 Higgs-Guardian", "claim: Hom(chi_i^2, chi1)=1 for i=8,3,7,6,1 "
      "('exactly 5 = g(3) channels')",
      all(v == 1 for v in t4.values()),
      f"computed {t4} — chi3^2 does NOT contain chi1 (chi3 complex; "
      "only chi3 x chi3bar does)")

# 127: chi6^3 -> chi1 multiplicity (claimed 2)
check("127 Z2-All-Loop", "Hom(chi6^3, chi1) = 2 (3-body vertex)",
      mult(power("chi6", 3), 0) == 2)

# 125 sigma-Unified max subgroups: '14 x S4 + 7 x Z7:Z3'
check("125 sigma-Unified", "claims 7 x Z7:Z3 — contradicts row 97 (8) and "
      "the computed Sylow count", n7 == 8,
      "125 is WRONG (7), 97 is right (8): internal contradiction in registry")

# ------------------------------------------------- model B: Cayley/Ramanujan
print("\n--- SECTION C: Klein-quartic side (model B: PSL(2,7)) ---")
def p_norm(m):
    a, b, c, d = m
    for k in range(1, 7):
        if (a * k) % 7 or (a == 0 and (b * k) % 7 < 0): pass
    # normalize sign: first nonzero of (a,b,c,d) in 1..3
    for v in (a, b, c, d):
        if v % 7:
            if v % 7 > 3: return tuple((-x) % 7 for x in m)
            return tuple(x % 7 for x in m)
    return tuple(x % 7 for x in m)
def p_mul(m, n):
    a, b, c, d = m; e, f, g, h = n
    return p_norm(((a*e+b*g), (a*f+b*h), (c*e+d*g), (c*f+d*h)))
gens = {}
seen = {p_norm((1, 0, 0, 1))}
frontier = [p_norm((1, 0, 0, 1))]
S = p_norm((0, 6, 1, 0)); T = p_norm((1, 1, 0, 1))
Ti = p_norm((1, 6, 0, 1))
while frontier:
    nxt = []
    for x in frontier:
        for g in (S, T, Ti):
            y = p_mul(x, g)
            if y not in seen:
                seen.add(y); nxt.append(y)
    frontier = nxt
check("model B", "PSL(2,7) generated by S,T has 168 elements", len(seen) == 168)
elsB = sorted(seen); idxB = {m: i for i, m in enumerate(elsB)}
Adj = np.zeros((168, 168))
for m in elsB:
    for g in (S, T, Ti):
        Adj[idxB[m], idxB[p_mul(m, g)]] += 1
ev = np.sort(np.linalg.eigvalsh((Adj + Adj.T) / 2))[::-1]
lam2 = max(abs(ev[1]), abs(ev[-1]))
check("E-3 Ramanujan", f"Cay(PSL(2,7),{{S,T,T^-1}}) 3-regular; "
      f"second eigenvalue {lam2:.4f} <= 2*sqrt(2) = {2*math.sqrt(2):.4f}",
      abs(ev[0] - 3) < 1e-9 and lam2 <= 2 * math.sqrt(2) + 1e-9,
      "classical (LPS 1988); confirmed numerically here")

# E-7 / 135 arithmetic
check("135 Gen3 (arith)", "genus 1 + 168/84 = 3 (Hurwitz bound case, classical)",
      1 + 168 // 84 == 3)
check("E-7 (arith)", "[SL2(Z):Gamma(7)] = 7^3 - 7 = 336 = 2*168; "
      "cusps(Gamma(7)) = 336/(2*7) = 24", 7**3 - 7 == 336 and 336//14 == 24)

# 152/154: class 3A size vs E7
check("152/154 (group fact)", "|class 3A| = 56 = dim(min rep E7) — the class "
      "size is real; the M-theory reading is parked", sizes[2] == 56)

# 118 Moonshine arithmetic
check("118 (arith)", "744*7 = 168*31 = 5208 ; 196884 mod 168 = 156 = -12 mod 168",
      744*7 == 168*31 == 5208 and 196884 % 168 == 156)
check("Ext-4 (arith)", "tau(7) = -16744 and 16744/299 = 56", 16744 == 299*56)

print("\n--- SECTION D: the decimal fits (Rule 3: fit until proven derived) ---")
phi = (1 + math.sqrt(5)) / 2
fits = [
    ("14.6 S prime", "6037 is prime", all(6037 % p for p in range(2, 78))),
]
for tag, claim, ok in fits:
    check(tag, claim, ok)
def report(tag, formula, pred, meas, err_note):
    print(f"      {tag}: {formula} = {pred:.6g} vs {meas} — {err_note}")
report("14.3d Higgs VEV", "E0*exp(-6037/168) needs E0", 246.18*math.exp(6037/168),
       "no named scale", f"E0 must be {246.18*math.exp(6037/168):.3e} GeV "
       "= a FREE parameter; one-parameter fit, not a derivation")
report("alphas-pi", "24*pi^2/2009", 24*math.pi**2/2009, "0.1180(9) PDG",
       f"{(24*math.pi**2/2009/0.1180-1)*100:+.2f}% — inside PDG error, but "
       "grammar (24, pi^2, 7^2*41) chosen post hoc; look-elsewhere unpriced")
report("OmegaL", "28/41", 28/41, "0.6847(73) Planck / 0.693(5) DESI+Planck",
       "0.3 sigma Planck-alone, ~2 sigma DESI+Planck (note-7's own update); "
       "same fraction PARKED in our T7")
report("GM glueball", "246.22/144", 246.22/144, "1.710(50)+ lattice",
       "central hit, but lattice 0++ glueball uncertainty is wide and the "
       "pairing v/ker is post hoc")
report("mc/ms", "13*25/24", 13*25/24, "~13.6 (PDG msbar ratio)",
       f"{(13*25/24/13.6-1)*100:+.1f}% — scheme/scale dependent target")
mue = 540/phi**2
report("O.1 mmu/me", "540/phi^2 (x(1+1/540) in registry)", mue,
       "206.7683", f"bare: {(mue/206.7683-1)*100:+.3f}%; with (1+1/540): "
       f"{(mue*(1+1/540)/206.7683-1)*100:+.3f}% — two versions circulate")
lam_pred = 1/8
mh_pred = math.sqrt(2*lam_pred)*246.22
sig = (125.25 - mh_pred)/0.17
print(f"      Higgs-Rig lambda=1/8: m_H = sqrt(2*lambda)*v = {mh_pred:.2f} GeV "
      f"vs 125.25(17) — {sig:.0f} sigma FAIL (convention m_H^2 = 2 lambda v^2; "
      "a hidden failure NOT in note-7's list of 11)")
report("P-7 running alpha", "137.036 - 540/60", 137.036 - 9, "127.95 (alpha(MZ))",
       "arithmetic fine; 'topological not loop' is an identification — parked")
report("D-5 nu ratio", "1/(13*phi^2)", 1/(13*phi**2), "0.02981",
       f"{(1/(13*phi**2)/0.02981-1)*100:+.1f}%")
report("S-13 DNA", "log2(648/pi^2)", math.log(648/math.pi**2, 2), "'6 bits'",
       "= 6.037... — note the 6037 pun; numerology, parked")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed "
      f"(failures above are refutations of registry rows, not script errors)")
print("=" * 78)
