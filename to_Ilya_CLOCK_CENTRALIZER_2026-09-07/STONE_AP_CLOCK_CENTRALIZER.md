# STONE AP — THE CLOCK'S LINEAR CENTRALIZER

**Stenberg side · with Claude · 2026-09-07. Brief
`BRIEF_STONE_AP_CLOCK_CENTRALIZER.md` sha-locked 68959fb4… BEFORE code; no
amendment. Verifier `verify_stone_ap_clock_centralizer.py`, log: 22 PASS +
2 FAIL — AP7 a registered guess INVERTED (real, informative), AP4d a
registered value that was the auditor's own arithmetic slip, corrected by
the labelled post-reveal AP4d-b; the first run (AP4c instrumentation:
Counter keys instead of a list, collapsing the two order-7 classes) is
kept as `verify_stone_ap_clock_centralizer_FIRSTRUN.log`. 3.3 s. Model:
`scar56_data.json` (SM-005, sha256 0a817fc5…, READ-ONLY); board machinery
verbatim from Stone AC/AF. Own cache `_stone_ap_cache/witnesses_ap.json`.
Registry row SM-054.**

## 0. Discipline

Not RH/GRH. Rule 3: "marker", "descent", "inbreath" are IB's labels; the
mathematics is a centralizer computation in S₅₆, a subgroup chain, and
class counts. Two registered items failed and are reported at the same
prominence as the twenty-two that passed.

## 1. One paragraph

IB asked for a canonical generating pair (a,b) of one of the still point's
36 PSL(2,7) copies so that he could test whether the clock Ψ fixes exactly
one of the three C₂'s in his V₄. No pair is needed. Every C₂ he can build
is an element of W(E₇) acting on the 56 (SM-013: the bridge class lifts
uniquely into W(E₇) = 2 × Sp₆(2); SM-040: the still point's action on the
board is that action), and **the centralizer of Ψ in S₅₆ — 69,984
permutations, built explicitly from the cycle type [18,18,18,2] — meets
W(E₇) in the identity alone.** Its 231 involutions all fail the pair-type
test. So Ψ C₂ Ψ⁻¹ = C₂ holds for no C₂ of any copy under any pair: his
test is NOT SEALED, universally. A bridge copy built in our own
coordinates (one targeted (2,3,7) search) confirms the setting: order 168,
orbits [28,28], SM-013's permutation character 2(χ₁+2χ₆+χ₇+χ₈) reproduced
class by class (fixed points 56/8/2/0/0/0), and the seven restricting to
it irreducibly as χ₇; all 336 of its (2,3,7)-generating pairs give his
S₄ ⊃ A₄ ⊃ V₄ ⊃ three C₂'s exactly as he describes, reach all 14 V₄'s, and
0 of the 3 C₂'s is Ψ-normalized for every one of them. On his bookkeeping:
his two "channels" D = lost − created and π·ΔL = c_nt(G) − c_nt(H) are the
same number identically (1, 1, 0, 2, 1), and his D(A₄,V₄) = 2 is refuted —
A₄'s involution class splits into V₄'s three, so D = 0, as three of his own
documents say. The registered guess that the best linear agreement among
the 231 Ψ-commuting involutions would be pr-like was inverted the
informative way: the maximum IS pr's exact number, 1432/1540, but the
maximizer is the transposition of the clock's own axis pair, and 1432 =
1540 − 2·54 is forced for any transposition — a number repeated, not a
structure repeated. This sharpens SM-044 (Ψ ∉ W(E₇); best agreement 14 of
56) to **C_{W(E₇)}(Ψ) = 1**.

## 2. Bars

