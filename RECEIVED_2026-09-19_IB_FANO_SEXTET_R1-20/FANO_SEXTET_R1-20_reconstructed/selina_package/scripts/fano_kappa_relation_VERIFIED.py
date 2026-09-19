"""
fano_kappa_relation_VERIFIED.py

Follow-on to fano_correct_STUV_basis_found.py. Requires numpy only.
The final step: with Theta, Theta', Omega now verified correct (all
168 elements, machine precision), this directly checks King-Luhn's
central vacuum-alignment claim (arXiv:0912.1344, Section 4.2.2, their
eq. 4.24-4.26): that chi_top (their eq. 2.10) is a critical point of
their potential f, once the two relations kappa_2=kappa_3=
kappa_4+kappa_5/sqrt(7) are imposed (equivalently, once f is written
in terms of their three combinations I=I1, I'=I2+I3+I4,
I''=I4-sqrt(7)*I5, as they do).

METHOD: build f directly from I0..I5 (all now confirmed-correct),
evaluate its gradient (12 real partial derivatives, real+imaginary
parts of each chi_i) numerically at their stated chi_top, for several
different (kappa,kappa',kappa'') choices spanning positive, negative,
and mixed-sign values.

RESULT: the gradient vanishes at chi_top (max |grad| ~1e-9, floating-
point-noise level) for EVERY (kappa,kappa',kappa'') tested -- exactly
as King-Luhn claim: once their two relations are imposed via this
I,I',I'' parametrization, chi_top is a critical point for ANY values
of the three remaining free couplings. This is a direct, independent,
from-scratch confirmation of their central vacuum-alignment result,
using formulas re-derived and cross-checked against their own basis
(arXiv:0905.1686) rather than assumed.

As a smaller consistency check en route: I2 and I3 evaluate to EXACTLY
equal values (5040) at chi_top, and I1=0 exactly -- both consistent
with, though not equivalent to, the stated relations.

STATUS: this confirms King-Luhn's OWN claim about their OWN potential
using their OWN formulas -- a from-scratch, independent verification,
not a restatement. It does not (yet) translate this into this
correspondence's Fano-built kappa-basis -- the six Fano invariants and
King-Luhn's I1..I6 match perfectly on REAL fields (see the previous
script), but the complex/antisymmetric piece (I5 vs this
correspondence's antisymmetric invariant) does not yet have a clean
closed-form translation; direct verification against King-Luhn's own
formulas, as done here, sidesteps that gap entirely for this specific
check.
"""
import numpy as np

# ---------------- King-Luhn's Theta, Theta' (arXiv:0912.1344, eqs 4.2-4.3) ----------------
def Theta(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        -2*np.sqrt(21)*c1_*c5_-6*c1_*c6_, 2*np.sqrt(21)*c2_*c5_-6*c2_*c6_,
        2*np.sqrt(14)*c3_*c4_+8*c3_*c6_, np.sqrt(14)*c3_**2-np.sqrt(14)*c4_**2+8*c4_*c6_,
        -np.sqrt(21)*c1_**2+np.sqrt(21)*c2_**2-6*c5_*c6_,
        -3*c1_**2-3*c2_**2+4*c3_**2+4*c4_**2-3*c5_**2+c6_**2])
def Thetap(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        2*np.sqrt(21)*c2_*c3_+2*np.sqrt(7)*c1_*c4_-2*np.sqrt(2)*c1_*c6_,
        2*np.sqrt(21)*c1_*c3_+2*np.sqrt(7)*c2_*c4_-2*np.sqrt(2)*c2_*c6_,
        2*np.sqrt(21)*c1_*c2_+2*np.sqrt(7)*c3_*c4_-2*np.sqrt(2)*c3_*c6_,
        np.sqrt(7)*c1_**2+np.sqrt(7)*c2_**2+np.sqrt(7)*c3_**2-np.sqrt(7)*c4_**2-2*np.sqrt(7)*c5_**2-2*np.sqrt(2)*c4_*c6_,
        -4*np.sqrt(7)*c4_*c5_-2*np.sqrt(2)*c5_*c6_,
        -np.sqrt(2)*c1_**2-np.sqrt(2)*c2_**2-np.sqrt(2)*c3_**2-np.sqrt(2)*c4_**2-np.sqrt(2)*c5_**2+5*np.sqrt(2)*c6_**2])

# ---------------- verify covariance under King-Luhn's own S,T,U,V one more time (self-contained check) ----------------
sqrt2,sqrt3,sqrt6,sqrt14,sqrt21 = np.sqrt(2),np.sqrt(3),np.sqrt(6),np.sqrt(14),np.sqrt(21)
S_gen = np.diag([-1,-1,1,1,1,1]).astype(float)
T_gen = 0.5*np.array([
    [1,1,0,0,sqrt2,0],[-1,-1,0,0,sqrt2,0],[0,0,-1,-sqrt3,0,0],
    [0,0,sqrt3,-1,0,0],[sqrt2,-sqrt2,0,0,0,0],[0,0,0,0,0,2]])
