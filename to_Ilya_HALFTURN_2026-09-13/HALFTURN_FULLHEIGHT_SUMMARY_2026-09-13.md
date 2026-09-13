# SUMMARY — the half-turn on the full-height orbit (SM-066), as §7.12.4

**Stenberg side · with Claude · 2026-09-13. Written as §7.12.4 of
`joint_paper/Roof_and_Clock_DRAFT.md` (v0.6), replacing that section's former
open line; Stone AY's remaining open items move to §7.12.5. Three-tier shape:
classical cited, computed graded, read marked. Source: Stone BB
(`STONE_BB_HALFTURN_FULLHEIGHT.md`, brief locked a5fab2bf… before the clean
verifier; 6 PASS + 0 FAIL). Not RH/GRH. Rule 3.**

#### 7.12.4 Why the orbit without λ [P + C, SM-066]

The question left open in §7.12.4 of Stone AY — *why* the half-turn is a Weyl
element on the orbit not containing the highest weight λ — has a proof, not a
search. Grade the spinor weights by rank (number of minus signs); W(B₄) =
𝔽₂⁴ ⋊ S₄ acts affinely, w(x) = π(x) ⊕ v with π a coordinate permutation and v
the sign-flips.

**Lemma (Weyl rank-shift) [P].** For w = (π,v), writing u := π⁻¹(v),
> rank(w(x)) = wt(π(x) ⊕ v) = wt(π(x ⊕ π⁻¹v)) = wt(x ⊕ u),
since a coordinate permutation preserves Hamming weight. Hence the rank-shift
Δ_w(x) := rank(w(x)) − rank(x) = **wt(u) − 2·|x∩u|** is a function of x through
the single vector u alone.

**Theorem [P; ingredients C, SM-066].** R⁴ agrees with no Weyl element on O₁
(the orbit of λ) and with −τ = (e₂e₃)(−e₁,−e₂,−e₃) on O₂.

*Proof.* On O₁ the half-turn shifts every rank by exactly ±2: the full-height
orbit reads 0,1,1,2,2,3,3,4 around the clock (rowmotion sends the bottom
weight w₀λ straight back to the top λ), and R⁴ pairs clock-positions j and
j+4, whose ranks differ by 2. Suppose R⁴|O₁ = w|O₁ for a Weyl w = (π,v); then
Δ_w(x) = ±2 for all x ∈ O₁. At x = λ = 0, which R⁴ moves up to rank 2,
Δ_w(0) = wt(u) = +2, so wt(u) = 2. Then Δ_w(x) = 2 − 2|x∩u| ∈ {2,0,−2}, and
|Δ_w(x)| = 2 forces |x∩u| ≠ 1, i.e. ⟨x,u⟩ = 0 for every x ∈ O₁. But O₁
contains 0 = λ and affinely spans 𝔽₂⁴, hence spans it linearly; a linear
functional vanishing on a spanning set is zero, so u = 0 — contradicting
wt(u) = 2. On O₂ the shifts are ±1; u = 1110 gives Δ(x) = 3 − 2|x∩u| ∈ {1,−1}
for all x ∈ O₂, realised by −τ, which (O₂ spanning) is the unique such Weyl
element. ∎

**The cause is λ.** The top weight, at rank 0, pins wt(u) = 2; the orbit's
spanning the whole cube then forces an odd overlap somewhere, collapsing the
shift to 0. "The orbit not containing λ" is exactly the orbit whose half-turn
can be a Weyl element, because it never forces wt(u) at rank 0.

**General B_n (n even).** Lemma above is dimension-free
(Δ_w(x) = wt(u) − 2|x∩u| in every W(B_n)). Hence: *if an orbit contains λ = 0,
spans 𝔽₂ⁿ, and R^{h/2} shifts every rank by constant magnitude m ≥ 2, then
R^{h/2} on it is not a Weyl element* (at λ, wt(u) = m; some spanning x has
|x∩u| = 1, giving shift m−2 ∉ {±m}). On the full-height orbit of B_n the
half-turn shifts rank by ±n/2, so for every n ≥ 4 the extreme-weight orbit's
half-turn is not a Weyl element. The sole n-specific input for n > 4 is that
the shift is exactly ±n/2 on the full-height orbit; the clean two-free-orbit
dichotomy is realised at B₄ and next at B₈ (m = 4, |W(B₈)| ≈ 10⁷).

**Cross-check [C].** Equivalently, R⁴|O extends to an affine map of the
4-cube whose linear part is the coordinate transposition (2 3) on O₂ (a Weyl
element, = −τ) and (2 3) composed with the transvection x ↦ x ⊕ (x₁+x₄)(e₂+e₃)
on O₁ — not a coordinate permutation, the transvection localised to the {1,4}
directions of the {14|23} pairing. This is a consistency check; the proof is
the rank-shift contradiction above and uses no linear algebra beyond one
functional's vanishing on a spanning set.

**Read [I].** The exception SM-063 found is not a crack in the family's rule
but the height of the board made visible: the clock's half-turn can be one of
the board's own symmetries only on an orbit that keeps to the middle, and the
one orbit that reaches the very top and bottom is the one carrying the highest
weight — which is exactly what forbids it there.
