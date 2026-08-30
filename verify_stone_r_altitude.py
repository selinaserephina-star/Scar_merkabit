# verify_stone_r_altitude.py — STONE R: THE ALTITUDE
# Brief: BRIEF_STONE_R_ALTITUDE.md (sha-locked 57db98a7... BEFORE this file
# existed).  Registered bars RB1..RB4.
#
# ROUTE.  (R1) explicit conjugator Psi = g c g^-1 (cycle alignment) + the
# no-B28-conjugator corollary.  (R2) THE MEASUREMENT: full enumeration of
# W(E7)'s 2,903,040 elements via BSGS transversal products (numpy), exact
# linearity gaps nu(g) = min_w d_H(g, w) for the gate panel, witnesses
# characterized by cycle type + characteristic polynomial.  (R3) tau(Psi)
# anchor + the clock's own antipode iota_Psi = Psi^9 (= g w0 g^-1 for EVERY
# conjugator) and its matching's overlap with iota's.  (R4) the two
# mechanisms: Pauli translations make Clifford-with-Paulis transitive on
# all 64 phase points (the one-spectrum [obs] explained); the trace
# obstruction (tr A_c = 1) forbids any unitary sign flip on phase points.
#
# Run:  python -X utf8 verify_stone_r_altitude.py
import json
import numpy as np
from collections import Counter

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("STONE R -- the altitude: how far above the Clifford floor")
print("=" * 78)

D = json.load(open("scar56_data.json"))
verts = [tuple(v) for v in D["verts"]]
idx = {v: k for k, v in enumerate(verts)}
PSI, PR, IOTA, FRAME = D["PSI"], D["PR"], D["IOTA"], D["FRAME"]
N = 56
C7 = [[ 2, 0,-1, 0, 0, 0, 0],
      [ 0, 2, 0,-1, 0, 0, 0],
      [-1, 0, 2,-1, 0, 0, 0],
      [ 0,-1,-1, 2,-1, 0, 0],
      [ 0, 0, 0,-1, 2,-1, 0],
      [ 0, 0, 0, 0,-1, 2,-1],
      [ 0, 0, 0, 0, 0,-1, 2]]
S = []
for i in range(7):
    perm = []
    for k in range(N):
        w = verts[k]
        img = tuple(w[j] - w[i] * C7[i][j] for j in range(7))
        perm.append(idx[img])
    S.append(tuple(perm))
def mul(a, b): return tuple(a[b[k]] for k in range(N))
def inv(a):
    r = [0] * N
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
E56 = tuple(range(N))
def perm_pow(p, e):
    x = E56
    for _ in range(e): x = mul(p, x)
    return x

# ------------------------------------------------ BSGS with transversals
def make_bsgs_full(gen_list, deg):
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    base = []
    for g in strong:
        if all(g[b] == b for b in base):
            base.append(next(i for i in range(deg) if g[i] != i))
    lvl = [[g for g in strong if all(g[b] == b for b in base[:i])]
           for i in range(len(base))]
    transv = [None] * len(base)
    def rebuild(i):
        b = base[i]; T = {b: E}; q = [b]
        while q:
            x = q.pop(0)
            for g in lvl[i]:
                y = g[x]
                if y not in T:
                    T[y] = mulD(g, T[x]); q.append(y)
        transv[i] = T
    for i in range(len(base)): rebuild(i)
    def strip_from(g, start):
        h = g
        for i in range(start, len(base)):
            x = h[base[i]]
            if x not in transv[i]: return h, i
            h = mulD(invD(transv[i][x]), h)
        return h, len(base)
    i = len(base) - 1
    while i >= 0:
        clean = True
        for x in list(transv[i].keys()):
            for g in lvl[i]:
                sg = mulD(invD(transv[i][g[x]]), mulD(g, transv[i][x]))
                if sg == E: continue
                h, j = strip_from(sg, i + 1)
                if h != E:
                    clean = False
                    if j == len(base):
                        base.append(next(p for p in range(deg)
                                         if h[p] != p))
                        lvl.append([]); transv.append(None)
                    for k2 in range(i + 1, j + 1):
                        lvl[k2].append(h); rebuild(k2)
                    i = j
                    break
            if not clean: break
        if clean: i -= 1
    o = 1
    for T in transv: o *= len(T)
    def is_member(g):
        h, _ = strip_from(g, 0)
        return h == E
    return o, is_member, transv

