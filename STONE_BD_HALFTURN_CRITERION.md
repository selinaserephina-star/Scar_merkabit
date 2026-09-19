# STONE BD — THE HALF-TURN CRITERION: WHY THE 4-CUBE, IN ONE SENTENCE

**Stenberg side · with Claude · 2026-09-19. Brief
`BRIEF_STONE_BD_HALFTURN_CRITERION.md` locked 0dbad52f… before code (BD0
re-checks it). Verifier `verify_stone_bd_halfturn_criterion.py`: 7 PASS +
3 INVERTED (BD2, BD3, BD5b); first run 6 + 3 kept in `_FIRSTRUN.log` (the
clean run adds the labelled post-reveal check BD3b). Registry row SM-068.
Merkabit-side mathematics. Not RH/GRH; Rule 3.**

## The sentence

*The shared grammar at the half-turn exceeds the centralizer exactly when the
Weyl element nearest to the half-turn commutes with it.* Verified on the six
enumerable spinor boards B₃..B₈ (BD5): true on B₃ and B₄, false on B₅, B₆, B₇,
B₈. Behind it, two lemmas proved in the brief and checked as computations
(BD6): for w ∈ W and the correction c = w⁻¹R^m (m = h/2), **BD-A:** c is an
involution iff R^m w R^m = w⁻¹, which for an involution w says exactly
w ∈ C_W(R^m); **BD-B:** if w commutes with R^m then w, c, R^m pairwise
commute, any two of "g commutes with w / with R^m / with c" imply the third,
and with Lemma B (SM-063) the extras of I_m inside Stab_W(Fix c) are exactly
C_W(c) ∖ C_W(w). On B₄ that is SM-063's "commute with c but not with τ"
(BD1, all identities exact). On B₈ the carrying element w =
−(e₂e₃)(e₄e₅)(e₆e₇) is an involution that does not commute with R⁸, so c is
not an involution (BD-A) and C_W(c) = {±1} = C₈ (BD2a): the 8-cube's collapse
is the sentence's negative case. On B₅, B₆, B₇ the same negative case (BD4).

## Guesses vs outcomes

| bar | registered guess | outcome |
|---|---|---|
| BD1 | B₄, w = −τ: w ∈ C₄, c² = 1, |Stab_W(O₂)| = 16, I₄ ⊆ Stab, I₄ = C_W(c) = 8, extras = C_W(c) ∖ C_W(w) | **PASS** (all exact) |
| BD2a | B₈: w ∉ C₈ ⇒ c² ≠ 1, C_W(c) = {±1} = C₈ = I₈, Lemma B holds | **PASS** |
| BD2 | B₈: Stab_W(Fix c) = {±1} | **INVERTED** — Stab_W(Y) has order 4: it is ⟨−1, w⟩, the carrying element itself preserves its 52-point agreement set; w and −w commute with neither c nor R⁸ and are not in I₈ |
| BD3 | B₃ inside W(B₃): a nearest w with spanning agreement set, Lemma B, w ∈ C₃, extras = C_W(c) ∖ C_W(w) | **INVERTED** — the four nearest elements agree with R³ on 4 of 8 points forming a 2-flat; **no element of W(B₃) has a spanning agreement set at all** (BD3b), so Lemma B never applies within W(B₃); the B₃ anomaly is the overgroup's (R³ ∈ W(D₄), SM-060) and the sentence does not reach it |
| BD4 | B₅, B₆, B₇: no nearest w commutes with R^m; C_W(c) ⊆ C_m; Lemma B where spanning | **PASS** (B₆'s nearest spans and Lemma B holds; B₅'s and B₇'s nearest do not span) |
| BD5 | the criterion on B₃..B₈ | **PASS** 6/6 — with the caveat that on B₃ it is a marker only (BD3) |
| BD5b | nearest unique up to the antipode ({w, −w}) | **INVERTED** — nearest is unique outright on B₄..B₈ (−w is farther), four-fold on B₃ |
| BD6 | BD-A, BD-B as computations on every nearest and carrying w | **PASS** (9 elements, all involutions) |

## The numbers (exact integers; no model band)

| board | h | |C_m| | |I_m| | nearest w to R^m (agreement) | w ∈ C_m | c² = 1 | c type | |C_W(c)| | |Stab_W(Y)| | Y spans |
|---|---|---|---|---|---|---|---|---|---|---|
| B₃ | 6 | 8 | 16 | four, each 4/8 (e.g. −e₁−e₃) | yes | yes | 2²1⁴ | 8 | 8 | no (2-flat) |
| B₄ | 8 | 4 | 8 | −τ = −(e₂e₃), e₄ fixed: 8/16 | yes | yes | 2⁴1⁸ | 8 | 16 | yes |
| B₅ | 10 | 2 | 2 | −(e₂e₃), e₁,e₄,e₅ negated: 10/32 | no | no | 5²4²2²1¹⁰ | 2 | 12 | no (dim 4) |
| B₆ | 12 | 2 | 2 | −(e₂e₃)(e₄e₅), e₆ fixed: 24/64 | no | no | 3⁸2⁸1²⁴ | 2 | 4 | yes |
| B₇ | 14 | 2 | 2 | −(e₂e₃)(e₄e₅), e₁,e₆,e₇ negated: 22/128 | no | no | 10⁴8²5⁴4²3²2⁸1²² | 2 | 4 | no (dim 6) |
| B₈ | 16 | 2 | 2 | −(e₂e₃)(e₄e₅)(e₆e₇), e₈ fixed: 52/256 | no | no | 8⁸4¹²3¹²2²⁸1⁵² | 2 | 4 | yes |

Spanning survey over *all* Weyl elements (BD3b, post-reveal): the number of
w whose agreement set with R^m affinely spans is 0 on B₃, 1 on B₄ (−τ), 0 on
B₅, 9 on B₆, 6 on B₇ (B₈ not surveyed: 10.3M elements). Wall time 43 s.

## What it says

The 4-cube anomaly is the conjunction of two facts, one structural and one
arithmetical. Structural (Lemma B): a Weyl element agreeing with the half-turn
on a spanning set turns the shared grammar into the centralizer of a
correction. Arithmetical (BD-A): that correction is an involution exactly when
the Weyl element commutes with the half-turn — and then (BD-B) the extras are
the Weyl elements commuting with the correction but not with w. On B₄ the
nearest element −τ commutes with R⁴; on every larger enumerable spinor board
the nearest element, always of the same shape −(e₂e₃)(e₄e₅)…, does not, its
correction has long cycles, and only ±1 commutes with it. A proof that the
nearest element never commutes with the half-turn for n > 4 is not in hand;
that is the open question this stone leaves, sharpened from "why B₄" to "why
does −(e₂e₃)(e₄e₅)… stop commuting with R^{h/2} after n = 4".

## Not claimed

Nothing beyond B₃..B₈; no theorem that C_W(c) collapses whenever w ∉ C_m
(five negative instances, no proof); nothing at lags other than the half-turn
(SM-063's D₅ lag-3 survivor is outside BD-A's hypothesis R^{−k} = R^k); no
paper edit yet — the criterion is written into §6.4 (v2.0) and §7.12.4 (v1.0)
together with Stone BE's result, one rebuild. Nothing physical.

## Synthesis line

The exception was a commutation: the one board where the nearest symmetry to
the half-turn also commutes with it — the same shape of element on every
board, obedient only on the smallest — which is the familiar way small cases
break a pattern: not by a different mechanism but by an extra coincidence the
mechanism does not need.
