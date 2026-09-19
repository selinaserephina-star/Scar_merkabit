# STONE BC — DOES THE 4-CUBE ANOMALY RECUR ON THE 8-CUBE? — NO

**Stenberg side · with Claude · 2026-09-19. Brief
`BRIEF_STONE_BC_B8_HALFTURN.md` locked fb2d5610… before code (BC0 re-checks
it). Verifier `verify_stone_bc_b8_halfturn.py`: 14 PASS + 4 INVERTED (BC3b,
BC4, BC6, BC7-law); first run 10 + 5 kept in `_FIRSTRUN.log`, two of the five
the executor's own scoring slips (below). Registry row SM-067. Merkabit-side
mathematics. Not RH/GRH; Rule 3 — "clock", "half-turn", "grammar" name
permutations and subgroups; "the 256 of Spin(17)" names a representation.**

## One paragraph

The question was whether the one exception in the family — on the 4-cube the
grammar two instants share at the half-turn, I₄, is twice the centralizer C₄
(SM-060), because the half-turn is a Weyl element on one of the clock's two
orbits (SM-063) and cannot be on the other (SM-066) — is a fact about B₄ or a
fact about free clocks, with B₈ (256 weights, W of order 10,321,920, h = 16,
sixteen free orbits of sixteen) the one decisive test in reach. **It is a fact
about B₄.** On B₈ the mechanism recurs faithfully: the orbit of λ is the
full-height orbit and its half-turn shift is exactly ±4, so Lemma BB-B forbids
a Weyl element there (BC2); exactly two orbits carry the half-turn as a Weyl
element, both by the same element w = −(e₂e₃)(e₄e₅)(e₆e₇), which negates
e₁..e₇ and fixes e₈ — the exact analogue of B₄'s −τ = −(e₂e₃) fixing e₄ — and
w is the unique Weyl element nearest to R⁸ (agreement 52 of 256) (BC3, BC4b);
Lemma B applies to its correction c = w⁻¹R⁸ (BC4a). But the consequence does
not recur: on B₄ the correction is an involution (2⁴1⁸) with a Weyl
centralizer of order 8; on B₈ it is not (cycle type 8⁸ 4¹² 3¹² 2²⁸ 1⁵²) and its
Weyl centralizer is {±1}. So **I₈ = C₈ = {±1}, and I_k = C_k at every lag** —
on B₈ (BC4, BC5), on the D₉ half-spin with W(D₉) of order 92,897,280
enumerated in full (BC6c, a disclosed tightening of the brief's
lemma-plus-sampling), and on B₆ and B₇ (BC7). The brief's conjectured law,
"the B_n spinor's shared grammar exceeds the centralizer at some lag iff n is a
power of 2", is refuted at its first new instance (BC7-law INVERTED): among
B₃..B₈ the anomaly lives on B₄ alone, with B₃'s signature explained by its
overgroup W(D₄) (SM-060).

## Registered guesses vs outcomes

| bar | registered guess (brief §2) | outcome |
|---|---|---|
| BC1 | R free on the B₈ spinor: 16 orbits of 16 | **PASS** — type 16¹⁶, order 16 |
| BC2 | O₁ ∋ λ full-height, ranks 0,1,1,…,7,7,8 around the clock; shift ±4; no u reproduces it | **PASS** — in R-order the ranks read 0,8,7,7,…,1,1 (the same cycle, the other way); shifts {±4}; O₁ spans 𝔽₂⁸; no u. First run FAILED on the reading direction alone |
| BC3 | ≥ 1 orbit ≠ O₁ carries the half-turn as a Weyl element | **PASS** — exactly two (O15, O16), both by w = −(e₂e₃)(e₄e₅)(e₆e₇) |
| BC3b | (low confidence) exactly 2, exchanged by w₀ = −1 | **INVERTED** — exactly 2, but −1 fixes each (−1 fixes 8 orbits and swaps 4 pairs) |
| BC4 | |I₈| > |C₈|, I₈ = C_W(c) by Lemma B, ratio 2 | **INVERTED** — I₈ = C₈ = {±1}; Lemma B holds and predicts exactly this (C_W(c) = {±1}) |
| BC5 | I_k = C_k on B₈ for k ≠ 8 | **PASS** — |I_k| = |C_k| = 1 for k ≠ 8, 2 at k = 8 |
| BC6 | (low confidence) D₉ carries a coprime-lag survivor that is a pure permutation moving e₉ | **INVERTED** — on D₉, I_k = C_k at all 15 lags (full enumeration); C₈(D₉) = {1, −(e₁..e₈)} |
| BC7 | B₆, B₇ clean at every lag | **PASS** — B₆ (R type 12⁵4¹), B₇ (14⁹2¹); half-turn survivors {±1} |
| BC7-law | the stated conjecture: anomaly iff n a power of 2 | **INVERTED** at n = 8 |
| BC8 | what distinguishes the carrying orbits | **[obs]** carrying ⇔ ranks ⊆ {3,4,5} = {n/2−1, n/2, n/2+1} ⇔ every half-turn shift is ±1; the same on B₄ (O₂ has ranks {1,2,3}) |

