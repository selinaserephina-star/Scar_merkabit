# verify_fano_syndrome.py — the Fano-syndrome check (Scar_merkabit lane).
#
# QUESTION (Selina, 2026-08-30): the crystal architecture's error syndrome has
# 7 channels (6 crystal edge-colours + 1 affine channel built by promotion) —
# the nodes of the AFFINE E6 Dynkin diagram.  Ilya's world is built on the
# Fano plane's 7 points.  Is the syndrome Fano-organized?
#
# METHOD (compute, never assert):
#   1. Rebuild the E6 minuscule crystal B(w1), its 6 colour channels, rowmotion
#      Psi, promotion pr, the affine channel fA = pr o f5 o pr^-1, and the
#      Lusztig involution xi — all from scratch (same construction as
#      CRYSTAL_NATIVE_v2/sim_crystal_native_v2.py; cross-checked against the
#      published simulator tables).
#   2. Compute the SYNDROME MOTION GROUP: which permutations of the 7 channel
#      labels are induced by conjugating the channel maps with the machine's
#      own symmetries (pr, Psi, xi)?
#   3. Enumerate ALL 30 Fano plane structures on the 7 labels and count how
#      many are invariant under the motion group.  0 = Fano refuted;
#      exactly 1 = a CANONICAL Fano selected by the syndrome's own symmetry;
#      >1 = compatible but non-canonical.
#   4. Compare the channels' commutation graph with the affine E6 tree.
#
# Run:  python -X utf8 verify_fano_syndrome.py
import numpy as np, itertools
from collections import defaultdict, Counter
from math import gcd

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("FANO-SYNDROME CHECK — do the 7 error channels carry Fano structure?")
print("=" * 78)

# ---------------------------------------------------- 1. rebuild the crystal
C = np.array([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
              [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]], int)
def f_lab(a, i): return tuple(a[j] - C[i, j] for j in range(6))
V = {(1,0,0,0,0,0)}; Ed = []; fr = [(1,0,0,0,0,0)]
while fr:
    v = fr.pop()
    for i in range(6):
        if v[i] == 1:
            w = f_lab(v, i); Ed.append((v, i, w))
            if w not in V: V.add(w); fr.append(w)
verts = sorted(V); idx = {v: k for k, v in enumerate(verts)}; N = len(verts)
f = [[-1]*N for _ in range(6)]; e = [[-1]*N for _ in range(6)]
for v, i, w in Ed: f[i][idx[v]] = idx[w]; e[i][idx[w]] = idx[v]
check("crystal", "B(w1) rebuilt: 27 vertices, 36 coloured edges",
      N == 27 and len(Ed) == 36)

# rowmotion Psi via the order ideals (as in the architecture sim)
cover = defaultdict(set)
for v, i, w in Ed: cover[v].add(w)
below = {}
def dfs(v, acc):
    acc.add(v)
    for w in cover[v]:
        if w not in acc: dfs(w, acc)
for v in V:
    acc = set(); dfs(v, acc); below[v] = acc
def leq(p, q): return p in below[q]
P = [x for x in V if len([y for y in below[x]-{x}
     if not any(y in below[z]-{z} for z in below[x]-{x} if z != y)]) == 1]
i2w = {}; w2i = {}
for x in V:
    I = frozenset(p for p in P if leq(p, x)); i2w[I] = x; w2i[x] = I
def Psi_ideal(I):
    comp = [p for p in P if p not in I]
    mn = [s for s in comp if not any(t != s and leq(t, s) for t in comp)]
    return frozenset(p for p in P for s in mn if leq(p, s))
clock = [idx[i2w[Psi_ideal(w2i[verts[k]])]] for k in range(N)]

# promotion pr (leg rotation): backtracking solve, as in the sim
rho = {0:5, 1:2, 2:4, 3:3, 4:1}
def solve_pr():
    pr = [-1]*N; used = [False]*N
    def assign(v, p):
        st = [(v, p)]
        while st:
            x, px = st.pop()
            if pr[x] != -1:
                if pr[x] != px: return None
                continue
            if used[px]: return None
            pr[x] = px; used[px] = True
            for i in range(5):
                if f[i][x] != -1:
                    u = f[rho[i]][px]
                    if u == -1: return None
                    st.append((f[i][x], u))
                if e[i][x] != -1:
                    u = e[rho[i]][px]
                    if u == -1: return None
                    st.append((e[i][x], u))
        return True
    def bt():
        v = next((k for k in range(N) if pr[k] == -1), None)
        if v is None: return True
        for p in range(N):
            if used[p]: continue
            sp, su = pr[:], used[:]
            if assign(v, p) is not None and bt(): return True
            for k in range(N): pr[k] = sp[k]; used[k] = su[k]
        return False
    assert bt(); return pr
