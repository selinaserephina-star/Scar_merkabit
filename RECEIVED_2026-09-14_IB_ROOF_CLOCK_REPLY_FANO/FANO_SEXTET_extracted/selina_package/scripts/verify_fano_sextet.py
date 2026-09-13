import itertools
import numpy as np

exec(open('build_gl32_and_check.py').read().split('print(f"Built')[0])

def mat_order3(M, limit=20):
    X=M; n=1
    I3 = ((1,0,0),(0,1,0),(0,0,1))
    while X!=I3:
        X = mat_mul3(X,M); n+=1
        if n>limit: return -1
    return n

# find A (order 2), B (order 3) with AB order 7, matching presentation <A,B|A^2=B^3=(AB)^7=[A,B]^4=1>
order2 = [M for M in GL32 if mat_order3(M)==2]
order3 = [M for M in GL32 if mat_order3(M)==3]

found = None
for A in order2[:5]:
    for B in order3:
        AB = mat_mul3(A,B)
        if mat_order3(AB)==7:
            found = (A,B)
            break
    if found: break
A, B = found
print("Found A (order 2), B (order 3) with AB order 7.")

# Build the 7-point Fano action (natural action on V's 7 nonzero points)
pts7 = [v for v in itertools.product([0,1],repeat=3) if any(v)]
pidx7 = {v:i for i,v in enumerate(pts7)}
def mat_vec3(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
def perm7(M): return tuple(pidx7[mat_vec3(M,p)] for p in pts7)

pA, pB = perm7(A), perm7(B)
def compose7(p,q): return tuple(p[q[i]] for i in range(7))
pAB = compose7(pA,pB)

# order-7 element check
def perm_order(p, n, limit=20):
    e=tuple(range(n)); x=p; k=1
    while x!=e:
        x=tuple(p[x[i]] for i in range(n)); k+=1
        if k>limit: return -1
    return k
print("orders: A=",perm_order(pA,7)," B=",perm_order(pB,7)," AB=",perm_order(pAB,7))

# Build the 6-dim "deleted permutation" rep: restrict to the sum-zero subspace of the 7-dim perm module
# basis: e_i - e_0 for i=1..6 (standard deleted-permutation basis)
def perm_to_matrix7(p):
    M = np.zeros((7,7))
    for i in range(7): M[p[i],i]=1
    return M

MA7, MB7 = perm_to_matrix7(pA), perm_to_matrix7(pB)
MAB7 = MA7 @ MB7

# change of basis: first 6 basis vectors of the "deleted" rep = e_i - e_0 (i=1..6), quotient by all-ones
U = np.zeros((7,6))
for i in range(6):
    U[i+1,i] = 1
    U[0,i] = -1
# project each M7 onto this basis via M7 @ U, expressed back in U-basis coordinates (pseudo-inverse since not orthogonal)
Uplus = np.linalg.pinv(U)
def restrict6(M7):
    return Uplus @ M7 @ U

M6_A = restrict6(MA7)
M6_B = restrict6(MB7)
M6_AB = restrict6(MAB7)

print()
print("Trace(A) in 6-dim rep:", np.trace(M6_A).round(6), " (expect chi6(order2)=2)")
print("Trace(B) in 6-dim rep:", np.trace(M6_B).round(6), " (expect chi6(order3)=0)")
print("Trace(AB) in 6-dim rep:", np.trace(M6_AB).round(6), " (expect chi6(order7)=-1)")
