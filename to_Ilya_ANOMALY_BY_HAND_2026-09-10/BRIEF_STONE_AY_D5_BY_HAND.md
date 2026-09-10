# BRIEF — STONE AY: THE D₅ ANOMALY BY HAND — THE HALF-TURN IS A WEYL ELEMENT ON ONE ORBIT

**Staged 2026-09-10 on Selina's "do this" (the ranked candidate 1 of
`NEXT_MAP_2026-09-10.md`). Locked before code
(`BRIEF_STONE_AY_LOCK.sha256`). No new free exploration: everything
below was derived by hand from the sealed record (SM-058 Stone AT,
SM-060 Stone AV, its disclosed probes `_explore_d5_probes_2026-09-10.py`
and log) before this brief was written; the machine's role is to check
the hand. Deviations = dated AMENDMENT; post-reveal changes are
findings. Merkabit-side mathematics. Registry row SM-063.**

## Question

SM-060 left the anomaly of SM-058 "computed, not understood": on the
B₄ spinor board (the sixteen vertices of the 4-cube, W = W(B₄) the
hyperoctahedral group of order 384, rowmotion R of order 8 with two free
8-orbits O₁ ∋ λ and O₂), the shared grammar I₄ = W ∩ R⁴WR⁻⁴ has order 8
against the centralizer C₄ = C_W(R⁴) of order 4; and on the D₅ half-spin
(same board, W(D₅) ⊃ W(B₄)) also I₃ = I₅ of order 2 against 1. Four
explanations were closed (not F₂-affine, not near-linear, not the B₃
overgroup mechanism, and the anomaly is not specific to the 4-cube in the
guessed sense). What is the mechanism?

## What was derived by hand (proved here, before code)

Notation. X the board (N points), W ≤ Sym(X), R ∈ Sym(X) the clock,
I_k = {g ∈ W : R^{−k} g R^k ∈ W}, C_k = C_W(R^k). For w ∈ W call
c = R^k w⁻¹ the *correction* of R^k by w (so R^k = c·w) and
Y_w = Fix(c) = {x : R^k x = w x} the *agreement set* of R^k with w.

**Lemma A (the shared grammar is a union of centralizers).**
I_k = ⋃_{w∈W} C_W(R^k w⁻¹).
*Proof.* g ∈ I_k ⟺ R^{−k} g R^k = w⁻¹ g w for some w ∈ W ⟺
g R^k w⁻¹ = R^k w⁻¹ g for some w ∈ W. ∎
So every extra (g ∈ I_k ∖ C_k) commutes with some correction of R^k by a
Weyl element w ≠ 1 with which g does not commute; and on I_k the
*transport* g ↦ R^{−k} g R^k coincides, on C_W(R^k w⁻¹), with
conjugation by w.

**Lemma B (one correction suffices when its agreement set determines).**
Let w ∈ W, c = R^k w⁻¹, Y = Fix(c). If the pointwise stabilizer of Y in
W is trivial (two Weyl elements agreeing on Y are equal), then
I_k ∩ Stab_W(Y) = C_W(c), and on it the transport is conjugation by w.
*Proof.* ⊇ by Lemma A (C_W(c) preserves Fix(c)). ⊆: for g ∈ I_k
preserving Y put h = c⁻¹ g c = w R^{−k} g R^k w⁻¹ ∈ W; for x ∈ Y,
h(x) = c⁻¹(g(x)) = g(x) since g(x) ∈ Y = Fix(c); h and g are in W and
agree on Y, so h = g, i.e. g ∈ C_W(c). ∎

**The 4-cube by hand.** Vertices = sign patterns (±½)⁴, written as the
set S ⊆ {1,2,3,4} of negative coordinates (λ = ∅). The board is
J(δ₄), δ₄ the shifted staircase; the ideal with row lengths
ℓ₁ > ℓ₂ > … is the pattern S = {5 − ℓ_i}. Rowmotion (the ideal generated
by the minimal elements of the complement) computed on all sixteen:

  O₁: ∅ → {4} → {3} → {2,4} → {1,3} → {1,2,4} → {1,2,3} → {1,2,3,4} → ∅
  O₂: {1} → {3,4} → {2} → {1,4} → {2,3} → {1,3,4} → {1,2} → {2,3,4} → {1}

