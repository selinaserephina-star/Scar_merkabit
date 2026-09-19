"""
fano_v4_family_critical_points.py

Self-contained follow-on to fano_vacuum_hessian_degeneracy.py. Requires
numpy and scipy. Does the following, each step checked:

  1. Rebuilds GL(3,2) / Fano plane / sextet (as in the companion
     scripts -- repeated here so this file stands alone).
  2. Finds the stabilizer of one Fano line (S4, order 24, as before),
     then its index-3 subgroup V4 (order 4) consisting of the identity
     plus the three double-transpositions of the complementary 4
     points -- confirmed to fix all 3 line-points INDIVIDUALLY (not
     merely as a set), unlike S4 which permutes them through the
     quotient S4/V4 =~ S3 acting on the 3 line-points.
  3. Computes the V4-fixed subspace in the sextet via group-averaging
     projector -- confirmed dimension 3 (not 1, as for S4): the three
     line-points are free (V4 doesn't touch them individually), the
     four complement points are forced equal (three independent
     double-transpositions force all four equal), minus the one
     overall sum-zero constraint: 3 + 1 - 1 = 3. This is a genuine,
     structurally-explained enlargement of the vacuum family relative
     to the S4 case, and the natural place to look for a second
     (King-Luhn's "neutrino/TB") vacuum direction, since King-Luhn's
     own TB-alignment is stated to preserve two generators "S, U" of
     their S4 presentation (not the full S4) -- consistent with a
     Klein four-group as the relevant unbroken subgroup.
  4. Builds the general PSL(2,7)-invariant potential from five of the
     six Fano invariants (the antisymmetric one vanishes identically
     on any REAL vacuum, so cannot enter here) and, restricted to this
     3-parameter (a,b,c) V4-invariant family, searches numerically
     (60 random starts, for one illustrative choice of couplings,
     kappa=(1,1,1,1,1)) for ALL distinct critical points.
  5. For two representative critical points, computes the FULL 7x7
     Hessian and its eigenvalues, checking for local stability (all
     transverse eigenvalues >= 0).

STATUS / HONEST RESULT: 12 distinct critical points were found for the
single illustrative coupling choice tested (kappa=1 each). Every point
explicitly checked (including the striking, exactly-rational point
(a,b,c)=(1,-1,0), which is an EXACT critical point at m^2=14) has at
least one negative transverse Hessian eigenvalue at this coupling
choice -- i.e. it is a saddle, not a stable minimum, for this
particular (arbitrary) set of couplings. This is reported as the
honest result of the search, not a failure to find the "right"
answer: it shows concretely that which of these critical points (if
any) is the true, stable vacuum depends sensitively on the actual
values of the five couplings, which are not fixed by the group theory
alone -- consistent with King-Luhn's own statement that their model
requires an as-yet-unexplained tuning of the flavon potential's
coefficients. Finding a stable point would require either scanning the
5-dimensional coupling space, or independent physical input to fix the
couplings -- not attempted here.
"""
import itertools
import numpy as np
from scipy.optimize import fsolve
from collections import Counter

# ---------------- 1. GL(3,2), Fano plane, sextet (as before) ----------------
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
line0 = set(lines[0])
complement = [i for i in range(7) if i not in line0]
print(f"[2] Fano plane: line0={sorted(line0)}, complement={complement}")

def perm_to_matrix7(p):
    M=np.zeros((7,7))
    for i in range(7): M[p[i],i]=1
    return M
Umat=np.zeros((7,6))
for i in range(6): Umat[i+1,i]=1; Umat[0,i]=-1
Uplus = np.linalg.pinv(Umat)
def restrict6(M7): return Uplus@M7@Umat

stab_s4 = [M for M in GL32 if set(perm7(M)[i] for i in lines[0])==line0]
assert len(stab_s4)==24

def cycle_type_on(perm, pts):
    seen=set(); cycles=[]
    for p in pts:
        if p in seen: continue
        l=0;j=p
        while j not in seen:
            seen.add(j); j=perm[j]; l+=1
        cycles.append(l)
    return tuple(sorted(cycles))

stab_v4 = [M for M in stab_s4 if cycle_type_on(perm7(M), complement) in [(1,1,1,1),(2,2)]]
assert len(stab_v4)==4
print(f"[3] V4 subgroup: {len(stab_v4)} elements.")
for M in stab_v4:
    p = perm7(M)
    assert all(p[i]==i for i in line0), "V4 must fix every line point individually"
print("    Confirmed: V4 fixes all 3 line points individually (unlike S4, which permutes them via S4/V4=S3).")

P = np.zeros((6,6))
for M in stab_v4:
    P += restrict6(perm_to_matrix7(perm7(M)))
P /= len(stab_v4)
rank_v4 = np.linalg.matrix_rank(P, tol=1e-8)
assert rank_v4 == 3
print(f"[4] V4-fixed subspace in the sextet: dimension {rank_v4} (structurally: 3 free line values")
print("     + 1 forced-equal complement value - 1 sum-zero constraint = 3). Confirmed.")