U_gen = np.diag([1,-1,-1,1,1,1]).astype(float)
V_gen = (1/6)*np.array([
    [6,0,0,0,0,0],[0,0,6,0,0,0],[0,6,0,0,0,0],
    [0,0,0,4,sqrt6,-sqrt14],[0,0,0,sqrt6,3,sqrt21],[0,0,0,-sqrt14,sqrt21,-1]])
np.random.seed(1)
chi_r = np.random.randn(6)
for name,g in [('S',S_gen),('T',T_gen),('U',U_gen),('V',V_gen)]:
    assert np.max(np.abs(Theta(g@chi_r)-g@Theta(chi_r))) < 1e-8
    assert np.max(np.abs(Thetap(g@chi_r)-g@Thetap(chi_r))) < 1e-8
print("[1] Theta, Theta' covariance under S,T,U,V re-confirmed.")

# ---------------- the six invariants, all now confirmed-correct ----------------
def all_I(chi):
    Y = sum(c*c for c in chi)
    T = Theta(chi); Tp = Thetap(chi)
    I0 = (sum(c.conjugate()*c for c in chi)).real**2
    I1 = (Y.conjugate()*Y).real
    I2 = np.sum(T.conjugate()*T).real
    I3 = np.sum(Tp.conjugate()*Tp).real
    I4 = ((1/np.sqrt(2))*np.sum(Tp.conjugate()*T+T.conjugate()*Tp)).real
    I5 = ((1j/np.sqrt(2))*np.sum(Tp.conjugate()*T-T.conjugate()*Tp)).real
    return I0,I1,I2,I3,I4,I5

# ---------------- their stated chi_top (arXiv:0912.1344 eq. 2.10) ----------------
b7 = (-1+1j*np.sqrt(7))/2
chi_top = (1-1j)*np.array([1, 1j*np.sqrt(3), -1j*np.sqrt(3)/b7, -np.sqrt(3)/b7, -np.sqrt(2), 0])

I0,I1,I2,I3,I4,I5 = all_I(chi_top)
print(f"\n[2] Invariants at chi_top: I0={I0:.4f} I1={I1:.4f} I2={I2:.4f} I3={I3:.4f} I4={I4:.4f} I5={I5:.4f}")
assert abs(I1) < 1e-8, "I1 should vanish exactly at chi_top"
assert abs(I2-I3) < 1e-8, "I2 should equal I3 exactly at chi_top"
print("    Consistency checks passed: I1=0 exactly, I2=I3 exactly.")

# ---------------- f in King-Luhn's I, I', I'' parametrization (their eq. 4.24) ----------------
def f_full(chi, kappa, kappap, kappapp):
    I0,I1,I2,I3,I4,I5 = all_I(chi)
    Iv = I1
    Iprime = I2+I3+I4
    Idprime = I4 - np.sqrt(7)*I5
    return (I0 + kappa*Iv + kappap*Iprime + kappapp*Idprime)/I0

def numerical_grad(func, chi, h=1e-6):
    grad = np.zeros(12)
    for i in range(6):
        cp=chi.copy(); cp[i]+=h; cm=chi.copy(); cm[i]-=h
        grad[i] = (func(cp)-func(cm))/(2*h)
        cp2=chi.copy(); cp2[i]+=1j*h; cm2=chi.copy(); cm2[i]-=1j*h
        grad[i+6] = (func(cp2)-func(cm2))/(2*h)
    return grad

# ---------------- THE KEY TEST: gradient of f at chi_top, for several (kappa,kappa',kappa'') ----------------
print("\n[3] THE KEY TEST -- gradient of f at chi_top, various (kappa,kappa',kappa''):")
test_points = [(0,0,-0.01), (0.01,0.02,-0.015), (1,1,1), (0.5,-0.3,0.2), (-2,3,-1.5)]
for (k,kp,kpp) in test_points:
    f_func = lambda chi: f_full(chi,k,kp,kpp)
    grad = numerical_grad(f_func, chi_top)
    max_grad = np.max(np.abs(grad))
    print(f"    kappa={k:+.3f}, kappa'={kp:+.3f}, kappa''={kpp:+.3f}: "
          f"max|grad|={max_grad:.2e}, f={f_func(chi_top):.4f}")
    assert max_grad < 1e-6, f"Gradient did not vanish for {(k,kp,kpp)}"

print("\nDone. King-Luhn's central vacuum-alignment claim (their eqs 4.24-4.26) is")
print("independently, directly confirmed: chi_top is a critical point of f for")
print("ANY (kappa,kappa',kappa''), exactly as they state.")
