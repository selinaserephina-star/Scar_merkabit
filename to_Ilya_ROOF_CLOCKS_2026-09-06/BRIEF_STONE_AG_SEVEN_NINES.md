# BRIEF — STONE AG: THE SEVEN NINES

**Staged 2026-09-05 on Selina's "yes, do the next" (the two candidates left
on the table by SM-044: the seven 9-cycles shared by the Coxeter element
from the roof and by Φ·c̄, and the order-24 twisted elements). Locked
before code (`BRIEF_STONE_AG_LOCK.sha256`). Deviations = dated AMENDMENT;
post-reveal changes are findings.**

## Question

SM-044 recorded, and did not pursue, that c̄₇ (the E₇ Coxeter element seen
from the roof, on the 120 vectors) and Φ·c̄ (the roof's eighteen, on the
360 points) both have exactly seven 9-cycles. Is that one object or a
counting rhyme? Where the two eighteens could meet is at their sixth
powers, both elements of order 3 inside Ω: are c̄₇⁶ and (Φ·c̄)⁶ conjugate?
And what are the order-24 twisted elements, orbit by orbit?

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AG0a (replay):** Stone AA's stage 0–2 machinery replayed VERBATIM
  (lines 71–696 of `verify_stone_aa_roofclock.py`, its own checks
  re-logged with the prefix REPLAY-, its `np.save` of the Φ cache removed
  so the sealed cache is read, not written); the recomputed Φ equals the
  sealed `_stone_aa_cache/phi360.npy` byte for byte; Φ·c̄ has order 18
  with cycle type {18: 16, 9: 7, 3: 3} on 360 (SM-039's sealed value,
  recomputed).
- **AG1 (the roof's seven nines, located):** the 63 points in 9-cycles of
  Φ·c̄ are the fixed points of (Φ·c̄)⁹ that (Φ·c̄)³ moves; 21 per block.
  (Φ·c̄)³ ∈ Ω restricted to the vector block has cycle type {6: 16, 3: 7,
  1: 3} and (Φ·c̄)⁶ has {3: 39, 1: 3} on EVERY block (arithmetic of the
  360-type, checked on the data); (Φ·c̄)⁹ is an involution of Ω with 24
  fixed points per block. [obs] the 21 vectors of the vector block: rank
  of their span, number of orthogonal pairs, whether they lie in one
  hyperplane u^⊥ — recorded, no claim.
- **AG2 (the Coxeter element's seven nines are a field — registered):**
  c̄₇⁹ = t_v; c̄₇² has order 9 and acts on v^⊥/v ≅ F₂⁶ (the 63 Paulis)
  with minimal polynomial x⁶ + x³ + 1 = Φ₉(x), irreducible over F₂, so
  F₂[c̄₇²] ≅ F₆₄ and the seven 9-cycles are the seven cosets of μ₉ in
  F₆₄^× [C + P]. The roof's seven nines collapse on each block to seven
  3-cycles of (Φ·c̄)³ (21 = 7 × 3, three blocks), not to an order-9
  action on one block: the "seven" is 63/9 in one case and 3 × 21/3 in
  the other — a counting rhyme, not one object. REGISTERED as the reading
  the numbers must support.
- **AG3 (where the eighteens could meet — registered guess):** x = (Φ·c̄)⁶
  and y = P360(c̄₇⁶) = P360(c̄₇²)³ are both in Ω (membership strip), both
  of order 3, both with {3: 39, 1: 3} on the vector block. Invariants
  compared: the cycle type on each of the three blocks (as an ordered
  triple and as a multiset, since ⟨Ω,Φ⟩ permutes the blocks), the
  dimension of the fixed subspace on V and the restriction of q to it.
  REGISTERED GUESS (resolvable INVERTED): x and y are NOT conjugate in
  ⟨Ω,Φ⟩ — separated by the spinor-block cycle types. If every invariant
  agrees the guess is INVERTED as instrumented and the conjugacy question
  is recorded OPEN (matching invariants do not prove conjugacy).
- **AG4 (the order-24 twisted elements — measurement, registered from
  SM-039's sealed sample):** re-sampling the coset Ω·Φ (fixed seed,
  30,000 draws) reproduces the order set {3, 6, 9, 12, 18, 21, 24} with no
  new order; the order-24 cycle types are {24: 12, 12: 3, 6: 5, 3: 2} and
  {24: 12, 12: 5, 6: 1, 3: 2} (both sealed types re-found, any further
  type recorded); for one element of each type: its cube (order 8, in Ω)
  and its eighth power (order 3, in Ω) restricted to the vector block —
  cycle types recorded; whether the order-3 part is conjugate-by-
  invariants to x or to y — recorded. No rowmotion in hand has order 24
  (E₇: 18; E₆ sheets: 12) and no roof poset is named: IB's "order-24
  element as rowmotion" NOT SUPPORTED as stated (registered, same rule as
  SM-044's AF5b).
- **AG5 ([obs] only):** among the sampled order-18 twisted elements, the
  distinct cycle types on 360 and their frequencies; whether Φ·c̄'s type
  is the common one.

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM (the F₂ / E₈ /
Clifford / spin machinery, P360, Φ, τ″), reading the sealed U/V/X/Z
caches READ-ONLY and `_stone_aa_cache/phi360.npy` for the cross-check;
the E₇ base BETA rebuilt as in SM-040/041; the SM-026 engine is not
needed. Own cache `_stone_ag_cache/`. Outputs: `verify_stone_ag_seven_nines.py`,
`.log`, `STONE_AG_SEVEN_NINES.md`. Runtime: under a minute.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3: "nine", "beat",
"clock" are labels; the mathematics is cycle types, a minimal polynomial
and conjugacy invariants.
