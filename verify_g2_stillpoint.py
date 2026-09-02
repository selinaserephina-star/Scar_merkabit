# -*- coding: utf-8 -*-
r"""verify_g2_stillpoint.py — the scar's group inside the fold's G2 (SM-034 join).

CONTEXT.  SM-034 (TRIALITY_CRYSTALS.md) computed that the triality fold of the
D4 triple lands on G2 with state count 7 (+) 1 at the weight level.  This run
joins that seven to the Scar side's seven: PSL(2,7).  The sealed lane table
(SM-001, verify_tsc_scarcat.py, derived by Burnside-Dixon and verified exactly)
has irreps of dims 1, 3, 3bar, 6, 7, 8 on classes 1A,2A,3A,4A,7A,7B with sizes
[1,21,56,42,24,24].  SEALED ROWS USED HERE (rational, read-only):
    chi1 = (1, 1, 1, 1, 1, 1)
    chi6 = (6, 2, 0, 0,-1,-1)
    chi7 = (7,-1, 1,-1, 0, 0)
(chi6, chi7 are rational and take EQUAL values on 7A and 7B, so the 7A/7B
labelling ambiguity of a fresh permutation model is immaterial below.)

REGISTERED EXPECTATIONS (fail-first; each resolvable REFUTED at equal
prominence):
  E1  PSL(2,7) < G2, COMPUTED not cited: the chi7-invariant alternating
      3-form phi (built exactly over Q) is GENERIC — the standard bilinear
      form B_phi(x,y) := (x _| phi) ^ (y _| phi) ^ phi  in Lambda^7 = Q
      is NONDEGENERATE (exact determinant != 0), so Stab_{GL7}(phi) is a
      real form of G2 [P: Hitchin/Bryant — generic 3-forms in dim 7 have
      G2 stabiliser] and PSL(2,7) <= Stab(phi).
  E2  CANONICITY: dim Lambda^3(Q^7)*^{PSL(2,7)} = 1 — the group determines
      its G2-structure up to scalar (character count AND constructive
      group-average must agree).
  E3  THE CLOCK AT THE STILL POINT: rowmotion on the G2 7-crystal
      (a 7-chain = J(6-chain), corpus convention) is a SINGLE FREE 7-CYCLE
      — order 7, EXCEEDING h(G2) = 6; CSP against RGF = 1+q+...+q^6.

BACKGROUND CHECK (the two sevens, nailed): (a) the 7-point Fano action of
GL(3,2) decomposes as 1 (+) chi6 (SIX-dimensional!); (b) the 8-point action
on P1(F7) decomposes as 1 (+) chi7 — chi7 IS the deleted permutation module
of the 8-point action, realisable over Q with integer matrices.  Both are
verified by exact character inner products against the sealed rows.

House rules: compute never assert; EXACT arithmetic (int / Fraction) for every
invariance / genericity / decomposition claim; floats only for the signature
of B_phi (flagged); refutations at equal prominence.  Not RH/GRH; no physics;
Rule 3 (no identifications) in force.  No registry / git / knowledge.yaml
writes; sealed files read-only.

Run:  python -X utf8 verify_g2_stillpoint.py
"""
import itertools, cmath
from collections import defaultdict, Counter
from fractions import Fraction
from functools import reduce
from math import gcd

import numpy as np

PASS_N = FAIL_N = 0
CHECK_NO = 0
def check(claim, ok, detail=""):
    global PASS_N, FAIL_N, CHECK_NO
    CHECK_NO += 1
    s = "PASS" if ok else "FAIL"
    if ok: PASS_N += 1
    else:  FAIL_N += 1
    print(f"[{s}] ({CHECK_NO:02d}) {claim}" + (f"  -> {detail}" if detail else ""))
    return ok

print("=" * 78)
print("G2 STILLPOINT — the scar's group inside the fold's G2 (join to SM-034)")
print("merkabit x scar combination run, 2026-09-02")
print("=" * 78)
print("""
REGISTERED EXPECTATIONS (logged before computation; fail-first):
  E1  PSL(2,7) < G2 COMPUTED: invariant 3-form phi is generic
      (det B_phi != 0, exact)  =>  Stab(phi) is a form of G2 containing
      PSL(2,7)   [may resolve REFUTED if B_phi degenerates]
  E2  CANONICITY: the invariant space in Lambda^3 is 1-DIMENSIONAL
      (character count AND constructive average)   [may resolve REFUTED]
  E3  CLOCK: rowmotion on the G2 7-crystal is a SINGLE FREE 7-CYCLE,
      order 7 > h(G2) = 6; CSP vs RGF = 1+q+...+q^6   [may resolve REFUTED]
Each may resolve REFUTED; the refutation is recorded at equal prominence.
""")

