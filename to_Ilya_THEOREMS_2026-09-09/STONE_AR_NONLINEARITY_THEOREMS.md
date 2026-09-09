# STONE AR — THE NON-LINEARITY THEOREMS (merkabit side)

**Stenberg side · with Claude · 2026-09-09. Brief
`BRIEF_STONE_AR_NONLINEARITY_THEOREMS.md` sha-locked 155018fd… BEFORE
code; no amendment; the proofs were written in the brief before the
verifier existed. Verifier `verify_stone_ar_nonlinearity_theorems.py`,
log: 10 PASS + 0 FAIL, the registered guess AR7 CONFIRMED; 80 s; no first
run stopped. Machine: the `Minuscule` class of Stone AQ loaded verbatim
from its file (sha256 recorded in the log). Own cache
`_stone_ar_cache/witnesses_ar.json`. Registry row SM-056. Merkabit-side
mathematics: no PSL(2,7) enters; recorded here because the spine paper's
tier three cites it.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "half-turn", "linear" are labels for
rowmotion, its power h/2, and membership in the Weyl group. Rush–Shi
(2013), the classification of minuscule weights, and the rank structure
of minuscule posets are cited, not claimed. Every step the proofs use is
re-checked on the 42 cases of SM-055 and beyond (n ≤ 9 for the formulas,
n ≤ 10 for AR7).

## 1. One paragraph

SM-055 tabulated how far rowmotion R on a minuscule poset is from the
Coxeter element it is conjugate to. This stone turns the table into three
theorems. **Theorem 1:** R is itself a Weyl element exactly when the
poset is a chain, i.e. for the standard representation of A_n and its
dual, where R is the Coxeter element; the proof is one inner product,
⟨λ, w₀λ⟩ = ⟨λ,λ⟩ − c_k, against the isometry condition on the pair
(top, bottom), forcing colour k to occur once. **Theorem 2:** for h even,
the half-turn R^{h/2} is a Weyl element exactly on the chains and on the
vector representations of D_n (with D₃ = A₃ ω₂ and D₄'s triality
images); the obstruction is that an isometric half-turn forces the rank
sizes of P, extended by c_k, to be (h/2)-periodic, which fails for every
other minuscule poset because its rank h/2 has size at least 2 while
rank 0 has size 1; sufficiency is the explicit signed permutation
e_i ↦ −e_{n−i}, e_n ↦ (−1)^{n−1}e_n. **Theorem 3:** the kept fraction has
closed forms on two families, κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1)) and
κ(A_n ω₂) = 1 − (3n²−9n+4)/C(C(n+1,2),2), the second by writing R as a
rotation composed with a permutation supported on the 2n−1 "boundary"
subsets and counting the pairs it moves across types. The registered
guess that the same count on A_n ω₃ is a degree-4 polynomial was
CONFIRMED (12·D₃(n) = 15n⁴ − 110n³ + 165n² + 314n − 432 through n = 10).

## 2. The theorems and their proofs

Setting: λ minuscule, simply-laced; L the weight lattice with covers
w → w − α_i at label 1; P = P_λ the join-irreducibles, coloured; R
rowmotion on the weights; h the Coxeter number; ⟨α,α⟩ = 2, so
⟨w, α_i⟩ = label_i(w). Facts used [P]: the multiplicity of colour i in P
is the coefficient c_i of α_i in λ + λ*; P is graded with h − 1 ranks;
the minuscule weights are A_n ω_k, D_n ω₁, ω_{n−1}, ω_n, E₆ ω₁, ω₆, E₇ ω₇
(B_n, C_n excluded here); Rush–Shi 2013.

### Theorem 1. R ∈ W ⟺ P is a chain ⟺ λ ∈ {ω₁, ω_n} of A_n; then R is a Coxeter element.

