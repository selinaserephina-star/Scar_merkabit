import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

H = list(np.load("H_elems.npy"))
Hclasses = np.load("Hclasses.npy", allow_pickle=True)
Horders = np.load("Horders.npy")
Hg_index_in_G = np.load("Hg_index_in_G.npy")
RHO8_all = np.load("RHO8.npy")

m = len(H)
nclasses = len(Hclasses)
print("H classes (order,size):", [(Horders[c[0]], len(c)) for c in Hclasses])

# class order in Hclasses (from previous run) is: [1(sz1), 2(sz3), 2(sz6), 3(sz8), 4(sz6)]
# i.e. e, (ab)(cd), (ab), (abc), (abcd)
class_sizes = [len(c) for c in Hclasses]
assert class_sizes == [1,3,6,8,6], class_sizes

# S4 character table in this exact class order: [e, (ab)(cd), (ab), (abc), (abcd)]
chartab = {
    '1' : [1,1,1,1,1],
    '1p': [1,1,-1,1,-1],
    '2' : [2,2,0,-1,0],
    '3' : [3,-1,1,0,-1],
    '3p': [3,-1,-1,0,1],
}
dims = {'1':1,'1p':1,'2':2,'3':3,'3p':3}

def elem_to_g(h_idx_in_H):
    return Hg_index_in_G[h_idx_in_H]

def isotypic_projector(irrep_name):
    dim = dims[irrep_name]
    chi = chartab[irrep_name]
    P = np.zeros((8,8), dtype=complex)
    for ci, cls in enumerate(Hclasses):
        chiv = chi[ci]
        for h_idx in cls:
            g_idx = elem_to_g(h_idx)
            P += np.conj(chiv) * RHO8_all[g_idx]
    P *= dim/24.0
    return P

results = {}
for name in ['1','1p','2','3','3p']:
    P = isotypic_projector(name)
    herm_err = np.max(np.abs(P - P.conj().T))
    idem_err = np.max(np.abs(P@P - P))
    rank = round(np.real(np.trace(P)))
    print(f"irrep {name}: dim={dims[name]}  herm_err={herm_err:.2e}  idem_err={idem_err:.2e}  trace(P)={np.trace(P):.4f} -> rank~{rank}")
    results[name] = P

np.save("projectors.npz".replace('.npz','_dummy'), 0) # placeholder no-op
import pickle
with open("projectors.pkl","wb") as f:
    pickle.dump(results, f)
