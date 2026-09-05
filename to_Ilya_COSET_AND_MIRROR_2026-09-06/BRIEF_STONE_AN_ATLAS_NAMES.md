# BRIEF — STONE AN: THE ATLAS NAMES

**Staged 2026-09-06 on Selina's "lets do this" (the lookup step named at
the end of SM-051), with her approval of the one download it needed.
Locked before code (`BRIEF_STONE_AN_LOCK.sha256`). Deviations = dated
AMENDMENT; post-reveal changes are findings.**

## Question

SM-047..051 computed the fourteen conjugacy classes of the roof's twisted
coset Ω·Φ with their Ω-centralizer orders, and the earlier stones
recorded, for each class, where its powers land (the heart, the two
involution classes, the turn). None of it was named. The published
character table of O₈⁺(2).3 — the GAP Character Table Library, version
1.3.11, file `data/ctoorth2.tbl`, tables "O8+(2)" and "O8+(2).3", origin
"ATLAS of finite groups" — carries the centralizer orders, the power maps
for 2, 3, 5, 7, and the class fusion of O₈⁺(2) into O₈⁺(2).3. The header
blocks of both tables (no character values) are cited verbatim in
`_stone_an_cache/` with source and licence. This stone matches ours to
theirs and lets the names follow.

Conversions: a twisted element e centralizes itself and lies outside Ω,
so its centralizer in O₈⁺(2).3 is 3·|C_Ω(e)|; an inner element g whose
centralizer contains a twisted element has |C_{G.3}(g)| = 3·|C_Ω(g)|,
otherwise |C_Ω(g)|. Element orders are derived from the power maps (the
least product of prime powers taking the class to 1).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AN1 (the count — [P cited]):** O₈⁺(2) has 53 classes and O₈⁺(2).3 has
  55; the fusion map fuses exactly 13 triples and fixes 14 classes; by
  Brauer's permutation lemma each outer coset has 14 classes: 27 inner +
  28 outer = 55. Our census (SM-051) has 14. The 14 triality-fixed
  classes of O₈⁺(2), by the ATLAS letter rule applied in table order, are
  1A, 2A, 2E, 3D, 3E, 4A, 4B, 4F, 6G, 6N, 7A, 8A, 8B, 12D (registered as
  what the data gives).
- **AN2 (the multiset — registered):** the 28 outer classes of the
  published table form 14 pairs (a class and its inverse in the other
  coset) with identical order and centralizer; the multiset of (element
  order, centralizer order) over the 14 is EXACTLY {(3, 36288), (3, 648),
  (6, 576), (6, 144), (6, 72), (9, 54), (12, 288), (12, 144), (12, 96),
  (12, 12), (18, 18), (21, 21), (24, 24), (24, 24)}, and equals the
  multiset of (order, 3·|C_Ω|) over our fourteen classes.
- **AN3 (the power maps against our fibres — registered):** in the
  published table: the order-18 class has e⁶ in the class of centralizer
  5832 (= 3·1944: the heart, 3D of O₈⁺(2)), e⁹ in the class of 331776
  (= 3·110592: 2A), e² in the order-9 class (54) and e³ in the inner
  order-6 class of centralizer 648; the order-21 class has e⁷ in the
  class of 36288 (the turn) and e³ in the order-7 class (21); both
  order-24 classes have e¹² in 2A; the order-12 classes with centralizers
  288, 144, 96 have e⁶ in 2A and the one with 12 has e⁶ in 2E (9216 =
  3·3072); the order-9 class has e³ in 3D; the order-6 classes with 576,
  144 have e² in the turn's class and e³ in 2A / 2E respectively, the one
  with 72 has e² in the 648-class and e³ in 2E. Every one of these that
  our stones recorded (SM-047: eighteen → heart, 2A-type involution;
  SM-049: twelfth powers → the 1,575-class; SM-050: seventh power → the
  turn; e⁶ of the 96/144/288-classes → the 1,575-class, of the 12-class
  → the 56,700-class; SM-051: cubes of the nine → heart; cubes of the
  sixes → 1,575 / 56,700 / 56,700) agrees, with 1,575 ↔ 2A (|C_Ω| =
  110592) and 56,700 ↔ 2E (|C_Ω| = 3072). Two entries our stones did not
  record are computed here: |C_Ω((Φ·c̄)³)| = 216 (through C_Ω(x)), and
  the squares of our three order-6 classes: the 576- and 144-classes'
  squares are turns (in the class of Φ, 14,400) and the 72-class's square
  lies in the class of Φ·g₆₇₂ (806,400).
- **AN4 (the two twenty-fours told apart — registered):** the published
  order-24 classes differ by their squares: one squares into the order-12
  class of centralizer 288 (density 1/96), the other into the class of
  centralizer 96 (density 1/32). Ours: the square of type B {24:12, 12:5,
  6:1, 3:2} has cycle type {12:24, 6:10, 3:4}, the 1/32 class (by cycle
  type, SM-050); the square of type A {24:12, 12:3, 6:5, 3:2} has cycle
  type {12:24, 6:6, 3:12}, the split type, and REGISTERED: its
  Ω-centralizer (through the involution fibre over e¹²) has order 96 —
  the 1/96 class — so type A ↔ the published class whose square has
  centralizer 288 and type B ↔ the one whose square has 96. Also
  registered: the cubes of the two types lie in the two inner order-8
  classes (8A, 8B; centralizer 96 in G.3, so |C_Ω(g₈)| = 32 and the
  class of g₈ in Ω has 5,443,200 elements — why SM-049 could not
  enumerate it).
- **AN5 (the names — [obs], by rule):** inner classes named through the
  fusion (the class of O₈⁺(2) that fuses to it, or the fused triple);
  outer classes named in table order continuing the lettering per
  element order (the GAP `ClassNames` convention), with the printed
  ATLAS's own labels for the triality extension not available to us and
  said so. The table of our fourteen classes with both labels is the
  deliverable.

## Machinery

The cited headers in `_stone_an_cache/` (parsed by a small reader:
centralizers, power maps, fusion); `verify_stone_aa_roofclock.py` lines
71–696 VERBATIM and the SM-045/047/048/050 helpers for the three
computations of AN3/AN4 (C_Ω((Φ·c̄)³); the order-6 squares' classes; the
centralizer of a type-A square). Sealed caches READ-ONLY. Own cache
`_stone_an_cache/`. Outputs: `verify_stone_an_atlas_names.py`, `.log`,
`STONE_AN_ATLAS_NAMES.md`. Runtime: about ten minutes.

## Discipline

Compute, never assert; cited data quoted verbatim with source and
version; registered expectations resolvable INVERTED at equal
prominence; exact arithmetic; no registry/git writes by the executor.
Not RH/GRH. Rule 3.
