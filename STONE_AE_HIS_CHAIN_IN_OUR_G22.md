# STONE AE — HIS CHAIN IN THE HOUSE'S STILL POINT

**Stenberg side · with Claude · 2026-09-05. Brief
`BRIEF_STONE_AE_HIS_CHAIN_IN_OUR_G22.md` sha-locked 6f30f2f4… BEFORE code;
no amendment. Verifier `verify_stone_ae_his_chain.py`, log: 11 PASS + 2
FAIL — AE4b a registered expectation INVERTED (real), AE6 an
instrumentation error resolved by the post-reveal AE6b; the first-run log
is kept as `verify_stone_ae_his_chain_FIRSTRUN.log`. 31 s. Model:
`_stone_z_cache/G_rows.npy` (SM-038's G₂(2), 12,096 permutations of the
120 nonsingular vectors; sha256 1d298c8d…), READ-ONLY. Own cache
`_stone_ae_cache/witnesses_ae.json`. Registry row SM-043.**

## 0. Discipline

Not RH/GRH. Rule 3: "axis", "spiral", "descent" are IB's labels; the
mathematics is a subgroup chain with normalizers and class lengths. A
reciprocal audit in the house's cadence: his numbers recomputed in a
different model (his: GAP on PrimitiveGroup(63,2); ours: the sealed
permutation group on the 120 nonsingular vectors), and the one line his
script did not compute, computed.

## 1. One paragraph

IB's `axis_spiral_verification_package.zip` (sha c4856451…) verifies
{e} ⊂ Z₂ ⊂ A₄ ⊂ S₄ ⊂ PSL(2,7) ⊂ G₂(2) with GAP, five PASS. Every number in
his report is reproduced here inside the house's own G₂(2): one class of
36 PSL(2,7)'s with normalizer PGL(2,7) of order 336; inside a fixed copy H
14 subgroups S₄ in two H-classes of seven, each self-normalizing in H with
N_G(S₄) ≅ C₂×S₄ of order 48 and G-class length 252; one A₄ in each with
the same normalizers; a Z₂ with normalizers C₂×C₂ (4), D₈ (8), D₈ (8),
and 192 in G, class lengths 21 in H and 63 in G. Two things his package
does not say are now computed. First, the two S₄ classes of H are FUSED
in G₂(2): every one of the 168 elements of PGL(2,7) outside H carries a
class-1 S₄ into class 2, and the G-orbit of one S₄ (252 subgroups)
contains all 14 — so his "Total S4 copies = 504, Total S4 classes = 2" is
a double count (one class of 252); likewise for A₄. Second, his N_G(Z₂)
"(SL(2,3):C4):C2" of order 192 is NOT the still point's other 192, the
hexagon-point (Pauli) stabilizer of SM-040: the two groups have different
fingerprints (centre of order 2 vs 1; 8 vs 32 elements of order 3), C_G(z)
fixes no Pauli, and no element of G conjugates one into the other. Our
registered expectation that they coincide is INVERTED. Finally, on the
board: H has orbits [1, 7, 7, 21] on the 36 even thetas; every S₄ fixes
the H-fixed theta and exactly one more, the two H-classes being the point
stabilizers of the two 7-orbits — his "S₄ = point stabilizer of the
7-point action", located.

## 2. His report, line by line, in our model

| his line | his value | ours |
|---|---|---|
| |G| | 12096 | 12096 (distinct rows, closed, fix v) |
| order-168 subgroup classes | 1 | 1 (36 copies, one G-orbit) |
| |N_G(H)| | — | 336 (PGL(2,7)) |
| H | PSL(3,2) [168,42] | PSL(2,7) by explicit iso to the Möbius model |
| S₄ classes in H | 2, length 7 each | 2 × 7 = 14, all S₄ by explicit iso |
| N_H(S₄) | S₄ (24) | 24, = S₄ |
| N_G(S₄) | C₂×S₄ (48) | 48, ≅ C₂×S₄ by explicit iso |
| S₄ class length in G | 252 | 252 |
| A₄ per S₄ | 1 | 1 (its derived subgroup) |
| N_{S₄}(A₄), N_H(A₄), N_G(A₄) | 24, 24, 48 | 24, 24, 48 (C₂×S₄) |
| Z₂ classes in A₄ | 1, length 3 | 1 (three involutions, one A₄-class) |
| N_{A₄}, N_{S₄}, N_H (Z₂) | C₂×C₂, D₈, D₈ | C₂×C₂ (4), D₈ (8), D₈ (8) |
| |N_G(Z₂)| | 192 | 192 |
| Z₂ class length in H, G | 21, 63 | 21, 63 |
| N_G({e}) | G | G; chain verified as subsets, orders 1/2/12/24/168/12096 |

