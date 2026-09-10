# BRIEF — STONE AZ: THE DOUBLED CLOCK — THE VECTOR BOARDS' SHARED GRAMMAR IS THE CENTRALIZER OF R^{2k}

**Staged 2026-09-10 on Selina's "stone az, do that before we seal".
Locked before code (`BRIEF_STONE_AZ_LOCK.sha256`). No new exploration:
the hand work below was done from the sealed record (SM-058 Stone AT's
table, SM-062's [obs] on the five non-linear antipodes, SM-063 Stone AY's
AY10/AY10c/AY10d) before this brief was written. Deviations = dated
AMENDMENT; post-reveal changes are findings. Merkabit-side mathematics.
Registry row SM-064.**

## Question

Stone AY found that on A₃ω₂ and the odd D_n vector boards (D₅ω₁, D₇ω₁)
some elements of the shared grammar I_k have transports R^{−k}gR^k that
are conjugate to g in no Weyl group tried — not in W(D_n), not in the
stabilizer W(B_n) of the antipodal pairing, and not by the antipode. What
are these transports, and why is the shared grammar on the vector
boards what SM-058 measured (the "gcd(k, n−1) pattern")?

## What was derived by hand (proved here, before code)

Notation as in Stone AY: X the board, W ≤ Sym(X), R the clock,
I_k = {g ∈ W : R^{−k}gR^k ∈ W}, C_k = C_W(R^k), the transport
φ_k(g) = R^{−k}gR^k. The D_n vector board: X = {±e_i}, 2n points,
W = W(D_n) = signed permutations with an even number of sign changes;
the clock is R = ρσ with ρ the (2n−2)-cycle e₁→e₂→…→e_{n−1}→−e_{n−1}→…
→−e₁ and σ = (e_n −e_n), so h = 2n−2 and R^{h/2} is the signed
permutation e_i ↦ −e_{n−i} (i < n), e_n ↦ (−1)^{n−1}e_n (SM-056). The
antipode ι = −1 is a permutation of X, central in W(B_n) ⊇ W(D_n), and
reverses the clock: ιρι = ρ⁻¹, ισι = σ, so ιRι = R⁻¹ (SM-062's [obs]
for the five boards, now by hand for the vectors).

**Lemma C (the doubled clock).** Let ι ∈ Sym(X) be an involution that
centralizes W and reverses R. Then I_k ⊆ C_W(R^{2k}) for every k.
*Proof.* g ∈ I_k, h = R^{−k}gR^k ∈ W. Then ιhι = (ιR^{−k}ι)(ιgι)(ιR^kι)
= R^k g R^{−k}; but ιhι = h since h ∈ W. So R^k g R^{−k} = R^{−k} g R^k,
i.e. R^{2k}g = gR^{2k}. ∎
It applies on every board with −1 ∈ W (ι = w₀, central, reverses R by
SM-059) and on the five self-dual boards whose antipode is not a Weyl
element (A₃ω₂, A₅ω₃, A₇ω₄, D₅ω₁, D₇ω₁; SM-062).

**Lemma D (the vector boards: equality).** On the D_n vector board
(n ≥ 3; D₃ = A₃ω₂), I_k = C_W(R^{2k}) for every k.
*Proof.* ⊆ is Lemma C. ⊇: let g ∈ C_W(R^{2k}) and h = R^{−k}gR^k. Then
ιhι = R^k g R^{−k} = R^k(R^{−2k}gR^{2k})R^{−k} = h, so h commutes with ι,
i.e. h lies in the centralizer of the fixed-point-free involution ι in
Sym(2n), which is the stabilizer of the antipodal pairing, W(B_n). The
sign of h as a permutation of the 2n points equals the sign of g (they
are conjugate in Sym(2n)), which is +1: a positive j-cycle of a signed
permutation is two j-cycles on X (even), a negative j-cycle is one
2j-cycle (odd), so the sign on X is (−1)^{number of negative cycles},
and W(D_n) = W(B_n) ∩ Alt(2n). Hence h ∈ W(D_n) and g ∈ I_k. ∎
Consequences: I_k = I_{−k}; φ_k is an automorphism of the group
C_W(R^{2k}); |I_k| = |C_W(ρ^{2k})| depends on k only through
gcd(2k, 2n−2) = 2·gcd(k, n−1) — SM-058's "gcd pattern" on the D_n
vectors, now a theorem, and the reason its guess I_k = C_k failed there
(C_W(R^{2k}) ⊋ C_W(R^k) off the half-turn).

**Lemma E (what a transport can change).** On the vector boards the
transport preserves the unsigned cycle type on X and the sign; in terms
of signed cycle types (the W(B_n)-classes) the only changes compatible
with both are trades **two negative j-cycles ↔ one positive 2j-cycle**
(each is two 2j-cycles on X, each has sign +1). A transport that makes
such a trade is not conjugation by any element of W(B_n), let alone
W(D_n) — Stone AY's AY10d, explained; and conjugation by the antipode
changes no signed type, so AY10c was doomed.

