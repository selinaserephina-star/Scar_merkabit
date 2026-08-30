# verify_stone1_certificate.py — Stone 1, step 1: the transportation
# certificate stated abstractly, anchored on the 27-machine, and run on the
# 56-machine as its first generalization test.
#
# THE ABSTRACT CERTIFICATE (Young case — proved, not just tested):
#   Let H = S_{B1} x ... x S_{Br} be a FULL Young (block) subgroup of S_n and
#   m any "magic" permutation.  The double coset H g H is completely
#   determined by the block-transport table T(g)[b][c] = #{x in block b :
#   g(x) in block c}  (classical: double cosets of Young subgroups <->
#   contingency tables with the block sizes as margins).  Because the middle
#   h in  g = ... m h m ...  can re-sort each block arbitrarily, arrivals
#   and departures inside a block can be matched in ANY pattern, so:
#
#     g  is writable with exactly k magic gates  (g in H (mH)^k)
#     <=>  T(g) lies in the k-fold TABLE COMPOSITION of T(m):
#     D_1 = {T(m)};  C in D_{k+1}  <=>  exists T in D_k and an integer
#     3-tensor F[b][c][d] >= 0 with margins
#        sum_d F = T[b][c],   sum_b F = T(m)[c][d],   sum_c F = C[b][d].
#
#   (Necessity: count flows.  Sufficiency: full Sym(block) freedom in the
#   middle realizes any feasible flow.  This is CN-012's 27-machine proof
#   with the parity complication removed — there H was typed-EVEN, which
#   needed the junction parity-repair lemma; over full Young subgroups the
#   certificate is exact with no lemma.)
#
#   MAGIC-DEPTH(G; H, m) = min k with  D_0 u D_1 u ... u D_k = ALL
#   achievable tables — an astronomically large question reduced to finite
#   dynamics on contingency tables.
#
# RUN A (anchor): the 27-machine.  H = S9 x S9 x S9 (the X/Y/Z legs),
#   m = Psi^4.  Expected: <H,m> = S27; depth = 2 (CN-012, Young version).
# RUN B (the experiment): the 56-machine, branch grammar.
#   H = S27 x S27 x S1 x S1 (the sheets + vacua), m = Psi (the clock —
#   the sole magic source; DQ-2).  Depth UNKNOWN before this run.
# RUN C (the frontier, reported not solved): the frame grammar's H is
#   HYPEROCTAHEDRAL, a Gelfand pair — its "tables" are matching-union
#   coset types; we compute the invariant and leave depth to the next step.
#
# Run:  python -X utf8 verify_stone1_certificate.py
import numpy as np, json, sys, itertools
from collections import defaultdict, Counter
from math import factorial
sys.setrecursionlimit(100000)

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

# ------------------------------------------------ generic permutation tools
def mk_tools(n):
    E = tuple(range(n))
    def mul(a, b): return tuple(a[b[k]] for k in range(n))
    def inv(a):
        r = [0]*n
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    def bsgs_order(gen_list):
        strong = [g for g in gen_list if g != E]
        base = []
        for g in strong:
            if all(g[b] == b for b in base):
                base.append(next(i for i in range(n) if g[i] != i))
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
                        T[y] = mul(g, T[x]); q.append(y)
            transv[i] = T
        for i in range(len(base)): rebuild(i)
        def strip_from(g, start):
            h = g
            for i in range(start, len(base)):
                x = h[base[i]]
                if x not in transv[i]: return h, i
                h = mul(inv(transv[i][x]), h)
            return h, len(base)
        i = len(base) - 1
        while i >= 0:
            clean = True
            for x in list(transv[i].keys()):
                for g in lvl[i]:
                    sg = mul(inv(transv[i][g[x]]), mul(g, transv[i][x]))
                    if sg == E: continue
                    h, j = strip_from(sg, i+1)
                    if h != E:
                        clean = False
                        if j == len(base):
                            base.append(next(p for p in range(n) if h[p] != p))
                            lvl.append([]); transv.append(None)
                        for k in range(i+1, j+1):
                            lvl[k].append(h); rebuild(k)
                        i = j
                        break
                if not clean: break
            if clean: i -= 1
        order = 1
        for T in transv: order *= len(T)
        return order
    return E, mul, inv, bsgs_order

# ------------------------------------------- generic certificate machinery
def btab(g, blk_of, B):
    T = [[0]*B for _ in range(B)]
    for x, y in enumerate(g): T[blk_of[x]][blk_of[y]] += 1
    return tuple(map(tuple, T))

