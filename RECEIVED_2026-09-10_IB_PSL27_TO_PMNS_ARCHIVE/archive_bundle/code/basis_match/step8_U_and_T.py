import numpy as np
import pickle
np.set_printoptions(precision=6, suppress=True, linewidth=140)
rng = np.random.default_rng(42)

G = list(np.load("group_elems.npy"))
RHO8_all = np.load("RHO8.npy")
n = len(G)

with open("projectors.pkl","rb") as f:
    P = pickle.load(f)

def basis_from_projector(Pmat, rank):
    w, v = np.linalg.eigh(Pmat)  # Hermitian eigendecomp
    order = np.argsort(-w.real)
    w = w[order]; v = v[:, order]
    U_block = v[:, :rank]
    # re-orthonormalize just in case
    U_block, _ = np.linalg.qr(U_block)
    return U_block

u2  = basis_from_projector(P['2'], 2)
u3  = basis_from_projector(P['3'], 3)
u3p = basis_from_projector(P['3p'], 3)

U = np.concatenate([u2, u3, u3p], axis=1)  # 8x8
print("U shape:", U.shape)
print("U^dagger U - I err:", np.max(np.abs(U.conj().T@U - np.eye(8))))

np.save("u2.npy", u2); np.save("u3.npy", u3); np.save("u3p.npy", u3p); np.save("U.npy", U)

# --- verify block structure on a couple of H elements ---
H = list(np.load("H_elems.npy"))
Hg_index_in_G = np.load("Hg_index_in_G.npy")

def key(M, decimals=6):
    return tuple(np.round(M, decimals).flatten().view(float))
idxG = {key(M): i for i, M in enumerate(G)}

test_h = H[5]
gi = idxG[key(test_h)]
R8 = RHO8_all[gi]
R8_block = U.conj().T @ R8 @ U
offblock = R8_block.copy()
offblock[0:2,0:2]=0; offblock[2:5,2:5]=0; offblock[5:8,5:8]=0
print("max off-block element for a sample h in H:", np.max(np.abs(offblock)))

# ============ Step: Reynolds-averaged G-invariant tensor T ============
# rho3(g) for all g
RHO3_all = np.array(G)  # G already stores rho3(g) as 3x3 matrices

# Build a random starting T0: map V8 (x) V3 -> V8 ; shape (8_out, 8_in, 3_in)
T0 = rng.normal(size=(8,8,3)) + 1j*rng.normal(size=(8,8,3))

def kron_inv_unitary(A, B):
    # (A tens B)^{-1} for unitary A,B = A^dagger tens B^dagger
    return np.kron(A.conj().T, B.conj().T)

T0_mat = T0.reshape(8, 24)  # combine (in8,in3) -> 24

T_mat_accum = np.zeros((8,24), dtype=complex)
for g_idx in range(n):
    g8 = RHO8_all[g_idx]
    g3 = RHO3_all[g_idx]
    Kinv = kron_inv_unitary(g8, g3)   # (rho8(g) tens rho3(g))^{-1}, shape 24x24, index order (in8,in3)
    T_mat_accum += g8 @ T0_mat @ Kinv

T_mat = T_mat_accum / n
T = T_mat.reshape(8,8,3)

print("\n||T|| Frobenius:", np.linalg.norm(T))

# Verify G-equivariance of T explicitly on a random group element
gtest = 77
g8 = RHO8_all[gtest]; g3 = RHO3_all[gtest]
lhs = np.einsum('op,pab->oab', g8, T)
Kinv = kron_inv_unitary(g8,g3)
rhs_mat = T_mat @ Kinv
# apply g8 on output side too? Actually equivariance means: T(g8 v, g3 w) = g8 T(v,w)
# i.e. T_mat @ (g8 tens g3) = g8 @ T_mat  =>  T_mat = g8 @ T_mat @ (g8 tens g3)^{-1}
check = g8 @ T_mat @ Kinv
print("Equivariance residual (should be ~0):", np.max(np.abs(check - T_mat)))

np.save("T_tensor.npy", T)
print("\nSaved T tensor, shape", T.shape)
