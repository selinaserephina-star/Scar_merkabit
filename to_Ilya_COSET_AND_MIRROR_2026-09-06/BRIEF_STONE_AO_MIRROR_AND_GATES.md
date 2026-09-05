# BRIEF — STONE AO: THE MIRROR AND THE GATES

**Staged 2026-09-06 on Selina's "do return to merkabit first". Locked
before code (`BRIEF_STONE_AO_LOCK.sha256`). A free exploration preceded
this brief (house rule: exploration is not gated); the brief registers
what the sealed run must reproduce and what it predicts. Deviations =
dated AMENDMENT; post-reveal changes are findings.**

## Question

SM-041 made the clock Ψ exact: rowmotion on the E₇ minuscule poset P
(27 elements, 56 ideals = the 56 states), order 18, orbits [18, 18, 18,
2]. SM-040 made the chirality ι exact: the transvection in v, the
antipode. The third gate of the machine, the mirror pr (SM-005's "sheet
mirror", 93 % incidence memory in SM-040), has no exact description yet.
This stone measures pr against everything now exact on the board — the
sheets, the poset order, the toggles, ι, the E₆ mirror σ = −w₀(E₆), the
clock and its powers — and asks what the three gates generate.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AO0a:** the AC machinery replayed: P from the crystal, PSI = rowmotion
  exactly, the pair type = the sign of the E₇ inner product.
- **AO1 (the sheets — registered):** the pairing of each state with the
  fundamental coweight of node 6 (the deleted colour of SM-005) takes the
  values ±3/2 once each (the two poles: top and bottom of the lattice) and
  ±1/2 twenty-seven times each (the two sheets). pr SWAPS the two sheets
  and FIXES both poles (its only two fixed points); ι swaps the sheets and
  swaps the poles; Ψ's sheet-transition counts recorded [obs].
- **AO2 (pr against the linear involutions — registered):** pr commutes
  with ι; pr is an involution with cycle type 2²⁷1²; pr∘ι has 6 fixed
  points; pr agrees with ι on 6 states, with σ = −w₀(E₆) on 14 and with
  w₀(E₆) on 2 (recorded; the point is that pr is none of them). The
  parity identity of SM-041 §4 holds for EVERY board permutation π (with
  δ_π(u) = u + π(u)): for pr, zero exceptions, and the kept count
  recovers SM-040's 92.99 %; pr's toggle multisets T_pr(u) = colours of
  I(u) Δ I(pr u) and its eight parity cells recorded [obs].
- **AO3 (the gates generate everything — registered):** |⟨Ψ, ι⟩| = 36
  (the dihedral group, ιΨι = Ψ⁻¹, SM-012 re-seen); ⟨pr, ι⟩ ≅ C₂ × C₂;
  **|⟨Ψ, pr⟩| = 56! — the clock and the mirror generate the full
  symmetric group of the board** (Schreier–Sims); hence ⟨Ψ, ι, pr⟩ = S₅₆.
  [P] consequence: the Cayley graph of S₅₆ on the generating set
  {Ψ, Ψ⁻¹, ι, pr} has diameter at least ⌈log₃(56!/2)⌉ = 157 (at most
  2·3^d − 1 elements within distance d, no backtracking); the inherited
  open "exact Cayley diameter (conj. 91–95)" therefore cannot refer to
  this graph — flagged for the crystal lane, whose definition of that
  object is not in this record; not a refutation.
- **AO4 (the relations — measured, registered on the form):** the orders
  m_k of pr·Ψ^k for k = 1..17 tabulated ((pr Ψ^k)^{m_k} = 1 is the
  dihedral-type relation of pr with each power); the shortest freely
  reduced word in {Ψ, Ψ⁻¹, pr} equal to the identity, other than the
  powers Ψ¹⁸ and pr², found by breadth-first search over all reduced
  words up to length 16 — reported, with its length; the inherited
  "shortest pr/Ψ⁴ relation" answered as stated by m₄ and by that word.
- **AO5 (pr on the lattice — registered):** ι reverses EVERY comparable
  pair of ideals (ι is an antiautomorphism of J(P): I ↦ the complement of
  the dual ideal); pr is neither order-preserving nor order-reversing —
  the counts of preserved / reversed / incomparable images over all
  comparable pairs recorded. Which of the seven colour-toggles T_c
  (product of the toggles of colour c, top to bottom) commute with pr —
  recorded [obs].
- **AO6 (pr and the sheet clock — registered guess):** with Ψ₆ the
  rowmotion of each 27-sheet as J(P₆) (SM-041 AC5; the poles fixed), pr
  does NOT normalize ⟨Ψ₆⟩ (pr Ψ₆ pr is no power of Ψ₆); the order of
  pr·Ψ₆ recorded. If pr Ψ₆ pr = Ψ₆⁻¹, INVERTED and recorded: the mirror is
  the sheet clock's reversal.

## Machinery

`scar56_data.json` (SM-005) READ-ONLY; `verify_stone_ac_parity_rule.py`
lines 55–108 and 111–146 VERBATIM (the E₈ replay, the pair type, the
poset, rowmotion, the toggles; its check calls re-issued under AO tags);
sympy's Schreier–Sims for the group orders. Pure combinatorics. Own cache
`_stone_ao_cache/`. Outputs: `verify_stone_ao_mirror_and_gates.py`,
`.log`, `STONE_AO_MIRROR_AND_GATES.md`. Runtime: seconds to a minute.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "mirror", "gate", "clock" are labels; the
mathematics is permutations of 56 ideals, a group order and a parity
identity.