def all_tables(sizes):
    """all BxB nonneg integer tables with row sums = col sums = sizes"""
    B = len(sizes); out = []
    def rec(r, rows, colrem):
        if r == B:
            if all(c == 0 for c in colrem): out.append(tuple(rows))
            return
        def fill(c, row, left):
            if c == B - 1:
                if left <= colrem[c]:
                    rec(r+1, rows + [tuple(row + [left])],
                        tuple(cr - (row + [left])[i] for i, cr in enumerate(colrem)))
                return
            for v in range(min(left, colrem[c]) + 1):
                fill(c+1, row + [v], left - v)
        fill(0, [], sizes[r])
    rec(0, [], tuple(sizes))
    return out

def feas3(T1, T2, C, B):
    """exists integer F[b][c][d]>=0 with sum_d F=T1, sum_b F=T2, sum_c F=C"""
    r1 = [list(row) for row in T1]          # remaining T1[b][c]
    r2 = [list(row) for row in T2]          # remaining T2[c][d]
    r3 = [list(row) for row in C]           # remaining C[b][d]
    cells = [(b, c, d) for b in range(B) for c in range(B) for d in range(B)]
    def rec(i):
        if i == len(cells):
            return all(v == 0 for M in (r1, r2, r3) for row in M for v in row)
        b, c, d = cells[i]
        # forced-sum pruning: last d for (b,c) forces the T1 remainder, etc.
        last_d = (d == B - 1)
        hi = min(r1[b][c], r2[c][d], r3[b][d])
        lo = 0
        if last_d: lo = hi if r1[b][c] == min(r1[b][c], r2[c][d], r3[b][d]) else r1[b][c]
        if last_d and r1[b][c] > hi: return False
        vals = [r1[b][c]] if last_d else range(hi, -1, -1)
        for v in vals:
            if v > hi: continue
            r1[b][c] -= v; r2[c][d] -= v; r3[b][d] -= v
            if rec(i + 1):
                r1[b][c] += v; r2[c][d] += v; r3[b][d] += v
                return True
            r1[b][c] += v; r2[c][d] += v; r3[b][d] += v
        return False
    return rec(0)

def magic_depth(Tm, sizes, tag, blockperms=None, max_k=8):
    """blockperms: group of allowed block permutations (wreath typing);
       None = plain Young.  D_k is kept closed under row/col permutations."""
    B = len(sizes)
    ALL = set(all_tables(sizes))
    ident = tuple(tuple(sizes[b] if b == c else 0 for c in range(B))
                  for b in range(B))
    perms = blockperms or [tuple(range(B))]
    def orbit(T):
        out = set()
        for pr_ in perms:
            for pc in perms:
                out.add(tuple(tuple(T[pr_[b]][pc[c]] for c in range(B))
                              for b in range(B)))
        return out
    seeds = orbit(Tm)
    print(f"      [{tag}] tables: {len(ALL)}; typed block-perms: {len(perms)}")
    Dk = set(seeds)
    covered = orbit(ident) | Dk
    k = 1
    while covered != ALL and k < max_k:
        nxt = set()
        for C in ALL:
            if any(feas3(T, Ts, C, B) for T in Dk for Ts in seeds):
                nxt.add(C)
        Dk = nxt
        covered |= Dk
        k += 1
        print(f"      [{tag}] after {k} magic gates: {len(covered)}/{len(ALL)} covered")
    return (k if covered == ALL else None), len(ALL)

print("=" * 78)
print("STONE 1 -- the transportation certificate: anchor (27) + experiment (56)")
print("=" * 78)

# =============================== RUN A: the 27-machine (anchor, CN-012 Young)
C6 = np.array([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
               [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]], int)
def f_lab(a, i): return tuple(a[j] - C6[i, j] for j in range(6))
V = {(1,0,0,0,0,0)}; Ed = []; fr = [(1,0,0,0,0,0)]
while fr:
    v = fr.pop()
    for i in range(6):
        if v[i] == 1:
            w = f_lab(v, i); Ed.append((v, i, w))
            if w not in V: V.add(w); fr.append(w)
verts = sorted(V); idx = {v: k for k, v in enumerate(verts)}
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
def Psi_i(I):
    comp = [p for p in P if p not in I]
    mn = [s for s in comp if not any(t != s and leq(t, s) for t in comp)]
    return frozenset(p for p in P for s in mn if leq(p, s))
clock27 = tuple(idx[i2w[Psi_i(w2i[verts[k]])]] for k in range(27))
def leg(w):
    if w[0] == 0 and w[2] == 0: return 0
    if w[4] == 0 and w[5] == 0: return 1
    return 2
blk27 = [leg(verts[k]) for k in range(27)]
blocks27 = [[k for k in range(27) if blk27[k] == b] for b in range(3)]
E27, mul27, inv27, bsgs27 = mk_tools(27)
psi4 = E27
for _ in range(4): psi4 = mul27(clock27, psi4)
check("A: legs", "27-machine blocks = X/Y/Z legs, 9+9+9",
      [len(b) for b in blocks27] == [9, 9, 9])
