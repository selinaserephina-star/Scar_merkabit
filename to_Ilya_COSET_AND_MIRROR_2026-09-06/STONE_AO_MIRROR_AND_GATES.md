# STONE AO — THE MIRROR AND THE GATES

**Stenberg side · with Claude · 2026-09-06. Brief
`BRIEF_STONE_AO_MIRROR_AND_GATES.md` sha-locked e45d83b7… BEFORE code; no
amendment. Verifier `verify_stone_ao_mirror_and_gates.py`, log: 11 PASS
+ 1 registered guess INVERTED (AO6a) + the post-reveal AO6b (labelled)
that turns the inversion into the stone's main finding. First run (before
AO6b) kept as `verify_stone_ao_mirror_and_gates_FIRSTRUN.log`. 105 s
(the Schreier–Sims order of ⟨Ψ, pr⟩ on 56 points and the toggle
constructions). Machinery: `scar56_data.json` (SM-005) READ-ONLY; the AC
verifier's E₈ replay, pair type, poset, rowmotion and toggles VERBATIM
(lines 55–108 and 111–146, its checks re-issued as AO0a/AO0b); the sheets
and their posets built exactly as SM-041 AC5; sympy's Schreier–Sims for
the group orders. Registry row SM-053.**

## 0. Discipline

Not RH/GRH. Rule 3: "mirror", "gate", "clock", "sheet" are labels; the
mathematics is permutations of 56 ideals, a group order, a parity
identity and one poset isomorphism. The registered guess (that pr does
not normalize the sheet clock) was ours and wrong; it is recorded first.

## 1. One paragraph

The third gate of the merkabit, the mirror pr, now has an exact
description. On the board the pairing with the fundamental coweight of
the deleted node 6 splits the 56 states into two poles (±3/2, the top and
bottom of the lattice) and two 27-sheets (±1/2); pr swaps the sheets and
fixes the poles (its only two fixed points), and ι swaps the sheets and
swaps the poles. pr commutes with ι, agrees with no linear involution
(6 states with ι, 14 with σ = −w₀(E₆), 2 with w₀), and its 93 % incidence
memory (SM-040) is the same bilinear parity identity as the clock's,
with toggle multisets of size exactly 9 on every non-pole state. The
registered guess that pr does not normalize the sheet clock Ψ₆ (rowmotion
on each sheet as J(P₆), order 12) was INVERTED outright: pr COMMUTES with
Ψ₆. The post-reveal test shows why: pr is an order-isomorphism between the
two sheets' ideal lattices — every one of the 324 comparable pairs of
each sheet is carried to a comparable pair of the other, in both
directions — and the map it induces on the sixteen join-irreducibles of a
sheet swaps colours 0 ↔ 5 and 2 ↔ 4 and fixes 1 and 3: **the mirror is
the E₆ Dynkin diagram automorphism acting on the sheet posets**, extended
by fixing the poles. It is not the Weyl-group realization of that
symmetry (that would be linear; pr is not), but its action on ideals.
Finally, the gates generate everything: ⟨Ψ, ι⟩ is the dihedral group of
order 36 (SM-012), ⟨pr, ι⟩ ≅ C₂ × C₂, and ⟨Ψ, pr⟩ is the full symmetric
group on the 56 (order 56!), so the merkabit's three gates generate S₅₆.
Its Cayley graph on {Ψ, Ψ⁻¹, ι, pr} therefore has diameter at least 157
by counting alone, so the inherited "exact Cayley diameter (conj. 91–95)"
must concern a different object — flagged for the crystal lane, not
refuted. There is no reduced identity word in {Ψ, Ψ⁻¹, pr} of length up
to 16 beyond the trivial ones; the order of pr·Ψ⁴ is 840.

## 2. The sheets and the two involutions (AO1, AO2)

| map | on the sheets | on the poles | order | fixed points |
|---|---|---|---|---|
| pr | swaps | fixes both | 2 | 2 (the poles) |
| ι | swaps | swaps | 2 | 0 |
| Ψ (obs) | 17 + 17 stay, 9 + 10 cross | top → bottom, bottom → a sheet | 18 | 0 |

pr commutes with ι; pr∘ι has 6 fixed points; agreement pr/ι 6, pr/σ 14,
pr/w₀ 2. Parity identity for pr: 0 exceptions, kept 1432/1540 = 92.99 %
(SM-040 re-seen); toggle-multiset sizes {0: 2, 9: 54}.

## 3. The gates generate everything (AO3, AO4)

