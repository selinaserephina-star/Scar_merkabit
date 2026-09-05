# STONE AG — THE SEVEN NINES

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AG_SEVEN_NINES.md` sha-locked fe4dea04… BEFORE code; no
amendment. Verifier `verify_stone_ag_seven_nines.py`, log: 18 PASS + 1
registered guess INVERTED (AG3a) — and the post-reveal exact test AG3b
turns that inversion into the stone's main finding. First run stopped on
an instrumentation error in AG4 (the brief mis-stated where an
order-24 element's eighth power lives); that log is kept as
`verify_stone_ag_seven_nines_FIRSTRUN.log`. 30 s. Machinery: Stone AA's
stage 0–2 replayed VERBATIM (lines 71–696; its nine checks re-logged as
REPLAY-AA*, all PASS; its cache write removed), sealed caches READ-ONLY;
the recomputed Φ equals `_stone_aa_cache/phi360.npy` exactly. Own cache
`_stone_ag_cache/`. Registry row SM-045.**

## 0. Discipline

Not RH/GRH. Rule 3: "nine", "beat", "clock", "meet" are labels; the
mathematics is cycle types, a minimal polynomial, conjugacy invariants and
one exact conjugacy class. The guess that the two order-3 elements are
not conjugate was ours; it was wrong; it is recorded at full prominence.

## 1. One paragraph

SM-044 left on the table that c̄₇ (the E₇ Coxeter element seen from the
roof) and Φ·c̄ (the roof's eighteen) both have exactly seven 9-cycles. As
nines they are different objects: c̄₇² has order 9 on v^⊥/v ≅ F₂⁶ with
minimal polynomial x⁶ + x³ + 1 = Φ₉(x), so F₂[c̄₇²] is the field F₆₄ and
its seven 9-cycles are the seven cosets of μ₉ in F₆₄^×, all on the 63
Paulis of one block; the roof's seven nines are 21 points per block on
which (Φ·c̄)³ acts by seven 3-cycles — 63/9 against 3 × 21/3, a counting
rhyme (AG2c, registered, confirmed). But at order 3 the two eighteens
meet: x = (Φ·c̄)⁶ and y = c̄₇⁶ are both in Ω, both have cycle type
{3: 39, 1: 3} on every block and a 2-dimensional anisotropic fixed line
on V (AG3a's invariants all agree — our registered guess that they
differ INVERTED), and the exact test decides it: the Ω-conjugacy class of
x has 89,600 elements (centralizer order 1944 = 2³·3⁵) and contains y.
The roof's eighteen and the E₇ Coxeter element share one order-3 element
up to conjugacy in Ω. The order-24 twisted elements come in exactly the
two sealed cycle types; their cubes are order-8 elements of Ω, their
eighth powers are fixed-point-free order-3 elements of the coset Ω·Φ²
with Φ²'s cycle type {3: 120}; no rowmotion in hand has order 24 and no
roof poset is named, so IB's order-24 reading is NOT SUPPORTED as stated.
Every one of the 5,039 order-18 twisted elements sampled has Φ·c̄'s
cycle type.

## 2. The roof's seven nines, located (AG1)

| power of Φ·c̄ | per block (all three equal) | in Ω |
|---|---|---|
| (Φ·c̄)³ | {6: 16, 3: 7, 1: 3} | yes |
| (Φ·c̄)⁶ | {3: 39, 1: 3} | yes |
| (Φ·c̄)⁹ | {2: 48, 1: 24} | yes |

The 63 points in 9-cycles are Fix((Φ·c̄)⁹) ∖ Fix((Φ·c̄)³), 21 per block.
[obs] The 21 vectors of the vector block span a 6-dimensional space, 135
of their 210 pairs are orthogonal, and their common orthogonal complement
is a 2-dimensional space (3 nonzero vectors) — the fixed line of x.

## 3. The Coxeter element's seven nines are a field (AG2)

c̄₇ (the E₇ Coxeter element as a 240-root permutation, reduced mod 2) has
Dickson invariant 1, order 18 on the 120, cycle type {18: 3, 9: 7, 2: 1,
1: 1}, and c̄₇⁹ = t_v (SM-044 re-seen). c̄₇² on v^⊥/v: annihilated by
x⁶ + x³ + 1, by none of x + 1, x² + x + 1, x³ + 1; order 9; cycle type
{9: 7} on the Paulis. F₂[c̄₇²] ≅ F₆₄; the seven 9-cycles are the cosets of
μ₉ in F₆₄^× [C + P].

## 4. Where the eighteens meet (AG3)

| | x = (Φ·c̄)⁶ | y = c̄₇⁶ |
|---|---|---|
| in Ω | yes | yes |
| cycle type on V, S⁺, S⁻ | {3: 39, 1: 3} each | {3: 39, 1: 3} each |
| fixed subspace on V | dim 2, q = 1 on all 3 nonzero vectors | same |
| Ω-conjugacy class size | 89,600 | 89,600 |
| centralizer order in Ω | 1944 | 1944 |
| y ∈ class(x) | **yes** (also y^Φ, y^Φ²) | |

AG3a (registered guess: not conjugate, separated by spinor-block types):
INVERTED — every invariant agrees. AG3b (post-reveal, labelled): the
class of x enumerated as 360-point permutations under conjugation by the
26 generators of Ω; y is in it. Conjugate in Ω, not merely in ⟨Ω,Φ⟩.

## 5. The order-24 twisted elements (AG4) and the order-18 ones (AG5)

Re-sampled coset Ω·Φ (30,000 draws, fixed seed): orders {3, 6, 9, 12, 18,
21, 24}, no new order; order-24 types exactly the two sealed ones.

| type on 360 | e³ (order 8, in Ω) per block | e⁶ (order 4) per block | e⁸ |
|---|---|---|---|
| {24: 12, 12: 3, 6: 5, 3: 2} | {8: 12, 4: 3, 2: 5, 1: 2} | {4: 24, 2: 6, 1: 12} | order 3, in Ω·Φ², {3: 120} |
| {24: 12, 12: 5, 6: 1, 3: 2} | {8: 12, 4: 5, 2: 1, 1: 2} | {4: 24, 2: 10, 1: 4} | order 3, in Ω·Φ², {3: 120} |

The brief wrote "eighth power (order 3, in Ω)"; e ∈ Ω·Φ and 8 ≡ 2 mod 3,
so e⁸ ∈ Ω·Φ² and moves the blocks — the first run's assertion stopped
there; corrected post-reveal, log kept. AG4b: no rowmotion in hand has
order 24; NOT SUPPORTED as stated. AG5 [obs]: all 5,039 sampled order-18
twisted elements have the cycle type {18: 16, 9: 7, 3: 3} of Φ·c̄.

## 6. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…AA2d | Stone AA stages 0–2 verbatim | 9 PASS |
| AG0a | Φ = sealed cache; Φ·c̄ type {18:16, 9:7, 3:3} | PASS |
| AG1a | 63 = 21 × 3; the three powers' block types; all in Ω | PASS |
| AG2a | c̄₇: Dickson 1, type, c̄₇⁹ = t_v | PASS |
| AG2b | c̄₇² on v^⊥/v: min poly Φ₉; F₆₄ | PASS |
| AG2c | seven nines = counting rhyme (3-cycles vs field) | PASS |
| AG3a | x, y not conjugate (guess) | **INVERTED** (all invariants agree) |
| AG3b | post-reveal: exact class test | PASS — **conjugate in Ω** |
| AG4a | order set reproduced; both order-24 types re-found | PASS |
| AG4b | no order-24 rowmotion in hand; not supported as stated | PASS |
| AG5 | order-18 types [obs] | recorded |

## 7. Grades

[C] everything in §§2–5 including the conjugacy (an enumerated class,
membership tested); [P] the field reading of AG2b (Φ₉ irreducible over
F₂ since ord₉(2) = 6); [obs] the 21-vector geometry, the order-18
uniformity of the sample (a sample, not a class count). The invariant
comparison of AG3a is [C] and was insufficient — recorded as such.

## 8. Not claimed

Nothing about the class of x in ATLAS terms (centralizer 1944 is computed,
not matched to a name); nothing about whether Φ·c̄ and c̄₇² share more
than the sixth power (their squares live in different cosets); nothing
about order-24 elements beyond the sample; no roof poset.

## 9. Synthesis line

At order 9 the seven nines were a counting rhyme; at order 3 the rhyme
became an identity — the roof's eighteen and the E₇ Coxeter element are
different elements in different cosets with one and the same order-3
heart; the opposite lesson to SM-043's two 192's, and the reason both
had to be computed rather than read off the numbers.
