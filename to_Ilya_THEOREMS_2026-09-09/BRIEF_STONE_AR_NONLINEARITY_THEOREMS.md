# BRIEF — STONE AR: THE NON-LINEARITY THEOREMS (merkabit side)

**Staged 2026-09-09 on Selina's "Do this" (make SM-055's table a theorem).
Locked before code (`BRIEF_STONE_AR_LOCK.sha256`). Merkabit-side
mathematics recorded in the joint lane because the spine paper's tier
three cites it. Deviations = dated AMENDMENT; post-reveal changes are
findings. The proofs below were written before the code; the verifier
checks every ingredient the proofs use, case by case, and the formulas
against the machine of Stone AQ (verbatim).**

## Setting (as in SM-055)

λ minuscule for a simply-laced simple root system, weights Wλ, the
lattice L on Wλ with covers w → w − α_i at label 1, P = P_λ its
join-irreducibles (coloured by i), R = rowmotion transported to the
weights, h the Coxeter number, W the Weyl group acting on Wλ. All inner
products are the W-invariant form with ⟨α,α⟩ = 2, so ⟨w, α_i⟩ = label_i(w).
Standard facts used [P]: for minuscule λ, |P| = ht(λ − w₀λ) and the
multiplicity of colour i in P is the coefficient c_i of α_i in λ − w₀λ =
λ + λ* (λ* = −w₀λ the dual weight); P is graded with h − 1 ranks; the
minuscule weights are A_n ω_k, D_n ω₁/ω_{n−1}/ω_n, E₆ ω₁/ω₆, E₇ ω₇ (and
B_n ω_n, C_n ω₁, not simply-laced, outside this stone); Rush–Shi 2013.

## Theorem 1 (rowmotion is a Weyl element only on chains)

R ∈ W ⟺ P is a chain ⟺ (λ = ω₁ or ω_n of A_n). Then R is the Coxeter
element s₁s₂⋯s_n (the (n+1)-cycle on e₁,…,e_{n+1}).

*Proof.* R(λ) = w₀λ (the ideal P ↦ ∅). The bottom w₀λ = −λ* has exactly
one nonzero label, −1 at the dual node k*, so it has exactly one cover
p₀ = w₀λ + α_{k*}, which is the unique minimal element of P; hence
R(w₀λ) = p₀. If R ∈ W it is an isometry, so ⟨λ, w₀λ⟩ = ⟨R λ, R w₀λ⟩ =
⟨w₀λ, w₀λ + α_{k*}⟩ = ⟨λ,λ⟩ − 1. But ⟨λ, λ − w₀λ⟩ = Σ c_i ⟨ω_k, α_i⟩ = c_k,
so ⟨λ, w₀λ⟩ = ⟨λ,λ⟩ − c_k, and c_k = 1: colour k occurs once in P. From
the classification, c_k = min(k, n+1−k) for A_n ω_k; 2 for D_n ω₁; ⌊n/2⌋
for D_n ω_n (n ≥ 4); 2 for E₆ ω₁; 3 for E₇ ω₇. So c_k = 1 forces A_n with
k ∈ {1, n}, whose poset is a chain. Conversely on the chain e₁ > … >
e_{n+1}, R is the cyclic shift e_j ↦ e_{j+1}, e_{n+1} ↦ e₁, a permutation
matrix in W(A_n) = S_{n+1}. ∎

## Theorem 2 (the half-turn is linear only on the vector representations)

Let h be even, m = h/2. Then R^m ∈ W ⟺ P is a chain or λ is the vector
representation of D_n (n ≥ 3, with D₃ ω₁ = A₃ ω₂ and, for D₄, its two
triality images ω₃, ω₄). In the vector case R^m is the signed
permutation e_i ↦ −e_{n−i} (1 ≤ i ≤ n−1), e_n ↦ (−1)^{n−1} e_n, which
has an even number of sign changes and so lies in W(D_n).

