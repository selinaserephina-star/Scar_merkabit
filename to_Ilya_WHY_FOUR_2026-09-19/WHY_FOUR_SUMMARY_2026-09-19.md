# WHY FOUR — the 4-cube anomaly from question to theorem (SM-067 … SM-070)

**Selina Stenberg, with Claude · 2026-09-19.** Four stones, run in one day on
the Stenberg side, each under a brief locked before code, each with its
first-run log kept. This summary is the story they tell together; the four
stone summaries and verifiers are enclosed and say each part in full. Written
as §6.4 of the mathematics edition (Propositions 6.7–6.11, Lemma 6.9, Lemma
6.12, Proposition 6.13, Theorem 6.14 = Theorem G) and as §7.12.4 of the record
edition. Not RH/GRH; Rule 3 throughout.

## 0. Where we stood

SM-058 found the one exception in the simply-laced minuscule family to "the
grammar two instants share is the centralizer of the clock power between
them": the D₅ half-spin, located by SM-060 on the B₄ spinor board — the
sixteen vertices of the 4-cube, W = 𝔽₂⁴ ⋊ S₄, clock R of order 8 with two free
orbits O₁ ∋ λ and O₂ — where |I₄| = 8 against |C₄| = 4. SM-063 gave the
mechanism: R⁴ equals the Weyl element −τ = −(e₂e₃) (e₄ fixed) on all of O₂,
and Lemma B turns I₄ into the Weyl centralizer of the correction c = (−τ)R⁴.
SM-066 gave the reason the other orbit cannot carry it: O₁ is the
full-height orbit, and a Weyl element's rank-shift wt(u) − 2|x∩u| cannot be a
constant ±2 on a spanning orbit containing λ. Its last line was "B₈ next": the
spinor clock is free (orbits of size h = 2n) exactly when n is a power of 2,
so B₈ was the one decisive test of whether this is a fact about B₄ or a fact
about free clocks.

## 1. SM-067 (Stone BC): the 8-cube — the mechanism recurs, the consequence does not

B₈: 256 weights, |W| = 10,321,920, h = 16, sixteen free orbits of sixteen.
W was never materialised: elements are pairs (π, v) acting as x ↦ π(x) ⊕ v,
and membership of a transport R^{−k} g R^k in W is decided at 0 and the unit
vectors and confirmed on all 256 points (the engine reproduces SM-060's
materialised sets on B₄, B₅, D₅ exactly). Findings:

- The orbit of λ is full-height, its half-turn shift exactly ±4 — SM-066's
  input at n = 8, verified.
- **Exactly two orbits carry the half-turn as a Weyl element, both by the same
  element w = −(e₂e₃)(e₄e₅)(e₆e₇) with e₈ fixed — the shape of −τ
  continued.** w is the unique Weyl element nearest to R⁸ (agreement 52/256).
- **But I₈ = C₈ = {±1}, and I_k = C_k at every lag** — on B₈, on the D₉
  half-spin (W(D₉), 92,897,280 elements, enumerated in full), and on B₆, B₇.
  Lemma B holds; the correction c = w⁻¹R⁸ is simply not an involution (cycle
  type 8⁸4¹²3¹²2²⁸1⁵²) and only ±1 commutes with it.
- The conjecture "anomaly iff n a power of 2" is refuted at n = 8. Among
  B₃..B₈ the anomaly is B₄'s alone (B₃'s signature is its overgroup's).
- [obs] On B₄ and B₈ alike the carrying orbits are exactly those whose ranks
  stay within one of the middle rank.

