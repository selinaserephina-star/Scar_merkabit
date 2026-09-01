# verify_ib_normalizer_mechanism.py — IB'S NORMALIZER MECHANISM, VERIFIED
# Cross-verification of RECEIVED_2026-09-01_IB_ANSWERS/"7<->6 NORMALIZER
# RESULT v0.1.md" against the sealed SM-024 (verify_envelope_normalizer.py,
# exhaustive over all 1,451,520 elements of Sp6(2)).
#
# IB's claim, with MECHANISM:
#   H = { diag(M, (M^-1)^T) : M in GL(3,2) }  <=  Sp6(2)
#       (the GL(3,2)-action on a Lagrangian decomposition F2^3 + (F2^3)*,
#        preserving the split symplectic form Gram [[0,I],[I,0]]),
#   outer element = the involution realizing M |-> (M^-1)^T (the symplectic
#   duality X <-> X*), so N_{Sp6(2)}(H) = <H, that> = PGL(2,7), [N:H] = 2.
#
# Our sealed SM-024 found TWO PSL(2,7) classes: the bitangent-transitive
# bridge class (C_G(H)=1, N = PGL(2,7), index 2) and the intransitive
# Fano-doubled class (self-normalizing).  This verifier (a) checks IB's
# mechanism exactly, and (b) identifies WHICH class his embedding is, by
# its fingerprint on the 28 odd (Arf-1) and 36 even (Arf-0) quadratic
# forms (Stone Q / SM-024 machinery, reused verbatim).
#
# DISCIPLINE: compute, never assert; discrepancies at full prominence.
# Run:  python -X utf8 verify_ib_normalizer_mechanism.py
#       (writes verify_ib_normalizer_mechanism.log as it goes)
import sys
from collections import Counter
from itertools import product
import numpy as np

