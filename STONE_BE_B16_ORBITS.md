# STONE BE — THE 16-CUBE AT THE ORBIT LEVEL

**Stenberg side · with Claude · 2026-09-19. Brief `BRIEF_STONE_BE_B16_ORBITS.md`
locked 60a27db0… before code (BE0 re-checks it). Verifier
`verify_stone_be_b16_orbits.py`: 9 PASS + 2 INVERTED (BE4, BE4b), 30 s; first
run 6 + 4 kept in `_FIRSTRUN.log` (two of its four failures were one
instrumentation error in the centralizer search — the column test compared
against g's images instead of π's, rejecting every element with a translation,
−1 among them; fixed, and the fixed search is cross-checked against Stone
BC/BD's enumerations on B₈ in BE6-engine). Registry row SM-069. Merkabit-side
mathematics. Not RH/GRH; Rule 3 ("the 65,536 of Spin(33)" names a
representation). W(B₁₆) is never enumerated; |I₁₆| is not claimed.**

## One paragraph

On the third free spinor clock, B₁₆ (65,536 weights, h = 32, W of order
2¹⁶·16! ≈ 1.4 × 10¹⁸), everything that Stone BC saw on B₈ and Stone BD
explained recurs, at larger scale and with one surprise in the count. The
clock (computed combinatorially on the shifted staircase δ₁₆ and validated
against the sealed clocks of B₄ and B₈, BE1) is free with 2,048 orbits of 32
(BE2); the orbit of λ is full-height with half-turn shift exactly ±8, so Lemma
BB-B applies at m = 8 (BE3). **Sixteen** orbits — not two — carry the
half-turn as a Weyl element, and all sixteen by the same element
w = −(e₂e₃)(e₄e₅)…(e₁₄e₁₅) with e₁₆ fixed, the shape of −τ continued; they
are exactly the orbits whose ranks stay in {7, 8, 9}, equivalently those on
which every half-turn shift is ±1 (BE4c; the band now on three boards, with
1, 2, 16 carrying orbits). Stone BD's criterion lands in its negative case
again: w does not commute with R¹⁶, so its correction c is not an involution;
its agreement set Y = Fix(c) has 1,900 points, its stabilizer in W is exactly
⟨−1, w⟩, and C_W(c) = {±1} — hence, by Lemma B, **no half-turn survivor beyond
±1 preserves Y** (BE5); also C_W(R¹⁶) = {±1} (BE6). What is left open is
exactly what the brief said: whether some element of I₁₆ moves Y.

## Guesses vs outcomes

| bar | registered guess | outcome |
|---|---|---|
| BE1 | combinatorial rowmotion = sealed clocks on B₄, B₈; order 32, |P| = 136 on δ₁₆ | **PASS** |
| BE2 | 2,048 free orbits of 32 | **PASS** |
| BE3 | O₁ full-height, shift ±8, spans, no u | **PASS** (ranks in R-order 0,16,15,15,…,1,1) |
| BE4 | exactly 2 carrying orbits, same w, each fixed by −1, band ⇔ carrying ⇔ shifts ±1 | **INVERTED on the count**: 16 carrying orbits; same w; −1 fixes 8 and swaps 4 pairs; band and shift equivalences hold |
| BE4b | every orbit affinely spans 𝔽₂¹⁶ | **INVERTED**: 1,987 span; 54 have dim 15, 6 dim 14, 1 dim 13 (all sixteen carrying orbits span, so their w is unique) |
| BE4c | post-reveal: the parts of BE4 that hold, stated separately | **PASS** |
| BE5 | w ∉ C_W(R¹⁶), c not an involution, Y spans, Stab_W(Y) = ⟨−1, w⟩, C_W(c) = {±1} ⇒ I₁₆ ∩ Stab_W(Y) = {±1} | **PASS** |
| BE6 | C_W(R¹⁶) = {±1} | **PASS** (first run: {1}, the instrumentation error above) |
| BE6-engine | the searches reproduce BC/BD's enumerated B₈ answers | **PASS** |
| BE7 | [obs] |Fix c|, cycle type | recorded |

## The numbers (exact; no model band)

| quantity | value | bar |
|---|---|---|
| orbits of R on B₁₆ | 32²⁰⁴⁸ (free) | BE2 |
| O₁ ranks around the clock | 0,1,1,…,15,15,16; half-turn shift ±8; no u ∈ 𝔽₂¹⁶ reproduces it | BE3 |
| carrying orbits | 16 (O2012, 2013, 2014, 2015, 2018, 2019, 2020, 2026, 2027, 2028, 2030, 2031, 2032, 2045, 2046, 2048 in min-element order); all ranks in {7,8,9}; all shifts ±1 | BE4c |
| carrying element | w = −(e₂e₃)(e₄e₅)(e₆e₇)(e₈e₉)(e₁₀e₁₁)(e₁₂e₁₃)(e₁₄e₁₅), e₁₆ fixed; unique per orbit (each carrying orbit spans) | BE4c |
| −1 on the carrying orbits | fixes 2020, 2026, 2028, 2030, 2032, 2045, 2046, 2048; swaps (2012,2013), (2014,2019), (2015,2018), (2027,2031) | BE4c |
| orbits with a reproducing u | exactly the 16 carrying orbits | BE4c |
| affine dimensions of the 2,048 orbits | 16: 1,987; 15: 54; 14: 6; 13: 1 | BE4b |
| w ∈ C_W(R¹⁶)? c² = 1? | no; no | BE5 |
| Y = Fix(c) | 1,900 points (2.90%; B₄ 50%, B₈ 20.3%), affinely spanning; 512 of them on the sixteen carrying orbits, 1,388 on no carrying orbit | BE5, BE7 |
| Stab_W(Y) | ⟨−1, w⟩, order 4 (4 candidate translations survive the rank-histogram filter; 1.6 s) | BE5 |
| C_W(c) | {±1} | BE5 |
| C_W(R¹⁶) | {±1} (11,552 candidate translations, 2.9 s) | BE6 |
| I₁₆ ∩ Stab_W(Y) | {±1} — by Lemma B (Y spanning) | BE5 |
| wall time | 30 s (u-survey over all orbits 23 s) | — |

## What it says, and what it does not

The mechanism of §7.12 is stable across the free clocks: the same-shaped
element −(e₂e₃)(e₄e₅)… is the Weyl element that agrees with the half-turn on
the middle-band orbits, on B₄, B₈ and B₁₆ alike, and the number of such orbits
grows (1, 2, 16). The consequence — a shared grammar larger than the
centralizer — depends on that element commuting with the half-turn (SM-068),
and it does so only on B₄: on B₁₆, as on B₈, the correction has long cycles,
its Weyl centralizer is {±1}, and by Lemma B no extra survivor of the
half-turn preserves the agreement set. This stone does **not** decide |I₁₆|:
an element of I₁₆ that moves Y is not excluded by anything computed here
(on B₄ and B₈ there was none, but there I_m was enumerated). C₁₆ = {±1} is
exact.

## Not claimed

|I₁₆|; anything about B₃₂; a proof of the band or of the collapse; the
count 1, 2, 16 as a law. Nothing physical.

## Synthesis line

Scaling the board did not change the actors, only their number: the same
element plays the same part on sixteen stages instead of two, and still
declines to commute with the half-turn — the exception of the 4-cube looks
less like a small board's accident and more like the one time a growing
family's first member had too little room to fail.
