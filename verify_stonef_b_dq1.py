# verify_stonef_b_dq1.py — STONE F(b): DQ-1 — the explicit PSL(2,7) action
# on the crystal 56, and the coordinate-level field-sector theorem.
#
# ROUTE.  W(E7) acts on the 56 minuscule weights by simple reflections
# s_i(w) = w - w_i * (row i of the Cartan matrix)  (omega-basis).  The
# antipode iota = -1 is central, so W acts on the 28 iota-pairs through
# Sp6(2) = W(E7)/{+-1}.  We hunt an L2(7) = PSL(2,7) in the pair action
# (random order-7 element c + involution x with <x,c> of order 168), lift
# the generators to the 56 by their reflection words, kill the possible
# {+-1} by passing to the derived subgroup (L2(7) is perfect, so the lift
# 2 x L2(7) has UNIQUE perfect part), enumerate all 168 elements, and:
#
#   DQ-1: compute the orbits on the 56.  PREDICTION registered in advance
#   (character level, from Stone F(a)'s sector theorem): permutation
#   character = chi1+chi3+chi3b+2chi6+3chi7+2chi8, hence fixed-point
#   profile [56,0,2,0,0,0] by class order (1,2,3,4,7,7) and a SINGLE
#   56-orbit with weight-stabilizer Z3.
#
# Run:  python -X utf8 verify_stonef_b_dq1.py
import json, random
from collections import Counter
from fractions import Fraction

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("STONE F(b) -- DQ-1: the explicit PSL(2,7) on the crystal 56")
print("=" * 78)

D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]
idx = {v: k for k, v in enumerate(verts)}
IOTA, FRAME = D["IOTA"], D["FRAME"]
N = 56
C7 = [[ 2, 0,-1, 0, 0, 0, 0],
      [ 0, 2, 0,-1, 0, 0, 0],
      [-1, 0, 2,-1, 0, 0, 0],
      [ 0,-1,-1, 2,-1, 0, 0],
      [ 0, 0, 0,-1, 2,-1, 0],
      [ 0, 0, 0, 0,-1, 2,-1],
      [ 0, 0, 0, 0, 0,-1, 2]]

# ---- W(E7) on the 56 weights via simple reflections
S = []
for i in range(7):
    perm = []
    for k in range(N):
        w = verts[k]
        img = tuple(w[j] - w[i]*C7[i][j] for j in range(7))
        perm.append(idx[img])
    S.append(tuple(perm))
check("reflections", "the 7 simple reflections are involutions permuting "
      "the 56 weights",
      all(all(s[s[k]] == k for k in range(N)) for s in S))

def mul(a, b): return tuple(a[b[k]] for k in range(N))
def inv(a):
    r = [0]*N
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
E56 = tuple(range(N))
def order_of(p):
    k, x = 1, p
    while x != E56: x = mul(x, p); k += 1
    return k
def comm(a, b): return mul(mul(a, b), mul(inv(a), inv(b)))

def bsgs_order(gen_list, deg):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0]*deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    if not strong: return 1
    base = []
    for g in strong:
        if all(g[b] == b for b in base):
            base.append(next(i for i in range(deg) if g[i] != i))
    lvl = [[g for g in strong if all(g[b] == b for b in base[:i])]
           for i in range(len(base))]
    transv = [None]*len(base)
    def rebuild(i):
        b = base[i]; T = {b: E}; q = [b]
        while q:
            x = q.pop(0)
            for g in lvl[i]:
                y = g[x]
                if y not in T:
                    T[y] = mulD(g, T[x]); q.append(y)
        transv[i] = T
    for i in range(len(base)): rebuild(i)
    def strip_from(g, start):
        h = g
        for i in range(start, len(base)):
            x = h[base[i]]
            if x not in transv[i]: return h, i
            h = mulD(invD(transv[i][x]), h)
        return h, len(base)
    i = len(base) - 1
    while i >= 0:
        clean = True
        for x in list(transv[i].keys()):
            for g in lvl[i]:
                sg = mulD(invD(transv[i][g[x]]), mulD(g, transv[i][x]))
                if sg == E: continue
                h, j = strip_from(sg, i+1)
                if h != E:
                    clean = False
                    if j == len(base):
                        base.append(next(p for p in range(deg) if h[p] != p))
                        lvl.append([]); transv.append(None)
                    for k2 in range(i+1, j+1):
                        lvl[k2].append(h); rebuild(k2)
                    i = j
                    break
            if not clean: break
        if clean: i -= 1
    o = 1
    for T in transv: o *= len(T)
    return o

