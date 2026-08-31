# verify_envelope_normalizer.py — THE 7<->6 ENVELOPE: EXACT NORMALIZER INDEX
# IB's open question on the 7<->6 envelope (bridge-table row 7<->6):
# inside G = Sp6(2) (order 1,451,520) with H = PSL(2,7) embedded transitive
# on the 28 odd forms (= 28 bitangents) with point stabilizer S3, compute
# the EXACT index [N_G(H) : H].  This decides canonicality of the envelope.
# Also verified: his reading "PSL(2,7)/S3 (28 points) is the restriction of
# the global Sp6(2)/P action" — i.e. H <= G transitive on the SAME 28-point
# set G acts on, with H-stabilizer = S3 = H ^ Stab_G(pt).
#
# ROUTE.  (1) G = Sp6(2) from the 3-qubit Clifford tableau (Stone Q's
# construction, reused verbatim); the 28-point action = odd quadratic-form
# labels.  (2) seeded uniform hunt (BSGS transversal sampling) for the
# bridge-class PSL(2,7): transitive on 28, stab S3, even-form orbits
# [1,7,7,21] (SM-003 / Stone F(b) / Stone Q fingerprint).  (3) restriction
# reading made explicit.  (4)+(5) FULL enumeration of all 1,451,520 elements
# via BSGS transversal products (Stone R's method, deg 28): exact C_G(H) and
# N_G(H) — test = conjugate H's two generators into the stored 168-element
# set.  (6) same pass, same test for the SECOND class (intransitive,
# Fano-doubled, orbits [7,21]) for contrast.  (7) verdict.
#
# Theory frame (stated, then MEASURED): H transitive with point stabilizer
# S3 that is SELF-NORMALIZING in H (L2(7) has no subgroup of order 12
# containing an S3: its order-12 subgroups are A4), so the centralizer of H
# in Sym(28) is already trivial => expect C_G(H) = 1.  Then N_G(H) = N/C
# embeds in Aut(PSL(2,7)) = PGL(2,7), so [N:H] divides 2: index 1 means H
# self-normalizing (rigid envelope), index 2 means the outer automorphism
# is ambient in G (N is a PGL(2,7)).
#
# Run:  python -X utf8 verify_envelope_normalizer.py
import random
from collections import Counter
import numpy as np

PASS = FAIL = 0
def check(tag, claim, ok, detail=""):
    global PASS, FAIL
    s = "PASS" if ok else "FAIL"
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{s}] {tag}: {claim}" + (f"  -> {detail}" if detail else ""))

print("=" * 78)
print("ENVELOPE NORMALIZER -- [N_G(H):H] for H = PSL(2,7) < G = Sp6(2) on 28")
print("=" * 78)

# ---------------------------------------------------------------- shared BSGS
def make_bsgs_full(gen_list, deg):
    """Deterministic incremental Schreier-Sims (Stone Q/R machinery).
    Returns (order, is_member, transversal chain)."""
    E = tuple(range(deg))
    def mulD(a, b): return tuple(a[b[k]] for k in range(deg))
    def invD(a):
        r = [0] * deg
        for i, x in enumerate(a): r[x] = i
        return tuple(r)
    strong = [g for g in gen_list if g != E]
    if not strong:
        return 1, (lambda g: g == E), []
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
                        base.append(next(p for p in range(deg) if h[p] != p))
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

def orbits_of(gens, pts):
    seen, out = set(), []
    for s0 in pts:
        if s0 in seen: continue
        orb = {s0}; q = [s0]
        while q:
            x = q.pop()
            for g in gens:
                y = g[x]
                if y not in orb: orb.add(y); q.append(y)
        seen |= orb
        out.append(sorted(orb))
    return out

def perm_order(p):
    seen, o = set(), 1
    for s0 in range(len(p)):
        if s0 in seen: continue
        L, x = 1, p[s0]
        seen.add(s0)
        while x != s0:
            seen.add(x); x = p[x]; L += 1
        o = o * L // __import__("math").gcd(o, L)
    return o

