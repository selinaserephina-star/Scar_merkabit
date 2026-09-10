# Literature Addendum — Novelty Assessment for the First-Paper Spine (2026-09-08)

**Auditor:** Claude (Sonnet 5), independent session
**Subject:** resolves the two open literature items flagged in the companion audits (`AUDIT_paper_spine_checkpoint_2026-09-08.md`, `AUDIT_paper_spine_part2_2026-09-08.md`) and expands the Rush–Shi priority finding into a full scope assessment before any arXiv/OSF submission.
**Status:** gates the publication decision. Nothing here touches the computational verification, which stands as reported in the two companion audits.

---

## 1. Purpose

The two prior audits confirmed that all 12 units of the proposed spine reproduce computationally. This document addresses a separate question: **how much of what the spine claims is actually new**, since a paper that presents known results as findings will lose on novelty at review regardless of how well it is computed. Three items were left open:

1. The scope of the Rush–Shi (2013) priority issue — is it confined to one line, or does it run through the corpus?
2. A second, targeted literature search for SM-041's parity rule.
3. A literature check for SM-053's mirror-as-diagram-automorphism claim.

## 2. Finding 1 — Rush–Shi (2013): scope is corpus-wide, not one paragraph

**The base fact.** D. Rush and X. Shi, *"On Orbits of Order Ideals of Minuscule Posets"* (J. Algebraic Combin., 2013) prove that rowmotion on any ADE-type minuscule poset has order equal to the Coxeter number of the associated Weyl group, with an accompanying cyclic sieving phenomenon. This applies directly and by name to the exceptional-type minuscule posets for E₇ and E₈ — i.e., exactly the 56-element board used throughout SM-039/040/041.

**This is not confined to SM-041.** A search of the correspondence's own language shows the "clock ticks at the Coxeter number" framing recurring as a narrative device across multiple stones and multiple registry entries, not as a single citable claim in one place:

- SM-035 (the G₂ 7-crystal): *"the still-point clock EXCEEDS the Coxeter number"* — here the underlying poset is a degenerate 6-element chain, and the verifier's own honest caveat already concedes the base fact is elementary. This instance is handled correctly and needs no change.
- SM-039 (the roof clock): *"the E₈ Coxeter image ... × turn = 18 — the E₇ clock number one floor up"* — presented as a measurement, not flagged as a known theorem.
- Registry synthesis lines (v0.47, v0.53, v0.57, v0.58, v0.73 and others): *"the turn returns the old rhythm one floor up (rhymes with SM-005, SM-035)"*; *"SM-035's seven-beat clock and SM-039's turn are one exact object with one exact class"* — these treat the Coxeter-number coincidence itself as the discovery, when the coincidence for the 56-board case is exactly what Rush–Shi already proved.

**Consequence for drafting.** This is not a one-line citation fix. Whoever drafts the paper needs to read every passage that invokes "the clock's order = the Coxeter number" as its point of interest and either (a) cite Rush–Shi at first use and reframe the passage around what actually is new (the specific identification of Ψ with rowmotion on this poset, or the parity mechanism), or (b) cut the passage if it adds nothing beyond restating Rush–Shi. A single citation added to SM-041 alone will not fix the SM-035/039 passages or the registry-derived synthesis lines, if those end up quoted or paraphrased into the manuscript.

## 3. Finding 2 — SM-041's parity rule: two targeted searches, no match found

Two searches were run, deliberately narrowed by area rather than by keyword-matching the corpus's own vocabulary:

