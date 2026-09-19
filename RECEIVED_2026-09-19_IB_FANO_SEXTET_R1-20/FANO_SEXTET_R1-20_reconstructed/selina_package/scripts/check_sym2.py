"""
Build Sym^2(V) for V = F2^3 under the natural GL(3,2) action, as the
6-dimensional space spanned by symmetric tensors e_i(x)e_j + e_j(x)e_i
(i<j) and e_i(x)e_i (all i, char 2 makes these ALSO part of a
well-defined 6-dim symmetric-tensor space). Check irreducibility.
"""
import itertools

def mat_mul3(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
def mat_det3_invertible(M):
    rows = [list(r) for r in M]
    rank = 0
    for col in range(3):
        piv = None
        for r in range(rank,3):
            if rows[r][col]==1: piv=r; break
        if piv is None: continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for r in range(3):
            if r!=rank and rows[r][col]==1:
                rows[r] = [(rows[r][k]+rows[rank][k])%2 for k in range(3)]
        rank += 1
    return rank==3

all_mats = list(itertools.product([0,1], repeat=9))
GL32 = []
for m in all_mats:
    M = (m[0:3], m[3:6], m[6:9])
    if mat_det3_invertible(M):
        GL32.append(M)
print(f"GL(3,2): {len(GL32)} elements")

# basis of Sym^2(V): index pairs (i,j) with i<=j, 6 total: (0,0),(1,1),(2,2),(0,1),(0,2),(1,2)
basis_pairs = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
pair_index = {p:i for i,p in enumerate(basis_pairs)}

def sym2_image(M):
    # for basis vector e_i (x) e_j + e_j (x) e_i (symmetrized), compute image under g=M:
    # g(e_i) = sum_k M[k][i] e_k  (M acts on V by matrix-vector mult, columns = images of basis vectors)
    # image of (e_i sym e_j) = sum over k,l of M[k][i]*M[l][j] * (e_k sym e_l), symmetrized properly
    cols = [[M[r][c] for r in range(3)] for c in range(3)]  # cols[c][r] = M[r][c], i.e. image of e_c
    result = [[0]*6 for _ in range(6)]  # result[input_pair_idx][output_pair_idx] coefficient
    for idx,(i,j) in enumerate(basis_pairs):
        # g(e_i) = sum_k cols[i][k] e_k ; g(e_j) = sum_l cols[j][l] e_l
        gi = cols[i]; gj = cols[j]
        acc = {}
        for k in range(3):
            for l in range(3):
                c = gi[k]*gj[l]
                if c==0: continue
                p = (min(k,l), max(k,l))
                acc[p] = (acc.get(p,0) + 1) % 2
        for p,c in acc.items():
            if c:
                result[idx][pair_index[p]] ^= 1
    return tuple(tuple(row) for row in result)

# this result matrix as built has result[input][output]; we want output = M_rep . input as column vector,
# so the representation matrix REP satisfies REP[output][input] = result[input][output]
def to_rep_matrix(img_table):
    n=6
    REP = [[0]*n for _ in range(n)]
    for inp in range(n):
        for out in range(n):
            REP[out][inp] = img_table[inp][out]
    return tuple(tuple(r) for r in REP)

sym2_reps = [to_rep_matrix(sym2_image(M)) for M in GL32]

def mat_mul6(A,B,n=6):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%2 for j in range(n)) for i in range(n))

import random
random.seed(0)
for _ in range(20):
    i,j = random.randrange(168), random.randrange(168)
    AB = mat_mul3(GL32[i], GL32[j])
    lhs = to_rep_matrix(sym2_image(AB))
    rhs = mat_mul6(sym2_reps[i], sym2_reps[j])
    assert lhs==rhs, f"homomorphism check FAILED at {i},{j}"
print("Sym^2(V) representation homomorphism verified on 20 random pairs")

import pickle
with open('sym2_reps.pkl','wb') as f:
    pickle.dump(sym2_reps, f)
print("Saved sym2_reps.pkl")
