# BRIEF — STONE AL: THE SEVEN-BEAT CLOCK'S CLASS, AND THE TURN'S CENTRALIZER

**Staged 2026-09-06 on Selina's "continue" (the order-21 prediction of
SM-049 and the remaining twisted orders). Locked before code
(`BRIEF_STONE_AL_LOCK.sha256`). Deviations = dated AMENDMENT; post-reveal
changes are findings.**

## Question

SM-039's seven-beat clock Φ·g₇ (g₇ of order 7 at the still point) has
order 21 and its sampled density in the twisted coset is 14.27 %, on 1/7.
There is no involution to use as a fibre (21 is odd), but there is a
better lever: (Φ·g₇)⁷ = Φ itself, so any two order-21 twisted elements
whose seventh powers are both Φ are conjugate only by elements of C_Ω(Φ),
and C_Ω(Φ) is the set of elements of Ω fixed by the turn's footprint —
SM-038's G₂(2), proved there "as far as the machine reaches" and here
made exact by a class count. The fibre over Φ is the still point.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AL0a (replay):** Stone AA stages 0–2 VERBATIM; G₂(2) on 360 by
  closure; Φ equals the sealed cache.
- **AL1 (the turn's centralizer is the still point — registered):** the
  Ω-class of Φ under conjugation (a class inside the coset Ω·Φ) has
  EXACTLY 14,400 = 174,182,400 / 12,096 elements, and its Schreier-closed
  centralizer C_Ω(Φ) equals G₂(2) on 360 points as a SET (12,096
  elements). SM-038's Z4 ("Fix(τ″) = G as far as the machine reaches")
  becomes exact: the elements of Ω commuting with the turn are exactly the
  still point.
- **AL2 (the seven-beat clock's centralizer — registered):** C_Ω(Φ·g₇) =
  {h ∈ G₂(2) : h g₇ h⁻¹ = g₇} = ⟨g₇⟩ of order 7 (G₂(2)'s 1,728 elements of
  order 7 form ONE G₂(2)-class, so the centralizer in G₂(2) has order
  12,096 / 1,728 = 7); hence the class of Φ·g₇ (its ⟨Ω,Φ⟩-class is its
  Ω-class) has 174,182,400 / 7 = 24,883,200 elements, exactly one seventh
  of the coset (sampled 14.27 %).
- **AL3 (one class — registered, exact per element):** 300 sampled
  order-21 twisted elements e′: e′⁷ lies in the class of Φ (every one),
  is transported onto Φ by the transversal, and the transported e′ is
  conjugated onto Φ·g₇ by an element of G₂(2): 300/300. The order-21
  twisted elements are one class of density exactly 1/7 (sample-bounded).
- **AL4 (the order-12 twisted elements — measured, registered guesses):**
  200 sampled order-12 twisted elements grouped by cycle type on 360;
  REGISTERED GUESS: the types are exactly those realised from the still
  point by Φ·g₄ (756 elements) and Φ·g₁₂ (3,024 elements). For each type
  a representative e: the class of the involution e⁶ (enumerated with
  transversal if within the cap), C_Ω(e⁶) closed, C_Ω(e) read off —
  order, and the class density; per-element conjugacy of the sampled
  elements of that type onto the representative. REGISTERED GUESS: one
  class per type; the densities sum to the sampled 31.5 % within sampling
  error. Whatever exceeds the cap is said so.
- **AL5 ([obs] only):** the twisted-coset densities now in hand — 18: 1/6,
  24: 1/8 + 1/8, 21: 1/7, 12: as found — and the remainder for orders 9,
  6, 3 against SM-039's sample; the cycle types of sampled twisted
  elements of order 3 against Φ's {3: 120} and the size 14,400 of Φ's
  class (0.008 % of the coset against the sampled 0.47 %: the twisted
  3-elements are mostly NOT turns).

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM; SM-045/047/048
helpers verbatim; G₂(2) on 360 as SM-048. Sealed caches READ-ONLY. Own
cache `_stone_al_cache/`. Outputs: `verify_stone_al_seven_beat_class.py`,
`.log`, `STONE_AL_SEVEN_BEAT_CLASS.md`. Runtime: minutes (AL4's
centralizer closures dominate).

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3.
