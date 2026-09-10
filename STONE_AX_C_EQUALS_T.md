# STONE AX — C = T: THE REVERSER AS A CONSTRAINT ON THE GRAMMAR

**Stenberg side · with Claude · 2026-09-10. Brief
`BRIEF_STONE_AX_C_EQUALS_T.md` sha-locked 7f68512a… BEFORE code; no
prior exploration; no amendment. Verifier `verify_stone_ax_c_equals_t.py`,
log: 21 PASS + 1 FAIL — AX2b the auditor's own miscount in the brief
(D₈ is not one of the 42 boards), kept as written, corrected by the
labelled post-reveal AX2b-b; the first run (before AX2b-b was added)
kept as `_FIRSTRUN.log`. 98 s. Machines: Stone AQ's class, Stone AT's
enumeration, the AP board block, Stone AS's enumeration of W(E₇) and
Stone AU's w₀(E₆), all verbatim. Declared dependencies (READ-ONLY):
`scar56_data.json` (0a817fc5…), `_stone_ap_cache/witnesses_ap.json`
(the bridge pair of SM-054). Own cache `_stone_ax_cache/witnesses_ax.json`.
Registry row SM-062. Merkabit-side mathematics with one joint bar (AX3).**

## 0. Discipline

Not RH/GRH. Rule 3: "charge conjugation", "time reversal" and "flavour"
name exact objects — the antipode of the weights, the reverser of
rowmotion, the bridge copy of PSL(2,7) in W(E₇) — and every statement
below is about those objects. Nothing is claimed about physical C, T
or leptons. The sentence the stone was built to make precise is in §1.

## 1. One paragraph

