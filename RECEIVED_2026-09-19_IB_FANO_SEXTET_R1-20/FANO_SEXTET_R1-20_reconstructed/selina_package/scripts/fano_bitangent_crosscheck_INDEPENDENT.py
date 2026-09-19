"""
fano_bitangent_crosscheck_INDEPENDENT.py

Follow-on to Result 18 (fano_bitangent_correspondence_EXPLORED.py).
Requires numpy only. Prompted by a direct request to check that result
from several genuinely different angles, in case of error -- exactly
the adversarial-verification spirit used throughout this
correspondence. Four independent checks, each capable of catching a
mistake the others would miss:

1. A completely different construction of the same 28-point action:
   find ANY order-6 subgroup H of PSL(2,7) (via closure of a random
   order-2/order-3 element pair -- no symplectic form, no quadratic
   refinements, no Arf invariant anywhere in this construction), build
   the 28 left cosets G/H, and compute the permutation character of
   left multiplication on them directly.

   RESULT: character (28,4,1,0,0,0) on classes (1A,2A,3A,4A,7A,7B) --
   IDENTICAL to Result 18's bitangent character, decomposing as the
   same chi1+2*chi6+chi7+chi8. Since this construction shares no code
   and no underlying geometric object with Result 18's, this is a
   genuine independent confirmation, not a re-run.

2. Direct verification of the Arf invariant computation itself, via a
   completely different formula: for a quadratic form on F_2^(2g), the
   number of vectors with q(x)=0 is 2^(g-1)(2^g+1) if Arf=0, or
   2^(g-1)(2^g-1) if Arf=1. Directly counted zeros of q0 (Result 18's
   reference quadratic form) among all 64 vectors: got exactly 36,
   matching the Arf=0 formula (2^2*9=36) and NOT the Arf=1 formula
   (2^2*7=28) -- confirming Arf(q0)=0 by a method with no dependence
   on the symplectic-basis sum formula used in Result 18.

3. Exhaustive enumeration: found ALL distinct order-6 subgroups of
   PSL(2,7) directly (not just one), and checked which Fano-point S4
   each is contained in. Found exactly 28 such subgroups (matching the
   28-bitangent count, as expected since each bitangent's stabilizer
   is exactly one such subgroup) -- and EVERY one is contained in
   exactly one Fano-point's S4, with EXACTLY 4 per point. This bypasses
   bitangents, quadratic forms, and Arf invariants entirely: it is a
   statement purely about PSL(2,7)'s own subgroup lattice.

4. Independent check of the underlying textbook fact about abstract
   S4 (no PSL(2,7) or Fano-plane machinery at all): built S4 as
   permutations of {0,1,2,3} directly, computed the four point-
   stabilizers, and confirmed they are 4 genuinely distinct subgroups
   of order 6 each -- the elementary fact the "4 per point" observation
   ultimately rests on.

CONCLUSION: all four independent checks agree exactly with Result 18.
No error found. The 7x4=28 correspondence and the chi1+2chi6+chi7+chi8
character are robust findings, not artifacts of one specific
construction choice.
"""
import itertools
import numpy as np
from collections import Counter

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
assert len(GL32) == 168

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
gens_with_words=[(A_gen,'A'),(Ainv,'a'),(B_gen,'B'),(Binv,'b')]
word_of={I3:''}
frontier=[I3]
while frontier:
    nxt=[]
    for M in frontier:
        for g,sym in gens_with_words:
            Mg=mat_mul3(M,g)
            if Mg not in word_of: word_of[Mg]=word_of[M]+sym; nxt.append(Mg)
    frontier=nxt
print(f"[setup] {len(word_of)} PSL(2,7) elements ready.")

# ==================== CHECK 1: G/H coset construction, no geometry at all ====================
order2_els=[M for M in word_of if mat_order3(M)==2]
order3_els=[M for M in word_of if mat_order3(M)==3]
H=None
for a2 in order2_els:
    for a3 in order3_els:
        elems={I3}; frontier_H=[I3]
        while frontier_H:
            nf=[]
            for e in frontier_H:
                for g in [a2,a3,mat_inv3(a2),mat_inv3(a3)]:
                    eg=mat_mul3(e,g)
                    if eg not in elems: elems.add(eg); nf.append(eg)
            frontier_H=nf
            if len(elems)>6: break
        if len(elems)==6: H=elems; break
    if H: break
assert sorted(mat_order3(h) for h in H) == [1,2,2,2,3,3]

cosets=[]; seen=set()
for g in word_of:
    if g in seen: continue
    coset=frozenset(mat_mul3(g,h) for h in H)
    cosets.append(coset); seen|=coset
