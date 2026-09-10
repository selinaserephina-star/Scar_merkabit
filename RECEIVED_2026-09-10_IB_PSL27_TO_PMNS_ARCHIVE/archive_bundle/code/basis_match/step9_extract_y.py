import numpy as np
np.set_printoptions(precision=8, suppress=True, linewidth=140)

u2  = np.load("u2.npy")
u3  = np.load("u3.npy")
u3p = np.load("u3p.npy")
U   = np.load("U.npy")
T   = np.load("T_tensor.npy")   # shape (out8, in8, in3)

# restrict input V8 leg to the 3' isotypic subspace: in8 = u3p @ a  (a in C^3)
# M[out, a, b] = sum_{in8} T[out, in8, b] * u3p[in8, a]
M = np.einsum('oib,ia->oab', T, u3p)   # shape (8,3,3):  out(8), a=3'-copy-in-V8 (3), b = V3=3' (3)

beta2  = np.einsum('oc,oab->cab', u2.conj(),  M)   # shape (2,3,3)
beta3  = np.einsum('oc,oab->cab', u3.conj(),  M)   # shape (3,3,3)
beta3p = np.einsum('oc,oab->cab', u3p.conj(), M)   # shape (3,3,3)

# residual: should be exactly captured, no leftover (no '1' block exists at all)
recon = (np.einsum('oc,cab->oab', u2,  beta2) +
         np.einsum('oc,cab->oab', u3,  beta3) +
         np.einsum('oc,cab->oab', u3p, beta3p))
print("reconstruction residual:", np.max(np.abs(recon - M)))

y2  = np.linalg.norm(beta2)
y3  = np.linalg.norm(beta3)
y3p = np.linalg.norm(beta3p)
y1  = 0.0  # no singlet subspace exists in V8|H at all (rank-0 projector, verified earlier)

print(f"\ny1  = {y1}")
print(f"y2  = {y2:.8f}")
print(f"y3  = {y3:.8f}")
print(f"y3' = {y3p:.8f}")
print(f"\ny3 / y2  = {y3/y2:.8f}")
print(f"y3'/ y2  = {y3p/y2:.8f}")
print(f"y3'/ y3  = {y3p/y3:.8f}")

# also norm of whole M, and check ||M||^2 = y2^2+y3^2+y3p^2 (Parseval, since U unitary)
print("\n||M||^2 =", np.linalg.norm(M)**2, "  y2^2+y3^2+y3p^2 =", y2**2+y3**2+y3p**2)

# Try to recognize ratios as algebraic numbers (simple rationals / sqrt's)
from fractions import Fraction
def guess(x, maxden=64):
    return Fraction(x).limit_denominator(maxden)

r32 = (y3/y2)**2
r3p2 = (y3p/y2)**2
print("\n(y3/y2)^2  ~", r32, " as fraction ~", guess(r32))
print("(y3'/y2)^2 ~", r3p2, " as fraction ~", guess(r3p2))
print("(y3/y2)^2 / (y3'/y2)^2 =", r32/r3p2, " as fraction ~", guess(r32/r3p2))