# ======================================================================
# 1. PSL(2,7) as Moebius maps on P1(F7) = {0..6, oo}; fresh model.
# ======================================================================
print("--- 1. the group: PSL(2,7) on P1(F7), generators z->z+1, z->-1/z " + "-" * 10)

def pt(x, y):
    """point index of (x:y): z = x/y in 0..6, or 7 for oo."""
    x %= 7; y %= 7
    if y:
        return (x * pow(y, 5, 7)) % 7          # y^-1 = y^5 mod 7
    return 7
PTS = [(z, 1) for z in range(7)] + [(1, 0)]    # index 7 = oo

def perm_of(a, b, c, d):
    return tuple(pt(a * x + b * y, c * x + d * y) for (x, y) in PTS)

T_gen = perm_of(1, 1, 0, 1)      # z -> z + 1
S_gen = perm_of(0, -1, 1, 0)     # z -> -1/z

def pmul(p, q):                   # (p*q)(x) = p(q(x))
    return tuple(p[q[i]] for i in range(8))
def pinv(p):
    out = [0] * 8
    for i in range(8): out[p[i]] = i
    return tuple(out)
ID = tuple(range(8))

seen = {ID}; frontier = [ID]
while frontier:
    nxt = []
    for p in frontier:
        for g in (S_gen, T_gen):
            q = pmul(p, g)
            if q not in seen:
                seen.add(q); nxt.append(q)
    frontier = nxt
els = sorted(seen)
check("<z->z+1, z->-1/z> on the 8 points of P1(F7) has exactly 168 elements",
      len(els) == 168, f"|G| = {len(els)}")

def p_order(p):
    k, x = 1, p
    while x != ID:
        x = pmul(x, p); k += 1
    return k
ORD = {p: p_order(p) for p in els}

# conjugacy classes (fresh, from the permutation model)
cls_of = {}
classes = []
for p in els:
    if p in cls_of: continue
    orb = {pmul(pmul(q, p), pinv(q)) for q in els}
    c = len(classes)
    for x in orb: cls_of[x] = c
    classes.append(sorted(orb))
classes.sort(key=lambda c: (ORD[c[0]], len(c)))
cls_of = {x: c for c, cl in enumerate(classes) for x in cl}
sizes = [len(c) for c in classes]
reps  = [c[0] for c in classes]
names = ["1A", "2A", "3A", "4A", "7A", "7B"]
check("class sizes = [1,21,56,42,24,24], element orders [1,2,3,4,7,7] "
      "(matches the sealed table's class data)",
      sizes == [1, 21, 56, 42, 24, 24] and
      [ORD[r] for r in reps] == [1, 2, 3, 4, 7, 7],
      f"sizes={sizes}, orders={[ORD[r] for r in reps]}")
print("      (7A/7B label order arbitrary in a fresh model; the sealed rows")
print("       used below are rational with chi(7A)=chi(7B), so nothing depends on it)")

# fixed points on the 8 points — constant per class
def fixn(p): return sum(1 for i in range(8) if p[i] == i)
fix_by_class = []
fix_const = True
for cl in classes:
    fs = {fixn(p) for p in cl}
    fix_const &= (len(fs) == 1)
    fix_by_class.append(fs.pop())
check("fixed-point count on the 8 points is constant on each class",
      fix_const, f"fix per class = {fix_by_class}")

# power maps of classes, computed from the model directly (well-definedness too)
pw2, pw3, pw_ok = [], [], True
for cl in classes:
    s2 = {cls_of[pmul(p, p)] for p in cl}
    s3 = {cls_of[pmul(pmul(p, p), p)] for p in cl}
    pw_ok &= len(s2) == 1 and len(s3) == 1
    pw2.append(s2.pop()); pw3.append(s3.pop())
