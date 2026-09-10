import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

G = list(np.load("group_elems.npy"))
orders = np.load("orders.npy")
n = len(G)

def key(M, decimals=6):
    return tuple(np.round(M, decimals).flatten().view(float))

idx = {key(M): i for i, M in enumerate(G)}

def generate_subgroup(gens, max_size=200):
    I3 = np.eye(3, dtype=complex)
    elems = {key(I3): I3}
    frontier = [I3]
    while frontier:
        new_frontier = []
        for M in frontier:
            for g in gens:
                N = g @ M
                k = key(N)
                if k not in elems:
                    elems[k] = N
                    new_frontier.append(N)
        frontier = new_frontier
        if len(elems) > max_size:
            return None
    return list(elems.values())

order4_idxs = [i for i in range(n) if orders[i]==4]
order3_idxs = [i for i in range(n) if orders[i]==3]
order2_idxs = [i for i in range(n) if orders[i]==2]

print(f"#order4={len(order4_idxs)}  #order3={len(order3_idxs)}  #order2={len(order2_idxs)}")

found = None
g4 = G[order4_idxs[0]]
for i3 in order3_idxs:
    g3 = G[i3]
    sub = generate_subgroup([g4, g3], max_size=30)
    if sub is not None and len(sub) == 24:
        found = sub
        print("Found order-24 subgroup with g4=order4[0], g3 index", i3)
        break

if found is None:
    print("trying more order4 seeds...")
    for i4 in order4_idxs:
        g4 = G[i4]
        for i3 in order3_idxs:
            g3 = G[i3]
            sub = generate_subgroup([g4, g3], max_size=30)
            if sub is not None and len(sub) == 24:
                found = sub
                print("Found with g4 idx", i4, "g3 idx", i3)
                break
        if found is not None:
            break

H = found
print("H size:", len(H))

# order profile within H
def order_of(M, maxord=20):
    I3 = np.eye(3, dtype=complex)
    P = M.copy()
    for k in range(1, maxord+1):
        if np.max(np.abs(P - I3)) < 1e-6:
            return k
        P = P @ M
    return None

Horders = [order_of(M) for M in H]
from collections import Counter
print("Order profile within H:", Counter(Horders))

np.save("H_elems.npy", np.array(H))
