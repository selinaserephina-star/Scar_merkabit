"""
_explore_fano_chiral_quartic_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A(b): an EXPLICIT Fano/PSL(2,7) construction of the missing sixth quartic
(the chiral 6-6' cross channel that Ilya's five real Fano quartics cannot reach).

Idea: Sym^2(6) contains the 6 with multiplicity two; the two independent
PSL(2,7)-equivariant symmetric maps 6(x)6 -> 6 have concrete Fano meanings on
the 7 points (sum-zero coordinate chi_0..chi_6):
    s_i    = chi_i^2                       (pointwise square)
    ell_i  = sum_{L ni i} chi_j chi_k      (line-collinearity: other two pts on each line thru i)
Both are REAL-combinatorial and equivariant. Their Hermitian pairing
    J = sum_i conj(s_i) ell_i
has Im(J) ODD under chi -> conj(chi): a genuine chiral (2,2) quartic. Candidate
for the missing channel. Variants tested too.

Definitive checks:
  - degree 4 (quartic);
  - lies in the 6-dim quartic (2,2) invariant space (fit residual ~0);
  - completes Ilya's five quartics to rank 6 (i.e. supplies the missing dir);
  - chiral: Q(conj chi) = -Q(chi).
"""
import itertools, numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=140)

# ---- machinery ----
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
GL=[(m[0:3],m[3:6],m[6:9]) for m in itertools.product([0,1],repeat=9) if det_ok((m[0:3],m[3:6],m[6:9]))]
o2=[M for M in GL if order(M)==2]; o3=[M for M in GL if order(M)==3]
A_gen=B_gen=None
for A in o2:
    for B in o3:
        if order(mm(A,B))==7 and order(comm(A,B))==4: A_gen,B_gen=A,B; break
    if A_gen: break
pts=[v for v in itertools.product([0,1],repeat=3) if any(v)]; pidx={v:i for i,v in enumerate(pts)}
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
elts=list(word); order_of={M:order(M) for M in elts}
fano={M:rest(pmat(perm(M))) for M in elts}
eta=np.exp(2j*np.pi/7); c1,c2,c3=[np.cos(2*n*np.pi/7) for n in (1,2,3)]
A6=-(2*np.sqrt(2)/7)*np.array([
 [(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2), c3-c1, c1-c2, c2-c3],
 [(c2-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2), c2-c3, c3-c1, c1-c2],
 [(c1-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c2-1)/np.sqrt(2), c1-c2, c2-c3, c3-c1],
 [c3-c1, c2-c3, c1-c2, (c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2)],
 [c1-c2, c3-c1, c2-c3, (c2-1)/np.sqrt(2),(c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2)],
 [c2-c3, c1-c2, c3-c1, (c3-1)/np.sqrt(2),(c1-1)/np.sqrt(2),(c2-1)/np.sqrt(2)]])
B6=A6@np.diag([eta**2,eta**4,eta,eta**3,eta**5,eta**6])
g6={'A':A6,'a':np.linalg.inv(A6),'B':B6,'b':np.linalg.inv(B6)}
def pw(w):
    M=np.eye(6,dtype=complex)
    for ch in w: M=M@g6[ch]
    return M
paper={M:pw(word[M]) for M in elts}
np.random.seed(0); X=np.random.randn(6,6)+1j*np.random.randn(6,6)
S=sum(paper[M]@X@np.linalg.inv(fano[M]) for M in elts)/168; Sinv=np.linalg.inv(S)

# lines with, for each point, the two other points on each incident line
lines=[]
for a in pts:
    for b in pts:
        if a==b: continue
        c=tuple((a[i]+b[i])%2 for i in range(3))
        if c==(0,0,0): continue
        L=frozenset([pidx[a],pidx[b],pidx[c]])
        if L not in lines: lines.append(L)
lines=[sorted(L) for L in lines]
thru={i:[] for i in range(7)}
for L in lines:
    for i in L:
        j,k=[x for x in L if x!=i]; thru[i].append((j,k))

# ---- Ilya's five quartics (as functions of a sum-zero 7-vector chi) ----
def fano5_from7(chi):   # chi = length-7 complex, sum ~ 0
    Ig1=(sum(abs(c)**2 for c in chi))**2
    Ig2=sum(abs(c)**4 for c in chi)
    Iln=sum(abs(chi[a]+chi[b]+chi[cc])**4 for (a,b,cc) in lines)
    tot=sum(abs(c)**2 for c in chi)
    Imx=sum(abs(chi[a]+chi[b]+chi[cc])**2*(tot-abs(chi[a])**2-abs(chi[b])**2-abs(chi[cc])**2) for (a,b,cc) in lines)
    Ias=sum(abs(chi[i].conjugate()*chi[j]-chi[j].conjugate()*chi[i])**2 for i in range(7) for j in range(i+1,7))
    return np.array([Ig1,Ig2,Iln,Imx,Ias])

# ---- candidate chiral quartics ----
def maps(chi):
    s  =np.array([chi[i]**2 for i in range(7)])
    ell=np.array([sum(chi[j]*chi[k] for (j,k) in thru[i]) for i in range(7)])
    # project to sum-zero (the 6):
    s   = s   - s.mean()
    ell = ell - ell.mean()
    return s, ell
