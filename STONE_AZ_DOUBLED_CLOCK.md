# STONE AZ — THE DOUBLED CLOCK: THE VECTOR BOARDS' SHARED GRAMMAR IS THE CENTRALIZER OF R^{2k}

**Stenberg side · with Claude · 2026-09-10. Brief
`BRIEF_STONE_AZ_DOUBLED_CLOCK.md` sha-locked 45d75b30… BEFORE code, three
lemmas proved in the brief, no new exploration. Verifier
`verify_stone_az_doubled_clock.py`, log: 11 PASS + 2 FAIL — AZ5b a
registered guess INVERTED (the realising pair for even n is not inside
the doubled centralizer; it is the half-turn and its negative), AZ5c a
post-reveal observation mis-stated for n = 3 (the Klein group has three
cyclic halves; with the transport-stable one, AZ5c-b, it holds). The
first run (a late-bound closure in the signed-type reader,
instrumentation) kept as `_FIRSTRUN.log`. 109 seconds. Machines: Stone
AV's e-coordinate boards, Stone AQ's `Minuscule`, Stone AT's BFS, all
VERBATIM, plus a four-line vector-board builder printed in the log;
`_stone_at_cache/table_at.json` read-only. Own cache
`_stone_az_cache/witnesses_az.json`. Registry row SM-064. Merkabit-side
mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "transport", "trade" are labels; nothing
here is about a lepton. Stone AY's Lemma A stays false; nothing below
uses it.

## 1. One paragraph

Stone AY left one thread loose: on A₃ω₂ and the odd D_n vector boards
some elements of the shared grammar have transports R^{−k}gR^k that are
conjugate to g in no Weyl group tried. This stone closes it by hand.
**Lemma C:** wherever an involution ι centralizes W and reverses the
clock, I_k ⊆ C_W(R^{2k}) — three lines: the transport h is fixed by ι,
so R^kgR^{−k} = R^{−k}gR^k. **Lemma D:** on the D_n vector boards it is
an equality, because the transport of any g commuting with R^{2k}
commutes with the antipode (so lies in the hyperoctahedral group) and
has even sign on the 2n points (so lies in W(D_n)). That is SM-058's
"gcd(k, n−1) pattern" on the vectors as a theorem: |I_k| = |C_W(ρ^{2k})|.
**Lemma E:** a transport keeps the unsigned cycle type and the sign, so
it can change the signed cycle type — the W(B_n)-class — only by trading
two negative j-cycles for one positive 2j-cycle; such a trade is
conjugation by nothing in W(B_n), which is why Stone AY's AY10c and
AY10d failed. On D₃ by hand: I₁ is the Klein group W(D₂) and the
transport swaps the reflection s_{e₁−e₂} with the double flip, a
transposition of S₄ traded for a double transposition. The machine
confirmed all of it exactly, reproduced every non-inner count of Stone
AY, and showed the shape beneath: at every lag coprime to n − 1 the
shared grammar is dihedral of order 2(n−1); the transport keeps its
cyclic half; for n odd it swaps the dihedral group's two reflection
classes (an outer automorphism, realised by no Weyl element), for n even
there is one reflection class and the transport is conjugation by the
half-turn R^{h/2} itself (a Weyl element by SM-056) or its negative.
The parity of n decides because the transport on C_W(R^{2k}) is
conjugation by any odd power of R^k, and h/2 = n − 1 is such an odd
power exactly when n is even.

## 2. The lemmas, as they stand

| lemma | statement | status |
|---|---|---|
| C | ι an involution centralizing W and reversing R ⇒ I_k ⊆ C_W(R^{2k}) | proved; checked on 11 boards, all lags (AZ1) |
| D | D_n vectors (n ≥ 3): I_k = C_W(R^{2k}) | proved; checked D₃..D₇, all lags (AZ2) |
| E | transports keep unsigned type and sign; signed-type changes are trades 2×(j,−) ↔ 1×(2j,+); W-inner ⟺ same signed type | proved (the trades); the iff checked (AZ3a, AZ3b) |

