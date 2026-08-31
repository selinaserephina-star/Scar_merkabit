# TWO-ENGINE DIFF — Blind Bridge Classification (2026-08-31)

**Engine 1 (IB's):** `RECEIVED_2026-08-31_IB_HINGE_COMPRESSION/blind_bridge_classification_engine_run.md`
(sha 30fe7ae5…, received 2026-08-31).
**Engine 2 (ours):** `blind_engine_OURS.md` + `verify_blind_engine.py` (55/55 checks).
**Blindness held:** our engine was run by an isolated agent given ONLY the six pairs
and the derivation list from IB's SECOND ENGINE spec; it never saw IB's run, the
registry, the T1–T6 typology, or SM-020/SM-022. This diff is the first contact
between the two outputs.

## Verdict up front

**The two engines agree on every computed fact — 6 pairs for 6.** Embeddings,
shared subgroup types, normal subgroups, quotients, directions, reversibility:
no factual discrepancy anywhere. The derived CLASS partitions agree up to
refinement: identical at the top, ours finer at the bottom.

## Per-pair diff

| pair | IB engine | our engine | data agreement |
|---|---|---|---|
| (PSL(2,7), C₆×ℤ₂) | Class III — deficient indirect (shared {1,C₂,C₃,V₄}, gcd bound 4/12 short) | SEVERED (same shared set; no mono/epi either way, 14 order-12 subgroups exhaustively tested, all A₄) | EXACT |
| (C₆×ℤ₂, A₅) | Class III — deficient indirect (same set, 4/12 short) | SEVERED (same set; A₅'s only order-12 type is A₄) | EXACT |
| (A₅, S₄) | Class II — saturated indirect (shared adds S₃, A₄; gcd 12/12 reached) | SEVERED, deepest shadow (same shared set {1,C₂,C₃,V₄,S₃,A₄}) | EXACT |
| (S₄, A₄) | Class I — direct, normal, index 2, split | ONE-WAY SPLIT DESCENT (normal, complemented, unique copy; A₄ NOT a quotient of S₄) | EXACT |
| (A₄, ℤ₂) | Class I — direct, non-normal, no dual quotient | LOOSE FRAGMENT (3 conjugate copies, none normal; ℤ₂ not a quotient of A₄) | EXACT |
| (ℤ₂, {e}) | Class I — terminal (subgroup/quotient coincide) | RETRACT COLLAPSE (split with left inverse — the only reversible pair) | EXACT |

## Where the partitions differ (refinement only, no conflict)

- IB's partition: {P1,P2} / {P3} / {P4,P5,P6}. Ours: {P1,P2} / {P3 flagged} /
  {P4} / {P5} / {P6}.
- IB separates P3 from P1–P2 by **gcd-bound saturation** (12/12 vs 4/12); our
  engine separated it by **nonabelian shared types** (S₃, A₄ appear only there).
  Two independent criteria, same cut — that the cut reproduces under a different
  load-bearing invariant strengthens it.
- Our engine splits IB's Class I three ways on computed predicates his run also
  records (P4 normal+split; P5 non-normal, no dual quotient; P6 retract). His
  own prose already distinguishes P4 from P5 in exactly these terms — so the
  refinement is latent in his run, just not promoted to class level.

## Convergent unprompted patterns

- IB's unprompted pattern: only the top two pairs fall short of the gcd bound.
- Ours: the "erosion tail" — P4–P6 are pure-loss genuine inclusions, P1–P3 hold
  no subgroup relation at all ("the chain becomes concrete at S₄"); no pair has
  a common nontrivial quotient ("no shared voice"); {1,C₂} is the persistent
  core, dying only at the last step; C₆/C₆×C₂ types are a "foreign body"
  appearing at P1 and vanishing at P2.
- Both match the sealed SM-020 two-regime theorem (bottom inclusions / top
  crossings) — found here twice more, blind, from raw data.

## Notes

- Neither engine used T1–T6; comparing the blind classes to the T1–T6 typology
  (SM-022 derived those 6/6 from computed signals) is a separate, now
  well-posed exercise: T6/T3/T2 land on the SEVERED pairs, T1(+T4)/T5/T1 on the
  concrete tail.
- IB's run's factual side-claims spot-checked against our census: PSL(2,7)
  element orders {1,2,3,4,7} ✓; A₄ as A₅'s unique order-12 type ✓; S₄'s normals
  {1,V₄,A₄,S₄} ✓; A₄ has no index-2 subgroup ✓. All confirmed.
