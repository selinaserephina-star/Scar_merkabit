"""
_explore_fano_kingluhn_channels_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A, open ends 1 & 2. Rule 3: King-Luhn PHYSICS parked out of the joint
paper; this is Stenberg-side free exploration of the MATHEMATICS.

Goal: build King-Luhn's six quartic invariants of chi_6 CANONICALLY from the
group -- the norms of the Clebsch-Gordan channels of (6 (x) 6)_s = 1+6+6'+8 --
in the unitary LNR basis, needing NO transcription of their eq. (4.1)-(4.7)
coefficients. Then express Ilya's six Fano-combinatorial invariants
(fano_sextet_six_invariants.py) in that channel basis, exactly (change of
basis, rank 6). Read off (a) where sqrt(7) enters and (b) how Ilya's derived
degeneracy condition 3*kappa_g2 = 2*kappa_mixed sits relative to King-Luhn's
kappa_2 = kappa_3 = kappa_4 + kappa_5/sqrt(7).

Everything is done in the unitary LNR sextet basis so the ordinary Hermitian
inner product is group-invariant and channel projectors are orthogonal.

FLAGS: King-Luhn's top vacuum (2.10) and LNR's singlet vev are TRANSCRIBED
from the paper via a web summariser; used only in clearly-marked side checks,
never in the canonical channel construction.
"""
import itertools, numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=140)

# ======================================================================
# 0. Rebuild GL(3,2), the Fano sextet, the LNR unitary sextet, and S
#    (verbatim machinery from the received scripts)
# ======================================================================
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
assert len(GL)==168
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
elts=list(word); order_of={M: order(M) for M in elts}
fano={M: rest(pmat(perm(M))) for M in elts}

eta=np.exp(2j*np.pi/7); c1,c2,c3=[np.cos(2*n*np.pi/7) for n in (1,2,3)]
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
paper={M: pw(word[M]) for M in elts}
uni = max(np.linalg.norm(paper[M].conj().T@paper[M]-np.eye(6)) for M in elts)
print(f"[0] LNR realization unitary: max||U^dag U - I|| = {uni:.1e}  (channels will be orthogonal)")

# intertwiner S: chi_lnr = S @ chi_fano
np.random.seed(0); X=np.random.randn(6,6)+1j*np.random.randn(6,6)
S=sum(paper[M]@X@np.linalg.inv(fano[M]) for M in elts)/168
Sinv=np.linalg.inv(S)

# ======================================================================
# 1. Sym^2(6) as symmetric 6x6 matrices; group action T -> R T R^T (unitary
#    under Frobenius <S,T>=tr(S^dag T)); build isotypic projectors 1,6,8.
# ======================================================================
# orthonormal basis of symmetric complex matrices (21 of them)
symbasis=[]
for i in range(6):
    E=np.zeros((6,6),complex); E[i,i]=1; symbasis.append(E)
for i in range(6):
    for j in range(i+1,6):
        E=np.zeros((6,6),complex); E[i,j]=E[j,i]=1/np.sqrt(2); symbasis.append(E)
assert len(symbasis)==21
def mat2vec(T): return np.array([np.vdot(B,T) for B in symbasis])          # <B,T>=tr(B^dag T)
def vec2mat(v): return sum(v[k]*symbasis[k] for k in range(21))

# action operator A_g on the 21-space
def Aop(R):
    cols=[mat2vec(R@vec2mat(np.eye(21)[k])@R.T) for k in range(21)]
    return np.array(cols).T
Aops={M: Aop(paper[M]) for M in elts}

# characters by element order (both 7A,7B share values here)
chi = {1:{1:1,2:1,3:1,4:1,7:1},              # trivial
       6:{1:6,2:2,3:0,4:0,7:-1},             # chi_6
       8:{1:8,2:0,3:-1,4:0,7:1}}             # chi_8 (Steinberg)
def projector(irr,dim):
    P=sum(np.conj(chi[irr][order_of[M]])*Aops[M] for M in elts)*dim/168
    return P
P1=projector(1,1); P6=projector(6,6); P8=projector(8,8)
r1,r6,r8=[int(round(np.trace(P).real)) for P in (P1,P6,P8)]
print(f"[1] Sym^2(6)=1+6+6'+8 : isotypic ranks  1->{r1}, 6-iso->{r6}, 8->{r8}  (sum {r1+r6+r8}/21)")
assert (r1,r6,r8)==(1,12,8)
assert np.linalg.norm(P1+P6+P8-np.eye(21))<1e-9