| bar | registered | result |
|---|---|---|
| AP0 | brief locked | PASS (68959fb4…) |
| AP1a/b | pair type = sign of ⟨w,w′⟩ (1512/1512/56); ι linear, trace −7; the seven reflections linear, trace 5 | PASS |
| AP2a–c | Ψ type [18,18,18,2]; centralizer 18³·3!·2 = 69,984 explicit, all commuting; 231 involutions | PASS |
| **AP3a** | **C_{S₅₆}(Ψ) ∩ W(E₇) = {1}** | **PASS** (1 linear element of 69,984: the identity) |
| AP3b | 0 of 231 involutions linear | PASS |
| AP3c | Ψ⁹, ιΨ⁹ commute with Ψ, neither linear (SM-016 re-seen) | PASS (kept 948/1540 each) |
| AP7 | best kept among the 231 = 1432/1540 with maximizers of pr's type 2²⁷1² | **FAIL — INVERTED**: max = 1432/1540 exactly, the unique maximizer has type 2¹1⁵⁴ |
| AP7b (post-reveal) | the maximizer is the swap of Ψ's 2-cycle (the axis ι-pair, SM-012); any transposition of an ι-pair touches 108 pairs and keeps 1432 | PASS |
| AP4a/b | a bridge PSL(2,7) found (34,369 samples, first (2,3,7) pair tried); all linear; orbits [28,28] | PASS |
| AP4c | census 1/21/56/42/24/24 | PASS (first run: instrumentation, log kept) |
| AP4d | fixed points 56/8/2/**4**/0/0 (as written in the brief) | **FAIL** — measured 56/8/2/**0**/0/0 |
| AP4d-b (post-reveal) | 2(χ₁+2χ₆+χ₇+χ₈) from SM-001's table = (56,8,2,0,0,0) = measured; the brief's 4 used χ₇(4A) = +1 against its own AP4e | PASS |
| AP4e | traces on the seven 7/−1/1/−1/0/0 = χ₇ | PASS |
| AP5a–d | 21 involutions, 56 order-3, 336 generating pairs; his words give 24 ⊳ 12 ⊳ 4 with three C₂'s one A₄-orbit (normalizer 4) for all 336; all 14 V₄'s reached; **0 Ψ-fixed C₂'s over all 336 pairs** | PASS |
| AP6a–c | class counts 5,4,3,3,1,0; (lost, created) = (2,1),(2,1),(2,2),(2,0),(1,0); D = 1,1,0,2,1 = c_nt differences identically; D(A₄,V₄) = 0 | PASS |

[obs] Involution fixed-point spectrum of W(E₇) on the 56 as sampled:
0 (287), 8 (1), 16 (1481) among 34,369 random words of length 30 —
the reflection class (32 fixed) was not reached by such words; not a
claim about the classes. [obs] pr: kept 1432/1540, type 2²⁷1², does not
commute with Ψ (SM-012 re-seen).

## 3. His request, answered

He wrote: "SEALED if exactly one C₂ is fixed by Ψ. Otherwise NOT SEALED."
The answer is NOT SEALED, and the reason is stronger than the test: the
clock commutes with **nothing** linear. There is no canonical (a,b) to
choose because the outcome does not depend on the choice; the pair found
here (`witnesses_ap.json`, `bridge_pair_a/b`) is offered as a convenience,
with the convention stated in the log, not as a canon. Universality over
the 36 copies of the still point and the 4,320 copies of the bridge class
in Sp₆(2) is one line: each is a subgroup of W(E₇) on the 56, and AP3a
holds for all of W(E₇) at once.

## 4. Corrections returned, at equal prominence

1. **D ≡ π·ΔL.** With his definitions, c_nt(H) = c_nt(G) − lost + created,
   so D = lost − created = c_nt(G) − c_nt(H). The "two channels" are one.
   "(D, ΔL) = (0, 0)" is one condition; his abelian-boundary theorem
   stands as a table on the fixed chain, not as a mechanism.
2. **D(A₄,V₄) = 0, not 2.** The involution class of A₄ (size 3) splits
   into the three classes of V₄; created = 2, lost = 2 (3A, 3B).
3. "Lossless" is a class-count word: the step loses log₂3 = 1.585 bits of
   order (his own Level-5 number).
4. His "Ψ cannot act through χ₈" (18 ∤ 168) is true and now exact: no
   Weyl-group element commutes with Ψ, so no linear map from any
   W(E₇)-module to his generation plane can be Ψ-equivariant.

## 5. Not-claims

Nothing here touches his 1/π, his crystal identifications, or his flavon
model (all PARKED, Rule 3). The sampled involution spectrum is an
observation, not a classification. The trace formula is exact but was
validated on two classes only (ι, reflections) — sufficient for AP4e,
where every value came out an integer of the predicted table.

## 6. Synthesis line

He asked the board for a choice and the board had none to give — SM-016's
altitude and SM-044's three rooms again: the clock is the one thing on the
board that is not linear, and every marker the descent can build is
linear. The one number that did repeat (1432) belonged to a transposition,
not to the mirror.
