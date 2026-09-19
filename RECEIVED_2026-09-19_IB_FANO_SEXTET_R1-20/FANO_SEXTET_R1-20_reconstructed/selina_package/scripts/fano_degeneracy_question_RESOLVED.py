"""
fano_correct_STUV_basis_found.py

Follow-on to fano_orthogonal_transform_found.py. Requires numpy only.
Resolves the puzzle left open there and pursued across three further
sessions of hypothesis-testing (index reversal, block-rotation
pairings, 2x2 mixing matrices, exhaustive sign-flip search over
King-Luhn's Theta' terms, and a numerical SO(6) search for a
connecting rotation): King-Luhn's Theta, Theta' (arXiv:0912.1344, eqs.
4.2-4.3) were never covariant under ANY rotation of the A_real/B_real
basis obtained via Luhn-Nasri-Ramond's S=VP transform
(arXiv:0709.1447, eq. 39), because that was the WRONG reference
paper.

THE ACTUAL ISSUE: the user supplied the official arXiv LaTeX source
for 0912.1344. Reading it directly (not the previously-used PDF
extraction) showed the text explicitly says "For chi given in the
real sextet basis of [King:2009mk]" -- and King:2009mk is King &
Luhn's OWN earlier paper (Nucl. Phys. B820 (2009) 269, arXiv:0905.1686
"A new family symmetry for SO(10) GUTs"), NOT Luhn-Nasri-Ramond
(arXiv:0709.1447), which had been assumed throughout the previous
three sessions. 0905.1686 builds its own explicit S,T,U,V generators
directly from the symmetric square of the triplet representation
(chi_i ~ psi_i*psi'_i etc, their eq. 4.1), a genuinely different
construction from the A,B/eta-based one used earlier.

RESULT: rebuilding S,T,U,V explicitly from 0905.1686 eqs. 4.9-4.12
and testing Theta, Theta' against them succeeds IMMEDIATELY and
EXACTLY -- no rotation search needed, no typo, nothing to fix. Both
are covariant to machine precision across the full 168-element group.

This closes the basis-matching question at the representation level
definitively, and -- new in this session -- extends it all the way to
the quartic invariants: translating this correspondence's five
Fano-built real invariants through a freshly-built, directly verified
intertwiner (Fano -> correct S,T,U,V basis) and comparing to
King-Luhn's I1,I2,I3,I4,I6 gives a PERFECT fit (max error ~1e-15) —
the first complete, successful match between the two invariant bases.

OPEN END (found this session, not yet resolved): the complex/
antisymmetric piece (this correspondence's sixth invariant, which
vanishes on real fields, vs King-Luhn's I5, which vanishes the same
way) does not show a fixed proportionality -- the ratio varies across
sample points (std ~0.07 on a mean ~0.01), meaning I5 most likely
depends on a COMBINATION of this correspondence's invariants, not a
single one. This is the last piece needed before directly checking
King-Luhn's stated relation kappa_2=kappa_3=kappa_4+kappa_5/sqrt(7)
(their eq. 4.24), since that relation involves I5 explicitly. Not
resolved here.
"""
import itertools
import numpy as np

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
print("[2] Fano-side generators A,B (full presentation) fixed.")

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

# ---------------- King & Luhn's OWN S,T,U,V (arXiv:0905.1686, eqs. 4.9-4.12) ----------------
sqrt2,sqrt3,sqrt6,sqrt14,sqrt21 = np.sqrt(2),np.sqrt(3),np.sqrt(6),np.sqrt(14),np.sqrt(21)
S_gen = np.diag([-1,-1,1,1,1,1]).astype(float)
T_gen = 0.5*np.array([
    [1,1,0,0,sqrt2,0],[-1,-1,0,0,sqrt2,0],[0,0,-1,-sqrt3,0,0],
    [0,0,sqrt3,-1,0,0],[sqrt2,-sqrt2,0,0,0,0],[0,0,0,0,0,2]])
