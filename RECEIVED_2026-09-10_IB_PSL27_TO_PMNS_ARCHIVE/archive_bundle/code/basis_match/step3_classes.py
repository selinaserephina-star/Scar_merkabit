import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

G = list(np.load("group_elems.npy"))
n = len(G)
print("G size:", n)

def key(M, decimals=6):
    return tuple(np.round(M, decimals).flatten().view(float))

idx = {key(M): i for i, M in enumerate(G)}

def order_of(M, maxord=20):
    I3 = np.eye(3, dtype=complex)
    P = M.copy()
    for k in range(1, maxord+1):
        if np.max(np.abs(P - I3)) < 1e-6:
            return k
        P = P @ M
    return None

orders = [order_of(M) for M in G]

# conjugacy classes: brute force g h g^-1 for all g in G (using inverses)
invs = [np.linalg.inv(M) for M in G]

visited = [False]*n
classes = []
for i in range(n):
    if visited[i]:
        continue
    cls = set()
    for g, ginv in zip(G, invs):
        conj = g @ G[i] @ ginv
        j = idx[key(conj)]
        cls.add(j)
    for j in cls:
        visited[j] = True
    classes.append(sorted(cls))

classes.sort(key=lambda c: (orders[c[0]], len(c)))
print("Number of conjugacy classes:", len(classes))
for c in classes:
    print(f"  order={orders[c[0]]:2d}  size={len(c):3d}")

# trace (chi_3) per class
print("\nchi_3 per class (representative trace):")
for c in classes:
    tr = np.trace(G[c[0]])
    print(f"  order={orders[c[0]]:2d} size={len(c):3d}  tr={tr:.6f}")

np.save("classes.npy", np.array(classes, dtype=object), allow_pickle=True)
np.save("orders.npy", np.array(orders))
