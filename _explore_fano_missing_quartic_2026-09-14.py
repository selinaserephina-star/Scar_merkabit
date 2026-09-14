"""
_explore_fano_missing_quartic_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A(a). Ilya's five QUARTIC Fano invariants span only a 5-dim subspace of
the 6-dim King-Luhn quartic space (shown in _explore_fano_degree_check). This
script:
  1. builds King-Luhn's six channel invariants canonically (1,6,6',8 of
     (6x6)_s), the full 6-dim quartic space;
  2. finds the 1-dim MISSING direction not covered by Ilya's five quartics,
     and identifies which channel(s) it is;
  3. searches natural Fano-combinatorial quartics for a nameable representative
     of the missing direction;
  4. redoes the full 6<->6 change of basis {Ilya 5 quartics + missing sixth}
     <-> {King-Luhn 6 channels}, now EXACT, and locates the sqrt(7).
All in the unitary LNR basis (ordinary inner product group-invariant).
"""
import itertools, numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=150)

# ---------- machinery ----------
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
lines=[]
for a in pts:
    for b in pts:
        if a==b: continue
        c=tuple((a[i]+b[i])%2 for i in range(3))
        if c==(0,0,0): continue
        L=frozenset([pidx[a],pidx[b],pidx[c]])
        if L not in lines: lines.append(L)
lines=[sorted(L) for L in lines]

# ---------- channel projectors ----------
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
chi={1:{1:1,2:1,3:1,4:1,7:1},6:{1:6,2:2,3:0,4:0,7:-1},8:{1:8,2:0,3:-1,4:0,7:1}}
def projector(irr,dim): return sum(np.conj(chi[irr][order_of[M]])*Aops[M] for M in elts)*dim/168
P1=projector(1,1); P6=projector(6,6); P8=projector(8,8)
np.random.seed(1); K=np.random.randn(21,21)+1j*np.random.randn(21,21); K=K+K.conj().T
Ceq=sum(Aops[M]@(P6@K@P6)@Aops[M].conj().T for M in elts)/168
w,V=np.linalg.eigh(Ceq); nz=[k for k in range(21) if abs(w[k])>1e-6]
uniq=sorted(set(np.round(w[nz],5)))
Qa=sum(np.outer(V[:,k],V[:,k].conj()) for k in nz if abs(w[k]-uniq[0])<1e-4)
Qb=sum(np.outer(V[:,k],V[:,k].conj()) for k in nz if abs(w[k]-uniq[1])<1e-4)
X0=Qa@(np.random.randn(21,21)+1j*np.random.randn(21,21))@Qb
Xcross=sum(Aops[M]@X0@Aops[M].conj().T for M in elts)/168
Xcross=Xcross/np.linalg.svd(Xcross,compute_uv=False)[0]
def channels(chi_lnr):
    t=mat2vec(np.outer(chi_lnr,chi_lnr))
    J=t.conj()@Xcross@t
    return np.array([(t.conj()@P1@t).real,(t.conj()@Qa@t).real,(t.conj()@Qb@t).real,
                     (t.conj()@P8@t).real,J.real,J.imag])
CH_names=["|1|^2","|6|^2","|6'|^2","|8|^2","Re<6|6'>","Im<6|6'>"]

# ---------- Ilya's five quartic invariants ----------
def fano5(chi_lnr):
    v6=Sinv@chi_lnr; chis=[-sum(v6)]+list(v6)
    Ig1=(sum(abs(c)**2 for c in chis))**2
    Ig2=sum(abs(c)**4 for c in chis)
    Iln=sum(abs(chis[a]+chis[b]+chis[cc])**4 for (a,b,cc) in lines)
    tot=sum(abs(c)**2 for c in chis)
    Imx=sum(abs(chis[a]+chis[b]+chis[cc])**2*(tot-abs(chis[a])**2-abs(chis[b])**2-abs(chis[cc])**2) for (a,b,cc) in lines)
    Ias=sum(abs(chis[i].conjugate()*chis[j]-chis[j].conjugate()*chis[i])**2 for i in range(7) for j in range(i+1,7))
    return np.array([Ig1,Ig2,Iln,Imx,Ias])
FQ_names=["Ig1","Ig2","Iline","Imixed","Iantisym"]

# ---------- candidate Fano quartics for the missing direction ----------
def cand(chi_lnr):
    v6=Sinv@chi_lnr; chis=[-sum(v6)]+list(v6)
    # C1: all point-pairs |chi_i chi_j|^2
    C1=sum(abs(chis[i])**2*abs(chis[j])**2 for i in range(7) for j in range(i+1,7))
    # C2: collinear pair products (pairs lying on a common line)
    C2=0.0
    for (a,b,cc) in lines:
        for i,j in [(a,b),(a,cc),(b,cc)]:
            C2+=abs(chis[i])**2*abs(chis[j])**2
    # C3: per-line symmetric pair-sum |chi_a chi_b + chi_b chi_c + chi_c chi_a|^2
    C3=sum(abs(chis[a]*chis[b]+chis[b]*chis[cc]+chis[a]*chis[cc])**2 for (a,b,cc) in lines)
    # C4: |sum_i chi_i^2|^2  (the trivial 1-channel of (6x6)_s in permutation coords)
    C4=abs(sum(c*c for c in chis))**2
    return np.array([C1,C2,C3,C4])
CAND_names=["C1=pairs|xi xj|^2","C2=collinear pairs","C3=line pair-sum^2","C4=|sum xi^2|^2"]