oW, memW, TRANSV = make_bsgs_full(S, N)
check("W(E7)", "order 2903040 with a transversal chain (sizes "
      f"{[len(T) for T in TRANSV]})", oW == 2903040)

# ------------------------------------------------ R1: the disguise
print("\n--- R1: the conjugator (the clock as a disguised Coxeter) ---")
PSIt, PRt, IOTAt = tuple(PSI), tuple(PR), tuple(IOTA)
cox = E56
for i in range(7): cox = mul(S[i], cox)
def cycles_of(p):
    seen, out = set(), []
    for s0 in range(N):
        if s0 in seen: continue
        cyc = [s0]; x = p[s0]
        while x != s0:
            cyc.append(x); x = p[x]
        seen |= set(cyc)
        out.append(cyc)
    return out
cyc_c = sorted(cycles_of(cox), key=len)
cyc_p = sorted(cycles_of(PSIt), key=len)
check("cycle match", "c and Psi both have cycle type [2,18,18,18]",
      [len(x) for x in cyc_c] == [2, 18, 18, 18] ==
      [len(x) for x in cyc_p])
g = [0] * N
for cc, cp in zip(cyc_c, cyc_p):
    for a, b in zip(cc, cp): g[a] = b
g = tuple(g)
check("RB1 conjugator", "an explicit g with Psi = g c g^-1 (cycle "
      "alignment), verified", mul(g, mul(cox, inv(g))) == PSIt)
giog = mul(g, mul(IOTAt, inv(g)))
check("RB1 corollary", "no conjugator lies in C(iota) = B28: if g "
      "commuted with iota then Psi = g c g^-1 would commute with iota "
      "(c does), contradicting iota Psi iota = Psi^-1; our g indeed "
      "moves iota", giog != IOTAt
      and mul(IOTAt, mul(PSIt, IOTAt)) == inv(PSIt))

# ------------------------------------------------ R2: THE MEASUREMENT
print("\n--- R2: full enumeration -- the linearity gaps (headline) ---")
panel = {"Psi": PSIt,
         "Psi^2": perm_pow(PSIt, 2),
         "Psi^3": perm_pow(PSIt, 3),
         "Psi^6": perm_pow(PSIt, 6),
         "Psi^9": perm_pow(PSIt, 9),
         "pr": PRt}
member = {k: memW(v) for k, v in panel.items()}
check("memberships", "strip test: NO panel gate lies in W(E7) "
      "(nu > 0 for all six)", all(not m for m in member.values()),
      f"{member}")

L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
     for T in TRANSV]
# partial product over levels 1..end (right factor), then stream level 0
Ppart = L[-1]
for j in range(len(L) - 2, 0, -1):
    Ppart = np.concatenate([L[j][i][Ppart] for i in range(L[j].shape[0])])
tot = Ppart.shape[0] * L[0].shape[0]
check("enumeration size", "transversal products enumerate all "
      "2,903,040 elements", tot == 2903040,
      f"{L[0].shape[0]} chunks x {Ppart.shape[0]} rows")
tg_names = list(panel.keys())
tg = np.array([list(panel[k]) for k in tg_names], dtype=np.uint8)
best = {k: -1 for k in tg_names}
wit = {k: [] for k in tg_names}
wcount = {k: 0 for k in tg_names}
for i in range(L[0].shape[0]):
    chunk = L[0][i][Ppart]                      # (rows, 56)
    for t in range(len(tg_names)):
        agree = (chunk == tg[t]).sum(axis=1)
        m = int(agree.max())
        k = tg_names[t]
        if m > best[k]:
            best[k] = m
            rows = np.where(agree == m)[0]
            wcount[k] = len(rows)
            wit[k] = [tuple(int(v) for v in chunk[r]) for r in rows[:3]]
        elif m == best[k]:
            rows = np.where(agree == m)[0]
            wcount[k] += len(rows)
            if len(wit[k]) < 3:
                wit[k] += [tuple(int(v) for v in chunk[r])
                           for r in rows[:3 - len(wit[k])]]