**D₃ by hand.** Six points ±e₁, ±e₂, ±e₃; W(D₃) ≅ S₄; R: e₁→e₂→−e₂→−e₁,
e₃↔−e₃; R² = s_{e₁+e₂} (e₁ ↦ −e₂, e₂ ↦ −e₁), C_W(R) = {1, R²}.
I₁ = C_W(R²) = {1, s_{e₁−e₂}, s_{e₁+e₂}, s_{e₁−e₂}s_{e₁+e₂}} = W(D₂), the
Klein four-group of the coordinates 1, 2; the transport fixes 1 and R²
and swaps the reflection s_{e₁−e₂} = (12) with the double flip
s_{e₁−e₂}s_{e₁+e₂} = (−1 on e₁, e₂): a positive 2-cycle traded for two
negative 1-cycles. In S₄ these are a transposition and a double
transposition: different classes, so 2 of the 4 transports are non-inner
(Stone AY's count), and φ₁ is the outer automorphism of the Klein group
swapping two of its involutions.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AZ0:** the brief is sha-locked.
- **AZ1 (Lemma C, [P] + check):** on the eleven boards with a W-central
  reverser — D₄ω₁/ω₃/ω₄, D₆ω₁/ω₅/ω₆, A₃ω₂, A₅ω₃, A₇ω₄, D₅ω₁, D₇ω₁ from
  the 42, and the B₄ spinor — the antipode is a permutation of the board
  that centralizes W and reverses R, and I_k ⊆ C_W(R^{2k}) at every lag.
  (E₇: I₉ = {1, ι} ⊆ C_W(R^{18}) = W and I_k = 1 otherwise, from SM-057/
  058; not re-run.)
- **AZ2 (Lemma D, [P] + check):** on the D_n vector boards n = 3..7 (in
  e-coordinates) I_k = C_W(R^{2k}) as sets at every lag; for every
  g ∈ C_W(R^{2k}) the transport lies in the pairing stabilizer and has
  even sign; the orders reproduce SM-058's table (D₅: 8, 32, 8, 1920, …;
  D₇: 12, 72, 384, 72, 12, 322560, …; D₄: 6, 6, 192, 6, 6; D₆: 10 ×4,
  23040, 10 ×4; D₃: 4, 24, 4).
- **AZ3 (Lemma E, REGISTERED GUESS on the counts):** on the D_n vectors,
  for every g ∈ I_k and every lag, φ_k(g) has g's unsigned cycle type and
  sign, and its signed cycle type differs from g's only by trades of two
  negative j-cycles for one positive 2j-cycle (either direction); g is
  W-inner if and only if the signed types agree (guess: the split
  W(D_n)-classes — all cycles positive of even length — never separate
  g from φ_k(g) when the types agree). Recorded: which j occur at which
  lags; the count of non-inner elements per board and lag reproduces
  Stone AY's (D₃: 2 of 4 at lags 1, 3; D₅: 4 of 8 at lags 1, 3, 5, 7 and
  18 of 32 at lags 2, 6; D₇: 6 of 12 at lags 1, 5, 7, 11, 252 of 384 at
  lags 3, 9, 0 at lags 2, 4, 8, 10; D₄, D₆: 0 everywhere).
- **AZ4 (D₃ by hand):** I₁ = W(D₂) as listed; φ₁ swaps s_{e₁−e₂} and the
  double flip, fixes R² = s_{e₁+e₂}.
- **AZ5 (REGISTERED GUESS, resolvable INVERTED):** (a) for n odd, at
  every lag k coprime to n − 1, exactly half of I_k is W-inner and the
  inner half is a subgroup of index 2 in I_k (which subgroup: recorded;
  if it is not a subgroup the guess is INVERTED and the set is recorded);
  (b) for n even every element is inner at every lag, realised by
  exactly two Weyl elements (Stone AY's count re-seen), and both of them
  lie in C_W(R^{2k}) (guess; the pair is recorded either way).
- **AZ6 [obs]:** the groups C_W(R^{2k}) on the vectors: order, abelian
  or not, exponent, and whether φ_k is inner in Aut — recorded, no guess.
- **AZ7 [obs] (the B₃ spinor, for the record):** its lag-3 transports are
  conjugation by R³ ∈ W(D₄) (SM-060 AV5c, SM-063 AY10d); it has −1 ∈ W and
  Lemma C applies: I₃ ⊆ C_W(R⁶) = W, vacuous. One line, no computation.

## Machinery

Stone AV's e-coordinate board machine VERBATIM (`board`, `B_spin`,
`comp`, `pinv`, `ppow`, `closure`, `orbits`, `ctype`, `signed_perm`, `IC`),
with a new four-line vector-board builder `D_vec(n)` (weights ±e_i,
roots e_i − e_{i+1} and e_{n−1} + e_n) — the only new machine, printed in
the log; Stone AQ's `Minuscule` and Stone AT's `enumerate_W_np`/`pow_arr`/
`inv_arr` VERBATIM for the 42-family boards of AZ1; the antipode as in
Stone AT (from `M.idx`). Membership by row bytes only. Signed cycle types
read off the action on the weights ±e_i. Own cache
`_stone_az_cache/witnesses_az.json`. Outputs: `verify_stone_az_doubled_clock.py`,
`.log`, `STONE_AZ_DOUBLED_CLOCK.md`. Runtime: a few minutes (D₇ and
A₇ω₄ are the largest).

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact rationals in the boards; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "clock", "transport", "trade" are labels;
nothing here is about a lepton. Stone AY's Lemma A stays false; nothing
below uses it.
