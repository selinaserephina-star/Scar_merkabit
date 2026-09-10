# Audit Checkpoint — First-Paper Spine Verification (2026-09-08)

**Auditor:** Claude (Sonnet 5), independent session
**Subject:** independent reproduction + literature check of the roof (SM-030) and the core (SM-038–041) of Selina's proposed spine for the first joint paper (roof, still point, turn, board, parity rule, census, mirror — SM-030, 038–041, 047–052, 053)
**Status:** checkpoint after 5 of 12 spine units; SM-047–053 (the census and the mirror) not yet run

---

## 1. Purpose

Selina proposed a spine for a first joint arXiv/OSF paper. Before endorsing publication, this session is independently re-verifying every unit of that spine from a clean checkout — not trusting the registry's own tally — and separately checking, for each unit, how much of its content is classical versus how much could be genuinely new, since a paper that presents known theorems as findings will not survive review.

Order chosen deliberately: the roof (SM-030) first, then the four units that form the paper's actual core (SM-038–041) — if the core failed to reproduce, the roof would not save the paper. It didn't fail.

## 2. Method

Unchanged from the two prior audits in this thread: SHA256 verification, dependency tracing, clean re-execution independent of the authoring machine, line-by-line diff against the shipped log. New this round: a literature pass per unit — web search for the specific mathematical claims, classified as classical / plausibly new / disputed.

## 3. Summary

| Stone | Name | Result | Matches shipped log | Dependencies (all located or regenerated) |
|---|---|---|---|---|
| SM-030 | Stone V — the roof (W⁺(E₈)) | 44 PASS / 0 FAIL | identical values; only cache-vs-fresh-build annotations differ | `_stone_u_cache` (incl. regenerated `kbar_*`) |
| SM-038 | Stone Z — the still point (G₂(2)) | 19 PASS / 1 disclosed FAIL (Z6b) | byte-identical | `_stone_u_cache`, `_stone_x_cache/witnesses_x.json` |
| SM-039 | Stone AA — the roof clock | 16 PASS / 0 FAIL | byte-identical | `_stone_u_cache`, `_stone_x_cache`, `_stone_z_cache` |
| SM-040 | Stone AB — the merkabit under the still point | 14 PASS / 0 FAIL | byte-identical | `_stone_u_cache`, `_stone_x_cache`, `_stone_z_cache`, `scar56_data.json` |
| SM-041 | Stone AC — the parity rule of the clock | 9 PASS / 2 disclosed FAIL (AC2b, AC5c) | byte-identical | `scar56_data.json` only |

All five reproduced their self-reported pass/fail tallies exactly, including every disclosed "registered expectation INVERTED" — nothing found here contradicts what the source documents already say about themselves.

## 4. Literature pass

### 4.1 SM-030 (the roof)
Entirely classical territory: |W(E₈)| = 696,729,600, the rotation subgroup W⁺(E₈) of index 2, the embeddings of Sp₆(2) and its non-split double cover 2·Sp₆(2), and the connection to O₈⁺(2) via triality trace back to **Conway, "Three Lectures on Exceptional Groups" (1971; reprinted in Conway–Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., ch. 10)** and the **ATLAS of Finite Groups** (Conway, Curtis, Norton, Parker, Wilson, 1985). The Schur covers used (SL(2,7), 2I=SL(2,5), GL(2,3)/2O, 2T=SL(2,3)) are standard. No source found stating the specific "roof theorem" (one minimal-found overgroup holding both towers simultaneously, with explicit witnesses) — this looks like a genuine, if narrow, computational contribution: an explicit verified construction built entirely from classical ingredients, not a new abstract theorem.

### 4.2 SM-038 (the still point = G₂(2))
The underlying fact — Out(O₈⁺(2)) ≅ S₃ (triality) and the centralizer of an order-3 outer automorphism is G₂(2) — is classical and is already cited as [P] inside the verifier itself. Standard references: Conway (as above); **Kleidman, "The maximal subgroups of the finite 8-dimensional orthogonal groups PΩ₈⁺(q) and of their automorphism groups"** (J. Algebra, 1987). The specific machine-built intertwiner τ″ and the exhaustive 12,096-element fixed-set computation are original computational work on top of a known structural fact.

### 4.3 SM-039/041 — the important finding
**The headline fact that the clock's order equals the Coxeter number is not new.** This is the content of **D. Rush and X. Shi, "On Orbits of Order Ideals of Minuscule Posets"** (Discrete Math., 2013 / arXiv 1112.xxxx), which proves exactly this — rowmotion on any ADE-type minuscule poset has order equal to the Coxeter number, with a cyclic sieving phenomenon — for the general class of minuscule posets, explicitly including the two exceptional-type minuscule posets associated to E₇ and E₈. The 56-element E₇ minuscule poset used throughout SM-039/041 (order-18 rowmotion, CSP against 1+q+…+q¹⁷) is a textbook instance of the Rush–Shi theorem, not a fresh discovery.

This matters because several stones (SM-035, SM-038, SM-039, SM-041) build a running narrative — "every other measured crystal clock ticked at its own Coxeter number" — that reads, across the correspondence, as if this pattern were being discovered. It should instead be cited: Rush–Shi (2013) for the base fact, with the paper's own contribution repositioned as (a) identifying that the specific combinatorial object Ψ built in this project's own machinery *is* rowmotion on this specific poset (a nontrivial but different kind of claim), and (b) SM-041's **parity rule** — the specific criterion (XOR of toggled simple-root masks, kept iff the total adjacency count is even) governing which pairs of states preserve incidence type under Ψ. No direct match for this second, more specific mechanism was found in this pass — it is the more plausible candidate for genuine novelty, but the search was not exhaustive and deserves a second, more targeted pass before the paper is drafted.

**SM-035's G₂ 7-cycle** (order 7 > h(G₂) = 6, flagged elsewhere in the correspondence as "the clock exceeding its Coxeter number") is a different, degenerate case: the "crystal" there is a totally ordered 6-chain, and the verifier's own honest caveat already concedes that rowmotion on a chain being a single cycle is elementary. That self-disclosure is correct and should stay in the paper as written.

## 5. What this checkpoint does and does not establish

**Established:** the roof and the four-stone core of the proposed spine are computationally sound and reproduce cleanly and completely from a clean checkout, with every self-disclosed failure matching independent re-execution. The load-bearing claim of the paper's proposed core section — rowmotion order = Coxeter number on the 56-board — needs a citation to Rush–Shi (2013) rather than being presented as newly observed.

**Not yet established:** the remaining seven spine units (SM-047–053: the census of twisted classes, the ATLAS naming, the mirror as the E₆ diagram automorphism) have not been re-run or checked against the literature in this session.

## 6. Outstanding

- Independent re-run of SM-047–053 (7 units: `ROOF_CLOCKS_2026-09-06` for SM-047–050, `COSET_AND_MIRROR_2026-09-06` for SM-051–053).
- A more targeted literature search specifically for SM-041's parity-rule mechanism, before treating it as confirmed novel.
- A citation check for SM-047–052's ATLAS class-naming work (already sourced to Thomas Breuer's GAP CTblLib per the correspondence — likely fine, but not yet independently checked here).