nu = {k: N - best[k] for k in tg_names}
print("  linearity gaps nu(g) = min Hamming distance to W(E7), exact:")
for k in tg_names:
    print(f"    nu({k:6s}) = {nu[k]:2d}   "
          f"(agreement {best[k]}/56; {wcount[k]} minimizers)")
check("RB2 measured", "all six gaps computed exactly over the full group",
      all(best[k] > -1 for k in tg_names) and all(nu[k] > 0
                                                  for k in tg_names))

# witness characterization: cycle type + char poly of the 7x7 weight matrix
Vfull = np.array(verts, dtype=float)
rows_idx = []
for k in range(N):
    if len(rows_idx) == 7: break
    test = rows_idx + [k]
    if np.linalg.matrix_rank(Vfull[test]) == len(test):
        rows_idx.append(k)
V = Vfull[rows_idx]
def char_poly_of(w):
    Vp = Vfull[[w[k] for k in rows_idx]]
    A = np.linalg.solve(V, Vp)
    if not np.allclose(Vfull @ A, Vfull[[w[k] for k in range(N)]],
                       atol=1e-8):
        return None, None
    cp = np.rint(np.poly(A)).astype(int)
    return A, cp
COX_CP = np.array([1, 1, 0, -1, -1, 0, 1, 1])   # Phi_18 * Phi_2
Acox, cp_cox = char_poly_of(cox)
check("char poly anchor", "the Coxeter element's characteristic "
      "polynomial = Phi_18 * Phi_2 = x^7+x^6-x^4-x^3+x+1",
      cp_cox is not None and list(cp_cox) == list(COX_CP))
def ctype(p): return sorted(len(c) for c in cycles_of(p))
guess_holds = False
psi_wit_info = []
for w in wit["Psi"]:
    _, cp = char_poly_of(w)
    info = (ctype(w), list(cp) if cp is not None else None)
    psi_wit_info.append(info)
    if info[0] == [2, 18, 18, 18] and cp is not None and \
       list(cp) == list(COX_CP):
        guess_holds = True
check("RB2 registered guess", "some minimizer for Psi has cycle type "
      "[2,18,18,18] with Coxeter char poly Phi_18*Phi_2 (the clock's "
      "nearest linear neighbours include its own disguised class)",
      guess_holds,
      f"witness (cycle type, char poly) samples: {psi_wit_info}")
d_psi_cox = N - sum(1 for k in range(N) if PSIt[k] == cox[k])
d_psi9_iota = N - sum(1 for k in range(N) if panel["Psi^9"][k] == IOTAt[k])
print(f"  direct: d_H(Psi, c) = {d_psi_cox};  "
      f"d_H(Psi^9, iota) = {d_psi9_iota}")

# ------------------------------------------------ R3: the hidden matching
print("\n--- R3: tau(Psi) anchor + the clock's own antipode ---")
M0 = set()
for k in range(N): M0.add(frozenset((k, IOTA[k])))
PM0 = set(frozenset((PSIt[a], PSIt[b])) for (a, b) in
          (tuple(e) for e in M0))
