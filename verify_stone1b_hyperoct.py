# verify_stone1b_hyperoct.py — Stone 1, step 2: the HYPEROCTAHEDRAL
# composition calculus (frame-grammar analogue of the transportation
# certificate).  v2 — v1 had a doubled-type bug (mtype counted both product
# cycles per union cycle) and a canonical-base assumption in the partner
# constructor; both fixed, and v1's triangle-law GUESS is retired in favour
# of mining the exact law from clean data.  The guess's fate is recorded in
# STONE1B doc per house rules.
#
# SETTING.  H = stabiliser of a perfect matching M0 on 2n points (56-machine:
# the 28 iota-pairs).  Gelfand pair (S_2n, B_n): double coset of g <-> the
# COSET TYPE type(M0, gM0) = partition of n (half-lengths of the cycles of
# the union M0 u gM0).  One magic step:
#     mu reachable from lambda  <=>  exist M1 (type(M0,M1)=lambda) and M2
#     (type(M1,M2)=tau(m)) with type(M0,M2)=mu
# — well-defined on types because Stab(M0) is transitive on matchings of a
# given type from M0 (classical).
#
# PLAN: (1) exact support tables n=4..7 by exhaustion; (2) LAW MINING from
# the clean tables (is support metric-only? an interval in d = n-#parts?);
# (3) ground-truth validation at n=5: matching-BFS depth == table-closure
# depth; (4) the 56: tau(Psi) = [9,9,9,1]; theorem by WITNESSES — explicit,
# verified depth-2 constructions for every one of the p(28)=3718 coset types
# (sampling + targeted annealing; every found witness is exact).
#
# Run:  python -X utf8 verify_stone1b_hyperoct.py
import json, random, sys
from collections import defaultdict, Counter

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

# ------------------------------------------------------- matching utilities
def mtype(A, B):
    """union type: partition of n (each union cycle counted ONCE)"""
    N2 = len(A); seen = [False]*N2; parts = []
    for s in range(N2):
        if seen[s]: continue
        L, x = 0, s
        cyc = []
        while not seen[x]:
            seen[x] = True; cyc.append(x); L += 1
            x = B[A[x]]
        for y in cyc: seen[A[y]] = True        # partner product-cycle
        parts.append(L)
    parts.sort(reverse=True)
    return tuple(parts)
def pairs_of(M):
    out, seen = [], set()
    for x in range(len(M)):
        if x in seen: continue
        seen.add(x); seen.add(M[x]); out.append((x, M[x]))
    return out
def partner_of_type(baseM, parts):
    """matching whose union with baseM has the given type (any base)"""
    prs = pairs_of(baseM); M = [0]*len(baseM); p = 0
    for k in parts:
        ch = prs[p:p+k]; p += k
        for j in range(k):
            a2 = ch[(j+1) % k][0]; b1 = ch[j][1]
            M[b1], M[a2] = a2, b1
    return M
def canon0(n):
    m = list(range(2*n))
    for i in range(n): m[2*i], m[2*i+1] = 2*i+1, 2*i
    return m
def all_matchings(pts):
    if not pts: yield []; return
    a = pts[0]
    for i in range(1, len(pts)):
        rest = pts[1:i] + pts[i+1:]
        for sub in all_matchings(rest): yield [(a, pts[i])] + sub
def to_inv(pairs, N2):
    m = [0]*N2
    for a, b in pairs: m[a], m[b] = b, a
    return m
def d(parts, n): return n - len(parts)
def partitions(n):
    out = []
    def gp(rem, mx, cur):
        if rem == 0: out.append(tuple(cur)); return
        for k in range(min(rem, mx), 0, -1): gp(rem-k, k, cur+[k])
    gp(n, n, [])
    return out

print("=" * 78)
print("STONE 1b (v2) -- the hyperoctahedral composition calculus")
print("=" * 78)

# sanity for the fixed utilities
M0t = canon0(4)
check("utils", "mtype(M0,M0) = [1,1,1,1]; partner realizes every type "
      "(n=4, both checked exhaustively)",
      mtype(M0t, M0t) == (1, 1, 1, 1) and
      all(mtype(M0t, partner_of_type(M0t, lam)) == lam
          for lam in partitions(4)))

