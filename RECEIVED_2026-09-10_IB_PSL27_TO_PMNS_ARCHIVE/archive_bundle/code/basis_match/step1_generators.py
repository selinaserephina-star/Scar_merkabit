import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

zeta = np.exp(2j*np.pi/7)
sqrtm7 = 1j*np.sqrt(7.0)   # sqrt(-7)

# S: order-7 diagonal generator (Elkies / Klein)
S = np.diag([zeta**4, zeta**2, zeta]).astype(complex)

# T: order-3 cyclic permutation
T = np.array([[0,0,1],
              [1,0,0],
              [0,1,0]], dtype=complex)

# R: order-2 "Klein involution"
a1 = zeta   - zeta**6
a2 = zeta**2 - zeta**5
a3 = zeta**4 - zeta**3
R = (-1.0/sqrtm7) * np.array([
    [a1, a2, a3],
    [a2, a3, a1],
    [a3, a1, a2]
], dtype=complex)

def close_to_I(M, tol=1e-9):
    return np.max(np.abs(M-np.eye(3))) < tol

I3 = np.eye(3, dtype=complex)

print("S^7 = I:", close_to_I(np.linalg.matrix_power(S,7)))
print("T^3 = I:", close_to_I(np.linalg.matrix_power(T,3)))
print("R^2 = I:", close_to_I(R@R))

def unitary_err(M):
    return np.max(np.abs(M.conj().T@M - I3))

print("S unitary err:", unitary_err(S))
print("T unitary err:", unitary_err(T))
print("R unitary err:", unitary_err(R))

print("det S:", np.linalg.det(S))
print("det T:", np.linalg.det(T))
print("det R:", np.linalg.det(R))

np.save("S.npy", S)
np.save("T.npy", T)
np.save("R.npy", R)
print("\nS=\n", S)
print("\nR=\n", R)