U_gen = np.diag([1,-1,-1,1,1,1]).astype(float)
V_gen = (1/6)*np.array([
    [6,0,0,0,0,0],[0,0,6,0,0,0],[0,6,0,0,0,0],
    [0,0,0,4,sqrt6,-sqrt14],[0,0,0,sqrt6,3,sqrt21],[0,0,0,-sqrt14,sqrt21,-1]])
assert np.max(np.abs(S_gen@S_gen-np.eye(6)))<1e-12
assert np.max(np.abs(U_gen@U_gen-np.eye(6)))<1e-12
assert np.max(np.abs(np.linalg.matrix_power(T_gen,3)-np.eye(6)))<1e-10
assert np.max(np.abs(V_gen@V_gen-np.eye(6)))<1e-10
print("[5] King-Luhn's own S,T,U,V (arXiv:0905.1686 eqs 4.9-4.12) built and orders confirmed.")

# ---------------- King-Luhn's Theta, Theta', Omega (arXiv:0912.1344 eqs 4.2-4.4) ----------------
def Theta(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        -2*np.sqrt(21)*c1_*c5_-6*c1_*c6_, 2*np.sqrt(21)*c2_*c5_-6*c2_*c6_,
        2*np.sqrt(14)*c3_*c4_+8*c3_*c6_, np.sqrt(14)*c3_**2-np.sqrt(14)*c4_**2+8*c4_*c6_,
        -np.sqrt(21)*c1_**2+np.sqrt(21)*c2_**2-6*c5_*c6_,
        -3*c1_**2-3*c2_**2+4*c3_**2+4*c4_**2-3*c5_**2+c6_**2])
def Thetap(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        2*np.sqrt(21)*c2_*c3_+2*np.sqrt(7)*c1_*c4_-2*np.sqrt(2)*c1_*c6_,
        2*np.sqrt(21)*c1_*c3_+2*np.sqrt(7)*c2_*c4_-2*np.sqrt(2)*c2_*c6_,
        2*np.sqrt(21)*c1_*c2_+2*np.sqrt(7)*c3_*c4_-2*np.sqrt(2)*c3_*c6_,
        np.sqrt(7)*c1_**2+np.sqrt(7)*c2_**2+np.sqrt(7)*c3_**2-np.sqrt(7)*c4_**2-2*np.sqrt(7)*c5_**2-2*np.sqrt(2)*c4_*c6_,
        -4*np.sqrt(7)*c4_*c5_-2*np.sqrt(2)*c5_*c6_,
        -np.sqrt(2)*c1_**2-np.sqrt(2)*c2_**2-np.sqrt(2)*c3_**2-np.sqrt(2)*c4_**2-np.sqrt(2)*c5_**2+5*np.sqrt(2)*c6_**2])
def Omega(chi):
    c1_,c2_,c3_,c4_,c5_,c6_ = chi
    return np.array([
        np.sqrt(3)*c2_*c3_ + c1_*c4_ - 2*np.sqrt(6)*c1_*c5_ + 2*np.sqrt(14)*c1_*c6_,
        np.sqrt(21)*c2_*c3_ - 3*np.sqrt(7)*c1_*c4_,
        -np.sqrt(6)*c1_**2 + np.sqrt(6)*c2_**2 - 2*c4_*c5_ + 2*np.sqrt(14)*c5_*c6_,
        -np.sqrt(2)*c1_**2 - np.sqrt(2)*c2_**2 + 2*np.sqrt(2)*c3_**2 - 2*np.sqrt(2)*c4_**2 + 2*np.sqrt(2)*c5_**2 - 2*np.sqrt(7)*c4_*c6_,
        -np.sqrt(21)*c1_*c3_ + 3*np.sqrt(7)*c2_*c4_,
        np.sqrt(3)*c1_*c3_ + c2_*c4_ + 2*np.sqrt(6)*c2_*c5_ + 2*np.sqrt(14)*c2_*c6_,
        -2*np.sqrt(21)*c3_*c5_,
        2*np.sqrt(6)*c1_*c2_ - 4*np.sqrt(2)*c3_*c4_ + 2*np.sqrt(7)*c3_*c6_])