check("power maps well-defined per class (computed, not assumed)",
      pw_ok,
      "g->g^2: " + ", ".join(f"{names[c]}->{names[pw2[c]]}" for c in range(6))
      + " ; g->g^3: " + ", ".join(f"{names[c]}->{names[pw3[c]]}" for c in range(6)))

# ======================================================================
# 2. sealed rows; the TWO SEVENS nailed by exact inner products.
# ======================================================================
print("\n--- 2. the two sevens: 8-point = 1 (+) chi7  vs  Fano 7-point = 1 (+) chi6 " + "-")
F = Fraction
CHI1 = [F(1)] * 6
CHI6 = [F(v) for v in (6, 2, 0, 0, -1, -1)]     # SEALED (SM-001)
CHI7 = [F(v) for v in (7, -1, 1, -1, 0, 0)]     # SEALED (SM-001)

def inner(u, v):
    """<u, v> = (1/168) sum_c |C_c| u(c) v(c)  — real rational rows only."""
    s = sum(F(sizes[c]) * u[c] * v[c] for c in range(6))
    return s / 168

pi8 = [F(f) for f in fix_by_class]               # 8-point permutation character
check("8-point action: <pi8, chi1> = 1, <pi8, chi7> = 1, <pi8, pi8> = 2  "
      "=> pi8 = 1 (+) chi7 EXACTLY (chi7 = deleted permutation module)",
      inner(pi8, CHI1) == 1 and inner(pi8, CHI7) == 1 and inner(pi8, pi8) == 2,
      f"pi8 = {[int(v) for v in pi8]}; inner products "
      f"({inner(pi8, CHI1)}, {inner(pi8, CHI7)}, {inner(pi8, pi8)})")

# --- the OTHER seven: GL(3,2) on the 7 Fano points (independent model) ---
def m_mul(a, b):
    return tuple((a[3*i]*b[j] ^ a[3*i+1]*b[3+j] ^ a[3*i+2]*b[6+j])
                 for i in range(3) for j in range(3))
def m_det(a):
    return (a[0]*(a[4]*a[8] ^ a[5]*a[7]) ^ a[1]*(a[3]*a[8] ^ a[5]*a[6])
            ^ a[2]*(a[3]*a[7] ^ a[4]*a[6])) & 1
gl = [m for m in itertools.product((0, 1), repeat=9) if m_det(m)]
E9 = (1, 0, 0, 0, 1, 0, 0, 0, 1)
def m_order(a):
    k, x = 1, a
    while x != E9:
        x = m_mul(x, a); k += 1
    return k
def m_fix7(g):
    cnt = 0
    for v in range(1, 8):
        vec = ((v >> 2) & 1, (v >> 1) & 1, v & 1)
        w = tuple((g[3*i]*vec[0] ^ g[3*i+1]*vec[1] ^ g[3*i+2]*vec[2])
                  for i in range(3))
        if w == vec: cnt += 1
    return cnt
ordhist = Counter(m_order(g) for g in gl)
check("GL(3,2) model: 168 elements, order histogram {1:1,2:21,3:56,4:42,7:48}",
      len(gl) == 168 and ordhist == Counter({1: 1, 2: 21, 3: 56, 4: 42, 7: 48}),
      f"{dict(sorted(ordhist.items()))}")
fix_by_ord = defaultdict(set)
for g in gl:
    fix_by_ord[m_order(g)].add(m_fix7(g))
check("Fano fixed-point count depends only on element order "
      "(both order-7 classes fix 0 points)",
      all(len(v) == 1 for v in fix_by_ord.values()),
      f"order->fix: { {k: sorted(v)[0] for k, v in sorted(fix_by_ord.items())} }")
pi7 = [F(sorted(fix_by_ord[o])[0]) for o in (1, 2, 3, 4, 7, 7)]
check("Fano action: <pi7, chi1> = 1, <pi7, chi6> = 1, <pi7, pi7> = 2  "
      "=> pi7 = 1 (+) chi6 EXACTLY (a SIX-dim complement, not chi7)",
      inner(pi7, CHI1) == 1 and inner(pi7, CHI6) == 1 and inner(pi7, pi7) == 2,
      f"pi7 = {[int(v) for v in pi7]}")
check("TWO-SEVENS FLAG: <pi7, chi7> = 0 — the Fano seven contains NO copy of "
      "chi7; the 7-dim irreducible lives in the EIGHT-point action only",
      inner(pi7, CHI7) == 0, f"<pi7, chi7> = {inner(pi7, CHI7)}")

