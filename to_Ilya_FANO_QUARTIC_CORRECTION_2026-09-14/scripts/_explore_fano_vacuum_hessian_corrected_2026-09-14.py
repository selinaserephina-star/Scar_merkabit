"""
_explore_fano_vacuum_hessian_corrected_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A, open end 2. With the corrected six-quartic Fano basis
(Ilya's five real quartics + the chiral Q_miss), compute the Hessian of the
general quartic potential at the S4 "3-3" vacuum, decomposed into the
S4-blocks chi_6|_S4 = 1 (radial) + 2 (doublet) + 3 (triplet), and look for
sqrt(7) in the spectrum and the alignment/degeneracy condition.

Plan:
  (V) VALIDATE the Hessian machinery by reproducing Ilya's Result 3 doublet
      and triplet coefficients for his basis {g1,g2,line,mixed,prod(sextic)}.
  (C) Recompute on the CORRECTED basis {g1,g2,line,mixed,antisym,Q_miss},
      report the doublet/triplet eigenvalues as linear forms in the couplings,
      the degeneracy condition, and whether sqrt(7) enters (it can only come
      from the chiral Q_miss, which couples the real and imaginary sectors).

Hessian extraction: exact for quartics via 2-step Richardson second-difference
+ polarization; the sextic (Iprod) is handled the same way (small O(h^4) error,
only used in the validation step).
"""
import itertools, numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=160)

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
I3=((1,0,0),(0,1,0),(0,0,1))
allM=[M for M in GL]
fano={M:rest(pmat(perm(M))) for M in allM}

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

def chis_of(v6): return np.array([-v6.sum()]+list(v6))
# ---- invariants as functions of complex v6 ----
def Ig1(v6):
    ch=chis_of(v6); return (sum(abs(c)**2 for c in ch))**2
def Ig2(v6):
    ch=chis_of(v6); return sum(abs(c)**4 for c in ch)
def Iline(v6):
    ch=chis_of(v6); return sum(abs(ch[a]+ch[b]+ch[cc])**4 for (a,b,cc) in lines)
def Imixed(v6):
    ch=chis_of(v6); tot=sum(abs(c)**2 for c in ch)
    return sum(abs(ch[a]+ch[b]+ch[cc])**2*(tot-abs(ch[a])**2-abs(ch[b])**2-abs(ch[cc])**2) for (a,b,cc) in lines)
def Iantisym(v6):
    ch=chis_of(v6); return sum(abs(ch[i].conjugate()*ch[j]-ch[j].conjugate()*ch[i])**2 for i in range(7) for j in range(i+1,7))
def Iprod(v6):   # Ilya's SEXTIC
    ch=chis_of(v6); return abs(sum(ch[a]*ch[b]*ch[cc] for (a,b,cc) in lines))**2
def Qmiss(v6):   # chiral quartic
    ch=chis_of(v6)
    s=np.array([ch[i]**2 for i in range(7)]); ell=np.array([sum(ch[j]*ch[k] for (j,k) in thru[i]) for i in range(7)])
    s=s-s.mean(); ell=ell-ell.mean(); return float(np.imag(np.vdot(s,ell)))
def mass(v6):
    ch=chis_of(v6); return sum(abs(c)**2 for c in ch)

# ---- vacuum (Ilya's +4 on a line, -3 off), in v6 coords ----
v0=np.array([-3,-3,4,4,-3,-3],dtype=float)   # chi0 = -sum = 4  => +4 on {0,3,4}
ch0=chis_of(v0.astype(complex))
print(f"[0] vacuum chis = {ch0.real.astype(int)}  (+4 on 3 points, -3 on 4)")

# ---- S4 = stabiliser of v0 in PSL(2,7) ----
S4=[M for M in allM if np.allclose(fano[M]@v0, v0, atol=1e-9)]
print(f"    |stabiliser of v0| = {len(S4)} (expect 24 = S4)")
rho={M:fano[M] for M in S4}

# ---- real 12-dim tangent (Re,Im of v6); S4 acts as diag(rho,rho) ----
def emb(epsR,epsI): return epsR, epsI   # helper
def V_eval(func, epsR, epsI):
    return func(v0.astype(complex) + epsR + 1j*epsI)
def dir2nd(func, d):   # exact 2nd directional derivative for quartics via 2-step Richardson
    dR=d[:6]; dI=d[6:]
    def f(t): return V_eval(func, t*dR, t*dI)
    f0=f(0.0)
    def D(h): return (f(h)-2*f0+f(-h))/h**2
    h1,h2=1e-2,2e-2
    return (h2**2*D(h1)-h1**2*D(h2))/(h2**2-h1**2)