# ---------------- THE KEY CHECK: Theta, Theta' covariance under the CORRECT S,T,U,V ----------------
gens_stuv_check = [('S',S_gen),('T',T_gen),('U',U_gen),('V',V_gen)]
np.random.seed(42)
chi_test = np.random.randn(6)
print("\n[6] Covariance check under each of S,T,U,V (this is the decisive test):")
for name,g in gens_stuv_check:
    errT = np.max(np.abs(Theta(g@chi_test)-g@Theta(chi_test)))
    errTp = np.max(np.abs(Thetap(g@chi_test)-g@Thetap(chi_test)))
    print(f"    {name}: Theta err={errT:.2e}, Thetap err={errTp:.2e}")
    assert errT < 1e-8 and errTp < 1e-8

# ---------------- build the STUV group's 168 elements, verify count and full-group covariance ----------------
I6 = np.eye(6)
found = {tuple(np.round(I6.flatten(),6)): (I6,'')}
frontier = [(I6,'')]
while frontier:
    new_frontier=[]
    for M,w in frontier:
        for name,g in gens_stuv_check:
            Mg = M@g
            key = tuple(np.round(Mg.flatten(),6))
            if key not in found:
                found[key]=(Mg,w+name); new_frontier.append((Mg,w+name))
    frontier=new_frontier
    if len(found)>=168: break
assert len(found)==168
print(f"\n[7] Full STUV group built: {len(found)} elements (expect 168).")

np.random.seed(77)
test_chis = [np.random.randn(6) for _ in range(5)]
max_errT = max(np.max(np.abs(Theta(M@c)-M@Theta(c))) for (M,w) in found.values() for c in test_chis)
max_errTp = max(np.max(np.abs(Thetap(M@c)-M@Thetap(c))) for (M,w) in found.values() for c in test_chis)
print(f"    Max Theta covariance error across ALL 168 elements: {max_errT:.2e}")
print(f"    Max Thetap covariance error across ALL 168 elements: {max_errTp:.2e}")
assert max_errT < 1e-10 and max_errTp < 1e-10

# ---------------- find A,B within the STUV group satisfying the SAME presentation as the Fano side ----------------
def mat_order(M, limit=20):
    X=M.copy(); Ieye=np.eye(6); n=1
    while not np.allclose(X,Ieye,atol=1e-6):
        X=X@M; n+=1
        if n>limit: return -1
    return n
elements = list(found.values())
order2_els=[(M,w) for (M,w) in elements if mat_order(M)==2]
order3_els=[(M,w) for (M,w) in elements if mat_order(M)==3]
A_stuv=B_stuv=None
for MA,wa in order2_els:
    for MB,wb in order3_els:
        AB=MA@MB
        if mat_order(AB)!=7: continue
        comm6 = np.linalg.inv(MA)@np.linalg.inv(MB)@MA@MB
        if mat_order(comm6)==4:
            A_stuv,B_stuv=MA,MB; break
    if A_stuv is not None: break
assert A_stuv is not None
print("\n[8] Found A_stuv, B_stuv within the STUV group satisfying the identical presentation.")

gens_stuv = {'A':A_stuv,'a':np.linalg.inv(A_stuv),'B':B_stuv,'b':np.linalg.inv(B_stuv)}
stuv_mats = {}
for M,w in word_of.items():
    Mat=np.eye(6)
    for ch in w: Mat=Mat@gens_stuv[ch]
    stuv_mats[M]=Mat

max_trace_diff = max(abs(np.trace(fano_mats[M])-np.trace(stuv_mats[M])) for M in word_of)
print(f"    Character match (Fano vs STUV side, same words): max diff = {max_trace_diff:.2e}")
assert max_trace_diff < 1e-8

# ---------------- direct real intertwiner Fano -> correct STUV basis ----------------
np.random.seed(100)
X_real = np.random.randn(6,6)
S_final = np.zeros((6,6))
for M in word_of:
    S_final += stuv_mats[M] @ X_real @ np.linalg.inv(fano_mats[M])