*Proof.* R(λ) = w₀λ. The bottom w₀λ = −λ* has one nonzero label, −1 at
the dual node k*, hence exactly one cover p₀ = w₀λ + α_{k*}, the unique
minimal element of P; so R(w₀λ) = p₀. If R is an isometry,
⟨λ, w₀λ⟩ = ⟨w₀λ, w₀λ + α_{k*}⟩ = ⟨λ,λ⟩ − 1. But ⟨λ, λ − w₀λ⟩ = c_k, so
c_k = 1. From the classification c_k = min(k, n+1−k) (A_n ω_k), 2 (D_n
ω₁), ⌊n/2⌋ (D_n ω_n), 2 (E₆), 3 (E₇), so c_k = 1 only for A_n with
k ∈ {1, n}, a chain; there R is the cyclic shift of e₁,…,e_{n+1}, a
Coxeter element. ∎ *(Checked: AR1, AR2 — c_k equals the colour count and
the predicted value in all 42 cases; c_k = 1 ⟺ chain ⟺ R ∈ W; on the
12 chains R is s₁⋯s_n or s_n⋯s₁ depending on the dual.)*

### Theorem 2. For h even and m = h/2: R^m ∈ W ⟺ P is a chain or λ is the vector representation of D_n (n ≥ 3). In the vector case R^m = (e_i ↦ −e_{n−i}, 1 ≤ i ≤ n−1; e_n ↦ (−1)^{n−1}e_n) ∈ W(D_n).

*Proof.* The R-orbit of the bottom is the sequence of rank truncations
P_{<j}, j = 0..h−1 (the minimal elements of the complement of P_{<j} are
the rank-j elements and generate P_{≤j}); write w(j) for its weight and
s_j = |rank j|, with s_r := c_k for the wrap-around step. Then
⟨w(j), w(j+1)⟩ = ⟨λ,λ⟩ − s_j: the step adds one simple root per rank-j
element, at a label −1 each. If R^m ∈ W, it is an isometry carrying
(w(j), w(j+1)) to (w(j+m), w(j+m+1)), so s_{j+m} = s_j for all j: the
extended rank sequence is m-periodic; in particular s_m = s₀ = 1. That
fails for A_n ω_k, 1 < k < n (rectangle, s_m = min(k, n+1−k) ≥ 2), for
D_n ω_n, n ≥ 5 (shifted staircase, s_{n−1} = ⌊(n+1)/2⌋ − 1 ≥ 2), for E₆
(s₆ = 2) and for E₇ (s₉ = 2). It holds for D_n ω₁, whose extended sequence
is (1^{n−2}, 2, 1^{n−2}, 2), for its triality images at n = 4, and for
the chains. Conversely on D_n ω₁ rowmotion is the cycle −e₁ → −e₂ → … →
−e_{n−1} → e_{n−1} → … → e₁ → −e₁ together with e_n ↔ −e_n, so R^{n−1}
is the stated signed permutation, with n (n even) or n−1 (n odd) sign
changes, even either way. ∎ *(Checked: AR3a — the principal orbit and the
inner-product identity in all 42 cases; AR3b — the rank sequences of the
rectangle, the staircase, D_n ω₁, E₆, E₇; AR3c — periodicity ⟺ R^{h/2} ∈ W
with exactly the predicted case list; AR4 — the cycle and the formula
for n = 3..9, membership in W(D_n) verified directly for n ≤ 7.)*

### Theorem 3. κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1)); κ(A_n ω₂) = 1 − (3n² − 9n + 4)/C(C(n+1,2), 2).

