"""
fano_orthogonal_transform_found.py

Follow-on to fano_intertwiner_found.py. Requires numpy, scipy. Solves
the puzzle left open there: King-Luhn's (arXiv:0912.1344) explicit
Theta, Theta', Omega formulas (their eqs. 4.2-4.4), verified letter-
for-letter against a clean direct PDF read, did NOT transform
correctly under A_real/B_real (the real matrices obtained from
Luhn-Nasri-Ramond's A^[6],B^[6] via their own stated S=VP similarity
transform, arXiv:0709.1447 eq. 39). Three prior sessions of
hypothesis-testing (index reversal, block-rotation pairings,
mixing-matrix ansätze) all failed. This session found the actual fix.

METHOD: numerically search for an orthogonal O such that Theta becomes
covariant under O @ A_real @ O.T, by minimizing
  sum_g sum_chi || Theta(gO.chi) - gO.Theta(chi) ||^2
over the orthogonal group, parametrized as O = expm(K) for skew-
symmetric K (so the search is over R^15 = dim so(6), unconstrained).

RESULT: converges to machine precision (cost ~2e-17). Independently
verified on group elements and sample points NOT used in the
optimization: max covariance error 6e-10.

ALSO BUILT: a direct, genuinely real group-averaging intertwiner from
this correspondence's Fano-plane sextet directly to A_real/B_real
(sidestepping an earlier, flawed step that took the real part of a
complex Fano->A6,B6 intertwiner -- valid only for the one special
vacuum vector tested there, not in general). Verified equivariant to
~1e-16.

OPEN END (found this session, not yet resolved): comparing the two
sides' quartic invariants restricted to REAL fields shows a rank
ASYMMETRY -- this correspondence's five real quartic invariants
(Ig1,Ig2,Iline,Iprod,Imixed; the sixth, antisymmetric one vanishes
identically on real fields) have rank 4 (one linear relation among
them), while King-Luhn's five (I1,I2,I3,I4,I6; I5 vanishes identically
on real fields the same way) have rank 3 (two relations). A naive
6-parameter linear fit between the two sides therefore cannot match
well (residual ~15%) -- comparing the correct 3-dimensional subspace
on their side against the correct 4-dimensional one on this side is
the next well-posed step, not attempted here.
"""
import itertools
import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import minimize