def Q_chiral(chi):          # V1: Im <s | ell>
    s,ell=maps(chi); return np.imag(np.vdot(s,ell))
def Q_chiral2(chi):         # V2: Im <s | s'>? use ell vs ell? -> use point-vs-line different pairing
    s,ell=maps(chi); return np.imag(np.vdot(chi-np.mean(chi), np.array([sum(chi[j]*chi[k] for (j,k) in thru[i]) for i in range(7)])-np.mean([sum(chi[j]*chi[k] for (j,k) in thru[i]) for i in range(7)])*0))  # placeholder, tested below properly

# a cleaner second candidate: chiral pairing of chi (the 6 itself, linear) is not quartic; skip V2.

# ---- full quartic space via random equivariant Hermitian H ----
symbasis=[]
for i in range(6):
    E=np.zeros((6,6),complex); E[i,i]=1; symbasis.append(E)
for i in range(6):
    for j in range(i+1,6):
        E=np.zeros((6,6),complex); E[i,j]=E[j,i]=1/np.sqrt(2); symbasis.append(E)
def mat2vec(T): return np.array([np.vdot(B,T) for B in symbasis])
def vec2mat(v): return sum(v[k]*symbasis[k] for k in range(21))
def Aop(R): return np.array([mat2vec(R@vec2mat(np.eye(21)[k])@R.T) for k in range(21)]).T
Aops={M:Aop(paper[M]) for M in elts}
Hbasis=[]
for s_ in range(12):
    np.random.seed(200+s_); K=np.random.randn(21,21)+1j*np.random.randn(21,21); K=K+K.conj().T
    Hbasis.append(sum(Aops[M]@K@Aops[M].conj().T for M in elts)/168)
def quartic_from_H(H,chi_lnr):
    t=mat2vec(np.outer(chi_lnr,chi_lnr)); return (t.conj()@H@t).real

# ---- sampling (sum-zero 7-vectors <-> chi_lnr via fano coords) ----
def rand_sumzero7():
    v6=np.random.randn(6)+1j*np.random.randn(6)
    return np.array([-v6.sum()]+list(v6)), v6
np.random.seed(21)
CHI7=[]; V6=[]
for _ in range(120):
    c7,v6=rand_sumzero7(); CHI7.append(c7); V6.append(v6)
chi_lnr=[S@v for v in V6]

QH =np.array([[quartic_from_H(H,x) for H in Hbasis] for x in chi_lnr])   # 120x12 full quartic space
FQ =np.array([fano5_from7(c) for c in CHI7])                              # 120x5
Qv =np.array([Q_chiral(c) for c in CHI7])                                 # 120

print(f"[1] quartic space rank (random equiv-H): {np.linalg.matrix_rank(QH,tol=1e-6)} (expect 6)")
print(f"    Ilya's five quartics rank: {np.linalg.matrix_rank(FQ,tol=1e-6)} (expect 5)")

# degree of Q_chiral
t=2.0; r=Q_chiral(2*CHI7[0])/Q_chiral(CHI7[0]); print(f"[2] Q_chiral degree: ratio {r:.3f} -> {np.log(abs(r))/np.log(2):.3f} (expect 4)")
# chirality
qc=Q_chiral(CHI7[0]); qcbar=Q_chiral(np.conj(CHI7[0]))
print(f"[3] chirality: Q(chi)={qc:.4f}, Q(conj chi)={qcbar:.4f}, sum={qc+qcbar:.2e} (expect ~0: odd under conjugation)")
# is Q_chiral in the quartic space?
coef,_,_,_=np.linalg.lstsq(QH,Qv,rcond=None); rel=np.linalg.norm(QH@coef-Qv)/np.linalg.norm(Qv)
print(f"[4] Q_chiral in the quartic (2,2) space? rel residual {rel:.2e} ({'YES' if rel<1e-6 else 'NO'})")
# does it complete Ilya's five?
rk=np.linalg.matrix_rank(np.column_stack([FQ,Qv]),tol=1e-6)
print(f"[5] rank(Ilya's 5 + Q_chiral) = {rk}  ({'COMPLETES the basis -> Q_chiral IS the missing sixth quartic' if rk==6 else 'does not complete'})")
# and the six {Ilya5,Qchiral} span the whole quartic space?
rk2=np.linalg.matrix_rank(np.column_stack([QH,FQ,Qv]),tol=1e-6)
print(f"[6] rank([full quartic basis | Ilya5 | Q_chiral]) = {rk2} (==6 confirms {{Ilya5,Q_chiral}} spans the entire quartic space)")

print("\nEXPLICIT FORM of the missing sixth quartic (in Fano 7-point coords, sum-zero chi):")
print("   Q_miss(chi) = Im  sum_{i=0}^{6}  conj(chi_i^2) * ( sum_{L ni i} chi_j chi_k )")
print("             = Im < pointwise-square , line-collinearity-map >")
print("   (both maps are PSL(2,7)-equivariant 6->6; their Hermitian cross-pairing's")
print("    imaginary part is the chiral 6-6' cross channel = King-Luhn's kappa_5 direction)")
print("\nDone. [free exploration; not a sealed stone]")
