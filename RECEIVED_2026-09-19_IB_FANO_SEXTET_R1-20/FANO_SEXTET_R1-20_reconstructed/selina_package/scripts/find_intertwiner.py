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

order2 = [M for M in GL32 if mat_order3(M)==2]
order3 = [M for M in GL32 if mat_order3(M)==3]
found = None
for A in order2[:5]:
    for B in order3:
        AB = mat_mul3(A,B)
        if mat_order3(AB)==7:
            found = (A,B); break
    if found: break
A, B = found

pts7 = [v for v in itertools.product([0,1],repeat=3) if any(v)]
pidx7 = {v:i for i,v in enumerate(pts7)}
def mat_vec3(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
def perm7(M): return tuple(pidx7[mat_vec3(M,p)] for p in pts7)
def compose7(p,q): return tuple(p[q[i]] for i in range(7))

pA, pB = perm7(A), perm7(B)
def perm_to_matrix7(p):
    M = np.zeros((7,7))
    for i in range(7): M[p[i],i]=1
    return M
MA7, MB7 = perm_to_matrix7(pA), perm_to_matrix7(pB)

U = np.zeros((7,6))
for i in range(6):
    U[i+1,i] = 1; U[0,i] = -1
Uplus = np.linalg.pinv(U)
def restrict6(M7): return Uplus @ M7 @ U
M6_A_fano = restrict6(MA7)
M6_B_fano = restrict6(MB7)

# paper's explicit sextet matrices (eq 29, 35) using eta=exp(2pi i/7)
eta = np.exp(2j*np.pi/7)
c = [np.cos(2*n*np.pi/7) for n in [0,1,2,3]]  # c[1]=c1,c[2]=c2,c[3]=c3
c1,c2,c3 = c[1],c[2],c[3]

A6 = -(2*np.sqrt(2)/7) * np.array([
 [ (c3-1)/np.sqrt(2), (c2-1)/np.sqrt(2), (c1-1)/np.sqrt(2), c3-c1, c1-c2, c2-c3],
 [ (c2-1)/np.sqrt(2), (c1-1)/np.sqrt(2), (c3-1)/np.sqrt(2), c2-c3, c3-c1, c1-c2],
 [ (c1-1)/np.sqrt(2), (c3-1)/np.sqrt(2), (c2-1)/np.sqrt(2), c1-c2, c2-c3, c3-c1],
 [ c3-c1, c2-c3, c1-c2, (c1-1)/np.sqrt(2), (c2-1)/np.sqrt(2), (c3-1)/np.sqrt(2)],
 [ c1-c2, c3-c1, c2-c3, (c2-1)/np.sqrt(2), (c3-1)/np.sqrt(2), (c1-1)/np.sqrt(2)],
 [ c2-c3, c1-c2, c3-c1, (c3-1)/np.sqrt(2), (c1-1)/np.sqrt(2), (c2-1)/np.sqrt(2)],
])
print("Paper's A^[6] trace:", np.trace(A6).round(6), " (expect 2)")

# A^[6]B^[6] = diag(eta^2,eta^4,eta,eta^3,eta^5,eta^6)
ABdiag = np.diag([eta**2, eta**4, eta, eta**3, eta**5, eta**6])
B6 = np.linalg.solve(A6, ABdiag)  # since A6 is an involution (A6 @ A6 = I), A6^-1=A6, so B6 = A6 @ ABdiag
B6 = A6 @ ABdiag
print("Paper's B^[6] trace:", np.trace(B6).round(6), " (expect 0)")
print("Paper's (AB)^[6] trace:", np.trace(ABdiag).round(6), " (expect -1)")

# Now solve for intertwiner S: S @ M6_A_fano = A6 @ S  and S @ M6_B_fano = B6 @ S
# stack as a linear system: vec(S @ Mf - Mp @ S) = 0 for both generators
from scipy.linalg import null_space
def comm_constraint(Mf, Mp):
    n = 6
    I = np.eye(n)
    # S @ Mf - Mp @ S = 0  <=>  (Mf^T (x) I - I (x) Mp) vec(S) = 0
    return np.kron(Mf.T, np.eye(n)) - np.kron(np.eye(n), Mp)

C1 = comm_constraint(M6_A_fano, A6)
C2 = comm_constraint(M6_B_fano, B6)
C = np.vstack([C1, C2])
ns = null_space(C, rcond=1e-8)
print(f"\\nNullity of intertwiner constraint: {ns.shape[1]}  (expect 1 for an irreducible rep, by Schur)")
if ns.shape[1]>=1:
    S = ns[:,0].reshape(6,6)
    print("Found intertwiner S (up to scale). Checking S@Mf - Mp@S norms:")
    print("  A:", np.linalg.norm(S@M6_A_fano - A6@S))
    print("  B:", np.linalg.norm(S@M6_B_fano - B6@S))
    np.save('intertwiner_S.npy', S)