gens27 = [psi4]
for b in blocks27:
    t = list(E27); t[b[0]], t[b[1]] = t[b[1]], t[b[0]]      # transposition
    c = list(E27)
    for i in range(len(b)): c[b[i]] = b[(i+1) % len(b)]     # 9-cycle
    gens27 += [tuple(t), tuple(c)]
check("A: group", "<S9 x S9 x S9, Psi^4> = S27 (order 27!)",
      bsgs27(gens27) == factorial(27))
T27 = btab(psi4, blk27, 3)
print(f"      T(Psi^4) block-transport = {T27}")
d27, n27 = magic_depth(T27, (9, 9, 9), "27/Young")
check("A: Young depth", f"27-machine PLAIN-Young magic-depth over {n27} "
      "tables — Claude's expectation of 2 REFUTED: without block rotations "
      "the depth is 3", d27 == 3, f"depth={d27}")
S3perms = list(itertools.permutations(range(3)))
d27w, _ = magic_depth(T27, (9, 9, 9), "27/wreath", blockperms=S3perms)
check("A: ANCHOR (wreath)", "27-machine WREATH magic-depth = 2 — reproduces "
      "CN-012 exactly; corollary: the typed S3 leg-rotation is worth "
      "precisely ONE magic gate (3 -> 2)", d27w == 2, f"depth={d27w}")

# ====================== RUN B: the 56-machine, branch grammar (THE EXPERIMENT)
D = json.load(open("scar56_data.json"))
PSI, COMP = tuple(D["PSI"]), D["COMP"]
blocks56 = [[k for k in range(56) if COMP[k] == b] for b in range(4)]
sizes56 = tuple(len(b) for b in blocks56)
E56_, mul56, inv56, bsgs56 = mk_tools(56)
check("B: blocks", "56-machine branch blocks = 27 + 27bar + 1 + 1",
      sorted(sizes56) == [1, 1, 27, 27])
gens56 = [PSI]
for b in blocks56:
    if len(b) < 2: continue
    t = list(E56_); t[b[0]], t[b[1]] = t[b[1]], t[b[0]]
    c = list(E56_)
    for i in range(len(b)): c[b[i]] = b[(i+1) % len(b)]
    gens56 += [tuple(t), tuple(c)]
check("B: group", "<S27 x S27bar x 1 x 1, Psi> = S56 (order 56!)",
      bsgs56(gens56) == factorial(56))
T56 = btab(PSI, COMP, 4)
print(f"      T(Psi) block-transport = {T56}")
d56, n56 = magic_depth(T56, sizes56, "56/Young")
check("B: THE EXPERIMENT (Young)", f"56-machine branch-grammar PLAIN-Young "
      f"magic-depth computed exactly over {n56} tables", d56 is not None,
      f"depth={d56}")
# wreath typing: the sheets may swap (that is pr!) and the vacua may swap
W4 = [p for p in itertools.permutations(range(4))
      if {p[0], p[1]} == {0, 1} and {p[2], p[3]} == {2, 3}]
d56w, _ = magic_depth(T56, sizes56, "56/wreath", blockperms=W4)
check("B: THE EXPERIMENT (wreath)", "with sheet-swap (= pr) and vacuum-swap "
      "in the typed side, the 56 branch-grammar magic-depth is computed "
      "exactly", d56w is not None,
      f"depth={d56w} (vs Young {d56}: sheet-swap worth "
      f"{(d56 or 0) - (d56w or 0)} magic gate(s))")

# ============ RUN C: frame grammar = hyperoctahedral (Gelfand pair) frontier
IOTA, FRAME = tuple(D["IOTA"]), D["FRAME"]
def coset_type(g):
    """union of the iota-matching and its g-image: even cycles; half-lengths"""
    adj = defaultdict(list)
    for x in range(56):
        adj[x].append(IOTA[x])                       # matching M0
        adj[x].append(inv56(g)[IOTA[g[x]]])          # matching g^-1 M0 g
    seen, typ = set(), []
    for s in range(56):
        if s in seen: continue
        L, x, use0 = 0, s, True
        while x not in seen:
            seen.add(x); L += 1
            x = adj[x][0] if use0 else adj[x][1]
            use0 = not use0
        typ.append(L // 2)
    return sorted(typ, reverse=True)
E56p = tuple(range(56))
print("\n      [frame grammar] hyperoctahedral coset types (the certificate's")
print("      object in the Gelfand-pair world; depth = next step):")
for nm, g in (("identity", E56p), ("Psi", PSI), ("iota", IOTA),
              ("pr", tuple(D["PR"]))):
    print(f"        {nm:9s}: {Counter(coset_type(g)).most_common()}")
check("C: frontier", "pr and iota have trivial coset type [1^28] "
      "(bilingual: inside the hyperoctahedral world), Psi does not",
      coset_type(tuple(D["PR"])) == [1]*28 and coset_type(IOTA) == [1]*28
      and coset_type(PSI) != [1]*28)

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