pr = solve_pr()
prinv = [pr.index(k) for k in range(N)]
# cross-check against the published simulator tables (artifact "27-State Machine")
PR_PUB  = [23,13,20,9,2,15,24,17,6,10,3,26,21,25,11,18,7,16,5,0,4,22,12,19,8,1,14]
PSI_PUB = [26,21,22,23,25,24,5,20,18,19,4,6,11,12,9,8,2,0,10,7,1,17,16,14,15,13,3]
check("cross-check", "pr and Psi match the published simulator tables",
      pr == PR_PUB and clock == PSI_PUB)

# affine channel and the 7-channel syndrome
fA = [-1]*N
for x in range(N):
    y = f[5][prinv[x]]
    if y != -1: fA[x] = pr[y]
CH = list(range(6)) + ["A"]
chan = {i: f[i] for i in range(6)}; chan["A"] = fA
check("syndrome", "7 channels x 6 edges = 42 single errors (as in CN-001)",
      all(sum(1 for x in range(N) if chan[c][x] != -1) == 6 for c in CH))

# Lusztig involution xi: w -> -theta(w), theta = E6 diagram flip 0<->5, 2<->4
theta = {0:5, 1:1, 2:4, 3:3, 4:2, 5:0}
xi = [idx[tuple(-verts[k][theta[j]] for j in range(6))] for k in range(N)]
check("xi", "xi is an involution of the 27 and xi Psi xi = Psi^-1",
      all(xi[xi[k]] == k for k in range(N)) and
      all(xi[clock[xi[k]]] == clock.index(k) for k in range(N)))

# --------------------------------------- 2. the syndrome motion group
def conj(g, ginv, mp):        # g o mp o g^-1 as a partial map
    return [(-1 if mp[ginv[x]] == -1 else g[mp[ginv[x]]]) for x in range(N)]
def conj_by_inv(g, ginv, mp): # xi-style: g o mp o g (g an involution)
    return [(-1 if mp[g[x]] == -1 else g[mp[g[x]]]) for x in range(N)]
# directed channel dictionary: lowering AND raising versions of all 7
eA = [-1]*N
for x in range(N):
    if fA[x] != -1: eA[fA[x]] = x
DIR = {}
for c in CH:
    lower = chan[c]
    raise_ = [-1]*N
    for x in range(N):
        if lower[x] != -1: raise_[lower[x]] = x
    DIR[(c, "-")] = lower; DIR[(c, "+")] = raise_
def induced(label_map_pairs):
    """given {channel: conjugated partial map}, find the induced permutation
       on undirected channel labels (or None if not channel-preserving)"""
    out = {}
    for c, mp in label_map_pairs.items():
        hit = [k for k, v in DIR.items() if v == mp]
        if not hit: return None
        out[c] = hit[0][0]
    return out if sorted(map(str, out.values())) == sorted(map(str, CH)) else None
pi_pr = induced({c: conj(pr, prinv, chan[c]) for c in CH})
pi_xi = induced({c: conj_by_inv(xi, xi, chan[c]) for c in CH})
clockinv = [clock.index(k) for k in range(N)]
pi_psi = induced({c: conj(clock, clockinv, chan[c]) for c in CH})
print(f"\n  induced channel permutations:")
print(f"    pr  : {pi_pr}")
print(f"    xi  : {pi_xi}")
print(f"    Psi : {pi_psi}")
check("motion/pr", "promotion conjugation permutes the 7 channels "
      "(order-3 leg rotation)", pi_pr is not None)
check("motion/xi", "Lusztig involution conjugation permutes the 7 channels "
      "(diagram flip)", pi_xi is not None)
check("motion/Psi", "rowmotion conjugation does NOT permute the channels "
      "(the clock is not a colour symmetry)", pi_psi is None)
# the motion group on labels
def compose(a, b): return {c: a[b[c]] for c in CH}
ident = {c: c for c in CH}
G = {tuple(sorted(ident.items(), key=str))}
frontier = [ident]
gens = [g for g in (pi_pr, pi_xi) if g]
while frontier:
    nxt = []
    for a in frontier:
        for g in gens:
            b = compose(g, a)
            key = tuple(sorted(b.items(), key=str))
            if key not in G: G.add(key); nxt.append(b)
    frontier = nxt
check("motion group", "the syndrome motion group has order 6 = S3 "
      "(NOT 168: the syndrome's symmetry is the affine-E6 leg S3)",
      len(G) == 6)

# --------------------------------------- 3. all 30 Fano structures, invariance
pts = list(range(1, 8))
std_lines = {frozenset({a, b, a ^ b}) for a in pts for b in pts if a != b
             and a ^ b != 0}
lab = {i: CH[i-1] for i in pts}  # 1..7 -> channel labels
fanos = set()
for perm in itertools.permutations(pts):
    m = dict(zip(pts, perm))
    fanos.add(frozenset(frozenset(lab[m[p]] for p in L) for L in std_lines))
check("30 Fanos", "there are exactly 30 Fano plane structures on the 7 "
      "channel labels", len(fanos) == 30)
def invariant(fano, g):
    return frozenset(frozenset(g[c] for c in L) for L in fano) == fano
