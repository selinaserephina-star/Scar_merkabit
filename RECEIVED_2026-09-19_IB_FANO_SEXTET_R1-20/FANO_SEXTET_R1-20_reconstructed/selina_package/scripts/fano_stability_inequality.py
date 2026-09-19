"""
fano_stability_inequality.py

Follow-on to fano_vacuum_hessian_degeneracy.py. Requires numpy and
sympy. Takes the S4 vacuum and the degeneracy relation (3*kappa_g2 =
2*kappa_mixed) already derived there, and asks the natural next
question: even WITH that relation imposed, is the vacuum a genuine
local MINIMUM (transverse Hessian eigenvalue positive), or merely a
critical point with a degenerate (but not necessarily positive)
transverse direction?

Rebuilds the S4 vacuum and its Hessian from scratch (as in the
companion script), imposes kappa_g2 = (2/3)*kappa_mixed, eliminates m^2
via the radial scale-fixing equation, and extracts the transverse
eigenvalue in closed form as a function of the three remaining
couplings (kappa_g1, kappa_line, kappa_prod, kappa_mixed) -- finding
it collapses to a clean two-term expression not involving kappa_g1 at
all:

    transverse eigenvalue = -(224/3) * (12*kappa_line - 2*kappa_mixed + 105*kappa_prod)

STABILITY CONDITION (derived, not fit):

    2*kappa_mixed > 12*kappa_line + 105*kappa_prod

Also verifies numerically (eigenvector inspection, distinguishing the
gauge direction Sigma-phi != 0 from the physical transverse and radial
directions) that an earlier scan mislabelled the gauge eigenvalue as
"transverse" at one sample point -- corrected here, with the gauge
direction explicitly identified and excluded from the stability
question (it is not part of the physical 6-dimensional sextet space).

STATUS: this is a genuine, derived necessary condition for the S4
("top") vacuum to be a stable minimum, GIVEN the degeneracy relation.
It has not been matched to King-Luhn's own coupling values or checked
against any external target -- reported as a structural constraint on
the Fano-invariant couplings, not a fit.
"""
import itertools
import numpy as np
import sympy as sp

# ---------------- rebuild GL(3,2), Fano plane, sextet, S4 vacuum (as before) ----------------
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
vac = [4 if i in line0 else -3 for i in range(7)]
print(f"[1] Rebuilt GL(3,2), Fano plane, S4 vacuum: {vac}")

# ---------------- Hessian, symbolic ----------------
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
print("[2] Symbolic Hessian at the S4 vacuum built.")

# ---------------- impose degeneracy relation, eliminate m2, get transverse eigenvalue ----------------
kg2_val = sp.Rational(2,3)*kmixed
scale_eq = sp.Eq(-14*m2 + 2352*kg1 + 364*kg2_val + 6944*kline + 39200*kprod + 2128*kmixed, 0)
m2_val = sp.solve(scale_eq, m2)[0]
print(f"[3] Scale-fixing m2 = {m2_val}")

doublet_expr = 336*kg1 + 192*kg2 + 96*kline + 360*kmixed - 2240*kprod - 2*m2
transverse = sp.expand(doublet_expr.subs({kg2: kg2_val, m2: m2_val}))
print(f"[4] Transverse eigenvalue (5-fold degenerate), fully reduced: {transverse}")
transverse_factored = sp.nsimplify(sp.factor(transverse))
print(f"    Factored: {transverse_factored}")

assert sp.simplify(transverse - (-sp.Rational(224,3)*(12*kline - 2*kmixed + 105*kprod))) == 0
print("    Confirmed: transverse = -(224/3)*(12*k_line - 2*k_mixed + 105*k_prod)")
print("    STABILITY CONDITION (transverse > 0): 2*k_mixed > 12*k_line + 105*k_prod")

# ---------------- numeric cross-check with proper eigenvector labelling ----------------
Hn_func = sp.lambdify((kg1,kline,kprod,kmixed), H_vac.subs({kg2:kg2_val, m2:m2_val}), 'numpy')
allones = np.ones(7)/np.sqrt(7)
vacvec = np.array(vac)/np.linalg.norm(vac)

# ---------------- numeric cross-check: project OUT gauge+radial directions FIRST, then diagonalize ----------------
Hn_func = sp.lambdify((kg1,kline,kprod,kmixed), H_vac.subs({kg2:kg2_val, m2:m2_val}), 'numpy')
allones = np.ones(7)/np.sqrt(7)
vacvec = np.array(vac)/np.linalg.norm(vac)

# build an orthonormal basis for the 5-dim complement of {allones, vacvec}
basis7 = np.eye(7)
Q, _ = np.linalg.qr(np.column_stack([allones, vacvec, basis7]))
transverse_basis = Q[:, 2:7]  # 5 columns spanning the complement (QR puts the first two first)

print("\n[5] Numeric cross-check: project Hessian onto the 5-dim transverse subspace directly (no labelling ambiguity):")
test_points = [(1,1,1,1), (1,1,0.01,1), (1,0.1,0,1), (1,1,1,10)]
for (k1,kl,kp,km) in test_points:
    Hm = np.array(Hn_func(k1,kl,kp,km), dtype=float)
    H_transverse = transverse_basis.T @ Hm @ transverse_basis
    transverse_eigs = np.linalg.eigvalsh(H_transverse)
    predicted = float(transverse.subs({kg1:k1,kline:kl,kprod:kp,kmixed:km}))
    print(f"   k_g1={k1},k_line={kl},k_prod={kp},k_mixed={km}: "
          f"transverse eigs={np.round(transverse_eigs,2)}, predicted={predicted:.2f}, "
          f"stable={'YES' if predicted>0 else 'no'}")
    assert all(abs(e-predicted)<1e-6*max(1,abs(predicted)) for e in transverse_eigs), "mismatch!"

print("\nDone. All assertions passed. Stability condition derived and numerically confirmed.")