# ======================================================================
# 3. chi7 built explicitly over Q: integer 7x7 matrices.
# ======================================================================
print("\n--- 3. chi7 over Q: deleted permutation module, integer matrices " + "-" * 10)
print("  basis of the complement of the all-ones vector in Q^8:")
print("  v_i = e_i - e_7 (i = 0..6, point 7 = oo);  g.v_i = v_{g(i)} - v_{g(7)}")

def mat_of(p):
    """7x7 integer matrix of g on span(v_0..v_6), v_7 := 0."""
    M = [[0] * 7 for _ in range(7)]
    for i in range(7):
        if p[i] != 7: M[p[i]][i] += 1
        if p[7] != 7: M[p[7]][i] -= 1
    return M
def matmul(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    return [[sum(A[r][t] * B[t][c] for t in range(k)) for c in range(m)]
            for r in range(n)]

rng = np.random.default_rng(7)
pairs = [(els[int(rng.integers(168))], els[int(rng.integers(168))])
         for _ in range(25)]
check("g -> M_g is a homomorphism: M_{pq} = M_p M_q on 25 random pairs (exact)",
      all(mat_of(pmul(p, q)) == matmul(mat_of(p), mat_of(q)) for p, q in pairs))
tr_by_class = []
tr_const = True
for cl in classes:
    ts = {sum(mat_of(p)[i][i] for i in range(7)) for p in cl}
    tr_const &= len(ts) == 1
    tr_by_class.append(ts.pop())
check("character of the 7-dim rep = SEALED chi7 row (7,-1,1,-1,0,0) on all six "
      "classes (traces constant per class)",
      tr_const and [F(t) for t in tr_by_class] == CHI7,
      f"traces = {tr_by_class}")
check("irreducibility: <chi7, chi7> = 1 EXACTLY",
      inner([F(t) for t in tr_by_class], [F(t) for t in tr_by_class]) == 1)

# ======================================================================
# 4. E1 + E2: the invariant alternating 3-forms.
# ======================================================================
print("\n--- 4. E1/E2: invariant 3-forms — character count, then construction " + "-" * 5)

# (i) character count:  Lambda^3 chi(g) = (chi(g)^3 - 3 chi(g) chi(g^2)
#                                          + 2 chi(g^3)) / 6, exact per class
lam3chi = []
for c in range(6):
    v = (CHI7[c] ** 3 - 3 * CHI7[c] * CHI7[pw2[c]] + 2 * CHI7[pw3[c]]) / 6
    lam3chi.append(v)
check("exterior-cube character integral on every class (power maps from the "
      "model)", all(v.denominator == 1 for v in lam3chi),
      "Lambda^3 chi7 = (" + ", ".join(str(v) for v in lam3chi) + ") on "
      + ",".join(names))
m_inv = inner(lam3chi, CHI1)
check("character count: dim Lambda^3(chi7)^G = <Lambda^3 chi7, 1> = 1",
      m_inv == 1, f"count = {m_inv}")

# (ii) constructive: group-average Lambda^3 of the DUAL rep over all 168
SUBS = list(itertools.combinations(range(7), 3))          # 35 basis 3-forms
IDX = {s: i for i, s in enumerate(SUBS)}
def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
          - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
          + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
def lam3mat(N):
    """35x35 matrix of Lambda^3(N): entry[I][J] = det N[I, J]."""
    return [[det3([[N[i][j] for j in J] for i in I]) for J in SUBS]
            for I in SUBS]
def transpose(M):
    return [[M[c][r] for c in range(len(M))] for r in range(len(M[0]))]

ACC = [[0] * 35 for _ in range(35)]        # = 168 * projector, integer
for p in els:
    N = transpose(mat_of(pinv(p)))         # dual rep: N_g = (M_{g^-1})^T
    L = lam3mat(N)
    for r in range(35):
        Ar, Lr = ACC[r], L[r]
        for c in range(35):
            Ar[c] += Lr[c]
check("group average: trace(sum_g Lambda^3 N_g) = 168  (=> trace of the "
      "projector = 1, matching the character count)",
      sum(ACC[i][i] for i in range(35)) == 168,
      f"trace = {sum(ACC[i][i] for i in range(35))}")
A2 = matmul(ACC, ACC)
check("projector property: (sum)^2 = 168 * (sum), exact integers",
      all(A2[r][c] == 168 * ACC[r][c] for r in range(35) for c in range(35)))

def rank_frac(M):
    A = [[F(x) for x in row] for row in M]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                A[i] = [A[i][j] - A[i][c] * A[r][j] for j in range(m)]
        r += 1
        if r == n: break
    return r
rk = rank_frac(ACC)
E2_ok = (rk == 1 and m_inv == 1)
check("E2: constructive dimension of the invariant subspace = rank of the "
      "averaged projector = 1 (agrees with character count)",
      E2_ok, f"rank = {rk}")
E2_RES = "PASS" if E2_ok else "REFUTED"
print(f"\n  ** E2 RESOLUTION: {E2_RES} — the invariant 3-form space is "
      + ("1-DIMENSIONAL: the group determines its G2-structure up to scalar. **"
         if E2_ok else f"{rk}-dimensional, NOT canonical. **"))

# extract phi: a nonzero column of the projector, gcd-reduced, integer
j0 = next(j for j in range(35) if any(ACC[i][j] for i in range(35)))
phi_vec = [ACC[i][j0] for i in range(35)]
g0 = reduce(gcd, (abs(x) for x in phi_vec if x))
phi_vec = [x // g0 for x in phi_vec]
if next(x for x in phi_vec if x) < 0:
    phi_vec = [-x for x in phi_vec]
nz = [(SUBS[i], phi_vec[i]) for i in range(35) if phi_vec[i]]
print(f"\n  phi (invariant 3-form, integer coefficients, {len(nz)} nonzero of 35):")
print("    phi = " + " ".join(
    f"{'+' if c > 0 else '-'}{abs(c) if abs(c) != 1 else ''}"
    f"e{i}{j}{k}" for (i, j, k), c in nz))

for gname, g in (("S: z->-1/z", S_gen), ("T: z->z+1", T_gen)):
    N = transpose(mat_of(pinv(g)))
    img = [sum(row[j] * phi_vec[j] for j in range(35)) for row in lam3mat(N)]
    check(f"phi invariant under generator {gname} (exact; generators generate "
          "=> invariant under all of PSL(2,7))", img == phi_vec)

# --- genericity: B_phi(x,y) via (x _| phi) ^ (y _| phi) ^ phi in Lambda^7 ---
print("\n  genericity test (exact):")
phi_form = {SUBS[i]: phi_vec[i] for i in range(35) if phi_vec[i]}
def contract(a, f3):
    out = defaultdict(int)
    for (i, j, k), c in f3.items():
        if a == i:   out[(j, k)] += c
        elif a == j: out[(i, k)] -= c
        elif a == k: out[(i, j)] += c
    return out
def wedge(f1, f2):
    out = defaultdict(int)
    for t1, c1 in f1.items():
        s1 = set(t1)
        for t2, c2 in f2.items():
            if s1 & set(t2): continue
            merged = list(t1) + list(t2)
            invs = sum(1 for a in range(len(merged)) for b in range(a + 1, len(merged))
                       if merged[a] > merged[b])
            out[tuple(sorted(merged))] += (-1) ** invs * c1 * c2
    return out
TOP = tuple(range(7))
B = [[0] * 7 for _ in range(7)]
for a in range(7):
    ca = contract(a, phi_form)
    for b in range(7):
        w = wedge(wedge(ca, contract(b, phi_form)), phi_form)
        B[a][b] = w.get(TOP, 0)
check("B_phi symmetric (exact)", all(B[a][b] == B[b][a]
                                     for a in range(7) for b in range(7)))
def det_frac(M):
    A = [[F(x) for x in row] for row in M]
    n = len(A); d = F(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c] != 0), None)
        if piv is None: return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]; d = -d
        d *= A[c][c]
        inv = 1 / A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] * inv
                A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return d
