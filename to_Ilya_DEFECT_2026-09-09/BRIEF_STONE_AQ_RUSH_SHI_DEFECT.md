# BRIEF — STONE AQ: THE RUSH–SHI DEFECT ACROSS THE MINUSCULE FAMILY

**Staged 2026-09-09 on Selina's "do it" (after "what is the next
interesting work"). Locked before code (`BRIEF_STONE_AQ_LOCK.sha256`).
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

Rush–Shi (2013) prove that rowmotion R on the ideals of a minuscule poset
P_λ is conjugate, under the natural bijection J(P_λ) ≅ Wλ, to a Coxeter
element c acting on the weights. A Coxeter element is an isometry: it
keeps every pairwise inner product. Rowmotion, transported to the weights
by that bijection, is not: on E₇ it keeps 1002 of 1540 pair types
(SM-041), agrees pointwise with its nearest Coxeter element on 14 of 56
points (SM-044), and commutes with no Weyl element (SM-054). Those three
numbers measure how far the Rush–Shi bijection is from linear. Compute
them for the whole minuscule family — A_n (ω_k, all k; n ≤ 7), D_n (ω₁;
the two half-spins; n = 4..7), E₆ (ω₁; ω₆ is dual), E₇ (ω₇) — from the
Cartan matrix alone, in one machine, and look for a law.

## Definitions (fixed here)

- Weights in Dynkin-label coordinates; s_i(w) = w − ⟨w, α_i^∨⟩ α_i with
  α_i = row i of the Cartan matrix C; the orbit Wλ generated from the
  dominant λ; inner product ⟨w, w′⟩ = wᵀ C⁻¹ w′ (exact rationals).
- The lattice L on Wλ: Hasse edge w → w − α_i whenever label_i(w) = 1;
  order = its transitive closure; P = join-irreducibles of L (elements
  with exactly one lower cover); I(x) = {p ∈ P : p ≤ x}; **rowmotion
  R(x) = the join in L of the minimal elements of {p ∈ P : p ≰ x}**
  (R(top) = bottom) — the convention SM-041 pinned on the sealed Ψ.
- Pair type of {w, w′} = the value ⟨w, w′⟩. **Kept fraction κ(R)** = the
  fraction of unordered pairs whose type is unchanged by R. **Random
  baseline** κ₀ = Σ_t p_t² over the ordered-pair type distribution.
- **Coxeter agreement** a(R) = max over all Coxeter elements c (all
  orderings of the simple reflections, distinct products) of
  #{w : R(w) = c(w)}. **Altitude** ν(R) = min over w ∈ W of the Hamming
  distance between R and w on Wλ (computed where |W| is enumerable as
  permutations of Wλ, i.e. |W| ≤ 400,000; for E₇ cited from SM-016, 38).
- **Linear centralizer** C_W(R) = {w ∈ W : wR = Rw}: for enumerable W by
  direct test; for E₇ by SM-054's method (the centralizer of R in Sym(Wλ)
  from its cycle type, filtered by "preserves every pair type", which is
  W(E₇)-membership since Aut of the E₇ weight configuration is W(E₇) [P]).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AQ0:** the brief is sha-locked.
- **AQ1 (the anchor — SM-041/044/054 re-seen from the Cartan matrix
  alone):** for E₇ ω₇ the machine gives 56 weights, |P| = 27, R of cycle
  type [18,18,18,2], κ(R) = 1002/1540, κ₀ = 0.4823, a(R) = 14, and
  C_W(R) = {1}; for E₆ ω₁: 27 weights, |P| = 16, R of type [12,12,3],
  κ(R) = 63.53 % (AC5c's sheet value) — without using `scar56_data.json`.
- **AQ2 (Rush–Shi, [P], seen on the data):** in every case R has order h
  and the cycle type of a Coxeter element (computed from an actual c).
- **AQ3 (REGISTERED GUESS, resolvable INVERTED):** R ∈ W exactly when P is
  a chain (A_n with k = 1 or k = n); in every other case R ∉ W.
- **AQ4 (REGISTERED GUESS, resolvable INVERTED):** C_W(R) is trivial in
  every non-chain case, and equals ⟨c⟩ (order h) in the chain cases.
- **AQ5 (REGISTERED GUESS, resolvable INVERTED):** κ(R) > κ₀ in every
  non-chain case, and within each one-parameter family (A_n ω₂ for
  n = 3..7; D_n half-spin for n = 4..7; D_n ω₁ for n = 4..7) κ(R)
  increases with n.
- **AQ6 [obs]:** the full table — type, λ, |Wλ|, |P|, h, cycle type, κ(R),
  κ₀, a(R), ν(R) (where enumerated), |C_W(R)|, R ∈ W — recorded, with any
  visible law stated as [obs] and tested as a registered guess in a later
  stone, not here.
- **AQ7 [P, checked on the data]:** for the simply-laced cases the parity
  mechanism of SM-041 is the identity B(Rw, Rw′) − B(w, w′) = B(δw, w′) +
  B(w, δw′) + B(δw, δw′) with δw = Rw − w a sum of simple roots — holds
  for every pair in every case as an exact rational identity (bilinearity;
  a tautology once R is a map on weights, stated so the reader sees where
  the content is: in δ).

## Machinery

Own, from scratch (no sealed cache needed): Cartan matrices of A_n, D_n,
E₆, E₇; exact rationals (`fractions`); permutation closure for W where
enumerated; Coxeter elements by all orderings. Cross-check of the E₇
numbers against the sealed SM-041 values is by number, not by data. Own
cache `_stone_aq_cache/table_aq.json`. Outputs:
`verify_stone_aq_rush_shi_defect.py`, `.log`, `STONE_AQ_RUSH_SHI_DEFECT.md`.
Runtime: minutes (the D₇ Weyl group, 322,560 elements on 64 points, is
the largest enumeration; a cap of 400,000 is fixed here).

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact arithmetic; no registry/git writes by the executor. Not
RH/GRH. Rule 3: "clock" and "defect" are labels; the mathematics is
rowmotion on minuscule posets against the Weyl group. Rush–Shi is cited
at first use; nothing about the order or orbit structure of R is claimed
as ours.
