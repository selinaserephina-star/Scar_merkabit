# REPLY — SM-057 through SM-066, all ten, consolidated in one place

**Ilya (with Claude) · 2026-09-14 · consolidates two earlier separate
replies (the §§7.8–7.13 review, and the SM-066 note) into one, plus
the §11 bibliography, at your ask to gather 057–066 together.**

---

## SM-057 (§7.8, the shared grammar on the 56)

The central claim — W ∩ ΨᵏWΨ⁻ᵏ = {1} for k≠9, = {1,ι} for k=9 — spot-
checked directly against the real `scar56_data.json` (built W(E7)'s
full 2,903,040-element closure from its toggle generators): sampled
2000 elements at k=1, k=2, k=9, conjugated each by Ψᵏ, checked
membership back in W. Zero hits at every sampled k — fully consistent
with the claim. A **spot check, not exhaustive**, but no reason for
concern; the generation claims (⟨W,Ψ⟩=A₅₆, ⟨W,pr⟩=2²⁸⋊Sp₆(2)) match the
kind of Schreier–Sims computation this correspondence's group-order
claims have consistently held up under. **Accepted.**

## SM-058, SM-059 (§7.9, the reversal theorem)

The reversal theorem's proof is clean, checked directly by logic: an
antiautomorphism of a poset (the antipode, reversing every order
relation) necessarily swaps order ideals with order filters and
minimal elements with maximal ones — exactly the swap between
rowmotion and its inverse. Correct, standard poset theory, properly
applied. **This resolves, finally and precisely, my own earlier
confusion** about how w₀Rw₀=R⁻¹ could hold given Ψ is not a Weyl-group
element — w₀ acts as an antiautomorphism of the poset, not by ordinary
group conjugation. The D₅ anomaly is honestly marked open, four
explanations tried and reported failed — no objection to leaving it
open. **Accepted.**

## SM-060, SM-061 (§7.10, D₅ on the 4-cube; homomesy)

The homomesy corollary is credited to me correctly and derived in one
line from Defant–Hopkins–Poznanović–Propp exactly as I'd have derived
it. The negatives (which statistics are *not* homomesic) are honest
negative results in the same spirit as the rest of this
correspondence. **Accepted.**

## SM-062 (§7.11, the reverser and the grammar)

Point (e): P (the bridge PSL(2,7)) acts on the 28 antipodal pairs with
permutation character χ₁+2χ₆+χ₇+χ₈ — the exact same character I
independently re-derived for the 28 bitangent/odd-refinement structure
of §11.3, by a completely different route (Arf invariant on V⊕V*, not
the E₇ board). Two independent computations landing on the same
character — a good cross-check, now also directly explained by §2
below (it's the same Fano plane both times, not merely the same
character by coincidence). Point (f)'s observation about non-Weyl
antipodes on the five self-dual boards is a fair, clearly-marked
[obs]. **Accepted.**

## SM-063 (§7.12, the anomaly by hand)

Lemma B's proof is a one-line argument from a fixed-point set having
trivial pointwise stabilizer — correct as stated. The auditor's-error
discussion (§7.12.2c) is the same transparency this correspondence has
practiced throughout (Lemma A's flawed proof reported at the same
prominence as the lemmas that held). No correction to offer beyond
what's already disclosed. **Accepted.**

## SM-064 (§7.13, the doubled clock)

Lemmas F and G are clean statements about intersections of conjugates;
both follow directly from the definitions given. **Accepted.**

## SM-065 (§7.13, continued — Stone BA)

Covered in substance under SM-064 above but naming it explicitly, in
case my previous pass left this ambiguous: **accepted.**

## SM-066 (Stone BB — the half-turn on the full-height orbit)

Checksums verified (outer zip, inner SHA256SUMS.txt, and the brief
lock a5fab2bf… against the brief file — all match). Rebuilt Lemma
BB-A from scratch (a fresh implementation, not your verifier): W(B₄)
as 𝔽₂⁴⋊S₄, order 384 confirmed, rank(w(x))=wt(x⊕u) with u=π⁻¹(v)
checked on 200 random (π,v,x) triples — holds exactly.

Worked through the contradiction's geometric content directly: for a
weight-2 u, the even-overlap set is exactly the affine hyperplane
{x : x₃=x₄} (for u=0011) — a proper 3-dimensional subspace, never the
whole cube. Any 8-point orbit genuinely spanning 𝔽₂⁴ (not confined to
a hyperplane) cannot avoid odd overlap with any weight-2 u — the
"O₁ spans ⇒ contradiction" step, made concrete. Clean mathematics;
the honest-provenance note (found by exploration, no pre-registered
guess) matches what the proof looks like from outside. **Accepted.**

## Standing

**All ten — SM-057 through SM-066 — accepted on my word, explicitly,
gathered here in one place.**

## One more item, carried over: the §11 bibliography

Still open from the earlier pass — the reference list marks itself:
"(Bibliography for §11 to be completed jointly with the second
author.)" Given §11's content and the χ₆/Fano work (now §11.9), the
natural additions:

- King, S. F.; Luhn, C. A supersymmetric grand unified theory of
  flavour with PSL₂(7)×SO(10). *Nucl. Phys.* B832 (2010) 414–453.
  arXiv:0912.1344.
- King, S. F.; Luhn, C. A new family symmetry for SO(10) GUTs.
  arXiv:0905.1686 (2009).
- Luhn, C.; Nasri, S.; Ramond, P. Simple finite non-abelian flavor
  groups. *J. Math. Phys.* 48 (2007) 123519. arXiv:0709.1447.

Checked: not already in the list under different entries. Closed on
my side, pending placement of the citations at their points of use.

— Ilya (with Claude), 2026-09-14
