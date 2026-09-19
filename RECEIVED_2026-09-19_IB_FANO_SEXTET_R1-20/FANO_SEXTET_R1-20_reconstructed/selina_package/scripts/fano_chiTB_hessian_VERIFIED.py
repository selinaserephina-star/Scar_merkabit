"""
fano_chiTB_hessian_VERIFIED.py

Follow-on to fano_kappa_relation_VERIFIED.py. Requires numpy only.
Extends the direct-verification approach to King-Luhn's OTHER major
vacuum alignment claim (arXiv:0912.1344, Section 4.2.1): that
chi_TB=(0,0,0,0,0,1) (breaking PSL(2,7) to S4, the neutrino/TB
direction) is a critical point for EACH of the five invariants
I1..I5 SEPARATELY (not just some combination, unlike the chi_top case
in fano_kappa_relation_VERIFIED.py) -- and that the Hessian of each
I_alpha/I0 at this point equals their explicitly stated 10x10 matrices
h1..h5 (their eqs. 4.12-4.16), on the 10 non-scaling real dimensions
(Re/Im of chi_1..chi_5; chi_6 itself is the scale direction they
explicitly exclude).

METHOD: build all seven invariants I0..I6 from the now fully-verified
Theta, Theta', Omega. Numerically differentiate I_alpha/I0 (alpha=1..5)
at chi_TB: first, the 12-component real gradient (should vanish for
each alpha individually); then the full 12x12 real Hessian, restricted
to the 10 dimensions excluding chi_6, compared directly against their
stated h1..h5.

RESULT: all five first-derivative checks vanish to floating-point
precision (~1e-9), and all five Hessians match their stated matrices
exactly (max abs diff ~1e-5, consistent with finite-difference
truncation error at step size 1e-4 -- not a real discrepancy).

This is a second, independent, from-scratch confirmation of King-
Luhn's central results (the first being fano_kappa_relation_VERIFIED.py
for chi_top) -- together these directly verify BOTH halves of their
vacuum-alignment story (the S4-preserving TB direction and the
S4-breaking top-Yukawa direction) using formulas re-derived from their
own cited source (arXiv:0905.1686) rather than assumed correct.
"""
import numpy as np

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
def Omega(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        np.sqrt(3)*c2_*c3_ + c1_*c4_ - 2*np.sqrt(6)*c1_*c5_ + 2*np.sqrt(14)*c1_*c6_,
        np.sqrt(21)*c2_*c3_ - 3*np.sqrt(7)*c1_*c4_,
        -np.sqrt(6)*c1_**2 + np.sqrt(6)*c2_**2 - 2*c4_*c5_ + 2*np.sqrt(14)*c5_*c6_,
        -np.sqrt(2)*c1_**2 - np.sqrt(2)*c2_**2 + 2*np.sqrt(2)*c3_**2 - 2*np.sqrt(2)*c4_**2 + 2*np.sqrt(2)*c5_**2 - 2*np.sqrt(7)*c4_*c6_,
        -np.sqrt(21)*c1_*c3_ + 3*np.sqrt(7)*c2_*c4_,
        np.sqrt(3)*c1_*c3_ + c2_*c4_ + 2*np.sqrt(6)*c2_*c5_ + 2*np.sqrt(14)*c2_*c6_,
        -2*np.sqrt(21)*c3_*c5_,
        2*np.sqrt(6)*c1_*c2_ - 4*np.sqrt(2)*c3_*c4_ + 2*np.sqrt(7)*c3_*c6_])

def all_I_with_omega(chi):
    Y = sum(c*c for c in chi)
    T = Theta(chi); Tp = Thetap(chi); Om = Omega(chi)
    I0 = (sum(c.conjugate()*c for c in chi)).real**2
    I1 = (Y.conjugate()*Y).real
    I2 = np.sum(T.conjugate()*T).real
    I3 = np.sum(Tp.conjugate()*Tp).real
    I4 = ((1/np.sqrt(2))*np.sum(Tp.conjugate()*T+T.conjugate()*Tp)).real
    I5 = ((1j/np.sqrt(2))*np.sum(Tp.conjugate()*T-T.conjugate()*Tp)).real
    I6 = np.sum(Om.conjugate()*Om).real
    return I0,I1,I2,I3,I4,I5,I6

chi_TB = np.array([0,0,0,0,0,1], dtype=complex)

def Ialpha_over_I0(chi, alpha):
    vals = all_I_with_omega(chi)
    return vals[alpha]/vals[0]

def perturb(chi, idx, amt):
    c = chi.copy()
    if idx < 6: c[idx] += amt
    else: c[idx-6] += 1j*amt
    return c

def numerical_grad12(func, chi, h=1e-6):
    grad = np.zeros(12)
    for i in range(12):
        grad[i] = (func(perturb(chi,i,h)) - func(perturb(chi,i,-h))) / (2*h)
    return grad

def numerical_hessian12(func, chi, h=1e-4):
    n = 12
    H = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            c_pp = perturb(perturb(chi,i,h),j,h)
            c_pm = perturb(perturb(chi,i,h),j,-h)
            c_mp = perturb(perturb(chi,i,-h),j,h)
            c_mm = perturb(perturb(chi,i,-h),j,-h)
            H[i,j] = (func(c_pp)-func(c_pm)-func(c_mp)+func(c_mm))/(4*h*h)
    return H

print("[1] First derivatives of I_alpha/I0 at chi_TB (should ALL vanish, alpha=1..5):")
for alpha in range(1,6):
    g = numerical_grad12(lambda c: Ialpha_over_I0(c,alpha), chi_TB)
    max_g = np.max(np.abs(g))
    print(f"    alpha={alpha}: max|grad| = {max_g:.2e}")
    assert max_g < 1e-7

print("\n[2] Hessians h1..h5 (arXiv:0912.1344 eqs 4.12-4.16) vs. direct computation:")
h1_theirs = -8*np.diag([0,0,0,0,0,1,1,1,1,1])
h2_theirs = 4*np.diag([14,14,35,35,14,20,20,27,27,20])
h3_theirs = -16*np.diag([14,14,14,14,14,9,9,9,9,9])
h4_theirs = -4*np.diag([14,14,7,7,14,-18,-18,45,45,-18])
h5tilde = 28*np.diag([2,2,-3,-3,2])
h5_theirs = np.block([[np.zeros((5,5)), h5tilde],[h5tilde, np.zeros((5,5))]])
# 10 real dims = (Re chi_1..5, Im chi_1..5); chi_6 (indices 5, 11) is the excluded scale direction
idx10 = [0,1,2,3,4,6,7,8,9,10]

for alpha, h_theirs in [(1,h1_theirs),(2,h2_theirs),(3,h3_theirs),(4,h4_theirs),(5,h5_theirs)]:
    H_full = numerical_hessian12(lambda c: Ialpha_over_I0(c,alpha), chi_TB, h=1e-4)
    H_10 = H_full[np.ix_(idx10,idx10)]
    diff = np.max(np.abs(H_10 - h_theirs))
    print(f"    h{alpha}: max abs diff = {diff:.6f}  (finite-difference noise level)")
    assert diff < 1e-3

print("\nDone. Both first- and second-derivative structure of King-Luhn's chi_TB")
print("vacuum alignment (their eqs 4.11-4.16) independently, directly confirmed.")