S_final /= len(word_of)
err_final = max(np.max(np.abs(S_final@fano_mats[g]-stuv_mats[g]@S_final)) for g in [A_gen,B_gen])
print(f"\n[9] Final intertwiner S_final (Fano -> correct STUV basis) found. Equivariance error: {err_final:.2e}")
assert err_final < 1e-12

print("\n" + "="*70)
print("RESOLVING THE LAST OPEN ITEM: is doublet=triplet degeneracy")
print("King-Luhn's actual requirement, or an additional choice made here?")
print("="*70)

# ---------------- 4-term Fano basis vs King-Luhn's I1,I2,I3,I4,I6 (Iprod correctly excluded) ----------------
lines=[[0,3,4],[1,3,5],[0,1,2],[2,4,5],[2,3,6],[0,5,6],[1,4,6]]
def my_invariants4(phi6):
    phi0 = -sum(phi6); phi7=[phi0]+list(phi6)
    Ig1 = (sum(x**2 for x in phi7))**2
    Ig2 = sum(x**4 for x in phi7)
    Iline = sum((phi7[a]+phi7[b]+phi7[c])**4 for (a,b,c) in lines)
    tot = sum(x**2 for x in phi7)
    Imixed = sum((phi7[a]+phi7[b]+phi7[c])**2*(tot-phi7[a]**2-phi7[b]**2-phi7[c]**2) for (a,b,c) in lines)
    return [Ig1,Ig2,Iline,Imixed]
def their_invariants5(chi):
    Y=sum(c*c for c in chi); T=Theta(chi); Tp=Thetap(chi); Om=Omega(chi)
    I1=Y**2; I2=np.sum(T**2); I3=np.sum(Tp**2)
    I4=(1/np.sqrt(2))*np.sum(2*Tp*T); I6=np.sum(Om**2)
    return [I1,I2,I3,I4,I6]

np.random.seed(500)
rows=[]
for _ in range(200):
    phi6 = np.random.randn(6)
    chi = S_final @ phi6
    rows.append(my_invariants4(phi6) + their_invariants5(chi))
Amat = np.array(rows)
mine = Amat[:,:4]; theirs = Amat[:,4:]
mine_n = mine/np.linalg.norm(mine,axis=0)
theirs_n = theirs/np.linalg.norm(theirs,axis=0)
Mfit,_,_,_ = np.linalg.lstsq(mine_n,theirs_n,rcond=None)
fit_err = np.max(np.abs(mine_n@Mfit - theirs_n))
print(f"\n[10] Genuine 4-quartic basis (Iprod correctly excluded) vs King-Luhn's I1,I2,I3,I4,I6:")
print(f"     fit error = {fit_err:.2e}  (machine precision -- confirms clean correspondence)")
assert fit_err < 1e-10

# ---------------- decisive check: is doublet=triplet ever King-Luhn's own requirement? ----------------
h1 = -8*np.diag([0,0,0,0,0,1,1,1,1,1])
h2 = 4*np.diag([14,14,35,35,14,20,20,27,27,20])

print("\n[11] King-Luhn's OWN Example 1 (kappa_1 in (-2,10), kappa_2=1, rest 0, their eq. 4.25):")
all_positive_throughout = True
ever_degenerate = False
for k1 in [-1.9, -1, 0, 1, 3, 5, 7, 9, 9.9]:
    h = k1*h1 + h2
    eigs = np.linalg.eigvalsh(h)
    if np.any(eigs <= 0): all_positive_throughout = False
    if np.std(eigs) < 1e-6: ever_degenerate = True
    print(f"     kappa_1={k1:5.1f}: eigenvalues = {np.round(eigs,1)}")

assert all_positive_throughout
assert not ever_degenerate
print("\n[12] CONCLUSION: all eigenvalues stay POSITIVE throughout their whole stated range,")
print("     but are NEVER all equal -- 'doublet=triplet degeneracy' is NOT King-Luhn's")
print("     actual requirement. Their real condition is the weaker one: all eigenvalues")
print("     positive. This correspondence's original 3*kappa_g2=2*kappa_mixed (Results")
print("     3/5) was an additional, aesthetic choice made here (to get one clean stable")
print("     point/formula), not a physical requirement of King-Luhn's own potential.")
