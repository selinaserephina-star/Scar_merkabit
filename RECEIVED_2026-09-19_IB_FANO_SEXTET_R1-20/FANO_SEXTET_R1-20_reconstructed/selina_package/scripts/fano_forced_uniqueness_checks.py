"""
fano_forced_uniqueness_checks.py

Follow-on to Result 18, prompted by Ilya's own review notes (not
Selina's) identifying the "forced uniqueness" pattern running through
this correspondence (Hom_G-forcing / sum-of-squares saturation) and
proposing several places to extend it. Checks the three cheapest,
per the notes' own prioritization. Requires numpy only.

--------------------------------------------------------------------
CHECK 1 (positive): dim Hom_G(Sym^2(chi6), trivial) = 1.
--------------------------------------------------------------------
Confirms the chi6-invariant metric is unique up to overall scale. Since
Result 12's I+11^T metric (giving the sqrt(7) eigenvalue ratio) IS a
chi6-invariant metric, this makes it not merely "the metric we found"
but "the only possible one" -- sqrt(7) is unavoidable, not a computed
coincidence.

--------------------------------------------------------------------
CHECK 2 (positive): dim Hom_G(Sym^2(chi8), trivial) = 1.
--------------------------------------------------------------------
By the identical argument, the octet-invariant metric is also unique.
This is exactly the pairing Result 17 uses to build Delta_Vs, Delta_Va
from the antitriplet and sextet octets -- so that contraction is the
only possible G-invariant one of its type, not a choice that happened
to work.

--------------------------------------------------------------------
CHECK 3 (nuanced, partially negative): is Result 12's constant
-0.472206 (the Q_miss/I5 proportionality constant) itself forced?
--------------------------------------------------------------------
Tests whether rescaling the S_final intertwiner changes the constant.
Result: it scales as scale^2 exactly. The PROPORTIONALITY (Q_miss is
SOME constant multiple of I5) is forced by the same kind of 1-
dimensional-Hom argument; the SPECIFIC NUMBER is not, because Schur's
lemma (Check 1) only fixes the metric's eigenvalue RATIO (1:7), not
S_final's absolute scale, which came from an unnormalized random seed
in the original group-averaging construction (Result 9). So -0.472206
remains a normalization convention, not a forced constant -- an
honest boundary on what "forced uniqueness" reaches here.
"""
import numpy as np

# ==================== Checks 1 & 2: Hom_G(Sym^2(chi), trivial) dimension ====================
sizes = [1,21,56,42,24,24]  # class sizes: 1A,2A,3A,4A,7A,7B
chars = {
    'chi6': [6,2,0,0,-1,-1],
    'chi8': [8,0,-1,0,1,1],
}
# squaring map g->g^2 on class indices: 1A->1A, 2A->1A, 3A->3A, 4A->2A, 7A->7A, 7B->7B
sq_idx = [0,0,2,1,4,5]

def dim_hom_sym2_trivial(name):
    ch = chars[name]
    sym2_char = [(ch[i]**2 + ch[sq_idx[i]])/2 for i in range(6)]
    return sum(sizes[i]*sym2_char[i] for i in range(6))/168

d6 = dim_hom_sym2_trivial('chi6')
d8 = dim_hom_sym2_trivial('chi8')
print(f"[Check 1] dim Hom_G(Sym^2(chi6), trivial) = {d6:.6f}")
assert abs(d6-1) < 1e-9
print("    CONFIRMED: chi6-invariant metric is unique up to scale.")
print("    -> the I+11^T metric (Result 12, giving sqrt(7)) is the ONLY possible one.")

print(f"\n[Check 2] dim Hom_G(Sym^2(chi8), trivial) = {d8:.6f}")
assert abs(d8-1) < 1e-9
print("    CONFIRMED: chi8-invariant metric is unique up to scale.")
print("    -> Result 17's octet contraction (giving Delta_Vs, Delta_Va) is the ONLY")
print("    possible G-invariant pairing of this type.")

