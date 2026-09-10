# STONE AY — THE D₅ ANOMALY BY HAND: THE HALF-TURN IS A WEYL ELEMENT ON ONE ORBIT

**Stenberg side · with Claude · 2026-09-10. Brief
`BRIEF_STONE_AY_D5_BY_HAND.md` sha-locked bc815042… BEFORE code, no new
exploration (the hand work is in the brief). Verifier
`verify_stone_ay_d5_by_hand.py`, log: 20 PASS + 5 FAIL — AY10 and
AY10c/AY10d guesses INVERTED, AY2 a convention (the machine's clock is
the hand's inverse), AY9b the auditor's slip (the lag-5 survivor
misnamed); one error in the brief's own mathematics (Lemma A's proof)
found by the machine and reported below at full size. Labelled
post-reveal blocks AY2-b, AY9b-b, AY1-b, AY10b, AY10c, AY10d; the first
run (which hung on an impossible set cover caused by that error) kept as
`_FIRSTRUN.log`. 85 seconds without AY10d, 250 with it. Machines: Stone
AV's e-coordinate boards, Stone AQ's `Minuscule`, Stone AT's BFS, all
VERBATIM; `_stone_at_cache/table_at.json` read-only. Own cache
`_stone_ay_cache/witnesses_ay.json`. Registry row SM-063. Merkabit-side
mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "anomaly", "correction", "agreement", "phase" are
labels; nothing here is about a lepton. The brief's Lemma A was stated
as proved and is false as stated: that is the auditor's error, and it
stands in the table beside the twenty passes.

## 1. One paragraph

