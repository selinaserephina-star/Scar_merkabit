# BRIEF — STONE BB: THE HALF-TURN AND THE FULL-HEIGHT ORBIT

**Staged 2026-09-13 on Selina's "attempt the formal lemma" (SM-063 §7.12.4,
open #1). Locked before the clean verifier (`BRIEF_STONE_BB_LOCK.sha256`).
HONEST PROVENANCE: the theorem below was *found this session by exploration*
(scratch scripts); this brief records the completed proof, and the clean
verifier `verify_stone_bb_halfturn_fullheight.py` re-checks its computational
ingredients. There are NO registered predictions — this is a theorem, not a
guess-run — so the lock certifies the proof text and the verifier, not the
outcome of an unknown search. Builds on the sealed clock of SM-063 (Stone AY,
its H3 orbit sequences) and the reduction of SM-060 (the 4-cube as the B₄
spinor board under W(B₄)). Merkabit-side mathematics. Registry row SM-066.**

## Question

SM-063 §7.12.4 left open, as its first item: **why the orbit not containing
the highest weight λ is the one on which the half-turn is a Weyl element — a
proof, not a computation.** Stone AY established it by a search (−τ is the
nearest Weyl element and agrees with R⁴ on exactly O₂). This stone replaces
the search with a proof.

## Setup [P, classical + SM-063]

The B₄ spinor is minuscule; its sixteen weights (±½)⁴ are the vertices of the
4-cube, read as 𝔽₂⁴ (bit i = 1 iff coordinate i is negative). Its Weyl group
is W(B₄) = 𝔽₂⁴ ⋊ S₄, the hyperoctahedral group, acting **affinely**:
w(x) = π(x) ⊕ v, π a coordinate permutation (S₄), v ∈ 𝔽₂⁴ the sign-flips
(order 2⁴·4! = 384). The spinor rowmotion R has order 8 with two free orbits
O₁ ∋ λ = 0000 (and w₀λ = 1111) and O₂; the half-turn is R⁴. Grade each weight
by its **rank** = number of minus signs = Hamming weight (λ = rank 0, w₀λ =
rank 4). The two orbit sequences are SM-063's H3 (verbatim).

## Lemma BB-A (the Weyl rank-shift) [P]

For every Weyl element w = (π, v) ∈ W(B₄), writing **u := π⁻¹(v)**,
> rank(w(x)) = wt(π(x) ⊕ v) = wt(π(x ⊕ π⁻¹v)) = wt(x ⊕ u),
since a coordinate permutation preserves Hamming weight. Hence the rank-shift
> **Δ_w(x) := rank(w(x)) − rank(x) = wt(x⊕u) − wt(x) = wt(u) − 2·|x∩u|**,
where |x∩u| is the size of the common support. *A Weyl element's rank-shift
is a function of x through the single vector u alone.* ∎

## Theorem BB (the answer) [P; ingredients C]

**R⁴ agrees with no Weyl element on O₁, and agrees with −τ =
(e₂e₃)(−e₁,−e₂,−e₃) on O₂.**

*Proof.* On O₁ the half-turn shifts **every** rank by exactly ±2: the
full-height sequence reads 0,1,1,2,2,3,3,4 around the clock, and R⁴ pairs
clock-positions j and j+4, whose ranks differ by exactly 2 (0↔2, 1↔3, 1↔3,
2↔4). Suppose R⁴|O₁ = w|O₁ for a Weyl w = (π,v); then Δ_w(x) = ±2 for all
x ∈ O₁. Evaluate at the highest weight x = λ = 0, which R⁴ moves *up* to rank
2: Δ_w(0) = wt(u) = +2, so **wt(u) = 2**. Then Δ_w(x) = 2 − 2|x∩u| ∈ {2,0,−2},
and |Δ_w(x)| = 2 forces |x∩u| ≠ 1, i.e. **⟨x,u⟩ = 0** (even overlap with the
two-element support of u) for every x ∈ O₁. But O₁ contains 0 = λ and
affinely spans 𝔽₂⁴, hence spans it linearly; a linear functional ⟨·,u⟩
vanishing on a spanning set is identically zero, forcing u = 0 — contradicting
wt(u) = 2. So no Weyl element agrees with R⁴ on O₁.