## 3. Bars

| bar | content | outcome |
|---|---|---|
| AZ0 | brief locked | PASS (45d75b30…) |
| AZ1 | Lemma C on A₃ω₂, A₅ω₃, A₇ω₄, D₄ ×3, D₅ω₁, D₆ ×3, D₇ω₁, B₄: antipode centralizes W, reverses R, inclusion at every lag | PASS |
| AZ2 | Lemma D: I_k = C_W(R^{2k}) as sets on D₃..D₇; transports in the pairing stabilizer, even | PASS |
| AZ2b | [P] SM-058's orders reproduced | PASS |
| AZ3a | Lemma E: only trades | PASS |
| AZ3b (guess) | inner ⟺ same signed type | PASS |
| AZ3c (guess) | non-inner counts = Stone AY's (D₃ 2/4; D₅ 4/8 and 18/32; D₇ 6/12 and 252/384; D₄, D₆ none) | PASS; trades by j: only j = 1 at coprime lags, j ≤ 2 on D₅ lag 2, j ≤ 3 on D₇ lag 3 |
| AZ4 | D₃ by hand | PASS |
| AZ5a (guess) | n odd, coprime lags: exactly half inner, a subgroup | PASS |
| AZ5b (guess) | n even: all inner, two realising elements, both in C_W(R^{2k}) | **FAIL — INVERTED** on the last clause: the pair is {R^{h/2}, w₀R^{h/2}} (AZ5d) |
| AZ5c (post-reveal) | dihedral of order 2(n−1) at coprime lags etc. | **FAIL** as first stated — the Klein group (n = 3) has three cyclic halves |
| AZ5c-b (post-reveal) | the same with the transport-stable cyclic half | PASS |
| AZ5d (post-reveal) | realising pair for n even = {R^{h/2}, w₀R^{h/2}} | PASS |
| AZ6 [obs] | the groups C_W(R^{2k}) | recorded (orders, abelian or not, element orders) |
| AZ7 [obs] | B₃: transports by R³ ∈ W(D₄); Lemma C vacuous there | recorded, by hand |

## 4. What was learned

- SM-058's registered guess I_k = C_W(R^k) failed on the D_n vectors
  because the true law there is I_k = C_W(R^{2k}): the shared grammar
  sees the clock at double speed. Off the half-turn C_W(R^{2k}) ⊋
  C_W(R^k), and the gap is the whole anomaly.
- The clock's transport is an automorphism of C_W(R^{2k}) on the
  vectors. It is inner (a Weyl conjugation) exactly when a Weyl element
  is an odd power of R^k, which on the vectors means n even and the
  half-turn. For n odd it is an outer automorphism that trades signed
  cycle types — the reason no Weyl group, not even W(B_n), realises it.
- The B₃ spinor's non-inner transports and the vectors' are different
  animals: B₃'s are inner one Weyl group up (W(D₄) ∋ R³); the vectors'
  are inner nowhere below Sym.

## 5. Not claimed

Nothing about boards without a W-central reverser (the E₆ 27, the
D_odd half-spins, the A_n ω_k with 2k ≠ n + 1): Lemma C does not apply.
No claim that C_W(R^{2k}) ⊆ I_k beyond the vector boards (on A₅ω₃, A₇ω₄
and the D₆ half-spins the inclusion is strict at the half-turn: I = 2 or
4 against C = W). The 4-cube's I₄ = 8 against C_W(R⁸) = 384 is Lemma C
vacuous, not explained by it; that stone is SM-063.

## 6. Synthesis line

On the boards whose only reverser is the antipode, the grammar two
instants share is the grammar the clock's double keeps — and the clock
carries it forward by an automorphism that a Weyl element can copy only
when the half-turn is one of the clock's odd steps.