## 3. Two flags returned (computed, not asserted)

**(i) The S₄'s fuse.** His script computes class lengths in G per
subgroup (252, correct) and then adds them ("504 copies, 2 classes")
without testing G-conjugacy. Computed: the G-orbit of one S₄ has 252
members and contains all 14 S₄'s of H; of the 168 elements of N_G(H) ∖ H,
all 168 conjugate a class-1 S₄ into class 2. One G-class of 252 meets H.
The same for A₄ (252, all 14). Registered expectation CONFIRMED (AE2b,
AE3b).

**(ii) Two different 192's.** SM-038 met a 192 as the raw turner's triple
intersection and SM-040 identified it as the stabilizer in G₂(2) of one
Pauli (the 63 points of the hexagon). His chain's 192 is N_G(Z₂) = C_G(z)
for an inner involution z (class of 63, SM-038's involution table). Our
registered expectation that these are the same subgroup is INVERTED
(AE4b; the post-reveal AE4c makes the statement exact): z fixes 15 Paulis
and 8 board points [obs]; the whole centralizer fixes none; the two groups
of order 192 have different fingerprints —

```text
                    |centre|  #ord2  #ord3  #ord4  #ord6  #ord8  #ord12   |derived|
C_G(z), his 192        2       43      8     36      8     48     48        48
Stab_G(Pauli), SM-040  1       43     32     32     32     32      0        48
```

— and no element of G conjugates one into the other. His structure label
"(SL(2,3):C4):C2" is consistent with the census (8 elements of order 3 =
SL(2,3)'s) but is not identified here [obs]. So the still point carries
two 192's: the point stabilizer (SM-040's, the hexagon) and the involution
centralizer (his chain's). Both are of index 63; they are not conjugate
and not isomorphic.

**(iii) On the board.** H on the 36 thetas: [1, 7, 7, 21] (SM-040). The
H-fixed theta (index 12 in the sealed order) is fixed by every S₄ — that
is why AE6 as instrumented ("exactly one fixed theta") failed; excluding
it, every S₄ fixes exactly one further theta and the two H-classes are the
stabilizers of the two 7-orbits (thetas {3,7,8,15,16,20,30} and
{1,2,5,19,21,22,23}). AE6b PASS.

## 4. Bars

| bar | registered | outcome |
|---|---|---|
| AE0a | the model: 12096 distinct, closed, fix v | PASS |
| AE1 | 36 copies, one class, N = 336, H = PSL(2,7) by iso | PASS |
| AE2 | 14 S₄'s, 2 × 7, N_H = S₄, N_G = C₂×S₄, class 252 | PASS |
| AE2b | the two S₄ classes FUSE in G | PASS (CONFIRMED) |
| AE3 | A₄'s: same normalizers, class 252 | PASS |
| AE3b | the two A₄ classes FUSE in G | PASS |
| AE4 | Z₂: 4 / 8 / 8 / 192; class 21 / 63 | PASS |
| AE4b | N_G(Z₂) = a Pauli stabilizer | **INVERTED** (z fixes 15 Paulis) |
| AE4c | post-reveal: not conjugate, not isomorphic | PASS (finding) |
| AE5 | the chain as subsets | PASS |
| AE6 | each S₄ fixes exactly one theta | **FAIL (instrumentation)** — the H-fixed theta |
| AE6b | post-reveal: excluding it, exactly one; classes ↔ 7-orbits | PASS |

## 5. Grades

[C] every line of §2 and §3; [P cited] G₂(2) = U₃(3):2 and its two
classes of maximal subgroups of order 96 in U₃(3) (4.S₄ and 4²:S₃) are the
classical reading of §3(ii) — cited, not used; [obs] the fixed-point
counts of z and the order census of N_G(Z₂). His package's own numbers:
reproduced, all of them.

## 6. Not claimed

No identification of N_G(Z₂)'s structure beyond order and census; nothing
about other S₄ classes of G₂(2) that do not meet H; nothing about the
degree-63 model he used beyond the numbers he reported from it.

## 7. Synthesis line

The same order, two different groups — the hexagon's point stabilizer and
the involution's centralizer — is the still point's own version of the
two-twos of SM-029 (one class lifts split, one spinorial): a number
repeated is not a structure repeated, which is Rule 3 said in group theory.
