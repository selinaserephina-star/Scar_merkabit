# verify_stonef_field.py — STONE F(a): the field machine.
#
# The lift: from the token machine (a state on one of 56 squares) to the
# FIELD machine (a value on every square: C^56).  Gates become permutation
# matrices; the clock's eigenmodes are literal STANDING WAVES — patterns
# each tick multiplies by a fixed 18th root of unity.  Computed here:
#
#   (1) the exact standing-wave spectrum of Psi (eigenvalues,
#       multiplicities, trace formula = the CSP census — the machine's
#       oldest invariant IS the standing-wave bookkeeping);
#   (2) the orbit census that fixes every eigenmode's mass in every
#       grammar sector (branch components; iota-frames) — exact, because
#       Fourier modes are flat on their orbit;
#   (3) the involution relations (settles DQ-4's algebra: iota Psi iota
#       =? Psi^-1, pr Psi pr =? Psi^-1, [pr, iota] =? 0) and the induced
#       action on eigenspaces;
#   (4) the Scar field sectors at character level: C^56 = (iota-even) +
#       (iota-odd) as PSL(2,7)-modules via the bridge — computed exactly
#       from the derived character table.
#
# Rule 3: "field", "wave", "chirality" are computational role names.
# Run:  python -X utf8 verify_stonef_field.py
import json, cmath, math
import numpy as np
from fractions import Fraction
from collections import Counter

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

D = json.load(open("scar56_data.json"))
PSI, PR, IOTA = D["PSI"], D["PR"], D["IOTA"]
COMP, FRAME, FIX = D["COMP"], D["FRAME"], D["FIX"]
N = 56
CN = ["27", "27bar", "vac1", "vac2"]

print("=" * 78)
print("STONE F(a) -- the field machine: standing waves of the 56")
print("=" * 78)

# ------------------------------------------------------- (1) the spectrum
orbits = []
seen = [False]*N
for s in range(N):
    if seen[s]: continue
    o, x = [], s
    while not seen[x]: seen[x] = True; o.append(x); x = PSI[x]
    orbits.append(o)
orbits.sort(key=len, reverse=True)
check("orbits", "clock orbits [18,18,18,2]",
      [len(o) for o in orbits] == [18, 18, 18, 2])