def hessian(func):
    H=np.zeros((12,12))
    dd=[dir2nd(func,np.eye(12)[i]) for i in range(12)]
    for i in range(12): H[i,i]=dd[i]
    for i in range(12):
        for j in range(i+1,12):
            e=np.eye(12); q=dir2nd(func,e[i]+e[j])
            H[i,j]=H[j,i]=0.5*(q-dd[i]-dd[j])
    return H

# ---- S4-isotypic projectors on R^6 via CHARACTER projectors (basis-independent,
#      correct even though rho is non-unitary) ----
complement=[i for i in range(7) if ch0[i].real<0]   # the 4 points, permuted as S4
cidx={c:k for k,c in enumerate(complement)}
def cycle_type4(M):
    p=perm(M); q=[cidx[p[c]] for c in complement]     # permutation of 0..3
    seen=[False]*4; ct=[]
    for s in range(4):
        if seen[s]: continue
        l=0; x=s
        while not seen[x]: seen[x]=True; x=q[x]; l+=1
        ct.append(l)
    return tuple(sorted(ct,reverse=True))
# S4 class of each element by cycle type on the 4 complement points
cls_of={(1,1,1,1):'e',(2,1,1):'t',(2,2):'tt',(3,1):'c3',(4,):'c4'}
# character tables (triv,sign,2,3,3'): keyed by class
CHAR={'2':{'e':2,'t':0,'tt':2,'c3':-1,'c4':0},
      '3':{'e':3,'t':1,'tt':-1,'c3':0,'c4':-1},
      "3'":{'e':3,'t':-1,'tt':-1,'c3':0,'c4':1}}
def char_proj(irr,dim):
    return sum(CHAR[irr][cls_of[cycle_type4(M)]]*rho[M] for M in S4)*dim/24
P2=char_proj('2',2); P3=char_proj('3',3); P3p=char_proj("3'",3)
r2,r3,r3p=[int(round(np.trace(P).real)) for P in (P2,P3,P3p)]
print(f"[1] character-projector ranks on R^6:  2->{r2}, 3->{r3}, 3'->{r3p}  (chi6|S4 = 1+2+3 => expect 2,3,0)")
def range_basis(P):
    u,s,vt=np.linalg.svd(P); k=int(round(np.trace(P).real)); return u[:,:k]
Bdoublet=range_basis(P2)
Btriplet=range_basis(P3 if r3>=r3p else P3p)

def block_eig(H, basisR):
    k=basisR.shape[1]
    B=np.zeros((12,2*k))
    B[:6,:k]=basisR; B[6:,k:]=basisR
    B,_=np.linalg.qr(B)
    Hs=B.T@H@B
    return np.linalg.eigvalsh(Hs)

# ============ (V) validation against Ilya's Result 3 ============
print("\n[V] VALIDATION vs Ilya Result 3 (basis g1,g2,line,mixed,prod; couplings=1; expect")
print("    doublet: 336 g1 +192 g2 + 96 line +360 mixed -2240 prod (-2 m^2)")
print("    triplet: 336 g1 +108 g2 + 96 line +416 mixed -2240 prod (-2 m^2))")
funcs_val={'g1':Ig1,'g2':Ig2,'line':Iline,'mixed':Imixed,'prod':Iprod,'mass':mass}
for nm,fn in funcs_val.items():
    H=hessian(fn)
    ed=block_eig(H,Bdoublet); et=block_eig(H,Btriplet)
    # the "real-sector" doublet/triplet eigenvalue = the repeated value
    print(f"    {nm:>6}: doublet-block eigs {np.round(ed,2)}   triplet-block eigs {np.round(et,2)}")

# ============ (C) corrected basis ============
print("\n[C] CORRECTED basis {g1,g2,line,mixed,antisym,Qmiss}. Doublet/triplet block eigenvalues:")
funcs_cor={'g1':Ig1,'g2':Ig2,'line':Iline,'mixed':Imixed,'antisym':Iantisym,'Qmiss':Qmiss,'mass':mass}
Drow={}; Trow={}
for nm,fn in funcs_cor.items():
    H=hessian(fn)
    ed=block_eig(H,Bdoublet); et=block_eig(H,Btriplet)
    Drow[nm]=ed; Trow[nm]=et
    print(f"    {nm:>8}: doublet eigs {np.round(ed,3)}    triplet eigs {np.round(et,3)}")

