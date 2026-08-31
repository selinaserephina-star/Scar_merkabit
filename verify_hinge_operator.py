# -*- coding: utf-8 -*-
r"""verify_hinge_operator.py  --  Ilya's HINGE OPERATOR on the descent bridges.

Proposal (IB, 2026-08-31): for a bridge (G_L, G_R) of the descent
    PSL(2,7) -> C6xZ2 -> A5 -> S4 -> A4 -> Z2 -> 1
define
    C_hinge(G_L, G_R) = ( N_{G_R}([C3]) , pi^-1( N_{G_R}([C3]) ) )
where [C3] is the shared conjugacy class of order-3 subgroups and
pi : 2.G_R -> G_R is "the canonical double cover" of the right-hand group.

Verified here, compute-never-assert:
  1. his C_max results on the top two bridges (shared subgroup iso-types,
     unique max-order class, the two incomparable inclusion-maximal classes)
     -- independent recomputation of the SM-020 floor;
  2. his trivial C_max failure on 6<->5 (nonabelian mediators vs abelian C6xZ2);
  3. his hinge result C_hinge(C6xZ2, A5) = (S3, Dic3), with an EXPLICIT iso
     A5 -> PSL(2,5) and the preimage computed inside SL(2,5);
  4. his declared next step, executed: C_hinge on ALL remaining bridges,
     including BOTH double covers of S4 (GL(2,3) = 2.S4- and the binary
     octahedral 2O = 2.S4+, built exactly as unit quaternions over Z[sqrt2]/2)
     and the 7<->6 cover obstruction (two non-isomorphic stem covers of C6xC2).

[C] = computed here.  [P] = classical, cited (Schur multiplier formula).
Refutations stay at full prominence.  Not RH/GRH.

Run:  python -X utf8 verify_hinge_operator.py
"""

PASS = 0; FAIL = 0; fails = []; NUM = 0
def check(claim, ok, detail=""):
    global PASS, FAIL, NUM
    NUM += 1
    tag = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1; fails.append(f"#{NUM:02d} {claim}")
    print(f"  [{NUM:02d}][{tag}] {claim}" + (f"  --  {detail}" if detail else ""))

# ===================== permutation machinery =====================
def compose(p, q): return tuple(p[q[i]] for i in range(len(p)))
def identity(n):   return tuple(range(n))
def inverse(p):
    r = [0]*len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def order_of(p):
    e = identity(len(p)); x = p; k = 1
    while x != e: x = compose(x, p); k += 1
    return k
def closure(gens):
    n = len(gens[0]); e = identity(n); G = {e}; fr = [e]
    while fr:
        a = fr.pop()
        for g in gens:
            b = compose(a, g)
            if b not in G: G.add(b); fr.append(b)
    return G
def order_profile(G):
    pr = {}
    for g in G: pr[order_of(g)] = pr.get(order_of(g), 0) + 1
    return dict(sorted(pr.items()))
def conj_set(g, H): return frozenset(compose(compose(g, h), inverse(g)) for h in H)
def normalizer(G, H):
    Hf = frozenset(H)
    return {g for g in G if conj_set(g, Hf) == Hf}
def is_abelian(G):
    L = list(G)
    return all(compose(a, b) == compose(b, a) for i, a in enumerate(L) for b in L[i:])
def c3_subgroups(G):
    return {frozenset(closure([x])) for x in G if order_of(x) == 3}
def conj_classes(G, subs):
    subs = set(subs); classes = []
    while subs:
        H = next(iter(subs))
        orb = {conj_set(g, H) for g in G}
        classes.append(orb); subs -= orb
    return classes
def derived_subgroup(G):
    comms = {compose(compose(g, h), compose(inverse(g), inverse(h)))
             for g in G for h in G}
    return closure(list(comms))
def quotient_profile(G, N):
    """(order, element-order profile) of G/N for N normal in G."""
    Nf = frozenset(N); reps = {}
    for g in G:
        c = frozenset(compose(g, n) for n in N)
        if c not in reps: reps[c] = g
    prof = {}
    for g in reps.values():
        x = g; k = 1
        while x not in Nf: x = compose(x, g); k += 1
        prof[k] = prof.get(k, 0) + 1
    return len(reps), dict(sorted(prof.items()))

# ---- iso-type fingerprint + naming (style of verify_bridge_transfer.py) ----
def fp_of(H):
    pr = {}
    for g in H: pr[order_of(g)] = pr.get(order_of(g), 0) + 1
    return (len(H), tuple(sorted(pr.items())))
