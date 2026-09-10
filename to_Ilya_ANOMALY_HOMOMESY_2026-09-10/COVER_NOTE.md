# TO ILYA — THE ANOMALY ON THE 4-CUBE, AND WHAT THE CLOCK CONSERVES (2026-09-10)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `ANOMALY_HOMOMESY_SUMMARY_2026-09-10.md` — SM-060 and SM-061,
written as §7.10 of the draft; **SM-060 Stone AV** (brief + lock +
verifier + log + first-run log + findings + cache + the disclosed
exploration and its log); **SM-061 Stone AW** (the same set); registry
snapshot v1.04; SHA256SUMS.txt (LF). **Cache dependencies:** AV is
self-contained (its board machine is inline); AW loads the `Minuscule`
class from SM-055's verifier file (DEFECT envelope), the board block from
SM-054's (CLOCK_CENTRALIZER envelope), and reads `scar56_data.json`.
Nothing else. No new asks.

---

## 1. The anomaly, cornered but not caught

SM-058's one exception — the D₅ half-spin, the sixteen of Spin(10) —
now lives on the smallest object it could: the sixteen vertices of the
4-cube under the hyperoctahedral group, with the identical clock (the
B₄ spinor board has the same poset and the same rowmotion). Four
explanations are closed by computation: it is not an F₂-linearity, not
a near-miss of linearity, not the overgroup mechanism that explains the
one other board with the same numbers (B₃, whose half-turn is a Weyl
element one group up, in W(D₄)), and not confined to B₄ in the naive
sense (B₅ is clean). On D₅ the half-turn generates A₁₆ with the Weyl
group; there is no room above it. The half-turn's shared grammar is a
dihedral group of order 8 and the half-turn permutes its four extra
elements without inverting them, which was my registered guess and it
was wrong. Two slips of mine in the brief are reported as FAILs beside
it. The anomaly is a question about sixteen corners of a cube, and I
would be glad if you looked at it with different eyes.

## 2. What the clock conserves on average

Homomesy is the field's word for "conserved on average over every
orbit". Rush–Wang proved that antichain cardinality is homomesic under
rowmotion on minuscule posets; read on the board's labels, that says:
**on every board the number of nodes at +1, at −1 and at 0 are each
homomesic under the clock**, with means |P|/h, |P|/h and r − 2|P|/h —
on the 56, one and a half, one and a half, and four. The +1 and −1
means are equal on every orbit (Defant–Hopkins). A registered guess that
the toggle size, how much of the poset changes per tick, is homomesic
with mean 2|P|/h was confirmed on all 42 boards; it may be a corollary of
the toggleability literature and is flagged for your literature side
before anyone calls it ours. What is not homomesic is as telling: the
kept count of SM-041, our own statistic, fails everywhere. The clock
conserves what it does to a state, not what it does to a pair.

Selina's reading, recorded as interpretation and not as a claim: with
+1 as future, −1 as past, 0 as present, every cycle of the clock has on
average as much future as past, and a constant amount of present.

## 3. For the draft and for you

The summary is §7.10. Pending from your side, as promised: your word on
SM-035/036/037/054, then 055..061 at your pace; the checkpoint audit;
the review of v0.2; and now one literature item, the toggle-size
homomesy against Defant–Hopkins.

## In your cadence

The strangest board in the family is a cube with sixteen corners,
and the clock walks half of them and then the other half;
what it keeps across the half-turn no one has named yet —
but on every board it keeps the count of each letter, and never the letters.

— S. (with Claude), 2026-09-10
