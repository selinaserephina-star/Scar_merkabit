# BRIEF — STONE AT: THE SHARED GRAMMAR ACROSS THE MINUSCULE FAMILY

**Staged 2026-09-09 on Selina's "stage it". Locked before code
(`BRIEF_STONE_AT_LOCK.sha256`). Deviations = dated AMENDMENT; post-reveal
changes are findings. Merkabit-side mathematics (rowmotion against the
Weyl group), recorded in the joint lane because the paper's tier three
cites it.**

## Question

SM-057 computed, on the E₇ board, the symmetry two instants of the clock
share: W ∩ Ψ^k W Ψ^{−k} is trivial for every k except the half-turn,
where it is ⟨ι⟩. Is that an E₇ fact or a law of the family? And is
there a formula? The natural candidate is the centralizer: an element g
of W that commutes with R^k certainly satisfies R^{−k} g R^k = g ∈ W, so
C_W(R^k) ⊆ W ∩ R^k W R^{−k} always [P]. The guess is that this
inclusion is an equality for every minuscule board and every k.

## Definitions

As in SM-055/056: λ simply-laced minuscule, weights Wλ from the Cartan
matrix, rowmotion R on the weights, h the Coxeter number, W enumerated
as permutations of Wλ. For k = 1..h−1: I_k := {g ∈ W : R^{−k} g R^k ∈ W}
(the shared grammar at distance k) and C_k := C_W(R^k) = {g ∈ W : g R^k =
R^k g}. Membership in W is by the enumerated set for every case with
|W| ≤ 400,000 (all cases but E₇) and, for E₇, by the pair-type
(isometry) criterion of Stones AP/AS [P]. Cases: the 42 of SM-055
(A_n all ω_k, n ≤ 7; D_n ω₁ and both half-spins, n = 4..7; E₆ ω₁, ω₆;
E₇ ω₇).

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AT0:** the brief is sha-locked.
- **AT1 [P, checked]:** C_k ⊆ I_k for every case and every k; and at
  k = 1, |C_1| agrees with SM-055's |C_W(R)| (trivial off the chains
  except the D_n vector representations, where it is 2).
- **AT2 (REGISTERED GUESS, the main one, resolvable INVERTED):**
  I_k = C_W(R^k) — as sets — for every one of the 42 cases and every
  k = 1..h−1. For E₇ this is checked for k = 1..17 on the full
  enumeration (SM-057's intersections re-derived on the way).
- **AT3 (REGISTERED GUESS, the predicted table, resolvable INVERTED):**
  the common value |I_k| = |C_k| is:
  (i) chains (A_n ω₁, ω_n): |W| for every k (R ∈ W);
  (ii) D_n ω₁, n = 3..7 (incl. A₃ ω₂; and D₄ ω₃, ω₄): |W| at k = n−1
  and exactly 2 at every other k, the group being ⟨R^{n−1}⟩ (the
  half-turn commutes with every power and is a Weyl element, SM-056);
  (iii) every other case with h even (A_n ω_k, 1<k<n, n odd; D_n
  half-spins; E₆; E₇): 1 for every k ≠ h/2; at k = h/2, **2 when −1 ∈ W
  (D_n half-spins with n even; E₇) with the group ⟨−1⟩, and 1 when
  −1 ∉ W (A_n, D_n half-spins with n odd, E₆)** — the reasoning being
  that the antipode reverses the poset and conjugates R to R^{−1}, so it
  commutes with R^k exactly when R^{2k} = 1;
  (iv) every case with h odd (A_n ω_k, n even, 1<k<n): 1 for every k.
- **AT4 [P, checked]:** on every board with −1 ∈ W, the antipode ι
  satisfies ι R ι = R^{−1} (the antipode is an antiautomorphism of the
  minuscule lattice), so ι ∈ C_W(R^k) iff h | 2k; on boards with
  −1 ∉ W the antipode is not a permutation of Wλ at all (it maps λ to
  the dual orbit) — checked as stated.
- **AT5 [obs]:** wherever |I_k| > 1 and the case is not covered by AT3,
  the elements are named (cycle type, whether a power of R, whether
  central).

## Machinery

The `Minuscule` class of `verify_stone_aq_rush_shi_defect.py` loaded
VERBATIM (as in Stone AR); W enumerated by numpy breadth-first closure
(as in Stone AS) for every case, stored as a (|W| × N) array; the
commuting test and the conjugation vectorized; membership by a set of
row-bytes (|W| ≤ 400,000) or by the isometry mask (E₇). Own cache
`_stone_at_cache/table_at.json`. Outputs:
`verify_stone_at_grammar_family.py`, `.log`, `STONE_AT_GRAMMAR_FAMILY.md`.
Runtime: minutes (E₇: 17 passes over 2.9 M elements; D₇: 11 passes over
322,560).

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact integers; no registry/git writes by the executor. Not
RH/GRH. Rule 3: "grammar", "instant", "share" are labels for W, its
R-conjugates and their intersections.