Cross-checks not in the brief: **BC1-x** the B₈ spinor rowmotion (AV
machine), the D₉ half-spin rowmotion (AV machine, ninth coordinate dropped) and
D₉ ω₉ from the Cartan matrix (AQ `Minuscule`, labels → signs) are one
permutation of the 256 sign patterns; **BC-engine** the new affine (π, v)
engine reproduces Stone AV's materialised I_k and C_k as sets on B₄ (all 7
lags), B₅ (all 9) and the D₅ half-spin (all 7); **BC2-orient** R(λ) = w₀λ on
B₄ and B₈ (the paper's §7.6 Lemma (a)); **BC4a** Lemma B at n = 8; **BC4b**
the carrying element and the B₄ contrast; **BC6a** containment (vacuous: no
extras); **BC6c** the D₉ full enumeration.

## The numbers, with the bar that produced them

All quantities are exact integers (group orders, orbit sizes, agreement
counts); no model band applies.

| quantity | value | bar |
|---|---|---|
| B₈: |I_k|, |C_k| for k = 1..15 | 1 = 1 at every k ≠ 8; **2 = 2 at k = 8** ({±1}) | BC4, BC5 |
| D₉ half-spin: |I_k|, |C_k| for k = 1..15 | identical to B₈ (C₈(D₉) = {1, −(e₁…e₈)}) | BC6c |
| B₆ (h = 12): |I_k| = |C_k| | 1 at every lag, 2 at k = 6 | BC7 |
| B₇ (h = 14): |I_k| = |C_k| | 1 at every lag, 2 at k = 7 | BC7 |
| carrying orbits on B₈ | 2 of 16: O15 (min element 19), O16 (min 25); ranks 3..5; every shift ±1 | BC3, BC8 |
| the carrying element | w = −(e₂e₃)(e₄e₅)(e₆e₇), e₈ fixed; v = u = 1111111·0 (weight 7); shift = 7 − 2|x∩u| = ±1 ⇔ |x∩u| ∈ {3,4} | BC4b |
| nearest Weyl element to R⁸ (whole board) | w, unique; agreement 52/256 (altitude 204); Fix(c) = 52 = O15 ∪ O16 (32) + 20 more | BC4b |
| the correction c = w⁻¹R⁸ | cycle type 8⁸ 4¹² 3¹² 2²⁸ 1⁵²; Fix(c) affinely spans; C_W(c) = {±1} | BC4a, BC4b |
| B₄ by the same engine | −τ = −(e₂e₃), e₄ fixed; c₄ = (−τ)⁻¹R⁴ of type 2⁴1⁸; C_W(c₄) of order 8 = I₄ | BC4b |
| altitude of R^k against W(B₈), k = 1..15 | 214, 236, 238, 240, 238, 224, 229, **204**, 229, 224, 238, 240, 238, 236, 214 | BC6 |
| altitude of R^k against W(D₉) | 214, 236, 238, 236, 222, 224, 205, **204**, 205, 224, 222, 236, 238, 236, 214 | BC6 |
| best Weyl agreement with R⁸ per orbit (O1..O16) | 8, 4, 4, 4, 6, 8, 4, 6, 4, 4, 4, 4, 4, 8, **16, 16** (same against W(D₉)) | BC3, BC6 |
| −1 on the sixteen orbits | fixes O1, O2, O6, O7, O10, O14, O15, O16; swaps (3,4), (5,8), (9,12), (11,13) | BC4b |
| wall time | C₈ 1.2 s, I₈ 1.9 s (10,321,920 elements each); 14 further B₈ lags 69 s; D₉ 15 lags 583 s (92,897,280 elements per lag); whole verifier 798 s | BC4–BC6 |

The half-turn rank-shift multisets of all sixteen orbits are in the log (BC3,
BC8): O₁ {±4}¹⁶; the two carrying orbits {±1}¹⁶; every other orbit mixes
magnitudes and contains a shift of magnitude ≥ 2.

## What it means for the paper

**§7.12.4 (v1.0), the sentence that replaces "B₈ next":** *"… the n > 4 case
reducing to the fact that the shift is exactly ±n/2 (verified at B₄ and at B₈,
SM-067). B₈: the anomaly does not recur. On the 8-cube the half-turn is again a
Weyl element on exactly two of the clock's sixteen orbits, by the analogue
−(e₂e₃)(e₄e₅)(e₆e₇) of −τ, but the correction's Weyl centralizer is {±1}, so
I₈ = C₈ and I_k = C_k at every lag — on B₈, on the D₉ half-spin, on B₆ and B₇;
among B₃..B₈ the shared grammar exceeds the centralizer only on the 4-cube."*
(Placed by `build_v1.py`, with a line in §13 and the unit listed in Appendix A
as the one cited unit not yet JOINT.) In the mathematics edition (v2.0):
§6.4 with Proposition 6.7 (C) and Remark 6.8, open problem 3 restated (is B₄
the only anomalous B_n spinor for n ≥ 4?), Appendix B row.

**A record correction, in passing (BC2-orient).** On the house machine
R(λ) = w₀λ — the paper's own §7.6 Lemma (a). Stone BB's O₁ list
(0,1,1,2,2,3,3,4) is therefore in the order of R⁻¹, and the phrase "rowmotion
sends w₀λ straight to λ" (BB5; also the parenthetical in the proof of Theorem
6.2 of v2.0, now corrected to Lemma 3.1(a)) is R⁻¹'s reading. Nothing in
Theorem BB or in this stone depends on the direction: the half-turn is its own
inverse. SM-066 is not reopened.