# --------------------------------------- 1: G = Sp6(2) and the 28-point set
print("\n--- 1: G = Sp6(2) on the 28 odd forms (Stone Q construction) ---")
def par(x): return bin(x).count("1") & 1
def q0(x): return par((x & 7) & (x >> 3))
def matvec(M, x):
    y = 0
    for i in range(6):
        if par(M[i] & x): y |= 1 << i
    return y
I6cols = [1 << i for i in range(6)]
def from_cols(cols):
    return tuple(sum(((cols[k] >> i) & 1) << k for k in range(6))
                 for i in range(6))
CLIF = {}
for i in range(3):                       # H_i : swap x_i <-> z_i
    cols = list(I6cols); cols[i], cols[i + 3] = cols[i + 3], cols[i]
    CLIF[f"H{i+1}"] = from_cols(cols)
for i in range(3):                       # S_i : z_i += x_i
    cols = list(I6cols); cols[i] = I6cols[i] ^ I6cols[i + 3]
    CLIF[f"S{i+1}"] = from_cols(cols)
for c in range(3):                       # CNOT c->t
    for t in range(3):
        if c == t: continue
        cols = list(I6cols)
        cols[c] = I6cols[c] ^ I6cols[t]
        cols[t + 3] = I6cols[t + 3] ^ I6cols[c + 3]
        CLIF[f"CX{c+1}{t+1}"] = from_cols(cols)
def mat_to_perm(M): return tuple(matvec(M, x) for x in range(64))
def perm_inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
SP_ORDER = 1451520
cl_perms = [mat_to_perm(M) for M in CLIF.values()]
oV, _, _ = make_bsgs_full(cl_perms, 64)
check("1a |G|", "the 12 Clifford tableau images generate order 1,451,520 "
      "= |Sp6(2)| on F2^6 (Stone Q's QB1 reproduced)", oV == SP_ORDER,
      f"order {oV}")

def qform(c): return tuple(q0(x) ^ par(c & x) for x in range(64))
zeros = [sum(1 for x in range(64) if qform(c)[x] == 0) for c in range(64)]
even_forms = [c for c in range(64) if zeros[c] == 36]
odd_forms = [c for c in range(64) if zeros[c] == 28]
check("1b Arf split", "64 refinements of omega = 36 even + 28 odd "
      "(the 28 Arf-invariant-1 forms = the 28 bitangents)",
      len(even_forms) == 36 and len(odd_forms) == 28)

def act_form_perm(Mperm_inv, c):
    tab = tuple(q0(Mperm_inv[x]) ^ par(c & Mperm_inv[x]) for x in range(64))
    cc = 0
    for k in range(6):
        if tab[1 << k] ^ q0(1 << k): cc |= 1 << k
    assert tab == qform(cc), "form action left the refinement family"
    return cc
label_gens = []
for p in cl_perms:
    pi = perm_inv(p)
    label_gens.append(tuple(act_form_perm(pi, c) for c in range(64)))
odd_idx = {c: i for i, c in enumerate(odd_forms)}
def rest28(p64):
    return tuple(odd_idx[p64[c]] for c in odd_forms)
G28gens = [rest28(p) for p in label_gens]
o28, memG28, TR28 = make_bsgs_full(G28gens, 28)
o64, memG64, TR64 = make_bsgs_full(label_gens, 64)
check("1c faithful on 28", "G acts on the 28 odd forms FAITHFULLY and "
      "TRANSITIVELY: 28-point order 1,451,520 = |G|; 64-label order agrees; "
      "first transversal = full orbit of size 28",
      o28 == SP_ORDER and o64 == SP_ORDER and len(TR28[0]) == 28,
      f"transversal chain sizes {[len(T) for T in TR28]}")

E28 = tuple(range(28))
E64 = tuple(range(64))
def mul28(a, b): return tuple(a[b[k]] for k in range(28))
def mul64(a, b): return tuple(a[b[k]] for k in range(64))
def inv28(a):
    r = [0] * 28
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def pow64(p, e):
    x = E64
    for _ in range(e): x = mul64(p, x)
    return x

