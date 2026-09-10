# BRIEF — STONE AW: HOMOMESY ON THE BOARDS — WHAT THE CLOCK CONSERVES ON AVERAGE

**Staged 2026-09-10 on Selina's "Go for it". Locked before code
(`BRIEF_STONE_AW_LOCK.sha256`). Disclosure: a free exploration
(`_explore_homomesy_2026-09-10.py`, NOT sealed) on six boards saw
AW1–AW4 as registered below; the family-wide statements and AW5 are the
guesses. Merkabit-side mathematics. Deviations = dated AMENDMENT;
post-reveal changes are findings.**

## Question

A statistic f on the states of a board is *homomesic* under the clock R
if its average over every R-orbit is the same number (Propp–Roby 2015).
It is the dynamical-algebraic-combinatorics notion of "conserved on
average". Which natural statistics of the board are homomesic under
rowmotion, across the whole minuscule family — and in particular the
three ternary label counts: the number of nodes at which a state's
Dynkin label is +1, −1, or 0?

## Known results, cited [P]

- Rush–Wang (arXiv:1509.08047, 2015): on any minuscule poset, the order
  ideal cardinality |I| and the antichain cardinality |max(I)| are
  homomesic under rowmotion; the refined (per-colour) ideal cardinalities
  are homomesic ("file homomesy").
- Defant–Hopkins (arXiv:2108.13227, 2021): for every finite poset the
  toggleability statistics T⁺_p − T⁻_p are 0-mesic under rowmotion.
- Dictionary on the weights (SM-041): label_i(w) = +1 iff w − α_i is a
  weight iff the ideal I(w) has a maximal element of colour i; label_i =
  −1 iff w + α_i is a weight iff P ∖ I(w) has a minimal element of
  colour i; label_i = 0 otherwise. Hence #(+1 labels) = |max(I)| (the
  antichain cardinality), #(−1 labels) = |min(P ∖ I)| = |max(R(I))|
  (the antichain cardinality of the next state), and #(0 labels) = r −
  #(+1) − #(−1). The colour counts of I are the coordinates of λ − w in
  the simple roots, so file homomesy is the statement that every
  rowmotion orbit has mean weight zero.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AW0:** the brief is sha-locked.
- **AW1 (Rush–Wang seen on the data):** on all 42 boards of SM-055 the
  mean weight of every R-orbit is the zero vector (file homomesy); hence
  every linear statistic is homomesic with mean 0.
- **AW2 (the ternary counts — registered, [P] by the dictionary + Rush–
  Wang for #(+1); [C] for the rest):** on all 42 boards #(+1 labels),
  #(−1 labels) and #(0 labels) are homomesic, with orbit means |P|/h,
  |P|/h and r − 2|P|/h respectively (E₇: 3/2, 3/2, 4; E₆: 4/3, 4/3, 10/3;
  D₅ spin: 5/4, 5/4, 5/2). In particular the means of #(+1) and #(−1)
  are equal on every orbit (Defant–Hopkins' 0-mesy of T⁺ − T⁻, seen).
- **AW3 (REGISTERED GUESS, resolvable INVERTED):** the toggle size
  |I Δ R(I)| — the number of elements of P that change between a state
  and the next, equivalently Σ|c_j| for R(w) − w = Σ c_j α_j — is
  homomesic on all 42 boards with mean 2|P|/h. (May follow from known
  toggleability results; flagged, not claimed as new.)
- **AW4 (registered negatives):** on all 42 non-chain boards the
  following are NOT homomesic: the number of distinct colours toggled;
  the per-state kept count #{u : ⟨Rw, Ru⟩ = ⟨w, u⟩}; and the number of
  lattice elements below w (recorded so that nobody confuses it with the
  rank |I|, which is homomesic by Rush–Wang).
- **AW5 (REGISTERED GUESS, resolvable INVERTED):** on the E₇ board the
  ternary counts are also homomesic under the sheet clock Ψ₆ (with the
  E₆ labels, per sheet) and under the mirror pr (orbits of size ≤ 2), but
  the kept count is homomesic under neither; and under the product
  pr∘Ψ (order 1170 on the board, SM-053) the ternary counts are NOT
  homomesic.
- **AW6 [obs]:** the orbit-average table for every statistic and board,
  and the family formula check |P|/h = (number of join-irreducibles)/
  (Coxeter number) against the classical antichain-mean.

## Machinery

`Minuscule` class of Stone AQ VERBATIM (42 boards); the AP board block
VERBATIM and `scar56_data.json` READ-ONLY for AW5 (Ψ, pr; Ψ₆ rebuilt
from the E₆ covers as in Stone AU, verbatim). Exact rationals. Own cache
`_stone_aw_cache/table_aw.json`. Outputs: `verify_stone_aw_homomesy.py`,
`.log`, `STONE_AW_HOMOMESY.md`. Runtime: under two minutes.

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact arithmetic; no registry/git writes by the executor.
Not RH/GRH. Rule 3: "conserved", "present", "future", "past" are labels;
the theorems are about orbit averages of label counts. The reading of
+1/−1/0 as future/past/present is Selina's and is recorded as [I].
