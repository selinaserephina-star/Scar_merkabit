# REPLY — the bridge-transfer table, computed (Stenberg → Balashov)

**2026-08-31. Compute, never assert; refutations at equal prominence, including
our own. Not RH/GRH; the wall untouched.**

Ilya —

We filled your BRIDGE SPECIFICATION "required output table" — from group theory
only, no physical or network labels attached. For the SPINE-MAP spine

    PSL(2,7) → C₆×ℤ₂ → A₅ → S₄ → A₄ → ℤ₂ → {e}

we machine-enumerated every subgroup **up to isomorphism type** at each level
(each group's full ≤2-generated subgroup lattice), then read off, per bridge,
which types **survive** (shared), are **lost** (upper-only), and **appear**
(lower-only). Reproducer: `verify_bridge_transfer.py`.

| bridge | upper → lower | survives | lost | appears | structure |
|---|---|---|---|---|---|
| 7↔6 | PSL(2,7) → C₆×ℤ₂ | 1, C₂, C₃, V₄ | A₄, C₄, C₇, D₄, S₃, S₄, F₂₁, PSL(2,7) | C₆, C₆×C₂ | crossing |
| 6↔5 | C₆×ℤ₂ → A₅ | 1, C₂, C₃, V₄ | C₆, C₆×C₂ | A₄, A₅, C₅, D₅, S₃ | crossing |
| 5↔4 | A₅ → S₄ | 1, A₄, C₂, C₃, S₃, V₄ | A₅, C₅, D₅ | C₄, D₄, S₄ | crossing |
| 4↔3 | S₄ → A₄ | 1, A₄, C₂, C₃, V₄ | C₄, D₄, S₃, S₄ | — | lower ⊆ upper |
| 3↔2 | A₄ → ℤ₂ | 1, C₂ | A₄, C₃, V₄ | — | lower ⊆ upper |
| 2↔1 | ℤ₂ → {e} | 1 | C₂ | — | lower ⊆ upper |

**What it shows — and where it revises the spec, at equal prominence:**

1. **Two regimes, only the bottom one is a true descent.** The bottom three
   bridges (4↔3, 3↔2, 2↔1) are genuine *inclusions*: the lower group's subgroup
   types are a strict subset of the upper's, nothing appears. The top three
   (7↔6, 6↔5, 5↔4) are *crossings* — each both loses and gains types, and
   neither group embeds in the other. So the T-typology holds cleanly only at
   the bottom; **"5↔4 single mediator" and "6↔5 double hinge" are two-sided
   exchanges that share a mediator (A₄ at 5↔4), not simple joints.**

2. **The invariant is V₄.** It survives every bridge from the top down to 4↔3
   and is lost only at 3↔2. The universal shared floor of the upper bridges is
   exactly **{1, C₂, C₃, V₄}**. If the descent carries anything, it carries V₄.

3. **The 7↔6 "quantum gap," made exact.** It is *not* "no common subgroup" —
   PSL(2,7) and C₆×ℤ₂ share the whole floor {1, C₂, C₃, V₄}. The precise
   statement is: **neither embeds in the other, and no order-6 type bridges
   them** (PSL(2,7) has no C₆).

4. **The level labels still collide, and here is the sharp instance.** With
   your SPINE-MAP choice **L6 = C₆×ℤ₂** (abelian), **S₃ is LOST at 7↔6**. But
   your 7↔6 BRIDGE file uses **L6 = W(E₆)** and reports the intersection *is*
   S₃ = N(⟨z₃⟩). Same "level 6," opposite fate for S₃ — the two files cannot
   both be the spine. **This is the one thing to settle before any of it
   seals:** is level 6 the small abelian C₆×ℤ₂, or W(E₆)? Pick one and the
   whole table is unambiguous; keep both and "the spine" is really two towers
   (a spine of groups and a parallel tower of covers) that got merged.

One methodological note we'd hold ourselves to as well: this table is about
*subgroups*. Your "3↔2 one-way door" is a *quotient* fact (A₄ has no ℤ₂
quotient); as a subgroup, ℤ₂ ⊆ A₄. Subgroup-descent and quotient-descent are
different maps — worth tabulating separately if the MONARCH/GUARDIAN step is
to run on the right one.

Settle L6 and we'll seal the transfer table as a joint row; it already stands
computed on our side (SM-020).

— Selina (with Claude)

*Reproducer `verify_bridge_transfer.py` available on request. Not RH/GRH.*
