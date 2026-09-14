"""
_explore_fano_degree_check_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Diagnostic prompted by the failed change-of-basis in
_explore_fano_kingluhn_channels_2026-09-14.py (residual ~15, not ~0).

Hypothesis: Ilya's six Fano invariants are NOT all quartic. King-Luhn's six
are all quartic ((6x6)_s (x) (6x6)_s -> degree (2,2) in (chi,chibar)). If one
of Ilya's six is a different degree, his set cannot span King-Luhn's quartic
space, and his stated "rank 6 = matches King-Luhn's six quartic invariants"
would be a count-coincidence, not an identification.

Tests:
  (T1) homogeneity degree of each Ilya invariant, by scaling chi -> t*chi.
  (T2) dimension of the space of PSL(2,7)-invariant quartic (2,2) forms
       (should be 6, = sum of squared multiplicities in Sym^2(6)).
  (T3) how many of Ilya's six are quartic, and do those span King-Luhn's
       6-dim quartic space or only a subspace? identify the missing direction.
"""
import itertools, numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=140)

# ---- machinery (same as sibling scripts) ----
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
GL=[(m[0:3],m[3:6],m[6:9]) for m in itertools.product([0,1],repeat=9)
    if det_ok((m[0:3],m[3:6],m[6:9]))]
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

lines=[]
for a in pts:
    for b in pts:
        if a==b: continue
        c=tuple((a[i]+b[i])%2 for i in range(3))
        if c==(0,0,0): continue
        L=frozenset([pidx[a],pidx[b],pidx[c]])
        if L not in lines: lines.append(L)
lines=[sorted(L) for L in lines]
def fano_invs(chi_lnr):
    v6=Sinv@chi_lnr; chis=[-sum(v6)]+list(v6)
    Ig1=(sum(abs(c)**2 for c in chis))**2
    Ig2=sum(abs(c)**4 for c in chis)
    Iln=sum(abs(chis[a]+chis[b]+chis[cc])**4 for (a,b,cc) in lines)
    Ipr=abs(sum(chis[a]*chis[b]*chis[cc] for (a,b,cc) in lines))**2
    tot=sum(abs(c)**2 for c in chis)
    Imx=sum(abs(chis[a]+chis[b]+chis[cc])**2*(tot-abs(chis[a])**2-abs(chis[b])**2-abs(chis[cc])**2) for (a,b,cc) in lines)
    Ias=sum(abs(chis[i].conjugate()*chis[j]-chis[j].conjugate()*chis[i])**2 for i in range(7) for j in range(i+1,7))
    return np.array([Ig1,Ig2,Iln,Ipr,Imx,Ias])
NAMES=["Ig1","Ig2","Iline","Iprod","Imixed","Iantisym"]

# ---- T1: homogeneity degree ----
print("[T1] homogeneity degree of each Ilya invariant (I(t*chi)/I(chi) vs t^4, t^6):")
np.random.seed(3); x=np.random.randn(6)+1j*np.random.randn(6); t=2.0
r=fano_invs(t*x)/fano_invs(x)
for k,n in enumerate(NAMES):
    deg=np.log(r[k])/np.log(t)
    print(f"     {n:>9}: ratio {r[k]:9.3f}   => degree {deg:.3f}   ({'QUARTIC' if abs(deg-4)<0.05 else 'SEXTIC' if abs(deg-6)<0.05 else '??'})")

# ---- T2: dim of the quartic (2,2) invariant space, via Sym^2 multiplicities ----
# = sum of squared multiplicities of irreps in Sym^2(6). Build Sym^2 character.
def trace_sym2(g):
    R=paper[g]; return (np.trace(R)**2+np.trace(R@R))/2
# multiplicity of each irrep = <chi_sym2, chi_irr>. Use class sums via order (7A/7B combine, ok for real irreps;
# for chi_3/chi_3bar we separate by the two order-7 classes).
# Simpler: dim(quartic (2,2) invariants) = <Sym2 (x) conj(Sym2), triv> = <Sym2,Sym2> = (1/|G|) sum |chi_sym2(g)|^2
dimq=sum(abs(trace_sym2(g))**2 for g in elts)/168
print(f"\n[T2] dim of PSL(2,7)-invariant quartic (2,2) forms = <Sym2,Sym2> = {dimq.real:.4f}  (expect 6)")

# ---- T3: which of Ilya's six are quartic; do they span King-Luhn's 6-dim quartic space? ----
# Build a generic basis of quartic (2,2) invariants by group-averaging random Hermitian quartics:
#   Q_H(chi) = <T, H T>,  T=chi (x) chi symmetric,  H a 21x21 Hermitian equivariant operator.
# Equivariant Hermitian H span exactly the 6-dim space. Get 6 independent ones.
symbasis=[]
for i in range(6):
    E=np.zeros((6,6),complex); E[i,i]=1; symbasis.append(E)
for i in range(6):
    for j in range(i+1,6):
        E=np.zeros((6,6),complex); E[i,j]=E[j,i]=1/np.sqrt(2); symbasis.append(E)
def mat2vec(T): return np.array([np.vdot(B,T) for B in symbasis])
def vec2mat(v): return sum(v[k]*symbasis[k] for k in range(21))
def Aop(R):
    return np.array([mat2vec(R@vec2mat(np.eye(21)[k])@R.T) for k in range(21)]).T
Aops={M:Aop(paper[M]) for M in elts}
Hbasis=[]
for s in range(12):
    np.random.seed(100+s); K=np.random.randn(21,21)+1j*np.random.randn(21,21); K=K+K.conj().T
    Heq=sum(Aops[M]@K@Aops[M].conj().T for M in elts)/168
    Hbasis.append(Heq)
def quartic_from_H(H,chi):
    t=mat2vec(np.outer(chi,chi)); return (t.conj()@H@t).real
# sample and build value matrices
np.random.seed(9); S6=[np.random.randn(6)+1j*np.random.randn(6) for _ in range(80)]
QH=np.array([[quartic_from_H(H,x) for H in Hbasis] for x in S6])  # 80 x 12, spans quartic space
qdim=np.linalg.matrix_rank(QH,tol=1e-6); print(f"     independent quartic invariants among 12 random equivariant H: rank {qdim} (expect 6)")
FAN=np.array([fano_invs(x) for x in S6])                          # 80 x 6 (Ilya)
# which Ilya invariants lie in the quartic span? fit each Ilya col from QH:
print("\n[T3] is each Ilya invariant inside the quartic (2,2) span?")
for k,n in enumerate(NAMES):
    coef,res,rk,sv=np.linalg.lstsq(QH,FAN[:,k],rcond=None)
    fit=QH@coef; rel=np.linalg.norm(fit-FAN[:,k])/np.linalg.norm(FAN[:,k])
    print(f"     {n:>9}: rel residual fitting from quartic span = {rel:.2e}  ({'in quartic space' if rel<1e-6 else 'NOT quartic'})")
# how many of Ilya's six are quartic, and what subspace-dim of the 6-dim quartic space do they cover?
quartic_cols=[k for k in range(6) if np.linalg.norm((QH@np.linalg.lstsq(QH,FAN[:,k],rcond=None)[0])-FAN[:,k])/np.linalg.norm(FAN[:,k])<1e-6]
FANq=FAN[:,quartic_cols]
print(f"\n     Ilya invariants that ARE quartic: {[NAMES[k] for k in quartic_cols]}")
print(f"     they span a subspace of the 6-dim quartic space of dim = {np.linalg.matrix_rank(FANq,tol=1e-6)}")
print("\nDone. [free exploration; not a sealed stone]")
