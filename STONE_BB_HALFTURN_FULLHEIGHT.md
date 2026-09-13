# STONE BB — THE HALF-TURN AND THE FULL-HEIGHT ORBIT

**Stenberg side · with Claude · 2026-09-13. Brief
`BRIEF_STONE_BB_HALFTURN_FULLHEIGHT.md` locked a5fab2bf… before the clean
verifier. Verifier `verify_stone_bb_halfturn_fullheight.py`: 6 PASS + 0 FAIL.
Closes SM-063 §7.12.4 open #1 — a proof, not a search. Registry row SM-066.
Merkabit-side mathematics. Not RH/GRH; Rule 3.**

## One paragraph

On the sixteen vertices of the 4-cube (the B₄ spinor board, W(B₄) = 𝔽₂⁴ ⋊ S₄
of order 384) the spinor clock R has order 8 and two free orbits O₁ ∋ λ and
O₂. Stone AY found, by a search, that the half-turn R⁴ is a Weyl element on
O₂ (equal to −τ there) and on no Weyl element on O₁, and left open *why* it is
the orbit without λ. The reason is a one-vector obstruction. Grade weights by
rank (number of minus signs). **Every Weyl element w = (π,v) shifts rank by
Δ_w(x) = wt(u) − 2|x∩u| with u = π⁻¹(v)** — a function of one vector u
(Lemma BB-A). The half-turn shifts every rank of O₁ by ±2 (O₁ is the unique
*full-height* orbit: it climbs 0→4 and wraps because rowmotion sends w₀λ
straight to λ); at λ this pins wt(u) = 2, and O₁'s spanning the cube then
forces an odd overlap ⟨x,u⟩ = 1 somewhere, collapsing the shift to 0 — a
contradiction. So no Weyl element agrees with R⁴ on O₁. On O₂ the shifts are
±1, realised by u = 1110, i.e. −τ. **λ is the cause**: the top weight pins
wt(u) at rank 0, and only an orbit avoiding the extremes can escape it.

## The theorem and its lemmas

- **Lemma BB-A (Weyl rank-shift) [P].** rank(w(x)) = wt(π(x)⊕v) = wt(x⊕u),
  u = π⁻¹(v); so Δ_w(x) = wt(u) − 2|x∩u|.
- **Theorem BB [P; ingredients C].** R⁴ agrees with no Weyl element on O₁ and
  with −τ = (e₂e₃)(−e₁,−e₂,−e₃) on O₂. (Proof in the brief: on O₁, |Δ_{R⁴}|≡2;
  λ ⇒ wt(u)=2; spanning ⇒ ⟨·,u⟩≡0 ⇒ u=0, contradiction.)
- **Lemma BB-B (general) [P].** If O ∋ λ = 0 spans 𝔽₂ⁿ and R^{h/2} shifts
  every rank by constant magnitude m ≥ 2, then R^{h/2}|O is not Weyl. The
  full-height orbit of B_n shifts by ±n/2, so the extreme-weight orbit's
  half-turn is non-Weyl for every n ≥ 4 (the n>4 input — that the shift is
  exactly ±n/2 — reduces to B₈).

## Bars

| bar | content | outcome |
|---|---|---|
| BB0 | brief locked (a5fab2bf…) | PASS |
| BB1 [C] | R⁴ shifts rank by ±2 on O₁, ±1 on O₂ | PASS |
| BB2 [C] | no u ∈ 𝔽₂⁴ reproduces O₁'s shift (⇒ not Weyl); u=1110 reproduces O₂ (⇒ −τ) | PASS |
| BB3 [C] | proof engine: λ ⇒ wt(u)=2; O₁ spans ⇒ odd overlap ⇒ contradiction | PASS |
| BB4 [C] | cross-check: affine linear part (2 3) ∈ S₄ on O₂; (2 3)∘transvection on {1,4} on O₁ | PASS |
| BB5 [obs] | O₁ the unique full-height orbit; rowmotion wraps w₀λ → λ | PASS |

## Not claimed

The ±n/2 rank-shift on the full-height orbit for n > 4 (reduces to B₈, m=4).
Nothing on boards without the clean two-free-orbit structure (needs n a power
of 2). BB4 (the transvection) is a cross-check; the proof is the rank-shift
contradiction alone. No physical identification.

## Synthesis line

The clock's half-turn can be one of the board's own symmetries only on an
orbit that keeps to the middle of the board; the one orbit that climbs to the
very top and bottom carries the highest weight, and the highest weight is
exactly what forbids the half-turn from being a symmetry there. The exception
of SM-063 is the height of the board made visible.
