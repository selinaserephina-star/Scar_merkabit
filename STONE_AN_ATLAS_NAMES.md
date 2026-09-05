# STONE AN — THE ATLAS NAMES

**Stenberg side · with Claude · 2026-09-06. Brief
`BRIEF_STONE_AN_ATLAS_NAMES.md` sha-locked 4960646b… BEFORE code; no
amendment. Verifier `verify_stone_an_atlas_names.py`. First run: 16 PASS +
1 FAIL (AN3c, an instrumentation error: the square of a twisted element
lies in the other coset Ω·Φ², so it was tested against the wrong classes);
kept as `verify_stone_an_atlas_names_FIRSTRUN.log`. Sealed run (AN3c
tested through e⁴ = e⁻², which lies in Ω·Φ): 17 PASS, 0 FAIL. About 25
minutes. Cited data: the GAP Character Table Library, version 1.3.11
(Thomas Breuer, RWTH Aachen; downloaded with Selina's approval), file
`data/ctoorth2.tbl`, tables "O8+(2)" and "O8+(2).3", origin "ATLAS of
finite groups": the header blocks (centralizer orders, power maps, class
fusion; no character values) are quoted verbatim in `_stone_an_cache/`
with their sha256 (1197f219…, 83703faa…). Machinery for the three
computations: Stone AA stages 0–2 VERBATIM and the SM-045..051 helpers.
Registry row SM-052.**

## 0. Discipline

Not RH/GRH. Rule 3. Cited data is quoted, not retyped; every claim about
it is a computation on the quoted text. The names are derived by stated
rules and graded [obs] where the rule is a convention.

## 1. One paragraph

