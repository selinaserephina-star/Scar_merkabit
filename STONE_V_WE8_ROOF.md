# STONE V — THE ROOF: both towers under W⁺(E₈)

**Run 2026-09-01 · verifier `verify_stone_v_we8_roof.py` · log
`verify_stone_v_we8_roof.log` · 44 checks, 44 PASS, 0 FAIL · 4.9 s from
caches · brief `BRIEF_STONE_V_WE8_ROOF.md`, lock verified in-run (V0,
sha `da1d02c2…e18b29`).**

## §0 Discipline

Computed, not asserted: every claim below carries a check number from the
log; sealed Stone U machinery was reloaded read-only and re-verified by
membership strips before use (V1a–V1i), with C-perfect and H-perfect
recomputed fresh in this run's own cache. The registered expectation
(VB2: K = ⟨C,H⟩ at most W⁺(E₈)) was resolvable INVERTED at equal
prominence and is resolved at its registered status: **PASS**.
Exhaustive claims are scoped where they stand; "minimal-found" is never
upgraded to "minimal". Not RH/GRH; no physical identification (Rule 3).
No registry/git writes by the executor.

## One paragraph

Both towers live inside W(E₈), and the smallest overgroup found to hold
them both is exactly the rotation subgroup **W⁺(E₈) = ker(det), order
348 364 800, index 2**: the joint closure K = ⟨C, H⟩ of the sealed
vector-type complement C ≅ Sp₆(2) and the sealed spin preimage
H ≅ 2·Sp₆(2) equals W⁺(E₈) on the nose (V4d), the spine (PSL(2,7),
C₆×ℤ₂, A₅, S₄, A₄, ℤ₂) sits in C with explicit presentation witnesses
(V2c–V2h), the Schur tower (SL(2,7), 2I, GL(2,3), 2O, 2T, plus C₃×D₄,
2·W(E₆), 2×PGL(2,7) and the free split covers Ih, Th) sits in H with
every member over the single central ℤ₂ = ⟨−1_{E₈}⟩ = z_H (V3a–V3j,
V5a–V5c), and neither tested reduction descends below W⁺: [K,K] = K
exactly (K is perfect, V4f) and even the 21 witness generators alone
regenerate all of W⁺ (K₂, V4g). The hinge survives into the roof
unchanged — spine beside the centre, Schur tower over it — and
R/⟨−1⟩ has order 174 182 400 = |O₈⁺(2)| (identification by order only,
V4j). True minimality over all subgroups is not proven.

## Bars

### VB1 — assembly with witnesses: **PASS** (16/16 members)

Spine inside C ≅ Sp₆(2) (the vector-type complement, sealed V1d; all
generators verified in C by membership strip):

| member | order | witness | fingerprint | status |
|---|---|---|---|---|
| PSL(2,7) | 168 | presentation hunt a²=b³=(ab)⁷=1 (V2c) | profile {1:1, 2:21, 3:56, 4:42, 7:48} = Möbius PSL(2,7) | PASS |
| C₆×ℤ₂ | 12 | commuting (6,2) pair, b ∉ ⟨a⟩ (V2g) | abelian, profile {1:1, 2:3, 3:2, 6:6} | PASS |
| A₅ | 60 | (2,3,5) pair (V2d) | profile {1:1, 2:15, 3:20, 5:24} | PASS |
| S₄ | 24 | (2,3,4) pair (V2e) | profile {1:1, 2:9, 3:8, 4:6} | PASS |
| A₄ | 12 | derived subgroup of the S₄ witness (V2f) | profile {1:1, 2:3, 3:8} | PASS |
| ℤ₂ | 2 | pool involution fixing α (V2h) | order 2, ≠ −1 | PASS |

Schur tower inside H ≅ 2·Sp₆(2) (sealed Stone U witnesses re-lifted
through the sealed shadow chain and re-classified; every witness
verified ⊂ H and containing −1):

| member | order | #involutions | decisive fingerprint | status |
|---|---|---|---|---|
| SL(2,7) | 336 | 1 (= −1) | order-14 elements, profile = SL(2,7) (V3a) | PASS |
| 2I = SL(2,5) | 120 | 1 (= −1) | profile = SL(2,5) (V3b) | PASS |
| GL(2,3) = 2·S₄ | 48 | 13 | transpositions lift to involutions (V3c) | PASS |
| 2O | 48 | 1 (= −1) | transpositions lift to order 4 (V3d) | PASS |
| 2T = SL(2,3) | 24 | 1 (= −1) | profile = SL(2,3) (V3e) | PASS |
| C₃×D₄ | 24 | 5 | stem over the D₄ part (V3f) | PASS |
| 2·W(E₆) | 103 680 | — | −1 in the derived subgroup: non-split (sealed chains re-verified, V3g) | PASS |
| 2×PGL(2,7) | 672 | 99 | split-double of PGL(2,7) profile (V3h) | PASS |
| Ih = ⟨−1⟩×A₅ | 120 | 31 | split cover, free inside ⟨−1⟩×C (V3i) | PASS |
| Th = ⟨−1⟩×A₄ | 24 | 7 | split cover, free inside ⟨−1⟩×C (V3j) | PASS |

### VB2 — the minimal roof: **PASS** (registered expectation CONFIRMED)

- Evenness instrument first (per brief): exact integer 8×8 matrices in
  the simple-root basis reproduce the 240-root action; Bareiss det = −1
  = permutation parity on all 8 simple reflections (V4a); −1_{E₈} has
  matrix −I, det +1 (dim 8 even) (V4b). Every generator of K has exact
  det +1 AND parity +1, the two instruments agreeing generator by
  generator (V4c).
