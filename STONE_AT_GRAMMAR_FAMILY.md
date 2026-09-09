# STONE AT — THE SHARED GRAMMAR ACROSS THE MINUSCULE FAMILY

**Stenberg side · with Claude · 2026-09-09. Brief
`BRIEF_STONE_AT_GRAMMAR_FAMILY.md` sha-locked 3f6f47b7… BEFORE code;
amendment `AMENDMENT_STONE_AT_2026-09-09.md` (b3b7b482…) locked before
the run, correcting one clause of AT4. Verifier
`verify_stone_at_grammar_family.py`, log: 7 PASS + 4 FAIL — AT2 and AT3
registered guesses INVERTED informatively, AT1 a clause of the brief
wrong (the chain centralizer is ⟨c⟩ of order h, as SM-055 said, not W),
AT4 as written wrong on five self-dual boards (three named in the
amendment, two more covered by its formula); the post-reveal AT2b, AT2c,
AT2d labelled and PASS; first run stopped on an instrumentation slip
(tuple as fancy index), log kept as `_FIRSTRUN.log`. 101 s. Machine:
Stone AQ's class verbatim; W enumerated in full for all 42 cases (E₇:
2,903,040). Own cache `_stone_at_cache/table_at.json`. Registry row
SM-058. Merkabit-side mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "grammar", "instant", "share" label W, its
R-conjugates and their intersections. Four registered items failed and
are reported at the same size as the seven that passed; the post-reveal
statements are labelled as such and are not the registered claims.

## 1. One paragraph

SM-057 found that on the E₇ board the symmetry two instants share,
I_k = W ∩ R^k W R^{−k}, is trivial except at the half-turn. This stone
asked whether that is a law of the family and whether I_k is the
centralizer C_W(R^k). **The registered guess I_k = C_W(R^k) is INVERTED
as a universal law and CONFIRMED exactly, for every k, on 21 of the 23
boards where no power of rowmotion is a Weyl element** — every middle
representation of A_n (n = 4..7), the D₆ and D₇ half-spins, E₆ and E₇.
It fails exactly where SM-056 says a power of R is linear (the chains,
where I_k = W while C_W(c^k) is small; the D_n vector representations,
where |I_k| follows gcd(k, n−1) and exceeds the centralizer), and on one
board it did not predict: the D₅ half-spin, where I_k is strictly larger
than the centralizer at the half-turn and its neighbours (8 against 4,
2 against 1) with no linear power of R in sight. The second registered
guess, the predicted table, was INVERTED at the half-turn: the lone
survivor there is not "−1 when −1 ∈ W and nothing otherwise" but **the
longest element w₀ on every rich board**, and the post-reveal check
shows why: **w₀ reverses rowmotion, w₀ R w₀ = R^{−1}, on every one of the
42 boards** (w₀ acts as −σ with σ the diagram automorphism, an
antiautomorphism of the minuscule lattice), so it commutes with the
half-turn and is a Weyl element. E₇'s ι of SM-057 is the special case
w₀ = −1.

## 2. Bars

| bar | content | outcome |
|---|---|---|
| AT0, AT0b | brief and amendment locked | PASS |
| AT1 | C_W(R^k) ⊆ I_k everywhere [P]; and \|C_W(R)\| = \|W\| on chains, 2 on vectors, 1 elsewhere | **FAIL** on the clause: on chains \|C_W(R)\| = h (⟨c⟩), as SM-055 recorded; the inclusion holds on all 42 cases; the vector and rich values as stated |
| AT2 (guess) | I_k = C_W(R^k) as sets, all cases, all k | **FAIL — INVERTED**: true on 21 rich boards, false on the 12 chains, the 7 vector cases, and the 2 D₅ half-spins |
| AT3 (guess) | the predicted table | **FAIL — INVERTED**: at k = h/2 the rich boards have 2 survivors even when −1 ∉ W (A₅, A₇, E₆, D₇ spin); vector boards have \|I_k\| ≥ h, not 2; D₅/D₆ spinors 8/4 at the half-turn |
| AT3b | E₇: SM-057 re-derived (1, …, 2 at k = 9, …, 1) | PASS |
| AT2b (post-reveal) | I_k = C_W(R^k) exactly on every board with no linear power of R, except the D₅ half-spins | PASS (23 rich boards, 2 exceptions) |
| AT2c (post-reveal) | w₀ ∈ W, w₀(top) = bottom, and w₀ R w₀ = R^{−1} on all 42 boards; hence w₀ commutes with R^{h/2} | PASS |
| AT2d (post-reveal) | half-turn survivors = {1, w₀} on every rich even board except the D₅, D₆ half-spins (D₆: 4 incl. w₀ = −1; D₅: 8 incl. w₀) | PASS (13 boards) |
| AT4 | as written: −1 ∉ W ⇒ antipode not a permutation | **FAIL** on A₃ ω₂, A₅ ω₃, A₇ ω₄ (amendment) and D₅ ω₁, D₇ ω₁ (covered by the amended formula, not named) |
| AT4b (amended) | antipode is a permutation iff λ self-dual; then ι R ι = R^{−1}; ι ∈ W iff −1 ∈ W | PASS |
| AT3c [obs] | vector family: \|I_k\| by gcd(k, n−1) | recorded |

