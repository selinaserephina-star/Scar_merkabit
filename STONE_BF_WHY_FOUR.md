# STONE BF — WHY FOUR: THE COMMUTATION THEOREM

**Stenberg side · with Claude · 2026-09-19. Brief `BRIEF_STONE_BF_WHY_FOUR.md`
locked 03a0ed63… before the clean verifier (honest provenance: found by free
exploration this session, `_explore_bf_witness_2026-09-19.py` + `.log` kept,
not sealed; the brief records the completed proofs). Verifier
`verify_stone_bf_why_four.py`: 8 PASS + 0 FAIL, 3.3 s; the first run is the
clean run (`_FIRSTRUN.log` identical). Registry row SM-070. Merkabit-side
mathematics. Not RH/GRH; Rule 3.**

## The theorem

**Theorem BF.** Let n ≥ 4 be even and w_n = −(e₂e₃)(e₄e₅)…(e_{n−2}e_{n−1})
(negating e₁..e_{n−1}, fixing e_n) on the B_n spinor board. Then w_n commutes
with the half-turn Rⁿ **if and only if n = 4**.

With SM-068's criterion this is the answer to "why the 4-cube": the mechanism
(a Weyl element of this shape agreeing with the half-turn on the middle-band
orbits) is present on every free clock, and its consequence (a shared grammar
larger than the centralizer) needs that element to commute with the
half-turn, which happens only at n = 4.

## The proof, in four steps (all in the brief, all re-checked as computations)

1. **Lemma BF-A — rowmotion in excess coordinates [P; BF1].** Write a weight
   by its plus positions c₁ < … < c_r and put d_k = c_k − k. Then rowmotion is
   d′_{k′} = min({d_k − 1 : k a gap row ≥ k′} ∪ {n − r − 1 if d_r < n − r and
   k′ ≤ r+1}), a gap row being one with d_k > d_{k−1} (d₀ = 0); rows with no
   generator vanish. Checked against the clock on every weight for n = 4..12.
2. **Proposition BF-B — the orbit of λ [P; BF2].** R^{2j}λ = [n] ∖ {n, n−2, …,
   n−2j+2}, R^{2j+1}λ = [n] ∖ {n−1, …, n−2j+1}; ranks 0, n, n−1, n−1, …, 1, 1
   around the clock; for even n the half-turn shifts every rank on this orbit
   by exactly ±n/2. **This proves the hypothesis of SM-066's Lemma BB-B for
   every even n** (SM-066 had verified it at n = 4, SM-067 at 8, SM-069 at 16).
   Checked for n = 3..16.
3. **Proposition BF-C — w_n on the orbit of λ [P; BF3].** w_n preserves the
   orbit of λ, acting on clock positions as i ↦ 2 − i (even i) and i ↦ −i
   (odd i), both of which commute with i ↦ i + n for even n. So w_n commutes
   with the half-turn on the full-height orbit, for every even n. On any
   orbit where the half-turn *is* w_n (a carrying orbit) commutation is
   automatic (Lemma BF-D: wHx = wwx = x = HHx = Hwx). **At n = 4 these two
   orbits are the whole board** — that is why −τ commutes with R⁴.
4. **Proposition BF-E and the witness [P; BF4, BF5].** For even n ≥ 6 the point
   e₂ (a single minus sign at position 2) lies on neither kind of orbit, and
   two explicit half-turn values decide it: H(e₂) = {1, 2} ∪ {5, 7, …, n−1}
   and H({3, n}) = [n] ∖ {4, 6, 7, 9, …, n−1} (at n = 6: {1,2,3,5,6}), each
   by an induction along the orbit in excess coordinates whose every step is
   listed in the brief and re-checked. Since w_n(e₂) = −{3, n} and H commutes
   with −1: 2 ∈ w_n(H e₂) but 2 ∉ H(w_n e₂). ∎

## Bars

| bar | content | outcome |
|---|---|---|
| BF0 | brief locked (03a0ed63…) | PASS |
| BF1 [C] | Lemma BF-A = the clock on all 8,176 weights of n = 4..12 | PASS (0 mismatches) |
| BF2 [C] | Prop. BF-B on n = 3..16: sets, ranks, antipode identity, ±n/2 shift (even n) | PASS |
| BF3 [C] | Prop. BF-C on even n = 4..16: the two reflections, commutation on O₁ | PASS |
| BF4 [C] | Prop. BF-E on even n = 6..16: H(e₂), H({3,n}), and every excess sequence of both inductions | PASS |
| BF5 [C] | Theorem BF on even n = 4..16: w₄ ∈ C₄; e₂ a witness for n ≥ 6 | PASS |
| BF6 [obs, guess] | R³(e_p) = −e_{n−1−p}; the closed form of H(e_p) | PASS (n = 4..16; n = 16 the new instance) |
| BF7 [obs, guess] | odd n = 5..15: the SM-068 shape does not commute | PASS |

Numbers (exact): the non-commuting set {x : w_n H x ≠ H w_n x} has size 0, 24,
148, 736, 3304, 14328, 60076 for n = 4, 6, 8, 10, 12, 14, 16 (BF5); for odd n
= 5..15 the corresponding sizes are 18, 90, 418, 1798, 7554, 31086 (BF7).

## What it closes and what it leaves

Closes: SM-068's sharpened question (why the nearest element commutes only at
n = 4) for the family w_n on even n, and SM-066's remaining input (the ±n/2
shift on the full-height orbit, now a theorem for every even n). Leaves: that
w_n is the *nearest* Weyl element to the half-turn for n > 8 (computed at
n ≤ 8; on B₁₆ it is the carrying element, nearest not computed); that
C_W(w_n⁻¹Rⁿ) = {±1} for every even n ≥ 6 (computed at 6, 8, 16); the closed
form of H(e_p) (BF6) as a theorem; odd n in general (BF7 is a computation).
The obvious next theorem — C_W(Rⁿ) = {±1} for n ≥ 5 — is not attempted here.

## Not claimed

Nothing beyond the statements above; no physical reading. |I₁₆| remains as in
SM-069.

## Synthesis line

The whole exception of §7.12 is now one line of arithmetic: on the 4-cube the
two orbits on which a symmetry cannot help but commute with the half-turn are
the entire board, and from the 6-cube on there is always a third kind of point
— which is the ordinary way a small case is exceptional: not by having more
structure, but by having no room for the generic case to appear.
