import itertools, json, sys
from collections import Counter
import numpy as np
def check(*a, **k): pass
def say(*a): print(*a)
roots = []
for i in range(8):
    for j in range(i + 1, 8):
        for si in (2, -2):
            for sj in (2, -2):
                v = [0] * 8; v[i] = si; v[j] = sj; roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=8):
    if signs.count(-1) % 2 == 0: roots.append(tuple(signs))
ridx = {r: k for k, r in enumerate(roots)}
def dot4(a, b): return sum(x * y for x, y in zip(a, b)) // 4
SIMPLE = [(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0),(0,-2,2,0,0,0,0,0),
          (0,0,-2,2,0,0,0,0),(0,0,0,-2,2,0,0,0),(0,0,0,0,-2,2,0,0),(0,0,0,0,0,-2,2,0)]
GRAM = [[dot4(a, b) for b in SIMPLE] for a in SIMPLE]
Gm = np.array(GRAM, dtype=np.int64); Ginv = np.rint(np.linalg.inv(Gm.astype(float))).astype(np.int64)
coords = []
for r in roots:
    d = np.array([dot4(r, a) for a in SIMPLE], dtype=np.int64); coords.append([int(x) for x in Ginv @ d])
rmask = [int(sum((coords[k][i] & 1) << i for i in range(8))) for k in range(240)]
qvals = []
for m in range(256):
    cv = np.array([(m >> i) & 1 for i in range(8)], dtype=np.int64); qvals.append(((int(cv @ Gm @ cv)) // 2) % 2)
def Bform(x, y): return qvals[x ^ y] ^ qvals[x] ^ qvals[y]
ALPHA_R = SIMPLE[0]; ALPHA = rmask[ridx[ALPHA_R]]
D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]; vidx = {v: k for k, v in enumerate(verts)}
PSI, IOTA, COMP, EDGES = D["PSI"], D["IOTA"], D["COMP"], D["EDGES"]
C7 = [[2,0,-1,0,0,0,0],[0,2,0,-1,0,0,0],[-1,0,2,-1,0,0,0],[0,-1,-1,2,-1,0,0],[0,0,0,-1,2,-1,0],[0,0,0,0,-1,2,-1],[0,0,0,0,0,-1,2]]
E7 = [r for r in roots if dot4(r, ALPHA_R) == 0]; B56 = [r for r in roots if dot4(r, ALPHA_R) == 1]
FUNC = (97, 89, 83, 79, 73, 71, 67, 61)
pos = [r for r in E7 if sum(a*b for a,b in zip(FUNC, r)) > 0]; posset = set(pos)
BASE = [r for r in pos if not any(tuple(a-b for a,b in zip(r,s)) in posset for s in pos)]
CART = [[dot4(a, b) for b in BASE] for a in BASE]
pi = next(p for p in itertools.permutations(range(7)) if all(CART[p[i]][p[j]] == C7[i][j] for i in range(7) for j in range(7)))
BETA = [BASE[pi[i]] for i in range(7)]; BETAM = [rmask[ridx[b]] for b in BETA]
root_of = {}
for r in B56: root_of[vidx[tuple(dot4(r, b) for b in BETA)]] = r
assert len(root_of) == 56
mask = {k: rmask[ridx[root_of[k]]] for k in range(56)}
def ptype(k, l):
    s = mask[k] ^ mask[l]
    if s == ALPHA: return "v"
    return "P" if qvals[s] == 1 else "S"
W2 = {k: tuple(2*x - a for x, a in zip(root_of[k], ALPHA_R)) for k in range(56)}
ipmap = Counter((ptype(k, l), sum(a*b for a, b in zip(W2[k], W2[l]))) for k in range(56) for l in range(56) if k != l)
PAIRS = [(k, l) for k in range(56) for l in range(k + 1, 56)]
def compose(p, q): return [p[q[k]] for k in range(56)]
def ppow(p, e):
    x = list(range(56))
    for _ in range(e): x = compose(p, x)
    return x
def score(p): return sum(1 for k, l in PAIRS if ptype(p[k], p[l]) == ptype(k, l)) / len(PAIRS)

# ---- exploration: per-type survival under Psi^k (Ilya's PROMPT "What exactly does Psi remember?")
# Psi order and orbits
def order(p):
    x=list(range(56)); n=0
    while True:
        x=compose(p,x); n+=1
        if x==list(range(56)): return n
seen=set(); orbs=[]
for k in range(56):
    if k in seen: continue
    o=[]; x=k
    while x not in seen: seen.add(x); o.append(x); x=PSI[x]
    orbs.append(len(o))
print("Psi order", order(PSI), "orbits", sorted(orbs, reverse=True))
types=Counter(ptype(k,l) for k,l in PAIRS); print("pair-type counts", dict(types))
print()
print("k | overall | v-kept | P-kept | S-kept | type-transition matrix (rows from, cols to: v,P,S)")
for kk in (1,2,3,4,5,6,9,17):
    Pk=ppow(PSI,kk)
    M=Counter((ptype(k,l), ptype(Pk[k],Pk[l])) for k,l in PAIRS)
    keep={T: M[(T,T)]/types[T] for T in "vPS"}
    overall=sum(M[(T,T)] for T in "vPS")/len(PAIRS)
    row=lambda T: "[%3d %3d %3d]"%(M[(T,'v')],M[(T,'P')],M[(T,'S')])
    print("%2d | %.4f | %.4f | %.4f | %.4f | v%s P%s S%s"%(kk,overall,keep['v'],keep['P'],keep['S'],row('v'),row('P'),row('S')))
# random baseline per type (mean over 200 random perms)
import random; random.seed(1)
acc={T:0.0 for T in "vPS"}; N=200
for _ in range(N):
    p=list(range(56)); random.shuffle(p)
    M=Counter((ptype(k,l), ptype(p[k],p[l])) for k,l in PAIRS)
    for T in "vPS": acc[T]+=M[(T,T)]/types[T]/N
print("random baseline per type:", {T: round(acc[T],4) for T in "vPS"})
# the 8 antipodal steps: which pairs {u, iota u} are kept as v-pairs
vk=[(k,l) for k,l in PAIRS if ptype(k,l)=="v" and ptype(PSI[k],PSI[l])=="v"]
print("v-pairs kept under Psi:", vk)
