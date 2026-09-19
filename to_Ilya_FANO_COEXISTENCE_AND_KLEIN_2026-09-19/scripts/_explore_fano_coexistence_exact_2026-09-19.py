"""
_explore_fano_coexistence_exact_2026-09-19.py   [FREE EXPLORATION, NOT SEALED; Stenberg side with Claude]

independent, exact check of the S4/S2 coexistence claim
at the specific kappa_prod=0 point our FANO-QUARTIC-CORRECTION envelope named
(t=0.125 on the A->B path, kappa_prod set to 0, m^2 refixed by S4 criticality at scale 1),
and at the original Result-6 point (kappa_prod=-0.0069 kept).

Differences from BOTH sides' scripts:
  * Hessian is SYMBOLIC (sympy), not finite-difference.
  * Hessian is restricted to the 6-dim sum-zero sextet via an explicit orthonormal basis,
    so the spurious all-ones direction of R^7 is excluded (and reported separately).
  * Critical points are refined to 30 digits with mpmath before the Hessian is evaluated.
"""
import sympy as sp, mpmath as mp, numpy as np
mp.mp.dps = 30

lines=[[0,3,4],[1,3,5],[0,1,2],[2,4,5],[2,3,6],[0,5,6],[1,4,6]]
complement=[1,2,5,6]
x = sp.symbols('x0:7', real=True)
m2s, k1s, k2s, k3s, k4s, k5s = sp.symbols('m2 k1 k2 k3 k4 k5', real=True)

tot = sum(xi**2 for xi in x)
I_g1 = tot**2
I_g2 = sum(xi**4 for xi in x)
I_line = sum((x[a]+x[b]+x[c])**4 for (a,b,c) in lines)
I_prod = sum(x[a]*x[b]*x[c] for (a,b,c) in lines)**2
I_mixed = sum((x[a]+x[b]+x[c])**2*(tot-x[a]**2-x[b]**2-x[c]**2) for (a,b,c) in lines)
V = -m2s*tot + k1s*I_g1 + k2s*I_g2 + k3s*I_line + k4s*I_prod + k5s*I_mixed

Hsym = sp.hessian(V, x)
H_f_raw = sp.lambdify((x, m2s, k1s, k2s, k3s, k4s, k5s), Hsym, 'mpmath')
def H_f(phi, m2, *k):
    return np.array(H_f_raw(phi, m2, *k).tolist(), dtype=float)

# criticality is taken IN THE SEXTET: differentiate V along the V4-slice (a,b,c) -> phi(a,b,c),
# exactly as both sides' scripts do (a gradient proportional to the all-ones vector is allowed).
a_, b_, c_ = sp.symbols('a b c', real=True)
d_ = -(a_+b_+c_)/4
phi_sym = [a_, d_, d_, b_, c_, d_, d_]
V_abc = V.subs(dict(zip(x, phi_sym)))
grad_abc = [sp.diff(V_abc, v) for v in (a_, b_, c_)]
grad_abc_f = sp.lambdify(((a_, b_, c_), m2s, k1s, k2s, k3s, k4s, k5s), grad_abc, 'mpmath')
def grad_f(phi, m2, *k):
    # phi is in the slice: a=phi[0], b=phi[3], c=phi[4]; returns the 3 slice derivatives, padded to 7 slots
    g = grad_abc_f((phi[0], phi[3], phi[4]), m2, *k)
    return [g[0], 0, 0, g[1], g[2], 0, 0]

# orthonormal basis of the sum-zero subspace of R^7 (columns), plus the unit all-ones vector
ones = np.ones(7)/np.sqrt(7)
Qfull, _ = np.linalg.qr(np.column_stack([ones, np.eye(7)[:, :6]]))
Q6 = Qfull[:, 1:]                      # 7x6, orthonormal, orthogonal to ones
assert np.allclose(Q6.T @ ones, 0)

def phi_of(a,b,c):
    d=-(a+b+c)/4; p=[mp.mpf(0)]*7; p[0]=a; p[3]=b; p[4]=c
    for q in complement: p[q]=d
    return p

def hess6(phi, m2, k):
    H = np.array(H_f(phi, m2, *k), dtype=float)
    H6 = Q6.T @ H @ Q6
    e6 = np.linalg.eigvalsh(H6)
    e1 = float(ones @ H @ ones)        # the spurious direction, reported only
    return e6, e1

def refine_s4(m2, k):
    f = lambda r: grad_f(phi_of(r,r,r), m2, *k)[0]
    return mp.findroot(f, mp.mpf(1))

def refine_s2(m2, k, a0, b0):
    f = lambda a,b: (grad_f(phi_of(a,b,b), m2, *k)[0], grad_f(phi_of(a,b,b), m2, *k)[3])
    return mp.findroot(f, (mp.mpf(a0), mp.mpf(b0)))

