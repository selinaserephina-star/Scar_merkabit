# verify_dq6_resurrection.py — DQ-6: does the dual-27 intuition resurrect on
# the E7 minuscule 56?
#
# CLAIM TO TEST (Claude's, 2026-08-30): under the E6-branching of the E7
# minuscule crystal (delete colour-6 edges), the 56 splits as 27 + 27bar +
# 1 + 1, and the odd diagram gate pr (cycle type 1^2 2^27) has EXACTLY the
# two singlets as its fixed points, with its 27 transpositions pairing the
# 27 with the 27bar — i.e. v1's dual-spinor picture (two counter-posed 27s
# exchanged by an involution), REFUTED as a description of the E6 crystal
# (Thm 3.3 / the two-27s), is TRUE one floor up.
#
# Also computed: the antipode iota's behaviour on components, the 28-frame
# structure (iota-pairs), rowmotion's component mixing, and the simulator
# data dump (scar56_data.json).
#
# Run:  python -X utf8 verify_dq6_resurrection.py
import numpy as np, sys, json
from collections import defaultdict, Counter
sys.setrecursionlimit(100000)

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("DQ-6  the resurrection question: 56 = 27 + 27bar + 1 + 1 vs the odd pr")
print("=" * 78)

# ------------------------------------------------ E7 minuscule crystal (56)
n = 7
C = np.array([
 [ 2, 0,-1, 0, 0, 0, 0],
 [ 0, 2, 0,-1, 0, 0, 0],
 [-1, 0, 2,-1, 0, 0, 0],
 [ 0,-1,-1, 2,-1, 0, 0],
 [ 0, 0, 0,-1, 2,-1, 0],
 [ 0, 0, 0, 0,-1, 2,-1],
 [ 0, 0, 0, 0, 0,-1, 2]], dtype=int)
def f_i(a, i): return tuple(a[j] - C[i, j] for j in range(n))
hw = (0, 0, 0, 0, 0, 0, 1)
V = {hw}; Ed = []; fr = [hw]
while fr:
    v = fr.pop()
    for i in range(n):
        if v[i] == 1:
            w = f_i(v, i); Ed.append((v, i, w))
            if w not in V: V.add(w); fr.append(w)
verts = sorted(V); idx = {v: k for k, v in enumerate(verts)}; N = len(verts)
f = [[-1]*N for _ in range(n)]; e = [[-1]*N for _ in range(n)]
for v, i, w in Ed: f[i][idx[v]] = idx[w]; e[i][idx[w]] = idx[v]
check("crystal", "E7 minuscule: 56 vertices", N == 56)

# rowmotion Psi via order ideals (as in the sealed E7 thread)
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
psi = [idx[i2w[Psi_ideal(w2i[verts[k]])]] for k in range(N)]
def ctype(perm):
    seen = [False]*N; out = Counter()
    for s in range(N):
        if seen[s]: continue
        L, x = 0, s
        while not seen[x]: seen[x] = True; L += 1; x = perm[x]
        out[L] += 1
    return sorted(out.items())
check("Psi", "rowmotion order 18, orbit type [18,18,18,2]",
      ctype(psi) == [(2, 1), (18, 3)])

# pr: the sealed E7-thread involution (intertwines colours 0..5 by E6 flip)
rho = {0: 5, 1: 1, 2: 4, 3: 3, 4: 2, 5: 0}
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
            for i in range(6):
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
check("pr", "the diagram gate: involution of cycle type 1^2 2^27 (ODD)",
      ctype(pr) == [(1, 2), (2, 27)] and
      all(pr[pr[k]] == k for k in range(N)))

# the antipode iota: w -> -w
iota = [idx[tuple(-verts[k][j] for j in range(n))] for k in range(N)]
check("iota", "antipode w -> -w: fixed-point-free involution (28 pairs)",
      ctype(iota) == [(2, 28)])

# ------------------------------------------ the E6 branching: delete colour 6
comp_of = [-1]*N
ncomp = 0
for s in range(N):
    if comp_of[s] >= 0: continue
    stack = [s]; comp_of[s] = ncomp
    while stack:
        x = stack.pop()
        for i in range(6):
            for y in (f[i][x], e[i][x]):
                if y != -1 and comp_of[y] < 0:
                    comp_of[y] = ncomp; stack.append(y)
    ncomp += 1
sizes = Counter(comp_of)
comp_sizes = sorted(sizes.values())
check("branching", "deleting colour-6 edges splits the 56 into components "
      "of sizes [1,1,27,27]  (56 = 27 + 27bar + 1 + 1 under E6)",
      comp_sizes == [1, 1, 27, 27], f"sizes={comp_sizes}")
