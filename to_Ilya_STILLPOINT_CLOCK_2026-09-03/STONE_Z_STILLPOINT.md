# STONE Z — THE STILL POINT OF THE ROOF TURN: G₂(2), the turner normalized to order three, and the bridge seven inside

**Stenberg side · with Claude · 2026-09-03. Brief `BRIEF_STONE_Z_STILLPOINT.md`
sha-locked e13da253… BEFORE code; no amendment. Verifier
`verify_stone_z_stillpoint.py`, log: 19 PASS + 1 registered expectation
INVERTED (Z6b) and resolved by a post-reveal check (Z6c, added after the
first run; first-run log kept as `verify_stone_z_stillpoint_FIRSTRUN.log`).
115 s, sealed Stone U/V/X caches read-only. Registry row SM-038.**

## 0. Discipline

Not RH/GRH. No identification (Rule 3): "still point", "turn", "hinge" are
labels; every theorem below is about subgroups of Ω = W⁺(E₈)/⟨−1⟩ ≅ O₈⁺(2)
and their covers in W(E₈). [P] facts cited and kept apart from [C].

## 1. One paragraph

SM-036 built the turner τ′, an outer 3-cycle of Ω on the three shadow
classes with τ′³ inner by a nontrivial h′. Stone Z asks what the turn holds
still. The intersection of the sealed vector shadow C̄ ≅ Sp₆(2) with its
turned image τ′(C̄), computed by an exhaustive sift of all 1,451,520
elements, is a group **G of order 12096 = |G₂(2)|**, index 120 in C̄; its
derived subgroup is perfect of order 6048 = |U₃(3)| with quotient C₂, and
the element-order census is {1,2,3,4,6,7,8,12}: **G = U₃(3):2 = G₂(2)**.
The raw turner does not normalize G (the triangle's three pairwise
intersections are three different G₂(2)'s; the triple intersection has
order 192). Solving the intertwiner for τ′ restricted to G gives a unique
invertible Dickson-0 isometry y, and **τ″ := inn(y⁻¹)∘τ′ fixes G pointwise
and satisfies τ″³ = identity on all 26 generators of Ω** — the turn of
exact order three, as registered. Under τ″ the triangle closes and all
three pairwise intersections equal G; every τ″-fixed element of the vector
shadow lies in G; a 1200-element random sample has no fixed element
outside G. At the still point sit **36 copies of PSL(2,7), one G-conjugacy
orbit, normalizer of order 336 = PGL(2,7)** — the ambient outer flip of
SM-024 lives there too — and **every copy is the bridge class** (involutions
in Sp₆(2)'s 315-class), in the vector shadow and in the spin-type shadow
alike: the seven that meets G₂ is the P¹(𝔽₇) seven, as SM-035 read it at
the crystal level, now at the roof. The register of the still point:
G's involutions form two classes, 63 inner (→ 315⁺) and 252 outer
(→ 3780⁺), all plus in both shadows — the registered expectation of a
minus class was **INVERTED** — and since M(G₂(2)) = 1 [P], the extension
class is detected by an outer involution's lift: **the spin-tower preimage
of the still point is SPLIT, 2×G₂(2)**. The still point passes through the
hinge without twisting.

## 2. Bars

| bar | registered expectation | outcome |
|---|---|---|
| ZB0 | replay reproduces the sealed Stone X witnesses | PASS (τ on 26 gens, T⁺, h′ byte-exact) |
| ZB1 | \|C̄ ∩ τ′(C̄)\| = 12096 = \|G₂(2)\| | PASS (index 120; [G,G] perfect, 6048; census {1,2,3,4,6,7,8,12}) |
| ZB2 | triangle intersections measured; τ′(G) = G tested | MEASURED: τ′(G) ≠ G; triple intersection 192; τ′(G) has order 12096 |
| ZB3 | y exists; τ″ fixes G; τ″³ = id on all generators | PASS (intertwiner space dim 2, one good solution; order three exact) |
| ZB4 | C̄ ∩ τ″(C̄) = G; triangle closes; no fixed sample outside G | PASS (set equality; τ″³(C̄) = C̄; 5 fixed of 1200, all in G) |
| ZB5 | PSL(2,7) ⊂ G, bridge class, N = PGL(2,7) | PASS (36 copies, one orbit, N of order 336; 315 in both shadows) |
| ZB6 | G meets a minus class in the spin reading ⇒ non-split | **INVERTED**: 63 → 315⁺, 252 → 3780⁺, all plus |
| Z6c (post-reveal) | — | the 252-class is outer, the 63-class inner; M(G₂(2)) = 1 [P] ⇒ **SPLIT**, 2×G₂(2) |

## 3. The three theorems, stated

1. **The still point.** C̄ ∩ τ′(C̄) = G₂(2) (order 12096, index 120), for
   the sealed vector shadow and the sealed turner. [C]; the name by the
   computed invariants + [P cited: G₂(2) = U₃(3):2 is the unique
   index-120 subgroup class of Sp₆(2)].
2. **The turn of order three.** τ″ = inn(y⁻¹)∘τ′ with y the unique
   invertible Dickson-0 isometric intertwiner of τ′|_G; τ″³ = id on Ω's
   generators; Fix(τ″) ∩ C̄ = G, and the triangle (C̄, τ″C̄, τ″²C̄) closes
   with all pairwise intersections G. [C]. Fix(τ″) = G₂(2) in full:
   [P cited] (the centralizer of an order-3 graph automorphism of
   O₈⁺(2) is G₂(2)); the machine checked it inside the three shadows and
   on a sample.
3. **The seven at the still point.** PSL(2,7) ⊂ G₂(2), one class of 36
   copies, N_{G₂(2)}(L₂(7)) = PGL(2,7), and the copy is the BRIDGE class
   of Sp₆(2) in both shadows containing G. [C].

## 4. Data worth keeping

- The 192 of the raw triangle's triple intersection (= 2⁶·3) is noted,
  not pursued.
- The intertwiner space for τ′|_G has dimension 2 (V is not G-irreducible:
  a fixed nonsingular vector), and exactly one of its three nonzero
  elements is an invertible Dickson-0 isometry.
- The random sample was biased toward C̄ (676 of 1200 words landed there);
  5 fixed elements is what the density 12096/1451520 predicts for that
  bias. Not a test of Fix outside the shadows; said so.

## 5. What it says to IB, in his format

```text
still point of the turn:     G2(2) = U3(3):2, order 12096, index 120 in Sp6(2)
turner normalized:           tau'' of EXACT order 3, fixing G2(2) pointwise
the seven inside:            PSL(2,7), 36 copies, one class, N = PGL(2,7)
its label:                   BRIDGE (315) in both shadows -- the P^1(F7) seven
register of the still point: TRIVIAL -- 2 x G2(2), split through the hinge
```

## 6. Grades

[C] every bar. [P cited]: G₂(2) = U₃(3):2 and its position in Sp₆(2); the
centralizer of a triality of order 3; M(G₂(2)) = 1 (ATLAS). [obs] none
claimed. Scope: the sealed C̄ and the sealed τ′; other vector shadows are
Ω-conjugate and give conjugate still points.

## 7. Not claimed

No statement about compact G₂ beyond SM-035's; no claim that τ″ is "the"
roof clock (it is the turn, not a clock: order three, no orbit dynamics
measured); nothing about physics.

## 8. Synthesis line

At E₇ the two twos went one per seven-class (SM-029); at the still point
of the roof the bridge seven keeps its outer two (PGL(2,7) inside G₂(2))
and the hinge lets the still point through untwisted — the group that
holds still under the turn is the one whose seven is the P¹(𝔽₇) seven, at
the crystal (SM-035) and at the roof (SM-038) alike; rhymes with Stone S
(the world that forgets its path is uniformly softer): what the turn
forgets, the hinge does not have to remember.
