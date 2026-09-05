# STONE AD — THE FORCED-NARROWING TABLE

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AD_FORCED_NARROWING.md` sha-locked 3c6cf23c… BEFORE code; no
amendment. Verifier `verify_stone_ad_forced_narrowing.py`, log: 8 PASS, 0
FAIL; 0.3 s; the SM-026 engine verbatim (lines 40–483 of
`verify_blind_engine.py`), no caches. Registry row SM-042.**

## 0. Discipline

Not RH/GRH. Rule 3: "narrowing", "compression", "lost" are IB's labels;
the mathematics is a table of counts and two inequalities. His transition
magnitudes enter only through his own decision rule and are tagged [I].

## 1. One paragraph

IB asked (PROMPT "Subgroup Diversity Along the Descent" + ADDENDUM "Forced
Narrowing as the Compression Mechanism", 2026-09-02, repeated 2026-09-03)
for the number of subgroups, conjugacy classes of subgroups, maximal
subgroups and normal subgroups at each spine level, and for his two
decision rules to be applied. The seven groups were rebuilt from raw
generators, every subgroup enumerated, and the table filled. Neither the
subgroup column nor the class column is monotone (subgroups rise from 10
to 59 at 6 → 5; classes rise from 9 to 11 at 5 → 4), so his diversity
rule is not met as stated. His forced-narrowing rule fails on both
clauses: the largest count difference (169, at 7 → 6) is not at his
largest magnitude (128, at 6 → 5), and the smallest difference is at
neither his smallest nor his reversing transition. The maximal and normal
columns are not monotone either. A caveat the addendum's formula hides: the
spine groups are not nested (C₆×C₂ has an element of order 6, PSL(2,7) has
none — computed), so "lost subgroups" is a difference of counts between
two unrelated groups, not a loss of anything.

## 2. The table (L6 = C₆×C₂ as his prompt instructs; other L6 labels not tested)

| level | group | order | #subgroups | #conj classes | #maximal | #normal | maximal classes |
|---|---|---:|---:|---:|---:|---:|---|
| 7 | PSL(2,7) | 168 | 179 | 15 | 22 | 2 | S₄ ×7, S₄ ×7, F₂₁ ×8 |
| 6 | C₆×C₂ | 12 | 10 | 10 | 4 | 10 | C₆ ×3 (one class each), C₂×C₂ ×1 |
| 5 | A₅ | 60 | 59 | 9 | 21 | 2 | A₄ ×5, D₁₀ ×6, S₃ ×10 |
| 4 | S₄ | 24 | 30 | 11 | 8 | 4 | A₄ ×1, D₈ ×3, S₃ ×4 |
| 3 | A₄ | 12 | 10 | 5 | 5 | 3 | C₂×C₂ ×1, C₃ ×4 |
| 2 | C₂ | 2 | 2 | 2 | 1 | 2 | {e} ×1 |
| 1 | {e} | 1 | 1 | 1 | 0 | 1 | — |

(The log prints the C₆×C₂ row as "C2xC2 x1, C6 x1" per class: the three
index-2 subgroups are three classes of one subgroup each in an abelian
group; the count of maximal subgroups is 4.)

## 3. His two rules, applied

**Diversity rule** (narrowing supported iff both #subgroups and #classes
decrease from level 7 to level 1): NOT SUPPORTED as stated — #subgroups
10 → 59 at 6 → 5; #classes 9 → 11 at 5 → 4.

**Forced-narrowing rule** (his formula, his magnitudes):

| transition | #subgroups(n) − #subgroups(n−1) | his magnitude [I] |
|---|---:|---:|
| 7 → 6 | 169 | 24 |
| 6 → 5 | −49 | 128 |
| 5 → 4 | 29 | 4 |
| 4 → 3 | 20 | −2 |
| 3 → 2 | 8 | 4 |
| 2 → 1 | 1 | 9 |

Clause 1 (largest loss at the largest compression): fails — 169 sits at
7 → 6, his 128 at 6 → 5, where the count goes UP by 49. Clause 2
(smallest loss at the smallest or reversing transition): fails — the
smallest difference is −49 at 6 → 5 (or, counting only decreases, 1 at
2 → 1), while his smallest magnitude is at 5 → 4 and his reversal at
4 → 3. By his own rule the mechanism is REFUTED, not "ambiguous".
[obs] Spearman rank correlation between the two columns: −0.32 (6 points;
recorded, no claim).

## 4. Bars

| bar | registered | outcome |
|---|---|---|
| AD1 | seven groups from raw generators; L6 = C₆×C₂ by explicit iso | PASS |
| AD1b | spine groups not nested (order-6 element) | PASS |
| AD2 | SM-026 census reproduced: 179/10/59/30/10/2/1; 15/10/9/11/5/2/1 | PASS |
| AD3 | maximal counts 22/4/21/8/5/1/0 with breakdown | PASS |
| AD4 | normal counts 2/10/2/4/3/2/1 | PASS |
| AD5a | his diversity rule: not monotone at 6→5 and 5→4 | PASS |
| AD5b | his forced-narrowing rule: both clauses fail | PASS |
| AD6 | maximal/normal monotonicity; Spearman — [obs] | recorded |

## 5. One finding on the brief itself (post-reveal, at full prominence)

The brief's AD5b parenthetical named "the smallest (1, at 2 → 1)" as the
smallest difference. With the 6 → 5 increase included the smallest
difference is −49 at 6 → 5. The registered claim (clause 2 fails) holds
under either reading; the parenthetical was wrong and is corrected here,
not in the brief.

## 6. Grades

[C] every count (AD1–AD4), every rule evaluation (AD5); [P] nothing new
(the maximal and normal subgroups of these groups are classical and are
here recomputed, not cited); [I] his transition magnitudes; [obs] AD6.

## 7. Not claimed

Nothing about any L6 label other than C₆×C₂ (his prompt's instruction).
Nothing about "compression" as geometry: the table is counts. No claim
that a different count (maximal, normal, classes) rescues the rule — the
columns are printed; none is monotone.

## 8. Synthesis line

The one place the count rises (10 → 59 at the C₆×C₂ → A₅ step) is the one
place the spine changes character from abelian to simple — the same seam
where SM-020's transfer table and SM-025's cover-dependent mediator both
broke; his "narrowing" fails exactly at the descent's own hinge.
