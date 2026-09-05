# STONE AM — THE COSET COMPLETE

**Stenberg side · with Claude · 2026-09-06. Brief
`BRIEF_STONE_AM_COSET_COMPLETE.md` sha-locked (see
`BRIEF_STONE_AM_LOCK.sha256`) BEFORE code; no amendment. Verifier
`verify_stone_am_coset_complete.py`. First run: 13 PASS + 2 FAIL (AM3a a
registered guess INVERTED; AM4a failed by exactly the duplicate that
inversion produced); kept as `verify_stone_am_coset_complete_FIRSTRUN.log`.
Sealed run: 15 PASS + 1 INVERTED (AM3a); the post-reveal AM3b (labelled) tests what the first run's
arithmetic forced, and AM4a then closes. About 5 minutes. Machinery:
Stone AA stages 0–2 VERBATIM; SM-045/047/048/050 helpers verbatim; sealed
caches READ-ONLY. Own cache `_stone_am_cache/`. Registry row SM-051.**

## 0. Discipline

Not RH/GRH. Rule 3: "turn", "heart", "still point" are labels; the
mathematics is fourteen conjugacy classes, their centralizers, and one
rational identity. The guess about which still-point element gives which
order-3 class was ours and wrong; it is recorded first.

## 1. One paragraph

The twisted coset Ω·Φ of the roof is now completely classified: FOURTEEN
conjugacy classes, whose densities sum to exactly 1. Order 9 is one class
of density 1/18 (centralizer of order 18; every sampled element's cube in
the heart's class; (Φ·c̄)⁻² among them). Order 6 is three classes,
1/192 + 1/24 + 1/48 = 13/192, found through the involution fibre and
assigned exactly for all 150 samples. Order 3 is two classes: the turn's
own, of 14,400 elements, and the class of Φ·g₆₇₂, of 806,400 = |Ω|/216 —
the reverse of the registered guess: it is the still point's order-3
element with the SMALL centralizer in G₂(2) (18) that gives the large
twisted class, while Φ·g₅₆, g₅₆ a heart with centralizer 216 in G₂(2), is
simply a turn: conjugate to Φ. The first run counted the class of Φ·g₅₆
separately, found it had 14,400 elements, and the census overshot 1 by
exactly 1/12,096; since distinct classes are disjoint, that excess forces
Φ·g₅₆ into the turn's class, and the post-reveal membership test confirms
it. All 40 sampled order-3 twisted elements lie in Φ·g₆₇₂'s class; none
is a turn (the turn's class is 0.008 % of the coset).

## 2. The roof's twisted class list [C]

| order | classes | centralizer orders in Ω | share of the coset | source |
|---|---|---|---|---|
| 24 | 2 | 8, 8 | 1/8 + 1/8 | SM-049 |
| 21 | 1 | 7 | 1/7 | SM-050 |
| 18 | 1 | 6 | 1/6 | SM-047 |
| 12 | 4 | 32, 4, 48, 96 | 1/32 + 1/4 + 1/48 + 1/96 = 5/16 | SM-050 |
| 9 | 1 | 18 | 1/18 | this stone |
| 6 | 3 | 192, 24, 48 | 13/192 | this stone |
| 3 | 2 | 12,096 (the turn), 216 | 1/12,096 + 1/216 | this stone |
| **total** | **14** | | **= 1 exactly** (over 12,096: 2016 + 3024 + 1728 + 3780 + 672 + 819 + 1 + 56) | |

Every class is exact: the centralizer of a representative enumerated, the
class size = |Ω| / |centralizer|; "one class per row" is exact on the
samples (100–300 per order) and forced on the population by the sum being
exactly 1 — a fifteenth class of any density would push the total above 1.

## 3. The stages

**AM1, order 9.** 150 sampled elements, all of cycle type {9: 39, 3: 3},
all with cube in the heart's class; transported into the fibre over x and
conjugated by C_Ω(x): one class, centralizer 18, density 1/18 (sampled
0.0571; SM-039 0.0554). Registered guess CONFIRMED.

**AM2, order 6.** 150 sampled elements in two cycle types. {6: 48, 3: 24}:
one class, centralizer 192 (e³ in the involution class of 1,575), 15/15.
{6: 56, 3: 8}: two classes, centralizers 24 and 48 (e³ in the involution
class of 56,700, centralizer 3,072), 85 + 50 of 135. Sum 13/192 = 0.0677
(sampled 0.0692; SM-039 0.0673). Measured, as registered.

**AM3, order 3.** The turn's class: 14,400 (SM-050). The class of Φ·g₆₇₂:
806,400 = |Ω|/216, enumerated (keys only, 85 s). Φ·g₅₆: class of 14,400,
and (AM3b, post-reveal) it IS the turn's class. Samples: 40 of 40 in
Φ·g₆₇₂'s class, 0 turns. The registered guess had the two still-point
classes the other way round; INVERTED, and the census then closes.

**AM4.** Sum of all fourteen densities = 1, exactly (rational
arithmetic). First run: 12097/12096, the duplicate; sealed run: 1.

## 4. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AM0a | replay; class(x), C_Ω(x) | PASS |
| AM1a | order 9: cubes in class(x); one class 1/18 | PASS |
| AM2a | order 6: classes found; all samples assigned | PASS (three classes, 13/192) |
| AM3a | Φ·g₅₆'s class = 806,400, Φ·g₆₇₂ in it; samples in it | **INVERTED** — Φ·g₆₇₂'s class is the 806,400; Φ·g₅₆'s is 14,400 |
| AM3b | post-reveal: Φ·g₅₆ is a turn | PASS (finding) |
| AM4a | all densities sum to exactly 1 | first run: excess 1/12,096 (the duplicate); sealed run: PASS |

## 5. Grades

[C] every class, centralizer, density and per-element conjugacy; [P] the
fibre arguments (SM-047), the coset argument, and the disjointness
argument that closes the count; [obs] none needed — the census is exact.
The sample-boundedness of "one class per row" is superseded by the exact
sum: with the sum at 1 there is no room for another class.

## 6. Not claimed

No ATLAS names (the fourteen classes and their centralizer orders are
computed; matching them to O₈⁺(2):3's character table is a separate,
citable step not taken here); nothing about the coset Ω·Φ² beyond the
inverse map; nothing about why Φ·g₆₇₂ has centralizer 216 while
C_{G₂(2)}(g₆₇₂) = 18.

## 7. Synthesis line

The roof's turned motions are fourteen exact rhythms and no more, and
the census closes on the nose — the still point's heart turns into a
turn, and its other three-element turns into the roof's commonest
three-beat: what SM-039 sampled as seven orders is now fourteen classes
with a proof of completeness that is one line of rational arithmetic.