# ======================================================================
# 2. Split the 6-isotypic block (12-dim = 6 (x) C^2) into 6 and 6', and
#    build the equivariant cross-map, all canonically up to the mult-space
#    basis (exactly King-Luhn's Theta/Theta' labelling freedom).
# ======================================================================
np.random.seed(1); K=np.random.randn(21,21)+1j*np.random.randn(21,21); K=K+K.conj().T
Craw=P6@K@P6
Ceq=sum(Aops[M]@Craw@Aops[M].conj().T for M in elts)/168   # equivariant, Hermitian, in 6-block
w,V=np.linalg.eigh(Ceq)
nz=[k for k in range(21) if abs(w[k])>1e-6]
vals=np.round(w[nz],6)
# two distinct eigenvalues, each multiplicity 6
uniq=sorted(set(np.round(w[nz],5)))
assert len(uniq)==2, f"expected 2 eigenvalues in 6-block, got {uniq}"
Qa=sum(np.outer(V[:,k],V[:,k].conj()) for k in nz if abs(w[k]-uniq[0])<1e-4)  # copy a (Theta)
Qb=sum(np.outer(V[:,k],V[:,k].conj()) for k in nz if abs(w[k]-uniq[1])<1e-4)  # copy b (Theta')
print(f"[2] 6-block split by a commutant operator: two 6-copies, ranks {int(round(np.trace(Qa).real))},{int(round(np.trace(Qb).real))}")
# equivariant partial isometry  Xcross: copy b -> copy a
X0=Qa@(np.random.randn(21,21)+1j*np.random.randn(21,21))@Qb
Xcross=sum(Aops[M]@X0@Aops[M].conj().T for M in elts)/168
# normalise so it's a partial isometry (singular values 1 on the 6-block)
sv=np.linalg.svd(Xcross,compute_uv=False); Xcross=Xcross/sv[0]

# ======================================================================
# 3. The six King-Luhn channel invariants as functions of chi (LNR coords)
# ======================================================================
def channels(chi_lnr):
    T=np.outer(chi_lnr,chi_lnr)          # holomorphic symmetric tensor chi_i chi_j
    t=mat2vec(T)
    I1 = (t.conj()@P1@t).real            # |1|^2
    I2 = (t.conj()@Qa@t).real            # |6|^2   (Theta)
    I3 = (t.conj()@Qb@t).real            # |6'|^2  (Theta')
    I8 = (t.conj()@P8@t).real            # |8|^2
    J  = t.conj()@Xcross@t               # complex cross  <Theta|Theta'>-type
    I4 = J.real; I5 = J.imag             # the (1/sqrt2)(Theta'bar Theta +- h.c.) pair (up to norm)
    return np.array([I1,I2,I3,I8,I4,I5])
KL_names=["I1=|1|^2","I2=|6|^2","I3=|6'|^2","I8=|8|^2","I4=Re<6|6'>","I5=Im<6|6'>"]

# ======================================================================
# 4. Ilya's six Fano invariants, as functions of chi (LNR coords -> Fano coords)
# ======================================================================
lines=[]
for a in pts:
    for b in pts:
        if a==b: continue
        c=tuple((a[i]+b[i])%2 for i in range(3))
        if c==(0,0,0): continue
        L=frozenset([pidx[a],pidx[b],pidx[c]])
        if L not in lines: lines.append(L)
lines=[sorted(L) for L in lines]; assert len(lines)==7
def fano_invs(chi_lnr):
    v6=Sinv@chi_lnr                       # Fano 6-coords
    chis=[-sum(v6)]+list(v6)
    Ig1=(sum(abs(c)**2 for c in chis))**2
    Ig2=sum(abs(c)**4 for c in chis)
    Iln=sum(abs(chis[a]+chis[b]+chis[cc])**4 for (a,b,cc) in lines)
    Ipr=abs(sum(chis[a]*chis[b]*chis[cc] for (a,b,cc) in lines))**2
    tot=sum(abs(c)**2 for c in chis)
    Imx=sum(abs(chis[a]+chis[b]+chis[cc])**2*(tot-abs(chis[a])**2-abs(chis[b])**2-abs(chis[cc])**2)
            for (a,b,cc) in lines)
    Ias=0
    for i in range(7):
        for j in range(i+1,7):
            Ias+=abs(chis[i].conjugate()*chis[j]-chis[j].conjugate()*chis[i])**2
    return np.array([Ig1,Ig2,Iln,Ipr,Imx,Ias])