def m2_for_s4_at_scale1(k):
    # V is quadratic in m2-linear: grad_0 at (1,1,1) is linear in m2 -> solve exactly
    g0 = grad_f(phi_of(1,1,1), mp.mpf(0), *k)[0]
    g1 = grad_f(phi_of(1,1,1), mp.mpf(1), *k)[0]
    return -g0/(g1-g0)

def report(label, k, m2, s2_guess):
    print(f"\n=== {label}")
    print(f"    kappa = (g1={k[0]}, g2={k[1]}, line={k[2]}, prod={k[3]}, mixed={k[4]}),  m2 = {mp.nstr(m2,12)}")
    r = refine_s4(m2, k); phi4 = phi_of(r,r,r)
    g = max(abs(v) for v in grad_f(phi4, m2, *k))
    e6, e1 = hess6(phi4, m2, k)
    print(f"    S4 point  a=b=c={mp.nstr(r,12)}   |grad|_max={mp.nstr(g,3)}")
    print(f"       6-dim Hessian eigenvalues: {np.array2string(e6, precision=4)}   (ones-direction: {e1:.3f})")
    print(f"       -> S4 {'STABLE' if e6.min()>0 else 'UNSTABLE'} (min = {e6.min():.5f})")
    a,b = refine_s2(m2, k, *s2_guess); phi2 = phi_of(a,b,b)
    g = max(abs(v) for v in grad_f(phi2, m2, *k))
    e6, e1 = hess6(phi2, m2, k)
    print(f"    S2 point  a={mp.nstr(a,12)}  b=c={mp.nstr(b,12)}   |grad|_max={mp.nstr(g,3)}")
    print(f"       6-dim Hessian eigenvalues: {np.array2string(e6, precision=4)}   (ones-direction: {e1:.3f})")
    print(f"       -> S2 {'STABLE' if e6.min()>0 else 'UNSTABLE'} (min = {e6.min():.5f})")
    print(f"    V(S4) = {mp.nstr(V_num(phi4,m2,k),10)}   V(S2) = {mp.nstr(V_num(phi2,m2,k),10)}")

V_f = sp.lambdify((x, m2s, k1s, k2s, k3s, k4s, k5s), V, 'mpmath')
def V_num(phi,m2,k): return V_f(phi,m2,*k)

kA = [mp.mpf(1), mp.mpf(2)/3, mp.mpf('0.1'), mp.mpf(0), mp.mpf(1)]
kB = [mp.mpf('1.933'), mp.mpf('0.890'), mp.mpf('0.697'), mp.mpf('-0.055'), mp.mpf('1.699')]
t = mp.mpf('0.125')
k_mid = [(1-t)*a_+t*b_ for a_,b_ in zip(kA,kB)]

# (1) the original Result-6 window point, sextic kept, m2 interpolated as in the original
m2A = m2_for_s4_at_scale1(kA); m2B = mp.mpf('4.368'); m2_mid = (1-t)*m2A + t*m2B
report("ORIGINAL Result-6 point (t=0.125, kappa_prod=-0.0069 kept, m2 interpolated)", k_mid, m2_mid, (1.849,-0.308))

# (2) OUR claimed pure-quartic point: same kappas with kappa_prod := 0, m2 refixed so S4 is critical at scale 1
k0 = list(k_mid); k0[3] = mp.mpf(0)
m2_0 = m2_for_s4_at_scale1(k0)
report("OUR CLAIM: same point with kappa_prod=0, m2 refixed for S4 criticality at scale 1", k0, m2_0, (1.849,-0.308))

# (3) sanity: scale-invariance -- the (2) point rescaled to m2 = m2_mid should give the same verdict
lam2 = m2_mid/m2_0
report("(2) rescaled to the original m2 (verdict must be identical by homogeneity)", k0, m2_mid, (1.849*mp.sqrt(lam2), -0.308*mp.sqrt(lam2)))

# (4) a small neighbourhood scan in kappa_prod=0 space along t, m2 refixed, exact 6-dim Hessians
print("\n=== scan along A->B with kappa_prod=0 identically, exact 6-dim Hessians")
print(f"    {'t':>6} {'S4 min eig':>11} {'S2 min eig':>11}  coexist")
s2g=(1.849,-0.308)
for tt in [mp.mpf(v)/1000 for v in range(100,161,5)]:
    kk=[(1-tt)*a_+tt*b_ for a_,b_ in zip(kA,kB)]; kk[3]=mp.mpf(0); mm=m2_for_s4_at_scale1(kk)
    r=refine_s4(mm,kk); e4,_=hess6(phi_of(r,r,r),mm,kk)
    try:
        a,b=refine_s2(mm,kk,*s2g); s2g=(float(a),float(b)); e2,_=hess6(phi_of(a,b,b),mm,kk); m2e=e2.min()
    except Exception as ex:
        m2e=float('nan')
    co = "  <== BOTH" if (e4.min()>0 and m2e>0) else ""
    print(f"    {float(tt):6.3f} {e4.min():11.4f} {m2e:11.4f}{co}")