detB = det_frac(B)
E1_ok = (detB != 0)
check("E1 genericity: det(B_phi) != 0 EXACTLY — phi is a GENERIC 3-form",
      E1_ok, f"det(B_phi) = {detB}")
evals = np.linalg.eigvalsh(np.array(B, dtype=float))
n_pos = int(np.sum(evals > 1e-9)); n_neg = int(np.sum(evals < -1e-9))
definite = (n_pos == 7 or n_neg == 7)
sig = (n_pos, n_neg)
check("signature of B_phi (numeric, signature only): DEFINITE up to overall "
      "sign => the stabiliser is the COMPACT real form of G2",
      definite, f"signature = {sig}, eigenvalues ~ {np.round(evals, 3).tolist()}")
E1_ok = E1_ok and True   # E1 is the genericity claim; form flavor recorded above
E1_RES = "PASS" if E1_ok else "REFUTED"
print(f"""
  ** E1 RESOLUTION: {E1_RES} — det(B_phi) = {detB} != 0, phi generic;
     [P: Hitchin 2000 / Bryant 1987 — a 3-form on R^7 with nondegenerate
      B_phi has stabiliser a real form of G2, compact iff B_phi definite]
     phi is PSL(2,7)-invariant (checked exactly on generators, hence on G):
        PSL(2,7)  <=  Stab_GL(7)(phi)  =  G2{'(compact)' if definite else '(split)'}
     PSL(2,7) < G2 EXHIBITED with an explicit invariant tensor over Q. **""")