def name(f):
    order, items = f; prof = dict(items); h = lambda k: prof.get(k, 0)
    if order == 1:  return "1"
    if order == 2:  return "C2"
    if order == 3:  return "C3"
    if order == 4:  return "C4" if h(4) else "V4"
    if order == 5:  return "C5"
    if order == 6:  return "C6" if h(6) else "S3"
    if order == 7:  return "C7"
    if order == 8:
        if h(8): return "C8"
        if h(4) == 6: return "Q8"
        if h(4) == 2 and h(2) == 5: return "D4"
        if h(2) == 7: return "C2^3"
        return "C4xC2"
    if order == 10: return "C10" if h(10) else "D5"
    if order == 12:
        if prof == {1:1, 2:3, 3:8}: return "A4"
        if h(2) == 7:  return "D6(12)=C2xS3"
        if h(12):      return "C12"
        if h(4) == 6:  return "Dic3"
        if h(6) == 6:  return "C6xC2"
        return "?12"
    if order == 21: return "F21(7:3)"
    if order == 24: return "S4" if h(2) == 9 else "?24"
    if order == 60: return "A5"
    if order == 168: return "PSL(2,7)"
    return f"?{order}"

def types_fp(Gset):
    """All subgroup iso-type fingerprints of Gset (every subgroup here is
    <=2-generated, as in the sealed SM-020 machinery)."""
    G = list(Gset); n = len(G)
    idx = {g: i for i, g in enumerate(G)}
    e = idx[identity(len(G[0]))]
    mul = [[idx[compose(a, b)] for b in G] for a in G]
    ordv = [order_of(g) for g in G]
    def fpH(H):
        pr = {}
        for i in H: pr[ordv[i]] = pr.get(ordv[i], 0) + 1
        return (len(H), tuple(sorted(pr.items())))
    def cl(gens):
        S = {e} | set(gens); fr = list(S)
        while fr:
            a = fr.pop()
            for g in gens:
                b = mul[a][g]
                if b not in S: S.add(b); fr.append(b)
        return frozenset(S)
    types = {fpH(frozenset([e]))}
    cyc = {}
    for i in range(n):
        H = cl([i]); cyc[i] = H; types.add(fpH(H))
    for a in range(n):
        Ca = cyc[a]
        for b in range(a + 1, n):
            if b in Ca: continue
            types.add(fpH(cl([a, b])))
    return types
def names_of(fps): return sorted({name(f) for f in fps}, key=lambda s: (len(s), s))

# ===================== matrix machinery mod p =====================
I2 = (1, 0, 0, 1)
def mmul(A, B, p):
    a,b,c,d = A; e,f,g,h = B
    return ((a*e+b*g) % p, (a*f+b*h) % p, (c*e+d*g) % p, (c*f+d*h) % p)
def morder(M, p):
    x = M; k = 1
    while x != I2: x = mmul(x, M, p); k += 1
    return k
def minv(M, p):
    a,b,c,d = M; dt = (a*d - b*c) % p; di = pow(dt, p-2, p)
    return ((d*di) % p, (-b*di) % p, (-c*di) % p, (a*di) % p)