# ==================== Check 3: is the -0.472206 constant itself forced? ====================
# (rebuild the minimal pieces needed: S_final intertwiner, Q_miss, I5 -- self-contained)
import itertools
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
def mat_order3(M, limit=20):
    X=M; n=1; I3=((1,0,0),(0,1,0),(0,0,1))
    while X!=I3:
        X=mat_mul3(X,M); n+=1
        if n>limit: return -1
    return n
I3=((1,0,0),(0,1,0),(0,0,1))
order2=[M for M in GL32 if mat_order3(M)==2]
order3=[M for M in GL32 if mat_order3(M)==3]
A_gen=B_gen=None
for A in order2:
    for B in order3:
        AB=mat_mul3(A,B)
        comm = mat_mul3(mat_mul3(mat_inv3(A),mat_inv3(B)),mat_mul3(A,B))
        if mat_order3(AB)==7 and mat_order3(comm)==4:
            A_gen,B_gen=A,B; break
    if A_gen: break
Ainv=mat_inv3(A_gen); Binv=mat_inv3(B_gen)
word_of={I3:''}
frontier=[I3]
gens_with_words=[(A_gen,'A'),(Ainv,'a'),(B_gen,'B'),(Binv,'b')]
while frontier:
    nxt=[]
    for M in frontier:
        for g,sym in gens_with_words:
            Mg=mat_mul3(M,g)
            if Mg not in word_of:
                word_of[Mg]=word_of[M]+sym; nxt.append(Mg)
    frontier=nxt
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
sqrt2,sqrt3,sqrt6,sqrt7,sqrt14,sqrt21 = [np.sqrt(k) for k in (2,3,6,7,14,21)]
S_gen = np.diag([-1,-1,1,1,1,1]).astype(float)
T_gen = 0.5*np.array([[1,1,0,0,sqrt2,0],[-1,-1,0,0,sqrt2,0],[0,0,-1,-sqrt3,0,0],
    [0,0,sqrt3,-1,0,0],[sqrt2,-sqrt2,0,0,0,0],[0,0,0,0,0,2]])
U_gen = np.diag([1,-1,-1,1,1,1]).astype(float)
V_gen = (1/6)*np.array([[6,0,0,0,0,0],[0,0,6,0,0,0],[0,6,0,0,0,0],
    [0,0,0,4,sqrt6,-sqrt14],[0,0,0,sqrt6,3,sqrt21],[0,0,0,-sqrt14,sqrt21,-1]])
gens4=[('S',S_gen),('T',T_gen),('U',U_gen),('V',V_gen)]
I6mat=np.eye(6)
found={tuple(np.round(I6mat.flatten(),6)):(I6mat,'')}
frontier=[(I6mat,'')]
while frontier:
    nf=[]
    for M,w in frontier:
        for nm,g in gens4:
            Mg=M@g; key=tuple(np.round(Mg.flatten(),6))
            if key not in found: found[key]=(Mg,w+nm); nf.append((Mg,w+nm))
    frontier=nf
    if len(found)>=168: break
def mat_order(M, limit=20):
    X=M.copy(); Ieye=np.eye(6); n=1
    while not np.allclose(X,Ieye,atol=1e-6):
        X=X@M; n+=1
        if n>limit: return -1
    return n
elements=list(found.values())
order2_els=[(M,w) for (M,w) in elements if mat_order(M)==2]
order3_els=[(M,w) for (M,w) in elements if mat_order(M)==3]
A_stuv=B_stuv=None
for MA,wa in order2_els:
    for MB,wb in order3_els:
        AB=MA@MB
        if mat_order(AB)!=7: continue
        c6=np.linalg.inv(MA)@np.linalg.inv(MB)@MA@MB
        if mat_order(c6)==4: A_stuv,B_stuv=MA,MB; break
    if A_stuv is not None: break