# ======================================================================
# 5. the branching identity + the two-sevens restated as a theorem/flag.
# ======================================================================
print("--- 5. the branching identity " + "-" * 47)
check("THEOREM (proved by the construction above): the G2-seven restricted to "
      "PSL(2,7) IS chi7, irreducibly — 7|_PSL(2,7) = chi7, <chi7,chi7> = 1",
      E1_ok and inner(CHI7, CHI7) == 1,
      "the staircase's founding 7-dim world and the fold's G2 seven are the "
      "SAME seven")
print("""  The 7-dim rep of Stab(phi) = G2 is the defining rep on V = Q^7 itself;
  by construction PSL(2,7) acts on V by chi7 (sealed row matched, irreducible).
  So the branching  G2's 7  |  PSL(2,7)  =  chi7  needs no further computation:
  the restriction IS the module we built.  FLAG FOR IB (precise): the OTHER
  seven — the 7-point Fano permutation module of GL(3,2) — is 1 (+) chi6 and
  contains NO chi7 (<pi7, chi7> = 0, check 09).  The seven that meets G2 is
  the DELETED PERMUTATION MODULE OF THE EIGHT-POINT ACTION, not the Fano seven.""")

# ======================================================================
# 6. E3: the clock at the still point — the G2 7-crystal and rowmotion.
# ======================================================================
print("--- 6. E3: the G2 7-crystal (independent rebuild) and its rowmotion " + "-" * 6)
# G2 Cartan data, Bourbaki: alpha1 SHORT (len^2 = 2), alpha2 LONG (len^2 = 6)
G2G = [[F(2), F(-3)], [F(-3), F(6)]]
def ip2(x, y):
    return sum(x[r] * G2G[r][c] * y[c] for r in range(2) for c in range(2))
def coA(i, mu):
    a = [(1, 0), (0, 1)][i - 1]
    return 2 * ip2(mu, a) / ip2(a, a)
POSROOTS = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
w1g, rho = (2, 1), (5, 3)
dim = F(1)
for a in POSROOTS:
    dim *= F(ip2((w1g[0] + rho[0], w1g[1] + rho[1]), a), ip2(rho, a))
check("Weyl dimension formula: dim V(w1) for G2 = 7 exactly", dim == 7,
      f"dim = {dim}")
def refl(i, mu):
    a = [(1, 0), (0, 1)][i - 1]
    c = coA(i, mu)
    return (mu[0] - c * a[0], mu[1] - c * a[1])
orbit = {w1g}; frontier = [w1g]
while frontier:
    m = frontier.pop()
    for i in (1, 2):
        m2 = refl(i, m); m2 = (F(m2[0]), F(m2[1]))
        if m2 not in orbit:
            orbit.add(m2); frontier.append(m2)
orbit = {(int(a), int(b)) for a, b in orbit}
check("weights of the 7 = the six short roots + 0 (W-orbit of w1, mult-free)",
      orbit == {(1, 0), (1, 1), (2, 1), (-1, 0), (-1, -1), (-2, -1)},
      f"orbit = {sorted(orbit)}")
