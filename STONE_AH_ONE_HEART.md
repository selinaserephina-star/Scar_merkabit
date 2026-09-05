# STONE AH — THE ONE HEART

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AH_ONE_HEART.md` sha-locked 1d056f53… BEFORE code; no
amendment. Verifier `verify_stone_ah_one_heart.py`, log: 17 PASS, 0 FAIL
(16 registered + the post-reveal AH2c, labelled). A first run stopped
before any AH check on a builder slicing error (two AG statements pulled
in with the helpers); that log is kept as
`verify_stone_ah_one_heart_FIRSTRUN.log`. 18 s. Machinery: Stone AA
stages 0–2 VERBATIM (nine REPLAY-AA checks PASS; Φ equals the sealed
cache), SM-045's class-enumeration helpers verbatim; sealed caches
READ-ONLY. Own cache `_stone_ah_cache/`. Registry row SM-046.**

## 0. Discipline

Not RH/GRH. Rule 3: "heart", "clock", "turned" are labels; the
mathematics is fixed dimensions predicted by exponents and Ω-conjugacy
classes decided by enumeration.

## 1. One paragraph

SM-045 found one order-3 element shared, up to conjugacy in Ω, by the
roof's twisted eighteen Φ·c̄ and the E₇ Coxeter element. This stone asks
which other clocks of the roof share it, predicting the answer from the
exponents and deciding it by class enumeration. The E₆ Coxeter element's
order-3 power (fixed dimension 2, the A₂ lattice mod 2 as an anisotropic
line) lies in the same class: ONE heart for the three clocks of orders 12
(E₆), 18 (E₇) and 18 (the roof's twisted one) — the class of 89,600
elements with centralizer of order 1944. The E₈ Coxeter image's own
order-3 power (fixed dimension 0, no fixed nonsingular vector) and the D₄
Coxeter element's (fixed dimension 6) are not in it; they lie in two
classes of 2,240 elements each (centralizer 77,760) whose block cycle
types are permutations of each other, and the post-reveal check shows why:
Φ² carries the E₈ one onto the D₄ one. The roof's own Coxeter heart is the
D₄ heart turned. On the board, the E₆ Coxeter element has exactly the
orbit structure of SM-041's E₆ rowmotion twice over plus the two singlets.
And for 300 sampled order-18 twisted elements, every sixth power lies in
the heart's class and every ninth power in the class of (Φ·c̄)⁹ (1,575
elements, centralizer 110,592): consistent with a single class, not yet
proved.

## 2. The order-3 powers (AH1)

| element | order | Dickson | cycle type on the 120 | fixed dim on V | q on the fixed space |
|---|---|---|---|---|---|
| c̄⁵ (E₈ Coxeter image, order 15) | 3 | 0 | {3: 40} | 0 (predicted 0) | — |
| c̄₆⁴ (E₆ Coxeter, order 12) | 3 | 0 | {3: 39, 1: 3} | 2 (predicted 2) | 1, 1, 1 |
| c̄₇⁶ (E₇ Coxeter, order 18) | 3 | 0 | {3: 39, 1: 3} | 2 (SM-045) | 1, 1, 1 |
| c̄₄² (D₄ Coxeter, order 6) | 3 | 0 | {3: 28, 1: 36} | 6 (predicted 6) | 36 nonsingular, 27 singular |

The predictions: an order-3 power of a Coxeter element fixes the
eigenvectors whose exponent is divisible by 3, plus the orthogonal
complement of the sub-root-system in E₈; a semisimple element of odd order
has the same fixed dimension in characteristic 0 and mod 2. E₆ and D₄ sit
inside E₇ as sub-diagrams of the sealed C7 base (nodes {0..5} and
{1,2,3,4}).

## 3. The classes (AH0a, AH2)

| class of | size | centralizer | block cycle types (V, S⁺, S⁻) | members |
|---|---|---|---|---|
| x = (Φ·c̄)⁶ | 89,600 | 1,944 = 2³·3⁵ | {3:39,1:3} × 3 | c̄₇⁶ (SM-045), **c̄₆⁴** |
| c̄⁵ (E₈) | 2,240 | 77,760 = 3·25,920 | {3:40}, {3:28,1:36}, {3:40} | |
| c̄₄² (D₄) | 2,240 | 77,760 | {3:28,1:36}, {3:40}, {3:40} | Φ² c̄⁵ Φ⁻² |

AH2a: c̄₆⁴ ∈ class(x) — registered, CONFIRMED. AH2b: c̄⁵ ∉, c̄₄² ∉ —
registered by fixed dimension, confirmed by membership. AH2c (post-reveal,
labelled): c̄⁵ ∉ class(c̄₄²) but Φ² c̄⁵ Φ⁻² ∈ class(c̄₄²) (Φ c̄⁵ Φ⁻¹ is not):
the two are triality images — the E₈ Coxeter's heart on the vector block
is the D₄ Coxeter's heart on a spinor block.

## 4. The clocks on the board (AH3)

| Coxeter element | cycle type on the 56 |
|---|---|
| E₆ (order 12) | {12: 4, 3: 2, 1: 2} = [12,12,3] ⊕ [12,12,3] ⊕ 1 ⊕ 1 |
| E₇ (order 18) | {18: 3, 2: 1} (SM-044) |
| D₄ (order 6) | {6: 6, 2: 6, 1: 8} [obs] |

The E₆ line is SM-041's Ψ₆ orbit structure on each 27-sheet, seen from the
Coxeter side (Rush–Shi at E₆, on the data).

## 5. The order-18 twisted elements (AH4)

300 drawn from the coset Ω·Φ (1,736 tries): all with cycle type
{18: 16, 9: 7, 3: 3}; 300/300 sixth powers in class(x); 300/300 ninth
powers in the Ω-class of (Φ·c̄)⁹ (1,575 elements, centralizer 110,592 =
2¹²·27). Necessary conditions for one class, all met; the class itself is
not enumerated (too large for the cap); OPEN-but-consistent.

## 6. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AH0a | Φ = cache; class(x) = 89,600, contains c̄₇⁶ | PASS |
| AH1 | fixed dims 0 / 2 / 6; all in Ω | PASS |
| AH2a | c̄₆⁴ ∈ class(x) | PASS |
| AH2b | c̄⁵, c̄₄² ∉ class(x) | PASS |
| AH2c | post-reveal: c̄₄² ~ Φ² c̄⁵ Φ⁻² | PASS (finding) |
| AH3 | E₆ Coxeter on the 56: {12:4, 3:2, 1:2}; E₇ [18,18,18,2] | PASS |
| AH4 | 300/300 sixth and ninth powers in the two classes | PASS |
| AH5 | arithmetic of 89,600 and 1,944 | [obs] |

## 7. Grades

[C] every class statement (enumerated classes, membership), every cycle
type and fixed dimension; [P] the exponent prediction and the
characteristic-0/mod-2 equality of fixed dimensions for odd-order
semisimple elements; [obs] the D₄ line of §4, AH5. AH4 is a sample:
consistent-with, not a class count.

## 8. Not claimed

No ATLAS names for the classes (sizes and centralizers are computed, not
matched); no statement that the order-18 twisted elements are one class;
nothing about the centralizer of x beyond its order; nothing about Φ·c̄
and c̄₇ beyond their sixth powers.

## 9. Synthesis line

The three clocks the merkabit and its roof actually use — E₆'s twelve,
E₇'s eighteen, the turned eighteen — beat around one order-3 heart, while
the roof's own Coxeter heart is D₄'s seen through the turn: the same
triality that SM-036 made explicit as an automorphism is here a statement
about which conjugacy classes the descent's clocks share.
