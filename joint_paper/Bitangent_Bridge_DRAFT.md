---
title: "The Bitangent Bridge"
subtitle: "PSL(2,7), W(E₆), and the 28 bitangents of the Klein quartic: where two computational frameworks meet — DRAFT v0.1"
author: "Selina Stenberg · Ilya Balashov · with Claude (Anthropic Fable 5)"
date: "2026-08-30 — draft v0.1, sealed-not-sent"
---

**Status.** Joint draft, v0.1 written on the Stenberg side; awaiting Ilya's
review pass (his corrections, additions, and the jointly completed
bibliography) before anything circulates. Every computational claim is reproduced by the scripts listed in
Appendix A (plain Python 3 + numpy, no GAP, no lookup tables). Claims are
graded: **[P]** proved here or classical with citation, **[C]** computed
exactly by a named script, **[obs]** observation we have not located in the
literature (possibly folklore — flagged for expert readers). No physical
identification is asserted anywhere in this note.

## Abstract

Two independently developed frameworks — a ternary computational architecture
on the E₆ minuscule crystal (the 27), and a representation-theoretic
framework on PSL(2,7) (the 168) — each underwent a full adversarial audit in
2026. This note records where the surviving mathematical cores of the two
frameworks actually meet. The meeting point is not E₆: PSL(2,7) embeds in no
E₆-Weyl or 27-line structure (7 ∤ 51840), and admits no transitive action on
27 objects. It is E₇: inside Sp₆(𝔽₂) ≅ W(E₇)/{±1}, realized as the symmetry
group of the 28 bitangents of a genus-3 curve — the Klein quartic being the
curve whose automorphism group is PSL(2,7) — the Weyl group W(E₆) is the
stabilizer of a single bitangent, PSL(2,7) acts transitively on all 28, and
the intersection is a single S₃ = N(⟨z₃⟩): precisely the "universal
stabilizer" of the PSL(2,7) framework and the canonical stabilizer of the
strata decomposition 168 = 31+62+75 verified in the E₆-side audit. We record
the resulting double cover (the 56 elements of class 3A map 2-to-1 onto the
bitangents, matching the 56 of E₇), the orbit structure of PSL(2,7) on the
even theta characteristics ([1,7,7,21]), two explicit branchings of the
27-dimensional representation to PSL(2,7) (3χ₁ ⊕ 3χ₈ and 6χ₁ ⊕ 3χ₇), the
field-level shadow (ℚ(ζ₂₁) as the compositum of the two frameworks'
character fields, linearly disjoint), and a machine-level corollary: the
E₆ architecture's 7-channel error syndrome admits exactly two Fano plane
structures compatible with its own symmetry — a chiral pair — hence is
"one bit away" from Fano organization, never forced.

## 1. Background: two programs and their audits

*(one paragraph per program: the crystal architecture — 27 states, rowmotion
clock of order 12, CSP census, two ternary gates generating A₂₇, magic
monotone μ, T-depth 2; the Scar-Cat registry — PSL(2,7) representation ring,
Hom-count selection rules, GAP-verified core independently reconfirmed. Both
audits published/recorded separately; this note uses only their VERIFIED
layers.)*

## 2. Preliminaries [P]/[C]

PSL(2,7) ≅ GL(3,𝔽₂), order 168, classes 1A,2A,3A,4A,7A,7B of sizes
1,21,56,42,24,24; character table (derived from scratch by Burnside–Dixon
and verified exactly over ℚ(√−7) in `verify_tsc_scarcat.py`):

| | 1A | 2A | 3A | 4A | 7A | 7B |
|---|---|---|---|---|---|---|
| χ₁ | 1 | 1 | 1 | 1 | 1 | 1 |
| χ₃ | 3 | −1 | 0 | 1 | α | ᾱ |
| χ̄₃ | 3 | −1 | 0 | 1 | ᾱ | α |
| χ₆ | 6 | 2 | 0 | 0 | −1 | −1 |
| χ₇ | 7 | −1 | 1 | −1 | 0 | 0 |
| χ₈ | 8 | 0 | −1 | 0 | 1 | 1 |

