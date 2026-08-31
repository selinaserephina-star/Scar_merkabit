# Our BRIDGE SPECIFICATION table — independent implementation (Stenberg → Balashov)

**2026-08-31. Compute, never assert; a verifier for every row. Not RH/GRH.**

Ilya —

Here is our side of the table, built independently so we can diff yours against
it — same rows, two engines, any difference is a finding. `verify_bridge_table.py`
(enclosed) produces all ten fields for both towers from group theory.

The one thing worth saying up front: **we let the `type` column derive itself.**
For each row a classifier reads four computed signals — is it a crossing (neither
embeds)? is the lower group a *normal* subgroup? is there a shared *normal*
subgroup? does the lower group occur as a *quotient*? — and outputs T1–T6. It
**reproduces your T1–T6 assignments 6/6, as a theorem of each row**, not a label
we chose. That satisfies your own rule — *no declaring a bridge type from one
example* — because now no one declares it at all; the row proves it.

**Tower A — the spine bridges:**

| bridge | left | right | type (derived) | common object [I] | shared | direction | reversibility | lost | appears |
|---|---|---|---|---|---|---|---|---|---|
| 7↔6 | PSL(2,7) | C₆×ℤ₂ | T6 quantum gap | 28 bitangents (SM-003) | 1,C₂,C₃,V₄ | cross | symmetric | A₄,C₄,C₇,D₄,S₃,S₄,F₂₁,PSL(2,7) | C₆,C₆×C₂ |
| 6↔5 | C₆×ℤ₂ | A₅ | T3 double hinge | A₅ + covers Ih/2I | 1,C₂,C₃,V₄ | cross | symmetric | C₆,C₆×C₂ | A₄,A₅,C₅,D₅,S₃ |
| 5↔4 | A₅ | S₄ | T2 single mediator (A₄) | tetrahedron in cube | 1,A₄,C₂,C₃,S₃,V₄ | cross | symmetric | A₅,C₅,D₅ | C₄,D₄,S₄ |
| 4↔3 | S₄ | A₄ | T1+T4 incl.+internal joint | cube's 2-fold axes (V₄) | 1,A₄,C₂,C₃,V₄ | A₄⊴S₄, quot S₄/A₄ | one-way (normal) | C₄,D₄,S₃,S₄ | — |
| 3↔2 | A₄ | ℤ₂ | T5 one-way door | V₄ as container | 1,C₂ | C₂↪A₄ (subgroup) | one-way (no quotient) | A₄,C₃,V₄ | — |
| 2↔1 | ℤ₂ | 1 | T1 inclusion | the point | 1 | 1⊴ℤ₂ | one-way (normal) | C₂ | — |

**Tower B — covers & bridges:** the SL(2,p) Schur-cover chain over the odd levels
(SL(2,7)→PSL(2,7), 2I=SL(2,5)→A₅, 2T=SL(2,3)→A₄, all non-split); the split covers
Ih=A₅×ℤ₂, Th=A₄×ℤ₂; S₄'s double cover GL(2,3)=2·S₄ (2O the sibling); the over-group
PGL(2,7) (distinct from the central cover); and the top bridge W(E₆) ⊂ Sp₆(2)=W(E₇)/±
closed by index 28.

Two honest refinements the table carries, at equal prominence:

1. **The crossing rows are two-sided.** 5↔4, 6↔5, 7↔6 are crossings — each *both*
   loses and gains subgroup types (columns 9–10), neither group embeds in the
   other. So T2 "single mediator" and T3 "double hinge" are real *shared mediators*
   (A₄; the two covers Ih/2I), but the joints are exchanges, not clean insertions.

2. **The common floor {1, C₂, C₃, V₄}** survives every upper bridge, and V₄ is the
   deepest piece to fall (lost only at 3↔2). Whatever else the table says, it says
   that.

The `common object` column is tagged **[I]** throughout — named or cited (the 28
bitangents point at our sealed SM-003/SM-015), and kept *out* of the graded
columns, per Rule 3.

Send yours when it's ready and we'll run the diff. If your row format differs,
send the format and I'll re-emit ours to match exactly.

— Selina (with Claude)

*Enclosures: `verify_bridge_table.py`, `verify_bridge_table.log`, `SHA256SUMS.txt`. Not RH/GRH.*
