# BRIEF — STONE AS: THE SHARED GRAMMAR — HOW MUCH SYMMETRY SURVIVES k TICKS

**Staged 2026-09-09 on Selina's "yes" to "shall I stage it" (open
exploration: what does it all mean). Locked before code
(`BRIEF_STONE_AS_LOCK.sha256`). Disclosure: a free exploration the same
hour (`_explore_clock_universal_2026-09-09.py`, NOT sealed) saw
⟨W, Ψ⟩ = A₅₆, |⟨W, pr⟩| = 2²⁸·|Sp₆(2)|, and no reflection (0 of 63) and no
sampled Weyl element (0 of 3,000) still linear after conjugation by Ψ.
This run re-derives those under registered bars and settles the
intersections exactly. Deviations = dated AMENDMENT; post-reveal changes
are findings.**

## Question

The Weyl group W = W(E₇) acting on the 56 states is the board's grammar:
every symmetry, every Scar selection rule, every descent marker, and the
mirror up to one bit, lives in it. The clock Ψ is rowmotion and is not in
W (SM-044), commutes with nothing in W (SM-054), and is conjugate to a
Coxeter element only through a non-linear bijection (SM-055/056). So
after k ticks the grammar is the conjugate W_k = Ψ^k W Ψ^{−k}. How much
grammar do two instants share: what is W ∩ W_k, exactly, for k = 1..17?
And what do the clock and the mirror each generate together with W?

## Definitions

Board, pair types, W-membership as in Stones AC/AF/AP: a permutation of
the 56 lies in W(E₇) iff it preserves every pair type (Aut of the E₇
weight configuration is W(E₇) [P], so "linear" = "in W"). ι = −1 ∈ W is
central. W is enumerated in full (2,903,040 elements, as in SM-016) by
breadth-first closure from the seven simple reflections.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AS0:** the brief is sha-locked.
- **AS1 (the enumeration):** W has exactly 2,903,040 elements on the 56,
  all linear; the 63 reflections form one W-class; ι ∈ W; Ψ ∉ W, pr ∉ W.
- **AS2 (registered, from the disclosure):** ⟨W, Ψ⟩ = A₅₆ (Ψ, ι and the
  reflections are even permutations; the order is 56!/2); ⟨W, pr⟩ has
  order 2²⁸·|Sp₆(2)| = 2³⁷·3⁴·5·7; ⟨W, Ψ, pr⟩ = S₅₆ (pr is odd).
- **AS3 (registered, SM-016 re-seen and completed):** pr = w·t with t
  the transposition of the two poles (an ι-pair) and w ∈ W; W is
  transitive on the 28 ι-pairs, so the normal closure of t in ⟨W, pr⟩ is
  the full group F ≅ 2²⁸ of pair-flips; F ∩ W = ⟨ι⟩; hence ⟨W, pr⟩ = F·W
  = 2²⁸ ⋊ Sp₆(2), the sign-flip group of the 28 bitangents. Checked:
  w = pr∘t is linear; every single pair-flip lies in ⟨W, pr⟩; the order
  matches.
- **AS4 (REGISTERED GUESS, the main one, resolvable INVERTED):**
  W ∩ Ψ^k W Ψ^{−k} = {1} for every k ∈ {1..17} except k = 9, where it is
  exactly {1, ι} (Ψ⁹ commutes with ι, SM-044, so ι survives the
  half-turn; nothing else does). Computed exactly for k = 1..9 (k and
  18−k give conjugate intersections of equal order — stated and checked
  on k = 1, 17) by conjugating every element of W and testing linearity.
- **AS5 (registered):** no reflection of W survives any tick k = 1..17
  (0 of 63 linear after conjugation by Ψ^k) — the grammar's generators
  are all carried out of the grammar at the first tick.
- **AS6 (descent markers under time; registered):** for the bridge copy
  of SM-054 (its 21 involutions z) and every k = 1..17, Ψ^k z Ψ^{−k} ∉ W:
  a marker made at one instant is not a symmetry at any later instant
  short of the full cycle. Follows from AS4 for k ≠ 9; checked directly
  for all k.
- **AS7 [obs]:** for each k, the number of elements of W whose conjugate
  by Ψ^k passes the cheap necessary test (commuting with ι after
  conjugation) before the full test — recorded as the "near-survivor"
  profile, not claimed.

## Machinery

Board block VERBATIM from `verify_stone_ap_clock_centralizer.py` (itself
verbatim from Stones AC/AF); W enumerated by numpy breadth-first closure
(rows as bytes; batches of compositions); conjugation and the linearity
test vectorized in chunks, the ι-commutation filter first, then the full
1,540-pair test on survivors; sympy Schreier–Sims for the three generated
groups; SM-016's pole pair read from the data (the two fixed points of
pr). Own cache `_stone_as_cache/witnesses_as.json`. Outputs:
`verify_stone_as_shared_grammar.py`, `.log`, `STONE_AS_SHARED_GRAMMAR.md`.
Runtime: minutes (the enumeration and nine conjugation passes over
2.9 M elements).

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact integers; `scar56_data.json` READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3: "grammar",
"instant", "survive" are labels for W, its Ψ-conjugates, and their
intersections.