# ---------------------- (1) exact support tables + (2) law mining, n = 4..7
SUP = {}
for n in (4, 5, 6, 7):
    N2 = 2*n; M0 = canon0(n); pn = partitions(n)
    Ms = [to_inv(p, N2) for p in all_matchings(list(range(N2)))]
    sup = {lam: defaultdict(set) for lam in pn}
    for lam in pn:
        M1 = partner_of_type(M0, lam)
        for M2 in Ms:
            sup[lam][mtype(M1, M2)].add(mtype(M0, M2))
    SUP[n] = sup
    # mining: (a) triangle necessity; (b) is support an EXACT d-interval?
    tri_needed_ok = True; interval_exact = 0; interval_fail = []
    for lam in pn:
        for tau in pn:
            got = sup[lam][tau]
            for mu in got:
                if not (abs(d(lam,n)-d(tau,n)) <= d(mu,n) <= d(lam,n)+d(tau,n)):
                    tri_needed_ok = False
            lo, hi = abs(d(lam,n)-d(tau,n)), min(d(lam,n)+d(tau,n), n-1)
            tri_set = {mu for mu in pn if lo <= d(mu,n) <= hi}
            if got == tri_set: interval_exact += 1
            else: interval_fail.append((lam, tau, len(tri_set-got), len(got-tri_set)))
    print(f"  n={n}: {len(Ms)} matchings, {len(pn)} types; triangle NECESSARY: "
          f"{tri_needed_ok}; support == full d-interval for "
          f"{interval_exact}/{len(pn)**2} (lam,tau) pairs")
    check(f"n={n} necessity", "triangle inequalities are NECESSARY "
          "(no feasible mu outside them)", tri_needed_ok)
# where does the interval law fail? classify
fails = []
for n in (4, 5, 6, 7):
    pn = partitions(n)
    for lam in pn:
        for tau in pn:
            got = SUP[n][lam][tau]
            lo, hi = abs(d(lam,n)-d(tau,n)), min(d(lam,n)+d(tau,n), n-1)
            tri_set = {mu for mu in pn if lo <= d(mu,n) <= hi}
            if got != tri_set:
                fails.append((n, lam, tau, sorted(tri_set-got), sorted(got-tri_set)))
print(f"  interval-law failures across n=4..7: {len(fails)}")
for f in fails[:8]:
    print(f"    n={f[0]} lam={f[1]} tau={f[2]}  missing={f[3][:4]}{'...' if len(f[3])>4 else ''}")
low_d_only = all(min(d(f[1], f[0]), d(f[2], f[0])) <= 1 for f in fails)
check("LAW (mined)", "support = the FULL d-interval whenever d(lam)>=2 and "
      "d(tau)>=2; failures occur only when one side is within distance 1 of "
      "the identity (there the step is exact-type, not an interval)",
      low_d_only, f"{len(fails)} failures, all at min(d)<=1: {low_d_only}")

# ------------------- (3) ground truth: matching-BFS == table closure (n=5)
def bfs_depth(n, tau, kmax=8):
    N2 = 2*n; M0 = canon0(n)
    Ms = [tuple(to_inv(p, N2)) for p in all_matchings(list(range(N2)))]
    alltypes = set(partitions(n))
    seen_types = {mtype(M0, M0)}
    frontier = {tuple(M0)}; seenM = {tuple(M0)}
    k = 0
    while seen_types != alltypes and k < kmax:
        nxt = set()
        for M in frontier:
            Ml = list(M)
            for M2 in Ms:
                if M2 not in seenM and mtype(Ml, list(M2)) == tau:
                    nxt.add(M2)
        for M2 in nxt:
            seenM.add(M2); seen_types.add(mtype(M0, list(M2)))
        frontier = nxt; k += 1
    return k if seen_types == alltypes else None
def table_depth(n, tau, kmax=8):
    pn = set(partitions(n)); sup = SUP[n]
    covered = {tuple([1]*n)}; Dk = {tuple([1]*n)}; k = 0
    while covered != pn and k < kmax:
        Dk = set().union(*(sup[lam][tau] for lam in Dk)) if Dk else set()
        covered |= Dk; k += 1
    return k if covered == pn else None
