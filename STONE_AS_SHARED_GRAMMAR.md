# STONE AS — THE SHARED GRAMMAR: HOW MUCH SYMMETRY SURVIVES k TICKS

**Stenberg side · with Claude · 2026-09-09. Brief
`BRIEF_STONE_AS_SHARED_GRAMMAR.md` sha-locked ee603df0… BEFORE code; no
amendment. Verifier `verify_stone_as_shared_grammar.py`, log: 14 PASS +
0 FAIL, the registered guess AS4 CONFIRMED exactly; 188 s; no first-run
stop. Board block verbatim from Stone AP (itself from AC/AF);
`scar56_data.json` READ-ONLY; W(E₇) enumerated in full (2,903,040
elements on the 56, 63 layers of breadth-first closure). Disclosure: the
free exploration `_explore_clock_universal_2026-09-09.py` (NOT sealed)
preceded the brief and is cited in it. Own cache
`_stone_as_cache/witnesses_as.json`. Registry row SM-057.**

## 0. Discipline

Not RH/GRH. Rule 3: "grammar", "instant", "survive" are labels for
W = W(E₇) on the 56, its conjugates Ψ^k W Ψ^{−k}, and their
intersections. Membership in W is the pair-type (isometry) criterion of
Stone AP [P], re-confirmed here on all 2,903,040 elements (AS1b).

## 1. One paragraph

The Weyl group W is the board's grammar: every symmetry, every Scar
selection rule, every descent marker, and the mirror up to one bit, lives
in it. The clock does not (SM-044) and commutes with nothing in it
(SM-054). So after k ticks the grammar is the conjugate W_k = Ψ^k W Ψ^{−k},
and the question is how much two instants share. The answer, computed
exactly by conjugating every one of the 2,903,040 elements of W by Ψ^k
and testing linearity: **W ∩ W_k = {1} for k = 1..8 and 10..17, and
W ∩ W₉ = {1, ι}.** Consecutive instants of the machine share no symmetry
at all; the half-turn shares only the antipode, which it must, since Ψ⁹
commutes with ι (SM-044). No reflection of W is a symmetry after any
tick, and none of the 21 descent markers (the involutions of a bridge
PSL(2,7)) is a symmetry at any later instant short of the full cycle.
Beside this, what the two non-linear gates generate with the grammar:
**⟨W, Ψ⟩ = A₅₆** — the clock is a universal gate relative to the
symmetry group, the exact permutation-group form of "Clifford plus one
non-Clifford gate is universal" — while **⟨W, pr⟩ = 2²⁸ ⋊ Sp₆(2)**, the
group of sign-flips on the 28 antipodal pairs extended by the symplectic
group, because pr is a Weyl element composed with a single swap of the
two poles (SM-016's ν(pr) = 2, completed): the mirror is a Pauli flip
times a Clifford element, the clock is the T-gate, and ⟨W, Ψ, pr⟩ = S₅₆.

## 2. Bars

| bar | content | outcome |
|---|---|---|
| AS0 | brief locked | PASS (ee603df0…) |
| AS1a–c | \|W\| = 2,903,040 on the 56; all linear; 63 reflections one class; ι ∈ W; Ψ, pr ∉ W | PASS |
| AS2a | Ψ, ι, reflections even; ⟨W, Ψ⟩ = A₅₆ (order 56!/2) | PASS |
| AS2b | \|⟨W, pr⟩\| = 2²⁸·\|Sp₆(2)\| = 2³⁷·3⁴·5·7 = 389,639,433,093,120 | PASS |
| AS2c | pr odd; ⟨W, Ψ, pr⟩ = S₅₆ | PASS |
| AS3a | pr fixes exactly the two poles, an ι-pair; pr∘(pole swap) ∈ W | PASS |
| AS3b | W transitive on the 28 pairs with image Sp₆(2) (kernel ⟨ι⟩); every single pair-flip ∈ ⟨W, pr⟩ | PASS |
| AS3c | ⟨W, pr⟩ = (2²⁸)·W with 2²⁸ ∩ W = ⟨ι⟩; order 2²⁸·\|W\|/2 | PASS |
| **AS4 (guess)** | **W ∩ Ψ^k W Ψ^{−k} = {1} for k = 1..8; = {1, ι} for k = 9** | **PASS, exactly** (k = 17 checked: 1) |
| AS4b | k and 18−k give equal orders | PASS |
| AS5 | no reflection linear after Ψ^k, k = 1..17 | PASS (0 of 63, every k) |
| AS6 | bridge copy: 168, 21 involutions; none linear after Ψ^k, k = 1..17 | PASS (0 of 21, every k) |
| AS7 [obs] | near-survivors (conjugates still commuting with ι) | 1 for k ≠ 9; all 2,903,040 for k = 9 (forced: ι central, Ψ⁹ commutes with ι) |

## 3. What the numbers say

- **The clock rewrites the grammar completely at every tick.** Not one
  non-trivial symmetry of the board is a symmetry of the board one tick
  later, or two, or eight. The only exception is the antipode at the
  half-turn, and that is forced by SM-044. The eighteen instants of the
  machine are eighteen mutually alien copies of W(E₇) inside S₅₆,
  pairwise meeting in the identity, all with one spectrum.
- **The clock is universal.** With the grammar it generates every even
  permutation of the 56 states. Nothing weaker than a universal gate is
  needed to make an operation that rewrites the whole symmetry group at
  every step, and nothing stronger exists.
- **The mirror is not.** With the grammar it generates the sign-flip
  group 2²⁸ ⋊ Sp₆(2): the mirror is a Weyl element up to one bit flip on
  one antipodal pair, so it lives in the Clifford-type world, one Pauli
  away from linear. This is SM-016's altitude 2 read as a structure
  theorem. The resource theory of the early stones (structure free, time
  expensive; Ψ-depth 2, W-depth 4) is the shadow of this dichotomy.
- **Descent markers cannot be carried by the clock.** SM-054 said no
  marker is fixed; this says no marker is even a symmetry at the next
  instant. A choice made in the grammar at one instant does not exist,
  as a symmetry, at any other.

## 4. Not claimed

Nothing about W ∩ W_k for other minuscule boards (E₆'s sheets, D_n) —
computable by the same method, not done. Nothing about the intersection
of the grammar with the conjugate by pr∘Ψ or other words. The
identification of ⟨W, pr⟩'s structure as a semidirect product is by
order and by the explicit normal subgroup of flips; its isomorphism type
beyond that is not claimed.

## 5. Synthesis line

Eighteen grammars, one spectrum, no shared word: the clock is the one
gate that is universal, and universality here means exactly that
nothing is preserved except the count of what returns.