big = [c for c in sizes if sizes[c] == 27]
small = [c for c in sizes if sizes[c] == 1]
A, B = big[0], big[1]
S1, S2 = small[0], small[1]
# name check: each 27-component is an E6 crystal: 36 edges, 6 per colour
for tag, comp in (("27A", A), ("27B", B)):
    ecount = Counter()
    for x in range(N):
        if comp_of[x] != comp: continue
        for i in range(6):
            if f[i][x] != -1: ecount[i] += 1
    check(f"{tag} structure", f"component is an E6-crystal candidate: "
          f"36 coloured edges, 6 per colour",
          sum(ecount.values()) == 36 and all(ecount[i] == 6 for i in range(6)))

# ---------------------------------------------------- THE RESURRECTION TEST
fixed_pr = [k for k in range(N) if pr[k] == k]
check("DQ-6a", "pr's two fixed points ARE the two singlet components",
      sorted(comp_of[k] for k in fixed_pr) == sorted([S1, S2]),
      f"fixed={fixed_pr}, components={[comp_of[k] for k in fixed_pr]}")
cross = sum(1 for k in range(N)
            if comp_of[k] == A and comp_of[pr[k]] == B)
check("DQ-6b", "ALL 27 transpositions of pr pair the 27 with the 27bar "
      "(27 cross-pairs, zero internal)",
      cross == 27 and
      all(comp_of[pr[k]] == B for k in range(N) if comp_of[k] == A) and
      all(comp_of[pr[k]] == A for k in range(N) if comp_of[k] == B))
# duality: is B the weight-dual of A? (weights of B = negated E6-weights of A
# up to the colour flip — test via iota and via lowest/highest structure)
iota_AB = all(comp_of[iota[k]] == B for k in range(N) if comp_of[k] == A)
iota_S = sorted(comp_of[iota[k]] for k in fixed_pr) if False else None
check("DQ-6c", "the antipode iota ALSO maps 27A onto 27B (and swaps the two "
      "singlets): the second component is the DUAL 27bar in the weight sense",
      iota_AB and comp_of[iota[[k for k in range(N) if comp_of[k]==S1][0]]] == S2)
# pr vs iota give DIFFERENT 27<->27bar pairings?
pair_pr = {frozenset((k, pr[k])) for k in range(N) if comp_of[k] == A}
pair_io = {frozenset((k, iota[k])) for k in range(N) if comp_of[k] == A}
print(f"      pr-pairing vs iota-pairing of the two 27s: "
      f"{len(pair_pr & pair_io)}/27 shared "
      f"(two distinct dualities between the sheets)")
# rowmotion mixes the components (the clock is E7-native, not E6-blocked)
mix = any(comp_of[psi[k]] != comp_of[k] for k in range(N))
check("DQ-6d", "rowmotion does NOT preserve the branching (the clock runs "
      "across the 27/27bar wall — dynamics is genuinely E7)", mix)

# ---------------------------------------------------- frames & chirality
frame_of = [-1]*N; sign_of = [0]*N
fidx = 0
for k in range(N):
    if frame_of[k] >= 0: continue
    frame_of[k] = frame_of[iota[k]] = fidx
    sign_of[k] = +1; sign_of[iota[k]] = -1
    fidx += 1
cross_frames = sum(1 for k in range(N)
                   if comp_of[k] == A and comp_of[iota[k]] == B)
check("frames", "28 iota-frames: 27 straddle the two 27s + 1 = the singlet "
      "pair (the vacuum frame)", fidx == 28 and cross_frames == 27)

# CSP census for the simulator
fixp = []
for d in range(18):
    x = list(range(N))
    for _ in range(d):
        x = [psi[t] for t in x]
    fixp.append(sum(1 for k in range(N) if x[k] == k))

# ---------------------------------------------------- data dump for artifact
data = {
    "verts": [list(map(int, v)) for v in verts],
    "PSI": list(map(int, psi)), "PR": list(map(int, pr)),
    "IOTA": list(map(int, iota)),
    "COMP": [int(("AB".index("A") if c == A else 1 if c == B else 2
                  if c == S1 else 3)) for c in comp_of],
    "FRAME": list(map(int, frame_of)), "SIGN": list(map(int, sign_of)),
    "FIX": fixp,
    "EDGES": [[int(idx[v]), int(i), int(idx[w])] for v, i, w in Ed],
}
with open("scar56_data.json", "w", encoding="utf-8") as fh:
    json.dump(data, fh)
print(f"\n  simulator data written: scar56_data.json "
      f"({len(data['EDGES'])} edges, CSP fix profile {fixp})")

print("\nVERDICT: " + ("THE RESURRECTION THEOREM HOLDS — v1's dual-spinor "
      "picture (two counter-posed 27s exchanged by an involution, with a "
      "2-element pivot) is TRUE one floor up: it is the E6-branching of the "
      "E7 minuscule 56, with the odd gate pr as the exchange and the two "
      "singlets as the pivot. Refuted at E6 (Thm 3.3), true at E7."
      if FAIL == 0 else
      "the resurrection claim FAILED somewhere above — read the FAIL lines; "
      "the refutation stands at both levels."))
print("=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