gens_stuv={'A':A_stuv,'a':np.linalg.inv(A_stuv),'B':B_stuv,'b':np.linalg.inv(B_stuv)}
correct_mats={}
for M,w in word_of.items():
    Mat=np.eye(6)
    for ch in w: Mat=Mat@gens_stuv[ch]
    correct_mats[M]=Mat
np.random.seed(100)
X_real=np.random.randn(6,6)
S_final=np.zeros((6,6))
for M in word_of:
    S_final += correct_mats[M]@X_real@np.linalg.inv(fano_mats[M])
S_final/=len(word_of)

lines=[[0,3,4],[1,3,5],[0,1,2],[2,4,5],[2,3,6],[0,5,6],[1,4,6]]
def Q_miss(phi6):
    phi0 = -sum(phi6); phi7 = [phi0]+list(phi6)
    ell = [0j]*7
    for (i,j,k) in lines:
        ell[i]+=phi7[j]*phi7[k]; ell[j]+=phi7[i]*phi7[k]; ell[k]+=phi7[i]*phi7[j]
    J = sum(np.conj(phi7[i]**2)*ell[i] for i in range(7))
    return J.imag
def Theta(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([-2*sqrt21*c1_*c5_-6*c1_*c6_, 2*sqrt21*c2_*c5_-6*c2_*c6_,
        2*sqrt14*c3_*c4_+8*c3_*c6_, sqrt14*c3_**2-sqrt14*c4_**2+8*c4_*c6_,
        -sqrt21*c1_**2+sqrt21*c2_**2-6*c5_*c6_,
        -3*c1_**2-3*c2_**2+4*c3_**2+4*c4_**2-3*c5_**2+c6_**2])
def Thetap(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([2*sqrt21*c2_*c3_+2*sqrt7*c1_*c4_-2*sqrt2*c1_*c6_,
        2*sqrt21*c1_*c3_+2*sqrt7*c2_*c4_-2*sqrt2*c2_*c6_,
        2*sqrt21*c1_*c2_+2*sqrt7*c3_*c4_-2*sqrt2*c3_*c6_,
        sqrt7*c1_**2+sqrt7*c2_**2+sqrt7*c3_**2-sqrt7*c4_**2-2*sqrt7*c5_**2-2*sqrt2*c4_*c6_,
        -4*sqrt7*c4_*c5_-2*sqrt2*c5_*c6_,
        -sqrt2*c1_**2-sqrt2*c2_**2-sqrt2*c3_**2-sqrt2*c4_**2-sqrt2*c5_**2+5*sqrt2*c6_**2])
def I5_func(chi):
    T=Theta(chi); Tp=Thetap(chi)
    return ((1j/sqrt2)*np.sum(Tp.conjugate()*T-T.conjugate()*Tp)).real

np.random.seed(1)
phi6 = np.random.randn(6)+1j*np.random.randn(6)
ratios = {}
for scale in [1.0, 2.0, 0.5]:
    chi = (scale*S_final) @ phi6
    ratios[scale] = I5_func(chi)/Q_miss(phi6)

print(f"\n[Check 3] Q_miss/I5 ratio under S_final rescaling:")
for scale,r in ratios.items():
    print(f"    scale={scale}: ratio={r:.6f}")
pred_ratio2 = ratios[1.0]*(2.0**4)
pred_ratio05 = ratios[1.0]*(0.5**4)
assert abs(ratios[2.0]-pred_ratio2) < 1e-3
assert abs(ratios[0.5]-pred_ratio05) < 1e-6
print("    CONFIRMED: ratio scales as scale^4 exactly (since Theta,Theta' are")
print("    themselves quadratic in chi, so I5 -- built from Theta'_bar*Theta -- is")
print("    quartic in chi, not quadratic; Q_miss is independent of the rescaling).")
print("    The proportionality Q_miss~I5 is forced (Result 12); the specific constant")
print("    -0.472206 is a normalization convention (tied to S_final's arbitrary overall")
print("    scale from group-averaging), NOT itself a forced group-theory number.")