## Why the consequence fails at n = 8 (what is proved, what is seen)

Lemma B is exact on both boards: I_{h/2} ∩ Stab_W(Fix c) = C_W(c), and here
every element of I₈ stabilises Fix(c), so I₈ = C_W(c). The difference is c
itself. On B₄, R⁴ and −τ are both involutions agreeing on O₂, so c = (−τ)R⁴ is
an involution (identity on O₂, fixed-point-free on O₁) and eight Weyl elements
commute with it. On B₈, w is an involution and R⁸ is an involution, but they
agree on only 52 of 256 points, and c has cycles of length 8, 4, 3 and 2 on
the other 204; no Weyl element beyond ±1 commutes with such a permutation. The
carrying orbits are also no longer "the other orbit": they are two of sixteen,
the orbits confined to the middle rank band, and their agreement set with w
extends by 20 further points that lie on no carrying orbit. That the band
{n/2−1, n/2, n/2+1} characterises the carrying orbits on both boards is an
observation; a proof was not found this session and none is claimed.

## Not claimed

Nothing about B₁₆ (65,536 weights) or beyond; no proof that C_W(c) = {±1} for
every n > 4, nor of the rank-band characterisation (two boards); nothing about
non-minuscule posets; D₉ only to the stated depth (every lag, by full
enumeration in the affine form — an extension of the brief's scope, disclosed);
nothing physical. The "power of 2" law of the brief is refuted, not replaced:
the surviving statement is "among B₃..B₈, only B₄ (and B₃ by its overgroup)",
a computation on six boards.

## Discipline notes

Brief locked before code; verifier checks the lock first; first run kept
(`verify_stone_bc_b8_halfturn_FIRSTRUN.log`: 10 PASS + 5 FAIL — BC2 scored the
literal rank list against the clock's direction, BC6a demanded extras that do
not exist; both re-scored with disclosure, the three genuine inversions BC3b,
BC4, BC6 unchanged, and BC7-law added post-reveal to state the brief's own
conjecture at equal prominence). The D₉ full enumeration tightens the brief's
"lemma and sampling" (bars move one way only). W(B₈) and W(D₉) were never
materialised as tuples (brief §3 step 2). Nothing sent; packaging for Ilya on
Selina's word.

## Synthesis line

The mechanism travelled to the next free clock intact — the same shaped Weyl
element on the same kind of middle-band orbit — and the consequence died on
arrival, because what carried the anomaly on the 4-cube was not the mechanism
but the coincidence that its correction was an involution: the exception of
§7.12 was a property of a small board's arithmetic, not of the family.