for tau in ((3, 1, 1), (2, 2, 1), (5,), (2, 1, 1, 1)):
    b, t = bfs_depth(5, tau), table_depth(5, tau)
    check(f"validate n=5 tau={tau}", "matching-BFS ground truth == exact-table "
          f"closure", b == t, f"BFS={b}, table={t}")

# small-n preview of OUR shape: three equal parts + a fixed pair
prev = table_depth(7, (2, 2, 2, 1))
check("preview n=7", "tau=(2,2,2,1) (the [9,9,9,1] shape scaled down): "
      "table-closure magic-depth", prev == 2, f"depth={prev}")

# --------------------------- (4) THE 56: theorem by exhaustive witnesses
D56 = json.load(open("scar56_data.json"))
IOTA, PSI = D56["IOTA"], D56["PSI"]
M0 = IOTA[:]
MPsi = [0]*56
for x in range(56): MPsi[PSI[x]] = PSI[IOTA[x]]
tau56 = mtype(M0, MPsi)
check("56: tau(Psi)", "coset type of the clock = [9,9,9,1] (d = 24)",
      tau56 == (9, 9, 9, 1))
P28 = partitions(28)
M1 = partner_of_type(M0, tau56)
prsM1 = pairs_of(M1)
random.seed(2856)
found = {}                                    # type -> witness M2 (verified)
found[mtype(M0, M0)] = M0[:]                  # M2 = M0: the [1^28] witness
def rand_stab_conj():
    perm = list(range(28)); random.shuffle(perm)
    rel = [0]*56
    for i, (a, b) in enumerate(prsM1):
        c, e = prsM1[perm[i]]
        if random.random() < .5: c, e = e, c
        rel[a], rel[b] = c, e
    base = partner_of_type(M1, tau56)
    M2 = [0]*56
    for x in range(56): M2[rel[x]] = rel[base[x]]
    return M2
NS = 400000
for _ in range(NS):
    M2 = rand_stab_conj()
    t = mtype(M0, M2)
    if t not in found: found[t] = M2
print(f"      sampling: {len(found)}/{len(P28)} coset types witnessed after "
      f"{NS} samples")
# targeted annealing for the stragglers
def anneal(mu, tries=25, steps=20000):
    M2t = partner_of_type(M0, mu)
    for _ in range(tries):
        M2 = rand_stab_conj()                 # starts with type(M1,M2)=tau
        def cost(M):
            c1, c2 = Counter(mtype(M0, M)), Counter(mu)
            return sum((c1-c2).values()) + sum((c2-c1).values())
        c = cost(M2)
        for _s in range(steps):
            if c == 0: break
            x = random.randrange(56); y = random.randrange(56)
            a, b = x, M2[x]; e, f = y, M2[y]
            if len({a, b, e, f}) != 4: continue
            new = M2[:]
            if random.random() < .5: new[a], new[e], new[b], new[f] = e, a, f, b
            else:                    new[a], new[f], new[b], new[e] = f, a, e, b
            if mtype(M1, new) != tau56: continue
            nc = cost(new)
            if nc <= c or random.random() < .02: M2, c = new, nc
        if c == 0: return M2
    return None
missing = [mu for mu in P28 if mu not in found]
print(f"      stragglers for annealing: {len(missing)}")
for mu in list(missing):
    w = anneal(mu)
    if w is not None: found[mu] = w
# final exact verification of EVERY witness
bad = 0
for mu, M2 in found.items():
    if not (mtype(M0, M2) == mu and mtype(M1, M2) == tau56 and
            mtype(M0, M1) == tau56):
        bad += 1
nfound = len(found)
check("56: WITNESS CAMPAIGN", f"explicit depth-2 witnesses (M0 -tau- M1 -tau- "
      f"M2), each verified exactly, for {nfound}/{len(P28)} coset types; "
      f"invalid witnesses: {bad}", bad == 0 and nfound == len(P28),
      "THEOREM: frame-grammar magic-depth of the 56-machine = 2"
      if nfound == len(P28) and bad == 0 else
      f"{len(P28)-nfound} types unwitnessed — depth-2 claim stays OPEN there")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