| group | order |
|---|---|
| ⟨Ψ, ι⟩ | 36 (dihedral; ιΨι = Ψ⁻¹) |
| ⟨pr, ι⟩ | 4 |
| ⟨Ψ, pr⟩ | 56! = 710,998,587,804,863,451,854,045,647,463,724,949,736,497,978,881,168,458,687,447,040,000,000,000,000 |
| ⟨Ψ, ι, pr⟩ | 56! |

[P] Diameter of Cay(S₅₆, {Ψ, Ψ⁻¹, ι, pr}) ≥ ⌈log₃(56!/2)⌉ = 157 (at most
2·3^d − 1 elements within distance d). Orders of pr·Ψ^k for k = 1..17:
1170, 120, 13860, 840, 840, 40, 9660, 1820, 78, 1820, 9660, 40, 840, 840,
13860, 120, 1170 (symmetric under k ↔ 18 − k as it must be). No reduced
identity word using pr up to length 16.

## 4. pr on the lattice (AO5)

Comparable pairs of ideals of the full lattice: 1407. ι reverses all 1407
(an antiautomorphism: I ↦ the complement of the dual). pr: 757 preserved,
571 reversed, 79 to incomparable pairs — but every one of the reversed
and incomparable images is a cross-sheet pair (§5). Ψ (obs): 1208 / 115 /
84. The seven colour toggles T_c are involutions; pr commutes with T₁ and
T₃ only (the two colours the diagram automorphism fixes) — consistent with
§5; ι commutes with all seven.

## 5. What the mirror is (AO6, AO6b)

Ψ₆, the rowmotion of each sheet as J(P₆) (AC5), extended by fixing the
poles, has order 12 and cycle type {12: 4, 3: 2, 1: 2}. Registered guess
"pr does not normalize ⟨Ψ₆⟩": INVERTED — pr Ψ₆ pr = Ψ₆. Post-reveal:

| pr on the within-sheet ideal order | preserved | reversed | neither | total |
|---|---|---|---|---|
| sheet 0 → sheet 1 | 324 | 0 | 0 | 324 |
| sheet 1 → sheet 0 | 324 | 0 | 0 | 324 |

Ideal sizes preserved; all 16 principal ideals map to principal ideals;
the induced map on the join-irreducibles has colour map {3→3 (×4),
2→4 (×3), 4→2 (×3), 1→1 (×2), 5→0 (×2), 0→5 (×2)} — the E₆ diagram
automorphism (in the C7 labelling with node 6 deleted: the chain
0–2–3–4–5 with 1 attached at 3, reflected).

## 6. Bars

| bar | registered | outcome |
|---|---|---|
| AO0a, AO0b | AC machinery re-seen | PASS |
| AO1a | sheets by the coweight; pr swaps sheets, fixes poles; ι swaps both | PASS |
| AO2a | pr vs ι, σ, w₀; commutes with ι | PASS |
| AO2b | parity identity for pr, 0 exceptions, 92.99 % | PASS |
| AO3a | ⟨Ψ,ι⟩ = 36, ⟨pr,ι⟩ = 4, ⟨Ψ,pr⟩ = 56! | PASS |
| AO3b | diameter ≥ 157 [P] | PASS |
| AO4a | the orders m_k; m₄ = 840; no short word | PASS |
| AO5a | ι an antiautomorphism; pr neither | PASS |
| AO6a | pr does not normalize ⟨Ψ₆⟩ (guess) | **INVERTED** — pr commutes with Ψ₆ |
| AO6b | post-reveal: pr an order-isomorphism of the sheet lattices | PASS (finding) |

## 7. Grades

[C] every count, order and the isomorphism; [P] the bilinearity of the
parity identity, the diameter bound, and the reading of the induced colour
map as the diagram automorphism (the colour permutation is computed; that
it is the diagram automorphism is read off the Cartan matrix C7); [obs]
Ψ's sheet transitions, the colour-toggle commutations. The inherited
"conj. 91–95" is flagged, not refuted: its object is not defined in this
lane's record.

## 8. Not claimed

Nothing about the Cayley diameter beyond the lower bound; nothing about
whether pr is realized by an element of any group acting on V (it is not
linear); no statement about promotion or other toggle-group elements; the
inherited "shortest pr/Ψ⁴ relation" is answered only as stated (the order
840 of pr·Ψ⁴ and the absence of short words).

## 9. Synthesis line

The mirror is the diagram symmetry of E₆ seen on ideals instead of on
weights — non-linear on the roof, exact on the lattice — and with the
clock it generates every permutation of the board: the machine's three
gates are a lattice clock, a lattice reflection, and the antipode, and
between them nothing on the board is out of reach; SM-041's "the clock is
what costs" has its counterpart — the mirror is what identifies.