# --------------------------------------- 2: the transitive H = PSL(2,7)
print("\n--- 2: the bridge-class H = PSL(2,7), transitive with stab S3 ---")
# uniform sampling: product of one random coset representative per BSGS
# level is a UNIFORM random element of G (deg-64 label action).
random.seed(20260831)
TLIST64 = [list(T.values()) for T in TR64]
def rand_elem64():
    g = E64
    for T in TLIST64:
        g = mul64(random.choice(T), g)
    return g

PSL_CENSUS = {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}     # PSL(2,7) order census
PGL_CENSUS = {1: 1, 2: 49, 3: 56, 4: 42, 6: 56, 7: 48, 8: 84}

def close_group(gens28):
    S = {E28}; frontier = [E28]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens28:
                b = mul28(g, a)
                if b not in S:
                    S.add(b); nxt.append(b)
        frontier = nxt
    return S

# one order-7 element c (Sp6(2) has a single class of order-7 elements;
# both PSL(2,7) classes contain such elements, so c serves both hunts)
c64 = None
for _ in range(20000):
    g = rand_elem64()
    o = perm_order(rest28(g))
    if o % 7 == 0:
        c64 = pow64(g, o // 7)
        break
c28 = rest28(c64)
check("2a order-7 seed", "an order-7 element of G found by uniform "
      "transversal sampling (seed 20260831)",
      c64 is not None and perm_order(c28) == 7)

ALLOWED = {1, 2, 3, 4, 7}          # the element orders of PSL(2,7)
foundH = foundK2 = None            # (x64, x28) for each class
tries = 0
while (foundH is None or foundK2 is None) and tries < 120000:
    tries += 1
    g = rand_elem64()
    r = rest28(g); o = perm_order(r)
    if o % 2: continue
    x64 = pow64(g, o // 2)
    x28 = rest28(x64)
    xc = mul28(x28, c28)
    if perm_order(xc) not in (3, 4, 7): continue
    comm = mul28(mul28(x28, c28), mul28(x28, inv28(c28)))   # x invol
    if perm_order(comm) not in ALLOWED: continue
    osz = sorted(len(t) for t in orbits_of([x28, c28], range(28)))
    if osz == [28] and foundH is None:
        got, _, _ = make_bsgs_full([x28, c28], 28)
        if got == 168:
            cen = Counter(perm_order(h) for h in close_group([x28, c28]))
            if dict(cen) == PSL_CENSUS:
                foundH = (x64, x28)
    elif osz == [7, 21] and foundK2 is None:
        got, _, _ = make_bsgs_full([x28, c28], 28)
        if got == 168:
            cen = Counter(perm_order(h) for h in close_group([x28, c28]))
            if dict(cen) == PSL_CENSUS:
                foundK2 = (x64, x28)
check("2b H found", f"a TRANSITIVE <x, c> of order 168 with the PSL(2,7) "
      f"order census {{1:1, 2:21, 3:56, 4:42, 7:48}} found "
      f"(after {tries} involution candidates)", foundH is not None)
xH64, xH28 = foundH
H168 = close_group([xH28, c28])
Hset = frozenset(H168)
check("2c |H| = 168", "the closure of <x, c> enumerated: exactly 168 "
      "elements, PSL(2,7) census confirmed on the full list",
      len(H168) == 168 and
      dict(Counter(perm_order(h) for h in H168)) == PSL_CENSUS)
p0 = 0                                       # base point (first odd form)
stabH = [h for h in H168 if h[p0] == p0]
stab_orders = sorted(perm_order(h) for h in stabH)
nonab = any(mul28(a, b) != mul28(b, a) for a in stabH for b in stabH)
check("2d stab = S3", "the H-stabilizer of a point has order 6, element "
      "orders {1,2,2,2,3,3}, NONABELIAN => S3 (the shared S3 of SM-003)",
      len(stabH) == 6 and stab_orders == [1, 2, 2, 2, 3, 3] and nonab)
horb = sorted(len(t) for t in orbits_of([xH28, c28], range(28)))
even_orb = sorted(len(t) for t in orbits_of([xH64, c64], even_forms))
check("2e fingerprint", "H transitive on the 28 ([28]) with even-form "
      "orbits [1,7,7,21] — the bridge-class fingerprint of Stone F(b) / "
      "Stone Q lands intact", horb == [28] and even_orb == [1, 7, 7, 21],
      f"odd orbits {horb}, even orbits {even_orb}")

# --------------------------------------- 3: the restriction reading
print("\n--- 3: PSL(2,7)/S3 as the restriction of the Sp6(2)/P action ---")
check("3a same set", "H's two generators pass the BSGS membership strip "
      "for G's 28-point action: H <= G acting on the SAME 28 points "
      "(no relabeling, the literal same set)",
      memG28(xH28) and memG28(c28))
# Stab_G(p0) by Schreier generators (Stone Q's QB5 machinery)
transv0 = {p0: E28}
qd = [p0]
while qd:
    x = qd.pop(0)
    for g in G28gens:
        if g[x] not in transv0:
            transv0[g[x]] = mul28(g, transv0[x])
            qd.append(g[x])
Sgens = set()
for x, ux in transv0.items():
    for g in G28gens:
        sg = mul28(inv28(transv0[g[x]]), mul28(g, ux))
        if sg != E28: Sgens.add(sg)
oStab, memStab, _ = make_bsgs_full(list(Sgens), 28)
check("3b Stab_G(pt)", "the G-point stabilizer P has order 51,840 = "
      "|W(E6)| = |U4(2):2| — the parabolic of the global 28-point action "
      "[classical]", oStab == 51840 and len(transv0) == 28)
inter = [h for h in H168 if memStab(h)]
check("3c H ^ P = S3", "H ^ Stab_G(pt) computed two ways agrees: the "
      "elements of H inside P are EXACTLY the 6-element S3 of 2d — the "
      "H-stabilizer IS the intersection with the G-stabilizer",
      sorted(inter) == sorted(stabH) and len(inter) == 6)
fibers = Counter(h[p0] for h in H168)
check("3d H/S3 = X28", "the coset map h*S3 -> h(pt) is onto all 28 points "
      "with every fiber of size exactly 6 = |S3|: H/S3 = X28 as H-sets, "
      "168/6 = 28 — IB's reading VERIFIED: PSL(2,7)/S3 is the restriction "
      "of the global Sp6(2)/P action to the subgroup H",
      len(fibers) == 28 and set(fibers.values()) == {6}
      and 168 // 6 == 28)

# --------------------------------------- 4+5: FULL enumeration of G
print("\n--- 4+5: C_G(H) and N_G(H) by full enumeration (1,451,520) ---")
# Theory frame (measured below, never assumed): S3 is self-normalizing in
# PSL(2,7) (order-12 subgroups of L2(7) are A4, containing no S3), and H
# is transitive, so the centralizer of H in ALL of Sym(28) is already
# trivial => expect C_G(H) = 1.  Then N_G(H) = N_G(H)/C_G(H) embeds in
# Aut(PSL(2,7)) = PGL(2,7) of order 336 => [N:H] divides 2.
L = [np.array([list(p) for p in T.values()], dtype=np.uint8)
     for T in TR28]
Ppart = L[-1]
for j in range(len(L) - 2, 0, -1):
    Ppart = np.concatenate([L[j][i][Ppart] for i in range(L[j].shape[0])])
tot = Ppart.shape[0] * L[0].shape[0]
check("5a enumeration size", "BSGS transversal products enumerate all "
      "1,451,520 elements of G, each exactly once (Stone R's method, "
      "deg 28)", tot == SP_ORDER,
      f"{L[0].shape[0]} chunks x {Ppart.shape[0]} rows")

# hash filter: g in N_G(H)  <=>  g c g^-1 in H  AND  g x g^-1 in H
# (conjugation is an automorphism, so it maps <x,c> onto a subgroup of H
# of full order 168 = H).  Filter on the order-7 generator first — only
# ~|C_G(c)| * 48 elements of G conjugate c into H — then confirm the
# survivors EXACTLY (tuple membership, no hash trust) and test x.
rng = random.Random(7)
W = np.array([rng.getrandbits(62) for _ in range(28)], dtype=np.uint64)
def key_of(t): return int((np.array(t, dtype=np.uint64) * W).sum())
Hkeys = np.array(sorted({key_of(h) for h in H168}), dtype=np.uint64)
cH = np.array(c28, dtype=np.uint8)
if foundK2 is not None:
    xK64, xK28 = foundK2
    K2 = close_group([xK28, c28])
    K2set = frozenset(K2)
    K2keys = np.array(sorted({key_of(h) for h in K2}), dtype=np.uint64)
NH, CH, NK2, CK2 = [], [], [], []
processed = 0
for i in range(L[0].shape[0]):
    chunk = L[0][i][Ppart]                       # rows g = t0 o p
    processed += chunk.shape[0]
    Ginv = np.argsort(chunk, axis=1)             # rows g^-1
    B = cH[Ginv]                                 # rows c(g^-1(.))
    conj = np.take_along_axis(chunk, B.astype(np.intp), axis=1)
    keys = (conj.astype(np.uint64) * W).sum(axis=1)
    for r in np.nonzero(np.isin(keys, Hkeys))[0]:
        cc = tuple(int(v) for v in conj[r])
        if cc not in Hset: continue              # hash false positive
        g = tuple(int(v) for v in chunk[r])
        gi = inv28(g)
        xx = mul28(g, mul28(xH28, gi))
        if xx in Hset:
            NH.append(g)
            if cc == c28 and xx == xH28: CH.append(g)
    if foundK2 is not None:
        keys2 = keys                             # same conj rows, K2 shares c
        for r in np.nonzero(np.isin(keys2, K2keys))[0]:
            cc = tuple(int(v) for v in conj[r])
            if cc not in K2set: continue
            g = tuple(int(v) for v in chunk[r])
            gi = inv28(g)
            xx = mul28(g, mul28(xK28, gi))
            if xx in K2set:
                NK2.append(g)
                if cc == c28 and xx == xK28: CK2.append(g)
check("5b full pass", "all 1,451,520 elements processed; the test "
      "(conjugate BOTH generators into the stored 168-element set) is "
      "exact — hash prefilter on the order-7 generator, every survivor "
      "verified by literal tuple membership", processed == SP_ORDER)
check("4 CENTRALIZER", "C_G(H) = 1: the ONLY element of G commuting with "
      "both generators of H is the identity — as forced by transitivity + "
      "self-normalizing S3 stabilizer (centralizer already trivial in "
      "Sym(28)), now MEASURED over the full group",
      len(CH) == 1 and CH[0] == E28, f"|C_G(H)| = {len(CH)}")
NHset = set(NH)
idxN = len(NH) // 168 if len(NH) % 168 == 0 else None
check("5c NORMALIZER", f"N_G(H) computed exhaustively: |N_G(H)| = "
      f"{len(NH)}, contains all 168 elements of H, and [N_G(H):H] = "
      f"{idxN} — the EXACT index", len(NH) % 168 == 0
      and all(h in NHset for h in H168), f"index {idxN}")
# identify N when the outer automorphism is ambient
if len(NH) == 336:
    n_out = next(g for g in NH if g not in Hset)
    closedN = all(mul28(a, b) in NHset for a in [xH28, c28, n_out]
                  for b in NH)
    cenN = dict(Counter(perm_order(g) for g in NH))
    check("5d N = PGL(2,7)", "the 336-element N_G(H) is closed under "
          "composition, and C_G(H) = 1 embeds N into Aut(PSL(2,7)) = "
          "PGL(2,7) with FULL order => N_G(H) = PGL(2,7); order census "
          "matches PGL(2,7) {1:1, 2:49, 3:56, 4:42, 6:56, 7:48, 8:84} — "
          "the outer automorphism of the Klein quartic group is AMBIENT "
          "in Sp6(2)", closedN and cenN == PGL_CENSUS,
          f"census {cenN}")
elif len(NH) == 168:
    check("5d N = H", "N_G(H) = H: H is SELF-NORMALIZING in G — the "
          "outer automorphism of PSL(2,7) is NOT realized inside Sp6(2) "
          "on this class", sorted(NH) == sorted(H168))
else:
    check("5d identify N", "N_G(H) has an order compatible with "
          "N/C <= Aut(PSL(2,7))", False, f"|N| = {len(NH)} UNEXPECTED")

# --------------------------------------- 6: the second (intransitive) class
print("\n--- 6: contrast — the SECOND class (Fano-doubled, orbits [7,21]) ---")
if foundK2 is None:
    print("  NOT RUN: no intransitive PSL(2,7) surfaced within the "
          f"{tries}-candidate hunt budget; the contrast column is left "
          "open, explicitly (nothing silently dropped).")
else:
    k2orb = sorted(len(t) for t in orbits_of([xK28, c28], range(28)))
    k2even = sorted(len(t) for t in orbits_of([xK64, c64], even_forms))
    check("6a K2 found", "a SECOND PSL(2,7) (order 168, PSL census), "
          "INTRANSITIVE on the 28 with orbits [7,21] — Stone F(b)'s "
          "Fano-doubled class", k2orb == [7, 21],
          f"odd orbits {k2orb}, even orbits {k2even} [obs]")
    not_conj = xK28 not in Hset            # cheap witness of distinctness
    idxN2 = len(NK2) // 168 if len(NK2) % 168 == 0 else None
    cenN2 = dict(Counter(perm_order(g) for g in NK2))
    check("6b K2 normalizer", f"same exhaustive test on the same full "
          f"pass: |C_G(K2)| = {len(CK2)}, |N_G(K2)| = {len(NK2)}, "
          f"[N_G(K2):K2] = {idxN2}",
          len(CK2) == 1 and len(NK2) % 168 == 0
          and all(h in set(NK2) for h in K2),
          f"index {idxN2}; N_K2 order census {cenN2}")

# --------------------------------------- 7: verdict
print("\n--- 7: verdict — the canonicality of the 7<->6 envelope ---")
if idxN == 1:
    verdict = ("[N_G(H):H] = 1: H is SELF-NORMALIZING.  The envelope is "
               "RIGID — the transitive PSL(2,7) sits in Sp6(2) with no "
               "ambient symmetry beyond its own; the 7<->6 row's left "
               "group admits no canonical enlargement inside the global "
               "28-point geometry.")
elif idxN == 2:
    verdict = ("[N_G(H):H] = 2: N_G(H) = PGL(2,7).  The outer "
               "automorphism of the Klein-quartic group is AMBIENT in "
               "Sp6(2) — the envelope is canonical only up to that "
               "involution: the global geometry sees H together with its "
               "outer flip as one object, and any construction natural in "
               "G is PGL(2,7)-equivariant, not merely PSL(2,7)-"
               "equivariant.")
else:
    verdict = f"[N_G(H):H] = {idxN}: OUTSIDE the theory frame — re-examine."
print("  " + verdict)
print(f"  (Centralizer measured: |C_G(H)| = {len(CH)}; frame N/C <= "
      "Aut(PSL(2,7)) = PGL(2,7) therefore held with room to spare.)")
if foundK2 is not None:
    print(f"  Contrast class: [N_G(K2):K2] = {idxN2} for the intransitive "
          "(Fano-doubled) copy — "
          + ("the two classes agree in normalizer index."
             if idxN2 == idxN else
             "the two classes DIFFER in normalizer index: transitivity "
             "is not a spectator here."))

print("\n" + "=" * 78)
print(f"RESULT: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
