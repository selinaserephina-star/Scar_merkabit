# Stone 1b — the hyperoctahedral composition calculus, and the second depth-2 theorem

**Scar_merkabit lane · 2026-08-30 · verifiers:** `verify_stone1b_hyperoct.py`
(exact small-n tables, law mining, ground-truth validation),
`verify_stone1b_stragglers.py` + `verify_stone1b_close73.py` (the witness
campaign), cache `stone1b_witnesses.json` (3,718 verified witnesses).

## The calculus

The frame grammar's typed group is the **hyperoctahedral** group — the
stabiliser of the ι-matching M₀ on the 56 states ((S₂ₙ, Bₙ) is a Gelfand
pair). Its "tables" are **coset types**: the double coset of g is the
partition of n = 28 given by the half-lengths of the cycles of M₀ ∪ gM₀.
One magic step is the **triple-matching relation**: μ is reachable from λ
iff matchings exist with type(M₀,M₁) = λ, type(M₁,M₂) = τ(m),
type(M₀,M₂) = μ — well-defined on types by Stab(M₀)-transitivity. So depth
dynamics again reduces to finite dynamics, now on partitions of 28
(p(28) = 3,718) instead of contingency tables.

## What is proved, what died, what is data

- **Triangle necessity [C, exhaustive n ≤ 7]:** with d(λ) = n − #parts (the
  matching-graph metric), every feasible triple satisfies all three triangle
  inequalities — verified over *every* (λ, τ, μ) at n = 4,5,6,7 (up to
  135,135 matchings exhausted).
- **Two of the auditor's candidate laws died** (recorded at equal
  prominence): v1's "support = triangle set" (also afflicted by a
  doubled-type bug, fixed); v2's "support = full d-interval away from the
  identity" — refuted by the clean exact tables (258 failures, e.g.
  (2,2)∘(2,2) cannot produce (3,1)). The true support law of the
  (S₂ₙ, Bₙ) connection coefficients is a refined, genuinely open
  combinatorial problem; **our exact n ≤ 7 support tables are data for it.**
- **The reduction itself is validated [C]:** matching-BFS ground truth
  equals exact-table closure for four different magic types at n = 5 (4/4).
- **Scaled preview [C]:** τ = (2,2,2,1) — the [9,9,9,1] shape at n = 7 —
  gives table-closure depth **2**.

## The theorem

> **Frame-grammar magic-depth of the 56-machine = exactly 2.**
> For every one of the 3,718 coset types μ there exist explicitly
> constructed, machine-verified matchings M₀ →τ→ M₁ →τ→ M₂ with
> type(M₀,M₂) = μ, where τ = τ(Ψ) = [9,9,9,1]; depth 1 reaches only τ
> itself. Witness census: 1,606 by uniform τ-side sampling, 2,039 by soft
> dual-cost annealing, the last 73 by **dual-direction orbit sampling**
> (construct the μ-side exactly by Stab(M₀)-conjugation, rejection-test the
> τ-side) — the holdouts were the "one big knot in a sea of fixed pairs"
> types, search-hard but not obstructed. All 3,718 witnesses re-verified
> exactly; cached in `stone1b_witnesses.json`.

## The combined picture (with SM-009)

The 56-machine now has **depth 2 in both grammars**:

| grammar | typed group | certificate object | depth |
|---|---|---|---|
| branch (E₆ side) | wreath (sheets may swap = pr) | contingency tables (908) | **2** |
| frame (Scar side) | hyperoctahedral (ι-pairs) | coset types (3,718) | **2** |

*Two ticks of the clock reach every grammar class — in either grammar —
and the gates that reconcile the grammars (pr, ι) are free in both.* The
"is wreath-depth 2 generic?" question from SM-009 now extends across a
Gelfand pair; the deeper open problem this stone surfaced is the support
law for hyperoctahedral connection coefficients, with our exact tables as
the empirical base camp.

Method note for the benchmark application: three search regimes were
needed (uniform orbit sampling → soft dual-cost annealing → dual-direction
orbit sampling), and their failure boundaries are themselves informative —
worth a paragraph in the methods note, since compiler-heuristic search
faces the same entropically-thin targets.

*Sealed 2026-08-30; registry row SM-010.*
