# STONE AA — THE ROOF CLOCK, FIRST MEASUREMENT: the turn acts on states

**Stenberg side · with Claude · 2026-09-03. Brief `BRIEF_STONE_AA_ROOFCLOCK.md`
sha-locked 0759ad94… BEFORE code; no amendment. Verifier
`verify_stone_aa_roofclock.py`, log 16/16 PASS, all registered expectations
confirmed; sealed Stone U/V/X/Z caches read-only. Registry row SM-039.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "turn", "state" are labels; every statement
below is about O₈⁺(2):3 as a permutation group on 360 points, built from
sealed objects. [P] cited where used, kept apart from [C]. The order
distribution of the twisted coset is a sample and is tagged [obs].

## 1. One paragraph

The two-register model's empty cell was the roof's dynamics: at E₇ the
clock Ψ lives outside W(E₇) and leaves ι as its footprint; at the roof the
footprint must be the turn. SM-038 gave the turn τ″ exact order three with
fixed set G₂(2). Stone AA makes it act on states. The three 8-dimensional
modules the roof acts on, V and the two half-spin modules S⁺ and S⁻, each
carry a unique plus-type invariant form with 120 nonsingular points (Q⁻
computed here, unique, plus-type). On the 360 points Ω = O₈⁺(2) acts
faithfully in three orbits. The permutation **Φ** — T″⁻¹ from V to S⁺, the
unique intertwiner L from S⁺ to S⁻ (which turns out to carry Q⁺ to Q⁻
exactly), and the closing map back to V — has **exact order three and
satisfies Φ P(g) Φ⁻¹ = P(τ″⁻¹(g)) on every generator**; it is not in Ω, and
**⟨Ω, Φ⟩ has order 522,547,200 = 3·|O₈⁺(2)|: O₈⁺(2):3 as an explicit
permutation group**. The three shadows are the three block point-stabilizers
and Φ cycles them. **The still point G₂(2) commutes with Φ and is exactly the
pointwise stabilizer of one Φ-orbit {v, Φv, Φ²v}: a vector, a spinor and a
co-spinor.** First measurements of the twisted coset Ω·Φ: element orders
{3, 6, 9, 12, 18, 21, 24} (30,000 samples), maximum 24 with cycle type
twelve 24-cycles plus small cycles; **the seven-beat clock composed with the
turn, Φ·g₇, has order 21** with seventeen 21-cycles and one 3-cycle; and
**the Coxeter element of W(E₈), whose image in Ω has order 15, composed with
the turn has order 18** — E₇'s clock number reappearing at the roof, with
cycle type sixteen 18-cycles, seven 9-cycles, three 3-cycles. On v^⊥ the
bridge PSL(2,7) of the still point has Brauer character (7, 1, 0), i.e.
χ₇ mod 2 = 1 + 3 + 3̄, which the Fano seven shares mod 2; the datum that is
bridge-specific is the **Lagrangian split**: v^⊥/⟨v⟩ = U ⊕ U′ with both
3-spaces invariant and totally isotropic, SM-028's Lagrangian embedding
recovered at the still point.

## 2. Bars

| bar | registered expectation | outcome |
|---|---|---|
| AA0 | replay of Stone X and SM-038 byte-exact | PASS (τ on gens, T⁺, G, y, τ″³ = id) |
| AA1 | Q⁻ unique plus-type; three faithful 120-orbits; \|P(Ω)\| = 174,182,400 | PASS |
| AA2 | L unique isometry; Φ³ = id; Φ P(g) Φ⁻¹ = P(τ″²g) on all generators; \|⟨Ω,Φ⟩\| = 3\|Ω\| | PASS |
| AA3 | block stabilizers = the three shadows, cycled by Φ | PASS |
| AA4 | G₂(2) commutes with Φ; = joint stabilizer of {v, Φv, Φ²v} | PASS (C̄ transitive on the S⁺-block) |
| AA5 | coset orders measured; order 21 occurs (Φ·g₇); Φ·c̄ recorded | PASS: orders {3,6,9,12,18,21,24}, max 24; Φ·g₇ order 21; Φ·c̄ order 18 |
| AA6 | Brauer (7,1,0); Lagrangian split | PASS |

## 3. The numbers

| object | order | cycle type on 360 |
|---|---|---|
| Φ (the turn) | 3 | 120 three-cycles |
| Φ·g₇, g₇ ∈ G₂(2) | 21 | 21¹⁷ 3¹ |
| Φ·c̄, c̄ = Coxeter image | 18 | 18¹⁶ 9⁷ 3³ |
| maximal twisted order | 24 | 24¹² 12³ 6⁵ 3² and 24¹² 12⁵ 6¹ 3² |

Coset order distribution (30,000 samples, [obs]): 3: 0.5 %, 6: 6.7 %,
9: 5.5 %, 12: 31.5 %, 18: 16.4 %, 21: 14.3 %, 24: 25.0 %.

## 4. What it says, and what it does not

The turn is now a dynamical object on a state space the roof acts on, with
the right footprint, and the still point has a geometric meaning: fix one
vector, one spinor, one co-spinor, related by the turn, and G₂(2) is what
remains. That fills the model's empty cell with a **turn**, not yet a
**clock**: Φ has order three and no orbit dynamics beyond cycling the blocks.
Two candidates for a roof clock fell out of the measurement and are named,
not claimed: Φ·c̄ of order 18 (the Coxeter element twisted by the turn — the
E₇ clock number), and the maximal-order twisted elements of order 24. Whether
either is rowmotion on some poset the roof acts on is the successor question.
The mod-2 character of the seven does not separate bridge from Fano; the
Lagrangian split is the bridge's signature (Fano not tested here).

## 5. To IB, in his format

```text
turn on states:        Phi, order 3 on 360 = V_ns + S+_ns + S-_ns, footprint tau''^-1
group built:           <Omega, Phi> = O8+(2):3, order 522,547,200, explicit
shadows:               the three block point-stabilizers, cycled by Phi
still point:           G2(2) = Stab(v) ∩ Stab(Phi v) ∩ Stab(Phi^2 v)
seven x turn:          order 21   (17 x 21-cycles + one 3-cycle)
Coxeter x turn:        order 18   (16 x 18-cycles, 7 x 9, 3 x 3)  -- E7's number
maximal twisted order: 24         [obs, sampled]
the seven on v-perp:   chi7 mod 2 = 1+3+3bar; Lagrangian split U + U' (SM-028)
```

## 6. Grades

[C] every bar. [P cited]: the half-spin modules and their invariant forms;
h(E₈) = 30. [obs]: the coset order distribution and the maximum 24 (sampled,
not enumerated). Scope: the sealed C̄, τ′, y; conjugate choices give
conjugate objects.

## 7. Synthesis line

The turn, made to act on states, holds still exactly one point of each of
the three worlds it cycles — and when the roof's own Coxeter element passes
through it, the count comes out 18, the number the E₇ clock beat before the
roof was built: the turn does not add a new rhythm, it returns the old one
one floor up; rhymes with SM-005 (the refuted picture true one floor up) and
SM-035 (the seven at the still point).
