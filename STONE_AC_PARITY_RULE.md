# STONE AC — THE PARITY RULE OF THE CLOCK

**Stenberg side · with Claude · 2026-09-03. Brief `BRIEF_STONE_AC_PARITY_RULE.md`
sha-locked 16349cbd… BEFORE code; no amendment. Verifier
`verify_stone_ac_parity_rule.py`, log: 9 PASS + 2 registered guesses
INVERTED at full prominence (AC2b, AC5c); 1.3 s; only `scar56_data.json`
(SM-005) and the E₈-root replay of SM-040. Registry row SM-041.**

## 0. Discipline

Not RH/GRH. Rule 3: "clock", "incidence", "flip" are labels; the theorem is
a parity identity on a minuscule poset. The exploration that found the rule
was free and is not the sealed object; the sealed object is the locked run.

## 1. One paragraph

SM-040 measured that the merkabit's clock keeps 65 % of the roof's pair
incidence on the board and its cube 51 %, and left the numbers unexplained.
The pair type of {u, u′} is the sign of the E₇ inner product ⟨w, w′⟩
(P = +½, S = −½, v = antipode), so the score is Ψ's preservation of the
Gosset graph, whose automorphism group is W(E₇). The sealed Ψ is, exactly,
**rowmotion R(I) = ↓min(P ∖ I)** on the 27-element minuscule poset P whose
ideals are the 56 states, reconstructed from the crystal graph as its
join-irreducibles — not the inverse, not a conjugate; the convention is
now pinned on the data. Writing δ(u) = u + Ψu, δ is the XOR of the simple
roots the clock toggles, and the rule is:

```text
type(u,u′) flips under Ψ  ⟺  t₁ + t₂ + t₃ is odd
  t₁ = #{toggled colours of u  at which u′ has an edge}
  t₂ = #{toggled colours of u′ at which u  has an edge}
  t₃ = #{Dynkin-adjacent pairs between the two toggle multisets}
```

Zero exceptions on all 1485 non-antipodal pairs; with the 28 antipodal pairs
the count is 1002 of 1540 = 65.06 %. The same rule iterated (the k-fold
toggle multiset) is exact for every Ψ^k and reproduces the sealed profile,
65.1 / 54.7 / 51.3 / … / 61.6 at k = 9. The E₆ control: each 27-sheet is
J(P₆) with |P₆| = 16, its rowmotion has order 12 with orbits [12, 12, 3]
(the sealed MC values), its types are the Schläfli adjacency, and the rule
with the E₆ diagram is exact there too. Two guesses inverted: the eight
antipodal steps are **not** the eight singleton toggles, and the E₆ clock
keeps **63.5 %**, less than the E₇ clock — smaller toggle sets do not mean
fewer flips.

## 2. Bars

| bar | registered | outcome |
|---|---|---|
| AC0a | type = sign of ⟨w,w′⟩ | PASS (1512 / 1512 / 56 ordered pairs) |
| AC1 | 27 join-irreducibles; PSI = ↓min(P∖I) exactly | PASS |
| AC2a | δ = XOR of toggled roots | PASS (toggle sizes 1:8, 2:28, 3:11, 4:2, 5:3, 6:2, 9:1, 27:1) |
| AC2b | antipodal steps = singleton toggles | **INVERTED** (two different 8-sets) |
| AC3 | the parity rule, exact; 65.06 % recovered | PASS (0 exceptions) |
| AC4 | iterated rule exact, profile reproduced | PASS (k = 1..17, 0 exceptions) |
| AC5a/b | sheets = J(P₆); Ψ₆ order 12, [12,12,3]; rule exact | PASS |
| AC5c | E₆ keeps ≥ 65 % | **INVERTED** (63.53 % on both sheets) |

## 3. The cells

| (t₁, t₂, t₃) | kept | pairs |
|---|---|---|
| (0,0,0) | yes | 174 |
| (0,1,1) | yes | 129 |
| (1,0,1) | yes | 145 |
| (1,1,0) | yes | **553** |
| (0,0,1) | no | 126 |
| (0,1,0) | no | 128 |
| (1,0,0) | no | 104 |
| (1,1,1) | no | 126 |

Marginals [obs]: t₁ odd on 61.6 % of pairs, t₃ on 35.6 %. The dominant way
to keep a type is for each state's toggles to touch the other an odd number
of times with no Dynkin adjacency between the toggle sets.

## 4. Why the rule is exact (one paragraph, [P])

B is bilinear and the type is B(u,u′) (for non-antipodal pairs, q(u+u′) =
B(u,u′) since q(u) = q(u′) = 1). Hence B(Ψu,Ψu′) − B(u,u′) = B(δu,u′) +
B(u,δu′) + B(δu,δu′). With δ = Σ β_c over the toggle multiset,
B(β_c, w′) = ⟨α_c, w′⟩ mod 2 = |label_c(w′)| for minuscule labels in
{−1, 0, 1}, and B(β_c, β_c′) is the Cartan entry mod 2, i.e. Dynkin
adjacency. The computation is the content: that the sealed Ψ is exactly
rowmotion, so its toggles are exactly I Δ ↓min(P∖I).

## 5. What was learned about the clock

- The clock is rowmotion in the standard convention, exactly, on the data.
- It moves to a −½ neighbour on 40 of its 56 steps, to a +½ neighbour on 8,
  and to the antipode on 8.
- Its cube scores like a random permutation not because it is random but
  because the three-fold toggle multisets (sizes up to 27 + …) touch almost
  everything: parity of a large sum is a coin.
- The E₆ clock is slightly worse than the E₇ clock at keeping its own
  graph, which the guess had backwards.

## 6. Grades

[C] every bar; [P] the bilinearity paragraph; [obs] the marginals and the
dominant cell. Scope: the sealed data of SM-005 and the base choice of
SM-040 (W(E₇)-conjugate choices change nothing).

## 7. Not claimed

No closed form for 65.06 % beyond the count; no statement about promotion
or about non-minuscule posets; nothing about the still point (the rule
does not use G₂(2)).

## 8. Synthesis line

The clock forgets the roof's incidence exactly where its toggles touch the
other state an odd number of times — memory of relationship, not of self
(SM-033's line), now as a parity on the crystal itself; and the turn rode
free while the clock is what costs (SM-034), one more time.
