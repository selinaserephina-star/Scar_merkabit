"""
_explore_fano_intertwiner_metric_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Stenberg-side follow-on to Ilya's fano_intertwiner_found.py (Result 7).
Rule 3: the King-Luhn flavon PHYSICS stays parked out of the joint paper;
this is a free exploration of the MATHEMATICS of the intertwiner S, on
our side, to see whether the sqrt(7) in King-Luhn's open relation
kappa_2 = kappa_3 = kappa_4 + kappa_5/sqrt(7) is a geometric fact about
the Fano realization's invariant metric rather than a tuned coincidence.

Observation that triggered this: S has singular values
[0.203794, 0.077027 (x5)], ratio 2.6457.. = sqrt(7).

Questions:
  (Q1) Is the singular-value ratio EXACTLY sqrt(7)?
  (Q2) Then G = S^dag S (the rho_fano-invariant Hermitian metric) is
       proportional to  I + (7-1)*P  for a rank-1 projector P onto one
       distinguished direction. Which direction is it, in Fano
       coordinates? Is it the singlet/vacuum axis?
  (Q3) Independently: build the rho_fano-invariant metric directly by
       group-averaging  G0 = (1/|G|) sum_g rho_fano(g)^dag rho_fano(g).
       It must agree with S^dag S up to scale. Confirms the metric is a
       property of the Fano rep, nothing to do with the choice of S.
  (Q4) The Fano sextet = deleted permutation module on 7 points, sitting
       in R^7 as the sum-zero subspace under the NON-orthonormal frame U
       (U[0,:]=-1, U[1:,:]=I_6). The natural (permutation) metric on R^7
       is the identity; pulled back through U it is NOT the identity on
       R^6. Compute that pullback metric U^T U and compare its spectrum
       to G. This is the concrete source of the stretch.
"""
import itertools
import numpy as np

# ---- rebuild GL(3,2) and the Fano sextet exactly as in the received scripts ----
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
def inv3(M):
    A=[list(r)+[1 if i==j else 0 for j in range(3)] for i,r in enumerate(M)]
    for c in range(3):
        p=next(r for r in range(c,3) if A[r][c]==1); A[c],A[p]=A[p],A[c]
        for r in range(3):
            if r!=c and A[r][c]==1: A[r]=[(A[r][k]+A[c][k])%2 for k in range(6)]
    return tuple(tuple(r[3:]) for r in A)
def det_ok(M):
    rows=[list(r) for r in M]; rk=0
    for c in range(3):
        p=next((r for r in range(rk,3) if rows[r][c]==1),None)
        if p is None: continue
        rows[rk],rows[p]=rows[p],rows[rk]
        for r in range(3):
            if r!=rk and rows[r][c]==1: rows[r]=[(rows[r][k]+rows[rk][k])%2 for k in range(3)]
        rk+=1
    return rk==3
def order(M,lim=20):
    I=((1,0,0),(0,1,0),(0,0,1)); X=M; n=1
    while X!=I:
        X=mm(X,M); n+=1
        if n>lim: return -1
    return n
def comm(X,Y): return mm(mm(inv3(X),inv3(Y)),mm(X,Y))

GL=[ (m[0:3],m[3:6],m[6:9]) for m in itertools.product([0,1],repeat=9)
     if det_ok((m[0:3],m[3:6],m[6:9])) ]
assert len(GL)==168
o2=[M for M in GL if order(M)==2]; o3=[M for M in GL if order(M)==3]
A_gen=B_gen=None
for A in o2:
    for B in o3:
        if order(mm(A,B))==7 and order(comm(A,B))==4: A_gen,B_gen=A,B; break
    if A_gen: break