On the 56, the operation that conjugates the states and the operation
that reverses the clock are one element, ι = −1, and it is the only
reverser inside W(E₇) (SM-059). This stone asks what that element does
to the grammar. **Across the family** the reversers of rowmotion inside
W are exactly the coset w₀·C_W(R) — on every one of the 41 enumerated
boards their number equals the order of the clock's linear centralizer,
and on the 56 it is 1 — and conjugation by the reverser acts on the
simple reflections as the diagram automorphism: trivially on the seven
boards where −1 ∈ W (the three boards of D₄, the three of D₆, and the
56), and as the flip on all 35 others — on the 27 the automorphism
that carries the representation to its dual. So **on the 56 the
reverser is central: it induces the identity on every subgroup of the
grammar.** On the 56 the sheet reversal w₀(E₆) induces the E₆ flip on
the six E₆ reflections and moves the seventh (guess CONFIRMED). **The
joint bar:** the bridge copy P ≅ PSL(2,7) of SM-013/SM-054 has
normaliser of order 672 in W(E₇) and centraliser ⟨ι⟩ (guess CONFIRMED
exactly), so W(E₇) realises the outer automorphism of PSL(2,7) — the
one that swaps the two classes of order 7 and the representations 3
and 3̄, which is what charge conjugation is on Ilya's flavour group —
by a Weyl element c, an involution with eight fixed points, and by 335
others. That element is not ι, does not commute with the clock and
does not reverse it; inside the 672 the only reverser is ι and the only
element commuting with Ψ is the identity. Hence, exactly: **on the
board the operation that conjugates the states and reverses the clock
is invisible to the flavour group, and the operation that conjugates
the flavour group is a different Weyl element which neither reverses
nor respects the clock.** And the flavour C has no triplet to act on:
the 56 restricted to P is 2(χ₁ + 2χ₆ + χ₇ + χ₈), seen here on the 28
ι-pairs, with no 3 or 3̄ (SM-013's erratum re-seen). Two observations
beyond the brief: on the five self-dual boards where −1 ∉ W (A₃ ω₂,
A₅ ω₃, A₇ ω₄, D₅ ω₁, D₇ ω₁) the antipode reverses the clock but is
not a Weyl element — a non-linear reverser, like Ψ⁹ is a non-linear
half-turn — and there the isometry criterion for W-membership
overcounts by exactly that antipode (no sealed stone used it on those
boards; checked).

## 2. Bars

| bar | content | outcome |
|---|---|---|
| AX0 | brief locked | PASS (7f68512a…) |
| AX1 | reversers of R in W = w₀·C_W(R): counts equal on the 41 enumerated boards; E₇ cited (then re-measured, AX1-E7) | PASS |
| AX1-E7 | on the 56, reversers of Ψ in W(E₇): 1; C_W(Ψ): 1 (SM-059 AU5, SM-054 AP3 re-measured over 2,903,040) | PASS |
| AX2a | w₀ s_i w₀ = s_σ(i) on all 42 boards, σ the diagram automorphism | PASS |
| AX2b | w₀ central exactly on "the 10 boards where −1 ∈ W (D₄, D₆, D₈ ×3, E₇)" | **FAIL** as written: 7 — the brief counted D₈, which is not in the family |
| AX2b-b (post-reveal) | w₀ central exactly on the 7 boards where −1 ∈ W: D₄ ω₁/ω₃/ω₄, D₆ ω₁/ω₅/ω₆, E₇ ω₇ | PASS |
| AX2c | on every self-dual board, w₀ = the antipode exactly when −1 ∈ W | PASS |
| AX2d | on the 56, ι commutes with all seven simple reflections | PASS |
| AX2e | w₀(E₆) s_i w₀(E₆) = s_σ₆(i) on the six E₆ nodes (0↔5, 2↔4) | PASS |
| AX2f (guess) | w₀(E₆) does not commute with the seventh reflection | **CONFIRMED** (the conjugate is a non-simple reflection, trace 5, type 2¹²1³²) |
| AX3a | the cached bridge pair generates order 168, fixed points 56/8/2/0/0 (SM-054) | PASS |
| AX3b | W(E₇) enumerated: 2,903,040 (SM-057) | PASS |
| AX3c (guess) | C_W(P) = ⟨ι⟩, \|N_W(P)\| = 672, N/C ≅ PGL(2,7) | **CONFIRMED** exactly (672 candidates by hashing, 672 exact) |
| AX3d | a chosen c ∉ P·C carries a 7-element to the other 7-class (outer) | PASS (c: involution 2²⁴1⁸) |
| AX3e | the outer coset contains involutions of type 2²⁴1⁸ | PASS (28 of them; and 28 of type 2²⁸) |
| AX4a | ι commutes with every element of P | PASS |
| AX4b | c ≠ ι, c linear, c neither commutes with Ψ nor reverses it | PASS (cΨc⁻¹ agrees with Ψ at 4 states, with Ψ⁻¹ at 2) |
| AX4c | \|⟨P, c⟩\| = 336, \|⟨P, c, ι⟩\| = 672 (= N) | PASS |
| AX4d | inside N: reversers of Ψ = {ι}, centralizer of Ψ = {1} | PASS |
| AX5a | P on the 28 ι-pairs: fixed points 28/4/1/0/0 | PASS |
| AX5b | permutation character on the pairs = χ₁ + 2χ₆ + χ₇ + χ₈, no χ₃/χ̄₃; census 1/21/56/42/48 | PASS |
| AX5c | ι of type 2²⁸; c permutes the pairs | PASS |

## 3. The family table

Reversers of R inside W and the linear centralizer, board by board
(E₇ from AX1-E7 on the 56). "central" = the reverser w₀ is central in
W; "σ" = the automorphism it induces on the simple reflections is the
non-trivial diagram flip.

| board | \|W\| | h | reversers | \|C_W(R)\| | central | σ non-trivial | self-dual | reverser = antipode |
|---|---|---|---|---|---|---|---|---|
| A2 ω1 | 6 | 3 | 3 | 3 | no | yes | no | — |
| A2 ω2 | 6 | 3 | 3 | 3 | no | yes | no | — |
| A3 ω1 | 24 | 4 | 4 | 4 | no | yes | no | — |
| A3 ω2 | 24 | 4 | 2 | 2 | no | yes | yes | no |
| A3 ω3 | 24 | 4 | 4 | 4 | no | yes | no | — |
| A4 ω1 | 120 | 5 | 5 | 5 | no | yes | no | — |
| A4 ω2 | 120 | 5 | 1 | 1 | no | yes | no | — |
| A4 ω3 | 120 | 5 | 1 | 1 | no | yes | no | — |
| A4 ω4 | 120 | 5 | 5 | 5 | no | yes | no | — |
| A5 ω1 | 720 | 6 | 6 | 6 | no | yes | no | — |
| A5 ω2 | 720 | 6 | 1 | 1 | no | yes | no | — |
| A5 ω3 | 720 | 6 | 1 | 1 | no | yes | yes | no |
| A5 ω4 | 720 | 6 | 1 | 1 | no | yes | no | — |
| A5 ω5 | 720 | 6 | 6 | 6 | no | yes | no | — |
| A6 ω1 | 5040 | 7 | 7 | 7 | no | yes | no | — |
| A6 ω2 | 5040 | 7 | 1 | 1 | no | yes | no | — |
| A6 ω3 | 5040 | 7 | 1 | 1 | no | yes | no | — |
| A6 ω4 | 5040 | 7 | 1 | 1 | no | yes | no | — |
| A6 ω5 | 5040 | 7 | 1 | 1 | no | yes | no | — |
| A6 ω6 | 5040 | 7 | 7 | 7 | no | yes | no | — |
| A7 ω1 | 40320 | 8 | 8 | 8 | no | yes | no | — |
| A7 ω2 | 40320 | 8 | 1 | 1 | no | yes | no | — |
| A7 ω3 | 40320 | 8 | 1 | 1 | no | yes | no | — |
| A7 ω4 | 40320 | 8 | 1 | 1 | no | yes | yes | no |
| A7 ω5 | 40320 | 8 | 1 | 1 | no | yes | no | — |
| A7 ω6 | 40320 | 8 | 1 | 1 | no | yes | no | — |
| A7 ω7 | 40320 | 8 | 8 | 8 | no | yes | no | — |
| D4 ω1 | 192 | 6 | 2 | 2 | yes | no | yes | yes |
| D4 ω3 | 192 | 6 | 2 | 2 | yes | no | yes | yes |
| D4 ω4 | 192 | 6 | 2 | 2 | yes | no | yes | yes |
| D5 ω1 | 1920 | 8 | 2 | 2 | no | yes | yes | no |
| D5 ω4 | 1920 | 8 | 1 | 1 | no | yes | no | — |
| D5 ω5 | 1920 | 8 | 1 | 1 | no | yes | no | — |
| D6 ω1 | 23040 | 10 | 2 | 2 | yes | no | yes | yes |
| D6 ω5 | 23040 | 10 | 1 | 1 | yes | no | yes | yes |
| D6 ω6 | 23040 | 10 | 1 | 1 | yes | no | yes | yes |
| D7 ω1 | 322560 | 12 | 2 | 2 | no | yes | yes | no |
| D7 ω6 | 322560 | 12 | 1 | 1 | no | yes | no | — |
| D7 ω7 | 322560 | 12 | 1 | 1 | no | yes | no | — |
| E6 ω1 | 51840 | 12 | 1 | 1 | no | yes | no | — |
| E6 ω6 | 51840 | 12 | 1 | 1 | no | yes | no | — |
| E7 ω7 | 2903040 | 18 | 1 | 1 | yes | no | yes | yes |

The reverser is unique on the 22 enumerated boards with C_W(R) = 1 and
on the 56 — the rich boards of SM-058 — and non-unique exactly where
the clock has linear symmetry: on chains (h reversers) and on the D_n
vector boards (2, the second being w₀ times the half-turn of SM-055).

## 4. What the bars say, in order

**AX1 — the reversers are a coset.** If g and g′ both reverse R then
g⁻¹g′ commutes with R, so the reversers of R inside W are w₀·C_W(R)
[P, one line]. Measured on 41 boards and on the 56: the number of
reversers equals the order of the linear centralizer everywhere. With
SM-054 (C_{W(E₇)}(Ψ) = 1) this is SM-059's uniqueness of ι as a
corollary rather than an enumeration.

**AX2 — what the reverser does to the grammar.** w₀ = −σ, and −1 is
central in the general linear group, so conjugation by w₀ acts on W as
σ does: w₀ s_i w₀ = s_σ(i) on all 42 boards. Where −1 ∈ W — D_even and
E₇, seven boards of the family — σ is trivial, w₀ = −1 is the antipode
of the weights and is central. Everywhere else the reverser is
non-central and acts on the grammar by the diagram flip: on A_n the
flip that exchanges Λ^k with Λ^{n+1−k}, on D_odd the exchange of the
two half-spins, on E₆ the exchange of 27 and 27̄. On the 56 both
readings are present at once: ι fixes all seven simple reflections,
while the sheet reversal w₀(E₆) — which reverses the sheet clock Ψ₆
and not Ψ (SM-059) — flips the six E₆ reflections and conjugates the
seventh to a non-simple reflection (the reflection in w₀(E₆)α₇).

**AX2c and the observation.** On the five self-dual boards with −1 ∉ W
the antipode is still a permutation of the weights and still reverses
the clock (it is an anti-automorphism of the poset), but it is not a
Weyl element. So those boards have a non-linear reverser beside their
linear ones, exactly as E₇ has a non-linear half-turn Ψ⁹ beside its
linear reversal. A consequence for method: on those five boards the
isometry group of the weight configuration is W × ⟨−1⟩, and the
isometry criterion used for the big boards would overcount W by the
antipode. SM-054's equivalence (linearity ⇔ pair types ⇔ W) is a
theorem for E₇ because −1 ∈ W(E₇); Stones AQ, AR, AU use the criterion
on E₇ alone (every other board was enumerated) — checked, nothing
sealed depends on it. Recorded so that no later stone does.

**AX3 — the bridge copy's normaliser (joint bar).** The registered
guess was exact: C_{W(E₇)}(P) = ⟨ι⟩ and N_{W(E₇)}(P) has order 672, so
N/C ≅ PGL(2,7) = Aut(PSL(2,7)), and W(E₇) realises the outer
automorphism of the bridge copy. The reasoning in the brief was the
permutation character: 56/8/2/0/0/0 is PSL(2,7) ⊂ S₈ on the 28 pairs
of the projective line, doubled, where PGL(2,7) normalises it with
trivial centraliser; the computation confirms it in W(E₇) itself
(672 candidates by exact row hashing over 2,903,040 conjugations, all
672 verified element by element). The outer coset holds 56
involutions (28 of type 2²⁴1⁸ with eight fixed points — the guess from
x ↦ 1/x fixing ±1 — and 28 fixed-point-free), 112 elements of order 6
and 168 of order 8.

**AX4 — C ≠ T on the grammar.** The board's reverser ι induces the
identity on P (central). The chosen c inducing the outer automorphism
is a Weyl element, so by SM-054 it does not commute with Ψ and by
SM-059 it does not reverse Ψ — re-measured: cΨc⁻¹ agrees with Ψ at
four states and with Ψ⁻¹ at two. Inside the whole normaliser the only
reverser of Ψ is ι and the only element commuting with Ψ is 1. So the
flavour group's charge conjugation and the board's time reversal are
different elements; the time reversal is invisible to the flavour
group; the flavour conjugation is a symmetry at no later instant
(SM-057, since it is a Weyl element).

**AX5 — what C has to act on.** P acts on the 28 ι-pairs with fixed
points 28/4/1/0/0, whose character is χ₁ + 2χ₆ + χ₇ + χ₈; the ι-even
half of the 56 is this representation and the ι-odd half is isomorphic
to it (SM-013). No 3 or 3̄ occurs, so on the 56 Ilya's C has no
triplet to act on: it acts on the grammar, not on the states. The
board's C = T = ι acts on every state (all 28 pairs swapped) and on no
element of the grammar.

**AX6 [obs] — the class of c.** c has order 2, cycle type 2²⁴1⁸, trace
1 and determinant −1 on the seven (eigenvalues +1⁴ −1³): it lies in
the ι-coset, not in W⁺ = Sp₆(2). ι·c has type 2²⁸, trace −1,
determinant +1: a fixed-point-free involution of Sp₆(2) that induces
the same outer automorphism. So N = ⟨ι⟩ × PGL(2,7) with the PGL(2,7)
complement ⟨P, ιc⟩ lying inside Sp₆(2) — consistent with SM-023's
structure lemma (every subgroup either contains −1 or embeds in
Sp₆(2)).

## 5. What this leaves open

- The 336 outer elements form one coset; which of them is "the"
  charge conjugation is a choice — the board offers no canonical one,
  exactly as it offered no canonical marker pair (SM-054). Whether
  Ilya's model prefers the eight-fixed-point involution (the S₈
  picture, x ↦ 1/x) or the fixed-point-free one in Sp₆(2) is his to
  say.
- The constraint for a board-realised reading of his model, stated
  once and computably: it must contain an operation that is trivial
  on the flavour group and reverses the clock (ι), and its flavour
  conjugation must be a Weyl element that is a symmetry at no later
  instant. His model has the second (as the outer automorphism) and
  nothing to be the first, because it has no clock.
- On E₆ (the 27), where the reverser is non-central and induces the
  27 ↔ 27̄ flip, the same question — what the reverser does to a
  PSL(2,7) or S₄ inside W(E₆) — is not computed here.
