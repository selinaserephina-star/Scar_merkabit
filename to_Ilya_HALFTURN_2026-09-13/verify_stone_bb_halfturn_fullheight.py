"""
verify_stone_bb_halfturn_fullheight.py  -- Stone BB, registry row SM-066.

Re-checks the completed proof of BRIEF_STONE_BB_HALFTURN_FULLHEIGHT.md:
SM-063 sec 7.12.4 open #1, the half-turn is a Weyl element on the orbit
WITHOUT the highest weight lambda, and not on lambda's orbit -- by the Weyl
rank-shift lemma (a proof, not a search).

First test: the brief's SHA-256 matches the lock.  Then BB1..BB5.
Plain Python 3, no numpy.  Builds on SM-063's H3 clock (verbatim).
"""
import hashlib, itertools, sys, os

# ---- BB0: the brief hash matches the lock ----------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
brief = os.path.join(HERE, "BRIEF_STONE_BB_HALFTURN_FULLHEIGHT.md")
lock  = os.path.join(HERE, "BRIEF_STONE_BB_LOCK.sha256")
with open(brief, "rb") as f: h = hashlib.sha256(f.read()).hexdigest()
with open(lock) as f: locked = f.read().split()[0]
assert h == locked, f"BB0 FAIL: brief hash {h} != lock {locked}"
print(f"BB0 PASS: brief locked, sha256 = {h[:12]}...")

# ---- the board: B4 spinor, W(B4) = F2^4 |x| S4, the sealed clock (SM-063 H3)
def bits(neg): return tuple(1 if (i+1) in neg else 0 for i in range(4))
O1 = [bits(s) for s in [set(),{4},{3},{2,4},{1,3},{1,2,4},{1,2,3},{1,2,3,4}]]
O2 = [bits(s) for s in [{1},{3,4},{2},{1,4},{2,3},{1,3,4},{1,2},{2,3,4}]]
assert (0,0,0,0) in O1 and (1,1,1,1) in O1, "lambda, w0.lambda in O1"
assert len(set(O1) | set(O2)) == 16, "the two free orbits cover the 16 vertices"
def wt(x): return sum(x)
def xor(a,b): return tuple(p^q for p,q in zip(a,b))
def cap(x,u): return sum(1 for i in range(4) if x[i]==1 and u[i]==1)
def R4(orb): return {orb[j]: orb[(j+4)%8] for j in range(8)}   # half-turn = +4

# ---- BB1: rank-shift is +-2 on O1, +-1 on O2 -------------------------------
sh1 = {x: wt(R4(O1)[x]) - wt(x) for x in O1}
sh2 = {x: wt(R4(O2)[x]) - wt(x) for x in O2}
assert set(sh1.values()) == {2,-2}, "BB1 FAIL"
assert set(sh2.values()) == {1,-1}, "BB1 FAIL"
print("BB1 PASS: R^4 shifts every rank by +-2 on O1, +-1 on O2.")

# ---- BB2: no Weyl u reproduces O1's rank-shift; exactly u=1110 does on O2 ---
# Lemma BB-A: a Weyl element has Delta(x) = wt(u) - 2|x cap u|, u = pi^{-1}(v).
def reproducing_us(orb, sh):
    return [u for u in itertools.product((0,1),repeat=4)
            if all(sh[x] == wt(u) - 2*cap(x,u) for x in orb)]
u1 = reproducing_us(O1, sh1); u2 = reproducing_us(O2, sh2)
assert u1 == [], "BB2 FAIL: some Weyl element would agree with R^4 on O1"
assert u2 == [(1,1,1,0)], "BB2 FAIL: O2 must be realised by u=1110 (=-tau)"
print("BB2 PASS: no u reproduces O1 (=> R^4|O1 not Weyl); u=1110 reproduces O2 (=> -tau).")

# ---- BB3: the proof engine (lambda pins wt(u)=2, spanning kills it) ---------
assert sh1[(0,0,0,0)] == 2, "BB3 FAIL: R^4 must move lambda up by 2"
# O1 linearly spans F2^4 (contains 0 and 8 pts of full rank), so every weight-2
# u meets some O1 vector in ODD overlap => cannot keep |shift|=2 => contradiction
def linear_span(pts):
    basis=[];
    for p in pts:
        v=p
        for b in basis:
            lead=min(i for i in range(4) if b[i]==1)
            if v[lead]==1: v=xor(v,b)
        if any(v): basis.append(v)
    return len(basis)==4
assert (0,0,0,0) in O1 and linear_span(O1), "O1 linearly spans F2^4"
for u in itertools.product((0,1),repeat=4):
    if wt(u)==2:
        assert any(sum(x[i]*u[i] for i in range(4))%2==1 for x in O1), \
            "BB3 FAIL: a weight-2 u has even overlap with all of O1"
print("BB3 PASS: lambda forces wt(u)=2; O1 spans => odd overlap => contradiction.")

# ---- BB4: cross-check against the affine picture ---------------------------
def affine_linear_part(orb):
    f = R4(orb); base = orb[0]; fb = f[base]
    known = {}
    for x in orb:
        d = xor(x,base); im = xor(f[x],fb)
        if d in known and known[d]!=im: return None
        known[d]=im
    changed=True
    while changed:
        changed=False
        for d1,i1 in list(known.items()):
            for d2,i2 in list(known.items()):
                d=xor(d1,d2); im=xor(i1,i2)
                if d in known:
                    if known[d]!=im: return None
                else: known[d]=im; changed=True
    e=[tuple(1 if k==i else 0 for k in range(4)) for i in range(4)]
    return [known[ei] for ei in e]
def is_perm(L): return all(sum(c)==1 for c in L) and len(set(L))==4
L1, L2 = affine_linear_part(O1), affine_linear_part(O2)
swap23 = [(1,0,0,0),(0,0,1,0),(0,1,0,0),(0,0,0,1)]; u_dir=(0,1,1,0)
assert L2 == swap23 and is_perm(L2), "BB4 FAIL: O2 linear part is (23)"
assert L1 is not None and not is_perm(L1), "BB4 FAIL: O1 linear part must be non-permutation"
def apply(L,x): return tuple(sum(x[i]*L[i][k] for i in range(4))%2 for k in range(4))
assert all(apply(L1,x)==xor(apply(swap23,x),
           tuple(((x[0]+x[3])%2)*d for d in u_dir))
           for x in itertools.product((0,1),repeat=4)), \
       "BB4 FAIL: L1 != (23)+(x1+x4)(e2+e3)"
sheared = sorted(i+1 for i in range(4) if sum(L1[i])!=1)
assert sheared == [1,4], "BB4 FAIL: shear must sit on directions {1,4}"
print("BB4 PASS: O2 linear part (23) in S4; O1 = (23) + transvection on {1,4}, not Weyl.")

# ---- BB5 [obs]: the full-height distinguisher ------------------------------
assert [wt(x) for x in O1] == [0,1,1,2,2,3,3,4], "O1 spans the full rank range"
assert not any(wt(x) in (0,4) for x in O2), "O2 stays in the middle ranks"
assert O1[(O1.index((1,1,1,1))+1)%8] == (0,0,0,0), "rowmotion wraps w0.lambda -> lambda"
print("BB5 PASS [obs]: O1 unique full-height orbit; rowmotion wraps w0.lambda -> lambda.")

print("\nSTONE BB: 6 PASS + 0 FAIL. Theorem BB proved and re-checked.")
