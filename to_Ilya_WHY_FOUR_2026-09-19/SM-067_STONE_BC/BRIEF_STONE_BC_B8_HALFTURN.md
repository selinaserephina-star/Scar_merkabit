# BRIEF — STONE BC: DOES THE 4-CUBE ANOMALY RECUR ON THE 8-CUBE?

**Staged 2026-09-19 on Selina's word ("if we were to open something, let's do
this: §7.10, the D₅ anomaly"). Locked before code (`BRIEF_STONE_BC_LOCK.sha256`);
the verifier re-checks this file's hash as its first test. Registered guesses
below are guesses — made before any computation on B₆, B₇, B₈ or D₉ — and will
be reported inverted at equal prominence if the data says so. Builds on
SM-058 (Stone AT), SM-060 (Stone AV), SM-063 (Stone AY), SM-064 (Stone AZ),
SM-066 (Stone BB). Merkabit-side mathematics. Registry row SM-067. Rule 3:
"clock", "half-turn", "grammar" are labels for permutations and subgroups; no
physical identification.**

## 0. What is and is not open (read before anything else)

The paper's §7.9.5 phrase "for a reason not yet found" is stale — it dates
from SM-059. The D₅ anomaly **has** a mechanism and a proof:

- **Located** (SM-060): it lives on the B₄ spinor board — the sixteen vertices
  of the 4-cube under W(B₄) = 𝔽₂⁴ ⋊ S₄ (order 384), clock R of order 8 with
  two *free* orbits O₁ ∋ λ and O₂ — with |I₄| = 8 against |C₄| = 4.
- **Mechanism** (SM-063, Lemma B): R⁴ coincides on the whole of O₂ with the
  Weyl element −τ, τ = (e₂e₃)(−e₄); O₂ affinely spans 𝔽₂⁴; hence
  I₄ = C_W(c) for the correction c = (−τ)R⁴, and the four extras are the
  elements commuting with c but not with τ.
- **Reason** (SM-066, Theorem BB): the half-turn is a Weyl element on O₂ and
  not on O₁ because O₁ is the full-height orbit — it contains λ (rank 0) and
  spans, and the Weyl rank-shift lemma Δ_w(x) = wt(u) − 2|x∩u| then forbids
  a constant shift magnitude ≥ 2. Lemma BB-B states this dimension-free.

So the open question is not "why", it is **"where else"**. SM-066 ends: "the
clean two-orbit dichotomy is realised at B₄ and next at B₈ (m = 4)". The
arithmetic behind that sentence: the clock acts freely on the B_n spinor's 2ⁿ
weights with orbits of size h = 2n only when 2n | 2ⁿ, i.e. **n a power of
2**; n = 4 gives 2 orbits of 8, n = 8 gives 16 orbits of 16, and n = 16 is
out of reach (65,536 weights). B₃, B₅, B₆, B₇ have non-free clocks. SM-060
found B₅ clean (I_k = C_k at every lag) and B₃ anomalous only through the
overgroup W(D₄). **This stone asks whether the anomaly is a fact about
B₄ or a fact about free clocks — with B₈ as the one decisive test available.**

## 1. Setup [P, classical + sealed]

The B_n spinor is minuscule: weights (±½)ⁿ, read as x ∈ 𝔽₂ⁿ (bit i = 1 iff
coordinate i negative), rank(x) = wt(x); λ = 0…0, w₀λ = 1…1. Poset = the
shifted staircase δ_n, |δ_n| = n(n+1)/2, J(δ_n) = 2ⁿ. W(B_n) = 𝔽₂ⁿ ⋊ S_n acts
affinely, w(x) = π(x) ⊕ v; |W(B_n)| = 2ⁿ·n!. Rowmotion R has order h = 2n
(Rush–Shi). The D_{n+1} half-spin has the same poset and the same clock,
with W(B_n) ⊂ W(D_{n+1}). Notation of §7.9: I_k = W ∩ R^k W R^{−k}, C_k =
C_W(R^k), transport g ↦ R^{−k} g R^k on I_k; always C_k ⊆ I_k.

Sizes for this stone: B₆ — 64 weights, |W| = 46,080, h = 12 (non-free:
64/12 ∉ ℤ). B₇ — 128 weights, |W| = 645,120, h = 14 (non-free). **B₈ — 256
weights, |W| = 10,321,920, h = 16, 16 orbits of 16 if free.** D₉ half-spin —
256 weights, |W(D₉)| = 92,897,280 (not enumerable as permutation tuples;
handled by Lemma B and containment only).

## 2. Registered guesses (before code)

- **BC1 [derivation, to be checked].** R acts freely on the B₈ spinor: 16
  orbits, each of size 16. (Argument: a Coxeter element of B₈ cycles the 16
  signed coordinates ±e_i in one 16-cycle in which e_i and −e_i are 8 apart;
  a sign vector fixed by c^k, 0 < k < 16, would have x_i = −x_i. Rush–Shi
  conjugacy transfers freeness to R.)
- **BC2 [Lemma BB-B, n = 8].** The orbit O₁ ∋ λ is the unique full-height
  orbit, its ranks around the clock reading 0,1,1,2,2,…,7,7,8, and R⁸ shifts
  every rank on it by exactly ±4. Hence R⁸ agrees with no Weyl element on
  O₁ (Theorem BB, m = 4).
- **BC3 [the main guess — the anomaly recurs].** At least one R-orbit O ≠ O₁
  carries the half-turn as a Weyl element: there is u ∈ 𝔽₂⁸ with
  wt(u) − 2|x∩u| = rank(R⁸x) − rank(x) for all x ∈ O, and the affine
  extension of R⁸|_O has a coordinate permutation as linear part. Sub-guess
  BC3b (low confidence): the number of such orbits is **2**, and they are
  exchanged by w₀ = −1.