WTS7 = sorted(orbit | {(0, 0)})
# Kashiwara build: mult-free weights => f_i edges are the alpha_i-strings;
# sl2 consistency (top of every length-L string has <mu, a_i^vee> = L-1)
edges7, str_ok = [], True
for i in (1, 2):
    a = [(1, 0), (0, 1)][i - 1]
    tops = [m for m in WTS7 if (m[0] + a[0], m[1] + a[1]) not in WTS7]
    for t in tops:
        s = [t]
        while (s[-1][0] - a[0], s[-1][1] - a[1]) in WTS7:
            s.append((s[-1][0] - a[0], s[-1][1] - a[1]))
        if len(s) > 1:
            str_ok &= coA(i, t) == len(s) - 1
            for u, v in zip(s, s[1:]):
                edges7.append((u, i, v))
check("all sl2-strings consistent (top label = string length - 1)", str_ok)
indeg = Counter(); outdeg = Counter()
for u, i, v in edges7:
    outdeg[u] += 1; indeg[v] += 1
top7 = [m for m in WTS7 if indeg[m] == 0]
chain_ok = (len(edges7) == 6 and len(top7) == 1
            and all(outdeg[m] <= 1 and indeg[m] <= 1 for m in WTS7))
colorseq = []
if chain_ok:
    x = top7[0]
    while outdeg[x]:
        u, i, v = next(e for e in edges7 if e[0] == x)
        colorseq.append(i); x = v
check("G2 7-crystal = 7-vertex CHAIN, color sequence 1,2,1,1,2,1 "
      "(matches SM-034 ground truth)",
      chain_ok and colorseq == [1, 2, 1, 1, 2, 1], f"sequence = {colorseq}")

# rowmotion, corpus convention (= Merkabit_crystal/verify_csp_27.py, unchanged):
# highest weight TOP, f-edges DOWN; L = J(P); Psi(I) = down-ideal generated by
# the minimal elements of the complement.
children = defaultdict(set)
for u, i, v in edges7:
    children[u].add(v)
below = {}
def dfs(v, acc):
    acc.add(v)
    for w in children[v]:
        if w not in acc: dfs(w, acc)
for v in WTS7:
    acc = set(); dfs(v, acc); below[v] = acc
above = {v: {u for u in WTS7 if v in below[u]} for v in WTS7}
P = [v for v in WTS7 if len(children[v]) == 1]
chain_P = all(p in below[q] or q in below[p]
              for p, q in itertools.combinations(P, 2))
check("join-irreducibles: P = a 6-chain (any two comparable) — the crystal "
      "order is the 7-chain = J(6-chain)",
      len(P) == 6 and chain_P, f"|P| = {len(P)}, totally ordered: {chain_P}")
def leq(p, q): return p in below[q]
ideal_of = {x: frozenset(p for p in P if leq(p, x)) for x in WTS7}
all_ideals = set()
for r in range(7):
    for sub in itertools.combinations(P, r):
        s = set(sub)
        if all(q in s for p in s for q in P if leq(q, p)):
            all_ideals.add(frozenset(s))
check("Birkhoff: x -> I(x) bijection onto J(P), |J(P)| = 7 (distributive)",
      len(set(ideal_of.values())) == 7 and set(ideal_of.values()) == all_ideals,
      f"|J(P)| = {len(all_ideals)}")
vert_of = {I: x for x, I in ideal_of.items()}
def rowmotion(I):
    comp = [p for p in P if p not in I]
    mins = [p for p in comp if not any(q != p and leq(q, p) for q in comp)]
    return frozenset(q for q in P if any(leq(q, m) for m in mins))
Psi = {x: vert_of[rowmotion(ideal_of[x])] for x in WTS7}
seen2 = set(); orbs = []
for x in sorted(WTS7):
    if x in seen2: continue
    o = []; y = x
    while y not in seen2:
        seen2.add(y); o.append(y); y = Psi[y]
    orbs.append(o)
