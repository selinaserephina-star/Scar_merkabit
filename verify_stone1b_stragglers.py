# verify_stone1b_stragglers.py — closing the 250 open coset types of the
# frame-grammar depth-2 witness campaign (companion to
# verify_stone1b_hyperoct.py; same objects, stronger search).
#
# Strategy change: SOFT dual-cost annealing — instead of rejecting every
# move that breaks type(M1,M)=tau, penalize BOTH mismatches
#     cost(M) = dist(type(M0,M), mu) + dist(type(M1,M), tau)
# and anneal freely to cost 0.  Witnesses cached to stone1b_witnesses.json;
# every witness re-verified exactly before the verdict.
# Run:  python -u -X utf8 verify_stone1b_stragglers.py
import json, random, os
from collections import Counter

def mtype(A, B):
    N2 = len(A); seen = [False]*N2; parts = []
    for s in range(N2):
        if seen[s]: continue
        L, x = 0, s; cyc = []
        while not seen[x]:
            seen[x] = True; cyc.append(x); L += 1; x = B[A[x]]
        for y in cyc: seen[A[y]] = True
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
    prs = pairs_of(baseM); M = [0]*len(baseM); p = 0
    for k in parts:
        ch = prs[p:p+k]; p += k
        for j in range(k):
            a2 = ch[(j+1) % k][0]; b1 = ch[j][1]
            M[b1], M[a2] = a2, b1
    return M
def partitions(n):
    out = []
    def gp(rem, mx, cur):
        if rem == 0: out.append(tuple(cur)); return
        for k in range(min(rem, mx), 0, -1): gp(rem-k, k, cur+[k])
    gp(n, n, [])
    return out

D56 = json.load(open("scar56_data.json"))
IOTA = D56["IOTA"]
M0 = IOTA[:]
TAU = (9, 9, 9, 1)
M1 = partner_of_type(M0, TAU)
assert mtype(M0, M1) == TAU
prsM1 = pairs_of(M1)
P28 = partitions(28)
key = lambda t: ",".join(map(str, t))

CACHE = "stone1b_witnesses.json"
found = {}
if os.path.exists(CACHE):
    raw = json.load(open(CACHE))
    for k, v in raw.items():
        found[tuple(int(x) for x in k.split(","))] = v
found[mtype(M0, M0)] = M0[:]

random.seed(285656)
def rand_stab_conj():
    perm = list(range(28)); random.shuffle(perm)
    rel = [0]*56
    for i, (a, b) in enumerate(prsM1):
        c, e = prsM1[perm[i]]
        if random.random() < .5: c, e = e, c
        rel[a], rel[b] = c, e
    base = partner_of_type(M1, TAU)
    M2 = [0]*56
    for x in range(56): M2[rel[x]] = rel[base[x]]
    return M2

NS = 1200000
print(f"sampling {NS} random tau-partners of M1 ...")
for i in range(NS):
    M2 = rand_stab_conj()
    t = mtype(M0, M2)
    if t not in found: found[t] = M2
    if (i+1) % 300000 == 0:
        print(f"  {i+1}: {len(found)}/{len(P28)} types witnessed")
missing = [mu for mu in P28 if mu not in found]
hist = Counter(28 - len(mu) for mu in missing)
print(f"stragglers: {len(missing)}; d-histogram: {sorted(hist.items())}")

def pdist(t, target):
    c1, c2 = Counter(t), Counter(target)
    return sum((c1-c2).values()) + sum((c2-c1).values())
def soft_anneal(mu, tries=6, steps=120000):
    for _try in range(tries):
        # warm start alternates: right-type-vs-M0, or right-type-vs-M1
        M = partner_of_type(M0, mu) if _try % 2 == 0 else rand_stab_conj()
        def cost(Mx):
            return pdist(mtype(M0, Mx), mu) + pdist(mtype(M1, Mx), TAU)
        c = cost(M); T0 = 2.5
    # anneal
        for s in range(steps):
            if c == 0: return M
            Tmp = T0 * (1 - s/steps) + 0.02
            x = random.randrange(56); y = random.randrange(56)
            a, b = x, M[x]; e, f = y, M[y]
            if len({a, b, e, f}) != 4: continue
            new = M[:]
            if random.random() < .5: new[a], new[e], new[b], new[f] = e, a, f, b
            else:                    new[a], new[f], new[b], new[e] = f, a, e, b
            nc = cost(new)
            if nc <= c or random.random() < 2.718 ** (-(nc - c)/Tmp):
                M, c = new, nc
        if c == 0: return M
    return None

closed = 0
for j, mu in enumerate(missing):
    w = soft_anneal(mu)
    if w is not None:
        found[mu] = w; closed += 1
    if (j+1) % 25 == 0:
        print(f"  annealed {j+1}/{len(missing)}: closed {closed}")
print(f"anneal pass: closed {closed}/{len(missing)}")

# save cache (json-serializable)
json.dump({key(t): list(map(int, M)) for t, M in found.items()},
          open(CACHE, "w"))

# final exact verification of everything
bad = 0
for mu, M2 in found.items():
    if not (mtype(M0, M2) == mu and mtype(M1, M2) == TAU):
        bad += 1
still = [mu for mu in P28 if mu not in found]
print("=" * 70)
print(f"witnessed {len(found)}/{len(P28)} coset types; invalid: {bad}; "
      f"still open: {len(still)}")
if still:
    print("open types (d, type):",
          [(28-len(mu), mu) for mu in still[:12]])
if not still and bad == 0:
    print("THEOREM (by 3718 verified witnesses): the frame-grammar")
    print("magic-depth of the 56-machine is EXACTLY 2.")
print("=" * 70)