pts=[v for v in itertools.product([0,1],repeat=3) if any(v)]
pidx={v:i for i,v in enumerate(pts)}
def mv(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
def perm(M): return tuple(pidx[mv(M,p)] for p in pts)
def pmat(p):
    P=np.zeros((7,7))
    for i in range(7): P[p[i],i]=1
    return P
U=np.zeros((7,6))
for i in range(6): U[i+1,i]=1; U[0,i]=-1
Up=np.linalg.pinv(U)
def rest(M7): return Up@M7@U

# all 168 fano matrices
I3=((1,0,0),(0,1,0),(0,0,1)); Ai=inv3(A_gen); Bi=inv3(B_gen)
gens=[(A_gen,'A'),(Ai,'a'),(B_gen,'B'),(Bi,'b')]
word={I3:''}; fr=[I3]
while fr:
    nx=[]
    for M in fr:
        for g,s in gens:
            Mg=mm(M,g)
            if Mg not in word: word[Mg]=word[M]+s; nx.append(Mg)
    fr=nx
fano={M: rest(pmat(perm(M))) for M in word}

# ---- LNR paper sextet, unitary realization ----
eta=np.exp(2j*np.pi/7)
c1,c2,c3=[np.cos(2*n*np.pi/7) for n in (1,2,3)]
A6=-(2*np.sqrt(2)/7)*np.array([
 [(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2), c3-c1, c1-c2, c2-c3],
 [(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2), c2-c3, c3-c1, c1-c2],
 [(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2), c1-c2, c2-c3, c3-c1],
 [c3-c1, c2-c3, c1-c2, (c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2)],
 [c1-c2, c3-c1, c2-c3, (c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2)],
 [c2-c3, c1-c2, c3-c1, (c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2)]])
ABdiag=np.diag([eta**2,eta**4,eta,eta**3,eta**5,eta**6]); B6=A6@ABdiag
g6={'A':A6,'a':np.linalg.inv(A6),'B':B6,'b':np.linalg.inv(B6)}
def pw(w):
    M=np.eye(6,dtype=complex)
    for ch in w: M=M@g6[ch]
    return M
paper={M: pw(word[M]) for M in word}

# is the paper realization unitary?
paper_unit = max(np.linalg.norm(paper[M].conj().T@paper[M]-np.eye(6)) for M in word)
print(f"[0] paper realization unitary?  max||rho^dag rho - I|| = {paper_unit:.2e}")

# ---- S by group averaging ----
np.random.seed(0)
X=np.random.randn(6,6)+1j*np.random.randn(6,6)
S=sum(paper[M]@X@np.linalg.inv(fano[M]) for M in word)/168

sv=np.linalg.svd(S,compute_uv=False)
print(f"[1] singular values of S: {np.round(sv,6)}")
print(f"    ratio sv[0]/sv[1] = {sv[0]/sv[1]:.10f}   sqrt(7) = {np.sqrt(7):.10f}")
print(f"    (ratio)^2 = {(sv[0]/sv[1])**2:.10f}   (expect 7)")

# ---- Q2/Q3: the invariant metric ----
G = S.conj().T@S
G0 = sum(fano[M].conj().T@fano[M] for M in word)/168     # direct group average
# normalise both to smallest eigenvalue 1
def norm_metric(M):
    w=np.linalg.eigvalsh(M); return M/ w[0]
Gn, G0n = norm_metric(G), norm_metric(G0)
print(f"\n[2] eig(S^dag S) normalised: {np.round(np.linalg.eigvalsh(Gn),6)}")
print(f"    eig(group-avg metric)   : {np.round(np.linalg.eigvalsh(G0n),6)}")
print(f"    ||S^dag S  -  group-avg metric|| (both normalised) = {np.linalg.norm(Gn-G0n):.2e}")

# distinguished direction = eigenvector of the large eigenvalue
w,V=np.linalg.eigh(G0n); big=V[:,np.argmax(w)]
print(f"\n[3] distinguished (stretched) direction in Fano 6-coords:")
print(f"    {np.round(big/np.max(np.abs(big)),4)}")

# ---- Q4: pullback of the plain 7-metric through U ----
UtU = U.T@U
print(f"\n[4] pullback metric U^T U (plain permutation metric on R^7, restricted):")
print(f"    eig(U^T U) = {np.round(np.linalg.eigvalsh(UtU),6)}   -> normalised {np.round(np.linalg.eigvalsh(UtU/np.linalg.eigvalsh(UtU)[0]),6)}")
# compare directions
wu,Vu=np.linalg.eigh(UtU); bigu=Vu[:,np.argmax(wu)]
overlap=abs(big.conj()@ (bigu/np.linalg.norm(bigu)))/np.linalg.norm(big)
print(f"    |<stretched dir | U^TU big dir>| = {overlap:.6f}  (1.0 = same axis)")

# ---- is the stretched axis the S4 vacuum axis? ----
vac=np.array([-3,-3,4,4,-3,-3],dtype=float)  # Ilya's S4-line vacuum in fano 6-coords
ov_vac=abs(big.conj()@(vac/np.linalg.norm(vac)))/np.linalg.norm(big)
print(f"\n[5] |<stretched dir | S4 vacuum>| = {ov_vac:.6f}")
# and the all-equal / singlet-ish direction (image of constant under U^+)?
const7=np.ones(7); singlet6=Up@const7
ov_s=abs(big.conj()@(singlet6/np.linalg.norm(singlet6)))/np.linalg.norm(big)
print(f"    |<stretched dir | U^+ (1,...,1)>| = {ov_s:.6f}")
print("\nDone. [free exploration; not a sealed stone]")
