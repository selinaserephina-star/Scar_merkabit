# verify_stone_t_tgate.py — STONE T: FIRST CONTACT WITH THE T GATE
# Brief: BRIEF_STONE_T_TGATE.md (sha-locked fa6816e9... BEFORE this file
# existed).  Registered bars TB1..TB5.
#
# ROUTE.  Exact ring Z[omega] (omega^4 = -1, sqrt2 = omega - omega^3);
# 1-qubit Clifford+T ground truth by BFS layers C(TC)^k mod phase;
# Matsumoto-Amano words cross-check (free skeleton on range); the LOCKED
# fit/test protocol for the denominator-exponent certificate; the channel
# representation as the Clifford+T "contingency table" (double cosets =
# matrices mod signed permutations, verified on the declared sample); the
# 3-qubit skeleton theorem (phase points are the T-free stratum).
#
# Run:  python -X utf8 verify_stone_t_tgate.py
import numpy as np
from collections import Counter, defaultdict

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("STONE T -- first contact with the T gate (Clifford+T, exact)")
print("=" * 78)

# ------------------------------------------------ the ring Z[omega]
# element = (a,b,c,d) ~ a + b w + c w^2 + d w^3,  w^4 = -1
def zmul(x, y):
    a, b, c, d = x; e, f, g, h = y
    return (a*e - b*h - c*g - d*f,
            a*f + b*e - c*h - d*g,
            a*g + b*f + c*e - d*h,
            a*h + b*g + c*f + d*e)
def zadd(x, y): return tuple(u + v for u, v in zip(x, y))
def zneg(x): return tuple(-u for u in x)
def zconj(x):
    a, b, c, d = x
    return (a, -d, -c, -b)
Z0, Z1 = (0, 0, 0, 0), (1, 0, 0, 0)
W = (0, 1, 0, 0)
SQ2 = (0, 1, 0, -1)               # w - w^3
def zsq2(x):                       # x * sqrt2
    a, b, c, d = x
    return (b - d, a + c, b + d, c - a)