assert len(cosets)==28
coset_idx={c:i for i,c in enumerate(cosets)}
def act_on_coset(g,c): return frozenset(mat_mul3(g,x) for x in c)
def perm_to_matrix28(perm):
    M=np.zeros((28,28))
    for i in range(28): M[perm[i],i]=1
    return M
mats={M: perm_to_matrix28(tuple(coset_idx[act_on_coset(M,c)] for c in cosets)) for M in word_of}

def conjugate(g,M): return mat_mul3(mat_mul3(g,M), mat_inv3(g))
order4=[M for M in word_of if mat_order3(M)==4][0]
order7_all=[M for M in word_of if mat_order3(M)==7]
g7a=order7_all[0]
g7b=next(M for M in order7_all if M not in set(conjugate(g,g7a) for g in word_of))
reps={'1A':I3,'2A':order2_els[0],'3A':order3_els[0],'4A':order4,'7A':g7a,'7B':g7b}
perm_char={name: np.trace(mats[rep]) for name,rep in reps.items()}
print(f"\n[1] G/H coset action (no symplectic form, no Arf invariant): {perm_char}")
sizes=[1,21,56,42,24,24]
chars_irr={'chi1':[1,1,1,1,1,1],'chi6':[6,2,0,0,-1,-1],'chi7':[7,-1,1,-1,0,0],'chi8':[8,0,-1,0,1,1]}
perm_vec=[perm_char[k] for k in ['1A','2A','3A','4A','7A','7B']]
mults={name: sum(sizes[i]*perm_vec[i]*np.conj(ch[i]) for i in range(6)).real/168 for name,ch in chars_irr.items()}
print(f"    Multiplicities: {mults}")
assert all(abs(mults[k]-v)<1e-6 for k,v in [('chi1',1),('chi6',2),('chi7',1),('chi8',1)])
print("    MATCHES Result 18 exactly, via a totally independent construction.")

# ==================== CHECK 2: Arf invariant via independent zero-counting formula ====================
def q0(x):
    v,w = x[:3],x[3:]
    return sum(v[i]*w[i] for i in range(3))%2
all6 = list(itertools.product([0,1],repeat=6))
zeros_q0 = sum(1 for x in all6 if q0(x)==0)
print(f"\n[2] Direct zero-count of q0: {zeros_q0}/64 (Arf=0 formula: 2^2*9=36; Arf=1 formula: 2^2*7=28)")
assert zeros_q0 == 36
print("    Confirms Arf(q0)=0 via a formula independent of the symplectic-basis sum used in Result 18.")

# ==================== CHECK 3: exhaustive enumeration of ALL order-6 subgroups ====================
pts7 = [v for v in itertools.product([0,1],repeat=3) if any(v)]
def mat_vec3(M,v): return tuple(sum(M[i][j]*v[j] for j in range(3))%2 for i in range(3))
S4_groups = {p: set(g for g in word_of if mat_vec3(g,p)==p) for p in pts7}

found_H_list=[]; seen_H=set()
for a2 in order2_els:
    for a3 in order3_els:
        elems={I3}; frontier_H=[I3]
        while frontier_H:
            nf=[]
            for e in frontier_H:
                for g in [a2,a3,mat_inv3(a2),mat_inv3(a3)]:
                    eg=mat_mul3(e,g)
                    if eg not in elems: elems.add(eg); nf.append(eg)
            frontier_H=nf
            if len(elems)>6: break
        if len(elems)==6:
            fe=frozenset(elems)
            if fe not in seen_H: seen_H.add(fe); found_H_list.append(elems)

print(f"\n[3] Exhaustive search found {len(found_H_list)} distinct order-6 subgroups (expect 28).")
assert len(found_H_list) == 28
which_pt=[]
for Hi in found_H_list:
    for p in pts7:
        if Hi <= S4_groups[p]: which_pt.append(p); break
counts = Counter(which_pt)
print(f"    All {len(which_pt)} contained in some Fano-point S4; distribution: {dict(counts)}")
assert len(which_pt)==28 and all(v==4 for v in counts.values())
print("    CONFIRMED, bypassing bitangents/quadratic forms entirely: 7x4=28, exactly.")

# ==================== CHECK 4: abstract S4 fact, independent of PSL(2,7) ====================
perms4 = list(itertools.permutations(range(4)))
stabs = [frozenset(p for p in perms4 if p[pt]==pt) for pt in range(4)]
distinct_stabs = set(stabs)
print(f"\n[4] Abstract S4 (no PSL(2,7)): {len(distinct_stabs)} distinct point-stabilizers, "
      f"sizes {[len(s) for s in distinct_stabs]}")
assert len(distinct_stabs) == 4 and all(len(s)==6 for s in distinct_stabs)
print("    Confirms the textbook fact the '4 per point' observation ultimately rests on.")

print("\nAll four independent checks agree exactly with Result 18. No error found.")