## 3. The table (\|I_k\| for k = 1..h−1, with \|C_W(R^k)\| beneath where they differ)

| board | h | \|I_k\| | \|C_W(R^k)\| |
|---|---|---|---|
| A_n ω₁, ω_n | n+1 | \|W\| every k | C_W(c^k): 3,3 / 4,8,4 / 5⁴ / 6,18,48,18,6 / 7⁶ / 8,32,8,384,8,32,8 |
| A₃ ω₂ (= D₃ ω₁) | 4 | 4, 24, 4 | 2, 4, 2 |
| A₄ ω₂ | 5 | 1,1,1,1 | equal |
| A₅ ω₂, ω₃ | 6 | 1,1,2,1,1 | equal |
| A₆ ω₂..ω₅ | 7 | 1⁶ | equal |
| A₇ ω₂..ω₆ | 8 | 1,1,1,2,1,1,1 | equal |
| D₄ ω₁, ω₃, ω₄ | 6 | 6, 6, 192, 6, 6 | 2, 6, 16, 6, 2 |
| D₅ ω₁ | 8 | 8, 32, 8, 1920, 8, 32, 8 | 2, 8, 2, 32, 2, 8, 2 |
| D₅ ω₄, ω₅ | 8 | 1, 1, 2, 8, 2, 1, 1 | 1, 1, 1, 4, 1, 1, 1 |
| D₆ ω₁ | 10 | 10⁴, 23040, 10⁴ | 2, 10, 2, 10, 128, 10, 2, 10, 2 |
| D₆ ω₅, ω₆ | 10 | 1⁴, 4, 1⁴ | equal |
| D₇ ω₁ | 12 | 12, 72, 384, 72, 12, 322560, 12, 72, 384, 72, 12 | 2, 12, 16, 72, 2, 384, 2, 72, 16, 12, 2 |
| D₇ ω₆, ω₇ | 12 | 1⁵, 2, 1⁵ | equal |
| E₆ ω₁, ω₆ | 12 | 1⁵, 2, 1⁵ | equal |
| E₇ ω₇ | 18 | 1⁸, 2, 1⁸ | equal |

## 4. What was learned

- **The law and its scope.** On a minuscule board with no linear power
  of rowmotion, the symmetry two instants share is exactly the symmetry
  that commutes with the time between them — with one exception, the
  D₅ half-spin, which we do not explain and record. Where a power of R
  is linear the shared grammar is larger than the centralizer, and on
  the vector boards its order follows gcd(k, n−1) [obs].
- **The longest element is the universal half-turn survivor.** w₀
  reverses rowmotion on every board. This is a clean statement, likely
  provable in one line from w₀ = −σ (the antipode is an antiautomorphism
  of the weight lattice; σ is an automorphism commuting with R), and it
  is what SM-057's "ι survives the half-turn" really was.
- **The E₇ board is not special here.** Every rich board behaves as E₇
  does: nothing survives but the identity, and w₀ at the half-turn.
  What is special about E₇ in the family is only what SM-055/056 said:
  it is the furthest from linear.
- **The D₅ half-spin is the one surprise** of the stone and the natural
  next question: what are the six extra half-turn survivors, and the one
  extra at k = 3 and 5 (an involution of type 2⁶1⁴)?

## 5. Not claimed

No proof of the law on the rich boards (it is a computation on 21 of
them); no proof that w₀ reverses rowmotion beyond the 42 checks, though
the argument is short; nothing about the D₅ anomaly beyond the counts
and cycle types in the log; nothing about non-simply-laced boards.

## 6. Synthesis line

The symmetry two instants share is the symmetry that commutes with the
time between them — wherever time is genuinely non-linear; and the one
thing that always survives the half-turn is the longest word, because it
is the one Weyl element that runs the clock backwards.