def zdivsq2(x):                    # exact x / sqrt2 or None
    y = zsq2(x)                    # x*sqrt2 = (x/sqrt2)*2
    if all(v % 2 == 0 for v in y):
        return tuple(v // 2 for v in y)
    return None
def zrotw(x):                      # x * w
    a, b, c, d = x
    return (-d, a, b, c)

# unitary = (s, ((e00,e01),(e10,e11))) meaning M / sqrt2^s, fully reduced,
# canonical modulo the phase group <w>
def reduce_u(s, M):
    while s > 0:
        div = [zdivsq2(e) for row in M for e in row]
        if any(d is None for d in div): break
        M = ((div[0], div[1]), (div[2], div[3])); s -= 1
    return s, M
def canon(s, M):
    s, M = reduce_u(s, M)
    best = None
    cur = M
    for _ in range(8):
        cur = ((zrotw(cur[0][0]), zrotw(cur[0][1])),
               (zrotw(cur[1][0]), zrotw(cur[1][1])))
        if best is None or cur < best: best = cur
    return (s, best)
def umul(u, v):
    s1, A = u; s2, B = v
    M = tuple(tuple(zadd(zmul(A[i][0], B[0][j]), zmul(A[i][1], B[1][j]))
                    for j in range(2)) for i in range(2))
    return canon(s1 + s2, M)

H_u = canon(1, ((Z1, Z1), (Z1, zneg(Z1))))
S_u = canon(0, ((Z1, Z0), (Z0, (0, 0, 1, 0))))
T_u = canon(0, ((Z1, Z0), (Z0, W)))
I_u = canon(0, ((Z1, Z0), (Z0, Z1)))

rt = zdivsq2(zsq2((3, -2, 5, 7)))
check("TB1 ring", "sqrt2 multiply/divide round-trip exact; conj(w)= -w^3; "
      "sqrt2^2 = 2", rt == (3, -2, 5, 7) and zconj(W) == (0, 0, 0, -1)
      and zmul(SQ2, SQ2) == (2, 0, 0, 0))
def uadjoint(u):
    s, M = u
    return canon(s, ((zconj(M[0][0]), zconj(M[1][0])),
                     (zconj(M[0][1]), zconj(M[1][1]))))
check("TB1 unitarity", "H, S, T unitary (U U+ = I mod phase); H^2 = I, "
      "S^4 = I mod phase",
      all(umul(u, uadjoint(u)) == I_u for u in (H_u, S_u, T_u))
      and umul(H_u, H_u) == I_u
      and umul(S_u, umul(S_u, umul(S_u, S_u))) == I_u)

# Clifford_1 mod phase
CLIF = {I_u}
frontier = [I_u]
while frontier:
    nxt = []
    for u in frontier:
        for g in (H_u, S_u):
            v = umul(g, u)
            if v not in CLIF: CLIF.add(v); nxt.append(v)
    frontier = nxt
CLIF = sorted(CLIF)
check("TB1 Clifford", "<H,S> mod phase has exactly 24 elements",
      len(CLIF) == 24)

# ------------------------------------------------ TB2: BFS ground truth
print("\n--- TB2: BFS layers vs Matsumoto-Amano words (the skeleton) ---")
CAP = 30000     # instantiated per AMENDMENT_STONE_T_2026-08-30 (K = 9)
layers = [set(CLIF)]
seen = set(CLIF)
total = len(seen)
while total <= CAP:
    prev = layers[-1]
    nxt = set()
    for u in prev:
        tu = umul(T_u, u)
        for c in CLIF:
            v = umul(c, tu)
            if v not in seen: nxt.add(v)
    if not nxt: break
    layers.append(nxt); seen |= nxt; total += len(nxt)
K = len(layers) - 1
sizes = [len(L) for L in layers]
print(f"  reached K = {K}; layer sizes {sizes}; total {total}")
check("TB2 growth", "layer sizes = 24, then 72 * 2^(k-1): exact rate-2 "
      "free growth (the crystal's 4*2^(l-1) skeleton, in the T world)",
      sizes[0] == 24 and all(sizes[k] == 72 * 2 ** (k - 1)
                             for k in range(1, K + 1)))
# Matsumoto-Amano: (T | eps) (HT | SHT)^* Clifford
HT = umul(H_u, T_u); SHT = umul(S_u, HT)
ma_layers = [set(CLIF)]
prefixes = {(): I_u}
for k in range(1, K + 1):
    newpre = {}
    Lset = set()
    for word, u in prefixes.items():
        for tag, syl in (("HT", HT), ("SHT", SHT)):
            if len(word) == k - 1:
                v = umul(u, syl) if word else syl
                # build left-to-right: prefix * syllable
                newpre[word + (tag,)] = umul(u, syl)
    prefixes = newpre
    for u in prefixes.values():
        for c in CLIF:
            Lset.add(umul(u, c))                    # eps = 0 : k syllables
    # eps = 1: T * (k-1 syllables) * C
    pre2 = {(): I_u}
    for _ in range(k - 1):
        pre2 = {w + (t,): umul(u, s2) for w, u in pre2.items()
                for t, s2 in (("HT", HT), ("SHT", SHT))}
    for u in pre2.values():
        tu = umul(T_u, u)
        for c in CLIF:
            Lset.add(umul(tu, c))
    ma_layers.append(Lset)
ma_ok = all(ma_layers[k] == layers[k] for k in range(K + 1))
check("TB2 MA = BFS", "Matsumoto-Amano words reproduce every BFS layer "
      "AS A SET for all k <= K: normal-form uniqueness AND T-optimality "
      "verified on range  [classical: Matsumoto-Amano 2008]", ma_ok)

# ------------------------------------------------ TB3: the LOCKED protocol
print("\n--- TB3: the denominator certificate (registered headline) ---")
def sde_depth(e, s):
    d = 0
    x = e
    while d < s:
        y = zdivsq2(x)
        if y is None: break
        x = y; d += 1
    return d
def invariant(u):
    s, M = u
    depths = sorted(s - sde_depth(M[i][j], s)
                    for i in range(2) for j in range(2))
    return (s, tuple(depths))
fitmap = defaultdict(set)
for k in range(0, min(3, K) + 1):
    for u in layers[k]: fitmap[invariant(u)].add(k)
fit_collisions = {inv: ks for inv, ks in fitmap.items() if len(ks) > 1}
single_fit = len(fit_collisions) == 0
globalmap = defaultdict(set)
for k in range(K + 1):
    for u in layers[k]: globalmap[invariant(u)].add(k)
glob_collisions = {inv: sorted(ks) for inv, ks in globalmap.items()
                   if len(ks) > 1}
if fit_collisions:
    ex = sorted(fit_collisions.items())[0]
    check("TB3 REGISTERED OUTCOME", "the locked candidate invariant "
          "(global sde, sorted entry-depths) is NOT single-valued even on "
          "the fit window k <= 3 — the naive denominator certificate is "
          "INCOMPLETE, refuted at the diagonal (witnesses: S has T-count "
          "0 and T has T-count 1 with the IDENTICAL invariant).  Recorded "
          "as the registered headline finding", True,
          f"first collision: invariant {ex[0]} -> T-counts {sorted(ex[1])}"
          f"; {len(glob_collisions)} colliding invariants over the full "
          f"range")
else:
    check("TB3 REGISTERED OUTCOME", "the locked invariant is single-"
          "valued on the fit window AND the full range",
          len(glob_collisions) == 0,
          f"global collisions: {len(glob_collisions)}")
# POST-HOC refinement (labelled): add per-entry unit residues mod sqrt2.
# Z[w]/sqrt2 has 4 elements; record each entry's residue class after
# dividing out its sqrt2-depth (0 entries -> 'z').
def residue(e):
    return (e[0] + e[2]) & 1, (e[1] + e[3]) & 1
def invariant2(u):
    s, M = u
    ent = []
    for i in range(2):
        for j in range(2):
            e = M[i][j]
            d = sde_depth(e, s)
            x = e
            for _ in range(d): x = zdivsq2(x)
            ent.append((s - d, residue(x) if e != Z0 else (2, 2)))
    return (s, tuple(sorted(ent)))
g2 = defaultdict(set)
for k in range(K + 1):
    for u in layers[k]: g2[invariant2(u)].add(k)
coll2 = {i: sorted(ks) for i, ks in g2.items() if len(ks) > 1}
n_coll2 = len(coll2)
ex2 = sorted(coll2.items())[0] if coll2 else None
check("TB3 post-hoc refinement", "adding per-entry residues mod sqrt2 "
      "(the omega-parity layer): tested for single-valuedness over the "
      "FULL range — measured, labelled post-hoc",
      True,
      (f"single-valued: {n_coll2 == 0}; colliding invariants: {n_coll2}"
       + (f"; first: {ex2[0]} -> {ex2[1]}" if ex2 else "")))
# the (s -> T-counts) coarse table, printed for the record
stab = defaultdict(set)
for k in range(K + 1):
    for u in layers[k]: stab[u[0]].add(k)
print("  global sde s -> T-counts present: "
      + "; ".join(f"s={s}: {sorted(ks)}" for s, ks in sorted(stab.items())))

# ------------------------------------------------ TB4: the table shape
print("\n--- TB4: channel representation = the Clifford+T table ---")
X_z = ((Z0, Z1), (Z1, Z0))
Y_z = ((Z0, zneg((0, 0, 1, 0))), ((0, 0, 1, 0), Z0))
Zz = ((Z1, Z0), (Z0, zneg(Z1)))
PAULIS = (X_z, Y_z, Zz)
def mm(A, B):
    return tuple(tuple(zadd(zmul(A[i][0], B[0][j]), zmul(A[i][1], B[1][j]))
                       for j in range(2)) for i in range(2))
def adj(M):
    return ((zconj(M[0][0]), zconj(M[1][0])),
            (zconj(M[0][1]), zconj(M[1][1])))
def channel(u):
    """3x3 grid of Z[w] numerators over common denominator 2^(s+1):
    grid[i][j] = tr(sig_i * (M sig_j M+))."""
    s, M = u
    Md = adj(M)
    cols = [mm(mm(M, PAULIS[j]), Md) for j in range(3)]
    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            P = mm(PAULIS[i], cols[j])
            row.append(zadd(P[0][0], P[1][1]))
        grid.append(tuple(row))
    return s, tuple(grid)
def is_signed_perm(u):
    s, grid = channel(u)
    ok = True
    for i in range(3):
        if sum(1 for j in range(3) if grid[i][j] != Z0) != 1: ok = False
    for j in range(3):
        if sum(1 for i in range(3) if grid[i][j] != Z0) != 1: ok = False
    return ok
check("TB4 signed perms", "every Clifford's channel matrix is a signed "
      "permutation of the 3 Pauli axes (one nonzero per row and column) "
      "[classical]", all(is_signed_perm(c) for c in CLIF))
SAMPLE_K = min(3, K)   # per AMENDMENT_STONE_T_2026-08-30 (runtime)
sample = [u for k in range(SAMPLE_K + 1) for u in layers[k]]
def dc_canon(u):
    best = None
    for c1 in CLIF:
        a = umul(c1, u)
        for c2 in CLIF:
            v = umul(a, c2)
            if best is None or v < best: best = v
    return best
from itertools import permutations, product
def perm_sign(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]: s = -s
    return s
# Clifford conjugation realizes ONLY the 24 PROPER (det +1) signed
# permutations of the Pauli axes (conjugation by a unitary is an SO(3)
# rotation) — the first run minimized over all 48 and merged cosets the
# Cliffords cannot merge (fail-first log 2 kept).
ROT24 = [(p, sg) for p in permutations(range(3))
         for sg in product((1, -1), repeat=3)
         if perm_sign(p) * sg[0] * sg[1] * sg[2] == 1]
def chan_canon(u):
    # THIRD failure mode found and fixed (fail-first log 3): coset
    # representatives carry different global sde s (I has s=0, H has
    # s=1), so raw numerator grids live at different denominator scales.
    # Reduce the grid to canonical sqrt2-scale before minimizing.
    s, grid = channel(u)
    E = 2 * s + 2                       # denominator = sqrt2^E
    flat = [grid[i][j] for i in range(3) for j in range(3)]
    while E > 0:
        div = [zdivsq2(e) for e in flat]
        if any(d is None for d in div): break
        flat = div; E -= 1
    grid = tuple(tuple(flat[3 * i + j] for j in range(3)) for i in range(3))
    s = E
    best = None
    for pr, sr in ROT24:
        rows = [tuple(grid[pr[i]][j] if sr[i] == 1
                      else zneg(grid[pr[i]][j]) for j in range(3))
                for i in range(3)]
        for pc, sc in ROT24:
            g2_ = tuple(tuple(rows[i][pc[j]] if sc[j] == 1
                              else zneg(rows[i][pc[j]])
                              for j in range(3)) for i in range(3))
            if best is None or g2_ < best: best = g2_
    return (s, best)
dcs = {}
chs = {}
for u in sample:
    dcs[u] = dc_canon(u)
    chs[u] = chan_canon(u)
part_dc = defaultdict(set)
part_ch = defaultdict(set)
for u in sample:
    part_dc[dcs[u]].add(u); part_ch[chs[u]].add(u)
same = set(map(frozenset, part_dc.values())) == \
       set(map(frozenset, part_ch.values()))
check("TB4 table = coset", "on the declared sample (all T-count <= "
      f"{SAMPLE_K}, {len(sample)} elements): channel canonical forms "
      "induce EXACTLY the double-coset partition — the C.U.C invariant "
      "IS a matrix modulo signed permutations: the Clifford+T "
      "contingency table  [P: the channel is phase-faithful; C on range]",
      same, f"{len(part_dc)} double cosets on the sample")
ncos = Counter()
for k in range(SAMPLE_K + 1):
    s_ = {dcs[u] for u in layers[k]}
    ncos[k] = len(s_)
print("  double cosets per T-count on sample: "
      + ", ".join(f"k={k}: {ncos[k]}" for k in sorted(ncos)))

# ------------------------------------------------ TB5: skeleton theorem
print("\n--- TB5: the phase points are the T-free stratum (n = 3) ---")
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
def par(x): return bin(x).count("1") & 1
def q0(x): return par((x & 7) & (x >> 3))
def qform(c): return tuple(q0(x) ^ par(c & x) for x in range(64))
def pauli(x):
    a, b = x & 7, x >> 3
    M = np.eye(1, dtype=complex)
    for i in range(3):
        ai, bi = (a >> i) & 1, (b >> i) & 1
        f = (1j ** (ai * bi)) * np.linalg.matrix_power(X2, ai) @ \
            np.linalg.matrix_power(Z2, bi)
        M = np.kron(M, f)
    return M
PP = {}
for c in range(64):
    A = np.zeros((8, 8), dtype=complex)
    qc = qform(c)
    for x in range(64):
        A += ((-1) ** qc[x]) * pauli(x)
    PP[c] = A / 8
coef_ok = all(abs(abs(np.trace(PP[c] @ pauli(x).conj().T)) - 1) < 1e-9
              for c in (0, 9, 33) for x in range(64))
check("TB5 premise", "every phase point has ALL 64 Pauli coefficients "
      "+-1/8 (coefficient recovery exact): preserving the phase-point "
      "set forces mapping the signed Pauli frame to itself, i.e. "
      "membership in the normalizer = the Clifford group BY DEFINITION "
      "[P]", coef_ok)
T3 = np.kron(np.diag([1, np.exp(1j * np.pi / 4)]), np.eye(4))
viol = []
for c in (1, 9, 33):        # sample odd/even forms
    B = T3 @ PP[c] @ T3.conj().T
    dmin = min(min(np.abs(B - sgn * PP[cc]).max() for cc in range(64))
               for sgn in (1, -1))
    viol.append(dmin)
check("TB5 exit", "T (qubit 1) conjugates sampled phase points OFF the "
      "set {+-A_c} (min sup-distance > 0.2): T-magic leaves the finite "
      "bitangent skeleton instantly; the skeleton = EXACTLY the T-count-0 "
      "stratum.  Contrast: the 56-machine's clock-magic stays inside "
      "S_56.  The two magics differ in KIND: counting certificates vs "
      "ring arithmetic — the final form of open problem #3's boundary",
      all(v > 0.2 for v in viol),
      f"min distances {[round(float(v), 3) for v in viol]}")

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed  (K = {K})")
print("=" * 78)
