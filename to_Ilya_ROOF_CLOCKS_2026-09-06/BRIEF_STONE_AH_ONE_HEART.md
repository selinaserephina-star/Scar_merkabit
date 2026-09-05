# BRIEF — STONE AH: THE ONE HEART

**Staged 2026-09-05 on Selina's "continue" (the two candidates named at the
end of SM-045). Locked before code (`BRIEF_STONE_AH_LOCK.sha256`).
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

SM-045 found that the roof's twisted eighteen Φ·c̄ and the E₇ Coxeter
element c̄₇ share one order-3 element up to conjugacy in Ω: (Φ·c̄)⁶ ~ c̄₇⁶,
class of 89,600, centralizer 1944. Which other clocks of the roof have
the same heart? The candidates, with their fixed dimensions on the E₈
lattice predicted by the exponents (an order-3 power of a Coxeter element
of order h fixes exactly the eigenvectors whose exponent m has 3 | m·(h/3)
… i.e. the count of exponents divisible by 3 · gcd, worked below), and
measured mod 2:

```text
c̄⁵   (E₈ Coxeter image, order 15; c̄⁵ of order 3)     exponents 1,7,11,13,17,19,23,29: none ≡ 0 mod 3 → fixed dim 0
c̄₇⁶  (E₇ Coxeter, order 18)                           exponents 1,5,7,9,11,13,17: one (9) → fixed dim 1 + 1 (α) = 2   [SM-045: measured 2]
c̄₆⁴  (E₆ Coxeter, order 12, inside E₇ by deleting node 6 of C7)  exponents 1,4,5,7,8,11: none → fixed dim 0 + 2 (E₆^⊥ = A₂) = 2
c̄₄²  (D₄ Coxeter, order 6, nodes {1,2,3,4} of C7)     exponents 1,3,3,5: two → fixed dim 2 + 4 (D₄^⊥) = 6
```

For a semisimple element of order coprime to 2 the fixed dimension is the
same in characteristic 0 and mod 2, so these are predictions [P] to be
measured [C]. Conjugacy in Ω is then decided exactly by class enumeration
(SM-045's method), not by invariants.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AH0a (replay):** Stone AA stages 0–2 VERBATIM as in SM-045 (checks
  re-logged REPLAY-AA*, cache write removed); Φ equals the sealed cache;
  x = (Φ·c̄)⁶ and its Ω-class (89,600; centralizer 1944) re-enumerated;
  y = c̄₇⁶ in it (SM-045 re-seen).
- **AH1 (fixed dimensions — registered from the exponents):** on V the
  fixed subspaces have dimensions c̄⁵: 0 (cycle type {3: 40} on the 120,
  no fixed nonsingular vector); c̄₆⁴: 2, with q = 1 on all three nonzero
  vectors (the A₂ lattice mod 2 is an anisotropic line); c̄₄²: 6. All three
  elements lie in Ω (even Dickson invariant).
- **AH2 (the heart — registered):** c̄₆⁴ ∈ class(x) (the E₆ clock's order-3
  power is conjugate in Ω to the roof's and the E₇'s: ONE heart for the
  three clocks 12, 18, 18); c̄⁵ ∉ class(x) and c̄₄² ∉ class(x) (different
  fixed dimensions — [P], and measured by membership). The Ω-classes of
  c̄⁵ and c̄₄² enumerated (sizes and centralizer orders recorded, cap 1.5 M).
- **AH3 (the clocks on the board — registered):** the E₆ Coxeter element
  acts on the 56 roots with ⟨r,α⟩ = 1 with cycle type {12: 4, 3: 2, 1: 2}
  (= two copies of the E₆ rowmotion orbit structure [12, 12, 3] of SM-041
  plus the two singlets — Rush–Shi at E₆, seen on the data); the E₇
  Coxeter element with [18, 18, 18, 2] (SM-044 re-seen); the D₄ Coxeter
  element's cycle type on the 56 recorded [obs].
- **AH4 (are the order-18 twisted elements one class? — necessary
  conditions, registered):** for 300 sampled order-18 elements e of the
  coset Ω·Φ: every e⁶ lies in class(x) and every e⁹ lies in the Ω-class
  of (Φ·c̄)⁹ (that involution class enumerated; size and centralizer
  recorded). If both hold the single-class question stays OPEN-but-
  consistent (recorded so); any failure settles it: more than one class.
- **AH5 ([obs] only):** the element-order census of the centralizer of x
  is NOT computed (no centralizer machinery); the class size 89,600 =
  2⁹·5²·7 and 1944 = 2³·3⁵ recorded as arithmetic.

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM (as SM-045); the
class-enumeration and block-cycle-type helpers of
`verify_stone_ag_seven_nines.py` VERBATIM; the E₇ base BETA as in
SM-040/041/045; reflections on the 240 roots for the Coxeter elements of
E₈, E₇, E₆, D₄ (E₆ and D₄ as sub-diagrams of the C7 base: nodes {0..5}
and {1,2,3,4}). Sealed caches READ-ONLY. Own cache `_stone_ah_cache/`.
Outputs: `verify_stone_ah_one_heart.py`, `.log`, `STONE_AH_ONE_HEART.md`.
Runtime: about a minute.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3: "heart",
"clock" are labels; the mathematics is fixed dimensions and Ω-conjugacy
classes.
