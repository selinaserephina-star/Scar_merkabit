# STONE AQ — THE RUSH–SHI DEFECT ACROSS THE MINUSCULE FAMILY

**Stenberg side · with Claude · 2026-09-09. Brief
`BRIEF_STONE_AQ_RUSH_SHI_DEFECT.md` sha-locked 5b389725… BEFORE code; no
amendment. Verifier `verify_stone_aq_rush_shi_defect.py`, log: 8 PASS + 2
FAIL — AQ4 and AQ5b registered guesses INVERTED, both informatively; AQ4b
the labelled post-reveal identification; the first run stopped on an
instrumentation error (the order matrix stored transposed) before any
result, log kept as `verify_stone_aq_rush_shi_defect_FIRSTRUN.log`. 92 s.
No sealed cache used: everything from the Cartan matrices. Own cache
`_stone_aq_cache/table_aq.json`. Registry row SM-055.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "defect", "half-turn" are labels; the
mathematics is rowmotion on minuscule posets against the Weyl group.
Rush–Shi (J. Algebraic Combin. 37 (2013) 545–569) is cited at first use:
rowmotion R on J(P_λ) is conjugate to a Coxeter element c on the weights
Wλ; nothing about the order or the orbit structure of R is claimed here.
What is computed is how far the conjugating bijection is from linear.

## 1. One paragraph