*Proof.* (Obstruction.) The R-orbit of λ is the principal orbit: with
P_{<j} the elements of rank < j, R(P_{<j}) = P_{<j+1} (the minimal
elements of the complement are the rank-j elements and generate P_{≤j}),
so the orbit is ∅ = P_{<0}, P_{<1}, …, P_{<r} = P, of length h = r + 1.
Write w(j) for the weight of P_{<j} and s_j = |rank j of P| for j < r,
s_r := c_k. Then ⟨w(j), w(j+1)⟩ = ⟨λ,λ⟩ − s_j for every j (indices mod h):
w(j+1) = w(j) + Σ_{p ∈ rank j} α_{c(p)}, and each such α has ⟨w(j), α⟩ =
−1 because adding p to the ideal is adding α_{c(p)} to a weight whose
label there is −1; the wrap-around step w(r) = λ → w(r+1) = w₀λ gives
⟨λ,λ⟩ − c_k as in Theorem 1. If R^m ∈ W then R^m is an isometry with
R^m(w(j)) = w(j+m), so s_{j+m} = s_j for all j: **the extended rank
sequence (s₀, …, s_{r−1}, c_k) is m-periodic.** Now s₀ = 1 always (p₀ is
the unique minimal element), so s_m = 1 is necessary. Case by case:
A_n ω_k (1 < k < n, n odd, m = (n+1)/2): P is the k × (n+1−k) rectangle,
s_m = min(k, n+1−k) ≥ 2 — fails. D_n ω_n (n ≥ 5, m = n−1): P is the
shifted staircase {(i,j): 1 ≤ i ≤ j ≤ n−1} with rank i+j−2, and s_{n−1}
= ⌊(n+1)/2⌋ − 1 ≥ 2 — fails. E₆ ω₁ (m = 6): ranks 1,1,1,2,2,2,2,2,1,1,1,
s₆ = 2 — fails. E₇ ω₇ (m = 9): ranks 1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1,
s₉ = 2 — fails. D_n ω₁ (m = n−1): P = chain(n−2) above the antichain
{e_n, −e_n} above chain(n−2), ranks 1^{n−2}, 2, 1^{n−2}, and c₁ = 2:
the extended sequence (1^{n−2}, 2, 1^{n−2}, 2) is (n−1)-periodic — passes.
D₄ ω₃, ω₄ are the images of ω₁ under triality — pass. Chains: R ∈ W —
pass. (Sufficiency for the vector case.) On D_n ω₁, the ideals are ∅,
the bottom-chain prefixes, the three ideals adding e_n, −e_n or both,
and the top-chain extensions; rowmotion cycles ∅ → … → P (length 2n−2)
and swaps the two one-sided ideals. In weights: −e₁ → −e₂ → … → −e_{n−1}
→ e_{n−1} → e_{n−2} → … → e₁ → −e₁ and e_n ↔ −e_n. Hence R^{n−1}(±e_i)
= ∓e_{n−i} for i ≤ n−1 and R^{n−1}(e_n) = (−1)^{n−1} e_n: the coordinate
permutation i ↔ n−i composed with n−1 sign changes on e₁..e_{n−1} and
(n−1 mod 2) on e_n — n changes for n even, n−1 for n odd, even in both
cases, so in W(D_n). ∎

## Theorem 3 (the kept fraction, two families)

(a) D_n ω₁, n ≥ 3: κ(R) = 1 − 2(n−1) / (n(2n−1)).
(b) A_n ω₂, n ≥ 3: κ(R) = 1 − (3n² − 9n + 4) / C(C(n+1,2), 2).

*Proof of (a).* Types are ⟨w,w′⟩ ∈ {0, −1}; the n antipodal pairs have
type −1. From the explicit R: {e_n, −e_n} stays antipodal; the other n−1
antipodal pairs go to non-antipodal pairs; since R permutes pairs,
exactly n−1 non-antipodal pairs become antipodal. So 2(n−1) of the
n(2n−1) pairs change type. ∎

*Proof of (b).* Weights are 2-subsets {a<b} of [n+1] (e_a + e_b), types
|S∩T| ∈ {0,1}. Ideals of the 2 × (n−1) rectangle are (x₁ ≥ x₂) row
lengths, ↔ {n−x₁, n+1−x₂}; rowmotion (the ideal generated by the minimal
elements of the complement, not containing the old ideal) gives
R{a,b} = {a−1, b−1} for a ≥ 2, b ≥ a+2; R{a,a+1} = {a−1, n+1} for a ≥ 2;
R{1,b} = {b−2, b−1} for b ≥ 3; R{1,2} = {n, n+1}. With ρ the rotation
i ↦ i−1 (mod n+1), a Coxeter element and an isometry, R = ρ∘φ where φ
fixes every 2-subset outside T = {{a,a+1}: 2≤a≤n} ∪ {{1,b}: 2≤b≤n+1} and
permutes T: {a,a+1} ↦ {1,a}, {1,b} ↦ {b−1,b} (b ≥ 3), {1,2} ↦ {1,n+1}.
κ(R) = κ(φ). Pairs (S ∈ T, G ∉ T) that change type: 2(n−2)² + 2(n−3)
(counted per S: for {a,a+1} the generic G ∋ a+1, for {1,b} the generic
G ∋ b−1, for {1,2} the G containing exactly one of 2, n+1). Pairs inside
T: 4n−5 of the (n−2) + 2(n−1) + C(n,2) intersecting pairs stay
intersecting, so (n−1)(n−2) pairs change. Total changed D(n) = 3n² − 9n
+ 4, out of C(C(n+1,2), 2). ∎