1. **General toggle-group / rowmotion literature** (Cameron–Fon-der-Flaass 1995; Striker–Williams 2012; Striker's generalized toggle groups, 2016; interval-closed-set rowmotion, 2023–2025). This field studies periodicity, homomesy (average-preservation of a statistic over an orbit), cyclic sieving, and the abstract group structure of the toggle group (symmetric vs. alternating). None of it addresses a per-pair preservation criterion of the kind SM-041 defines.
2. **A more specific search** for rowmotion interactions with an ambient inner-product sign or pairwise-type structure on minuscule weights — again no match.

**SM-041's actual object:** a criterion, exact with zero exceptions on all 1,485 non-antipodal pairs of the 56-element board, stating that a pair of states keeps its "pair type" (the sign of an ambient E₇ inner product) under one application of Ψ if and only if a specific sum — (toggled colours of one state active at the other) + (the same reversed) + (Dynkin-diagram adjacencies between the two toggle sets) — is even. This is a genuinely specific combinatorial mechanism, and it is not addressed by the standard toggle-group vocabulary (periodicity, homomesy, CSP), which asks different kinds of questions (statistics over whole orbits, not pairwise relations between two arbitrary states).

**Caveat, stated plainly:** this is two searches by one non-specialist reviewer, not a formal literature review. It raises reasonable confidence that the parity rule is original but does not settle the question. Before submission, this specific mechanism should be checked by someone who can search MathSciNet/zbMATH directly and who knows the area's internal vocabulary well enough to recognize a disguised restatement if one exists.

## 4. Finding 3 — SM-053's mirror: classical, not new

The claim that the "mirror" operator pr realizes the E₆ Dynkin diagram automorphism (swapping nodes 1 and 6, i.e., swapping the two dual 27-dimensional minuscule representations) and acts as an order-isomorphism between the corresponding minuscule posets is **classical on both halves of the claim**:

- The E₆ diagram automorphism itself, and the fact that it swaps the two minuscule 27's, is standard Lie theory (Bourbaki).
- That such a diagram automorphism induces an isomorphism between the corresponding minuscule posets/crystals — "up to diagram automorphisms" — is stated explicitly in the minuscule-representation literature, e.g. **"Branching rules of minuscule representations via a new partial order"** (arXiv:2402.06732): minuscule representations "differ only by the corresponding automorphism," and are recoverable from their posets "up to diagram automorphisms of 𝔤 in all cases." Crystal-theoretic treatments of E₆ diagram automorphisms (e.g. work on E₆ affine crystal structures) make the same point at the level of crystal graphs.

So, like SM-047–052's census, SM-053's underlying structural fact is not new. What is a genuine (if narrow) contribution is the identification exercise: showing that the specific operator "pr," built independently inside this project's own 56-board machinery via other means, *is* this classical automorphism, and verifying it computationally (SM-053's AO1–AO6, all reproduced in the part-2 audit).

## 5. Consolidated novelty map for the spine

| Unit | Underlying fact | Status |
|---|---|---|
| SM-030 (roof) | W⁺(E₈) contains both towers | Classical ingredients (Conway–Sloane, ATLAS); explicit construction is a computational contribution |
| SM-038 (still point) | Fixed point of triality on O₈⁺(2) is G₂(2) | Classical (Conway; Kleidman 1987) |
| SM-039/040 (turn, board) | Rowmotion order = Coxeter number on the 56-board | **Classical — Rush–Shi 2013 — needs citing, corpus-wide (Finding 1)** |
| SM-041 (parity rule) | The specific pairwise parity mechanism | **No match found after two targeted searches — best candidate for genuine novelty** |
| SM-047–051 (census) | 14 classes of the twisted coset | Classical (part of O₈⁺(2).3's known character table) |
| SM-052 (ATLAS names) | Matching to published GAP CTblLib data | Correctly and explicitly cited already |
| SM-053 (mirror) | pr = E₆ diagram automorphism, order-isomorphism | **Classical — minuscule-representation / crystal literature (Finding 3)** |

## 6. Recommendation before publication

1. **Do not submit with the current framing.** The corpus-wide "the clock ticks at the Coxeter number" narrative (Finding 1) needs an editorial pass across every passage that uses it as a point of interest, not a single citation added in one place.
2. **Cite on first use, throughout:** Rush–Shi (2013) for the rowmotion/Coxeter-number fact; Conway (1971/1999) and the ATLAS for the group-theoretic roof and still-point material; Breuer's GAP CTblLib (already correctly cited in SM-052); the minuscule-representation/crystal literature (e.g. arXiv:2402.06732 or an equivalent standard reference) for SM-053's diagram automorphism.
3. **Reframe the contribution honestly:** the paper's real claim is (a) an independently verified, cross-validated computational model of a large and mostly classical piece of exceptional group theory, plus (b) one specific new mechanism, SM-041's parity rule, plus (c) the identification work connecting the project's own constructed objects to the classical classification. That is a legitimate and publishable shape for the paper — but it is a different shape from "we discovered X, Y, Z," and reviewers will notice the difference either way.
4. **Before treating SM-041 as settled novel:** have someone with direct MathSciNet/zbMATH access and closer familiarity with the dynamical-algebraic-combinatorics literature run a proper check — two web searches by a non-specialist is supporting evidence, not a clearance.

## 7. What remains outstanding

- The corpus-wide editorial pass described in §6.1 — not yet done, and it is a drafting task, not a verification task, so it falls outside the scope of these audits.
- A specialist-level confirmation of SM-041's novelty (§3, §6.4).
- Everything else in the spine (computational integrity, the census, the roof, the still point) is settled per the two companion audits and does not need revisiting.
