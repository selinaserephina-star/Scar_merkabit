# verify_stone1b_close73.py — closing the last 73 coset types (dual-direction
# sampling: build M2 with type(M0,M2)=mu exactly by Stab(M0)-conjugation,
# accept when type(M1,M2)=tau).  Appends to stone1b_witnesses.json.
# Run:  python -u -X utf8 verify_stone1b_close73.py
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
M0 = D56["IOTA"][:]
TAU = (9, 9, 9, 1)
M1 = partner_of_type(M0, TAU)
prsM0 = pairs_of(M0)
P28 = partitions(28)
key = lambda t: ",".join(map(str, t))
CACHE = "stone1b_witnesses.json"
found = {}
if os.path.exists(CACHE):
    for k, v in json.load(open(CACHE)).items():
        found[tuple(int(x) for x in k.split(","))] = v
missing = [mu for mu in P28 if mu not in found]
print(f"open targets: {len(missing)}")
random.seed(7356)

def conj_M0(base):
    perm = list(range(28)); random.shuffle(perm)
    rel = [0]*56
    for i, (a, b) in enumerate(prsM0):
        c, e = prsM0[perm[i]]
        if random.random() < .5: c, e = e, c
        rel[a], rel[b] = c, e
    M2 = [0]*56
    for x in range(56): M2[rel[x]] = rel[base[x]]
    return M2

closed = 0
for j, mu in enumerate(missing):
    base = partner_of_type(M0, mu)
    hit = None
    for _ in range(400000):
        M2 = conj_M0(base)
        if mtype(M1, M2) == TAU:
            hit = M2; break
    if hit is not None:
        assert mtype(M0, hit) == mu
        found[mu] = hit; closed += 1
        print(f"  [{j+1}/{len(missing)}] mu (d={28-len(mu)}) CLOSED")
    else:
        print(f"  [{j+1}/{len(missing)}] mu={mu} still open after 4e5 tries")
json.dump({key(t): list(map(int, M)) for t, M in found.items()},
          open(CACHE, "w"))
bad = sum(1 for mu, M2 in found.items()
          if not (mtype(M0, M2) == mu and mtype(M1, M2) == TAU))
still = [mu for mu in P28 if mu not in found]
print("=" * 70)
print(f"witnessed {len(found)}/{len(P28)}; invalid {bad}; still open {len(still)}")
if still:
    print("remaining:", [(28-len(m), m) for m in still])
else:
    print("THEOREM (by 3718 verified witnesses): frame-grammar magic-depth")
    print("of the 56-machine = EXACTLY 2.")
print("=" * 70)