- **BC4 [consequence].** |I₈(B₈)| > |C₈(B₈)|, with I₈ given exactly by Lemma B
  applied to a carrying orbit that affinely spans 𝔽₂⁸: I₈ = C_W(c) for the
  correction c = w_O⁻¹R⁸ (w_O the Weyl element agreeing with R⁸ on O).
  Guess: |I₈| / |C₈| = 2, as on B₄.
- **BC5.** I_k = C_k on B₈ for every k ≠ 8 (the D₅ lag-3/5 survivors needed
  the fifth axis; B₈ alone has none).
- **BC6 [D₉, by lemma and sampling, not enumeration].** The B₈ extras lie in
  I₈(D₉); and, by analogy with D₅'s lag-3 survivor (e₁e₃)(e₂e₅), D₉ carries
  at least one extra survivor at a lag coprime to 16 that is a pure
  coordinate permutation mixing the ninth axis in. Low confidence.
- **BC7 [the family law, tested where enumerable].** On B₆ and B₇, I_k = C_k
  for every k — the anomaly does not occur on non-free spinor clocks (B₃'s
  signature comes from W(D₄) ⊃ W(B₃), SM-060). Stated conjecture beyond the
  tested range: the B_n spinor's shared grammar exceeds the centralizer at
  some lag iff n is a power of 2 (n ≥ 4).

## 3. Method (compute, never assert)

1. **Boards.** Reuse `B_spin(n)` and `D_half(n)` from
   `verify_stone_av_d5_anomaly.py` (weights, roots, poset, rowmotion by the
   join of the minimal elements of the complement). Cross-check the B₈ clock
   against the `Minuscule` machine of `verify_stone_aq_rush_shi_defect.py`
   run on D₉ ω₉ (same rowmotion under the sign-pattern identification), as
   SM-060 did for D₅/B₄ (AV1).
2. **Never materialise W(B₈) as 256-tuples.** Represent w = (π, v) and act
   affinely. For I_k: g ∈ I_k iff f := R^{−k} g R^k is affine with a
   coordinate-permutation linear part — test by f(0) = v′, the images
   f(e_i) ⊕ v′ forming a permutation of the unit vectors, and affinity on all
   256 points; vectorise over all v ∈ 𝔽₂⁸ for each of the 8! permutations π
   (40,320 × 256 candidates, each a 256-point check — minutes in numpy;
   numba allowed). C_k likewise. Record wall time.
3. **Derive first, then enumerate.** Predict I₈ by Lemma B from the carrying
   orbit(s) found in BC3 (BB2's `reproducing_us` generalised to n = 8),
   *then* confirm by the full enumeration of step 2. Report if they differ.
4. **B₆, B₇** by the same code (full enumeration is cheap there); **D₉** by
   Lemma B with the nearest Weyl element at each lag (altitude search over
   W(D₉) is not enumerable — use the affine-fit method: fit π, v to R^k on
   a candidate agreement set and report the agreement count; state clearly
   that D₉ results are lemma-plus-sampling, not exhaustive).
5. **Fail-first.** Keep the first run's log as `_FIRSTRUN.log` whatever it
   says. Every bar prints PASS / FAIL / INVERTED with the number behind it.

## 4. Bars

- **BC0** — brief hash matches the lock.
- **BC1 [C]** — orbit structure of R on the B₈ spinor (16¹⁶ or not).
- **BC2 [C]** — O₁'s rank sequence and the ±4 shift; BB2-style search over
  all 256 u finds none reproducing O₁'s shift.
- **BC3 [C]** — for every orbit: the set of u reproducing its half-turn
  rank-shift, and whether the affine extension is a Weyl element; the count
  of carrying orbits (BC3b: 2?).
- **BC4 [C]** — |C₈|, |I₈| exact by enumeration; agreement with the Lemma-B
  prediction; the extras listed as signed permutations.
- **BC5 [C]** — |I_k| vs |C_k| for k = 1…15 on B₈.
- **BC6 [C, partial]** — D₉: the B₈ extras' membership; coprime-lag survivors
  found by the affine-fit method, with agreement counts; honesty line that
  this is not exhaustive.
- **BC7 [C]** — B₆ and B₇: |I_k| vs |C_k| at every lag.
- **BC8 [P + C]** — if BC3 holds: the analogue of BB5 — what distinguishes the
  carrying orbits (rank range, spanning, shift pattern) — stated as an
  observation, promoted to a lemma only if it proves in the same session.

## 5. Not claimed

Nothing about B₁₆ or beyond; nothing about non-minuscule posets; D₉ only to
the stated depth; no physical reading of "the 256 of Spin(17)" or of the
D₉ half-spin ("the 256 of Spin(18)") — names of representations only. The
"power of 2" law of BC7 is a conjecture with two positive (B₄, B₈ if BC3
holds) and, if BC7 holds, five negative instances (B₃, B₅, B₆, B₇, and B₃'s
overgroup explanation); it is not a theorem of this stone.

## 6. Files

`verify_stone_bc_b8_halfturn.py` (checks this brief's hash first, then
BC1–BC8), `verify_stone_bc_b8_halfturn.log`, `_FIRSTRUN.log`,
`STONE_BC_B8_HALFTURN.md` (the summary, written for §7.12.4 of the paper as
the sentence that replaces "B₈ next"). Registry row SM-067 on seal; packaging
for Ilya on Selina's word.