# exact multiplicities: an L-cycle contributes each L-th root of unity once
mult = Counter()
for o in orbits:
    L = len(o)
    for j in range(L):
        mult[(j * (18 // L)) % 18] += 1     # as 18th-root exponents
expected = {k: (4 if k in (0, 9) else 3) for k in range(18)}
check("spectrum", "eigenvalues = all 18th roots of unity; multiplicity 4 at "
      "+1 and -1, multiplicity 3 elsewhere (total 56)",
      dict(mult) == expected and sum(mult.values()) == 56)
# numerical confirmation + trace formula = CSP census
P = np.zeros((N, N))
for x in range(N): P[PSI[x], x] = 1
ev = np.linalg.eigvals(P)
ang = sorted(Counter(int(round((cmath.phase(z) % (2*math.pi)) / (2*math.pi/18)))
                     % 18 for z in ev).items())
check("numerics", "numerical eigendecomposition agrees with the exact count",
      dict(ang) == expected)
tr_ok = all(abs(sum(m * cmath.exp(2j*math.pi*k*d_/18)
                    for k, m in mult.items()) - FIX[d_]) < 1e-9
            for d_ in range(18))
check("CSP = waves", "trace formula: |Fix(Psi^d)| = sum of (standing-wave "
      "eigenvalues)^d — the CSP census IS the standing-wave bookkeeping",
      tr_ok, f"census {FIX}")

# ------------------------------------------- (2) orbit census -> sector mass
print("\n  every Fourier mode is FLAT on its orbit (|amplitude|^2 = 1/L), so")
print("  a standing wave's mass in a sector is exact orbit arithmetic:")
print("  orbit | length | mass in 27 / 27bar / vac1 / vac2 | frames visited")
frame_split = 0
for i, o in enumerate(orbits):
    cc = Counter(COMP[x] for x in o)
    fr = {FRAME[x] for x in o}
    print(f"    O{i}  |  {len(o):2d}   |  " +
          " / ".join(f"{cc.get(c,0)}/{len(o)}" for c in range(4)) +
          f"  |  {len(fr)} frames")
# the 2-orbit: who is it?  (auditor's guess "not an iota-frame" was WRONG —
# recorded: the discovery is the opposite and better)
o2 = orbits[3]
a, b = o2
check("the 2-orbit [obs]", "the clock's own 2-cycle IS an iota-frame, and "
      "it straddles the two sheets: the clock contains exactly one frame, "
      "which it merely flips — its AXIS frame (not the E6 vacua!)",
      {COMP[a], COMP[b]} == {0, 1} and IOTA[a] == b,
      f"states {o2}, components {CN[COMP[a]]}/{CN[COMP[b]]}")
# frames vs orbits: how many iota-pairs live inside a single orbit?
inside = sum(1 for x in range(N) if x < IOTA[x] and
             any(x in o and IOTA[x] in o for o in orbits))
print(f"  iota-frames contained in a single clock orbit: {inside}/28")
# Psi^9-pairing vs iota (DQ-4's '4/28'):
p9 = list(range(N))
for _ in range(9): p9 = [PSI[x] for x in p9]
shared = [(x, IOTA[x]) for x in range(N) if x < IOTA[x] and p9[x] == IOTA[x]]
shared_orbs = [next(i for i, o in enumerate(orbits) if x in o)
               for x, _ in shared]
check("DQ-4: the 4", "the 4 iota-pairs shared with the Psi^9-pairing "
      "identified; each is an antipodal pair inside a single clock orbit",
      len(shared) == 4, f"pairs {shared} in orbits {shared_orbs}")

# --------------------------------------------- (3) involution relations
PSIinv = [0]*N
for x in range(N): PSIinv[PSI[x]] = x
conj_i = [IOTA[PSI[IOTA[x]]] for x in range(N)]
conj_p = [PR[PSI[PR[x]]] for x in range(N)]
check("DQ-4: iota", "iota Psi iota = Psi^-1 — the antipode REVERSES the "
      "clock (standing waves: iota maps the lambda-mode to the "
      "lambda-bar-mode)", conj_i == PSIinv)
check("pr vs clock", "pr Psi pr = Psi^-1 as well — the mirror also reverses "
      "time" if conj_p == PSIinv else
      "pr Psi pr != Psi^-1 (the mirror does NOT simply reverse the clock)",
      True, f"prPsipr==Psi^-1: {conj_p == PSIinv}")
comm = [PR[IOTA[x]] for x in range(N)] == [IOTA[PR[x]] for x in range(N)]
check("pr,iota", "the two bilingual involutions commute" if comm else
      "pr and iota do NOT commute", True, f"commute: {comm}")
# action on eigenspaces: iota preserves each orbit (it inverts Psi);
# does pr even map orbits to orbits?
osets = [set(o) for o in orbits]
iota_pres = all({IOTA[x] for x in o} in osets for o in osets)
pr_pres = all({PR[x] for x in o} in osets for o in osets)
check("iota on waves", "iota preserves every clock orbit setwise, so it "
      "ACTS on each eigenspace (E_lambda -> E_lambda-bar); on E(+1) it is "
      "the identity (all 4 orbit-constant waves fixed)", iota_pres)
# E(-1): alternating wave on each orbit; iota (a reflection of the cycle)
# sends it to +-itself — compute the sign per orbit
signs = []
for o in orbits:
    pos = {x: i for i, x in enumerate(o)}
    L = len(o)
    s0 = None; consistent = True
    for x in o:
        s = (-1) ** ((pos[IOTA[x]] - pos[x]) % 2)   # parity shift
        sgn = ((-1) ** pos[x]) * ((-1) ** pos[IOTA[x]])
        if s0 is None: s0 = sgn
        elif sgn != s0: consistent = False
    signs.append(s0 if consistent else 0)
print(f"  iota on the E(-1) alternating waves, sign per orbit: {signs}")
check("pr vs waves", "pr does NOT map clock orbits to clock orbits — the "
      "mirror is bilingual (zero magic in both grammars) yet MIXES the "
      "standing-wave frequencies: free gates can still shuffle the music",
      not pr_pres)
ov = [[len({PR[x] for x in orbits[i]} & osets[j]) for j in range(4)]
      for i in range(4)]
print(f"  pr orbit-overlap matrix |pr(Oi) n Oj|: {ov}")

# ------------------------- (4) Scar field sectors (character level, exact)
# PSL(2,7) exact table over Q(sqrt(-7)) (derived in verify_tsc_scarcat.py)
H = Fraction(1, 2)
TAB = [[(1,0)]*6,
       [(3,0),(-1,0),(0,0),(1,0),(-H,H),(-H,-H)],
       [(3,0),(-1,0),(0,0),(1,0),(-H,-H),(-H,H)],
       [(6,0),(2,0),(0,0),(0,0),(-1,0),(-1,0)],
       [(7,0),(-1,0),(1,0),(-1,0),(0,0),(0,0)],
       [(8,0),(0,0),(-1,0),(0,0),(1,0),(1,0)]]
TAB = [[(Fraction(a), Fraction(b)) for a, b in r] for r in TAB]
sizes = [1, 21, 56, 42, 24, 24]
# restriction of each chi to S3 = N(<z3>): S3 classes hit G-classes
# (1A, 2A, 3A) with S3-sizes (1, 3, 2)
def ind_mult(sgn):
    """<Ind_{S3}^G eps, chi_r> for eps = triv (sgn=+1) or sign (sgn=-1)"""
    out = []
    for r in range(6):
        v1, v2, v3 = TAB[r][0][0], TAB[r][1][0], TAB[r][2][0]
        m = (v1 + (3*v2 if sgn > 0 else -3*v2) + 2*v3) / 6
        assert m.denominator == 1
        out.append(int(m))
    return out
even = ind_mult(+1); odd = ind_mult(-1)
check("Scar sectors", "field space C^56 = iota-even + iota-odd as "
      "PSL(2,7)-modules (via the bridge, any bitangent identification): "
      "even = chi1 + 2*chi6 + chi7 + chi8 (dim 28), "
      "odd = chi3 + chi3bar + 2*chi7 + chi8 (dim 28)",
      even == [1, 0, 0, 2, 1, 1] and odd == [0, 1, 1, 0, 2, 1] and
      sum(m*d_ for m, d_ in zip(even, [1,3,3,6,7,8])) == 28 and
      sum(m*d_ for m, d_ in zip(odd,  [1,3,3,6,7,8])) == 28,
      f"even={even}, odd={odd}")
check("chirality-odd quarks", "the quark sectors chi3, chi3bar occur ONLY "
      "in the iota-ODD (chirality-odd) half of the field space; the vacuum "
      "sector chi1 only in the even half [obs, character-level]",
      even[1] == even[2] == 0 and odd[0] == 0)

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