with α = (−1+√−7)/2. On the E₆ side we use the minuscule crystal B(ϖ₁)
(27 vertices, W(E₆) of order 51840 = 2⁷·3⁴·5 on the weights / 27 lines), and
the E₇ minuscule 56. Classical background: the 28 bitangents of a smooth
plane quartic, odd/even theta characteristics on H₁(X,𝔽₂) ≅ 𝔽₂⁶,
Sp₆(𝔽₂) ≅ W(E₇)/{±1}, O₆⁻(2) ≅ W(E₆), O₆⁺(2) ≅ S₈ [P: standard; refs to be
inserted — Dolgachev, Gross–Harris, Elkies' Klein-quartic survey].

## 3. The no-go at E₆ [P]/[C]

7 ∤ |W(E₆)|, so PSL(2,7) embeds in no structure whose automorphism group is
W(E₆) — in particular not in the 27-line incidence geometry. Moreover 27
divides no subgroup index of PSL(2,7) reachable at that size (168/27 ∉ ℤ):
PSL(2,7) has no transitive action on 27 objects. Any meeting of the two
frameworks at the level of the 27 itself is therefore impossible; this
sharpens the second author's own registry entry S-15.

## 4. The field-level shadow [C]

Gal(ℚ(ζ₂₁)/ℚ) ≅ C₆ × C₂ (order 12), with quadratic subfields ℚ(√−3),
ℚ(√−7), ℚ(√21) (Gauss sums g₃² = −3, g₇² = −7, (g₃g₇)² = +21). ℚ(√−7) is
the character field of PSL(2,7) (the unique irrationality in the table
above; the Klein quartic has CM by ℚ(√−7)); ℚ(√−3) = ℚ(ω) is the Eisenstein
field underlying the ternary/E₆ side. The compositum contains both, linearly
disjointly: **at field level the two frameworks meet only in ℚ.** This is
the arithmetic preview of Theorem 5.3's "small intersection".

## 5. The bitangent home [C, skeleton P]

Realize PSL(2,7) = GL(3,𝔽₂) on V ⊕ V* ≅ 𝔽₂⁶ with the symplectic form
ω((v,f),(w,h)) = f(w)+h(v). The 64 quadratic refinements of ω split into 36
even + 28 odd (Arf invariant / zero-counts 36 vs 28). Then, all computed in
`verify_tbr_bridge.py`:

**5.1** PSL(2,7) fixes exactly one even refinement, q₀(v,f) = f(v); its
orbits on the 36 even refinements are **[1, 7, 7, 21]** — the fixed form,
the Fano points, the Fano planes, the flags **[obs]**. The stabilizer of an
even form in the full Sp₆(2) has order 1451520/36 = 40320 = 8!
(O₆⁺(2) ≅ S₈): the 8-point action of PSL(2,7) on P¹(𝔽₇) is its action
inside the stabilizer of its own invariant even theta characteristic.

**5.2** PSL(2,7) is transitive on the 28 odd refinements (the bitangents),
with stabilizer S₃ = N(⟨z₃⟩); the permutation character is
χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈. The stabilizer of an odd form in the full Sp₆(2) has
order 1451520/28 = 51840 = |W(E₆)| (O₆⁻(2) ≅ W(E₆)).

**5.3 (the bridge).** Inside Sp₆(2) ≅ W(E₇)/{±1}: W(E₆) is the stabilizer
of one bitangent; PSL(2,7) is transitive on all 28; and
PSL(2,7) ∩ Stab(bitangent) = S₃ = N(⟨z₃⟩). This S₃ is simultaneously (i)
the "universal stabilizer" of the Scar-Cat registry (28 = 168/6), (ii) the
canonical stabilizer of the strata decomposition 168 = 31+62+75 (audit
thread T4), and (iii) the type-group S₃ of the E₆ architecture's typed
algebra (1 → K → H → S₃ → 1).

**5.4 (the 56).** The map z ↦ N(⟨z⟩) is exactly 2-to-1 from the 56 elements
of class 3A onto the 28 bitangent stabilizers [C] — the group-internal
incarnation of the classical ±-doubling by which the 28 bitangents index
the 56 weights of the E₇ minuscule representation. On the crystal side the
56-vertex E₇ minuscule crystal carries the corresponding dynamics
(rowmotion of order 18; the antipode ι as the fixed-point-free pair
involution [C]).

## 6. Branchings of the 27 [C, embeddings P]

Via trinification E₆ ⊃ SU(3)³ (27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)) with
PSL(2,7) embedded diagonally by Klein's χ₃: each block restricts to
χ₃⊗χ̄₃ = χ₁ ⊕ χ₈, hence **27| = 3χ₁ ⊕ 3χ₈**. Via
PSL(2,7) ⊂ G₂ = Aut(𝕆) (7 = χ₇) and 27 = J₃(𝕆): **27| = 6χ₁ ⊕ 3χ₇**.
These are the two canonical "functors" from the E₆ world to the PSL(2,7)
world; the previously conjectured "27 ↔ 2χ₈" is impossible (dimension 16
appears in no restriction of the 27).

## 7. A machine-level corollary: the chiral Fano pair [C]

