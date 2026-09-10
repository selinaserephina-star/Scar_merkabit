# BRIEF — STONE AX: C = T — THE REVERSER AS A CONSTRAINT ON THE GRAMMAR

**Staged 2026-09-10 on Selina's "do it" (after the time-and-physics
reflection). Locked before code (`BRIEF_STONE_AX_LOCK.sha256`). No
prior exploration: every numerical statement below that is not cited
from a sealed unit is a guess, resolvable INVERTED at equal prominence.
Merkabit-side mathematics with one joint bar (AX3, the bridge copy).
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

SM-059 proved that on every minuscule board the longest element w₀
reverses the clock, w₀ R w₀ = R⁻¹, and that on the 56 the reverser
inside W(E₇) is unique and equals the antipode ι = −1 — the map that
carries every weight to its negative, which in representation theory is
what charge conjugation does to the weights of a self-conjugate
representation. So on the 56, the board's own C and its own T are one
element. This stone asks what that element does to the *grammar* — the
symmetry group W and the subgroups inside it that the Scar side reads
as flavour — and whether the same holds across the family.

Three exact questions:

1. How many reversers does W hold on each board, and is the reverser
   the antipode?
2. What automorphism of W does conjugation by the reverser induce?
   When is it trivial (the reverser central)?
3. On the 56: the bridge copy P ≅ PSL(2,7) of SM-013/SM-054 is the
   group in which Ilya's flavour grammar lives. His charge conjugation
   is the *outer* automorphism of PSL(2,7) (the one that swaps the two
   classes of order 7, and the representations 3 and 3̄). Does W(E₇)
   realise it — is there a Weyl element normalising P and inducing the
   outer automorphism — and how does that element stand to the clock?

## Cited [P] and sealed inputs

- SM-059 (Stone AU): w₀ = −σ reverses R on all 42 boards; on the 56
  exactly one element of W(E₇) reverses Ψ (ι) and exactly one of
  W(E₆) reverses Ψ₆ (w₀(E₆)); pr = ι ∘ w₀(E₆) ∘ t.
- SM-054 (Stone AP): C_{W(E₇)}(Ψ) = 1; the bridge copy P in our
  coordinates (generators cached, `_stone_ap_cache/witnesses_ap.json`,
  READ-ONLY): order 168, orbits [28, 28], fixed points 56/8/2/0/0/0.
- SM-013 (Stone F(b)): ι = −1 is central in W(E₇); ℂ⁵⁶|P =
  2(χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈), the ι-odd half ≅ the ι-even half; χ₃, χ̄₃
  do not occur in the Weyl action at all.
- SM-057 (Stone AS): W(E₇) enumerated on the 56 (2,903,040).
- SM-058 (Stone AT): the centralizer table C_W(R^k) on all 42 boards.
- Standard [P]: (i) if g and g′ both reverse R then g⁻¹g′ centralises
  R, so the reversers in W form the coset w₀·C_W(R); (ii) −1 ∈ W
  exactly for D_n with n even and E₇ among the minuscule types, and
  then w₀ = −1 is central; otherwise w₀ = −σ with σ the non-trivial
  diagram automorphism, and conjugation by w₀ acts on W as σ does
  (because −1 is central in GL); (iii) Aut(PSL(2,7)) = PGL(2,7) of
  order 336, the outer automorphism swapping the two classes 7A, 7B;
  (iv) PSL(2,7) ⊂ S₈ on the projective line over F₇ is 2-transitive,
  its point-stabiliser 7:3 is self-normalising, so its centraliser in
  S₈ is trivial, and PGL(2,7) ⊂ S₈ realises the outer automorphism.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AX0:** the brief is sha-locked.
- **AX1 (reversers = w₀·C_W(R); [P] (i), [C] on the family):** on every
  board with |W| ≤ 400,000 (38 of the 42) the number of g ∈ W with
  g R g⁻¹ = R⁻¹ equals |C_W(R)| as measured; on the four large boards
  (D₈ ω₁, ω₇, ω₈; E₇) the coset statement is cited from SM-058/SM-059
  (E₇: exactly one reverser, ι). Consequence recorded: the reverser is
  unique on precisely the boards where C_W(R) = 1.
