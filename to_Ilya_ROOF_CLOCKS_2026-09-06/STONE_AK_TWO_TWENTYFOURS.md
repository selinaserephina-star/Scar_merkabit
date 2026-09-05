# STONE AK — THE TWO TWENTY-FOURS

**Stenberg side · with Claude · 2026-09-06. Brief
`BRIEF_STONE_AK_TWO_TWENTYFOURS.md` sha-locked 8920105d… BEFORE code; no
amendment. Verifier `verify_stone_ak_two_twentyfours.py`, log: 14 PASS,
0 FAIL on the sealed run. On the first run AK1a reported FAIL although the
printed data met the registered guess exactly: the check keyed the two
order-8 classes by their size, both 1,512, and the second overwrote the
first — an instrumentation collision, corrected post-reveal (keyed by
class index); that log is kept as
`verify_stone_ak_two_twentyfours_FIRSTRUN.log`. About 6 minutes (two
centralizer closures of 110,592 elements). Machinery: Stone AA stages 0–2
VERBATIM; SM-045/047/048 helpers verbatim; sealed caches READ-ONLY. Own
cache `_stone_ak_cache/`. Registry row SM-049.**

## 0. Discipline

Not RH/GRH. Rule 3: "twenty-four", "still point", "turn" are labels; the
mathematics is conjugacy classes and centralizers, exact.

## 1. One paragraph

The order-24 elements of the twisted coset — the roof's maximal twisted
order — are exactly two conjugacy classes, one per cycle type, each of
21,772,800 elements, one eighth of the coset apiece. Their centralizers
are as small as they can be, C_Ω(e) = ⟨e³⟩ of order 8 for both, found
through the fibre over the twelfth power: that involution's class has
1,575 elements with centralizer of order 110,592, enumerated with a
transversal and closed by Schreier generators, and the elements of it
commuting with e are exactly the eight powers of e³. One hundred sampled
elements of each type were each carried into the fibre and conjugated
onto the representative — 100 and 100, exactly. The still point supplies
both classes cleanly: its 3,024 elements of order 8 form two G₂(2)-classes
of 1,512, and each class turns, by Φ, into one order-24 type. And both
twelfth powers lie in the same involution class as the eighteen's ninth
power (the class of 1,575 with 24 fixed points per block): the three
maximal-order twisted elements of the roof share their involution. The
twisted coset is now exactly accounted for at orders 18 (1/6) and 24
(1/8 + 1/8), five twelfths of it, against SM-039's sampled 41.5 %; the
order-21 density 14.27 % sampled sits on 1/7, the value if the
centralizer of Φ·g₇ is just ⟨g₇⟩ — a prediction for a later stone.

## 2. The still point's eights (AK1)

| G₂(2)-class of order 8 | size | Φ·g₈ cycle type on 360 |
|---|---|---|
| class 0 | 1,512 | {24: 12, 12: 3, 6: 5, 3: 2} |
| class 1 | 1,512 | {24: 12, 12: 5, 6: 1, 3: 2} |

Registered guess (two classes of 1,512, one type each, different):
CONFIRMED.

## 3. The centralizers and classes (AK2, AK3)

| type | class of e¹² | C_Ω(e¹²) | C_Ω(e) | class of e | sample |
|---|---|---|---|---|---|
| {24:12, 12:3, 6:5, 3:2} | 1,575 | 110,592 | ⟨e³⟩, order 8 | 21,772,800 = 1/8 | 100/100 conjugate |
| {24:12, 12:5, 6:1, 3:2} | 1,575 | 110,592 | ⟨e³⟩, order 8 | 21,772,800 = 1/8 | 100/100 conjugate |

Method: e′¹² ∈ class(e¹²) by key lookup; u = transversal element;
u⁻¹ e′ u has twelfth power e¹²; some h ∈ C_Ω(e¹²) conjugates it onto e.

## 4. [obs]

- Both e¹² lie in the Ω-class of (Φ·c̄)⁹ (1,575 elements; 24 fixed points
  on each block): the eighteen and the two twenty-fours share one
  involution class.
- Densities in hand: 18 → 1/6; 24 → 1/8 + 1/8; together 5/12 = 0.4167
  (SM-039 sampled 0.4146). Order 21: sampled 0.1427, predicted 1/7 =
  0.1429 if C_Ω(Φ·g₇) = ⟨g₇⟩ — not tested (no involution to use as fibre;
  a later stone).

## 5. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AK0a | Φ = cache; G₂(2) on 360 | PASS |
| AK1a | two order-8 classes of 1,512, one type each (guess) | PASS (first run: key collision, log kept) |
| AK2a | C_Ω(e) = ⟨e³⟩, order 8, both types; classes 1/8 each | PASS |
| AK3a | 100 + 100 sampled, all conjugate to their representative | PASS |
| AK4, AK5 | involution classes; densities | [obs] |

## 6. Grades

[C] every class size, centralizer and per-element conjugacy; [P] the
fibre argument (SM-047) and the coset argument; [obs] the shared
involution class, the densities, the order-21 prediction. "Two classes" is
exact on the sample (200 elements) and bounded on the population.

## 7. Not claimed

Nothing about order 21, 12, 9, 6 or 3 twisted classes beyond the
recorded densities; no ATLAS names; nothing about why the two order-8
classes of G₂(2) are the two types beyond the computed map.

## 8. Synthesis line

The roof's three maximal twisted clocks — one eighteen, two twenty-fours
— are each rigid (centralizer = own powers), each one class, and they
share one involution; the still point cannot make the eighteen but makes
both twenty-fours by hand, one from each of its two kinds of eight: what
SM-039 sampled as "the roof's number 24" is now two exact classes with a
provenance.
