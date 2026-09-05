# STONE AL — THE SEVEN-BEAT CLOCK'S CLASS, AND THE TURN'S CENTRALIZER

**Stenberg side · with Claude · 2026-09-06. Brief
`BRIEF_STONE_AL_SEVEN_BEAT_CLASS.md` sha-locked (see
`BRIEF_STONE_AL_LOCK.sha256`) BEFORE code; no amendment. Verifier
`verify_stone_al_seven_beat_class.py`, log: 15 PASS + 2 registered guesses
INVERTED (AL4a, AL4b), with the post-reveal AL4c (labelled) completing
what the inversions opened. The first run (without AL4c) is kept as
`verify_stone_al_seven_beat_class_FIRSTRUN.log`. 9 minutes (four
centralizer closures). Machinery: Stone AA stages 0–2 VERBATIM;
SM-045/047/048 helpers verbatim; sealed caches READ-ONLY. Own cache
`_stone_al_cache/`. Registry row SM-050.**

## 0. Discipline

Not RH/GRH. Rule 3: "seven-beat clock", "turn", "still point" are labels;
the mathematics is centralizers and conjugacy classes, all exact per
element and sample-bounded per population. Two guesses were ours and
wrong; they are recorded first.

## 1. One paragraph

The turn's centralizer in Ω is exactly the still point: the Ω-class of Φ
has 14,400 elements and its Schreier-closed centralizer is G₂(2) as a set
of 12,096 permutations — SM-038's "Fix(τ″) = G₂(2) as far as the machine
reaches" is now a count. That gives the fibre for order 21: (Φ·g₇)⁷ = Φ,
so two order-21 twisted elements with seventh power Φ are conjugate only
by G₂(2). The seven-beat clock's centralizer is ⟨g₇⟩ of order 7 (G₂(2)'s
1,728 elements of order 7 are one class), its class has 24,883,200
elements, exactly one seventh of the coset, and 300 sampled order-21
elements were each transported onto Φ and conjugated onto Φ·g₇ by the
still point: 300 of 300. The order-12 twisted elements inverted both
registered guesses, informatively: a THIRD cycle type {12: 28, 6: 4},
not produced from the still point at all, carries most of the order-12
mass (155 of 200 samples), one class of density 1/4 with centralizer of
order 4; the still point's own type {12: 24, 6: 6, 3: 12} splits into two
classes of densities 1/48 and 1/96 (19 and 6 of 25 samples, each
conjugated exactly to its representative); the type {12: 24, 6: 10, 3: 4}
is one class of density 1/32. Four order-12 classes, densities summing to
exactly 5/16. The coset is now accounted at orders 18, 24, 21 and 12 to
293/336 = 0.8720; the remainder 43/336 = 0.1280 for orders 9, 6 and 3
matches SM-039's sampled 0.1274. The twisted elements of order 3 are
almost never turns: Φ's class is 14,400 elements, 0.008 % of the coset,
against a sampled 0.5 %, and every sampled one has Φ's cycle type
{3: 120}.

## 2. The turn and the seven-beat clock (AL1–AL3)

| quantity | value |
|---|---|
| Ω-class of Φ | 14,400 = |Ω| / |G₂(2)| |
| C_Ω(Φ) | = G₂(2) as a set (12,096) |
| G₂(2)'s elements of order 7 | 1,728, one G₂(2)-class |
| C_Ω(Φ·g₇) | ⟨g₇⟩, order 7 |
| class of Φ·g₇ | 24,883,200 = 1/7 of the coset (sampled 0.1417 here, 0.1427 in SM-039) |
| 300 sampled order-21 elements | 300 with seventh power in class(Φ); 300 conjugate to Φ·g₇ |

## 3. The order-12 twisted elements (AL4, AL4c)

| cycle type on 360 | from the still point? | class of e⁶ | C_Ω(e⁶) | C_Ω(e) | density | sampled / conjugate |
|---|---|---|---|---|---|---|
| {12: 24, 6: 10, 3: 4} | yes (Φ·g₄, 378) | 1,575 | 110,592 | 32 | 1/32 | 20 / 20 |
| {12: 28, 6: 4} | **no** | 56,700 | 3,072 | 4 | 1/4 | 155 / 155 |
| {12: 24, 6: 6, 3: 12}, first class | yes (Φ·g₄ 378, Φ·g₁₂ 3,024) | 1,575 | 110,592 | 48 | 1/48 | 25 / 19 |
| {12: 24, 6: 6, 3: 12}, second class | | 1,575 | 110,592 | 96 | 1/96 | 6 / 6 (post-reveal) |

Sum of the four densities: 1/32 + 1/4 + 1/48 + 1/96 = 5/16 = 0.3125
(SM-039 sampled 0.3153; this stone's 200-in-706 sample 0.2833). The
registered guesses — that the sampled types are exactly the still point's,
and one class per type — were both INVERTED; the post-reveal AL4c shows
the split type is exactly two classes on the sample.

## 4. The coset accounted (AL5, [obs])

| twisted order | exact share | source |
|---|---|---|
| 18 | 1/6 | SM-047 |
| 24 | 1/8 + 1/8 | SM-049 |
| 21 | 1/7 | this stone |
| 12 | 5/16 (four classes) | this stone |
| sum | 293/336 = 0.8720 | |
| remainder (9, 6, 3) | 43/336 = 0.1280 | SM-039 sampled 0.0554 + 0.0673 + 0.0047 = 0.1274 |

(The log's "[obs] densities in hand" line labels the order-12 share with
the pre-AL4c sum 0.3021; the total 0.8720 printed beside it already uses
the four-class sum. Corrected here, not in the log.)

## 5. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AL0a | Φ = cache; G₂(2) on 360 | PASS |
| AL1a | class of Φ = 14,400; C_Ω(Φ) = G₂(2) | PASS |
| AL2a | C_Ω(Φ·g₇) = ⟨g₇⟩; class 1/7 | PASS |
| AL3a | 300/300 order-21 elements conjugate to Φ·g₇ | PASS |
| AL4a | order-12 types = the still point's (guess) | **INVERTED** — a third type, 1/4 of the coset |
| AL4b | one class per type (guess) | **INVERTED** — the still point's type splits |
| AL4c | post-reveal: the split type is two classes | PASS (finding) |
| AL5 | the coset accounted; order-3 twisted elements | [obs] |

## 6. Grades

[C] every class count, centralizer and per-element conjugacy; [P] the
fibre argument over Φ (SM-047's lemma with p = e⁷) and the coset
argument; [obs] the densities as population statements (sample-bounded),
the order-3 observation. The 5/16 is a sum of four exact fractions; that
it matches SM-039's sample is a check, not a claim.

## 7. Not claimed

No structural names for the centralizers of orders 32, 48, 96, 4; no
classification of orders 9, 6, 3; nothing about why the still point misses
the dominant order-12 type; no count of order-12 classes beyond the four
seen in a 200-sample (a fifth of density under about 1 % would have
escaped with probability ~ 0.1).

## 8. Synthesis line

The still point is the turn's whole centralizer, exactly, and from it the
seven-beat clock is one rigid class — while the roof's commonest twelve
is a beat the still point cannot make at all: G₂(2) holds the clocks that
matter to the descent (7, 21, the heart, the cube) and not the roof's
own background rhythm; SM-035's seven-beat clock and SM-039's turn are now
one exact object with one exact class.
