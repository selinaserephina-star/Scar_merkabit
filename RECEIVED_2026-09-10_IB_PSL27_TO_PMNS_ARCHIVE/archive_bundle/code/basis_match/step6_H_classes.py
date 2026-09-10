import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

H = list(np.load("H_elems.npy"))
RHO8_all = np.load("RHO8.npy")
G = list(np.load("group_elems.npy"))
m = len(H)

def key(M, decimals=6):
    return tuple(np.round(M, decimals).flatten().view(float))

idxG = {key(M): i for i, M in enumerate(G)}
idxH = {key(M): i for i, M in enumerate(H)}

def order_of(M, maxord=20):
    I3 = np.eye(3, dtype=complex)
    P = M.copy()
    for k in range(1, maxord+1):
        if np.max(np.abs(P - I3)) < 1e-6:
            return k
        P = P @ M
    return None

Horders = [order_of(M) for M in H]
invsH = [np.linalg.inv(M) for M in H]

visited = [False]*m
Hclasses = []
for i in range(m):
    if visited[i]:
        continue
    cls = set()
    for h, hinv in zip(H, invsH):
        conj = h @ H[i] @ hinv
        j = idxH[key(conj)]
        cls.add(j)
    for j in cls:
        visited[j] = True
    Hclasses.append(sorted(cls))

Hclasses.sort(key=lambda c: (Horders[c[0]], len(c)))
print("Number of H-conjugacy classes:", len(Hclasses))
for c in Hclasses:
    print(f"  order={Horders[c[0]]}  size={len(c)}")

# map each H element to its index in G to fetch rho8
Hg_index_in_G = [idxG[key(M)] for M in H]

# chi8 and chi3 per H-class
print("\nchi8|H and chi3|H per class:")
for c in Hclasses:
    rep = H[c[0]]
    gi = Hg_index_in_G[c[0]]
    tr8 = np.trace(RHO8_all[gi])
    tr3 = np.trace(rep)
    print(f"  order={Horders[c[0]]} size={len(c)}   chi8={tr8:.6f}   chi3={tr3:.6f}")

np.save("Hclasses.npy", np.array(Hclasses, dtype=object), allow_pickle=True)
np.save("Horders.npy", np.array(Horders))
np.save("Hg_index_in_G.npy", np.array(Hg_index_in_G))
