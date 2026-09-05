# STONE AI — THE CLASS OF THE EIGHTEEN, AND THE HEART'S CENTRALIZER

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AI_CLASS_OF_THE_EIGHTEEN.md` sha-locked b41ab779… BEFORE
code; no amendment. Verifier `verify_stone_ai_class18.py`, log: 15 PASS,
0 FAIL (nine REPLAY-AA checks + AI0a, AI1a, AI1b, AI2a, AI3a, and the
lock); no failed first run. 42 s. Machinery: Stone AA stages 0–2
VERBATIM, SM-045's helpers verbatim, the class enumeration extended to
keep a transversal, Schreier generators closed by numpy BFS. Sealed
caches READ-ONLY. Own cache `_stone_ai_cache/`. Registry row SM-047.**

## 0. Discipline

Not RH/GRH. Rule 3: "heart", "eighteen" are labels; the mathematics is
centralizers, transversals and a fibre argument, all exact. The one
population statement (one class) is exact per sampled element and
sample-bounded as a whole; it is graded so.

## 1. One paragraph

The centralizer in Ω of the heart x = (Φ·c̄)⁶ has order exactly 1944 =
2³·3⁵ (Schreier generators from the class transversal, closed; every
element commutes with x), with centre of order 9 containing x and acting
transitively on the three fixed nonsingular vectors of x; the full
centralizer in ⟨Ω,Φ⟩ is three cosets of it by e = Φ·c̄ itself, order 5832.
The centralizer of the eighteen is as small as it can be: C_Ω(e) = ⟨e³⟩ of
order 6, so the conjugacy class of e (its ⟨Ω,Φ⟩-class is its Ω-class) has
29,030,400 elements, exactly one sixth of the twisted coset. And the
order-18 elements of the coset are one class: 300 sampled order-18
elements were each tested exactly — sixth power transported into the
fibre over x by the transversal, then conjugated by the 1944 elements of
C_Ω(x) — and all 300 are conjugate to Φ·c̄; the sampled density 0.173
against the class density 1/6; a second class of density 1 % would have
escaped a 300-sample with probability 9·10⁻⁹. The order-24 elements'
centralizers were not reached: their cubes' classes exceed the
enumeration cap, as the brief allowed.

## 2. The centralizer of the heart (AI1)

| quantity | value |
|---|---|
| |C_Ω(x)| | 1944 = 2³·3⁵ (= |Ω| / 89,600) |
| element orders | 1:1, 2:9, 3:296, 4:54, 6:720, 9:432, 12:432 |
| centre | order 9, contains x, 8 elements of order 3 |
| on the 3 fixed nonsingular vectors of x | one orbit |
| |C_{⟨Ω,Φ⟩}(x)| | 5832 = 3 × 1944, the extra cosets by e and e² |

No structural name is claimed for the group of order 1944 [obs].

## 3. The class of the eighteen (AI2, AI3)

| quantity | value |
|---|---|
| C_Ω(Φ·c̄) | ⟨(Φ·c̄)³⟩, order 6 |
| class of Φ·c̄ in ⟨Ω,Φ⟩ | 29,030,400 = |Ω| / 6 = 1/6 of the coset Ω·Φ |
| 300 sampled order-18 twisted elements | all of cycle type {18:16, 9:7, 3:3}; all 300 conjugate to Φ·c̄, exactly |
| sampled order-18 density | 0.1728 (SM-039: 0.164; SM-045: 0.168) vs 1/6 |

Method per element e′: x′ = e′⁶ ∈ class(x) (key lookup), e″ = u_{x′}⁻¹ e′
u_{x′} has sixth power x, and some h among the 1944 gives h e″ h⁻¹ = Φ·c̄.

## 4. Bars

| bar | registered | outcome |
|---|---|---|
| REPLAY-AA0…2d | AA stages 0–2 | 9 PASS |
| AI0a | class(x) = 89,600 with transversal; c̄₇⁶, c̄₆⁴ in it | PASS |
| AI1a | |C_Ω(x)| = 1944, all commute | PASS |
| AI1b | e centralizes x, e ∉ Ω, full centralizer 5832 | PASS |
| AI2a | C_Ω(e) = ⟨e³⟩, order 6; class 29,030,400 | PASS |
| AI3a | 300/300 conjugate to Φ·c̄ | PASS |
| AI4 | order-24 centralizers | not reached (cap), as allowed |

## 5. Grades

[C] every centralizer order, class size and per-element conjugacy; [P]
the fibre argument (h e h⁻¹ = e′ with equal sixth powers forces h ∈
C(x)) and the coset argument (the ⟨Ω,Φ⟩-class of a twisted e is its
Ω-class); [obs] the census and centre of C_Ω(x), the sampled density, the
binomial bound. "One class" is exact on the sample and bounded on the
population, not proved.

## 6. Not claimed

No name for the group of order 1944; no count of the order-18 elements of
the coset beyond ≥ 29,030,400; nothing about the order-24 centralizers;
nothing about whether Φ·c̄ is conjugate to Φ·g for a g in the still point
or in a shadow (a natural next question).

## 7. Synthesis line

The roof's eighteen is rigid — its only symmetries are its own powers —
while its heart is soft (a centralizer of 1944 with a nine-element centre);
one class of eighteens around one class of hearts: the clock is unique up
to the roof's motions, which is what "the roof clock" had to mean if it
meant anything (SM-036's hunt, closed in the form it can be closed).