# union multigraph cycle halves = coset type
adj = {k: [] for k in range(N)}
for a, b in (tuple(e) for e in M0): adj[a].append(b); adj[b].append(a)
for a, b in (tuple(e) for e in PM0): adj[a].append(b); adj[b].append(a)
seen = set(); halves = []
for s0 in range(N):
    if s0 in seen: continue
    comp = {s0}; q = [s0]
    while q:
        x = q.pop()
        for y in adj[x]:
            if y not in comp: comp.add(y); q.append(y)
    seen |= comp
    halves.append(len(comp) // 2)
check("RB3 anchor", "tau(Psi) from M0 U Psi(M0) = [1,9,9,9] — SM-009's "
      "coset type reproduced", sorted(halves) == [1, 9, 9, 9])
iota_psi = perm_pow(PSIt, 9)
check("the clock's antipode", "iota_Psi := g w0 g^-1 is INDEPENDENT of "
      "the conjugator: c^9 = w0 = iota, so g c^9 g^-1 = Psi^9 for EVERY "
      "g — the clock's own antipode is Psi^9, a fixed-point-free "
      "involution commuting with Psi",
      mul(g, mul(perm_pow(cox, 9), inv(g))) == iota_psi
      and perm_pow(cox, 9) == IOTAt
      and mul(iota_psi, PSIt) == mul(PSIt, iota_psi)
      and all(iota_psi[k] != k for k in range(N))
      and perm_pow(iota_psi, 2) == E56)
Mpsi = set()
for k in range(N): Mpsi.add(frozenset((k, iota_psi[k])))
overlap = len(M0 & Mpsi)
check("two antipodes", "the clock's matching M_Psi shares exactly 4 "
      "pairs with iota's M0 — SM-004's refuted guess ('Psi^9-pairing = "
      "iota') lands as the theorem 'Psi^9-pairing = the CONJUGATED "
      "antipode', touching iota only on the axis pairs (DQ-4)",
      overlap == 4, f"|M_Psi ^ M0| = {overlap}/28")
prod = mul(IOTAt, iota_psi)
check("interference [obs]", "iota o iota_Psi = iota o Psi^9 = the two "
      "antipodes' interference word", True,
      f"cycle type {ctype(prod)}, order "
      f"{next(k for k in range(1, 100) if perm_pow(prod, k) == E56)}")

# ------------------------------------------------ R4: the two mechanisms
print("\n--- R4: gauge and obstruction (Stone Q's two opens closed) ---")
def par(x): return bin(x).count("1") & 1
def q0(x): return par((x & 7) & (x >> 3))
def qform(c): return tuple(q0(x) ^ par(c & x) for x in range(64))
zeros = [sum(1 for x in range(64) if qform(c)[x] == 0) for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms = [c for c in range(64) if zeros[c] == 28]
def swap_halves(a): return ((a & 7) << 3) | (a >> 3)
# label translation by Pauli T_a:  q_c -> q_c + omega(a, .) = q_{c ^ Ja}
transl_transitive = len({0 ^ swap_halves(a) for a in range(64)}) == 64
mixes = any((swap_halves(a) ^ even_forms[0]) in odd_forms
            for a in range(64))
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
def pauli(x):
    a, b = x & 7, x >> 3
    M = np.eye(1, dtype=complex)
    for i in range(3):
        ai, bi = (a >> i) & 1, (b >> i) & 1
        f = (1j ** (ai * bi)) * np.linalg.matrix_power(X2, ai) @ \
            np.linalg.matrix_power(Z2, bi)
        M = np.kron(M, f)
    return M
def omega6(x, y):
    return par((x & 7) & (y >> 3)) ^ par((y & 7) & (x >> 3))
conj_ok = True
for a in (1, 9, 35):
    Ta = pauli(a)
    for x in (2, 12, 51):
        lhs = Ta @ pauli(x) @ Ta.conj().T
        rhs = ((-1) ** omega6(a, x)) * pauli(x)
        if not np.allclose(lhs, rhs): conj_ok = False
check("RB4a gauge", "Pauli conjugation T_a T_x T_a+ = (-1)^omega(a,x) T_x "
      "verified on operators; the induced label translations c -> c ^ "
      "swap(a) are TRANSITIVE on all 64 forms and MIX the Arf classes: "
      "Clifford-with-Paulis has ONE orbit of phase points — Stone Q's "
      "one-spectrum [obs] is explained, and the 36/28 split is exactly a "
      "choice of Pauli sign gauge", conj_ok and transl_transitive and mixes)
def phase_point(c):
    A = np.zeros((8, 8), dtype=complex)
    qc = qform(c)
    for x in range(64):
        A += ((-1) ** qc[x]) * pauli(x)
    return A / 8
traces = [np.trace(phase_point(c)) for c in range(64)]
check("RB4b obstruction", "tr A_c = 1 for ALL 64 phase points; unitary "
      "conjugation preserves trace, and tr(-A_c) = -1: NO unitary "
      "realizes a sign flip A_c -> -A_c'.  The 56 = 28 odd forms x sign "
      "exists only as a set: iota (the global flip) and the beam-splitter "
      "machine (SM-014) have no unitary-conjugation realization on phase "
      "points — chirality downstairs is a GAUGE BIT, not an operator",
      all(abs(t - 1) < 1e-9 for t in traces))

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