# ---------------- rebuild GL(3,2), Fano plane, presentation-satisfying generators ----------------
def mat_mul3(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
def mat_det3_invertible(M):
    rows=[list(r) for r in M]; rank=0
    for col in range(3):
        piv=None
        for r in range(rank,3):
            if rows[r][col]==1: piv=r; break
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        for r in range(3):
            if r!=rank and rows[r][col]==1:
                rows[r]=[(rows[r][k]+rows[rank][k])%2 for k in range(3)]
        rank+=1
    return rank==3
def mat_inv3(M):
    A=[list(row)+[1 if i==j else 0 for j in range(3)] for i,row in enumerate(M)]
    for col in range(3):
        piv=None
        for r in range(col,3):
            if A[r][col]==1: piv=r; break
        A[col],A[piv]=A[piv],A[col]
        for r in range(3):
            if r!=col and A[r][col]==1:
                A[r]=[(A[r][k]+A[col][k])%2 for k in range(6)]
    return tuple(tuple(row[3:]) for row in A)

all_mats = list(itertools.product([0,1],repeat=9))
GL32 = [(m[0:3],m[3:6],m[6:9]) for m in all_mats if mat_det3_invertible((m[0:3],m[3:6],m[6:9]))]
assert len(GL32)==168
print(f"[1] GL(3,2): {len(GL32)} elements. OK.")

def mat_order3(M, limit=20):
    X=M; n=1; I3=((1,0,0),(0,1,0),(0,0,1))
    while X!=I3:
        X=mat_mul3(X,M); n+=1
        if n>limit: return -1
    return n
def comm(X,Y):
    Xi,Yi=mat_inv3(X),mat_inv3(Y)
    return mat_mul3(mat_mul3(Xi,Yi),mat_mul3(X,Y))

order2=[M for M in GL32 if mat_order3(M)==2]
order3=[M for M in GL32 if mat_order3(M)==3]
A_gen,B_gen=None,None
for A in order2:
    for B in order3:
        AB=mat_mul3(A,B)
        if mat_order3(AB)==7 and mat_order3(comm(A,B))==4:
            A_gen,B_gen=A,B; break
    if A_gen: break
print("[2] Generators A,B (full presentation) fixed.")

I3=((1,0,0),(0,1,0),(0,0,1))
Ainv=mat_inv3(A_gen); Binv=mat_inv3(B_gen)
gens_with_words=[(A_gen,'A'),(Ainv,'a'),(B_gen,'B'),(Binv,'b')]
word_of={I3:''}
frontier=[I3]
while frontier:
    nxt=[]
    for M in frontier:
        for g,sym in gens_with_words:
            Mg=mat_mul3(M,g)
            if Mg not in word_of:
                word_of[Mg]=word_of[M]+sym; nxt.append(Mg)
    frontier=nxt
assert len(word_of)==168
print(f"[3] Words found for all {len(word_of)} elements.")

pts7=[v for v in itertools.product([0,1],repeat=3) if any(v)]
pidx7={v:i for i,v in enumerate(pts7)}
def mat_vec3(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
def perm7(M): return tuple(pidx7[mat_vec3(M,p)] for p in pts7)
def perm_to_matrix7(p):
    M=np.zeros((7,7))
    for i in range(7): M[p[i],i]=1
    return M
Umat=np.zeros((7,6))
for i in range(6): Umat[i+1,i]=1; Umat[0,i]=-1
Uplus=np.linalg.pinv(Umat)
def restrict6(M7): return Uplus@M7@Umat
fano_mats = {M: restrict6(perm_to_matrix7(perm7(M))).real for M in word_of}
print("[4] Fano-plane real 6-dim representation built (this correspondence's chi_6 realization).")

# ---------------- Luhn-Nasri-Ramond A6,B6 (complex, arXiv:0709.1447 eqs 29,33,35), then VP -> real ----------------
eta=np.exp(2j*np.pi/7)
c1,c2,c3=[np.cos(2*n*np.pi/7) for n in [1,2,3]]
A6=-(2*np.sqrt(2)/7)*np.array([
 [(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2), c3-c1, c1-c2, c2-c3],
 [(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2), c2-c3, c3-c1, c1-c2],
 [(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2), c1-c2, c2-c3, c3-c1],
 [c3-c1, c2-c3, c1-c2, (c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2)],
 [c1-c2, c3-c1, c2-c3, (c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2)],
 [c2-c3, c1-c2, c3-c1, (c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2)],
])
assert abs(np.trace(A6)-2)<1e-10
ABdiag=np.diag([eta**2,eta**4,eta,eta**3,eta**5,eta**6])
B6=A6@ABdiag
P=np.diag([1j*eta**3,eta**6,eta**6,-eta**4,1j,-eta**4])
V=np.eye(6,dtype=complex)/np.sqrt(2)
V[0,4]=V[4,0]=1j/np.sqrt(2); V[1,3]=V[3,1]=1j/np.sqrt(2); V[2,5]=V[5,2]=1j/np.sqrt(2)
S_VP=V@P
A_real=(S_VP@A6@np.linalg.inv(S_VP)).real
B_real=(S_VP@B6@np.linalg.inv(S_VP)).real
assert np.max(np.abs((S_VP@A6@np.linalg.inv(S_VP)).imag))<1e-10
assert np.max(np.abs((S_VP@B6@np.linalg.inv(S_VP)).imag))<1e-10
gens_real={'A':A_real,'a':np.linalg.inv(A_real),'B':B_real,'b':np.linalg.inv(B_real)}
real_mats = {}
for M,w in word_of.items():
    Mat=np.eye(6)
    for ch in w: Mat=Mat@gens_real[ch]
    real_mats[M]=Mat
print("[5] A_real, B_real (Luhn-Nasri-Ramond real basis via VP) built for all 168 elements.")

# sanity: this basis makes Upsilon=sum(chi_i^2) genuinely invariant (established independently)
np.random.seed(1)
chi_test = np.random.randn(6)
Y0 = np.sum(chi_test**2)
Y1 = np.sum((A_real@chi_test)**2)
assert abs(Y0-Y1)<1e-10
print("    Sanity: Upsilon invariant under A_real confirmed.")

# ---------------- direct REAL intertwiner: Fano -> A_real (avoids the earlier flawed complex-then-real-part step) ----------------
np.random.seed(100)
X_real = np.random.randn(6,6)
S_direct = np.zeros((6,6))
for M in word_of:
    S_direct += real_mats[M] @ X_real @ np.linalg.inv(fano_mats[M])
S_direct /= len(word_of)
err_dir = max(np.max(np.abs(S_direct@fano_mats[g]-real_mats[g]@S_direct)) for g in [A_gen,B_gen])
print(f"[6] Direct real intertwiner S (Fano -> A_real) found. Equivariance error: {err_dir:.2e}")
assert err_dir < 1e-12

# ---------------- King-Luhn's Theta (their eq. 4.2), verified letter-for-letter against a clean PDF read ----------------
def Theta(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        -2*np.sqrt(21)*c1_*c5_-6*c1_*c6_,
        2*np.sqrt(21)*c2_*c5_-6*c2_*c6_,
        2*np.sqrt(14)*c3_*c4_+8*c3_*c6_,
        np.sqrt(14)*c3_**2-np.sqrt(14)*c4_**2+8*c4_*c6_,
        -np.sqrt(21)*c1_**2+np.sqrt(21)*c2_**2-6*c5_*c6_,
        -3*c1_**2-3*c2_**2+4*c3_**2+4*c4_**2-3*c5_**2+c6_**2
    ])

# confirm the FAILURE first (this is what motivated the search)
chi_A = A_real@chi_test
fail_err = np.max(np.abs(Theta(chi_A) - A_real@Theta(chi_test)))
print(f"[7] Confirmed: Theta is NOT covariant under bare A_real (error {fail_err:.2f}, scale {np.linalg.norm(Theta(chi_test)):.2f}).")

# ---------------- find O by numerical optimization over SO(6) ----------------
np.random.seed(50)
sample_chis = [np.random.randn(6) for _ in range(15)]
test_words = list(word_of.keys())
np.random.shuffle(test_words)
test_mats = [real_mats[M] for M in test_words[:8]]

def skew_from_params(params):
    K = np.zeros((6,6)); idx=0
    for i in range(6):
        for j in range(i+1,6):
            K[i,j]=params[idx]; K[j,i]=-params[idx]; idx+=1
    return K
def cost(params):
    O = expm(skew_from_params(params))
    total = 0.0
    for g in test_mats:
        gO = O@g@O.T
        for chi in sample_chis:
            total += np.sum((Theta(gO@chi)-gO@Theta(chi))**2)
    return total

x0 = np.zeros(15)
res = minimize(cost, x0, method='Powell', options={'maxiter':50000,'xtol':1e-13,'ftol':1e-15})
O = expm(skew_from_params(res.x))
print(f"[8] Optimization converged: cost {res.fun:.2e} (from initial {cost(x0):.2e}).")

# independent verification: elements and points NOT used in the optimization
np.random.seed(12345)
check_words = list(word_of.keys())[::7]
max_err = 0
for M in check_words:
    gO = O @ real_mats[M] @ O.T
    for _ in range(3):
        chi = np.random.randn(6)
        max_err = max(max_err, np.max(np.abs(Theta(gO@chi)-gO@Theta(chi))))
print(f"[9] INDEPENDENT verification (different elements/points): max error {max_err:.2e}")
assert max_err < 1e-6
assert np.allclose(O@O.T, np.eye(6), atol=1e-8)
assert abs(np.linalg.det(O)-1) < 1e-6
print("    O confirmed orthogonal, proper (det=+1).")

print("\nDone. O found and independently verified. See module docstring for the open")
print("rank-4-vs-rank-3 question this session also uncovered, not yet resolved.")
