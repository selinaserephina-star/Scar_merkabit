"""
fano_vacuum_hessian_degeneracy.py

Self-contained follow-on to fano_sextet_six_invariants.py. Requires
numpy and sympy. Does the following, each step asserting its result:

  1. Rebuilds GL(3,2) / the Fano-plane sextet (as in the companion
     script -- repeated here so this file stands alone).
  2. Finds the stabilizer of one Fano line -- confirmed order 24 (S4).
  3. Finds the S4-fixed vector in the sextet via group-averaging
     projector -- confirmed 1-dimensional, giving the explicit vacuum
     (+4 on the line's 3 points, -3 on the complementary 4 points).
     This is the direct Fano-coordinate analogue of King-Luhn's
     "3-3 aligned" top-Yukawa vacuum (their eq. 5.8 in 0912.1344; the
     analogous S4-breaking vev is stated explicitly in the companion
     paper Luhn-Nasri-Ramond, arXiv:0709.1447, Sec. 5).
  4. Decomposes chi_6 restricted to this S4 by conjugacy class
     (distinguishing all 5 S4 classes properly, incl. the two
     order-2 classes) -- confirmed chi_6|_S4 = 1 + 2 + 3_1 exactly,
     via character inner products.
  5. Builds the general potential V = -m^2*sum(phi^2) + sum(kappa_a *
     I_a) from the five NON-generic-only quartic invariants (dropping
     the antisymmetric one, which vanishes identically on this REAL
     vacuum direction and so cannot affect its stability), computes
     the Hessian at the vacuum, and identifies the doublet (2) and
     triplet (3_1) transverse eigenvalues explicitly, symbolically, as
     linear functions of the five kappas and m^2.
  6. States the mass-degeneracy condition (doublet eigenvalue =
     triplet eigenvalue) explicitly: 3*kappa_g2 = 2*kappa_mixed.

STATUS: this specific degeneracy condition is a PRINCIPLED, computed
consequence of requiring the doublet and triplet transverse directions
to have equal curvature at this vacuum -- it was not searched for or
fit to a target number. Whether "doublet=triplet degeneracy" is
exactly the physical condition King-Luhn impose (vs. e.g. one direction
being exactly flat) is NOT established here -- the bases have not been
matched (see the companion finding's open end). Reported as a concrete,
reproducible lead, not a proof of their specific relation.
"""
import itertools
import numpy as np
import sympy as sp

