# STONE AF — THE THREE EIGHTEENS

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AF_THREE_EIGHTEENS.md` sha-locked 52baa7b7… BEFORE code; no
amendment. Verifier `verify_stone_af_three_eighteens.py`, log: 13 PASS, 0
FAIL; 0.1 s; only `scar56_data.json` (SM-005), the E₈-root replay of
SM-040/041 verbatim, and the sealed SM-039 log read for two cycle types.
One non-registered consistency check (AF4c) failed on the first run by an
ordering bug in the check itself (the mod-2 product applied the seven
reflections in the reverse order of the real product); the first-run log
is kept as `verify_stone_af_three_eighteens_FIRSTRUN.log`, the check
corrected, 13/13 on the second run. Registry row SM-044.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "gear", "remember" are labels; the
mathematics is orbit structures, agreement counts, a Dickson invariant and
a coset argument. IB's two prompts are answered by his own decision rules.

## 1. One paragraph

Three objects carry the number 18 = h(E₇): the merkabit's clock Ψ, the E₇
Coxeter element c₇ on the 56 weights, and the roof's Φ·c̄ (SM-039). They
are three different objects. Ψ is rowmotion (SM-041) and shares the
Coxeter element's orbit structure [18, 18, 18, 2] exactly — the Rush–Shi
equality of orbit structures, seen on the data — and nothing else of it:
it is not a Weyl element (the board masks span V and no linear map agrees
with Ψ), it agrees with the best of the 64 Coxeter elements on 14 of 56
points, and its ninth power is not the chirality bit ι, whereas c⁹ = ι for
every Coxeter element. Seen from the roof, c̄₇ has Dickson invariant 1: it
sits outside Ω in ι's coset, while Φ·c̄ sits in the triality coset; in
Ω:S₃ conjugation preserves the coset's class in S₃, so they are not
conjugate, and Φ·c̄'s sealed cycle type on 360 ({18: 16, 9: 7, 3: 3})
matches no rowmotion orbit structure in hand. Under IB's own rule, "Φ·c̄
or an order-24 element is rowmotion on a roof poset" is NOT SUPPORTED as
stated; the only 18-clock that is rowmotion is the merkabit's. And his
"what exactly does Ψ remember?": not a type. P-pairs and S-pairs survive
alike (66.7 % and 65.7 %), the 28 antipodal pairs are destroyed at once
(1 of 28, random 1.7 %) and come back whole at the ninth beat, where
P = S = 460 / 756 exactly.

## 2. What Ψ remembers, by type (his PROMPT of 2026-09-04)

| k | overall | v kept | P kept | S kept |
|---|---|---|---|---|
| 1 | 65.06 % | 1 / 28 | 504 / 756 | 497 / 756 |
| 2 | 54.68 % | 1 / 28 | 424 / 756 | 417 / 756 |
| 3 | 51.30 % | 1 / 28 | 393 / 756 | 396 / 756 |
| 9 | 61.56 % | 28 / 28 | 460 / 756 | 460 / 756 |
| 17 | 65.06 % | 1 / 28 | 504 / 756 | 497 / 756 |

Random baseline (200 permutations): v 1.7 %, P 49.2 %, S 49.2 %. Full
table k = 1..17 and the 3 × 3 transition counts in the log. At k = 1 the
v-pairs go to P (10) and to S (17); the eight antipodal steps of SM-041
are the states with Ψu = ιu. His decision rule ("one type survives much
better than the others; the surviving type matches the seven or the
bridge"): NOT met — no type is privileged. Ψ⁹ commutes with ι (forced by
SM-012's ιΨι = Ψ⁻¹ and order 18), is fixed-point-free, and is not ι.

## 3. Ψ against the E₇ Coxeter element

- The 7! orderings of the seven simple reflections (BETA base of SM-040)
  give exactly 64 distinct Coxeter elements (2⁶, the acyclic orientations
  of the E₇ diagram); all of order 18, all with cycle type [18, 18, 18, 2]
  on the board, all with c⁹ = ι (the exponents of E₇ are odd).
- Ψ has the same cycle type — and is not in W(E₇): the 56 masks have
  F₂-rank 8, and the linear map defined by Ψ on eight independent board
  points disagrees with Ψ (SM-040's "no linear extension", re-seen).
- Agreement of Ψ (or Ψ⁻¹) with the 64 Coxeter elements, by number of
  board points: {5: 4, 6: 10, 7: 10, 8: 12, 9: 4, 10: 8, 11: 6, 12: 4,
  14: 6}; maximum 14 of 56. [obs] For a best c, Ψ∘c⁻¹ has cycle type
  [24, 11, 5, 2, 1¹⁴], order 1320, and the same type-score as Ψ (0.6506,
  as it must, c being linear).

## 4. The Coxeter element from the roof, and the roof's own eighteen

c̄₇ = t_β₁ ⋯ t_β₇ on the 120 nonsingular vectors: a q-isometry fixing v,
Dickson invariant 1 — outside Ω = W⁺(E₈)/±, in the coset of ι = t_v.
Cycle type on the 120: one fixed point (v), one 2-cycle and three
18-cycles on the board (= c₇ on the weights, checked: the mod-2 image of
a Coxeter element with the same ordering is the same permutation of the
56), seven 9-cycles on the 63 Paulis. Φ·c̄ lies in Ω·Φ (⟨Ω,Φ⟩ = Ω:3,
SM-039); c̄₇ in Ω·ι; in Ω:S₃ (SM-036) a 3-cycle is not a transposition, so
the two are not conjugate [P on computed inputs]. Φ·c̄'s sealed cycle
type on 360 is {18: 16, 9: 7, 3: 3}; the rowmotion orbit structures in
hand are [18, 18, 18, 2] on 56 (E₇) and [12, 12, 3] on 27 (E₆ sheets,
SM-041); no match, and no roof poset is named. NOT SUPPORTED as stated.
[obs, not pursued] both c̄₇ and Φ·c̄ have exactly seven 9-cycles.

## 5. Bars

| bar | registered | outcome |
|---|---|---|
| AF0a | type = sign of the E₇ inner product | PASS |
| AF1a | k = 1: v 1/28, P 504/756, S 497/756 | PASS |
| AF1b | no type privileged; his rule not met | PASS |
| AF1c | k = 9: all v kept, P = S = 460; Ψ⁹ commutes with ι, ≠ ι | PASS |
| AF2a | 64 Coxeter elements, all [18,18,18,2], c⁹ = ι; Ψ same type | PASS |
| AF2b | Ψ ∉ W(E₇) (rank 8, no linear map agrees) | PASS |
| AF3a | max agreement 14 of 56 | PASS |
| AF4a | c̄₇ isometry, fixes v, Dickson 1 (ι's coset) | PASS |
| AF4b | cycle type {1:1, 2:1, 18:3, 9:7} | PASS |
| AF4c | mod-2 image = real Coxeter action on the 56 (consistency, not registered) | PASS on rerun (first run: ordering bug in the check) |
| AF5a | c̄₇ and Φ·c̄ not conjugate (coset argument) | PASS |
| AF5b | Φ·c̄ matches no rowmotion in hand; IB's rule: not supported | PASS |

## 6. Grades

[C] AF0a–AF4c, AF5b's comparison; [P] AF5a's coset argument on computed
inputs (Dickson 1; ⟨Ω,Φ⟩ = Ω:3 from SM-039; Ω:S₃ from SM-036), the
exponent argument for c⁹ = ι, and the Rush–Shi orbit-structure equality
[cited], here seen on the data; [obs] the agreement distribution, the
Ψ∘c⁻¹ type, the seven 9-cycles. Φ·c̄'s cycle type is sealed SM-039 data,
read, not recomputed.

## 7. Not claimed

No statement about order-24 twisted elements beyond "no poset is named";
no rowmotion on any non-minuscule roof poset was tested (none was
proposed); nothing about the Rush–Shi bijection itself; nothing about
Ψ⁹ beyond what is computed (it commutes with ι and is not ι).

## 8. Synthesis line

Three eighteens, three rooms: the merkabit's clock keeps the Coxeter
element's rhythm and none of its linearity; the roof's eighteen lives in
the triality coset where no rowmotion has been named — the same lesson
as SM-043's two 192's, one floor up: a shared number is a rhyme, not an
identity, and Rule 3 is what turns a rhyme into a computation.