- **AX2 (the induced automorphism; [P] (ii), [C] on all 42):** on every
  board, w₀ s_i w₀ = s_{σ(i)} for every simple reflection, σ the
  diagram automorphism of the type (identity for D_even and E₇; the
  flip for A_n, D_odd, E₆). Table: the reverser is central in W, and
  equals the antipode of the weights, exactly on the D_even boards and
  E₇ (the 10 boards where −1 ∈ W: D₄, D₆, D₈ three boards each, and the 56); on every other board it is
  non-central and induces σ — on the 27 the automorphism that carries
  the representation to its dual. On the 56: ι s_i ι = s_i for all
  seven; w₀(E₆) (Stone AU's definition) satisfies w₀(E₆) s_i w₀(E₆) =
  s_{σ₆(i)} for the six E₆ nodes with σ₆: 0↔5, 2↔4, and fixes s_6 …
  **registered guess:** w₀(E₆) does NOT commute with the seventh
  reflection s_6 (the node-7 reflection moves the poles).
- **AX3 (REGISTERED GUESS, resolvable INVERTED — the bridge copy's
  normaliser):** with P the cached bridge copy, |C_{W(E₇)}(P)| = 2
  (= ⟨ι⟩) and |N_{W(E₇)}(P)| = 672, so N/C ≅ PGL(2,7): W(E₇) realises
  Ilya's charge conjugation on the bridge copy by a Weyl element c
  inducing the outer automorphism (c a c⁻¹ not P-conjugate to a for a
  of order 7). Reasoning for the guess: the permutation character
  56/8/2/0/0/0 of SM-054 is exactly that of PSL(2,7) ⊂ S₈ = W(A₇) on
  the 28 pairs of points doubled (Λ²8 ⊕ Λ²8*: fixed pairs 28, 4, 1, 0,
  0, 0), where PGL(2,7) normalises it with trivial centraliser; the
  ⟨ι⟩ is forced. If |C| > 2 or the image is only PSL(2,7), the guess is
  INVERTED and the true normaliser is reported.
- **AX4 (C ≠ T on the grammar; [C], forced by SM-054/SM-059 once AX3
  gives c):** the board's reverser ι induces the identity automorphism
  on P (central); the element c that induces Ilya's C is not ι, does
  not commute with Ψ and does not reverse Ψ — so on the board the
  flavour charge conjugation and the time reversal are different
  elements, and the time reversal is invisible to the flavour group.
  [obs] recorded: the order and cycle type of a chosen c (the guess: an
  involution of type 2²⁴1⁸ with 8 fixed points, from x ↦ 1/x on the
  projective line fixing ±1); the numbers #{x : cΨc⁻¹x = Ψx} and
  #{x : cΨc⁻¹x = Ψ⁻¹x} (a distance to the clock and to its reverse,
  as in SM-041's kept counts); |⟨P, c⟩| = 336, |⟨P, c, ι⟩| = 672.
- **AX5 (what C has to act on; [C] with SM-013 cited):** the
  permutation character of P on the 28 ι-pairs is 28/4/1/0/0/0 =
  χ₁ + 2χ₆ + χ₇ + χ₈, so the ι-even half of the 56 is this
  representation and the ι-odd half is isomorphic to it (SM-013 seen
  on the pairs); no 3 or 3̄ anywhere. Hence on the 56 Ilya's C has no
  triplet to act on — it acts on the grammar (the group P), not on the
  states — while the board's C = T = ι acts on the states (every pair
  swapped) and trivially on the grammar.
- **AX6 [obs]:** the class of c in W(E₇) as far as the cycle type on
  the 56 and the trace on the seven determine it; whether c lies in W⁺
  (the Sp₆(2) half of SM-023) or in the ι-coset.

## Machinery

Stone AQ's `Minuscule` class VERBATIM (42 boards; enumeration by the
numpy BFS of Stone AT, VERBATIM) for AX1/AX2; the AP board block
VERBATIM and `scar56_data.json` READ-ONLY, Stone AS's enumeration of
W(E₇) VERBATIM (rebuilt, ~2 min), Stone AU's w₀(E₆) VERBATIM for
AX2/AX3/AX4; the bridge generators from `_stone_ap_cache/
witnesses_ap.json` (READ-ONLY; dependency declared). Normaliser and
centraliser by vectorised conjugation over all 2,903,040 elements with
exact row hashing, then verified element by element. Own cache
`_stone_ax_cache/witnesses_ax.json`. Outputs: `verify_stone_ax_c_equals_t.py`,
`.log`, `STONE_AX_C_EQUALS_T.md`. Runtime: under five minutes.

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact arithmetic (integer permutations); no registry/git
writes by the executor. Not RH/GRH. **Rule 3:** "charge conjugation",
"time reversal", "flavour" are names for exact objects — the antipode
of the weights, the reverser of rowmotion, the bridge copy of PSL(2,7)
— and every statement here is about those objects; nothing is claimed
about physical C, T, or leptons. The one sentence this stone is built
to make precise: *on the 56 the operation that conjugates the states
and the operation that reverses the clock coincide, and that operation
acts trivially on the flavour group; the operation that conjugates the
flavour group is a different Weyl element which neither reverses nor
respects the clock.*