14 PASS + 4 INVERTED (the recurrence itself, the swap of the carrying orbits
by −1, a D₉ survivor, the power-of-2 law). One record correction in passing:
R(λ) = w₀λ on our machine (the paper's own Lemma), so SM-066's rank list is
read in the direction of R⁻¹; nothing depends on it.

## 2. SM-068 (Stone BD): the criterion — why, in one sentence

*The shared grammar at the half-turn exceeds the centralizer exactly when the
Weyl element nearest to the half-turn commutes with it.* Verified on
B₃..B₈ (6/6). Behind it two lemmas, proved and checked:

- **BD-A.** For w ∈ W and c = w⁻¹R^m (m = h/2): c² = 1 iff R^m w R^m = w⁻¹;
  for an involution w this says w ∈ C_W(R^m).
- **BD-B.** If w ∈ C_W(R^m) then w, c, R^m pairwise commute, any two of
  "g commutes with w / R^m / c" imply the third, and (Lemma B) the extras of
  I_m on Stab_W(Fix c) are exactly C_W(c) ∖ C_W(w) — SM-063's "commute with c
  but not with τ" as a lemma.

On B₄, −τ commutes with R⁴. On B₅..B₈ the nearest element (always of the
shape −(e₂e₃)(e₄e₅)…) does not, its correction has long cycles, and
C_W(c) = {±1}. Inverted guesses: the stabilizer of the B₈ agreement set is
⟨−1, w⟩, not {±1}; within W(B₃) no element has a spanning agreement set at
all (so B₃ stays the overgroup's case and the criterion is only a marker
there); the nearest element is unique outright. 7 PASS + 3 INVERTED.

## 3. SM-069 (Stone BE): the 16-cube at the orbit level

B₁₆: 65,536 weights, |W| ≈ 1.4 × 10¹⁸ (not enumerable; |I₁₆| not claimed).
Rowmotion computed combinatorially on the shifted staircase δ₁₆ and validated
against the sealed B₄/B₈ clocks; carrying orbits by matching columns of the
difference vectors; stabilizer and centralizers by backtracking with every
solution verified on all 65,536 points (searches cross-checked against the
B₈ enumerations). Findings: free clock, 2,048 orbits of 32; O₁ full-height
with shift ±8; **sixteen carrying orbits — not two — all by the same
−(e₂e₃)…(e₁₄e₁₅), e₁₆ fixed, and exactly the rank band {7,8,9}** (the band on
a third board; 1, 2, 16 carrying orbits on B₄, B₈, B₁₆); w does not commute
with R¹⁶; C_W(R¹⁶) = {±1}; Stab_W(Fix c) = ⟨−1, w⟩; C_W(c) = {±1}; hence by
Lemma B no half-turn survivor beyond ±1 preserves the 1,900-point agreement
set. 9 PASS + 2 INVERTED (the count; 61 non-spanning orbits).

## 4. SM-070 (Stone BF): why four — the theorem

**Theorem.** For even n ≥ 4, w_n = −(e₂e₃)(e₄e₅)…(e_{n−2}e_{n−1}) commutes with
the half-turn Rⁿ if and only if n = 4.

Proof in four steps, each re-checked on the actual clocks up to n = 16:

1. **Rowmotion in excess coordinates.** Write a weight by its plus positions
   c₁ < … < c_r and put d_k = c_k − k. Rowmotion is
   d′_{k′} = min({d_k − 1 : k a gap row ≥ k′} ∪ {n − r − 1 if d_r < n − r}),
   a gap row being one with d_k > d_{k−1}. (Checked on every weight, n ≤ 12.)
2. **The orbit of λ in closed form, for all n:** R^{2j}λ = [n] ∖ {n, n−2, …,
   n−2j+2}, R^{2j+1}λ = [n] ∖ {n−1, …, n−2j+1}; ranks 0, n, n−1, n−1, …, 1, 1.
   **So the half-turn shifts every rank on the full-height orbit by exactly
   ±n/2 for every even n** — SM-066's remaining input is now a theorem.
3. **Where commutation is forced.** w_n preserves the orbit of λ, acting on
   clock positions as i ↦ 2 − i (even) and i ↦ −i (odd), both commuting with
   i ↦ i + n; on a carrying orbit commutation is automatic (wHx = x = Hwx).
   **At n = 4 these two orbits are the whole board** — that is why −τ
   commutes with R⁴.
4. **The witness for n ≥ 6.** e₂ (one minus sign, at position 2) lies on
   neither kind of orbit. Two half-turn values in closed form, by induction
   along their orbits in excess coordinates: Rⁿ(e₂) = {1, 2} ∪ {5, 7, …, n−1}
   and Rⁿ({3, n}) = [n] ∖ {4, 6, 7, 9, …, n−1} (at n = 6: {1,2,3,5,6}). Since
   w_n(e₂) = −{3, n} and Rⁿ commutes with −1: 2 ∈ w_n(Rⁿe₂) but
   2 ∉ Rⁿ(w_n e₂). ∎

8 PASS + 0 FAIL; found by free exploration (kept, enclosed, cited as
unsealed), proofs completed before the brief was locked.

## 5. What is closed, what is open

Closed: SM-066's "B₈ next"; SM-063's "why the 4-cube" (mechanism + criterion +
theorem); SM-066's ±n/2 input for all even n. Open, stated as such: that w_n
is the *nearest* Weyl element for n > 8 (computed at n ≤ 8; on B₁₆ it is the
carrying element); C_W(Rⁿ) = {±1} for n ≥ 5 in general (computed at 6, 7, 8,
16); |I₁₆|; the closed form of Rⁿ(e_p) (an observation to n = 16).

## 6. Numbers, exact

| board | |W| | orbits | carrying orbits (element) | |C_{h/2}| | |I_{h/2}| |
|---|---|---|---|---|---|
| B₄ | 384 | 8² | 1, by −τ = −(e₂e₃), e₄ fixed | 4 | **8** |
| B₆ | 46,080 | 12⁵4¹ | — (nearest −(e₂e₃)(e₄e₅), e₆ fixed, 24/64) | 2 | 2 |
| B₇ | 645,120 | 14⁹2¹ | — | 2 | 2 |
| B₈ | 10,321,920 | 16¹⁶ | 2, by −(e₂e₃)(e₄e₅)(e₆e₇), e₈ fixed | 2 | 2 |
| D₉ half-spin | 92,897,280 | 16¹⁶ | (same clock) | 2 | 2 |
| B₁₆ | ≈ 1.4 × 10¹⁸ | 32²⁰⁴⁸ | 16, by −(e₂e₃)…(e₁₄e₁₅), e₁₆ fixed | 2 (exact) | ∩ Stab(Fix c) = 2; total not claimed |

Non-commuting points of w_n with Rⁿ: 0, 24, 148, 736, 3304, 14328, 60076 for
n = 4, 6, …, 16.