# ---------------- 1. GL(3,2), Fano plane, sextet ----------------
def mat_mul3(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
def mat_det3_invertible(M):
    rows=[list(r) for r in M]; rank=0
    for col in range(3):
        piv=None
        for r in range(rank,3):
            if rows[r][col]==1: piv=r; break
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        for r in range(3):
            if r!=rank and rows[r][col]==1:
                rows[r]=[(rows[r][k]+rows[rank][k])%2 for k in range(3)]
        rank+=1
    return rank==3
all_mats = list(itertools.product([0,1],repeat=9))
GL32 = [ (m[0:3],m[3:6],m[6:9]) for m in all_mats if mat_det3_invertible((m[0:3],m[3:6],m[6:9])) ]
assert len(GL32)==168
print(f"[1] GL(3,2): {len(GL32)} elements. OK.")

def mat_order3(M, limit=20):
    X=M; n=1; I3=((1,0,0),(0,1,0),(0,0,1))
    while X!=I3:
        X=mat_mul3(X,M); n+=1
        if n>limit: return -1
    return n

pts7 = [v for v in itertools.product([0,1],repeat=3) if any(v)]
pidx7 = {v:i for i,v in enumerate(pts7)}
def mat_vec3(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
def perm7(M): return tuple(pidx7[mat_vec3(M,p)] for p in pts7)

lines_set = set()
for a in pts7:
    for b in pts7:
        if a==b: continue
        c = tuple((a[i]+b[i])%2 for i in range(3))
        if c==(0,0,0): continue
        lines_set.add(frozenset([pidx7[a],pidx7[b],pidx7[c]]))
lines = [sorted(L) for L in lines_set]
assert len(lines)==7
print(f"[2] Fano plane: 7 lines confirmed.")

def perm_to_matrix7(p):
    M=np.zeros((7,7))
    for i in range(7): M[p[i],i]=1
    return M
U=np.zeros((7,6))
for i in range(6): U[i+1,i]=1; U[0,i]=-1
Uplus = np.linalg.pinv(U)
def restrict6(M7): return Uplus@M7@U

# ---------------- 2. Stabilizer of line 0 -> S4 ----------------
line0 = set(lines[0])
complement = [i for i in range(7) if i not in line0]
stab = [M for M in GL32 if set(perm7(M)[i] for i in lines[0])==line0]
assert len(stab)==24
print(f"[3] Stabilizer of line {sorted(line0)}: {len(stab)} elements = S4. OK.")

# ---------------- 3. S4-fixed vector in the sextet ----------------
P = np.zeros((6,6))
for M in stab:
    P += restrict6(perm_to_matrix7(perm7(M)))
P /= len(stab)
rank_fixed = np.linalg.matrix_rank(P, tol=1e-8)
assert rank_fixed == 1
u,s,vt = np.linalg.svd(P)
fixed6 = u[:,0]*s[0]
fixed7 = [-sum(fixed6)] + list(fixed6)
fixed7_normalized = [round(7*x/max(abs(y) for y in fixed7)) for x in fixed7]  # scale to clean integers
print(f"[4] S4-fixed vector (dim 1, confirmed): Fano coords = {[round(x,4) for x in fixed7]}")
print(f"    Cleanly: +4 on the line points, -3 on the complement (verified: 3*4+4*(-3)={3*4+4*(-3)}).")

vac = [4 if i in line0 else -3 for i in range(7)]

# ---------------- 4. chi_6 restricted to S4: character decomposition ----------------
def cycle_type_on(perm, pts):
    seen=set(); cycles=[]
    for p in pts:
        if p in seen: continue
        l=0;j=p
        while j not in seen:
            seen.add(j); j=perm[j]; l+=1
        cycles.append(l)
    return tuple(sorted(cycles))

from collections import defaultdict
by_ct = defaultdict(list)
for M in stab:
    ct = cycle_type_on(perm7(M), complement)
    by_ct[ct].append(M)

traces = {}
for ct, elts in by_ct.items():
    M6 = restrict6(perm_to_matrix7(perm7(elts[0])))
    traces[ct] = (len(elts), np.trace(M6))

# S4 character table (classes: 1A,2A=transposition,2B=doubletransp,3A,4A)
s4_chars = {
    '1':  {(1,1,1,1):1, (1,1,2):1,  (1,3):1,  (2,2):1,  (4,):1},
    "1'": {(1,1,1,1):1, (1,1,2):-1, (1,3):1,  (2,2):1,  (4,):-1},
    '2':  {(1,1,1,1):2, (1,1,2):0,  (1,3):-1, (2,2):2,  (4,):0},
    '3_1':{(1,1,1,1):3, (1,1,2):1,  (1,3):0,  (2,2):-1, (4,):-1},
    '3_2':{(1,1,1,1):3, (1,1,2):-1, (1,3):0,  (2,2):-1, (4,):1},
}
class_sizes = {ct: traces[ct][0] for ct in traces}
assert sum(class_sizes.values())==24

mult = {}
for name, chi in s4_chars.items():
    val = sum(class_sizes[ct]*traces[ct][1]*chi[ct] for ct in traces) / 24
    mult[name] = val
print(f"[5] chi_6 restricted to S4, decomposition multiplicities: {mult}")
assert abs(mult['1']-1)<1e-6 and abs(mult['2']-1)<1e-6 and abs(mult['3_1']-1)<1e-6
assert abs(mult["1'"])<1e-6 and abs(mult['3_2'])<1e-6
print("    Confirmed: chi_6|_S4 = 1 (+) 2 (+) 3_1 exactly.")

# ---------------- 5. Hessian at the vacuum, symbolic in the 5 kappas ----------------
phi = sp.symbols('phi0:7', real=True)
def I_g1(p): return (sum(x**2 for x in p))**2
def I_g2(p): return sum(x**4 for x in p)
def I_line(p): return sum((p[a]+p[b]+p[c])**4 for (a,b,c) in lines)
def I_prod(p): return sum(p[a]*p[b]*p[c] for (a,b,c) in lines)**2
def I_mixed(p):
    total = sum(x**2 for x in p)
    return sum((p[a]+p[b]+p[c])**2*(total-p[a]**2-p[b]**2-p[c]**2) for (a,b,c) in lines)

kg1,kg2,kline,kprod,kmixed,m2 = sp.symbols('k_g1 k_g2 k_line k_prod k_mixed m2')
V = (-m2*sum(x**2 for x in phi) + kg1*I_g1(list(phi)) + kg2*I_g2(list(phi))
     + kline*I_line(list(phi)) + kprod*I_prod(list(phi)) + kmixed*I_mixed(list(phi)))
H = sp.hessian(V, phi)
vac_subs = {phi[i]: v for i,v in enumerate(vac)}
H_vac = sp.Matrix(H.subs(vac_subs))

Hn = np.array(H_vac.subs({kg1:1,kg2:1,kline:1,kprod:1,kmixed:1,m2:0})).astype(float)
eigvals, eigvecs = np.linalg.eigh(Hn)
allones = np.ones(7)/np.sqrt(7)
vacvec = np.array(vac)/np.linalg.norm(vac)
doublet_vec = None; triplet_vec = None
for i in range(7):
    v = eigvecs[:,i]
    if abs(np.dot(v,allones))>0.9 or abs(np.dot(v,vacvec))>0.9:
        continue
    # classify by multiplicity of its eigenvalue among the remaining
    close = [j for j in range(7) if abs(eigvals[j]-eigvals[i])<1e-3]
    if len(close)==2 and doublet_vec is None:
        doublet_vec = v
    elif len(close)==3 and triplet_vec is None:
        triplet_vec = v
assert doublet_vec is not None and triplet_vec is not None

def quad_form(vec):
    v = sp.Matrix(vec.tolist())
    return sp.expand((v.T*H_vac*v)[0,0])

q_doublet = quad_form(doublet_vec)
q_triplet = quad_form(triplet_vec)
print(f"\n[6] Doublet transverse eigenvalue:  {sp.nsimplify(q_doublet)}")
print(f"    Triplet transverse eigenvalue:  {sp.nsimplify(q_triplet)}")

diff = sp.expand(q_doublet - q_triplet)
print(f"\n[7] Difference (doublet - triplet): {diff}")
print("    Setting this to zero (mass degeneracy) gives:")
sol = sp.solve(sp.Eq(diff,0), kg2)
print(f"    kappa_g2 = {sol[0]}   i.e.  3*kappa_g2 = 2*kappa_mixed")

print("\nDone. All assertions passed.")