A Coxeter element is an isometry of the weights; rowmotion, transported
to the weights by the natural bijection, is not, and the lane had three
numbers for E₇ saying how much (SM-041: 1002 of 1540 pair types kept;
SM-044: 14 of 56 points agreeing with the nearest Coxeter element; SM-054:
no Weyl element commuting). One machine built from the Cartan matrix
alone — weights in Dynkin labels, the lattice by w → w − α_i at label 1,
its join-irreducibles, rowmotion as the join of the minimal elements of
the complement — reproduces those three numbers for E₇ and SM-041's
63.53 % for E₆ without touching the sealed data, and computes the same
defects for 42 minuscule cases: A_n (all ω_k, n ≤ 7), D_n (ω₁ and both
half-spins, n = 4..7), E₆ (ω₁, ω₆), E₇ (ω₇). Rush–Shi is seen on the
data in all 42 (order h, a Coxeter element's cycle type). **Rowmotion is
itself a Weyl element exactly when the poset is a chain** (A_n, ω₁ and
ω_n: R = c, κ = 1, C_W(R) = ⟨c⟩), and in no other case — registered,
confirmed. **The linear centralizer is trivial in every other case except
the vector representations of D_n** (and A₃ ω₂ = D₃'s vector, D₄ ω₃/ω₄ =
its triality images), where it has order 2; the post-reveal check
identifies the element: **the half-turn R^{h/2} of rowmotion itself**,
which is linear for the vector representations and for nothing else — for
E₇, Ψ⁹ is not (SM-054). The kept fraction exceeds the random baseline in
every non-chain case (registered, confirmed) but does not grow with rank
as guessed: it rises along D_n ω₁ (0.786 → 0.868) and along A_n ω₂ from
n = 4 (0.644 → 0.767), and falls along the half-spins (0.633, 0.637,
0.585); the exceptional cases sit in the same band as the spinors
(E₆ 0.635, E₇ 0.651). Two guesses inverted, both recorded.

## 2. Bars

| bar | registered | outcome |
|---|---|---|
| AQ0 | brief locked | PASS (5b389725…) |
| AQ1a | E₇ ω₇ from the Cartan matrix: 56, \|P\| = 27, [18,18,18,2], κ = 1002/1540, κ₀ = 0.4823, a(R) = 14, C_W(R) = 1, R ∉ W | PASS |
| AQ1b | E₆ ω₁: 27, \|P\| = 16, [12,12,3], κ = 63.53 % | PASS |
| AQ2 | Rush–Shi seen on the data: order h and a Coxeter element's cycle type, all 42 cases | PASS |
| AQ3 (guess) | R ∈ W iff P is a chain | PASS (12 chains in W, 30 non-chains not) |
| AQ4 (guess) | C_W(R) trivial off the chains, ⟨c⟩ of order h on them | **FAIL — INVERTED**: order 2 in A₃ω₂, D₄ω₁/ω₃/ω₄, D₅ω₁, D₆ω₁, D₇ω₁; trivial in the other 23 non-chain cases; ⟨c⟩ on the chains ✓ |
| AQ4b (post-reveal) | the order-2 element is R^{h/2} in every inverted case | PASS (types 2²1², 2⁴, 2⁴1², 2⁶, 2⁶1²; never −1) |
| AQ5a (guess) | κ > κ₀ in every non-chain case | PASS |
| AQ5b (guess) | κ increasing with n in A_n ω₂, D_n half-spin, D_n ω₁ | **FAIL — INVERTED**: D_n ω₁ increasing; A_n ω₂ increasing from n = 4 after the D₃ coincidence at n = 3; half-spins not monotone |
| AQ7 [P] | the bilinear identity for δ = Rw − w on every pair of every case | PASS |

## 3. The table

| case | \|Wλ\| | \|P\| | h | R cycle type | κ(R) | κ₀ | a(R) | ν(R) | \|C_W(R)\| | R ∈ W |
|---|---|---|---|---|---|---|---|---|---|---|
| A_n ω₁, ω_n (n = 2..7) | n+1 | n | n+1 | (n+1)¹ | 1 | 1 | n+1 | 0 | n+1 | yes |
| A₃ ω₂ (= D₃ ω₁) | 6 | 4 | 4 | 4·2 | 11/15 = 0.733 | 0.680 | 3 | 3 | 2 | no |
| A₄ ω₂, ω₃ | 10 | 6 | 5 | 5² | 29/45 = 0.644 | 0.556 | 5 | 5 | 1 | no |
| A₅ ω₂, ω₄ | 15 | 8 | 6 | 6²·3 | 71/105 = 0.676 | 0.510 | 6 | 9 | 1 | no |
| A₅ ω₃ | 20 | 9 | 6 | 6³·2 | 58/95 = 0.611 | 0.452 | 7 | 13 | 1 | no |
| A₆ ω₂, ω₅ | 21 | 10 | 7 | 7³ | 76/105 = 0.724 | 0.500 | 10 | 11 | 1 | no |
| A₆ ω₃, ω₄ | 35 | 12 | 7 | 7⁵ | 339/595 = 0.570 | 0.419 | 10 | 25 | 1 | no |
| A₇ ω₂, ω₆ | 28 | 12 | 8 | 8³·4 | 145/189 = 0.767 | 0.506 | 15 | 13 | 1 | no |
| A₇ ω₃, ω₅ | 56 | 15 | 8 | 8⁷ | 431/770 = 0.560 | 0.405 | 12 | 44 | 1 | no |
| A₇ ω₄ | 70 | 16 | 8 | 8⁸·4·2 | 417/805 = 0.518 | 0.380 | 12 | 56 | 1 | no |
| D₄ ω₁, ω₃, ω₄ | 8 | 6 | 6 | 6·2 | 11/14 = 0.786 | 0.755 | 4 | 3 | 2 | no |
| D₅ ω₁ | 10 | 8 | 8 | 8·2 | 37/45 = 0.822 | 0.802 | 5 | 5 | 2 | no |
| D₅ ω₄, ω₅ | 16 | 10 | 8 | 8² | 19/30 = 0.633 | 0.556 | 5 | 10 | 1 | no |
| D₆ ω₁ | 12 | 10 | 10 | 10·2 | 28/33 = 0.848 | 0.835 | 6 | 5 | 2 | no |
| D₆ ω₅, ω₆ | 32 | 15 | 10 | 10³·2 | 79/124 = 0.637 | 0.469 | 9 | 19 | 1 | no |
| D₇ ω₁ | 14 | 12 | 12 | 12·2 | 79/91 = 0.868 | 0.858 | 7 | 7 | 2 | no |
| D₇ ω₆, ω₇ | 64 | 21 | 12 | 12⁵·4 | 295/504 = 0.585 | 0.432 | 13 | 48 | 1 | no |
| E₆ ω₁, ω₆ | 27 | 16 | 12 | 12²·3 | 223/351 = 0.635 | 0.527 | 9 | 15 | 1 | no |
| E₇ ω₇ | 56 | 27 | 18 | 18³·2 | 501/770 = 0.651 | 0.482 | 14 | 38 (SM-016) | 1 | no |

κ = fraction of unordered pairs whose inner product R keeps; κ₀ = Σ p_t²
over the type distribution (the random baseline); a(R) = best pointwise
agreement with a Coxeter element; ν(R) = Hamming distance to the nearest
Weyl element (W enumerated as permutations of the weights, |W| ≤ 322,560;
E₇ cited); dual representations give equal rows (ω_k ↔ ω_{n+1−k}; the two
half-spins; ω₁ ↔ ω₆ of E₆), as they must.

## 4. What the table says, as observations [obs]

- **The chains are the linear case and the only one.** R = c exactly when
  P_λ is a chain; then all three defects vanish and C_W(R) = ⟨c⟩. This is
  the standard representation of A_n and its dual, and nothing else in
  the family.
- **The half-turn is linear exactly for the vector representations of
  D_n.** There R has cycle type [2n−2, 2] (one long orbit and the
  antipodal pair of the axis), R^{n−1} is a Weyl element of type
  2^{n−1}·1² (n odd) or 2ⁿ (n even), never −1, and C_W(R) = ⟨R^{n−1}⟩.
  Reading it through the E₇ case: there the corresponding power Ψ⁹ is not
  linear (SM-016: ν(Ψ⁹) = 36; SM-054), so the 56-board's clock is further
  from the Weyl group than any vector clock, in this precise sense.
- **a(R) = N/2 exactly along the vector family** (4, 5, 6, 7 of 8, 10,
  12, 14) and ν(R) is tiny there (3, 5, 5, 7); for the spinors and the
  middle ω_k of A_n both defects grow with the size of the orbit (A₇ ω₄:
  a = 12 of 70, ν = 56; D₇ spin: a = 13 of 64, ν = 48; E₇: 14 of 56, 38).
- **κ − κ₀ is largest for A_n ω₂ and the E's** (+0.26 at A₇ ω₂, +0.17 at
  E₇, +0.17 at D₆ spin) and smallest for the vector family, where it
  tends to 0 (+0.031, +0.020, +0.014, +0.010): the vector clocks keep many
  pairs because there are few types to keep.
