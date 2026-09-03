# BRIEF — STONE AC: THE PARITY RULE OF THE CLOCK

**Staged 2026-09-03 on Selina's "let's look for the mechanism" (the AB6
numbers of SM-040: Ψ keeps 65 % of the roof's pair incidence, Ψ³ 51 %).
Locked before code (`BRIEF_STONE_AC_LOCK.sha256`). The exploration that
found the rule was free (house rule: exploration is not gated); this brief
registers what the sealed run must reproduce and what it predicts.
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

Why does the merkabit's clock keep two thirds of the roof's incidence on
the board and its cube half? SM-040 showed the pair type of {u, u′} on the
56 is the sign of the E₇ inner product ⟨w, w′⟩ (P = +½, S = −½, v =
antipode), i.e. Ψ's score is how much of the Gosset graph it preserves,
and that a pair keeps its type iff B(u,δu′) + B(δu,u′) + B(δu,δu′) = 0
with δ(u) = u + Ψu. The mechanism is therefore in δ, and δ is a mod-2 sum
of the simple roots the clock toggles. Stone AC makes that a rule on the
crystal and tests it on the E₇ board and on the E₆ sheets.

## The rule (declared, to be verified exactly)

Let P be the minuscule poset (27 elements) whose order ideals are the 56
states, with colour c(p) ∈ {0..6}; a state u is an ideal I(u). Rowmotion
is R(I) = ↓min(P ∖ I). The toggle multiset T(u) = colours of I Δ R(I).
Then δ(u) = Σ_{c ∈ T(u)} β_c mod 2, and for u ≠ u′ not antipodal:

```text
type flips under Ψ  ⟺  t₁ + t₂ + t₃ ≡ 1 (mod 2), where
  t₁ = #{c ∈ T(u)  : u′ has a colour-c edge}       (|label_c(u′)| = 1)
  t₂ = #{c ∈ T(u′) : u  has a colour-c edge}
  t₃ = #{(c, c′) ∈ T(u) × T(u′) : c — c′ in the Dynkin diagram}
```

(B(β_c, w′) = ⟨α_c, w′⟩ mod 2 = |label_c(w′)| for minuscule labels in
{−1, 0, 1}; B(β_c, β_c′) = the Cartan entry mod 2 = Dynkin adjacency.)

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AC1 (the convention pinned):** the join-irreducibles of the sealed
  crystal lattice form a 27-element poset; its 56 ideals are the 56
  states; the sealed PSI equals rowmotion R(I) = ↓min(P ∖ I) EXACTLY
  (not its inverse, not an ι-conjugate).
- **AC2 (δ):** δ(u) = XOR of the toggled simple-root masks for all 56
  states; toggle-multiset sizes tabulated. REGISTERED: the 8 antipodal
  steps (Ψu = ιu, SM-016's axis) are exactly the 8 states whose toggle
  set is a single element.
- **AC3 (THE PARITY RULE — registered expectation):** on all non-antipodal
  pairs, kept ⟺ t₁ + t₂ + t₃ even, with ZERO exceptions; the eight parity
  cells tabulated with their counts; the 65.06 % recovered as the count.
- **AC4 (the profile):** for Ψ^k the same rule with T_k(u) = the toggle
  multiset of the k-fold iterate (δ_k = XOR of k successive δ's) is exact
  for k = 1..17 and reproduces the sealed profile (65.1, 54.7, 51.3, …,
  61.6 at k = 9, …).
- **AC5 (THE E₆ CONTROL — registered expectations):** deleting colour 6
  splits the 56 into 27 ⊕ 27̄ ⊕ 1 ⊕ 1 (SM-005); each 27-sheet is J(P₆) for
  the 16-element E₆ minuscule poset; its rowmotion Ψ₆ has order 12 and
  orbits [12, 12, 3] (the sealed MC values); the pair type restricted to a
  sheet is the Schläfli adjacency (P ↔ ⟨w̄,w̄′⟩ = ⅓, S ↔ −⅔); the same
  parity rule with the E₆ Dynkin diagram is EXACT for Ψ₆ on each sheet.
  REGISTERED GUESS (resolvable INVERTED): the E₆ clock keeps a HIGHER
  fraction of its sheet's incidence than the E₇ clock keeps of the
  board's (≥ 65 %) — smaller toggle sets, fewer flips.
- **AC6 (what the cells say — [obs] only):** which parity cell dominates
  among the kept pairs, and the marginal frequencies of t₁ and t₃;
  recorded, not explained further.

## Machinery

`scar56_data.json` (SM-005: verts, EDGES, PSI, IOTA, COMP) read-only; the
E₈-root replay and the label matching of SM-040 (verbatim). Pure
combinatorics, no group caches. Own cache `_stone_ac_cache/`. Outputs:
`verify_stone_ac_parity_rule.py`, `.log`, `STONE_AC_PARITY_RULE.md`.
Runtime: seconds.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "clock", "incidence", "flip" are labels;
the theorem is a parity identity on a minuscule poset.
