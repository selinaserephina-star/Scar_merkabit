"""
Build PSL(2,7) = GL(3,2) explicitly (168 invertible 3x3 matrices over F2),
construct its natural action on V (+) V* = F2^6 (the standard symplectic
embedding into Sp(6,2)), and check whether this F2-representation is
IRREDUCIBLE as a PSL(2,7)-module -- the key question for comparing it to
the complex sextet chi_6 used by King-Luhn.
"""
import itertools

# ---------------- Build GL(3,2): all invertible 3x3 matrices over F2 ----------------
def mat_mul3(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))

def mat_det3_invertible(M):
    # invertible iff rows are linearly independent over F2
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
print(f"Found {len(GL32)} invertible 3x3 matrices over F2 (expect 168 = |GL(3,2)|)")

def mat_inv3(M):
    A = [list(row)+[1 if i==j else 0 for j in range(3)] for i,row in enumerate(M)]
    for col in range(3):
        piv=None
        for r in range(col,3):
            if A[r][col]==1: piv=r; break
        A[col],A[piv]=A[piv],A[col]
        for r in range(3):
            if r!=col and A[r][col]==1:
                A[r]=[(A[r][k]+A[col][k])%2 for k in range(6)]
    return tuple(tuple(row[3:]) for row in A)

def mat_transpose3(M):
    return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))

# ---------------- Build the 6-dim representation on V (+) V* ----------------
# g acts on V as g, on V* as (g^-1)^T (the dual/contragredient action, standard)
def rep6(M):
    Minv_T = mat_transpose3(mat_inv3(M))
    # 6x6 block-diagonal matrix
    top = [list(M[i])+[0,0,0] for i in range(3)]
    bot = [[0,0,0]+list(Minv_T[i]) for i in range(3)]
    return tuple(tuple(r) for r in (top+bot))

def mat_mul6(A,B,n=6):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%2 for j in range(n)) for i in range(n))

gens_M = GL32[:20]  # sample some elements as generators to double-check closure works; we'll use full group anyway
rep6_full = [rep6(M) for M in GL32]
print(f"Built {len(rep6_full)} 6x6 matrices (representation of full GL(3,2) on V+V*)")

# sanity: verify these 6x6 matrices form a valid representation (multiplication matches)
import random
random.seed(0)
for _ in range(20):
    i,j = random.randrange(168), random.randrange(168)
    A, B = GL32[i], GL32[j]
    AB = mat_mul3(A,B)
    lhs = rep6(AB)
    rhs = mat_mul6(rep6(A), rep6(B))
    assert lhs==rhs, "representation homomorphism check FAILED"
print("Representation homomorphism verified on 20 random pairs: rep6(AB)==rep6(A)rep6(B)")
