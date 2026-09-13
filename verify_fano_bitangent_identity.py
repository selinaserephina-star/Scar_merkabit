# Is his chi6-model's Fano-7 (the 7 points of P^2(F2), GL(3,2) natural action)
# the same as section 11.3's "Fano points" -- a size-7 PSL(2,7)-orbit among the
# 36 EVEN quadratic refinements of the symplectic form on V(+)V* = F2^6?
import itertools
F=[0,1]
def mv(M,v): return tuple(sum(M[i][k]*v[k] for k in range(3))%2 for i in range(3))
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))
I3=((1,0,0),(0,1,0),(0,0,1))
def inv3(M):
    A=[list(M[i])+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    for c in range(3):
        p=next(r for r in range(c,3) if A[r][c]==1); A[c],A[p]=A[p],A[c]
        for r in range(3):
            if r!=c and A[r][c]==1: A[r]=[(A[r][k]+A[c][k])%2 for k in range(6)]
    return tuple(tuple(row[3:]) for row in A)
# GL(3,2)
G=[]
for cols in itertools.product(list(itertools.product(F,repeat=3)),repeat=3):
    M=tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))
    # invertible over F2?  check rows independent
    rows=[M[i] for i in range(3)]
    # gaussian rank
    basis=[]; 
    for r in rows:
        v=list(r)
        for b in basis:
            lead=next(i for i in range(3) if b[i]==1)
            if v[lead]==1: v=[(v[k]+b[k])%2 for k in range(3)]
        if any(v): basis.append(tuple(v))
    if len(basis)==3: G.append(M)
print("GL(3,2):", len(G))
def order(M):
    P=M; n=1
    while P!=I3: P=mm(P,M); n+=1
    return n
# conjugacy signature key: order (+ split 7A/7B later not needed for char equality)
pts=[v for v in itertools.product(F,repeat=3) if any(v)]   # 7 points of P^2(F2)
def fix_points(M): return sum(1 for v in pts if mv(M,v)==v)

# ---- even refinements of omega on V(+)V* = F2^6 ----
# x=(v,f), v,f in F2^3; omega(x,y)=f.w + h.v.  Split form q0(v,f)=f.v.
# refinements q = q0 + linear l, l in (F2^6)^* (64 of them). Arf invariant.
V6=list(itertools.product(F,repeat=6))
def omega(x,y):
    v,f=x[:3],x[3:]; w,h=y[:3],y[3:]
    return (sum(f[i]*w[i] for i in range(3))+sum(h[i]*v[i] for i in range(3)))%2
def q0(x):
    v,f=x[:3],x[3:]; return sum(f[i]*v[i] for i in range(3))%2
# linear functionals l_a(x)=a.x
def make_q(a): return lambda x: (q0(x)+sum(a[i]*x[i] for i in range(6)))%2
# Arf: q is even (Arf 0) iff #{x: q(x)=0} = 2^5 + 2^2 = 36 (for a 6-dim space, even -> 36 zeros)
def arf_even(q): return sum(1 for x in V6 if q(x)==0)==36
refs=[a for a in itertools.product(F,repeat=6)]
even=[a for a in refs if arf_even(make_q(a))]
print("even refinements:", len(even), " (expect 36)")
# GL(3,2) acts on V(+)V* by g.(v,f)=(g v, (g^{-1})^T f); on q by (g.q)(x)=q(g^{-1}x)
def act6(M,x):
    Mi=inv3(M); MiT=tuple(tuple(Mi[j][i] for j in range(3)) for i in range(3))
    v,f=x[:3],x[3:]
    return mv(M,v)+mv(MiT,f)
def act_ref(M,a):
    # g.q has coefficients a' with (g.q)(x)=q(g^{-1}x)= q0(g^{-1}x)+a.(g^{-1}x)
    # q0(g^{-1}x): g^{-1} preserves omega and fixes q0? q0 is the split form, GL(3,2) fixes it.
    # so g.q = q0 + (a composed with g^{-1}) -> a'(x)=a.(g^{-1}x) -> a' = (g^{-1})^T applied in F2^6
    Mi=inv3(M)
    def g6inv(x):  # apply g^{-1} on V(+)V*
        MiT=tuple(tuple(Mi[j][i] for j in range(3)) for i in range(3))
        # inverse of act6(M,.) is act6(Mi,.)
        v,f=x[:3],x[3:]; return mv(Mi,v)+mv(tuple(tuple(M[j][i] for j in range(3)) for i in range(3)),f)
    # a' defined by a'.x = a.(g^{-1} x); compute a' by images of basis
    ap=[0]*6
    for i in range(6):
        e=tuple(1 if k==i else 0 for k in range(6))
        ap[i]=sum(a[j]*g6inv(e)[j] for j in range(6))%2
    return tuple(ap)
# orbits of GL(3,2) on the 36 even refinements
evenset=set(even); seen=set(); orbits=[]
for a in even:
    if a in seen: continue
    orb=set([a]); frontier=[a]
    while frontier:
        b=frontier.pop()
        for M in G:
            c=act_ref(M,b)
            if c not in orb: orb.add(c); frontier.append(c)
    seen|=orb; orbits.append(sorted(orb))
print("orbit sizes on the 36 even refinements:", sorted(len(o) for o in orbits))
size7=[o for o in orbits if len(o)==7]
# fixed-count signature of an action, as a class function keyed by element order
def sig(fixfn):
    from collections import defaultdict
    d=defaultdict(list)
    for M in G: d[order(M)].append(fixfn(M))
    return {o:(min(v),max(v)) for o,v in d.items()}
sig_pts=sig(fix_points)
print("\npoint action (his Fano-7) fixed-count signature by order:", sig_pts)
for idx,o in enumerate(size7):
    oset=set(o)
    fixfn=lambda M,oset=oset: sum(1 for a in oset if act_ref(M,a) in oset and act_ref(M,a)==a)
    print(f"size-7 even-refinement orbit #{idx}: signature", sig(fixfn),
          " MATCHES points:", sig(fixfn)==sig_pts)
# expected perm char 1+chi6 = (7,3,1,1,0,0) on classes 1A,2A,3A,4A,7A,7B
print("\nexpected 1+chi6 fixed counts: id=7, ord2=3, ord3=1, ord4=1, ord7=0")