FANO_names=["Ig1=(S|x|^2)^2","Ig2=S|x|^4","Iline","Iprod","Imixed","Iantisym"]

# ======================================================================
# 5. Change of basis: KL channel invariants  =  M @ Ilya Fano invariants
# ======================================================================
np.random.seed(7)
samples=[np.random.randn(6)+1j*np.random.randn(6) for _ in range(60)]
KLm =np.array([channels(x)  for x in samples])     # 60 x 6
FANm=np.array([fano_invs(x) for x in samples])     # 60 x 6
print(f"[3] rank of Ilya's six over 60 samples: {np.linalg.matrix_rank(FANm,tol=1e-6)} ;  KL six: {np.linalg.matrix_rank(KLm,tol=1e-6)}")
# solve KLm = FANm @ M^T  ->  M^T = pinv(FANm) @ KLm
Mt,res,rk,sv2=np.linalg.lstsq(FANm,KLm,rcond=None)
M=Mt.T
recon=FANm@M.T
print(f"[4] change-of-basis fit residual (max|KL - M*Fano|): {np.max(np.abs(recon-KLm)):.2e}  rank {rk}")
print(f"\n    M  (rows = KL channels, cols = Ilya Fano invariants):")
print(f"    {'':>14}"+"".join(f"{n:>13}" for n in FANO_names))
for i,n in enumerate(KL_names):
    print(f"    {n:>14}"+"".join(f"{M[i,j]:13.5f}" for j in range(6)))

# locate sqrt(7)=2.64575 signatures: ratios of entries
print(f"\n[5] sqrt(7) = {np.sqrt(7):.5f} ;  7 = 7.0 ;  1/sqrt(7)={1/np.sqrt(7):.5f}")
print("    notable entry ratios within rows (looking for sqrt7 / 7):")
for i,n in enumerate(KL_names):
    row=M[i]; nz=[(FANO_names[j],row[j]) for j in range(6) if abs(row[j])>1e-6]
    if len(nz)>=2:
        base=nz[0][1]
        rs=", ".join(f"{nm}:{val/base:+.4f}" for nm,val in nz)
        print(f"      {n:>14}: [{rs}]")

# ======================================================================
# 6. side check (TRANSCRIBED vectors, flagged): what symmetry does King-Luhn's
#    top vacuum (2.10) have, and is it Ilya's S4 (+4/-3) vacuum?
# ======================================================================
b7=(-1+1j*np.sqrt(7))/2
chi_top = ((1-1j)/(3*np.sqrt(2)))*np.array([1, 1j*np.sqrt(3), -1j*np.sqrt(3)/b7, -np.sqrt(3)/b7, -np.sqrt(2), 0])
# little group in LNR: elements g with paper[g] chi_top proportional to chi_top
def little_group(v):
    cnt=0
    for M in elts:
        w=paper[M]@v
        # projective fix: w parallel to v ?
        if np.linalg.norm(v)>1e-9:
            proj=np.vdot(v,w)/np.vdot(v,v)
            if np.linalg.norm(w-proj*v)<1e-6*np.linalg.norm(v): cnt+=1
    return cnt
lg_top=little_group(chi_top)
vac_fano=np.array([-3,-3,4,4,-3,-3],dtype=complex); vac_lnr=S@vac_fano
lg_vac=little_group(vac_lnr)
print(f"\n[6] (TRANSCRIBED, flagged) projective little group order:")
print(f"    King-Luhn top vacuum (2.10): |stab| = {lg_top}   (24 = S4 expected for a 3-3 top alignment)")
print(f"    Ilya's S4 (+4/-3) vacuum   : |stab| = {lg_vac}")
# are they the same ray up to the diagonal eta-twist freedom?
best=0
for exps in itertools.product(range(7),repeat=1):
    pass
ov=abs(np.vdot(vac_lnr/np.linalg.norm(vac_lnr), chi_top/np.linalg.norm(chi_top)))
print(f"    |<Ilya-vac | KL-top>| (raw, no relabel) = {ov:.4f}")
print("\nDone. [free exploration; not a sealed stone]")