# ============ (D) King-Luhn's two cross channels I4 (Re), I5 (Im) at MATCHED norm ============
# Build LNR rep, intertwiner S, and the 6-6' cross map; I4=Re<6|6'>, I5=Im<6|6'>.
Ai=inv3(A_gen); Bi=inv3(B_gen); gens=[(A_gen,'A'),(Ai,'a'),(B_gen,'B'),(Bi,'b')]
word={I3:''}; frq=[I3]
while frq:
    nx=[]
    for M in frq:
        for g,s in gens:
            Mg=mm(M,g)
            if Mg not in word: word[Mg]=word[M]+s; nx.append(Mg)
    frq=nx
elts=list(word); order_of={M:order(M) for M in elts}
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
def pw(w_):
    M=np.eye(6,dtype=complex)
    for ch in w_: M=M@g6[ch]
    return M
paper={M:pw(word[M]) for M in elts}
np.random.seed(0); Xr=np.random.randn(6,6)+1j*np.random.randn(6,6)
Sint=sum(paper[M]@Xr@np.linalg.inv(fano[M]) for M in elts)/168; Sinv=np.linalg.inv(Sint)
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
chiG={6:{1:6,2:2,3:0,4:0,7:-1}}
P6=sum(np.conj(chiG[6][order_of[M]])*Aops[M] for M in elts)*6/168
np.random.seed(1); Kk=np.random.randn(21,21)+1j*np.random.randn(21,21); Kk=Kk+Kk.conj().T
Ceq=sum(Aops[M]@(P6@Kk@P6)@Aops[M].conj().T for M in elts)/168
w6,V6=np.linalg.eigh(Ceq); nz=[k for k in range(21) if abs(w6[k])>1e-6]
uq=sorted(set(np.round(w6[nz],5)))
Qa=sum(np.outer(V6[:,k],V6[:,k].conj()) for k in nz if abs(w6[k]-uq[0])<1e-4)
Qb=sum(np.outer(V6[:,k],V6[:,k].conj()) for k in nz if abs(w6[k]-uq[1])<1e-4)
X0=Qa@(np.random.randn(21,21)+1j*np.random.randn(21,21))@Qb
Xc=sum(Aops[M]@X0@Aops[M].conj().T for M in elts)/168
Xc=Xc/np.linalg.svd(Xc,compute_uv=False)[0]
def cross_J(v6):
    chi_lnr=Sint@v6; t=mat2vec(np.outer(chi_lnr,chi_lnr)); return t.conj()@Xc@t
def I4(v6): return np.sqrt(2)*np.real(cross_J(v6))   # King-Luhn Re-cross (matched norm)
def I5(v6): return np.sqrt(2)*np.imag(cross_J(v6))   # King-Luhn Im-cross (matched norm)

print(f"\n[D] King-Luhn cross channels I4=Re<6|6'>, I5=Im<6|6'> (matched normalisation).")
# I5 should be proportional to Qmiss (both the antisymmetric/chiral cross):
np.random.seed(5); tv=[np.random.randn(6)+1j*np.random.randn(6) for _ in range(20)]
r5=np.array([I5(x) for x in tv]); rq=np.array([Qmiss(x) for x in tv])
print(f"    I5 vs Qmiss proportional? corr={abs(np.dot(r5,rq))/(np.linalg.norm(r5)*np.linalg.norm(rq)):.6f}  ratio~{np.mean(r5/rq):.4f}")
for nm,fn in [('I4(Re-cross)',I4),('I5(Im-cross)',I5)]:
    H=hessian(fn); ed=block_eig(H,Bdoublet); et=block_eig(H,Btriplet)
    print(f"    {nm:>13}: doublet eigs {np.round(ed,3)}   triplet eigs {np.round(et,3)}")

# the sqrt7: compare the cross channel's contribution scale to the diagonal 6-channels.
# King-Luhn: kappa_2=kappa_3=kappa_4+kappa_5/sqrt7. Check ratio of I5 to I4 block-scales.
HI4=hessian(I4); HI5=hessian(I5)
d4=np.max(np.abs(block_eig(HI4,Bdoublet))); d5=np.max(np.abs(block_eig(HI5,Bdoublet)))
t4=np.max(np.abs(block_eig(HI4,Btriplet))); t5=np.max(np.abs(block_eig(HI5,Btriplet)))
print(f"\n[E] cross-channel block-scale ratios (looking for sqrt7={np.sqrt(7):.4f} or 1/sqrt7={1/np.sqrt(7):.4f}):")
print(f"    doublet |I4|/|I5| = {d4/d5:.4f} ,  |I5|/|I4| = {d5/d4:.4f}")
print(f"    triplet |I4|/|I5| = {t4/t5:.4f} ,  |I5|/|I4| = {t5/t4:.4f}")
print("\nDone. [free exploration; not a sealed stone]")
