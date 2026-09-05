# BRIEF — STONE AK: THE TWO TWENTY-FOURS

**Staged 2026-09-06 on Selina's "continue" (the two opens named at the end
of SM-048: the order-24 classes, cap-free; which order-8 class of the
still point gives which type). Locked before code
(`BRIEF_STONE_AK_LOCK.sha256`). Deviations = dated AMENDMENT; post-reveal
changes are findings.**

## Question

SM-039 sampled the twisted coset Ω·Φ and found the maximal order 24 in
two cycle types, each about one eighth of the coset; SM-048 found all
3,024 order-24 elements Φ·g₈ at the still point, split 1,512 / 1,512
between the types. SM-047's fibre method needed a power whose Ω-class fits
the cap; for order 24 the cube's class does not, but the TWELFTH power is
an involution, whose class is small. So: the centralizers, the class
sizes, and whether each type is one class — exactly.

If each type is one class of density 1/8, then |C_Ω(e)| = 8, i.e.
C_Ω(e) = ⟨e³⟩ exactly, and each class has 174,182,400 / 8 = 21,772,800
elements.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AK0a (replay):** Stone AA stages 0–2 VERBATIM; G₂(2) on 360 by closure
  (12,096); Φ equals the sealed cache.
- **AK1 (the still point's eights — registered guess):** the 3,024
  elements of order 8 of G₂(2) form exactly two G₂(2)-conjugacy classes of
  1,512, and each class turns into ONE order-24 type: the type map
  class → cycle type of Φ·g₈ is constant on each class and different
  between the two.
- **AK2 (the centralizers — registered):** for a representative e_A, e_B
  = Φ·g₈ of each type: the Ω-class of the involution e¹² enumerated with a
  transversal (size and centralizer order recorded); C_Ω(e¹²) by Schreier
  closure; C_Ω(e) = {h ∈ C_Ω(e¹²) : h e h⁻¹ = e} has order EXACTLY 8 and
  equals ⟨e³⟩, for both types; hence each type's class (the ⟨Ω,Φ⟩-class
  of a twisted element is its Ω-class, SM-047) has 21,772,800 elements,
  one eighth of the coset, the two together one quarter (SM-039 sampled
  25.0 %, SM-045 25.2 %).
- **AK3 (one class per type — registered, exact per element):** 100
  sampled order-24 twisted elements of each type: e′¹² transported into
  the fibre over e¹² by the transversal, then conjugated by C_Ω(e¹²): every
  one is conjugate to the representative of its type. Any failure settles
  more than two classes.
- **AK4 ([obs] only):** the involution classes of e_A¹² and e_B¹² against
  the class of (Φ·c̄)⁹ (1,575 elements, SM-046): same class or not; the
  three fixed-point counts per block.
- **AK5 ([obs] only, no bar):** the twisted-coset densities now exact for
  18 (1/6) and 24 (1/8 + 1/8): 5/12 = 41.7 % against the sampled 41.4 %
  (SM-039); the order-21 density 14.27 % sampled against 1/7 = 14.29 %
  predicted if C_Ω(Φ·g₇) = ⟨g₇⟩ — recorded as a prediction for a later
  stone, not tested here (no involution to use as fibre).

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM; SM-045/047 helpers
verbatim; G₂(2) on 360 as SM-048. Sealed caches READ-ONLY. Own cache
`_stone_ak_cache/`. Outputs: `verify_stone_ak_two_twentyfours.py`,
`.log`, `STONE_AK_TWO_TWENTYFOURS.md`. Runtime: a few minutes (two
involution-class enumerations and their centralizer closures).

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3.