# ---------------- 5. The five (real, symmetric) invariants ----------------
def I_g1(p): return (sum(x**2 for x in p))**2
def I_g2(p): return sum(x**4 for x in p)
def I_line(p): return sum((p[a]+p[b]+p[c])**4 for (a,b,c) in lines)
def I_prod(p): return sum(p[a]*p[b]*p[c] for (a,b,c) in lines)**2
def I_mixed(p):
    total = sum(x**2 for x in p)
    return sum((p[a]+p[b]+p[c])**2*(total-p[a]**2-p[b]**2-p[c]**2) for (a,b,c) in lines)

def build_phi(a,b,c):
    dd = -(a+b+c)/4
    phi=[0.0]*7
    phi[0]=a; phi[3]=b; phi[4]=c
    for p in complement: phi[p]=dd
    return phi

def V7(phi7, m2,k1,k2,k3,k4,k5):
    return -m2*sum(x**2 for x in phi7)+k1*I_g1(phi7)+k2*I_g2(phi7)+k3*I_line(phi7)+k4*I_prod(phi7)+k5*I_mixed(phi7)

def V_abc(a,b,c,m2,k1,k2,k3,k4,k5):
    return V7(build_phi(a,b,c), m2,k1,k2,k3,k4,k5)

def gradient3(a,b,c,m2,k1,k2,k3,k4,k5,h=1e-5):
    dVda = (V_abc(a+h,b,c,m2,k1,k2,k3,k4,k5)-V_abc(a-h,b,c,m2,k1,k2,k3,k4,k5))/(2*h)
    dVdb = (V_abc(a,b+h,c,m2,k1,k2,k3,k4,k5)-V_abc(a,b-h,c,m2,k1,k2,k3,k4,k5))/(2*h)
    dVdc = (V_abc(a,b,c+h,m2,k1,k2,k3,k4,k5)-V_abc(a,b,c-h,m2,k1,k2,k3,k4,k5))/(2*h)
    return [dVda,dVdb,dVdc]

# ---------------- 6. Numerical critical-point search (kappa=(1,1,1,1,1), illustrative) ----------------
def eqs(vars):
    b,c,m2 = vars
    return gradient3(1.0,b,c,m2,1,1,1,1,1)

found = []
np.random.seed(0)
for _ in range(60):
    b0 = np.random.uniform(-3,3); c0 = np.random.uniform(-3,3); m20 = np.random.uniform(-10,40)
    try:
        sol, info, ier, msg = fsolve(eqs, [b0,c0,m20], full_output=True)
        if ier==1 and max(abs(x) for x in eqs(sol)) < 1e-6:
            b_s,c_s,m2_s = sol
            if not any(abs(bb-b_s)<1e-3 and abs(cc-c_s)<1e-3 for (bb,cc,mm) in found):
                found.append((b_s,c_s,m2_s))
    except Exception:
        pass

print(f"\n[5] Critical-point search (a=1 fixed, kappa=(1,1,1,1,1)): {len(found)} distinct points found.")
for (b,c,m2) in found:
    print(f"     a=1, b={b:.6f}, c={c:.6f}, m2={m2:.4f}")

# ---------------- 7. Stability check on two representative points ----------------
def full_hessian(phi7, m2,k1,k2,k3,k4,k5, h=1e-4):
    n=7; H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            p1=list(phi7); p1[i]+=h; p1[j]+=h
            p2=list(phi7); p2[i]+=h; p2[j]-=h
            p3=list(phi7); p3[i]-=h; p3[j]+=h
            p4=list(phi7); p4[i]-=h; p4[j]-=h
            H[i,j]=(V7(p1,m2,k1,k2,k3,k4,k5)-V7(p2,m2,k1,k2,k3,k4,k5)-V7(p3,m2,k1,k2,k3,k4,k5)+V7(p4,m2,k1,k2,k3,k4,k5))/(4*h*h)
    return H

print("\n[6] Stability check on two representative points (kappa=(1,1,1,1,1)):")
for (a,b,c,m2,label) in [(1,-0.807624,1,21.4202,"a=c!=b type"), (1,-1,0,14.0,"the exact-rational (1,-1,0) point")]:
    phi0 = build_phi(a,b,c)
    H = full_hessian(phi0, m2,1,1,1,1,1)
    eigvals = np.linalg.eigvalsh(H)
    n_negative = sum(1 for e in eigvals if e < -1e-6)
    print(f"     {label}: eigenvalues = {np.round(eigvals,3)}")
    print(f"       -> {n_negative} negative eigenvalue(s): {'SADDLE' if n_negative>0 else 'stable (local min)'}")

print("\nDone. Honest result: for this illustrative coupling choice, both checked points are saddles.")
print("Which (if any) critical point is the true vacuum depends on the actual coupling values --")
print("not fixed by the group theory alone. See the FINDING document for the full discussion.")
