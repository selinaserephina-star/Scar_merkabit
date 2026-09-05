# BRIEF — STONE AD: THE FORCED-NARROWING TABLE

**Staged 2026-09-05 on Selina's "prepare the response package for him first
and foremost … 4" (the two small verifiers owed). Locked before code
(`BRIEF_STONE_AD_LOCK.sha256`). Answers IB's PROMPT "Subgroup Diversity
Along the Descent" and its ADDENDUM "Forced Narrowing as the Compression
Mechanism" (filed `RECEIVED_2026-09-02_IB_AUDIT_AND_BETA/`), repeated in
his RESPONSE of 2026-09-03 ("run maximal and normal subgroup counts as
already requested"). Deviations = dated AMENDMENT; post-reveal changes are
findings.**

## Question

His table, level by level on the SPINE (L7..L1 = PSL(2,7), C₆×C₂, A₅, S₄,
A₄, C₂, {e}; L6 = C₆×C₂ as his prompt instructs, alternatives NOT tested):

```text
level | |G| | #subgroups | #conj classes | #maximal | #normal
```

and then his two decision rules, applied mechanically to the computed
numbers. Nothing is asserted; the SM-026 census (subgroups 179/10/59/30/
10/2/1, classes 15/10/9/11/5/2/1) is recomputed, not copied.

## Definitions (declared)

- #subgroups: all subgroups, enumerated by the SM-026 engine (BFS over
  cyclic generators, complete), including {e} and G.
- #conj classes: G-conjugacy classes of subgroups (including the two
  trivial classes).
- #maximal: proper subgroups contained in no other proper subgroup
  (counted as subgroups, with the class breakdown by iso type reported).
- #normal: subgroups whose conjugacy class has one element, double-checked
  by direct conjugation.
- "lost subgroups" at n → n−1 = #subgroups(n) − #subgroups(n−1), exactly
  his formula. The spine groups are NOT nested as subgroups (C₆×C₂ has an
  element of order 6; PSL(2,7) has none — computed), so the difference is a
  count difference, not a loss of anything; stated, not softened.
- His "transition magnitudes" 24 / 128 / 4 / −2 / 4 / 9 are taken as
  given, tagged [I] (physics-side provenance, per the read-as-corrected
  line of v0.58); they enter only through his own decision rule.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AD1 (the seven groups from raw generators, verbatim SM-026 engine):**
  orders 168 / 12 / 60 / 24 / 12 / 2 / 1; the order-12 abelian input
  identified as C₆×C₂ by explicit isomorphism.
- **AD2 (SM-026 census reproduced — registered):** #subgroups 179 / 10 /
  59 / 30 / 10 / 2 / 1 and #conj classes 15 / 10 / 9 / 11 / 5 / 2 / 1.
- **AD3 (maximal counts — registered expectation, classical):** 22 / 4 /
  21 / 8 / 5 / 1 / 0, with class breakdown PSL(2,7): S₄×7, S₄×7, F₂₁×8;
  C₆×C₂: C₆×3, C₂×C₂×1; A₅: A₄×5, D₁₀×6, S₃×10; S₄: A₄×1, D₈×3, S₃×4;
  A₄: C₂×C₂×1, C₃×4; C₂: {e}×1; {e}: none.
- **AD4 (normal counts — registered expectation, classical):** 2 / 10 / 2 /
  4 / 3 / 2 / 1.
- **AD5a (his diversity rule — registered):** the subgroup count is NOT
  monotone (10 → 59 at 6 → 5) and the class count is NOT monotone (9 → 11
  at 5 → 4): by his own rule "narrowing" is NOT SUPPORTED as stated.
- **AD5b (his forced-narrowing rule — registered):** the count differences
  per transition (7→6 … 2→1) are 169 / −49 / 29 / 20 / 8 / 1; the largest
  (169, at 7→6) does not sit at his largest magnitude (128, at 6→5); the
  smallest (1, at 2→1) sits at neither his smallest (4) nor his reversing
  (4→3) transition: by his own rule the mechanism is REFUTED (not
  "ambiguous": both clauses fail).
- **AD6 ([obs] only):** monotonicity of the maximal and normal columns,
  recorded; the rank correlation (Spearman, exact on 6 points) between
  count difference and his magnitude, recorded — no claim.

## Machinery

Permutation-group class, subgroup enumeration, conjugacy classes,
normality test, explicit-isomorphism identifier and the seven raw
generator sets — VERBATIM from `verify_blind_engine.py` (SM-026). Pure
Python, no caches. Outputs: `verify_stone_ad_forced_narrowing.py`, `.log`,
`STONE_AD_FORCED_NARROWING.md`. Runtime: seconds.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "narrowing", "compression", "lost" are
labels; the mathematics is a table of counts and two inequalities.