The fourteen conjugacy classes of the roof's twisted coset (SM-047..051)
are the fourteen outer classes of the published character table of
O₈⁺(2).3, exactly. The count is forced by the published class numbers
alone: O₈⁺(2) has 53 classes, O₈⁺(2).3 has 55, the fusion fixes 14 of the
53 and fuses the other 39 in 13 triples, so each outer coset carries 14
classes. The multiset of (element order, centralizer order) over the
published outer classes is {(3, 36288), (3, 648), (6, 576), (6, 144),
(6, 72), (9, 54), (12, 288), (12, 144), (12, 96), (12, 12), (18, 18),
(21, 21), (24, 24), (24, 24)}, and it equals ours with every centralizer
tripled — as it must, since a twisted element centralizes itself outside
Ω. Every published power-map entry that our fibre computations had
recorded agrees: the eighteen's sixth power is the class of centralizer
5832 = 3·1944, which is O₈⁺(2)'s class 3D — the heart; its ninth power and
the twenty-fours' twelfth powers are 2A (331776 = 3·110592, our
involution class of 1,575); the order-12 class of centralizer 12 and two
of the order-6 classes have their involutions in 2E (9216 = 3·3072, our
class of 56,700); the seven-beat clock's seventh power is the turn; the
nine's cube is the heart. Three entries our stones had not recorded were
computed and agree: the eighteen's cube has Ω-centralizer 216 (the
published inner class 6G, centralizer 648); the order-6 classes' squares
fall as published (the 576- and 144-classes square to turns, the 72-class
into Φ·g₆₇₂'s class); and the two twenty-fours are told apart by their
squares — type A, from the still point's first order-8 class, squares
into the order-12 class of centralizer 288 (our 1/96 class), type B into
the class of centralizer 96 (our 1/32 class). The names follow.

## 2. The count [P cited]

| | classes |
|---|---|
| O₈⁺(2) | 53 |
| O₈⁺(2).3 | 55 = 27 inner + 28 outer |
| triality-fixed classes of O₈⁺(2) | 14: 1A, 2A, 2E, 3D, 3E, 4A, 4B, 4F, 6G, 6N, 7A, 8A, 8B, 12D |
| fused triples | 13 |
| classes per outer coset | 14 (Brauer's permutation lemma) — our census |

## 3. The fourteen classes, named

Two naming conventions are given. "GAP-style" letters the classes of the
O₈⁺(2).3 table in its own order per element order (inner fused classes
counted once); "inherited" keeps O₈⁺(2)'s letters for inner classes and
continues the lettering for the outer ones. The printed ATLAS's own labels
for this extension were not available to us; the identification rests on
(order, centralizer, power maps), which is unambiguous except for the two
twenty-fours, which the squares separate.

| ours (order, |C_Ω|) | published |C_{G.3}| | table pair | GAP-style | inherited | what it is |
|---|---|---|---|---|---|---|
| (3, 12096) | 36288 | 28/29 | 3D/3E | 3F | the turn Φ; also Φ·g₅₆ (the still point's heart, turned) |
| (3, 216) | 648 | 30/31 | 3F/3G | 3G | Φ·g₆₇₂ |
| (6, 192) | 576 | 32/33 | 6G/6H | 6O | the 576-class; e² a turn, e³ in 2A |
| (6, 48) | 144 | 34/35 | 6I/6J | 6P | the 144-class; e² a turn, e³ in 2E |
| (6, 24) | 72 | 36/37 | 6K/6L | 6Q | the 72-class; e² in Φ·g₆₇₂'s class, e³ in 2E |
| (9, 18) | 54 | 38/39 | 9B/9C | 9D | (Φ·c̄)⁻²'s class; e³ = the heart 3D |
| (12, 96) | 288 | 40/41 | 12D/12E | 12H | the 1/96 class = type A's square |
| (12, 48) | 144 | 42/43 | 12F/12G | 12I | the 1/48 class |
| (12, 32) | 96 | 44/45 | 12H/12I | 12J | the 1/32 class = type B's square |
| (12, 4) | 12 | 46/47 | 12J/12K | 12K | the 1/4 class, not from the still point; e⁶ in 2E |
| (18, 6) | 18 | 48/49 | 18A/18B | 18A | Φ·c̄, the roof's eighteen; e⁶ = 3D, e⁹ = 2A, e³ = 6G |
| (21, 7) | 21 | 50/51 | 21A/21B | 21A | Φ·g₇, the seven-beat clock; e⁷ = the turn, e³ = 7A |
| (24, 8) | 24 | 52/53 | 24A/24B | 24A | Φ·g₈ type A {24:12, 12:3, 6:5, 3:2}; e² → 288-class, e³ = 8A or 8B, e¹² = 2A |
| (24, 8) | 24 | 54/55 | 24C/24D | 24B | Φ·g₈ type B {24:12, 12:5, 6:1, 3:2}; e² → 96-class, e¹² = 2A |

Key inner classes, by the fusion: the heart = 3D (1944 in Ω, 5832 in
G.3); the E₈ and D₄ Coxeter hearts = the fused triple 3A/3B/3C (77760),
which is why Φ² carries one onto the other (SM-046); the two involution
classes our fibres used = 2A (110592) and 2E (3072); the eighteen's cube =
6G (216 in Ω); the seven = 7A (centralizer 7 in Ω); the eights = 8A, 8B
(32 in Ω, classes of 5,443,200 — why SM-049 could not enumerate the cube).

## 4. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AN1a | 53 / 55; 13 triples, 14 fixed; 14 per coset | PASS |
| AN2a | the (order, centralizer) multiset equals ours ×3 | PASS |
| AN3a | 16 published power-map entries vs our fibre data | PASS |
| AN3b | |C_Ω((Φ·c̄)³)| = 216 | PASS |
| AN3c | the order-6 squares fall as published | first run FAIL (wrong coset); sealed run PASS |
| AN4a | type A's square: centralizer 96; type B's: 32 | PASS |
| AN4b | the cubes are 8A, 8B (|C_Ω(g₈)| = 32) | PASS |
| AN5 | the names | [obs], by rule |

## 5. Grades

[P cited] everything read from the quoted headers (counts, centralizers,
power maps, fusion); [C] the three computations (216; the squares; the
twenty-fours' squares' centralizers) and the parsing; [obs] the naming
conventions. The identification of our classes with the published ones
is [C + P]: exact on (order, centralizer, power maps).

## 6. Not claimed

The printed ATLAS's labels for O₈⁺(2):3 (not consulted); any character
values (not quoted); anything about the coset Ω·Φ² beyond inversion.

## 7. Synthesis line

Fourteen classes we found by walking the roof are the fourteen the ATLAS
printed in 1985, centralizer for centralizer and power for power — the
census was complete before it was named, and the naming cost one
download and no new computation: what "compute, never assert" buys is
that the lookup confirms rather than informs.