Corollary [obs, not claimed]: on A_n ω₂ the rotation ρ agrees with R on
the C(n,2) − (n−1) generic subsets, so a(R) ≥ C(n,2) − (n−1).

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AR0:** the brief is sha-locked.
- **AR1 (Lemma data, all 42 cases of SM-055):** R(λ) = w₀λ; the bottom has
  exactly one cover p₀ = w₀λ + α_{k*} and R(w₀λ) = p₀; ⟨λ,λ⟩ − ⟨λ, w₀λ⟩ =
  c_k = the multiplicity of colour k in P, with the values listed in
  Theorem 1's proof.
- **AR2 (Theorem 1 on the data):** c_k = 1 ⟺ P chain ⟺ R ∈ W, all 42
  cases; on chains R equals the product of the simple reflections in
  order.
- **AR3 (Theorem 2 on the data):** for every case with h even: the
  principal orbit is (P_{<j}) of length h; ⟨w(j), w(j+1)⟩ = ⟨λ,λ⟩ − s_j
  with s_r = c_k; the extended rank sequence is (h/2)-periodic ⟺
  R^{h/2} ∈ W (as computed in SM-055), and the periodic cases are exactly
  the chains with h even and D₃..D₇ ω₁ (+ A₃ ω₂, D₄ ω₃/ω₄); the rank
  sequences of the rectangle, the shifted staircase, E₆, E₇ are as stated.
- **AR4 (the vector formula):** for n = 3..9, R on D_n ω₁ is the stated
  cycle, and R^{n−1} equals e_i ↦ −e_{n−i}, e_n ↦ (−1)^{n−1}e_n on every
  weight, with the stated sign-change count.
- **AR5 (Theorem 3 on the data):** for n = 3..9 the explicit R on
  2-subsets equals the machine's R under {a,b} ↔ e_a + e_b; κ(A_n ω₂)
  = 1 − (3n²−9n+4)/C(C(n+1,2),2) and κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1))
  exactly (fractions), n = 3..9 — beyond SM-055's range at n = 8, 9.
- **AR6 [obs]:** a(R) ≥ C(n,2) − (n−1) on A_n ω₂, n = 3..8, with equality
  recorded where it holds.
- **AR7 (REGISTERED GUESS, resolvable INVERTED):** on A_n ω₃ the changed-
  pair count D₃(n) := (1 − κ)·C(C(n+1,3),2), computed for n = 5..10, is a
  polynomial in n of degree 4 (the degree-4 interpolant through n = 5..9
  predicts n = 10 exactly).

## Machinery

The `Minuscule` class of `verify_stone_aq_rush_shi_defect.py` VERBATIM
(weights, lattice, P, R, Coxeter elements, W enumeration where |W| ≤
400,000); ranks of P by longest chain from the minimum; exact rationals.
Own cache `_stone_ar_cache/witnesses_ar.json`. Outputs:
`verify_stone_ar_nonlinearity_theorems.py`, `.log`,
`STONE_AR_NONLINEARITY_THEOREMS.md` (the proofs above, with the checks).
Runtime: minutes (A₁₀ ω₃ has 165 weights, 13,530 pairs; no W
enumeration above 400,000).

## Discipline

Compute, never assert: the proofs are [P] and every step they use is
re-checked on the data as [C]; the classification of minuscule weights,
the rank structure of P, and Rush–Shi are cited, not claimed. Registered
guess AR7 resolvable INVERTED at equal prominence. Not RH/GRH. Rule 3.
Merkabit-side content; no PSL(2,7) enters.
