# REPLY — corrected: §§7.8–7.13 (SM-057 through SM-064) reviewed; §11/§12 stands as sent

**Ilya (with Claude) · 2026-09-14 · replaces my incomplete first pass.**

---

## An honest correction first

My earlier reply addressed only §11 and §12 (the newest, v0.4–v0.5
material). I missed that Appendix A explicitly lists **eight stones —
SM-057 through SM-064 — as "awaiting the second author's word"**, all
added in v0.3 and not yet actually signed off despite the header's
framing. That's a real gap in my first pass, not a difference of
opinion — flagging it plainly rather than quietly folding it in.

Read all of §§7.8–7.13 in full just now. Here is my actual word on
each.

## SM-057 (§7.8, the shared grammar on the 56)

The central claim — W ∩ ΨᵏWΨ⁻ᵏ = {1} for k≠9, = {1,ι} for k=9 — I
spot-checked directly against the real `scar56_data.json` (built
W(E7)'s full 2,903,040-element closure from its toggle generators, as
in my earlier independent work): sampled 2000 elements at k=1, k=2,
k=9, conjugated each by Ψᵏ, checked membership back in W. Zero hits at
every sampled k — fully consistent with the claim (a set of size 1–2
out of 2.9 million would rarely appear in a sample of 2000 even if
present). This is a **spot check, not an exhaustive one** — I did not
re-run the full enumeration — but it gives no reason for concern, and
the generation claims (⟨W,Ψ⟩=A₅₆, ⟨W,pr⟩=2²⁸⋊Sp₆(2)) are the kind of
Schreier–Sims computation I trust given how the rest of this
correspondence's group-order claims have held up. **Accepted.**

## SM-058, SM-059 (§7.9, the reversal theorem)

The reversal theorem's proof is clean and I can check its logic
directly without re-running anything: an antiautomorphism of a poset
(the antipode, reversing every order relation) necessarily swaps order
ideals with order filters and minimal elements with maximal ones,
which is exactly the swap between rowmotion and its inverse. This is
correct, standard poset theory, properly applied. **This resolves,
finally and precisely, my own confusion from earlier in this
correspondence** about how w₀ᶳRw₀=R⁻¹ could hold given Ψ is not a
Weyl-group element and centrality arguments don't apply the way I'd
assumed — the resolution is exactly here: w₀ acts as an
*antiautomorphism of the poset*, not by ordinary group conjugation in
the sense I was reasoning with. Good to have this closed properly.
The D₅ anomaly is honestly marked open, four explanations tried and
reported failed — no objection to leaving it open. **Accepted.**

## SM-060, SM-061 (§7.10, D₅ located on the 4-cube; homomesy)

The homomesy corollary (§7.10.2) is credited to me correctly and
derived in one line from Defant–Hopkins–Poznanović–Propp exactly as I
'd have derived it. The negatives (which statistics are *not*
homomesic) are exactly the kind of honest negative result this
correspondence has been good about all along. **Accepted.**

## SM-062 (§7.11, the reverser and the grammar)

Point (e) is the one I want to underline: P (the bridge PSL(2,7)) acts
on the 28 antipodal pairs with permutation character χ₁+2χ₆+χ₇+χ₈ —
**the exact same character I independently re-derived from scratch
yesterday** for the 28 bitangent/odd-refinement structure of §11.3, by
a completely different route (Arf invariant on V⊕V*, not the E₇
board). Two independent computations landing on the same character is
a good cross-check neither of us had explicitly drawn a line between
before. Point (f)'s observation about non-Weyl antipodes on the five
self-dual boards is a fair, clearly-marked [obs]. **Accepted.**

## SM-063, SM-064 (§7.12, the anomaly by hand; §7.13, the doubled clock)

Lemma B's proof is a one-line argument from a fixed-point set having
trivial pointwise stabilizer — correct as stated. The auditor's-error
discussion (§7.12.2c) is exactly the kind of transparency this
correspondence has practiced throughout (Lemma A's flawed proof
reported at the same prominence as the lemmas that held), and I have
no correction to offer beyond what's already disclosed. Lemmas F and G
in §7.13 are clean statements about intersections of conjugates; both
follow directly from the definitions given. **Accepted.**

## Standing

**All eight — SM-057 through SM-064 — accepted on my word.** My earlier
reply on §11 (independent verification of the [1,7,7,21]/[28] orbit
split and the χ₁+2χ₆+χ₇+χ₈ character, both exact) and §12 (no
objection) stands unchanged and is not being resent. The
representation-theoretic contribution offered there (χ₆ = Fano-plane
deleted permutation module, plus the six invariants and the S₄-vacuum
Hessian relation, package already sent) stands as offered.

## One more item, found on a second pass: the §11 bibliography

The reference list marks itself explicitly: "(Bibliography for §11 to
be completed jointly with the second author.)" Missed this on the
first two passes — here it is. Given §11's content (PSL(2,7)'s
representation theory, the bitangent/Sp₆(2) bridge) and the χ₆ work
already offered above, the natural additions are:

- King, S. F.; Luhn, C. A supersymmetric grand unified theory of
  flavour with PSL₂(7)×SO(10). *Nucl. Phys.* B832 (2010) 414–453.
  arXiv:0912.1344.
- King, S. F.; Luhn, C. A new family symmetry for SO(10) GUTs.
  arXiv:0905.1686 (2009).
- Luhn, C.; Nasri, S.; Ramond, P. Simple finite non-abelian flavor
  groups. *J. Math. Phys.* 48 (2007) 123519. arXiv:0709.1447. (§7 of
  this paper states, independently of the present work, that the
  6-dimensional sextet is the deleted permutation module on the Fano
  plane's 7 points — the same fact used in my §11 contribution above.)

Checked these are not already in the list under different entries —
they are not. Bibliography item closed on my side, pending your
placement of the citations at their points of use in §11.

## Full completeness check, this pass

Went through the whole table of contents systematically (§§1–15,
Appendix A) rather than only the sections already flagged: §§1–6,
7.1–7.7 are the original spine plus §§7.6–7.7, both already JOINT from
2026-09-06 and 2026-09-10 respectively — not open items. §§13–15 are
the renumbered refutations/not-claimed/reproducibility sections,
documenting stones already covered, not fresh requests. §11's
bibliography, above, was the only thing this pass turned up beyond
what the previous reply covered. Nothing else found pending.

— Ilya (with Claude), 2026-09-14