(phases 0..7 from ∅ on O₁ and from {1} on O₂). W(B₄) acts on F₂⁴ (S as
a bit vector) as the affine maps x ↦ πx + v, π ∈ S₄ a coordinate
permutation, v the sign flips. C₄ = {±1, ±τ} with τ = (e₂e₃)·(−e₄),
i.e. x ↦ (23)x + e₄, from Stone AV. Hand facts:

  (H1) R⁴ = −τ on O₂: {1}↔{2,3,4}, {3,4}↔{1,3,4}, {2}↔{1,2},
       {1,4}↔{2,3}. On O₁, R⁴ = ∅↔{1,3}, {4}↔{1,2,4}, {3}↔{1,2,3},
       {2,4}↔{1,2,3,4}, which is the restriction of no affine map
       (it would need π(e₄) = 0111).
  (H2) O₂ affinely spans F₂⁴ (1000 + {1100, 0011, 0001, 1011} spans), so
       the pointwise stabilizer of O₂ in W is trivial: Lemma B applies
       with w = −τ, c = (−τ)R⁴ (= R⁴(−τ), −τ ∈ C₄), Fix(c) = O₂.
  (H3) With AV2b (all of I₄ preserves the orbits): I₄ = C_W(c), and the
       transport g ↦ R⁻⁴ g R⁴ on I₄ is conjugation by τ.
  (H4) Stab_W(O₁) has order 16: v ∈ O₁ and π in a coset of {1,(12)(34)}:
       (1|(12)(34); 0000 or 1111), ((23)|(1342); 0001 or 1110),
       ((14)|(1243); 0010 or 1101), ((14)(23)|(13)(24); 0101 or 1010).
       Its image in S₄ is the dihedral stabilizer D₈ of the pairing
       {14|23}, kernel {±1}. I₄ is the preimage of the Klein four-group
       V = {1,(14),(23),(14)(23)}: C₄ = {(1;0000),(1;1111),((23);0001),
       ((23);1110)} and the four extras E1 = ((14);0010),
       E4 = ((14);1101), E2 = ((14)(23);0101), E3 = ((14)(23);1010),
       which are Stone AV's (e₁↔e₄, −e₃), (e₁↔−e₄, −e₂), the signed
       4-cycle and its inverse. E3 = E2⁻¹, E2² = −1.
  (H5) Conjugation by τ (= the transport, by H3): E1↔E4, E2↔E3 — Stone
       AV's recorded AV6b map exactly; so the half-turn does invert the
       two 4-cycles and swaps the two reflections. The commutator
       [E1, R⁴] = E1·E4 = −1: an extra commutes with the half-turn up to
       the antipode.
  (H6) Weyl elements swapping O₁ and O₂ exist (x ↦ (23)x + e₁, i.e.
       (e₂e₃)·(−e₁)): Stab_W({O₁,O₂}) has order 32; none is in I₄.
  (H7) Phases in binary (p = 4a+2b+c): −1 = XOR 111 on both orbits; τ =
       XOR 001 on O₁ and XOR 011 (= p ↦ 3 − p) on O₂; R⁴ = XOR 100 on
       both. So C₄ acts on each orbit by translations of (ℤ/2)³ — the
       group {000,111,001,110} on O₁, {000,111,011,100} on O₂ — and the
       half-turn's translation 100 lies in the image on O₂ only. That
       is the whole of H1 in one line.

**The mechanism, stated once.** The shared grammar at any lag is the
union of the Weyl centralizers of the corrections R^k w⁻¹ (Lemma A); on
a rich board every correction's centralizer lies in C_k. On the 4-cube
the correction by −τ ∈ C₄ is the identity on a whole clock orbit, that
orbit determines Weyl elements (Lemma B), and the centralizer of that
correction is twice C₄: the half-turn is a Weyl element on one orbit.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **AY0:** the brief is sha-locked.
- **AY1 (Lemma A, numerically):** on B₄ and on D₅ (both boards, all
  lags k = 1..7), ⋃_{w∈W} C_W(R^k w⁻¹) = I_k as sets. [P]
- **AY2 (the hand clock):** the machine's rowmotion on the B₄ board,
  read as sets of negative coordinates, is the two 8-cycles above
  (REGISTERED GUESS: as written, not reversed; if it is the inverse, the
  direction is recorded and every phase below is read backwards).
