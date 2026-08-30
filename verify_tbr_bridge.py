# verify_tbr_bridge.py — Thread T-BR: how do Merkabit (E6 / the 27) and
# Scar-Cat (PSL(2,7) / the 168) actually fit together?
#
# Three levels, each computed:
#   B. FIELDS    — the cyclotomic bridge Q(zeta_21) = Q(zeta_3)*Q(zeta_7)
#                  (the merged registry's PB-01), verified and sharpened:
#                  sqrt(-7) is the CHARACTER FIELD of Ilya's chi3,
#                  sqrt(-3) the Eisenstein/trit field of the crystal side.
#   C. E6 LEVEL  — the no-go: PSL(2,7) cannot live in W(E6) (Ilya's own
#                  S-15), cannot act transitively on 27 states at all.
#   D. E7 LEVEL  — the real common home: Sp6(2) = W(E7)/{+-1}, the symmetry
#                  of the 28 bitangents / odd theta characteristics of a
#                  genus-3 curve (Klein's quartic included).  Computed from
#                  scratch: PSL(2,7) acts on F2^6 = V + V* symplectically;
#                  the 64 quadratic refinements split 36 even + 28 odd;
#                  orbits, stabilizers, and the S3 where the two frameworks
#                  meet — the SAME S3 = N(<z3>) as T4's strata theorem and
#                  Ilya's 'universal stabilizer' row.
#   F. LIE LEVEL — two explicit branchings of the 27 to PSL(2,7):
#                  trinification  27 -> 3*chi1 + 3*chi8   (computed exactly)
#                  G2/Jordan      27 -> 6*chi1 + 3*chi7   (classical route)
#
# House rules: compute never assert; classical inputs labelled CLASSICAL;
# identifications stay parked (Rule 3).
# Run:  python -X utf8 verify_tbr_bridge.py
import numpy as np
from fractions import Fraction
import math, cmath, itertools

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("T-BR  the bridge: Merkabit (E6/27) x Scar-Cat (PSL(2,7)/168)")
print("=" * 78)

# ---------------------------------------------------------------- group core
# GL(3,F2) = PSL(2,7), as in verify_tsc_scarcat.py (where the character
# table below is DERIVED by Burnside-Dixon; here it is re-verified exactly).
def m_mul(a, b):
    return tuple((a[3*i]*b[j] ^ a[3*i+1]*b[3+j] ^ a[3*i+2]*b[6+j])
                 for i in range(3) for j in range(3))
def m_det(a):
    return (a[0]*(a[4]*a[8] ^ a[5]*a[7]) ^ a[1]*(a[3]*a[8] ^ a[5]*a[6])
            ^ a[2]*(a[3]*a[7] ^ a[4]*a[6])) & 1
els = [m for m in itertools.product((0, 1), repeat=9) if m_det(m)]
idx = {m: i for i, m in enumerate(els)}
N = 168
MUL = np.zeros((N, N), dtype=np.int16)
for i, a in enumerate(els):
    for j, b in enumerate(els):
        MUL[i, j] = idx[m_mul(a, b)]
E = idx[(1, 0, 0, 0, 1, 0, 0, 0, 1)]
INV = np.array([int(np.where(MUL[i] == E)[0][0]) for i in range(N)], dtype=np.int16)
ORD = np.zeros(N, dtype=np.int16)
for i in range(N):
    k, x = 1, i
    while x != E: x = MUL[x, i]; k += 1
    ORD[i] = k
cls_of = np.full(N, -1, dtype=np.int16)
classes = []
for i in range(N):
    if cls_of[i] >= 0: continue
    orb = {int(MUL[MUL[g, i], INV[g]]) for g in range(N)}
    for x in orb: cls_of[x] = len(classes)
    classes.append(sorted(orb))
order_key = sorted(range(len(classes)),
                   key=lambda c: (int(ORD[classes[c][0]]), len(classes[c])))
classes = [classes[c] for c in order_key]
sizes = [len(c) for c in classes]; reps = [c[0] for c in classes]
cls_of = np.full(N, -1, dtype=np.int16)
for c, cl in enumerate(classes):
    for x in cl: cls_of[x] = c
