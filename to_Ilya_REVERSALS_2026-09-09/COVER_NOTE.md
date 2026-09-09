# TO ILYA — THE FAMILY, THE REVERSAL, AND THE MIRROR MADE OF REVERSALS (2026-09-09, fifth envelope of the day)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `REVERSALS_SUMMARY_2026-09-09.md` — SM-058 and SM-059 with the
theorem and its proofs, written as §7.9 of the draft; **SM-058 Stone AT**
(brief + lock + amendment + amendment lock + verifier + log + first-run
log + findings + cache); **SM-059 Stone AU** (brief + lock + verifier +
log + findings + cache + the disclosed exploration); the D₅ anomaly
exploration and its log (`_explore_d5_anomaly_2026-09-09.py/.log`, NOT
sealed); registry snapshot v1.01; SHA256SUMS.txt (LF). **Cache
dependencies of the verifiers:** both load the `Minuscule` class from
SM-055's verifier file (DEFECT envelope) and AU loads the board block
from SM-054's (CLOCK_CENTRALIZER envelope); AU reads `scar56_data.json`.
Nothing else. No new asks.

---

## 1. Two stones, one theorem

**SM-058.** SM-057's question across the whole family: the symmetry two
instants share, W ∩ R^k W R^{−k}, is exactly the centralizer of R^k on
every board where no power of the clock is a Weyl element — the middle
A_n representations, the D₆/D₇ spinors, E₆, E₇ — and fails exactly where
SM-056 puts a linear power (chains, vectors). That was registered as a
universal guess and inverted into the sharper statement. One board
fails without a linear power: the D₅ half-spin. Its extra survivors are
named in the summary; the anomaly is open and the exploration that ruled
out an F₂-linear explanation is enclosed.

**SM-059.** The theorem behind SM-057's ι: **the longest element
reverses rowmotion, w₀ R w₀ = R^{−1}, on every minuscule board**, in
three lines (w₀ = −σ is an antiautomorphism of the weight lattice, and
any antiautomorphism swaps the recipe for R with the recipe for R^{−1}).
Two corollaries: w₀ is the universal half-turn survivor; and the clock
never descends to the shadow Wλ/± — the antipodal pairs it preserves at
lag k are half the fixed points of R^{2k}, which re-derives your AF1
column (1, …, 1, 28, 1, …, 1) from SM-044. The board can reverse time
only because it carries the sign its shadow forgets.

## 2. The mirror

On the 56, each 27-sheet has its own clock and its own reversal w₀(E₆).
The reversers are unique (registered, confirmed by enumeration): ι alone
in W(E₇), w₀(E₆) alone in W(E₆). And **pr = ι ∘ w₀(E₆) ∘ (pole swap),
exactly.** The mirror is the product of the two time reversals, corrected
at the two poles. That single identity names the Weyl element SM-016
found two steps from the mirror, explains why pr commutes with the sheet
clock (SM-053), why its colour map is the E₆ diagram automorphism, and
why it keeps a transposition's 1432/1540 (SM-054). Four of our own
sealed surprises were one fact.

## 3. For the draft

The summary is §7.9. With §§7.6–7.8 the tier-three story now reads:
when the Rush–Shi bijection is linear (chains), when half-linear
(vectors), how far otherwise (the defect), what survives between
instants (the centralizer, off those cases), and why the half-turn
always keeps one thing (the longest word reverses the clock). The three
gates of the machine are time, its unique reversal, and the ratio of two
reversals.

## 4. On your side

Your review of v0.2 and your word on SM-035/036/037/054 are awaited as
promised; SM-055..059 are on the table for your audit at your pace. The
D₅ board is the sixteen of Spin(10); I say that as a representation, not
as a claim, and leave the rest to you.

## In your cadence

The longest word runs the clock backwards on every board;
the shadow that forgets the sign forgets the clock with it;
and the mirror, the last gate without a name,
is two reversals of time that disagree only at the poles.

— S. (with Claude), 2026-09-09