On O₂ the half-turn shifts every rank by ±1; take u = 1110 (wt 3): then
Δ(x) = 3 − 2|x∩u| ∈ {1,−1} for all x ∈ O₂ (its overlaps with u are 1 or 2),
and the Weyl element with this u and the matching translation is −τ, which
therefore agrees with R⁴ on all of O₂ (and, O₂ spanning, is the unique such
Weyl element). ∎

**The cause is λ.** The top weight, at rank 0, pins wt(u) = 2; the orbit's
spanning the whole cube then forces an odd overlap somewhere, collapsing the
shift to 0. "The orbit not containing λ" is exactly the orbit whose half-turn
*can* be a Weyl element, because it never forces wt(u) at rank 0.

## Lemma BB-B (the general statement) [P]

Lemma BB-A is dimension-free. Hence: **if an orbit O contains λ = 0, spans
𝔽₂ⁿ, and R^{h/2} shifts every rank by a constant magnitude m ≥ 2, then
R^{h/2}|O is not a Weyl element of W(B_n).** (At λ, wt(u) = m; then some
spanning x has |x∩u| = 1, giving shift m − 2 ∉ {±m} for m ≥ 2 — contradiction.)
On the full-height orbit of B_n the half-turn shifts rank by ±n/2, so for
every n ≥ 4 the extreme-weight orbit's half-turn is not a Weyl element. The
sole n-specific input for n > 4 is that R^{h/2} shifts rank by exactly ±n/2 on
the full-height orbit; the clean two-orbit dichotomy is realised at B₄ and
next at B₈ (m = 4).

## Bars (the verifier re-checks these; no guesses, all confirmations)

- **BB0** — brief locked (`BRIEF_STONE_BB_LOCK.sha256`).
- **BB1 [C]** — R⁴'s rank-shift is ±2 on all of O₁ and ±1 on all of O₂.
- **BB2 [C]** — over all 16 candidate u ∈ 𝔽₂⁴, *none* reproduces
  wt(u)−2|x∩u| = Δ_{R⁴}(x) on O₁ (⇒ Theorem BB: not Weyl), while exactly
  u = 1110 reproduces it on O₂ (⇒ −τ).
- **BB3 [C]** — the proof engine: R⁴ sends λ up by 2 (⇒ wt(u)=2 forced); and
  every weight-2 u meets some O₁ vector in odd overlap (⇒ the contradiction).
- **BB4 [C, cross-check]** — consistency with the affine picture: R⁴|O
  extends affinely; the linear part is the coordinate transposition (2 3) on
  O₂ (Weyl, = −τ) and (2 3) composed with the transvection x ↦ x⊕(x₁+x₄)(e₂+e₃)
  on O₁ (not a coordinate permutation), the transvection localised to the
  {1,4} directions of the {14|23} pairing.
- **BB5 [obs]** — the distinguisher: O₁ is the unique orbit spanning the full
  rank range 0…4 (rowmotion sends w₀λ straight to λ); O₂ stays in the middle.

## Not claimed

The ±n/2 rank-shift on the full-height orbit for n > 4 is stated, not proved
here (it reduces to the B₈ computation, m = 4). Nothing about boards without
the clean two-free-orbit structure (which needs 2n | 2ⁿ, i.e. n a power of 2).
The affine/transvection description (BB4) is a cross-check, not the proof; the
proof is the rank-shift contradiction (Theorem BB), which needs no linear
algebra beyond one functional's vanishing on a spanning set. No RH/GRH; Rule 3
("clock", "half-turn" are labels). No physical identification.

## Files

`verify_stone_bb_halfturn_fullheight.py` (checks the brief hash first, then
BB1–BB5), `.log`, `STONE_BB_HALFTURN_FULLHEIGHT.md`.