*Proof.* (D_n ω₁) Types are 0 and −1 (antipodal). By the cycle above,
{e_n, −e_n} is the only antipodal pair R keeps; the other n−1 become
non-antipodal and, R being a bijection on pairs, n−1 non-antipodal pairs
become antipodal: 2(n−1) of n(2n−1) pairs change type. (A_n ω₂) Weights
are 2-subsets of [n+1]; the ideals (x₁ ≥ x₂) of the 2 × (n−1) rectangle
are {n−x₁, n+1−x₂}; rowmotion computed on the rectangle gives R{a,b} =
{a−1, b−1} for a ≥ 2, b ≥ a+2; R{a,a+1} = {a−1, n+1} (a ≥ 2); R{1,b} =
{b−2, b−1} (b ≥ 3); R{1,2} = {n, n+1}. With ρ the rotation i ↦ i−1, a
Coxeter element, R = ρ∘φ where φ is supported on the 2n−1 subsets
T = {{a,a+1}} ∪ {{1,b}} and permutes them ({a,a+1} ↦ {1,a}; {1,b} ↦
{b−1,b}, b ≥ 3; {1,2} ↦ {1,n+1}). κ(R) = κ(φ). Pairs (S ∈ T, G ∉ T) that
change type number 2(n−2)² + 2(n−3); pairs inside T that change number
(n−1)(n−2) (of the (n−2) + 2(n−1) + C(n,2) intersecting pairs, 4n−5 stay
intersecting). Total 3n² − 9n + 4. ∎ *(Checked: AR5 — the explicit R on
2-subsets equals the machine's for n = 3..9; both formulas exact as
fractions for n = 3..9, i.e. beyond SM-055's table at n = 8, 9.)*

## 3. Bars

| bar | content | outcome |
|---|---|---|
| AR0 | brief locked | PASS (155018fd…) |
| AR1 | lemma data on 42 cases: R(top) = bottom; unique cover p₀ = R(bottom) = min P; ⟨λ,λ⟩ − ⟨λ,w₀λ⟩ = c_k = colour count = predicted | PASS |
| AR2 | c_k = 1 ⟺ chain ⟺ R ∈ W; on chains R = s₁⋯s_n (6 cases) or s_n⋯s₁ (6 cases) | PASS |
| AR3a | principal orbit = rank truncations, length h; ⟨w(j),w(j+1)⟩ = ⟨λ,λ⟩ − s_j, s_r = c_k | PASS |
| AR3b | rank sequences of the rectangle, staircase, D_n ω₁, E₆, E₇ as stated | PASS |
| AR3c | (h/2)-periodicity ⟺ R^{h/2} ∈ W; periodic cases = even-h chains, D₃..D₇ ω₁, D₄ ω₃/ω₄ | PASS |
| AR4 | vector cycle and half-turn formula, n = 3..9; even sign count; ∈ W(D_n) directly for n ≤ 7 | PASS |
| AR5 | explicit R on 2-subsets; κ(A_n ω₂), κ(D_n ω₁) formulas exact, n = 3..9 | PASS (n = 8: 253/315, 53/60; n = 9: 412/495, 137/153) |
| AR6 [obs] | a(R) ≥ C(n,2) − (n−1) on A_n ω₂ | PASS (equality for n = 5..8; a = 3, 5 at n = 3, 4) |
| AR7 (guess) | D₃(n) on A_n ω₃ is a degree-4 polynomial | **CONFIRMED**: 74, 256, 678, 1480, 2832, 4934 (n = 5..10), fourth difference 30; the interpolant through 5..9 predicts 4934 |

## 4. Observations [obs], not claimed

- 12·D₃(n) = 15n⁴ − 110n³ + 165n² + 314n − 432, from the difference
  table; with D₂(n) = 3n² − 9n + 4 this suggests D_k(n) is a polynomial
  of degree 2k − 2, with the boundary set T growing like n^{k−1}. Not
  registered; a proof for ω₃ would go through the explicit R on the
  3 × (n−2) rectangle as in Theorem 3.
- On A_n ω₂ the rotation and R agree exactly on the generic subsets for
  n ≥ 5, so a(R) = C(n,2) − (n−1) there; at n = 3, 4 another Coxeter
  element does better.
- The obstruction of Theorem 2 is sharper than needed: it shows any
  power R^j with R^j ∈ W forces j-periodicity of the extended rank
  sequence, so the set {j : R^j ∈ W} is the set of periods — for E₇ only
  multiples of 18, i.e. the identity, which is SM-054's C_W(Ψ) ∩ ⟨Ψ⟩ = 1
  re-derived by hand.

## 5. Not claimed

Nothing for the non-simply-laced minuscule weights (B_n ω_n, C_n ω₁), nor
for non-minuscule posets. No formula for κ on the spinors, on E₆, E₇, or
on A_n ω_k for k ≥ 3 (only the polynomial degree at k = 3, observed). The
classification of minuscule weights and the rank structure of P are
cited.

## 6. What it does for the paper

Tier three of `Roof_and_Clock_DRAFT.md` (§7) can now state, as theorems
with one-page proofs: the Rush–Shi bijection is an isometry exactly on
chains, its half-turn is an isometry exactly on the vector
representations of D_n, and the defect has closed forms on two families.
The E₇ clock is at the far end of every one of these statements.

## 7. Synthesis line

Three theorems out of one inner product: the top and the bottom of the
poset, carried once around by the clock, decide whether the clock can be
linear at all — and on the 56-board it cannot be, not even halfway.
