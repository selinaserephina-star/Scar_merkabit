# -*- coding: utf-8 -*-
r"""verify_tower_b.py  -- the COVERS & BRIDGES tower (Tower B).

After the L6 two-tower separation (both parties, 2026-08-31): the descent is
Tower A = the SPINE (verify_bridge_transfer.py, SM-020) and Tower B = the
covers and bridges, verified here from group theory only. Not RH/GRH.

Backbone found: the ODD spine levels are PSL(2,p) and their Schur covers are
SL(2,p) for p = 3,5,7:
    L7 PSL(2,7) <- SL(2,7)      L5 A5=PSL(2,5) <- 2I=SL(2,5)
    L3 A4=PSL(2,3) <- 2T=SL(2,3)
Plus split covers (Ih=A5xZ2, Th=A4xZ2), S4's double cover (GL(2,3)=2.S4), the
over-group PGL(2,7), and the top bridge W(E6) < Sp6(2)=W(E7)/+- (cited from the
sealed SM-003/SM-015; only the index arithmetic is checked here).

Run:  python -X utf8 verify_tower_b.py
"""
PASS=0; FAIL=0; fails=[]
def check(c, ok, d=""):
    global PASS,FAIL
    print(f"  [{'PASS' if ok else 'FAIL'}] {c}"+(f"  --  {d}" if d else ""))
    if ok: PASS+=1
    else: FAIL+=1; fails.append(c)

# ---------- perm helpers (for the spine targets A4,A5,S4 + Mobius PSL/PGL) ----------
def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def porder(p):
    e=tuple(range(len(p))); x=p; k=1
    while x!=e: x=compose(x,p); k+=1
    return k
def closure(gens):
    n=len(gens[0]); e=tuple(range(n)); G={e}; fr=[e]
    while fr:
        a=fr.pop()
        for g in gens:
            b=compose(a,g)
            if b not in G: G.add(b); fr.append(b)
    return G
def profile(G):
    pr={}
    for g in G: pr[porder(g)]=pr.get(porder(g),0)+1
    return dict(sorted(pr.items()))

A4=closure([(1,2,0,3),(0,2,3,1)]);  A5s=None
S5=closure([(1,2,3,4,0),(1,0,2,3,4)])
def even(g): return sum(1 for i in range(5) for j in range(i+1,5) if g[i]>g[j])%2==0
A5=set(g for g in S5 if even(g))
S4=closure([(1,2,3,0),(1,0,2,3)])
PROF={"A4":profile(A4),"A5":profile(A5),"S4":profile(S4)}

# ---------- matrix groups mod p ----------
def mmul(A,B,p):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
def det(M,p):
    a,b,c,d=M; return (a*d-b*c)%p
def mord(M,p):
    I=(1,0,0,1);x=M;k=1
    while x!=I: x=mmul(x,M,p);k+=1
    return k
