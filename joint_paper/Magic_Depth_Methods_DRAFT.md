---
title: "Magic Depth by Transportation Certificates and Witness Campaigns"
subtitle: "Exact minimal-scrambling theorems on two crystal machines, the certificate that proves them, and where the method ends — DRAFT v0.1"
author: "Selina Stenberg · Ilya Balashov · with Claude (Anthropic Fable 5)"
date: "2026-08-30 — draft, sealed-not-sent; companion to *The Bitangent Bridge*"
---

**Status.** Joint-lane draft under the same protocol as the bridge paper:
v0.1 written on the Stenberg side, awaiting Ilya's review pass. Every
numerical claim is a passing check of a named script (Appendix A; plain
Python 3 + numpy). Grades: **[P]** proved/classical, **[C]** computed
exactly, **[obs]** observation we have not located in the literature,
**[OPEN]** open. No physical claims.

## Abstract

Many computational cost models have a two-tier shape: a large *structured*
group of cheap operations and one expensive *scrambling* generator, with
cost measured by how many expensive layers a program needs (the shape of
Clifford+T compiling, where T-count and T-depth price fault tolerance). We
study this question *exactly* on two finite model systems — permutation
machines built on the E₆ and E₇ minuscule crystals (27 and 56 states,
rowmotion clocks as the scrambler, two independent "grammars" of cheap
gates) — and prove exact minimal-depth theorems for all of their ~10²⁸ and
~10⁷⁴ programs. The method is a **certificate**: when the cheap group is a
Young (block) or wreath subgroup, double cosets are contingency tables and
depth-k writability is equivalent to an integer transportation-feasibility
problem, reducing the depth question to finite dynamics on a few hundred
tables. When the cheap group is hyperoctahedral (a Gelfand pair), the
table calculus is replaced by coset-type dynamics on partitions; there the
general composition law is open, and we close the depth question instead
by an exhaustive **witness campaign** — an explicit, machine-verified
two-layer construction for every one of the 3,718 coset types. Headline
results: both machines have magic-depth exactly 2 relative to their
natural wreath typing, and the 56-machine has depth exactly 2 in *both* of
its rival grammars; removing specific cheap symmetries raises the depth by
measured amounts (a leg-rotation is worth one expensive gate, a mirror
worth three). We release the instance families with certified optima as
benchmarks, our exact small-n hyperoctahedral support tables as data for
the open (S₂ₙ, Bₙ) connection-coefficient support problem, and record two
refuted candidate laws and three search regimes with their failure
boundaries.

## 1. Setting

Let G = ⟨H, m⟩ ≤ S_N with H a "typed" (cheap) subgroup and m a "magic"
(expensive) generator. The **magic depth** of g is the least k with
g ∈ H(mH)^k; MAGIC-DEPTH(G; H, m) is the least k covering all of G. Our
model systems [C]:

- **The 27-machine**: the E₆ minuscule crystal; typed = the X/Y/Z register
  structure (Young S₉³, or wreath S₉≀S₃); magic = the rowmotion power Ψ⁴.
  ⟨H, Ψ⁴⟩ = S₂₇ (Schreier–Sims). Prior exact resource theory (magic
  monotone μ, T-count bound, wreath∩A₂₇ depth-2) in the CRYSTAL_NATIVE_v2
  registry (CN-011/012).
- **The 56-machine**: the E₇ minuscule crystal, which carries two rival
  typings — the **branch grammar** (blocks 27 ⊕ 27̄ ⊕ 1 ⊕ 1 of the
  E₆-branching; Young/wreath) and the **frame grammar** (the stabiliser of
  the antipodal matching ι, hyperoctahedral B₂₈); magic = the rowmotion
  clock Ψ. ⟨H, Ψ⟩ = S₅₆ in both cases. The two grammars' reconciling gates
  (the sheet-mirror pr and the antipode ι) have magic zero in *both*
  grammars [C] — the machine's "structure is free; only time is expensive."

## 2. The transportation certificate (Young and wreath typing)

**Theorem 2.1 [P].** For H a full Young subgroup, the double coset HgH is
the block-transport contingency table T(g), and
g ∈ H(mH)^k ⟺ T(g) lies in the k-fold *table composition* of T(m), where
one composition step is integer 3-tensor transportation feasibility with
margins T(previous), T(m), T(candidate). Wreath typing = the same calculus
with table sets closed under row/column block permutations.

*Proof idea:* necessity by counting flows; sufficiency because a full
block symmetric group in the middle can match any feasible arrival pattern
to any departure pattern. (The earlier CN-012 proof needed a parity-repair
lemma only because its H was cut to even permutations; over full
Young/wreath the certificate is exact with no lemma.)

The astronomically large depth question thus becomes finite dynamics on
contingency tables: 1,540 tables for the 27-machine, 908 for the
56-machine's branch grammar.

**Results [C]** (`verify_stone1_certificate.py`, 9 checks):

| machine | typed side | magic | depth |
|---|---|---|---|
| 27 | Young S₉³ | Ψ⁴ | **3** |
| 27 | wreath S₉≀S₃ | Ψ⁴ | **2** |
| 56 branch | Young S₂₇×S₂₇̄ | Ψ | **5** |
| 56 branch | + sheet-swap (= pr) & vacuum-swap | Ψ | **2** |