The E₆ architecture's error syndrome has 7 channels — the affine E₆ Dynkin
nodes (6 colours + 1 promotion-built affine channel). Computed in
`verify_fano_syndrome.py`: the syndrome's motion group (promotion
conjugation + Lusztig involution; rowmotion does not act) is S₃ (order 6,
not 168); the channels' non-commutation graph is the affine E₆ tree; of the
30 Fano plane structures on 7 labels, **exactly 2** are invariant under the
motion group — sharing the three "centre lines" {centre, leg} and exchanged
by the unique inner↔outer duality of the diagram. The syndrome is therefore
*not* Fano-organized, but is precisely **one bit** (a chirality convention)
away from a full Fano labelling — compatible, never forced **[obs]**.

## 7½. The resurrection theorem [C]

The first framework's original design intuition (its v1 paper) pictured two
counter-posed 27s exchanged by an involution around a small pivot — a picture
the E₆-side audit *refuted* as a description of the E₆ crystal (the two-27s
theorem: the product 27 and the crystal 27 are provably different objects).
Computed in `verify_dq6_resurrection.py` (12 exact checks): on the E₇
minuscule 56, deleting the seventh colour splits the crystal as
**27 ⊕ 27̄ ⊕ 1 ⊕ 1** (each 27-component a full E₆-crystal candidate, 36
coloured edges); the odd diagram gate pr (cycle type 1²·2²⁷) fixes *exactly*
the two singlets and its 27 transpositions pair the sheets bijectively; the
antipode ι gives a second, inequivalent sheet-duality (the two pairings share
3 of 27 pairs); and rowmotion runs across the wall (the dynamics is genuinely
E₇). **The refuted intuition is true one floor up**: it describes the
E₆-branching of the 56, not the 27 itself. As a corollary of the same
computation, both structural gates are *bilingual*: pr and ι have distance 0
to the branching-preserving subgroup **and** to the frame-preserving
subgroup, while rowmotion alone carries all the magic in both grammars
(μ_branch(Ψ) = 21/56, μ_frame(Ψ) = 27/56, exact assignment computation).
An interactive instrument realizing all of this ("The 56-State Machine") is
published alongside this note.

## 8. What is new and what is not

The skeleton of §5 — bitangents, theta characteristics, O₆± ≅ W(E₆)/S₈,
Sp₆(2) ≅ W(E₇)/± — is classical. A precursor **within the Stenberg corpus**
deserves record: Paper 8 §4.2 (2026, pre-audit) already stated the 36+28
theta-characteristic split on the Klein quartic, the transitivity of
PSL(2,7) on the 28 odd characteristics with S₃ stabilizer, and that the
even characteristics split into "multiple orbits" — the germ of §5,
perceived before the audit era. What is new here relative to that
precursor: the stabilizer-of-one-bitangent identified as W(E₆) (replacing
the cardinality reading 28 = dim D₄), the exact even-orbit structure
[1,7,7,21], the 2:1 map from class 3A, the S₃ identified with both
programs' canonical S₃, and the whole assembled as the meeting of the two
frameworks. The contribution of this note is (a) the
identification: two independently built frameworks each singled out, for
internal reasons, an object (the universal-stabilizer S₃; the strata S₃ and
typed S₃) that turns out to be the *same* subgroup at the same place in
this classical geometry — the frameworks are the two point-of-view subgroups
of the bitangent configuration; (b) the computed observations flagged [obs]
(the even-orbit structure [1,7,7,21] in this normalization; the resurrection
theorem of §7½ with its bilingual-gates corollary; the chiral Fano
pair on the affine-E₆ syndrome); (c) the audit-grade reproducibility: every
claim is a passing check in a short script a reader can run in seconds.

## 9. Outlook

The natural joint object is the E₇ minuscule 56 — the first structure
carrying both frameworks natively (design brief: `56_MACHINE_BRIEF.md`;
open questions DQ-1..5 there, including the PSL(2,7) orbit structure on the
56 weights and the 8-channel affine-E₇ syndrome vs the P¹(𝔽₇) action).

## Appendix A — reproducibility

`verify_tsc_scarcat.py` (48 checks: character table derivation + registry
audit), `verify_tbr_bridge.py` (20 checks: §§3–6), `verify_fano_syndrome.py`
(14 checks: §7), plus the E₆/E₇ crystal verifiers in `Merkabit_crystal/`.
Python 3 + numpy only.

*(Bibliography to be completed jointly: Klein 1878; Hecke 1928; Elkies 1999;
Dolgachev; Gross–Harris; Lubotzky–Phillips–Sarnak 1988; Cohen–Wales for
PSL(2,7) ⊂ G₂; standard crystal/rowmotion references.)*