- **AY3 (H1, REGISTERED GUESS):** R⁴ agrees with −τ exactly on O₂; −τ is
  the unique Weyl element nearest to R⁴ (Hamming distance 8); no other
  Weyl element agrees with R⁴ on all of O₂, and none agrees with it on
  all of O₁.
- **AY4 (H2, Lemma B):** the pointwise stabilizer of O₂ in W(B₄) is
  trivial; I₄ = C_W(c) for c = (−τ)R⁴, Fix(c) = O₂. [P by hand; checked]
- **AY5 (H4, REGISTERED GUESS):** Stab_W(O₁) is the sixteen elements
  listed, I₄ the eight with π ∈ V; C₄ = C_W(c) ∩ C_W(τ).
- **AY6 (H5):** the transport on I₄ equals conjugation by τ; E1↔E4,
  E2↔E3 = E2⁻¹; [E1,R⁴] = −1; E2² = −1.
- **AY7 (H6):** Stab_W({O₁,O₂}) has order 32; (e₂e₃)·(−e₁) swaps the
  orbits; I₄ ∩ (swappers) = ∅.
- **AY8 (H7, REGISTERED GUESS):** the phase translations as listed for
  −1, τ, R⁴ on both orbits; the four extras are not phase translations
  on either orbit.
- **AY9 (D₅ lag 3, REGISTERED GUESS, resolvable INVERTED):** on the D₅
  half-spin the nearest Weyl element w₃ to R³ is unique (distance 7,
  Stone AV), its agreement set Y (9 points) has trivial pointwise
  stabilizer in W(D₅), and the lag-3 survivor p = (e₁e₃)(e₂e₅) lies in
  C_W(R³w₃⁻¹) — so I₃ = C_W(R³w₃⁻¹) = {1, p} by Lemma B, and p's
  transport is conjugation by w₃. If p ∉ C_W(R³w₃⁻¹) the guess is
  INVERTED and the w's that do carry p (Lemma A) are recorded. Same for
  lag 5 by SM-059's reversal, and lag 4 with w = −τ read in D₅
  coordinates (−e₁,−e₃,−e₂,+e₄,−e₅).
- **AY10 (the family, REGISTERED GUESS, resolvable INVERTED):** on every
  board of SM-058's table (from `_stone_at_cache/table_at.json`) and
  every lag with I_k ≠ C_k — the chains, A₃ω₂, the D_n vectors
  (n = 4..7), the D₅ half-spins — and on the B₃ spinor at lag 3, the
  transport g ↦ R^{−k} g R^k on I_k is induced by conjugation by a
  single Weyl element w_k (one correction suffices). Guess: yes,
  everywhere. INVERTED if some board and lag needs two corrections; the
  first such is named.
- **AY11 [obs] (from the map's open question, settled by hand):** the
  anomaly is already on B₄, whose reverser −1 is central; it is not tied
  to D₅'s non-central reverser (SM-062 §7.11.4). No computation.

## Machinery

Stone AV's e-coordinate board machine VERBATIM (`board`, `B_spin`,
`D_half`, `comp`, `pinv`, `ppow`, `closure`, `orbits`, `ctype`,
`signed_perm`, `IC` from `verify_stone_av_d5_anomaly.py`, between its
"e-coordinate board machine" fence and the IC definition); Stone
AQ's `Minuscule` class and Stone AT's `enumerate_W_np`/`pow_arr`/`inv_arr`
VERBATIM for AY10 (W by BFS, membership by row bytes; no isometry
criterion — the SM-062 caveat; all boards there have |W| ≤ 322,560);
the anomalous-lag list from `_stone_at_cache/table_at.json` (dependency
declared). Centralizers and conjugation vectorized in numpy. Own cache
`_stone_ay_cache/witnesses_ay.json`. Outputs:
`verify_stone_ay_d5_by_hand.py`, `.log`, `STONE_AY_D5_BY_HAND.md`.
Runtime: a few minutes (the D₇ vector's W is the largest).

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; exact rationals in the boards; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "anomaly", "correction", "agreement",
"phase" are labels; "the 16 of Spin(10)" is a representation, not a
claim; nothing here is about a lepton.