**Corollary (symmetry exchange rates) [C].** Cheap symmetries convert to
expensive-gate savings at measurable rates: the typed S₃ leg-rotation of
the 27-machine is worth exactly one magic gate (3 → 2); the 56-machine's
sheet-mirror is worth exactly three (5 → 2) — and the mirror is itself a
zero-magic gate.

## 3. The hyperoctahedral case (Gelfand-pair typing)

For the frame grammar, H = Stab(ι-matching): the pair (S₂ₙ, Bₙ) is a
Gelfand pair, the double coset of g is its **coset type** (the partition
of n = 28 from the half-lengths of the union cycles of M₀ ∪ gM₀), and one
magic step is the **triple-matching relation** (∃ M₁, M₂ with
type(M₀,M₁) = λ, type(M₁,M₂) = τ(m), type(M₀,M₂) = μ), well-defined on
types by Stab-transitivity [P].

What we establish (`verify_stone1b_hyperoct.py` and companions):

1. **Triangle necessity [C, exhaustive n ≤ 7].** With the matching metric
   d(λ) = n − ℓ(λ), all feasible triples satisfy the triangle
   inequalities — verified over every triple at n = 4..7 (up to 135,135
   matchings exhausted).
2. **Two candidate sufficiency laws refuted [C].** Neither "support = the
   triangle set" nor "support = the full d-interval away from the
   identity" survives the exact tables (e.g. (2,2)∘(2,2) cannot produce
   (3,1)). The general support law for (S₂ₙ, Bₙ) connection coefficients
   remains **[OPEN]**; our exact n ≤ 7 support tables are released as data
   for it.
3. **The reduction validated [C].** Matching-BFS ground truth equals
   exact-table closure for four magic types at n = 5 (4/4), and the scaled
   shape τ = (2,2,2,1) gives closure depth 2 at n = 7.
4. **Theorem 3.1 [C, by witnesses].** *The frame-grammar magic-depth of
   the 56-machine is exactly 2.* For every one of the p(28) = 3,718 coset
   types there is an explicitly constructed, machine-verified witness
   M₀ →τ→ M₁ →τ→ M₂ with τ = τ(Ψ) = [9,9,9,1]; depth 1 reaches only τ.
   Census: 1,606 witnesses by uniform τ-side orbit sampling, 2,039 by soft
   dual-cost annealing, and the final 73 by **dual-direction orbit
   sampling** (construct the target side exactly by Stab(M₀)-conjugation;
   rejection-test the τ side). All witnesses cached and re-verifiable
   (`stone1b_witnesses.json`).

**Combined [C].** The 56-machine has magic-depth exactly 2 in *both* of
its rival grammars: two ticks of the clock reach every grammar class,
whichever language prices the program — and the translation gates between
the languages are free in both.

## 4. Lessons

1. **Cost lives in the quotient.** 10⁷⁴ programs; 908 (or 3,718)
   essentially-different cases. Before optimizing over circuits, find the
   invariant the free gates cannot change; the size of *that* space is the
   problem's true size. Our machines are a fully worked, end-to-end
   instance of the principle.
2. **Symmetry has an exchange rate.** Enlarging the free library has a
   quantifiable expensive-layer dividend (here: one gate per S₃, three per
   mirror). Worth measuring deliberately in real gate libraries.
3. **Failed search is weak evidence of infeasibility.** Seventy-three
   entropically thin targets defeated two search regimes and fell
   instantly to a re-parametrized third. "No shorter circuit found" and
   "no shorter circuit exists" are separated exactly by such
   re-parametrizations.
4. **The hardness gradient.** Young/wreath typing: solved by a poly-size
   certificate. Gelfand-pair typing: depth decidable by witness campaigns;
   the composition law open. Unitary Clifford+T: open. Knowing where the
   certificate dies is the map of where the research is.

## 5. Released artifacts

Benchmark families with certified optimal depth (both machines, both
typings, with verifiers); the exact hyperoctahedral support tables
(n ≤ 7); the 3,718-witness cache; all scripts (Python 3 + numpy, no
external group-theory software — the point being that a reader can
re-derive everything, including the character-table and Schreier–Sims
substrate, from first principles in seconds to minutes).

## 6. Open problems

1. The support law for (S₂ₙ, Bₙ) coset-type composition (our tables as
   data; triangle necessity proved; two candidate laws refuted).
2. Is wreath-depth 2 *generic* for minuscule-crystal clocks? (Both our
   machines land on 2; a positivity condition on T(m) may explain it.)
3. The unitary generalization: do transportation-style certificates exist
   for genuine Clifford+T double cosets? (We state this as a question for
   the synthesis community rather than a claim.)

## Appendix A — reproducibility

`verify_stone1_certificate.py` (9 checks; §2), `verify_stone1b_hyperoct.py`
(11 checks; §3.1–3.3), `verify_stone1b_stragglers.py` +
`verify_stone1b_close73.py` + `stone1b_witnesses.json` (§3.4), with the
substrate verifiers of the Scar_merkabit lane (bridge, resurrection,
machine data). Registry rows SM-009/SM-010 carry the sealed history,
including the two refuted candidate laws and one fixed implementation bug
(a doubled-type error in v1 of the coset-type routine), recorded per the
lane's rules: refutations at equal prominence.

*(Bibliography joint, to be completed at review: Clifford+T resource
theory and T-depth optimization; Young double cosets and contingency
tables; the (S₂ₙ, Bₙ) Gelfand pair, zonal polynomials and matching
connection coefficients; dynamical algebraic combinatorics of rowmotion.)*
