# STONE AW — HOMOMESY ON THE BOARDS: WHAT THE CLOCK CONSERVES ON AVERAGE

**Stenberg side · with Claude · 2026-09-10. Brief
`BRIEF_STONE_AW_HOMOMESY.md` sha-locked dbf5759f… BEFORE code, the free
exploration `_explore_homomesy_2026-09-10.py` disclosed in it; no
amendment. Verifier `verify_stone_aw_homomesy.py`, log: 6 PASS + 1 FAIL
— AW5 a registered guess INVERTED, AW5b the labelled post-reveal; the
first run (before AW5b was added) kept as `_FIRSTRUN.log`. 4 s.
Machines: Stone AQ's class verbatim (42 boards); the AP board block and
Stone AU's sheet rowmotion verbatim for the 56. Own cache
`_stone_aw_cache/table_aw.json`. Registry row SM-061. Merkabit-side
mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "conserved", "present", "future", "past" are labels;
the results are orbit averages of label counts. Rush–Wang (2015) and
Defant–Hopkins (2021) are cited at first use; the reading of +1/−1/0 as
future/past/present is Selina's, recorded as [I].

## 1. One paragraph

A statistic is homomesic under the clock if its average is the same on
every clock orbit (Propp–Roby). Rush–Wang proved that on minuscule
posets the ideal cardinality and the antichain cardinality are
homomesic under rowmotion, and that the per-colour ideal cardinalities
are; on the weights the latter says every rowmotion orbit has mean
weight zero, which is seen here on all 42 boards. The dictionary of
SM-041 turns the antichain statistic into a label count: a state's
number of +1 labels is the size of its ideal's antichain of maximal
elements, its number of −1 labels is the antichain size of the next
state, and its zeros are the rest. So **the three ternary counts —
+1, −1, 0 — are homomesic on every minuscule board, with means |P|/h,
|P|/h and r − 2|P|/h**: on E₇ each orbit of the clock has on average
1½ labels at +1, 1½ at −1 and 4 at 0; on the D₅ spinor board 1¼, 1¼
and 2½. In Selina's reading: over any full cycle of the clock, the
average amounts of future and past are equal, and the average amount of
present is conserved — on every board, exactly. The registered guess
that the **toggle size**, the number of elements of P that change
between one state and the next, is homomesic with mean 2|P|/h was
CONFIRMED on all 42 boards (possibly a corollary of known toggleability
results; flagged). Three natural non-linear statistics are NOT homomesic
on any non-chain board: the number of distinct colours toggled, the
per-state kept count of SM-041, and the number of lattice elements
below a state. On the 56 the registered guess about the other gates was
INVERTED: under the mirror the ternary counts are not homomesic (a state
and its mirror image differ in label counts), and under the sheet clock
they fail only because the two poles are fixed points; on the two
27-sheets alone they are homomesic with the E₆ means 4/3, 4/3, 10/3,
Rush–Wang on each sheet.

## 2. Bars

| bar | content | outcome |
|---|---|---|
| AW0 | brief locked | PASS (dbf5759f…) |
| AW1 | orbit-mean weight zero on all 42 boards (Rush–Wang file homomesy) | PASS |
| AW2 | #(+1), #(−1), #(0) homomesic on all 42 with means \|P\|/h, \|P\|/h, r − 2\|P\|/h | PASS |
| AW3 (guess) | toggle size \|I Δ R(I)\| homomesic with mean 2\|P\|/h | **CONFIRMED** on all 42 |
| AW4 | #distinct colours toggled, kept count, #lattice elements below: not homomesic on all 30 non-chain boards | PASS |
| AW5 (guess) | on the 56: ternary counts homomesic under Ψ₆ and under pr; kept count under neither; not under pr∘Ψ | **FAIL — INVERTED**: not homomesic under Ψ₆ (poles) nor pr; the rest as guessed |
| AW5b (post-reveal) | on the two sheets alone, ternary E₆-label counts homomesic under Ψ₆ with means 4/3, 4/3, 10/3 | PASS |

## 3. The table (orbit means)

| board | orbits | mean #(+1) = #(−1) = \|P\|/h | mean #(0) | mean toggle size |
|---|---|---|---|---|
| E₇ ω₇ | [18,18,18,2] | 3/2 | 4 | 3 |
| E₆ ω₁ | [12,12,3] | 4/3 | 10/3 | 8/3 |
| D₅ ω₅ | [8,8] | 5/4 | 5/2 | 5/2 |
| D₇ ω₇ | [12⁵,4] | 7/4 | 7/2 | 7/2 |
| A₇ ω₄ | [8⁸,4,2] | 2 | 3 | 4 |
| A₅ ω₂ | [6,6,3] | 4/3 | 7/3 | 8/3 |
| chains A_n ω₁ | [n+1] | n/(n+1) | (n−1)·n/(n+1)… | 2n/(n+1) |

(All 42 in the cache.)

## 4. What was learned

- The ternary structure of the board — the three possible labels at
  each node — has an exact conservation law under the clock: not the
  label at a given node (that is not conserved), but the count of each
  kind, on average over every orbit. And the two non-zero kinds balance
  exactly, which is Defant–Hopkins' 0-mesy of T⁺ − T⁻ seen on the weights.
- The toggle size is the new item of the stone if it is not in the
  literature: how much of P the clock touches per tick is conserved on
  average at 2|P|/h, twice the antichain mean.
- The negatives matter: the kept count of SM-041, our own statistic, is
  not homomesic anywhere. What the clock conserves on average is what it
  does to a state, not what it does to a pair.

## 5. Not claimed

No proof of AW3 beyond the 42 boards; no claim of novelty for AW2 beyond
the dictionary (it is Rush–Wang's antichain homomesy read on labels);
nothing about non-simply-laced boards; nothing physical.

## 6. Synthesis line

Time does not conserve any one label, but it conserves the amount of
each kind: over every cycle of the clock the future and the past are
equal on average and the present is constant — Rush–Wang's antichain
theorem, read in the board's own three letters.