ctype = sorted((len(o) for o in orbs), reverse=True)
order_Psi = reduce(lambda a, b: a * b // gcd(a, b), ctype, 1)
print(f"\n  rowmotion orbit type {ctype}, order {order_Psi}   (h(G2) = 6)")
for o in orbs:
    print("    (" + " -> ".join(str(x) for x in o) + ")")
E3_cycle = (ctype == [7])
check("E3: rowmotion on the G2 7-crystal is a SINGLE FREE 7-CYCLE (order 7)",
      E3_cycle, f"cycle type {ctype}, order {order_Psi}")
check("the still-point clock EXCEEDS the Coxeter number: ord(Psi) = 7 > 6 = "
      "h(G2) — every other measured crystal clock ticked at its own h "
      "(D4: 6, E6-27: 12, E7-56: 18)",
      order_Psi == 7 and order_Psi > 6)
# CSP at the measured order
sizesI = Counter(len(I) for I in ideal_of.values())
RGF = [sizesI.get(r, 0) for r in range(max(sizesI) + 1)]
zeta = cmath.exp(2j * cmath.pi / order_Psi)
csp_ok = True; details = []
powmap = {x: x for x in WTS7}
for dd in range(order_Psi):
    fx = sum(1 for x in WTS7 if powmap[x] == x)
    val = sum(RGF[r] * zeta ** (dd * r) for r in range(len(RGF)))
    csp_ok &= abs(fx - val) < 1e-9
    details.append(f"d={dd}:{fx}|{val.real:+.2f}{val.imag:+.2f}i")
    powmap = {x: Psi[powmap[x]] for x in WTS7}
check(f"CSP at the measured order: |Fix(Psi^d)| = RGF(zeta_{order_Psi}^d) "
      "for all d, RGF = 1+q+...+q^6",
      csp_ok and RGF == [1] * 7, "  ".join(details))
E3_ok = E3_cycle and order_Psi == 7 and csp_ok
E3_RES = "PASS" if E3_ok else "REFUTED"
print(f"""
  ** E3 RESOLUTION: {E3_RES} — at the still point of the turn, the merkabit
     clock ticks in SEVENS: one free 7-cycle, order 7 = the order of the
     scar's own Frobenius, EXCEEDING h(G2) = 6.
     HONEST CAVEAT: rowmotion on J(chain) being a single cycle is elementary
     (it slides the ideal size by one, mod 7).  The content is (a) the
     CONTRAST with h — every other measured crystal clock in the corpus
     ticked at its Coxeter number — and (b) the identification of WHICH
     seven-cycle structure the still point's crystal carries. **""")

# ======================================================================
# 7. the octonion tie [P] — cited, not computed.
# ======================================================================
print("--- 7. the octonion tie [P: cited, NOT computed] " + "-" * 28)
print("""  [P] A generic 3-form on R^7 with definite B_phi is the structure tensor of
  an octonion multiplication on R (+) R^7 (G2 = Aut(O), Cartan); the classical
  Fano-plane mnemonic for octonion multiplication uses the 7 imaginary units
  as Fano points, and PSL(2,7) = GL(3,2) = Aut(Fano) acts on the mnemonic's
  labellings.  We keep [P] and [C] separate: our COMPUTED anchor is the
  explicit rational phi with det(B_phi) != 0 and its PSL(2,7)-invariance;
  the octonionic reading of phi is cited theory, and note the two-sevens flag
  (check 09): the Fano mnemonic's seven POINTS carry 1 (+) chi6, while the
  seven UNITS transform as chi7 only through the G2 structure itself.""")

# ======================================================================
# 8. summary
# ======================================================================
print("=" * 78)
print(f"SUMMARY: {PASS_N} PASS / {FAIL_N} FAIL of {CHECK_NO} checks")
print(f"  E1 (PSL(2,7) < G2 via explicit generic invariant phi) : {E1_RES}"
      f"   [det B_phi = {detB}, signature {sig}]")
print(f"  E2 (canonicity: invariant 3-form space 1-dim)         : {E2_RES}"
      f"   [character count {m_inv}, constructive rank {rk}]")
print(f"  E3 (still-point clock = single free 7-cycle, 7 > h=6) : {E3_RES}"
      f"   [cycle type {ctype}, CSP {'holds' if csp_ok else 'FAILS'}]")
print(f"  two sevens: pi8 = 1 (+) chi7 ; Fano pi7 = 1 (+) chi6, <pi7,chi7> = 0")
print("=" * 78)
print("Not RH/GRH; no physics; Rule 3 (no identifications) in force.")
print("The still point of the turn now contains: the fold's G2 [SM-034], the")
print("scar's own group PSL(2,7) sitting inside it with a CANONICAL (1-dim)")
print("invariant structure phi computed exactly over Q, and a clock that ticks")
print("in sevens — the one crystal clock measured so far that beats its own")
print("Coxeter number.  Computed, not asserted.")