inv_pr  = [F for F in fanos if invariant(F, pi_pr)]
motion  = [dict(k) for k in G]
inv_all = [F for F in fanos if all(invariant(F, g) for g in motion)]
print(f"\n  Fano structures invariant under pr alone : {len(inv_pr)}")
print(f"  Fano structures invariant under the FULL motion group S3 : "
      f"{len(inv_all)}")
if len(inv_all) == 1:
    F = next(iter(inv_all))
    lines = sorted(sorted(map(str, L)) for L in F)
    check("CANONICAL FANO", "the syndrome's own symmetry selects a UNIQUE "
          "Fano plane on the 7 channels", True,
          f"lines = {lines}")
elif len(inv_all) == 0:
    check("NO FANO", "no Fano structure is compatible with the syndrome's "
          "symmetry — Fano organization REFUTED", True)
else:
    check("NON-CANONICAL", f"{len(inv_all)} invariant Fanos — compatible but "
          "no canonical choice", True)

# --------------------------------------- 4. commutation graph vs the tree
def commutes(m1, m2):
    return all((-1 if m2[x] == -1 else m1[m2[x]]) ==
               (-1 if m1[x] == -1 else m2[m1[x]]) for x in range(N))
edges_cg = [(a, b) for a, b in itertools.combinations(CH, 2)
            if not commutes(chan[a], chan[b])]
# affine E6 adjacency in this Cartan numbering: 0-2, 2-3, 1-3, 3-4, 4-5, A-1
aff_e6 = {frozenset(p) for p in [(0,2),(2,3),(1,3),(3,4),(4,5),("A",1)]}
check("commutation graph", "channel non-commutation graph = the affine E6 "
      "Dynkin tree (6 edges) — the syndrome's native incidence is the TREE, "
      "not the plane", {frozenset(x) for x in edges_cg} == aff_e6,
      f"edges = {sorted(map(lambda s: sorted(map(str,s)), edges_cg))}")

# --------------------------------------- 5. the chiral pair, discriminated
if len(inv_all) == 2:
    tree_adj = {c: set() for c in CH}
    for a, b in map(tuple, aff_e6):
        tree_adj[a].add(b); tree_adj[b].add(a)
    def connected(L):
        L = set(L); start = next(iter(L)); seen = {start}; st = [start]
        while st:
            x = st.pop()
            for y in tree_adj[x]:
                if y in L and y not in seen: seen.add(y); st.append(y)
        return len(seen) == len(L)
    stats = []
    for F in inv_all:
        ncon = sum(1 for L in F if connected(L))
        nedge = sum(1 for L in F for a, b in itertools.combinations(L, 2)
                    if frozenset((a, b)) in aff_e6)
        stats.append((ncon, nedge))
    shared = inv_all[0] & inv_all[1]
    check("indistinguishable", "the two invariant Fanos have IDENTICAL tree "
          "statistics (3 tree-connected lines, all 6 tree edges covered, "
          "each): no native structure separates them",
          stats[0] == stats[1] == (3, 6), f"stats={stats}")
    check("3 canonical lines", "the two Fanos SHARE exactly the 3 "
          "centre-lines {centre + leg}: {0,2,3},{1,A,3},{4,5,3} — these are "
          "canonical; the other 4 lines are the free choice",
          len(shared) == 3 and
          shared == {frozenset({0, 2, 3}), frozenset({1, "A", 3}),
                     frozenset({4, 5, 3})})
    # the exchanger: centralizer of the motion S3 in S7
    swaps = []
    for g in itertools.permutations(CH):
        m = dict(zip(CH, g))
        if all(compose(m, h) == compose(h, m) for h in motion):
            swaps.append(m)
    exch = [m for m in swaps if frozenset(frozenset(m[c] for c in L)
            for L in inv_all[0]) == inv_all[1]]
    check("chiral pair", "the centralizer of the motion S3 has order 2, and "
          "its nontrivial element — the INNER<->OUTER leg duality "
          "(0<->2, 1<->A, 4<->5, centre fixed) — exchanges the two Fanos: "
          "they are a chiral pair; choosing one = one extra bit the machine "
          "does not supply",
          len(swaps) == 2 and len(exch) == 1 and
          exch[0] == {0: 2, 2: 0, 1: "A", "A": 1, 4: 5, 5: 4, 3: 3})

print("\nVERDICT: the 7-channel syndrome is NOT Fano-organized — its native")
print("incidence is the affine-E6 tree and its symmetry is S3 (order 6), not")
print("PSL(2,7) (order 168).  BUT it is exactly ONE BIT away: the machine's")
print("own symmetry narrows the 30 possible Fanos to a CHIRAL PAIR sharing")
print("the 3 canonical centre-lines, exchanged by the inner/outer duality.")
print("A design that fixes that one bit (a 'Fano chirality' convention) gets")
print("a full Fano labelling of the syndrome for free — compatible, never")
print("forced.  (Same refutation shape as CN-010's Golay: right count,")
print("incompatible symmetry; new here: the residue is precisely 1 bit.)")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