def SL2(p):
    return [(a,b,c,d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if (a*d-b*c) % p == 1]
def GL2(p):
    return [(a,b,c,d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if (a*d-b*c) % p != 0]
def mobius(M, p):
    """Action on P^1(F_p) = {0..p-1, oo=p} as a permutation tuple."""
    a,b,c,d = M; img = []
    for x in range(p + 1):
        if x == p:
            img.append(p if c % p == 0 else (a * pow(c, p-2, p)) % p)
        else:
            den = (c*x + d) % p
            img.append(p if den == 0 else ((a*x + b) % p * pow(den, p-2, p)) % p)
    return tuple(img)
def mat_fp(Ms, p):
    pr = {}
    for M in Ms: pr[morder(M, p)] = pr.get(morder(M, p), 0) + 1
    return (len(Ms), tuple(sorted(pr.items())))

# ===================== exact quaternions over (Z + Z*sqrt2)/2 =====================
# coordinate (p, q) means (p + q*sqrt2)/2 ; exact integer arithmetic throughout.
ONE_Q = ((2,0), (0,0), (0,0), (0,0))
def _cm(c1, c2):           # coordinate product at scale 1/4
    p1, r1 = c1; p2, r2 = c2
    return (p1*p2 + 2*r1*r2, p1*r2 + r1*p2)
def _neg4(c): return (-c[0], -c[1])
def qmul(q1, q2):
    w1,x1,y1,z1 = q1; w2,x2,y2,z2 = q2
    comps = []
    for terms in (
        (_cm(w1,w2), _neg4(_cm(x1,x2)), _neg4(_cm(y1,y2)), _neg4(_cm(z1,z2))),
        (_cm(w1,x2), _cm(x1,w2), _cm(y1,z2), _neg4(_cm(z1,y2))),
        (_cm(w1,y2), _neg4(_cm(x1,z2)), _cm(y1,w2), _cm(z1,x2)),
        (_cm(w1,z2), _cm(x1,y2), _neg4(_cm(y1,x2)), _cm(z1,w2))):
        A = sum(t[0] for t in terms); B = sum(t[1] for t in terms)
        assert A % 2 == 0 and B % 2 == 0, "left the (Z+Z*sqrt2)/2 lattice"
        comps.append((A // 2, B // 2))
    return tuple(comps)
def qconj(q):
    return (q[0], (-q[1][0], -q[1][1]), (-q[2][0], -q[2][1]), (-q[3][0], -q[3][1]))
def qorder(q):
    x = q; k = 1
    while x != ONE_Q: x = qmul(x, q); k += 1
    return k
def qclosure(gens):
    G = {ONE_Q}; fr = [ONE_Q]
    while fr:
        a = fr.pop()
        for g in gens:
            b = qmul(a, g)
            if b not in G: G.add(b); fr.append(b)
    return G
def quat_fp(Qs):
    pr = {}
    for q in Qs: pr[qorder(q)] = pr.get(qorder(q), 0) + 1
    return (len(Qs), tuple(sorted(pr.items())))

# ===================== generic Dic3 presentation witness =====================
def dic3_witness(P, mul, inv, ordf, e):
    """Find a,b in P with a^6=1, b^2=a^3, b a b^-1 = a^-1, <a,b> = P."""
    Pset = set(P)
    a6 = [x for x in P if ordf(x) == 6]; b4 = [x for x in P if ordf(x) == 4]
    for a in a6:
        a3 = mul(mul(a, a), a); ai = inv(a)
        for b in b4:
            if mul(b, b) == a3 and mul(mul(b, a), inv(b)) == ai:
                S = {e}; fr = [e]
                while fr:
                    x = fr.pop()
                    for g in (a, b):
                        y = mul(x, g)
                        if y not in S: S.add(y); fr.append(y)
                if S == Pset: return a, b
    return None

# ===================== build the groups =====================
S5 = closure([(1,2,3,4,0), (1,0,2,3,4)])
def even5(g): return sum(1 for i in range(5) for j in range(i+1,5) if g[i] > g[j]) % 2 == 0
A5   = {g for g in S5 if even5(g)}                       # on 5 points
S4   = closure([(1,2,3,0), (1,0,2,3)])                   # on 4 points
A4   = closure([(1,2,0,3), (0,2,3,1)])                   # on 4 points
Z2   = closure([(1,0)])
C6Z2 = closure([(1,2,3,4,5,0,6,7), (0,1,2,3,4,5,7,6)])   # C6 x Z2 on 8 points
SL27 = SL2(7); PSL27 = {mobius(M, 7) for M in SL27}      # on 8 points
SL25 = SL2(5); PSL25 = {mobius(M, 5) for M in SL25}      # on 6 points
SL23 = SL2(3); GL23 = GL2(3)
PGL23 = {mobius(M, 3) for M in GL23}                     # = S4 on P^1(F3), 4 points
PSL23 = {mobius(M, 3) for M in SL23}                     # = A4 on P^1(F3)

print("=" * 74)
print("HINGE OPERATOR   C_hinge(G_L,G_R) = ( N_{G_R}([C3]) , pi^-1(N_{G_R}([C3])) )")
print("descent: PSL(2,7) -> C6xZ2 -> A5 -> S4 -> A4 -> Z2 -> 1   (IB, 2026-08-31)")
print("=" * 74)
check("sanity: |PSL(2,7)|=168, |C6xZ2|=12, |A5|=60, |S4|=24, |A4|=12, |Z2|=2 [C]",
      (len(PSL27), len(C6Z2), len(A5), len(S4), len(A4), len(Z2))
      == (168, 12, 60, 24, 12, 2))

# ======================================================================
print("\n" + "=" * 74)
print("PART 1.  C_max: shared subgroup iso-types on the top two bridges")
print("=" * 74)
T7, T6, T5 = types_fp(PSL27), types_fp(C6Z2), types_fp(A5)
print(f"  PSL(2,7) subgroup types: {names_of(T7)}")
print(f"  C6xZ2    subgroup types: {names_of(T6)}")
print(f"  A5       subgroup types: {names_of(T5)}")

sh76 = T7 & T6; sh65 = T6 & T5
check("shared iso-types (PSL(2,7), C6xZ2) = {1, C2, C3, V4} [C]",
      set(names_of(sh76)) == {"1", "C2", "C3", "V4"}, str(names_of(sh76)))
mx76 = [f for f in sh76 if f[0] == max(f2[0] for f2 in sh76)]
check("7<->6: UNIQUE max-order shared class, and it is V4 (order 4) [C]",
      len(mx76) == 1 and name(mx76[0]) == "V4", f"max-order classes: {[name(f) for f in mx76]}")
check("shared iso-types (C6xZ2, A5) = {1, C2, C3, V4} [C]",
      set(names_of(sh65)) == {"1", "C2", "C3", "V4"}, str(names_of(sh65)))
mx65 = [f for f in sh65 if f[0] == max(f2[0] for f2 in sh65)]
check("6<->5: UNIQUE max-order shared class, and it is V4 [C]",
      len(mx65) == 1 and name(mx65[0]) == "V4", f"max-order classes: {[name(f) for f in mx65]}")

# inclusion-maximal shared classes (embedding order on iso-types)
REP = {"1": closure([(0,)]), "C2": closure([(1,0)]), "C3": closure([(1,2,0)]),
       "V4": closure([(1,0,3,2), (2,3,0,1)])}
SUBNAMES = {k: set(names_of(types_fp(v))) for k, v in REP.items()}
def embeds(a, b): return a in SUBNAMES[b]      # iso-type a embeds in iso-type b
shared_names = set(names_of(sh76))
maximal = {t for t in shared_names
           if not any(t != u and embeds(t, u) for u in shared_names)}
check("7<->6: inclusion-MAXIMAL shared classes = {C3, V4}, two of them [C]",
      maximal == {"C3", "V4"}, str(sorted(maximal)))
check("C3 and V4 are INCOMPARABLE (neither embeds in the other) "
      "-> C_max-by-inclusion is NOT unique (his 'uniqueness problem') [C]",
      not embeds("C3", "V4") and not embeds("V4", "C3"))
mx65n = {t for t in set(names_of(sh65))
         if not any(t != u and embeds(t, u) for u in set(names_of(sh65)))}
print(f"  [note] 6<->5 has the same two incomparable maximal classes: {sorted(mx65n)}")
print("  [cross-check] SM-020 (verify_bridge_transfer.py) reported SURVIVES =")
print("  {1,C2,C3,V4} on both top bridges; recomputed independently here: agrees.")

# ======================================================================
print("\n" + "=" * 74)
print("PART 2.  C_max failure on 6<->5 (trivial, recorded): nonabelian mediators")
print("=" * 74)
# NB naming: Ilya's 'D6' = the ORDER-6 dihedral = S3 here. Dic3 = dicyclic order 12.
S3grp = closure([(1,2,0), (1,0,2)])
check("C6xZ2 is ABELIAN [C]", is_abelian(C6Z2))
check("D6-in-his-sense (= S3, order-6 dihedral) is NONABELIAN [C]",
      not is_abelian(S3grp) and len(S3grp) == 6)
# a Dic3 instance, found inside SL(2,5) (as in the sealed mediator-descent run)
mul5 = lambda A, B: mmul(A, B, 5); inv5 = lambda M: minv(M, 5)
ord5 = lambda M: morder(M, 5)
# build one Dic3 directly: a of order 6, b of order 4 with the relations
Dic3mats = None
for a in [M for M in SL25 if morder(M,5) == 6]:
    a3 = mul5(mul5(a, a), a); ai = inv5(a); done = False
    for b in [M for M in SL25 if morder(M,5) == 4]:
        if mul5(b, b) == a3 and mul5(mul5(b, a), inv5(b)) == ai:
            S = {I2}; fr = [I2]
            while fr:
                x = fr.pop()
                for g in (a, b):
                    y = mul5(x, g)
                    if y not in S: S.add(y); fr.append(y)
            Dic3mats = S; done = True; break
    if done: break
check("a Dic3 (order-12 dicyclic) exists (inside SL(2,5)); it is NONABELIAN [C]",
      Dic3mats is not None and len(Dic3mats) == 12
      and any(mul5(x, y) != mul5(y, x) for x in Dic3mats for y in Dic3mats))
check("neither S3 nor Dic3 is a subgroup iso-type of abelian C6xZ2 [C]",
      "S3" not in names_of(T6) and "Dic3" not in names_of(T6),
      f"C6xZ2 types = {names_of(T6)}")
print("  [note] trivial (nonabelian into abelian is impossible) -- recorded as asked.")

# ======================================================================
print("\n" + "=" * 74)
print("PART 3.  C_hinge on 6<->5, input (C6xZ2, A5): claim = (S3, Dic3)")
print("=" * 74)
c3_6 = c3_subgroups(C6Z2)
check("C6xZ2 has exactly ONE C3 subgroup (shared class [C3] exists on the left) [C]",
      len(c3_6) == 1, f"{len(c3_6)} subgroup(s)")
c3sA5 = c3_subgroups(A5); clA5 = conj_classes(A5, c3sA5)
check("[C3] is UNIQUE up to conjugacy in A5 (10 C3-subgroups, ONE class) [C]",
      len(c3sA5) == 10 and len(clA5) == 1,
      f"{len(c3sA5)} subgroups in {len(clA5)} class(es)")

# presentation pair for A5 = <s,t | s^5 = t^3 = (st)^2 = 1>
def find_pres_pair(G):
    fives = [g for g in G if order_of(g) == 5]
    threes = [g for g in G if order_of(g) == 3]
    for s in fives:
        for t in threes:
            if order_of(compose(s, t)) != 2: continue
            if len(closure([s, t])) == len(G): return s, t
    return None
sA, tA = find_pres_pair(A5)
sB, tB = find_pres_pair(PSL25)
check("A5 = <s,t | s^5=t^3=(st)^2=1> realized on 5 points; same in PSL(2,5) [C]",
      sA is not None and sB is not None)

phi = {identity(5): identity(6)}
fr = [identity(5)]
while fr:
    g = fr.pop()
    for ga, gb in ((sA, sB), (tA, tB)):
        h = compose(g, ga)
        if h not in phi:
            phi[h] = compose(phi[g], gb); fr.append(h)
A5l = list(A5)
hom_ok = all(phi[compose(g, h)] == compose(phi[g], phi[h]) for g in A5l for h in A5l)
check("EXPLICIT iso phi: A5 -> PSL(2,5) built (bijective, homomorphism on all "
      "3600 pairs) [C]",
      len(phi) == 60 and len(set(phi.values())) == 60 and set(phi.values()) == PSL25
      and hom_ok)

C3A = frozenset(closure([tA]))
N65 = normalizer(A5, C3A)
check("N_{A5}(C3) has order 6 and iso-type S3 (nonabelian) [C]",
      len(N65) == 6 and name(fp_of(N65)) == "S3", f"profile {order_profile(N65)}")
phiN = {phi[g] for g in N65}
check("phi carries N to N: phi(N_{A5}(C3)) = N_{PSL(2,5)}(phi(C3)) [C]",
      phiN == normalizer(PSL25, {phi[g] for g in C3A}))

Zc = [M for M in SL25 if all(mmul(M, X, 5) == mmul(X, M, 5) for X in SL25)]
check("SL(2,5): order 120, center {+-I} of order 2, pi = mod-+- onto PSL(2,5) "
      "(order 60) [C]",
      len(SL25) == 120 and len(Zc) == 2 and (4,0,0,4) in Zc and len(PSL25) == 60)
pre65 = [M for M in SL25 if mobius(M, 5) in phiN]
check("pi^-1(N) in SL(2,5) has order 12 [C]", len(pre65) == 12)
p65 = dict(mat_fp(pre65, 5)[1])
check("pi^-1(N): UNIQUE involution (only -I) and HAS an order-4 element [C]",
      p65.get(2, 0) == 1 and p65.get(4, 0) > 0, f"profile {p65}")
w = dic3_witness(pre65, mul5, inv5, ord5, I2)
check("pi^-1(N) satisfies <a,b | a^6=1, b^2=a^3, b a b^-1=a^-1> with <a,b> = "
      "the whole preimage => ISO TYPE Dic3 [C]",
      w is not None, f"witness a={w[0]}, b={w[1]}" if w else "no witness")
check("profile check agrees: pi^-1(N) fingerprint names as Dic3 [C]",
      name(mat_fp(pre65, 5)) == "Dic3", f"{name(mat_fp(pre65, 5))}")
print("  => C_hinge(C6xZ2, A5) = (S3, Dic3)   -- IB's 6<->5 double hinge REPRODUCED.")
print("     The Dic3 slot coincides with the mediator-descent run's spinorial hinge")
print("     (verify_mediator_descent.py: Dic3 < 2I); the S3 slot is the normalizer,")
print("     related to that run's D6 = S3 x Z2 (order 12) by dropping the central Z2.")

# ======================================================================
print("\n" + "=" * 74)
print("PART 4a.  EXTEND 5<->4, input (A5, S4): TWO covers of S4 -> TWO answers")
print("=" * 74)
c3sS4 = c3_subgroups(S4); clS4 = conj_classes(S4, c3sS4)
check("[C3] shared and UNIQUE up to conjugacy in S4 (4 subgroups, one class) [C]",
      len(c3sS4) == 4 and len(clS4) == 1 and any(order_of(g) == 3 for g in A5))
C3S4 = next(iter(c3sS4)); N54 = normalizer(S4, C3S4)
check("N_{S4}(C3) has order 6 and iso-type S3 [C]",
      len(N54) == 6 and name(fp_of(N54)) == "S3", f"profile {order_profile(N54)}")
print("  [cited: sealed verify_tower_b.py] S4 has TWO non-isomorphic double covers,")
print("  GL(2,3) = 2.S4- (transpositions lift to involutions) and the binary")
print("  octahedral 2O = 2.S4+ (transpositions lift to order 4). 'THE canonical")
print("  double cover' is therefore ALREADY ambiguous at this bridge. Both computed:")

# ---- cover 1: GL(2,3), pi = mobius onto PGL(2,3) = S4 on P^1(F3) ----
ZGL = [M for M in GL23 if all(mmul(M, X, 3) == mmul(X, M, 3) for X in GL23)]
check("GL(2,3): order 48, center = scalars {I,2I}, pi image = S4 on P^1(F3) [C]",
      len(GL23) == 48 and len(ZGL) == 2 and len(PGL23) == 24
      and name(fp_of(PGL23)) == "S4", f"image profile {order_profile(PGL23)}")
c3sP = c3_subgroups(PGL23)
check("in this S4 copy too: 4 C3-subgroups, one conjugacy class [C]",
      len(c3sP) == 4 and len(conj_classes(PGL23, c3sP)) == 1)
C3P = next(iter(c3sP)); NP = normalizer(PGL23, C3P)
preGL = [M for M in GL23 if mobius(M, 3) in NP]
fpGL = mat_fp(preGL, 3)
check("GL(2,3): pi^-1(N_{S4}(C3)) has order 12 [C]", len(preGL) == 12)
check("GL(2,3) preimage ISO TYPE identified: D6(12) = C2xS3 (7 involutions, no "
      "order-4 element) [C]",
      name(fpGL) == "D6(12)=C2xS3", f"profile {dict(fpGL[1])} -> {name(fpGL)}")

# ---- cover 2: 2O as exact unit quaternions; pi = rotation action on the 4 cube diagonals ----
qi    = ((0,0), (2,0), (0,0), (0,0))            # i
omega = ((1,0), (1,0), (1,0), (1,0))            # (1+i+j+k)/2
sigma = ((0,1), (0,1), (0,0), (0,0))            # (1+i)/sqrt2
TwoO = qclosure([qi, omega, sigma])
fp2O = quat_fp(TwoO)
check("2O built exactly (unit quaternions over (Z+Z*sqrt2)/2): order 48, "
      "UNIQUE involution -1 [C]",
      len(TwoO) == 48 and dict(fp2O[1]).get(2, 0) == 1, f"profile {dict(fp2O[1])}")
check("2O is NOT isomorphic to GL(2,3) (1 involution vs "
      f"{dict(mat_fp(GL23,3)[1]).get(2,0)}) => genuinely two covers [C]",
      dict(fp2O[1]).get(2, 0) != dict(mat_fp(GL23, 3)[1]).get(2, 0))

DIAG = [(1,1,1), (1,1,-1), (1,-1,1), (-1,1,1)]
def vrep(v): return ((0,0), (2*v[0],0), (2*v[1],0), (2*v[2],0))
def rot(q, v):
    w = qmul(qmul(q, vrep(v)), qconj(q))
    assert w[0] == (0, 0)
    out = []
    for (p, r) in w[1:]:
        assert r == 0 and p % 2 == 0
        out.append(p // 2)
    return tuple(out)
def pi2O(q):
    img = []
    for d in DIAG:
        w = rot(q, d)
        for j, d2 in enumerate(DIAG):
            if w == d2 or w == tuple(-c for c in d2): img.append(j); break
        else: raise RuntimeError("diagonal not mapped to a diagonal")
    return tuple(img)
qpi = {q: pi2O(q) for q in TwoO}
IM = set(qpi.values())
TwoOl = list(TwoO)
pi_hom = all(qpi[qmul(a, b)] == compose(qpi[a], qpi[b]) for a in TwoOl for b in TwoOl)
kern = [q for q in TwoO if qpi[q] == identity(4)]
check("pi: 2O -> S4 (cube-diagonal action) is a homomorphism, image = S4, "
      "kernel = {+-1} [C]",
      pi_hom and len(IM) == 24 and name(fp_of(IM)) == "S4" and len(kern) == 2)
c3s2O = c3_subgroups(IM); C3O = next(iter(c3s2O)); NO = normalizer(IM, C3O)
check("this S4 copy: N(C3) again S3, C3 class unique [C]",
      len(NO) == 6 and name(fp_of(NO)) == "S3"
      and len(conj_classes(IM, c3s2O)) == 1)
pre2O = [q for q in TwoO if qpi[q] in NO]
fpP2O = quat_fp(pre2O)
w2 = dic3_witness(pre2O, qmul, qconj, qorder, ONE_Q)   # inverse = conjugate (unit)
check("2O: pi^-1(N_{S4}(C3)) has order 12 and ISO TYPE Dic3 (profile + "
      "presentation witness) [C]",
      len(pre2O) == 12 and name(fpP2O) == "Dic3" and w2 is not None,
      f"profile {dict(fpP2O[1])} -> {name(fpP2O)}")
check("the two 5<->4 preimages are NON-ISOMORPHIC (C2xS3 vs Dic3) => C_hinge's "
      "second slot is COVER-DEPENDENT at 5<->4 [C]",
      name(fpGL) != name(fpP2O), f"{name(fpGL)} vs {name(fpP2O)}")
print("  => C_hinge(A5, S4) = (S3, D6(12)=C2xS3) under GL(2,3),")
print("     but        = (S3, Dic3)          under 2O.  Output NOT well-defined")
print("     unless a cover convention is fixed. (Dic3 side matches the 6<->5 hinge.)")

# ======================================================================
print("\n" + "=" * 74)
print("PART 4b.  EXTEND 4<->3, input (S4, A4)")
print("=" * 74)
c3sA4 = c3_subgroups(A4); clA4 = conj_classes(A4, c3sA4)
check("[C3] shared; in A4: 4 C3-subgroups, ONE conjugacy class [C]",
      len(c3sA4) == 4 and len(clA4) == 1 and any(order_of(g) == 3 for g in S4))
C3A4 = next(iter(c3sA4)); N43 = normalizer(A4, C3A4)
check("N_{A4}(C3) = C3 ITSELF (order 3; the C3 is self-normalizing in A4) [C]",
      frozenset(N43) == C3A4 and len(N43) == 3, f"|N| = {len(N43)}")
# preimage in SL(2,3) = 2.A4 via mobius onto PSL(2,3) = A4 on P^1(F3)
check("SL(2,3): order 24, image PSL(2,3) = A4 (order 12) [C]",
      len(SL23) == 24 and len(PSL23) == 12 and name(fp_of(PSL23)) == "A4")
c3s23 = c3_subgroups(PSL23); C3q = next(iter(c3s23))
Nq = normalizer(PSL23, C3q)
check("in the PSL(2,3) copy too: N(C3) = C3 itself [C]", frozenset(Nq) == C3q)
pre43 = [M for M in SL23 if mobius(M, 3) in Nq]
fp43 = mat_fp(pre43, 3)
check("pi^-1(C3) in SL(2,3): order 6 and CYCLIC C6 (has an order-6 element) [C]",
      len(pre43) == 6 and name(fp43) == "C6", f"profile {dict(fp43[1])}")
print("  => C_hinge(S4, A4) = (C3, C6).")

# ======================================================================
print("\n" + "=" * 74)
print("PART 4c.  EXTEND 3<->2, input (A4, Z2)")
print("=" * 74)
check("Z2 has NO order-3 element -> no shared [C3] -> C_hinge UNDEFINED at 3<->2 [C]",
      not any(order_of(g) == 3 for g in Z2), f"Z2 profile {order_profile(Z2)}")
print("  (2<->1 is likewise trivially undefined: the trivial group has no C3.)")

# ======================================================================
print("\n" + "=" * 74)
print("PART 4d.  EXTEND 7<->6, input (PSL(2,7), C6xZ2): the cover obstruction")
print("=" * 74)
check("shared [C3] exists (PSL(2,7) has order-3 elements; C6xZ2 has its unique "
      "C3) [C]",
      any(order_of(g) == 3 for g in PSL27) and len(c3_6) == 1)
C36 = next(iter(c3_6)); N76 = normalizer(C6Z2, C36)
check("N_{C6xZ2}(C3) = the WHOLE group C6xZ2 (abelian, order 12) [C]",
      set(N76) == set(C6Z2), f"|N| = {len(N76)}")
g6, g2 = 6, 2
check("[P] Schur multiplier M(C6 x C2) = C_gcd(6,2) = C2 (formula M(Cm x Cn) = "
      "C_gcd(m,n), classical) -- a nontrivial double cover EXISTS; gcd checked [C]",
      __import__("math").gcd(g6, g2) == 2)

def stem_check(label, E):
    """E is a stem extension of C6xC2 by C2 iff there is Z ~ C2 central,
    Z <= [E,E], with E/Z ~ C6xC2. We exhibit Z = [E,E]."""
    D = derived_subgroup(E)
    central = all(compose(z, g) == compose(g, z) for z in D for g in E)
    qord, qprof = quotient_profile(E, D)
    ok = (len(E) == 24 and len(D) == 2 and central
          and qord == 12 and qprof == {1:1, 2:3, 3:2, 6:6})
    check(f"{label}: |E|=24; Z:=[E,E] has order 2, CENTRAL (so Z ~ C2 <= [E,E]); "
          f"E/Z has order 12 with the C6xC2 profile => STEM cover of C6xC2 [C]",
          ok, f"|D|={len(D)}, central={central}, E/Z: order {qord}, profile {qprof}")
    return ok

# E1 = C3 x D4  (C3 on 0-2, D4 on the square 3-4-5-6)
E1 = closure([(1,2,0,3,4,5,6), (0,1,2,4,5,6,3), (0,1,2,3,6,5,4)])
# E2 = C3 x Q8  (C3 on 0-2, Q8 in its left-regular representation on 3-10)
def _ax(a, b):
    if a == 0: return (1, b)
    if b == 0: return (1, a)
    if a == b: return (-1, 0)
    table = {(1,2):(1,3), (2,3):(1,1), (3,1):(1,2),
             (2,1):(-1,3), (3,2):(-1,1), (1,3):(-1,2)}
    return table[(a, b)]
def _qidx(x, y):   # multiply quaternion units indexed 0..7 = +-1,+-i,+-j,+-k
    sx, ax = 1 - 2*(x % 2), x // 2
    sy, ay = 1 - 2*(y % 2), y // 2
    s, az = _ax(ax, ay); s *= sx * sy
    return az*2 + (0 if s > 0 else 1)
Li = tuple(_qidx(2, y) for y in range(8))   # left mult by i
Lj = tuple(_qidx(4, y) for y in range(8))   # left mult by j
Q8 = closure([Li, Lj])
check("Q8 (left-regular, 8 points): order 8, profile {1:1,2:1,4:6} [C]",
      len(Q8) == 8 and order_profile(Q8) == {1:1, 2:1, 4:6}, str(order_profile(Q8)))
def shift(p, off, deg):
    base = list(range(deg))
    for i, x in enumerate(p): base[off + i] = off + x
    return tuple(base)
E2 = closure([(1,2,0) + tuple(range(3, 11)), shift(Li, 3, 11), shift(Lj, 3, 11)])

ok1 = stem_check("E1 = C3 x D4", E1)
ok2 = stem_check("E2 = C3 x Q8", E2)
f1, f2 = fp_of(E1), fp_of(E2)
check("E1 and E2 are NON-ISOMORPHIC (5 involutions vs 1) [C]",
      f1 != f2 and dict(f1[1])[2] == 5 and dict(f2[1])[2] == 1,
      f"E1 {dict(f1[1])}  vs  E2 {dict(f2[1])}")
check("CONCLUSION 7<->6: double covers EXIST (multiplier C2) but >=2 non-isomorphic "
      "stem covers of C6xC2 -> NO canonical 2.G_R -> C_hinge UNDEFINED; IB's claim "
      "CONFIRMED with the sharpened reason (uniqueness fails, not existence) [C]",
      ok1 and ok2 and f1 != f2)
print("  [note] IB said 'no canonical double cover on the abelian side'. Sharpened:")
print("  covers exist (M(C6xC2)=C2 [P]); what fails is CANONICALITY -- C3xD4 and")
print("  C3xQ8 are both stem C2-covers of C6xC2 and are not isomorphic.")

# ======================================================================
print("\n" + "=" * 74)
print("C_hinge OUTPUT TABLE (all six bridges of the descent)")
print("=" * 74)
print("| bridge | (G_L, G_R)          | N_{G_R}([C3]) | pi^-1(N) in 2.G_R           | C_hinge |")
print("|--------|---------------------|---------------|------------------------------|---------|")
print("| 7<->6  | (PSL(2,7), C6xZ2)   | C6xZ2 (whole) | no canonical cover           | UNDEFINED (>=2 stem covers: C3xD4, C3xQ8) |")
print("| 6<->5  | (C6xZ2, A5)         | S3            | Dic3  (in SL(2,5))           | (S3, Dic3) |")
print("| 5<->4  | (A5, S4)            | S3            | GL(2,3): C2xS3 / 2O: Dic3    | COVER-DEPENDENT |")
print("| 4<->3  | (S4, A4)            | C3 (self-nrm) | C6    (in SL(2,3))           | (C3, C6) |")
print("| 3<->2  | (A4, Z2)            | -             | -                            | UNDEFINED (Z2 has no C3) |")
print("| 2<->1  | (Z2, 1)             | -             | -                            | UNDEFINED (trivial group has no C3) |")

print("\n" + "=" * 74)
print(f"HINGE OPERATOR: {PASS} computed checks PASS, {FAIL} FAIL")
if FAIL:
    print("REFUTED / TO-INVESTIGATE:")
    for f in fails: print("   - " + f)
print("=" * 74)
print("VERDICT.")
print("(i)  C_hinge REPRODUCES IB's 6<->5 double hinge: C_hinge(C6xZ2,A5) = (S3,Dic3),")
print("     computed via an explicit iso A5 -> PSL(2,5) and the preimage in SL(2,5).")
print("(ii) On 5<->4 it yields (S3, C2xS3) under GL(2,3) but (S3, Dic3) under 2O --")
print("     the operator's 'canonical double cover' is ambiguous exactly where S4 has")
print("     two covers; and NEITHER slot equals the OBSERVED 5<->4 bridge object,")
print("     which per the sealed SM-020/mediator-descent is the mediator A4 = A5 ^ S4.")
print("     The 4<->3 output (C3, C6) likewise does not name the observed 4<->3 hinge")
print("     V4 (SM-020). MISMATCH RECORDED AS A FINDING, not a failure of the run.")
print("(iii) C_hinge is UNDEFINED at 3<->2 and 2<->1 (no C3 below A4) and at 7<->6 --")
print("     there because canonicality of the cover fails on the abelian side:")
print("     M(C6xC2) = C2 gives existence, but C3xD4 and C3xQ8 are two non-isomorphic")
print("     stem covers, so 'THE' double cover does not exist. Not RH/GRH.")
if FAIL: raise SystemExit(1)