The anomaly of SM-058, located by SM-060 on the sixteen vertices of the
4-cube under the hyperoctahedral group W(B₄) with the spinor clock R of
order 8, has a mechanism, and it fits in a sentence: **the half-turn R⁴
is a Weyl element on one of the clock's two orbits.** On the orbit O₂
(the one not containing the highest weight) R⁴ coincides with
−τ = (e₂e₃)·(−e₁,−e₂,−e₃), an element of its own centralizer C₄; on the
other orbit O₁ it coincides with no Weyl element at all. Because O₂
affinely spans F₂⁴, a Weyl element is determined by what it does on O₂;
so for any Weyl element g preserving O₂, the transported element
R⁻⁴gR⁴ is again a Weyl element exactly when it equals τgτ — and that
holds for the eight elements of the Weyl centralizer of the *correction*
c = (−τ)R⁴, an involution that is the identity on O₂ and a fixed-point-
free involution on O₁. Those eight are the shared grammar I₄; the four
that commute with c but not with τ are the extras of SM-058/060. Every
one of Stone AV's recorded facts about I₄ — the dihedral group of order
8, the four extras as two reflections and a signed 4-cycle with its
inverse, the half-turn's permutation of them — is now derived by hand
(H1–H7 in the brief, all confirmed): the transport is conjugation by τ,
so the half-turn swaps the two reflections and inverts the 4-cycles, and
an extra commutes with the half-turn up to the antipode. The same
mechanism (Lemma B) accounts for the D₅ lag-3 survivor with the nearest
Weyl element w₃ (unique at distance 7, its agreement set of nine points
determining W(D₅)): the survivor commutes with the correction R³w₃⁻¹, and
its lag-5 partner is its transport. Across the family the picture is a
dichotomy, not a theorem: on 83 of the 98 anomalous (board, lag) pairs a
single Weyl element realises the transport, and on the other 15 some
transports leave their Weyl conjugacy class outright — on the B₃ spinor
they are inner in the overgroup W(D₄) (Stone AV's reading), on A₃ω₂ and
the odd D_n vectors they are inner in no group tried. Never does a pair
need two corrections.

## 2. The two lemmas, as they stand after the run

Notation: X the board, W ≤ Sym(X), R the clock, I_k = {g ∈ W :
R^{−k}gR^k ∈ W}, C_k = C_W(R^k), the *transport* g ↦ R^{−k}gR^k on I_k;
for w ∈ W the *correction* c = R^k w⁻¹ and its agreement set Fix(c).

**Lemma A′ (corrected).** ⋃_{w∈W} C_W(R^k w⁻¹) ⊆ I_k, with equality if
and only if every transport R^{−k}gR^k (g ∈ I_k) is W-conjugate to g.
*The brief's Lemma A claimed equality outright; its proof read "R^{−k}gR^k
∈ W" as "R^{−k}gR^k = w⁻¹gw for some w ∈ W", which is only the converse.*
Measured: equality holds on B₄ and D₅ at every lag (AY1) and fails on
the B₃ spinor at lag 3 (8 of the 16 elements of I₃ have transports in no
W-class of theirs), on A₃ω₂ and on the odd D_n vectors (AY1-b).

**Lemma B (stands; its proof did not use Lemma A).** If Fix(c) has
trivial pointwise stabilizer in W, then I_k ∩ Stab_W(Fix(c)) = C_W(c),
and there the transport is conjugation by w.

## 3. The 4-cube by hand (H1–H7, all confirmed)

| hand fact | machine |
|---|---|
| the clock in sets of negative coordinates: O₁: ∅→{4}→{3}→{2,4}→{1,3}→{1,2,4}→{1,2,3}→{1,2,3,4}; O₂: {1}→{3,4}→{2}→{1,4}→{2,3}→{1,3,4}→{1,2}→{2,3,4} | exactly the inverse (the machine grows ideals from the lowest weight): AY2 FAIL as registered, AY2-b; phases read along the hand's direction |
| H1: R⁴ = −τ on O₂; on O₁ no affine map | AY3: −τ the unique nearest (distance 8), its agreement set = O₂; the next best agree on 6; max agreement on O₁ is 4 of 8 |
| H2: O₂ affinely spans, so its pointwise stabilizer is trivial | AY4a |
| H3: I₄ = C_W(c), c = (−τ)R⁴, Fix c = O₂, c of type 2⁴1⁸ | AY4b |
| H4: Stab_W(O₁) = 16 listed affine maps → D₈ ⊂ S₄ (stabilizer of {14\|23}), kernel ±1; I₄ = preimage of V₄ | AY5a, AY5b, AY5c |
| H5: transport = τ-conjugation; E1↔E4, E2↔E3 = E2⁻¹; E2² = −1; [E1,R⁴] = −1 | AY6a, AY6b (Stone AV's AV6b map reproduced and explained) |
| H6: 16 Weyl elements swap the orbits, e.g. (e₂e₃)(−e₁); none in I₄ | AY7 |
| H7: C₄ acts on each orbit's binary phase by XOR translations {000,111,001,110} on O₁, {000,111,011,100} on O₂; R⁴ = XOR 100 | AY8 (the extras are translations on neither orbit) |

The four Weyl elements realising the transport on the 4-cube are the
coset (−τ)·C_W(I₄) = {(−e₁,−e₃,−e₂,+e₄), (−e₁,+e₃,+e₂,+e₄),
(+e₁,−e₃,−e₂,−e₄), (+e₁,+e₃,+e₂,−e₄)}.

## 4. Bars

| bar | content | outcome |
|---|---|---|
| AY0 | brief locked | PASS (bc815042…) |
| AY1 | union of correction-centralizers = I_k on B₄ and D₅, all lags | PASS (as a measured fact; see AY1-b) |
| AY2 (guess) | the hand clock as written | **FAIL** — the machine's R is the hand's R⁻¹ (convention) |
| AY2-b (post-reveal) | exactly the inverse; phases read along the hand's direction | PASS |
| AY2b | O₁, O₂ are the two free orbits | PASS |
| AY3 (guess) | −τ unique nearest, agreement = O₂; none on all of O₁ | PASS |
| AY4a, AY4b | Lemma B on the 4-cube: O₂ determining; I₄ = C_W(c) | PASS, PASS |
| AY5a, b, c (guess) | Stab_W(O₁) the sixteen; I₄ the eight; the extras named | PASS ×3 |
| AY6a, b | transport = τ-conjugation; E1↔E4, E2↔E3 = E2⁻¹, [E1,R⁴] = −1 | PASS, PASS |
| AY7 | swappers: 16, e.g. (e₂e₃)(−e₁); none in I₄ | PASS |
| AY8 (guess) | the binary phases | PASS |
| AY9 (guess) | D₅ lag 3: w₃ unique at 7, nine points determine, p ∈ C_W(R³w₃⁻¹) = I₃, transport = conj by w₃ | PASS — CONFIRMED |
| AY9b | "the same at lag 5" with p | **FAIL** — the auditor's slip: the lag-5 survivor is R⁻³pR³ = (e₁→e₃, e₂→−e₅, e₃→e₁, e₅→−e₂) |
| AY9b-b (post-reveal) | with the transported p: all of Lemma B holds at lag 5 | PASS |
| AY9c | D₅ lag 4 with −τ in five coordinates: Fix = O₂'s image, determining, I₄ = C_W(c) | PASS |
| AY10a | [P] SM-058's (\|I_k\|, \|C_k\|) reproduced on all 21 anomalous boards | PASS |
| AY10 (guess) | one Weyl element realises the transport on every anomalous pair | **FAIL — INVERTED**: 83 of 98 pairs yes; B₃ lag 3, A₃ω₂ lags 1/3, D₅ω₁ lags 1,2,3,5,6,7, D₇ω₁ odd lags: no |
| AY1-b (post-reveal) | the brief's Lemma A is wrong as written; every one of the 15 failures has transports outside their W-classes | PASS (records the error) |
| AY10b (post-reveal, [obs]) | where all transports are inner but no single w: two corrections | PASS vacuously — no such pair exists |
| AY10c (post-reveal guess) | the non-inner transports are antipode-conjugation | **FAIL** — 0 of them, on every pair |
| AY10d (post-reveal guess) | the non-inner transports are inner in the overgroup (W(D₄) for B₃; the pairing stabilizer W(B_n) for A₃ω₂ = D₃ and the odd D_n vectors) | **FAIL** — true for B₃ (all inner in W(D₄), 4 single elements); false for A₃ω₂ and D₅/D₇ vectors (the same elements uncarried in W(B_n)) |
| AY11 [obs] | the anomaly is on B₄ where −1 is central: not tied to D₅'s non-central reverser | recorded, by hand |

## 5. The family, as observed [obs]

Where a single Weyl element realises the transport, the count of such
elements is a coset of C_W(I_k): 1 on the chains and at the half-turns
where R^{h/2} ∈ W (the element is R^k itself), 2 on the D₄ and D₆
vectors at every anomalous lag and on D₇ at lags 2 and 10, 4 on the
4-cube, 4 and 32 on the D₅ half-spin (lags 4; 3 and 5). Where none does,
the failure is always of the same kind — some element's transport is in
no W-conjugacy class of it — and never a covering problem. The
non-inner cases sort by board: B₃ (inner one Weyl group up), and the
self-dual boards whose antipode is not a Weyl element (A₃ω₂, D₅ω₁,
D₇ω₁ — the list of SM-062's [obs]) at every odd lag and at lags 2, 6
on D₅, where the transports are inner neither in W nor in the stabilizer
of the antipodal pairing. The even D_n vectors (−1 ∈ W) never fail.

## 6. Not claimed

No proof that O₂ must be the orbit on which the half-turn is a Weyl
element on other boards (on the D₆ and D₇ half-spins, where I = C, the
question is void by AY10a's table). No account of the non-inner
transports on the odd D_n vectors beyond the two negatives above. The
binary-phase description (H7) is a description of C₄ and R⁴, not of the
extras. Nothing about which group the non-inner transports are inner in.

## 7. Synthesis line

The clock's half-turn on the smallest board keeps a symmetry across it
because, on half of the board, the half-turn is one of the board's own
symmetries — and that half is enough to know a symmetry by. The
anomaly is not an exception to the family's rule; it is the one place
where the clock, for one full orbit, agrees to be a Weyl element.