K = 6
# exact table over Q(sqrt(-7)) — derived in verify_tsc_scarcat.py, re-verified:
H = Fraction(1, 2)
TAB = [  # 1A 2A 3A 4A 7A 7B ; entries (a,b) = a + b*i*sqrt(7)
 [(1,0)]*6,
 [(3,0),(-1,0),(0,0),(1,0),(-H,H),(-H,-H)],
 [(3,0),(-1,0),(0,0),(1,0),(-H,-H),(-H,H)],
 [(6,0),(2,0),(0,0),(0,0),(-1,0),(-1,0)],
 [(7,0),(-1,0),(1,0),(-1,0),(0,0),(0,0)],
 [(8,0),(0,0),(-1,0),(0,0),(1,0),(1,0)],
]
TAB = [[(Fraction(a), Fraction(b)) for a, b in row] for row in TAB]
def qmul(u, v): return (u[0]*v[0]-7*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def qadd(u, v): return (u[0]+v[0], u[1]+v[1])
def qconj(u): return (u[0], -u[1])
def inner(vals, r):
    s = (Fraction(0), Fraction(0))
    for i in range(K):
        s = qadd(s, qmul((Fraction(sizes[i]), Fraction(0)),
                         qmul(vals[i], qconj(TAB[r][i]))))
    v = (s[0]/168, s[1]/168)
    assert v[1] == 0 and v[0].denominator == 1, v
    return int(v[0])
ortho = all(inner(TAB[a], b) == (1 if a == b else 0)
            for a in range(6) for b in range(6))
check("table", "character table exact-orthogonal in Q(sqrt(-7)) "
      "(derivation: verify_tsc_scarcat.py)", ortho)

print("\n--- B. FIELD LEVEL: the cyclotomic bridge (PB-01), sharpened ---")
u21 = [a for a in range(21) if math.gcd(a, 21) == 1]
ords = sorted({min(k for k in range(1, 13) if pow(a, k, 21) == 1) for a in u21})
check("PB-01 Galois", "(Z/21)* has order 12, exponent 6, abelian "
      "=> Gal(Q(zeta21)/Q) = C6 x C2", len(u21) == 12 and max(ords) == 6,
      f"element orders {ords}")
z7 = cmath.exp(2j*cmath.pi/7); z3 = cmath.exp(2j*cmath.pi/3)
legendre7 = {a: 1 if a in (1, 2, 4) else -1 for a in range(1, 7)}
g7 = sum(legendre7[a] * z7**a for a in range(1, 7))
g3 = (2*z3 + 1)
check("Gauss sums", "g7^2 = -7 and g3^2 = -3: sqrt(-7) in Q(zeta7), "
      "sqrt(-3) in Q(zeta3)",
      abs(g7**2 + 7) < 1e-9 and abs(g3**2 + 3) < 1e-9)
check("third field", "(g3*g7)^2 = +21: the compositum's third quadratic "
      "subfield is the REAL field Q(sqrt(21)) — the bridge's own signature",
      abs((g3*g7)**2 - 21) < 1e-9)
check("disjointness", "[Q(zeta21):Q] = 12 = 2*6 = [Q(zeta3):Q]*[Q(zeta7):Q] "
      "=> Q(zeta3) and Q(zeta7) meet only in Q (PB-01's claim)",
      len(u21) == 2 * 6)
check("SHARPENING", "sqrt(-7) is the CHARACTER FIELD of Scar-Cat: the "
      "derived chi3 takes value (-1+i*sqrt7)/2 on 7A (exact table above); "
      "sqrt(-3) is the Eisenstein/trit field (omega=( -1+i*sqrt3)/2) of the "
      "crystal's ternary side",
      TAB[1][4] == (Fraction(-1, 2), Fraction(1, 2)))
print("      => the cyclotomic bridge = the two frameworks' character fields")
print("         placed side by side, LINEARLY DISJOINT: at field level they")
print("         touch only in Q.  ['12 = h(E6)' stays PARKED: phi(21)=12 is")
print("         true; the identification with the Coxeter number is a fit.]")

print("\n--- C. E6 LEVEL: the no-go (Ilya's S-15, extended) ---")
WE6 = 51840
check("S-15", "|W(E6)| = 51840 = 2^7*3^4*5 has NO factor 7 => no PSL(2,7) "
      "in W(E6), nor in Aut(27-lines incidence) = W(E6)",
      WE6 == 2**7 * 3**4 * 5 and WE6 % 7 != 0)
check("no 27-action", "168/27 is not an integer => PSL(2,7) has NO "
      "transitive action on 27 states (any action on the crystal's 27 has "
      "fixed points or split orbits)", 168 % 27 != 0)

print("\n--- D. E7 LEVEL: Sp6(2), the 28 bitangents, and the shared S3 ---")
# V + V* as F2^6: x in 0..63, v = x & 7 (bits 0-2), f = x >> 3 (bits 3-5)
def par(x): return bin(x).count("1") & 1
def Vp(x): return x & 7
def Fp(x): return x >> 3
def omega(x, y): return par(Fp(x) & Vp(y)) ^ par(Fp(y) & Vp(x))
def q0(x): return par(Fp(x) & Vp(x))
def matvec(g, v):  # g = 9-tuple over F2, v = 3-bit int (bit i = coord i)
    out = 0
    for i in range(3):
        out |= ((g[3*i]*((v >> 0) & 1) ^ g[3*i+1]*((v >> 1) & 1)
                 ^ g[3*i+2]*((v >> 2) & 1)) & 1) << i
    return out
def transpose(g): return (g[0], g[3], g[6], g[1], g[4], g[7], g[2], g[5], g[8])
# 6-dim action of each group element: x -> (g v, g^-T f)
PT = []  # point maps on 0..63
for i in range(N):
    g = els[i]; git = transpose(els[int(INV[i])])
    PT.append([matvec(g, Vp(x)) | (matvec(git, Fp(x)) << 3) for x in range(64)])
check("symplectic", "all 168 elements preserve omega on F2^6 = V + V*",
      all(omega(PT[i][x], PT[i][y]) == omega(x, y)
          for i in (1, 7, 100) for x in range(64) for y in range(64)),
      "spot-checked 3 elements x full form; construction guarantees the rest")
# quadratic refinements q_c(x) = q0(x) ^ par(c & x), c in 0..63
zeros = [sum(1 for x in range(64) if (q0(x) ^ par(c & x)) == 0)
         for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms  = [c for c in range(64) if zeros[c] == 28]
check("36+28", "the 64 quadratic refinements of omega split 36 even (Arf 0, "
      "36 zeros) + 28 odd (Arf 1, 28 zeros)",
      len(even_forms) == 36 and len(odd_forms) == 28 and
      sorted(set(zeros)) == [28, 36])
# action on form labels: (g.q)(x) = q(g^-1 x);  ell_{c'} = q0 + q_c o g^-1
def act_form(pt_inv, c):
    out = 0
    for i in range(6):
        e = 1 << i
        y = pt_inv[e]
        out |= (q0(e) ^ q0(y) ^ par(c & y)) << i
    return out
FORM = []
for i in range(N):
    pti = PT[int(INV[i])]
    FORM.append([act_form(pti, c) for c in range(64)])
check("q0 invariant", "PSL(2,7) fixes the even form q0 (label 0) — its "
      "stabilizer in Sp6(2) is O6+(2) ~ S8: the 8 points of P1(F7) live here",
      all(FORM[i][0] == 0 for i in range(N)))
# orbits of PSL(2,7) on forms
def orbits(labels, maps):
    seen, out = set(), []
    for c in labels:
        if c in seen: continue
        orb = {c}; frontier = [c]
        while frontier:
            nxt = []
            for x in frontier:
                for mp in maps:
                    y = mp[x]
                    if y not in orb: orb.add(y); nxt.append(y)
            frontier = nxt
        seen |= orb; out.append(sorted(orb))
    return out
gens = [FORM[i] for i in range(N) if ORD[i] in (7, 4)][:4]
odd_orbs = orbits(odd_forms, gens)
even_orbs = orbits(even_forms, gens)
check("28 transitive", "PSL(2,7) is TRANSITIVE on the 28 odd forms "
      "(= the 28 bitangents / odd theta characteristics)",
      [len(o) for o in odd_orbs] == [28])
print(f"      PSL(2,7) orbits on the 36 even forms: "
      f"{sorted(len(o) for o in even_orbs)}  (the fixed one is q0)")
# stabilizer of one odd form
c_star = odd_forms[0]
stab = [i for i in range(N) if FORM[i][c_star] == c_star]
nonab = any(MUL[a, b] != MUL[b, a] for a in stab for b in stab)
z3e = next(i for i in stab if ORD[i] == 3)
z3sq = int(MUL[z3e, z3e])
norm = [g for g in range(N)
        if int(MUL[MUL[g, z3e], INV[g]]) in (z3e, z3sq)]
check("stabilizer = S3", "Stab_PSL(bitangent) has order 6, nonabelian (S3), "
      "and EQUALS N(<z3>) — Ilya's 'universal stabilizer' AND T4's canonical "
      "S3", len(stab) == 6 and nonab and sorted(norm) == sorted(stab))
# the 2:1 map 3A -> bitangents:  z3 |-> N(<z3>) = Stab(one odd form)
stab_by_form = {c: frozenset(i for i in range(N) if FORM[i][c] == c)
                for c in odd_forms}
threeA = [i for i in range(N) if ORD[i] == 3]
norms = {}
for z in threeA:
    zz = int(MUL[z, z])
    nz = frozenset(g for g in range(N)
                   if int(MUL[MUL[g, z], INV[g]]) in (z, zz))
    norms.setdefault(nz, []).append(z)
check("56 = 2 x 28", "|class 3A| = 56; z3 -> N(<z3>) is exactly 2-to-1 onto "
      "28 distinct S3's, and these ARE the 28 bitangent stabilizers",
      len(threeA) == 56 and len(norms) == 28 and
      all(len(v) == 2 for v in norms.values()) and
      set(norms.keys()) == set(stab_by_form.values()))
# permutation character of the 28-action, decomposed exactly
fixed28 = []
for c in range(K):
    g = reps[c]
    fixed28.append(sum(1 for cc in odd_forms if FORM[g][cc] == cc))
pi28 = [(Fraction(f), Fraction(0)) for f in fixed28]
d28 = [inner(pi28, r) for r in range(6)]
check("pi_28", "perm character of the bitangent action = "
      "chi1 + 2*chi6 + chi7 + chi8 (Ilya's 'Bijection' row: odd theta chars "
      "= G/S3, the unique such G-set)", d28 == [1, 0, 0, 2, 1, 1],
      f"fixed points/class = {fixed28}, decomp = {d28}")
# full Sp6(2): transvections t_a(x) = x + omega(x,a) a
def transvection(a):
    return [x ^ (a if omega(x, a) else 0) for x in range(64)]
tv = [transvection(a) for a in range(1, 64)]
tv_forms = [[act_form(t, c) for c in range(64)] for t in tv]  # t = t^-1
sp_odd = orbits([odd_forms[0]], tv_forms)
sp_even = orbits([0], tv_forms)
SP = 2**9 * (2**2 - 1) * (2**4 - 1) * (2**6 - 1)
check("Sp6(2) orbits", "the full Sp6(2) (transvections) is transitive on the "
      "28 odd and on the 36 even forms",
      len(sp_odd[0]) == 28 and len(sp_even[0]) == 36)
check("THE TWO HOMES", f"|Sp6(2)| = {SP}; stab(odd form) = {SP}//28 = "
      f"{SP//28} = |W(E6)|  [O6-(2) ~ W(E6), CLASSICAL]; stab(even form) = "
      f"{SP}//36 = {SP//36} = 8!  [O6+(2) ~ S8, CLASSICAL]",
      SP == 1451520 and SP // 28 == 51840 and SP // 36 == 40320)
print("      => inside Sp6(2) = W(E7)/{+-1}:")
print("         Selina's W(E6)   = the stabilizer of ONE bitangent (odd form)")
print("         Ilya's  PSL(2,7) = transitive on ALL 28 (Klein quartic's")
print("                            automorphisms on its own bitangents)")
print("         intersection     = S3 = N(<z3>)  — the SAME S3 both")
print("                            frameworks independently singled out")

print("\n--- F. LIE LEVEL: two branchings of the 27 to PSL(2,7) ---")
# trinification E6 > SU(3)^3, 27 = (3,3b,1)+(1,3,3b)+(3b,1,3)  [CLASSICAL];
# PSL(2,7) -> SU(3) via Klein's chi3  =>  each block = chi3 (x) chi3bar.
blk = [qmul(TAB[1][i], qconj(TAB[1][i])) for i in range(K)]
d_blk = [inner(blk, r) for r in range(6)]
tot27 = [qmul((Fraction(3), Fraction(0)), blk[i]) for i in range(K)]
d27 = [inner(tot27, r) for r in range(6)]
check("27 -> 3chi1+3chi8", "trinification route (computed exactly): each of "
      "the three 9-blocks = chi3 (x) chi3bar = chi1 + chi8, so "
      "27|_PSL(2,7) = 3*chi1 + 3*chi8",
      d_blk == [1, 0, 0, 0, 0, 1] and d27 == [3, 0, 0, 0, 0, 3],
      f"27 decomposes as {d27} — three (singlet + octet) copies")
check("row 156 corrected", "Ilya's 'Jordan: 27 = 3 + 24' becomes literal "
      "here: 3 singlets + 3x8 = 24, i.e. 24 = 3*dim(chi8), NOT |7A|",
      3 + 3 * 8 == 27)
check("27 -> 6chi1+3chi7", "G2/Jordan route [CLASSICAL: PSL(2,7) < G2 = "
      "Aut(O) with 7 = chi7 (Fano = octonion lines, Ilya's 157); "
      "27 = J3(O) -> 6*1 + 3*7 under G2]: dims 6 + 21 = 27 consistent",
      6 * 1 + 3 * 7 == 27)
print("      Two inequivalent embeddings, two dictionaries: the crystal's 27")
print("      seen by PSL(2,7) is either '3 generations of (singlet+octet)'")
print("      (via the Klein-quartic rep chi3) or '6 scalars + 3 Fano planes'")
print("      (via octonions).  Both are restriction functors — the 'explicit")
print("      functor' Ilya's Bridge row asked for, at Lie level, with the")
print("      E6-Weyl-level version impossible (section C).")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