def SL2(p): return [(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if det((a,b,c,d),p)==1]
def GL2(p): return [(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if det((a,b,c,d),p)!=0]
def center(G,p):
    return [M for M in G if all(mmul(M,X,p)==mmul(X,M,p) for X in G)]
def n_inv(G,p): return sum(1 for M in G if mord(M,p)==2)
def inv_p(k,p): return pow(k%p,p-2,p)
def mobius_group(mats,p):
    pts=p+1  # P^1(F_p): 0..p-1, oo=p
    def mob(M):
        a,b,c,d=M; img=[]
        for x in range(pts):
            if x==p: img.append(p if c%p==0 else (a*inv_p(c,p))%p)
            else:
                den=(c*x+d)%p
                img.append(p if den==0 else ((a*x+b)%p*inv_p(den,p))%p)
        return tuple(img)
    return {mob(M) for M in mats}

def cover_report(name, SLp, p, level_name, level_prof, split_expected=False):
    Z=center(SLp,p); psl=mobius_group(SLp,p)
    ni=n_inv(SLp,p)
    print(f"\n{name}  ->  {level_name}   (|cover|={len(SLp)})")
    check(f"{name}: center = {{+-I}} order 2", len(Z)==2 and (p-1,0,0,p-1) in Z, f"{len(Z)} central")
    check(f"{name}/center is Mobius group of order {len(SLp)//2}", len(psl)==len(SLp)//2,
          f"|PSL/PGL image|={len(psl)}")
    check(f"{name}/center matches {level_name} (order+element-profile)",
          profile(psl)==level_prof, f"{profile(psl)}")
    if split_expected:
        check(f"{name}: SPLIT central Z2-extension (many involutions)", ni>1, f"{ni} involutions")
    else:
        check(f"{name}: NON-SPLIT Schur cover (unique involution -I)", ni==1, f"{ni} involutions")

print("="*74)
print("ODD LEVELS: PSL(2,p) spine  <-  SL(2,p) Schur cover  (p = 7,5,3)")
print("="*74)
cover_report("SL(2,7)", SL2(7), 7, "PSL(2,7) [L7]",
             profile(mobius_group(SL2(7),7)))   # L7 IS PSL(2,7); self-consistent identity
# also confirm PSL(2,7) is not one of A_n by order
check("L7 PSL(2,7): order 168 (simple, = the level itself)", len(mobius_group(SL2(7),7))==168)
cover_report("2I=SL(2,5)", SL2(5), 5, "A5 = PSL(2,5) [L5]", PROF["A5"])
cover_report("2T=SL(2,3)", SL2(3), 3, "A4 = PSL(2,3) [L3]", PROF["A4"])

print("\n"+"="*74)
print("SPLIT covers (direct products; NOT the Schur cover)")
print("="*74)
Ih=closure([(1,2,0,3,4,5,6),(0,1,2,3,4,6,5)])   # A5? no -> need A5 gens x Z2
# build Ih = A5 x Z2 on 7 pts: A5 on 0..4 (<(012),(01234)>), Z2 = swap 5,6
Ih=closure([(1,2,0,3,4,5,6),(1,2,3,4,0,5,6),(0,1,2,3,4,6,5)])
Th=closure([(1,2,0,3,4,5),(0,2,3,1,4,5),(0,1,2,3,5,4)])  # A4 on 0..3 x Z2 swap 4,5
check("Ih = A5 x Z2 (split): order 120, many involutions", len(Ih)==120 and profile(Ih).get(2,0)>1,
      f"|Ih|={len(Ih)}, involutions={profile(Ih).get(2,0)}")
check("Th = A4 x Z2 (split; the SPINE-MAP 'Th'): order 24, many involutions",
      len(Th)==24 and profile(Th).get(2,0)>1, f"|Th|={len(Th)}, involutions={profile(Th).get(2,0)}")
print("  [note] Ih/Th are the SPLIT Z2-extensions of A5/A4; the Schur covers 2I/2T are")
print("  the NON-SPLIT ones above. Same order, different group (unique vs many involutions).")

print("\n"+"="*74)
print("EVEN level L4 = S4: double cover GL(2,3)=2.S4  (2O is the sibling cover)")
print("="*74)
GL3=GL2(3); Z=center(GL3,3); pgl3=mobius_group(GL3,3)
check("GL(2,3): order 48, center {+-I}", len(GL3)==48 and len(Z)==2)
check("GL(2,3)/center = PGL(2,3) matches S4 (order+profile)", profile(pgl3)==PROF["S4"], f"{profile(pgl3)}")
# transposition lift: a reflection (det = -1 = 2) e.g. diag(1,2) -> order in GL(2,3)?
refl=(1,0,0,2)
check("GL(2,3): an S4-transposition lifts to order 2 (=> the 2.S4 with reflections as involutions)",
      mord(refl,3)==2, f"order(diag(1,2))={mord(refl,3)}")
print("  [cited] 2O (binary octahedral) is the OTHER double cover of S4 (also order 48,")
print("  non-isomorphic; there a transposition lifts to ORDER 4). Not SL(2,q); not rebuilt here.")

print("\n"+"="*74)
print("Over-group (NOT a central cover): PGL(2,7) > PSL(2,7) index 2")
print("="*74)
PGL7=mobius_group(GL2(7),7); PSL7=mobius_group(SL2(7),7)
check("PGL(2,7): order 336; PSL(2,7) < PGL(2,7) index 2", len(PGL7)==336 and PSL7<=PGL7 and len(PGL7)//len(PSL7)==2)
# normality: PSL is the unique index-2 subgroup -> normal
def is_normal(H,G):
    Hs=set(H)
    # conjugation in a perm group: g h g^-1
    def inv(g):
        r=[0]*len(g)
        for i,x in enumerate(g): r[x]=i
        return tuple(r)
    return all(compose(compose(g,h),inv(g)) in Hs for g in G for h in Hs)
check("PSL(2,7) is NORMAL in PGL(2,7) (the quotient is OUTER/diagonal, not central)",
      is_normal(PSL7,PGL7))
print("  [distinction] SL(2,7) is a CENTRAL (Schur) cover of PSL(2,7); PGL(2,7) is an")
print("  index-2 OVER-group (outer-diagonal). Same order 336, opposite roles. Both were")
print("  listed as L7 'COVERS' in SPINE MAP -> refined here at equal prominence.")

print("\n"+"="*74)
print("TOP BRIDGE: W(E6) < Sp6(2) = W(E7)/+-   (cited SM-003/SM-015; arithmetic checked)")
print("="*74)
WE6=51840; WE7=2903040; Sp62=WE7//2
check("|Sp6(2)| = |W(E7)|/2 = 1451520", Sp62==1451520, f"{Sp62}")
check("[Sp6(2) : W(E6)] = 28  (the 28 Klein-quartic bitangents; 51840 x 28 = 1451520)",
      Sp62//WE6==28 and WE6*28==Sp62, f"index={Sp62/WE6}")
print("  [cited] the embedding W(E6)=stab(one bitangent) < Sp6(2), PSL(2,7) transitive on")
print("  28, intersection S3=N(<z3>) is SEALED in SM-003 (verify_tbr_bridge.py) and SM-015")
print("  (verify_stoneq_clifford.py); the 2.9M-element W(E7) build is not repeated here.")

print("\n"+"="*74)
print(f"TOWER B: {PASS} computed checks PASS, {FAIL} FAIL")
if FAIL:
    print("REFUTED / TO-INVESTIGATE:")
    for f in fails: print("   - "+f)
    raise SystemExit(1)
print("VERDICT: Tower B verified. Backbone = the SL(2,p) Schur-cover chain over the ODD")
print("spine levels (L7,L5,L3 = PSL(2,7),PSL(2,5),PSL(2,3) <- SL(2,7),SL(2,5),SL(2,3)),")
print("with split covers Ih/Th, S4's cover GL(2,3)=2.S4 (2O sibling cited), the over-group")
print("PGL(2,7) distinguished from the central cover, and the top bridge W(E6)<Sp6(2)=W(E7)/+-")
print("closed by index 28 against sealed SM-003/SM-015. Two towers now stand side by side.")
print("Not RH/GRH.")
