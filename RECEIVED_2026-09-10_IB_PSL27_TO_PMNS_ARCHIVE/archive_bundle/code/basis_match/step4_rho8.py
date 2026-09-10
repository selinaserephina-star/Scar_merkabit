import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

G = list(np.load("group_elems.npy"))
orders = np.load("orders.npy")
classes = np.load("classes.npy", allow_pickle=True)
n = len(G)

# Orthonormal basis (HS inner product tr(X Y^dagger)) of traceless 3x3 matrices
# Cartan part
H1 = np.diag([1,-1,0]).astype(complex)/np.sqrt(2)
H2 = np.diag([1,1,-2]).astype(complex)/np.sqrt(6)

def E(j,k):
    M = np.zeros((3,3), dtype=complex)
    M[j,k] = 1.0
    return M

offdiag_pairs = [(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)]
basis = [H1, H2] + [E(j,k) for (j,k) in offdiag_pairs]
assert len(basis) == 8

# verify orthonormality under HS inner product <X,Y> = tr(X Y^dagger)
Gram = np.array([[np.trace(X @ Y.conj().T) for Y in basis] for X in basis])
print("Gram matrix deviation from I8:", np.max(np.abs(Gram-np.eye(8))))

def rho8_matrix(g):
    # action: X -> g X g^dagger  (g assumed unitary here, so g^dagger = g^{-1})
    out = np.zeros((8,8), dtype=complex)
    for jcol, Xb in enumerate(basis):
        Y = g @ Xb @ g.conj().T
        # coordinates in orthonormal basis: c_i = <basis_i, Y> = tr(basis_i^dagger Y)... careful w/ convention
        coords = np.array([np.trace(Ei.conj().T @ Y) for Ei in basis])
        out[:, jcol] = coords
    return out

# sanity check on identity
I3 = np.eye(3, dtype=complex)
R8_I = rho8_matrix(I3)
print("rho8(I) deviation from I8:", np.max(np.abs(R8_I - np.eye(8))))

# check homomorphism property on two random group elements
import random
random.seed(0)
g1 = G[10]; g2 = G[37]
R1 = rho8_matrix(g1); R2 = rho8_matrix(g2)
R12 = rho8_matrix(g1@g2)
print("homomorphism check err:", np.max(np.abs(R1@R2 - R12)))

# character (trace) of rho8 per conjugacy class
print("\nchi_8 per class:")
chi8_vals = {}
for c in classes:
    rep = G[c[0]]
    tr = np.trace(rho8_matrix(rep))
    chi8_vals[c[0]] = tr
    print(f"  order={orders[c[0]]:2d} size={len(c):3d}  tr={tr:.6f}")

# save rho8 for all group elements (needed later for Reynolds averaging)
RHO8 = np.array([rho8_matrix(g) for g in G])
np.save("RHO8.npy", RHO8)
np.save("basis8.npy", np.array(basis))
print("\nSaved RHO8 for all 168 elements, shape:", RHO8.shape)