LOG = open("verify_ib_normalizer_mechanism.log", "w", encoding="utf-8")
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); LOG.write(s + "\n"); LOG.flush()

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    say(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

say("=" * 78)
say("IB NORMALIZER MECHANISM -- H = {diag(M, M^-T)} <= Sp6(2), N = <H, swap>")
say("=" * 78)

# ------------------------------------------------- F2 matrix utilities
# a d x d matrix over F2 is a tuple of d ints: row i as a bitmask
# (bit j of row i = entry M[i][j]).  matvec: y_i = parity(M[i] & x).
def par(x): return bin(x).count("1") & 1

def mulM(A, B):
    d = len(A)
    out = []
    for i in range(d):
        r = 0
        a = A[i]
        for k in range(d):
            if (a >> k) & 1: r ^= B[k]
        out.append(r)
    return tuple(out)

def Tm(A):
    d = len(A)
    return tuple(sum(((A[j] >> i) & 1) << j for j in range(d))
                 for i in range(d))

def eye(d): return tuple(1 << i for i in range(d))

def rankM(A):
    d = len(A); rows = list(A); r = 0
    for c in range(d):
        piv = next((i for i in range(r, d) if (rows[i] >> c) & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(d):
            if i != r and (rows[i] >> c) & 1: rows[i] ^= rows[r]
        r += 1
    return r

def ordM(A):
    d = len(A); I = eye(d); X = A; o = 1
    while X != I:
        X = mulM(X, A); o += 1
        if o > 64: raise RuntimeError("order overflow")
    return o

# ------------------------------------------------- 1: GL(3,2) itself
say("\n--- 1: GL(3,2) -- the 168, census, simplicity, generators ---")
I3 = eye(3)
GL32 = [tuple(rows) for rows in product(range(8), repeat=3)
        if rankM(tuple(rows)) == 3]
check("1a |GL(3,2)|", "brute enumeration of all 512 3x3 matrices over F2: "
      "exactly 168 invertible", len(GL32) == 168, f"{len(GL32)} found")

PSL_CENSUS = {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}
PGL_CENSUS = {1: 1, 2: 49, 3: 56, 4: 42, 6: 56, 7: 48, 8: 84}
cen3 = dict(Counter(ordM(M) for M in GL32))
check("1b order census", "GL(3,2) element-order census = the PSL(2,7) "
      "census {1:1, 2:21, 3:56, 4:42, 7:48}", cen3 == PSL_CENSUS,
      f"census {cen3}")

INV3 = {}                                    # inverse table in GL(3,2)
GLset = set(GL32)
for M in GL32:
    for N in GL32:
        if mulM(M, N) == I3:
            INV3[M] = N; break
check("1c inverses", "every element has a two-sided inverse inside the "
      "168-set (closure under inversion; N*M = I re-checked)",
      len(INV3) == 168 and all(mulM(INV3[M], M) == I3 for M in GL32))

# simplicity, measured: conjugacy classes, then normal closure of each
# nontrivial class = whole group
conj_classes = []
seen = set()
for M in GL32:
    if M in seen: continue
    cls = {mulM(mulM(g, M), INV3[g]) for g in GL32}
    seen |= cls
    conj_classes.append(cls)
def gen_closure(gens, amb=None):
    S = {I3 if len(gens[0]) == 3 else eye(len(gens[0]))}
    frontier = list(S)
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = mulM(g, a)
                if b not in S:
                    S.add(b); nxt.append(b)
        frontier = nxt
    return S
simple_ok = True
for cls in conj_classes:
    rep = next(iter(cls))
    if rep == I3: continue
    if len(gen_closure(sorted(cls))) != 168: simple_ok = False
check("1d simple", "GL(3,2) is SIMPLE, measured: the normal closure "
      "(subgroup generated by the full conjugacy class) of EVERY "
      "nontrivial class is the whole 168 -- with 1b, GL(3,2) is the unique "
      "simple group of order 168 = PSL(2,7) [classical uniqueness]",
      simple_ok, f"{len(conj_classes)} conjugacy classes, sizes "
      f"{sorted(len(c) for c in conj_classes)}")

A3 = ((1 | 2), 2, 4)                 # transvection [[1,1,0],[0,1,0],[0,0,1]]
B3 = (4, 1, 2)                       # cyclic coordinate shift, order 3
gen168 = gen_closure([A3, B3])
check("1e generators", "the pair A = transvection e1->e1+e2, "
      "B = coordinate 3-cycle generates ALL of GL(3,2)",
      len(gen168) == 168 and A3 in GLset and B3 in GLset)

# ------------------------------------------------- 2: H = diag(M, M^-T)
say("\n--- 2: IB's H = {diag(M, (M^-1)^T)} <= Sp6(2) ---")
I6 = eye(6)
OMEGA = tuple([1 << (i + 3) for i in range(3)] + [1 << i for i in range(3)])
def is_symplectic(M):
    return mulM(Tm(M), mulM(OMEGA, M)) == OMEGA

def phi(M):                                  # the embedding diag(M, M^-T)
    Mit = Tm(INV3[M])
    return tuple([M[i] for i in range(3)] + [Mit[i] << 3 for i in range(3)])

H6 = {M: phi(M) for M in GL32}
Hset6 = set(H6.values())
check("2a H <= Sp6(2)", "ALL 168 elements diag(M, (M^-1)^T) preserve the "
      "split symplectic form Omega = [[0,I3],[I3,0]] (M^T Omega M = Omega "
      "checked matrix-by-matrix): H <= Sp6(2)",
      all(is_symplectic(g) for g in Hset6) and len(Hset6) == 168)
hom_ok = all(mulM(H6[M1], H6[M2]) == H6[mulM(M1, M2)]
             for M1 in GL32 for M2 in GL32)
check("2b phi is an injective hom", "phi(M1) phi(M2) = phi(M1 M2) for ALL "
      "168 x 168 pairs, and the 168 images are distinct: H = GL(3,2) = "
      "PSL(2,7) (by 1b/1d), |H| = 168", hom_ok and len(Hset6) == 168)
A6, B6 = H6[A3], H6[B3]                       # generators of H (by 1e)

# ------------------------------------------------- 3: the duality element J
say("\n--- 3: the outer element -- block swap J = [[0,I],[I,0]] ---")
J = tuple([1 << (i + 3) for i in range(3)] + [1 << i for i in range(3)])
check("3a J symplectic involution", "J preserves Omega, J^2 = I, and "
      "J is NOT in H (block-swap vs block-diagonal)",
      is_symplectic(J) and mulM(J, J) == I6 and J not in Hset6)
dual_ok = all(mulM(J, mulM(H6[M], J)) == H6[Tm(INV3[M])] for M in GL32)
check("3b J realizes the duality", "J diag(M, M^-T) J^-1 = "
      "diag(M^-T, M) = phi(M^-T) for ALL 168 M: conjugation by J induces "
      "exactly IB's map M |-> (M^-1)^T on H (so J normalizes H)", dual_ok)
outer_ok = True
for h in GL32:                                # is M |-> M^-T inner?  no h works
    if all(mulM(mulM(h, M), INV3[h]) == Tm(INV3[M]) for M in GL32):
        outer_ok = False; break
check("3c the duality is OUTER", "NO element of GL(3,2) realizes "
      "M |-> (M^-1)^T by conjugation (all 168 candidates tried): J induces "
      "the outer automorphism of PSL(2,7), not an inner one", outer_ok)
N336 = gen_closure([A6, B6, J])
cenN = dict(Counter(ordM(g) for g in N336))
check("3d <H,J> = PGL(2,7)", "the closure of <H, J> has EXACTLY 336 "
      "elements with the PGL(2,7) order census "
      "{1:1, 2:49, 3:56, 4:42, 6:56, 7:48, 8:84}",
      len(N336) == 336 and cenN == PGL_CENSUS, f"census {cenN}")
inN_sympl = all(is_symplectic(g) for g in N336)
# explicit normalizer membership test for every n in <H,J>:
INV6 = {}
for g in N336:
    for h in N336:
        if mulM(g, h) == I6:
            INV6[g] = h; break
norm_ok = all(mulM(n, mulM(A6, INV6[n])) in Hset6 and
              mulM(n, mulM(B6, INV6[n])) in Hset6 for n in N336)
check("3e <H,J> <= N_G(H)", "every one of the 336 elements conjugates "
      "BOTH generators of H back into the stored 168-set, and all 336 are "
      "symplectic: <H,J> <= N_{Sp6(2)}(H)", norm_ok and inN_sympl
      and len(INV6) == 336)

# ------------------------------------------------- 4: WHICH CLASS on the 28
say("\n--- 4: WHICH CLASS -- H on the 28 odd / 36 even quadratic forms ---")
# Stone Q / SM-024 machinery, verbatim conventions: vectors x in F2^6 as
# ints 0..63 (bits 0-2 the F2^3 part, bits 3-5 the dual part), base form
# q0(x) = sum x_i x_{i+3}, the 64 refinements q0 + <c,.>, Arf split 36/28,
# action q |-> q o g^-1.
def q0(x): return par((x & 7) & (x >> 3))
def matvec(M, x):
    y = 0
    for i in range(6):
        if par(M[i] & x): y |= 1 << i
    return y
def qform(c): return tuple(q0(x) ^ par(c & x) for x in range(64))
zeros = [sum(1 for x in range(64) if qform(c)[x] == 0) for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms = [c for c in range(64) if zeros[c] == 28]
check("4a Arf split", "64 refinements of Omega = 36 even + 28 odd "
      "(the 28 = the bitangents), same split as Stone Q / SM-024",
      len(even_forms) == 36 and len(odd_forms) == 28)
# polarization sanity: q0(x+y)+q0(x)+q0(y) = x^T Omega y
pol_ok = all(q0(x ^ y) ^ q0(x) ^ q0(y) == par(matvec(OMEGA, y) & x)
             for x in range(64) for y in range(64))
check("4b q0 polarizes to Omega", "q0(x+y)+q0(x)+q0(y) = x^T Omega y for "
      "all 64x64 pairs: the form family refines THE SAME Omega that H "
      "preserves -- same geometry, same 28, no relabeling", pol_ok)

def mat_to_perm(M): return tuple(matvec(M, x) for x in range(64))
def perm_inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def act_form_perm(Mperm_inv, c):
    tab = tuple(q0(Mperm_inv[x]) ^ par(c & Mperm_inv[x]) for x in range(64))
    cc = 0
    for k in range(6):
        if tab[1 << k] ^ q0(1 << k): cc |= 1 << k
    assert tab == qform(cc), "form action left the refinement family"
    return cc
def label_perm(M):
    pi = perm_inv(mat_to_perm(M))
    return tuple(act_form_perm(pi, c) for c in range(64))

def orbits_of(gens, pts):
    seen, out = set(), []
    for s0 in pts:
        if s0 in seen: continue
        orb = {s0}; q = [s0]
        while q:
            x = q.pop()
            for g in gens:
                y = g[x]
                if y not in orb: orb.add(y); q.append(y)
        seen |= orb
        out.append(sorted(orb))
    return out

lpA, lpB = label_perm(A6), label_perm(B6)
odd_orb = sorted(len(t) for t in orbits_of([lpA, lpB], odd_forms))
even_orb = sorted(len(t) for t in orbits_of([lpA, lpB], even_forms))
say(f"  H-orbits on the 28 odd forms:  {odd_orb}")
say(f"  H-orbits on the 36 even forms: {even_orb}")

odd_idx = {c: i for i, c in enumerate(odd_forms)}
def rest28(lp): return tuple(odd_idx[lp[c]] for c in odd_forms)
H28 = [rest28(label_perm(g)) for g in Hset6]
faithful28 = len(set(H28)) == 168
transitive = odd_orb == [28]
if transitive:
    def perm_order(p):
        import math
        seen, o = set(), 1
        for s0 in range(len(p)):
            if s0 in seen: continue
            L, x = 1, p[s0]
            seen.add(s0)
            while x != s0:
                seen.add(x); x = p[x]; L += 1
            o = o * L // math.gcd(o, L)
        return o
    stab = [h for h in H28 if h[0] == 0]
    st_orders = sorted(perm_order(h) for h in stab)
    def m28(a, b): return tuple(a[b[k]] for k in range(28))
    nonab = any(m28(a, b) != m28(b, a) for a in stab for b in stab)
    check("4c transitive, stab S3", "H is TRANSITIVE on the 28 odd forms "
          "(faithfully), point stabilizer of order 6 with element orders "
          "{1,2,2,2,3,3}, NONABELIAN => S3",
          faithful28 and len(stab) == 6
          and st_orders == [1, 2, 2, 2, 3, 3] and nonab,
          f"|stab| = {len(stab)}, orders {st_orders}")
    check("4d even fingerprint", "even-form orbit structure [1,7,7,21] -- "
          "the bridge-class fingerprint of SM-003 / Stone F(b) / Stone Q",
          even_orb == [1, 7, 7, 21], f"even orbits {even_orb}")
    check("4e CLASS VERDICT", "IB's diag(M, M^-T) embedding IS the "
          "bitangent-transitive BRIDGE CLASS of the sealed "
          "SM-003/SM-015/SM-024 (transitive on 28, stab S3, even orbits "
          "[1,7,7,21]) -- his N = PGL(2,7) is a claim about the SAME class "
          "our exhaustive SM-024 measured at index 2: MATCH, now with "
          "mechanism attached",
          transitive and even_orb == [1, 7, 7, 21]
          and len(stab) == 6 and faithful28)
else:
    check("4c/4e CLASS VERDICT -- DISCREPANCY CANDIDATE",
          "H is NOT transitive on the 28: this would make IB's embedding "
          "the SECOND (Fano-doubled) class, which sealed SM-024 found "
          "SELF-NORMALIZING -- a DISCREPANCY with his index-2 claim, "
          "reported at full prominence", False,
          f"odd orbits {odd_orb}, even orbits {even_orb}")

# ------------------------------------------------- 5: full normalizer, C = 1
say("\n--- 5: C_G(H) by direct linear solve; N = <H,J> exactly ---")
# centralizer conditions are LINEAR over F2: X with XA = AX, XB = BX for
# the two generators A6, B6 of H; then filter symplectic (= membership in
# Sp6(2), which IS the full isometry group of Omega).  36 unknowns x_ij.
def comm_rows(Amat):
    A = np.array([[(Amat[i] >> j) & 1 for j in range(6)]
                  for i in range(6)], dtype=np.uint8)
    rows = []
    for i in range(6):
        for j in range(6):
            v = np.zeros((6, 6), dtype=np.uint8)
            v[i, :] ^= A[:, j]                # (XA)_ij = sum_k x_ik A_kj
            v[:, j] ^= A[i, :]                # (AX)_ij = sum_k A_ik x_kj
            rows.append(v.reshape(36) & 1)
    return rows
Msys = np.array(comm_rows(A6) + comm_rows(B6), dtype=np.uint8)
# GF(2) nullspace
Mr = Msys.copy(); nrow, ncol = Mr.shape
pivots = []; r = 0
for c in range(ncol):
    piv = next((i for i in range(r, nrow) if Mr[i, c]), None)
    if piv is None: continue
    Mr[[r, piv]] = Mr[[piv, r]]
    for i in range(nrow):
        if i != r and Mr[i, c]: Mr[i] ^= Mr[r]
    pivots.append(c); r += 1
free = [c for c in range(ncol) if c not in pivots]
basis = []
for f in free:
    v = np.zeros(ncol, dtype=np.uint8); v[f] = 1
    for ri, c in enumerate(pivots):
        v[c] = Mr[ri, f]
    basis.append(v)
say(f"  commutant nullspace dimension over F2: {len(basis)} "
    f"(=> {2 ** len(basis)} matrices commuting with both generators)")
cent = []
for bits in product([0, 1], repeat=len(basis)):
    v = np.zeros(36, dtype=np.uint8)
    for b, w in zip(bits, basis):
        if b: v ^= w
    Xm = tuple(int(sum((v[6 * i + j] & 1) << j for j in range(6)))
               for i in range(6))
    if rankM(Xm) != 6: continue               # not invertible
    if not is_symplectic(Xm): continue        # not in Sp6(2)
    if mulM(Xm, A6) != mulM(A6, Xm): continue # sanity re-check
    if mulM(Xm, B6) != mulM(B6, Xm): continue
    cent.append(Xm)
check("5a CENTRALIZER", "C_{Sp6(2)}(H) = {I}: the full F2-linear commutant "
      "of the two generators, filtered to invertible symplectic matrices, "
      "contains ONLY the identity", cent == [I6],
      f"|C| = {len(cent)}, commutant dim {len(basis)}")
check("5b N = <H,J> EXACTLY", "with C = 1 (measured, 5a), N_G(H) = N/C "
      "embeds in Aut(PSL(2,7)) = PGL(2,7) of order 336 [classical]; "
      "<H,J> <= N_G(H) (3e) already HAS order 336 (3d) => "
      "N_{Sp6(2)}(H) = <H,J> = PGL(2,7) and [N:H] = 336/168 = 2 exactly",
      cent == [I6] and len(N336) == 336 and norm_ok
      and cenN == PGL_CENSUS and len(Hset6) == 168)

# ------------------------------------------------- 6: verdict
say("\n--- 6: verdict ---")
mech_ok = (FAIL == 0)
say("  VERDICT.  IB's mechanism is " +
    ("VERIFIED in full" if mech_ok else "NOT fully verified (see FAILs)") +
    ": H = {diag(M,(M^-1)^T)} is a faithful PSL(2,7) inside Sp6(2) "
    "preserving the split form [[0,I],[I,0]], and the block-swap "
    "involution J realizes the symplectic duality M |-> (M^-1)^T, an "
    "OUTER automorphism, giving <H,J> = PGL(2,7) = N_{Sp6(2)}(H) with "
    "[N:H] = 2 (centralizer measured trivial, so the Aut-embedding "
    "argument closes the normalizer from above).")
say(f"  WHICH CLASS.  Odd-form orbits {odd_orb}, even-form orbits "
    f"{even_orb}: " +
    ("this is the bitangent-TRANSITIVE bridge class (stab S3, even "
     "fingerprint [1,7,7,21]) of the sealed SM-003/SM-015/SM-024 -- the "
     "same class our exhaustive engine measured."
     if transitive and even_orb == [1, 7, 7, 21] else
     "NOT the bridge-class fingerprint -- DISCREPANCY with sealed SM-024, "
     "flagged at full prominence above."))
say("  CROSS-VERIFICATION.  Two independent engines now give the same "
    "normalizer for the same class: IB's structural/duality route "
    "(Lagrangian-split embedding + explicit outer involution) and our "
    "exhaustive route (SM-024, all 1,451,520 elements tested).  "
    "N_{Sp6(2)}(PSL(2,7)_transitive) = PGL(2,7), index 2, "
    "centralizer trivial -- agreed, with mechanism attached.")

say("\n" + "=" * 78)
say(f"RESULT: {PASS} checks passed, {FAIL} failed")
say("=" * 78)
LOG.close()
sys.exit(0 if FAIL == 0 else 1)