- **The exceptional cases are ordinary in this table.** E₆ (0.635) and E₇
  (0.651) sit where the spinors of D₅–D₇ sit (0.585–0.637); nothing in κ,
  a or ν marks E₇ out except its size.
- No law in n or h is visible from these 42 numbers that we would
  register; a later stone may register one after more of type A (n = 8, 9
  are cheap) and D₈.

## 5. Corrections to the lane's own reading

None to sealed numbers. The E₇ and E₆ values of SM-041/044/054 are
reproduced from the Cartan matrix, which is an independent second
derivation of the sealed board's Ψ = rowmotion identification: the
generic machine, given only C(E₇) and ω₇, produces a permutation of the
same cycle type with the same kept fraction, the same best Coxeter
agreement and the same trivial linear centralizer as the sealed Ψ.

## 6. Not claimed

Nothing about non-minuscule posets, promotion, or birational rowmotion.
No formula for κ. No statement about D₈ or A₈ and beyond. The bilinear
identity AQ7 is a tautology stated for orientation, not a result. ν(E₇)
is cited (SM-016), not recomputed.

## 7. Synthesis line

The Rush–Shi bijection is linear on the chains, half-linear on the vector
representations — its half-turn is a Weyl element — and nowhere else; the
56-board's clock is as far from linear as a minuscule clock gets, and
the paper's one open rule now has a family of 42 numbers behind it rather
than one.