- **K = ⟨C, H⟩ has order 348 364 800 = |W(E₈)|/2 and equals W⁺(E₈)
  exactly** (all generators even ⇒ K ≤ ker(det); equal order closes it)
  — index 2 in W(E₈), proper (V4d). Registered expectation resolved
  **PASS** at its registered site.
- Minimization (a): **[K,K] = K exactly** — C perfect and H perfect
  (both recomputed fresh, V1h/V1i) give K = ⟨[C,C],[H,H]⟩ ≤ [K,K];
  spot-checked by 24 random commutators regenerating order 348 364 800
  (V4f). Both towers ⊂ [K,K] since [K,K] = K; C ≤ [K,K] and H ≤ [K,K]
  verified by membership (V4e).
- Minimization (b): **K₂ = ⟨witness generators only⟩ (21 generators: one
  full spine chain in C + one full Schur chain in H + −1) already has
  order 348 364 800 = |W⁺|** (V4g, V4h) — the leaner closure does not
  descend either.
- (c) **Minimal-found roof: R = W⁺(E₈), order 348 364 800, index 2 in
  W(E₈)** (V4i). Scope word: minimal-FOUND over the tested overgroups
  {K, [K,K], K₂}; true minimality over all subgroups of W(E₈) is NOT
  proven.

### VB3 — the two centres: **PASS**

- **z_H = −1_{E₈}**, verified explicitly: −1 ∈ H, central; Z(K̄) computed
  trivial by exhaustive scan of all 1 451 520 elements of the sealed
  enumeration (exactly one commutes with both generators), so
  Z(H) = ⟨−1⟩ EXACTLY (V5a). The two centres in play coincide:
  ⟨z_H⟩ = ⟨−1_{E₈}⟩ = Z(W(E₈)).
- −1 is a member of K, of [K,K] = K, and of K₂, and central in each
  (V5b).
- Per-witness lines (V5c, one line each in the log): all ten Schur-side
  witnesses sit over ⟨−1⟩ — witness ∩ ⟨±1⟩ = ⟨−1⟩, and each quotient
  re-verified as the fingerprinted spine-level copy by set equality of
  the pair-action image (2·W(E₆) via the sealed chains). The spine
  witnesses meet ⟨−1⟩ trivially (C misses −1, V1d). The hinge structure
  survives into the roof unchanged.

### VB4 — the roof theorem: **PASS**

**Theorem (minimal-found roof).** Inside W(E₈) (order 696 729 600), the
rotation subgroup **R = W⁺(E₈) = ker(det), of order 348 364 800 and
index 2**, contains both towers and is the smallest overgroup found to
do so: R = ⟨C, H⟩ exactly, with the spine PSL(2,7) ⊃ C₆×ℤ₂ ⊃ A₅ ⊃ S₄ ⊃
A₄ ⊃ ℤ₂ witnessed inside the vector-type complement C ≅ Sp₆(2) (V2c–V2h)
and the Schur tower SL(2,7), 2I, GL(2,3), 2O, 2T (with C₃×D₄, 2·W(E₆),
2×PGL(2,7), Ih, Th) witnessed inside the spin preimage H ≅ 2·Sp₆(2)
(V3a–V3j). R's hinge structure: the one central ℤ₂ of the roof is
⟨−1_{E₈}⟩ = Z(W(E₈)) = z_H (the stem centre of H — the two centres
coincide, V5a); every Schur witness sits over it and the spine sits
beside it (V5c); R is perfect ([R,R] = R, V4f); and R/⟨−1⟩ has order
174 182 400 = |O₈⁺(2)| — identification **by order only** [P cited:
ATLAS], not a verified isomorphism (V4j). Open, stated plainly: TRUE
minimality of R over all subgroups of W(E₈) is not proven (no lattice
argument was run); canonicality of the pair (C, H) inside R up to
conjugacy is not proven (W⁺ itself is canonical as ker(det)).
Successor questions, named not computed: (i) does any proper subgroup of
W⁺(E₈) contain full copies of both towers (lattice search below index
2)? (ii) is (C, H) canonical up to W⁺(E₈)-conjugacy (transporter
computation)? (iii) is R/⟨−1⟩ ≅ O₈⁺(2) as a verified isomorphism,
opening the triality reading of the roof?

## Grades

| claim | grade |
|---|---|
| W(E₈), π, ker π = {±1}, C, H = 2·Sp₆(2) (sealed machinery, re-verified by strips + fresh perfectness) | [C] |
| spine witnesses in C (orders, profiles, presentations) | [C] |
| Schur witnesses in H (orders, profiles, unique involutions, quotient set-equalities) | [C] |
| K = W⁺(E₈) = ker(det), order, index, exact dets | [C] |
| [K,K] = K (perfectness route + spot-check) | [C] |
| |K₂| = |W⁺| | [C] |
| z_H = −1, Z(H) = ⟨−1⟩ (exhaustive centre scan) | [C] |
| |O₈⁺(2)| = 174 182 400 (identification of R/⟨−1⟩ by order) | [P cited: ATLAS] |
| Sp₆(2)/W(E₆)/PSL(2,7) abstract identifications behind the sealed fingerprints | [C] + [P cited] (as sealed in SM-023/SM-027) |

## Not-claims

- NOT claimed: that W⁺(E₈) is minimal over ALL subgroups of W(E₈)
  containing both towers — only minimal-found over {K, [K,K], K₂}.
- NOT claimed: R/⟨−1⟩ ≅ O₈⁺(2) as a verified isomorphism — order match
  only.
- NOT claimed: uniqueness/canonicality of the witnesses or of the pair
  (C, H) up to conjugacy.
- NOT claimed: anything about subgroup classes not sampled by the hunts
  (negative statements, where any occur, are scoped to the found
  copies; this run needed no negative embedding claims).
- Not RH/GRH; no physical identification (Rule 3).