WE7 = 2903040
check("W(E7)", "the reflections generate a group of order 2903040 = |W(E7)| "
      "on the 56 weights", bsgs_order(list(S), N) == WE7)
# the antipode is the central -1
anti = tuple(idx[tuple(-x for x in verts[k])] for k in range(N))
check("iota = -1", "the data's iota IS the weight antipode, and it commutes "
      "with every reflection", list(anti) == IOTA and
      all(mul(s, anti) == mul(anti, s) for s in S))

# ---- the pair action (Sp6(2), degree 28)
def to28(p56):
    out = [0]*28
    for x in range(N): out[FRAME[x]] = FRAME[p56[x]]
    return tuple(out)
S28 = [to28(s) for s in S]
check("pair action", "reflections descend to the 28 iota-pairs; the "
      "quotient group is Sp6(2) of order 1451520",
      bsgs_order(S28, 28) == WE7 // 2)

# ---- hunt PSL(2,7): random word c of order 7 (on 28), then involution x
random.seed(728)
def rand_word(L=40):
    w56 = E56
    word = [random.randrange(7) for _ in range(L)]
    for i in word: w56 = mul(S[i], w56)
    return w56
def ord28(p56):
    p = to28(p56); k, x = 1, p
    while x != tuple(range(28)): x = tuple(x[p[j]] for j in range(28)); k += 1
    return k
c56 = None
for _ in range(4000):
    g = rand_word()
    o = ord28(g)
    if o % 7 == 0:
        c56 = g
        for _ in range(o // 7 - 1):
            pass
        # power down to order exactly 7 (on 28)
        e = o // 7
        h = E56
        for _ in range(e): h = mul(c56, h)
        c56 = h
        break
check("order-7", "an order-7 element found in the pair action", c56 is not None
      and ord28(c56) == 7)
c28 = to28(c56)
def orbits_of(gens, deg):
    seen = [False]*deg; out = []
    for s0 in range(deg):
        if seen[s0]: continue
        orb = {s0}; q = [s0]
        while q:
            x = q.pop()
            for g in gens:
                if g[x] not in orb: orb.add(g[x]); q.append(g[x])
        for t in orb: seen[t] = True
        out.append(sorted(orb))
    return out
L28 = None; x56 = None; other_class = None
tries = 0
for _ in range(200000):
    tries += 1
    g = rand_word(random.randrange(20, 60))
    o = ord28(g)
    if o % 2: continue
    h = E56
    for _ in range(o // 2): h = mul(g, h)
    x = h                                     # involution on 28 (maybe on 56)
    xc = to28(mul(x, c56))
    oxc = 1; t = xc
    while t != tuple(range(28)): t = tuple(t[xc[j]] for j in range(28)); oxc += 1
    if oxc not in (3, 4, 7): continue
    got = bsgs_order([to28(x), c28], 28)
    if got == 168:
        osz = [len(o_) for o_ in orbits_of([to28(x), c28], 28)]
        if osz == [28]:
            L28 = [to28(x), c28]; x56 = x
            break
        elif other_class is None:
            other_class = (x, sorted(osz))
check("PSL(2,7), bridge class", f"a copy TRANSITIVE on the 28 pairs found "
      f"(after {tries} candidates) — the bitangent class of T-BR",
      L28 is not None)
if other_class is not None:
    x2, osz2 = other_class
    g2 = [comm(x2, c56), comm(x2, mul(c56, c56)),
          comm(mul(x2, c56), mul(c56, x2))]
    o2 = bsgs_order(g2, N)
    orbs2 = sorted(len(o_) for o_ in orbits_of(g2, N)) if o2 == 168 else None
    check("BONUS: second class [obs]", "a SECOND conjugacy class of "
          f"PSL(2,7) found en route: 28-orbits {osz2}; its canonical lift "
          f"acts on the 56 with orbits {orbs2} — the crystal seen as FANO "
          "GEOMETRY doubled (perm char 4chi1+6chi6+2chi8: two point-"
          "actions + two flag-actions)", osz2 == [7, 21])

# ---- lift: kill the +-1 by taking the perfect part
H56 = [x56, c56]
oH = bsgs_order(H56, N)
gensK = [comm(x56, c56), comm(x56, mul(c56, c56)),
         comm(mul(x56, c56), mul(c56, x56)), comm(c56, mul(x56, mul(c56, x56)))]
oK = bsgs_order(gensK, N)
if oK != 168:      # add more commutators if needed
    for _ in range(20):
        a = gensK[random.randrange(len(gensK))]
        gensK.append(comm(a, mul(x56, c56)))
        oK = bsgs_order(gensK, N)
        if oK == 168: break
check("the lift", f"lift <x,c> to the 56 has order {oH} (= 168 or 336); its "
      "PERFECT part has order exactly 168 — the canonical PSL(2,7) x 1 "
      "inside W(E7) = 2 x Sp6(2)", oK == 168 and oH in (168, 336))

# enumerate all 168 elements of K
K = {E56}; frontier = [E56]
while frontier:
    nxt = []
    for a in frontier:
        for g in gensK:
            b = mul(g, a)
            if b not in K: K.add(b); nxt.append(b)
    frontier = nxt
check("enumeration", "the canonical copy enumerated: exactly 168 elements",
      len(K) == 168)

# ---- DQ-1: orbits on the 56 + the registered prediction
orbs56 = orbits_of(gensK, N)
sizes56 = sorted(len(o) for o in orbs56)
fixprof = Counter()
for g in K:
    o = order_of(g)
    fixprof[(o, sum(1 for k in range(N) if g[k] == k))] += 1
prof = sorted(fixprof.items())
print(f"  orbits on the 56: {sizes56}")
print(f"  (element order, #fixed weights) -> count: {prof}")
true_ok = (sizes56 == [28, 28] and
           fixprof.get((2, 8), 0) == 21 and fixprof.get((3, 2), 0) == 56 and
           fixprof.get((4, 0), 0) == 42 and fixprof.get((7, 0), 0) == 48)
o1 = set(orbs56[0])
iota_swaps = {IOTA[x] for x in o1} == set(orbs56[1])
check("DQ-1 ANSWERED", "the canonical PSL(2,7) has orbits [28, 28] on the "
      "56 — TWO bitangent sheets, interchanged by iota, weight-stabilizer "
      "S3.  The header's registered prediction (single 56-orbit, "
      "stabilizer Z3) is REFUTED — recorded per house rules",
      true_ok and iota_swaps,
      "the lift does NOT mix a pair's two weights: the +- doubling is "
      "equivariantly trivial")

# ---- coordinate-level sector theorem: decompose the permutation character
Hh = Fraction(1, 2)
TAB = [[(1,0)]*6,
       [(3,0),(-1,0),(0,0),(1,0),(-Hh,Hh),(-Hh,-Hh)],
       [(3,0),(-1,0),(0,0),(1,0),(-Hh,-Hh),(-Hh,Hh)],
       [(6,0),(2,0),(0,0),(0,0),(-1,0),(-1,0)],
       [(7,0),(-1,0),(1,0),(-1,0),(0,0),(0,0)],
       [(8,0),(0,0),(-1,0),(0,0),(1,0),(1,0)]]
sizes = {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}     # 7A+7B merged (real char)
fixby = {o: next(f for (oo, f), c in fixprof.items() if oo == o)
         for o in (1, 2, 3, 4, 7)}
mults = []
for r in range(6):
    tot = Fraction(0)
    vals = {1: TAB[r][0][0], 2: TAB[r][1][0], 3: TAB[r][2][0],
            4: TAB[r][3][0], 7: TAB[r][4][0] + TAB[r][5][0]}
    for o in (1, 2, 3, 4):
        tot += sizes[o] * fixby[o] * vals[o]
    tot += Fraction(sizes[7], 2) * fixby[7] * vals[7]
    m = tot / 168
    assert m.denominator == 1
    mults.append(int(m))
check("coordinate-level sectors [CORRECTION to SM-012]", "the TRUE field "
      "decomposition: C^56 = 2*(chi1 + 2chi6 + chi7 + chi8) = two copies "
      "of the bitangent module pi_28; the iota-odd half is ISOMORPHIC to "
      "the even half (both = pi_28).  Stone F(a)'s sign-twisted guess "
      "('quarks chirality-odd') is REFUTED for the Weyl-realized action: "
      "PSL(2,7) is perfect, so its lift into W(E7) = 2 x Sp6(2) is UNIQUE "
      "and untwisted — chi3/chi3bar do NOT occur in C^56 at all (the "
      "quark sectors of the 27 come from Lie-group embeddings, never from "
      "the Weyl action)", mults == [2, 0, 0, 4, 2, 2],
      f"multiplicities {mults}")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
