# STONE AJ — THE HEART AT THE STILL POINT

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AJ_HEART_AT_STILLPOINT.md` sha-locked 9ae492ed… BEFORE code;
no amendment. Verifier `verify_stone_aj_heart_stillpoint.py`, log: 17
PASS, 0 FAIL. First run stopped in AJ4 on an instrumentation error (the
sealed generators of the vector shadow are permutations of the 240 roots,
reduced by M2_of as in Stone Z; they were passed to the 120-vector
reducer); that log is kept as `verify_stone_aj_heart_stillpoint_FIRSTRUN.log`
and carries AJ0–AJ3 already PASS. 54 s. Machinery: Stone AA stages 0–2
VERBATIM, SM-045/047 helpers verbatim; G₂(2) lifted to 360 points by
closure from four of its elements; sealed caches READ-ONLY. Own cache
`_stone_aj_cache/`. Registry row SM-048.**

## 0. Discipline

Not RH/GRH. Rule 3: "heart", "still point", "turn", "clock" are labels;
the mathematics is orders, conjugacy classes and membership, all exact.

## 1. One paragraph

The still point commutes with the turn — Φ P(g) = P(g) Φ for all 12,096
elements — so Φ·g has order lcm(3, ord g), and the twisted orders that
the still point produces are exactly {3, 6, 12, 21, 24} with the census
multiplicities: no eighteen. By SM-047's one class, the roof clock Φ·c̄ is
conjugate to no Φ·g with g at the still point; but the maximal twisted
order 24 lives there entirely naturally — every one of the 3,024 elements
of order 8 gives an order-24 twisted element, and they split 1,512 / 1,512
between the two sealed order-24 cycle types. The heart, though, IS at the
still point: G₂(2)'s 728 elements of order 3 form two classes, of 56
(fixed dimension 2 on V) and 672 (fixed dimension 4), and exactly the
class of 56 lies in the heart's Ω-class — 56 hearts at the still point,
each with centralizer of order 216 in G₂(2). So is the cube of the clock:
of the 2,520 elements of order 6 in G₂(2), 504 have their square in the
heart's class, and every one of the 504 is conjugate in Ω to (Φ·c̄)³ (the
fibre-over-x method of SM-047). The eighteen itself cannot be turned out
of the still point, but its cube and its sixth power can. And the vector
shadow C̄ = Stab_Ω(v) can be turned into an eighteen: of 3,000 random
elements g of C̄, 485 give Φ·g of order 18 (with orders 3, 6, 9, 12, 18,
21, 24 all present), so the clock's class meets Φ·C̄. [obs] Φ·c̄₇² has
order 12 and Φ·c̄₇⁶ has order 9.

## 2. The still point's twisted orders (AJ1)

| ord g in G₂(2) | count | ord Φ·g | count of Φ·g |
|---|---|---|---|
| 1, 3 | 1, 728 | 3 | 729 |
| 2, 6 | 315, 2520 | 6 | 2835 |
| 4, 12 | 756, 3024 | 12 | 3780 |
| 7 | 1728 | 21 | 1728 |
| 8 | 3024 | 24 | 3024: {24:12, 12:3, 6:5, 3:2} × 1512, {24:12, 12:5, 6:1, 3:2} × 1512 |

Registered guess "both order-24 types appear": CONFIRMED, and in equal
numbers (the two G₂(2)-classes of elements of order 8, presumably; not
tested [obs]).

## 3. The heart and the cube at the still point (AJ2, AJ3)

| G₂(2)-class | size | fixed dim on V | block types | in class(x)? |
|---|---|---|---|---|
| order 3, "56" | 56 | 2 | {3:39, 1:3} × 3 | **yes** — 56 hearts; C_{G₂(2)} of order 216 |
| order 3, "672" | 672 | 4 | {3:38, 1:6} × 3 | no |
| order 6 with square in class(x) | 504 of 2,520 | — | {6:16, 3:7, 1:3} × 3 | **all 504 conjugate to (Φ·c̄)³** |

Registered guesses AJ2a (the 56, not the 672) and AJ3a (the cube is at
the still point): CONFIRMED.

## 4. The vector shadow (AJ4)

Orders of Φ·g for 3,000 random g ∈ C̄: 3: 17, 6: 230, 9: 152, 12: 918,
18: 485, 21: 426, 24: 772. Registered "18 appears": CONFIRMED (16.2 %,
against 1/6 in the whole coset). The clock can be turned out of the vector
shadow though not out of the still point.

## 5. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AJ0a | G₂(2) on 360: 12,096, vector parts = G_list | PASS |
| AJ0b | class(x) 89,600; C_Ω(x) 1944 | PASS |
| AJ1a | Φ commutes with all of G₂(2); orders lcm(3, ·); no 18; 24 present | PASS |
| AJ1b | both order-24 types among Φ·g₈ (guess) | PASS (1512 / 1512) |
| AJ2a | hearts at the still point = the class of 56 (guess) | PASS |
| AJ3a | (Φ·c̄)³ conjugate to an order-6 element of G₂(2) (guess) | PASS (all 504) |
| AJ4a | Φ·C̄ contains eighteens | PASS (485 / 3000) |

## 6. Grades

[C] everything in §§2–4 (full enumeration over G₂(2); exact conjugacy
per element in AJ3; sampled in AJ4 with the existence claim exact); [P]
lcm(3, ord g) for commuting elements of coprime-order cyclic groups; [obs]
the 216, the equal split, the shadow's order histogram, the two orders of
Φ·c̄₇² and Φ·c̄₇⁶.

## 7. Not claimed

No statement about which G₂(2)-classes of order 8 give which order-24
type (not tested); nothing about the class of Φ·g₈ in ⟨Ω,Φ⟩ (the order-24
classes are still unreached, SM-047); no structural reading of the 504.

## 8. Synthesis line

The still point holds the clock's heart and the clock's cube but not the
clock — it can pause and it can beat in threes, and the eighteen itself
must be turned out of the vector shadow: the same shape as SM-034's
"the turn rode free while the clock is what costs", now as a statement
about which powers of the roof clock G₂(2) can carry.