# ---------- sample ----------
np.random.seed(11); SMP=[np.random.randn(6)+1j*np.random.randn(6) for _ in range(120)]
CHm=np.array([channels(x) for x in SMP])   # 120x6 full quartic space
FQm=np.array([fano5(x)   for x in SMP])    # 120x5 Ilya quartics
CAm=np.array([cand(x)    for x in SMP])    # 120x4 candidates
print(f"[1] rank(King-Luhn 6 channels) = {np.linalg.matrix_rank(CHm,tol=1e-6)}  (full quartic space, expect 6)")
print(f"    rank(Ilya's 5 quartics)     = {np.linalg.matrix_rank(FQm,tol=1e-6)}  (expect 5)")

# ---------- missing direction in channel coordinates ----------
# express Ilya's 5 in channel basis: FQ = CH @ W  (W is 6x5)
W,_,_,_=np.linalg.lstsq(CHm,FQm,rcond=None)     # 6x5
resW=np.max(np.abs(CHm@W-FQm));
# missing = left-null of W  (6-vector orthogonal to columns of W)
u,s,vt=np.linalg.svd(W)
miss=u[:,-1]                                     # smallest singular direction -> orthogonal complement
miss=miss/np.max(np.abs(miss))
print(f"\n[2] Ilya's 5 quartics reconstructed from channels, residual {resW:.1e}")
print(f"    MISSING quartic direction, in channel coordinates {CH_names}:")
print(f"    {np.round(miss,4)}")
domi=np.argmax(np.abs(miss))
print(f"    dominant channel: {CH_names[domi]}  (weight {miss[domi]:.4f})")

# missing invariant as a function:
def missing_inv(x): return channels(x)@miss
# ---------- which candidate matches the missing direction? ----------
print(f"\n[3] do natural Fano candidates supply the missing 6th quartic? (rank of Ilya5 + candidate):")
for k,nm in enumerate(CAND_names):
    stack=np.column_stack([FQm,CAm[:,k]])
    rk=np.linalg.matrix_rank(stack,tol=1e-6)
    # correlation of candidate's missing-component with the missing direction
    coef,_,_,_=np.linalg.lstsq(np.column_stack([FQm,np.ones(len(SMP))]),CAm[:,k],rcond=None)
    resid=CAm[:,k]-np.column_stack([FQm,np.ones(len(SMP))])@coef
    mvals=np.array([missing_inv(x) for x in SMP]); mres=mvals-np.column_stack([FQm,np.ones(len(SMP))])@np.linalg.lstsq(np.column_stack([FQm,np.ones(len(SMP))]),mvals,rcond=None)[0]
    corr=abs(np.dot(resid,mres))/(np.linalg.norm(resid)*np.linalg.norm(mres)+1e-30)
    print(f"    {nm:>22}: rank(Ilya5+cand)={rk}  |corr with missing dir|={corr:.4f}  {'<-- COMPLETES BASIS' if rk==6 else ''}")

# ---------- dictionary W: Ilya's 5 quartics in King-Luhn channel coordinates ----------
print(f"\n[4] W: each Ilya quartic as a combination of King-Luhn channels (exact, residual {resW:.1e}):")
print(f"    {'':>10}"+"".join(f"{c:>11}" for c in CH_names))
for j,n in enumerate(FQ_names):
    print(f"    {n:>10}"+"".join(f"{W[i,j]:11.4f}" for i in range(6)))
print("    (note: |1|^2 and |8|^2 columns show which Ilya quartics carry singlet/octet weight)")

# ---------- no natural candidate worked; complete the basis with the canonical missing direction ----------
print(f"\n[5] No naive real Fano quartic (C1-C4) supplies the missing 6th; it is a chiral 6-6' cross channel.")
print(f"    Completing the basis with the canonical missing channel-direction itself.")
missvals=np.array([missing_inv(x) for x in SMP])                 # 120
FULL=np.column_stack([FQm,missvals])                            # 120x6, guaranteed rank 6
print(f"    rank(Ilya5 + missing) = {np.linalg.matrix_rank(FULL,tol=1e-6)}")
Mt,_,_,_=np.linalg.lstsq(FULL,CHm,rcond=None)
Mmat=Mt.T; res=np.max(np.abs(FULL@Mt-CHm))
cols=FQ_names+["MISS(6-6' chiral)"]
print(f"    change of basis [KL channels] = M [Ilya5 + MISS], residual {res:.2e}:")
print(f"    {'':>11}"+"".join(f"{c:>11}" for c in cols))
for i,n in enumerate(CH_names):
    print(f"    {n:>11}"+"".join(f"{Mmat[i,j]:11.4f}" for j in range(6)))

# ---------- locate sqrt(7) in the dictionary W (Ilya's real quartics -> channels) ----------
print(f"\n[6] sqrt7={np.sqrt(7):.5f}, 1/sqrt7={1/np.sqrt(7):.5f}, 7=7.0 ; scan W (Ilya->channel) ratios per Ilya-invariant:")
for j,n in enumerate(FQ_names):
    col=W[:,j]; base=col[np.argmax(np.abs(col))]
    rs=", ".join(f"{CH_names[i]}:{col[i]/base:+.4f}" for i in range(6) if abs(col[i])>1e-4)
    print(f"    {n:>10} (norm to {CH_names[np.argmax(np.abs(col))]}): [{rs}]")
print("\nDone. [free exploration; not a sealed stone]")
