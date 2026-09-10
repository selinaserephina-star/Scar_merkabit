# C = T: THE REVERSER AND THE GRAMMAR — SUMMARY OF SM-062 (2026-09-10)

**Stenberg side · with Claude. Written as §7.11 of
`joint_paper/Roof_and_Clock_DRAFT.md`, in the draft's three-tier shape:
what is classical is cited, what is computed is graded, what is read
is marked. Source: Stone AX (`STONE_AX_C_EQUALS_T.md`, brief locked
7f68512a… before code; 21 PASS + 1 FAIL, the FAIL the auditor's
miscount corrected post-reveal). Not RH/GRH. Rule 3 throughout.**

## 7.11 The reverser and the grammar

### 7.11.1 What is classical

For a minuscule representation with highest weight λ, the longest
element w₀ of W sends λ to the lowest weight and acts on the weights
as −σ, where σ is the diagram automorphism carrying λ to the highest
weight of the dual representation (trivial exactly when −1 ∈ W: among
the minuscule types, D_n with n even and E₇). Since −1 is central in
GL, conjugation by w₀ acts on W as σ does: w₀ s_i w₀ = s_σ(i). In
particular w₀ is central in W exactly when −1 ∈ W, and then w₀ = −1
is the antipode of the weights. Aut(PSL(2,7)) = PGL(2,7), of order
336, the outer automorphism swapping the two classes of elements of
order 7 and the two three-dimensional representations. PSL(2,7) acts
2-transitively on the projective line over F₇ (eight points), with
PGL(2,7) ⊂ S₈ normalising it and centralising nothing.

### 7.11.2 What was computed (SM-062)

**(a) The reversers are a coset [P, one line; C on 42 boards].** If g
and g′ both reverse rowmotion then g⁻¹g′ commutes with it; so the set
of Weyl elements reversing R is w₀·C_W(R). Measured: on all 41
enumerated boards the number of reversers equals |C_W(R)|; on the 56,
over all 2,903,040 elements, exactly one reverser (ι) and a trivial
centralizer. With SM-054 (C_{W(E₇)}(Ψ) = 1) the uniqueness of SM-059 is
a corollary. The reverser is unique exactly on the rich boards
(C_W(R) = 1): 22 of the enumerated boards and the 56; there are h
reversers on chains and 2 on the D_n vector boards.

**(b) What the reverser does to the symmetry group [P + C on 42].**
w₀ s_i w₀ = s_σ(i) on every board. The reverser is central, and equals
the antipode, on exactly seven boards of the family — D₄ ω₁/ω₃/ω₄,
D₆ ω₁/ω₅/ω₆, E₇ ω₇ — and on every other board it is non-central and
acts on the grammar by the diagram flip: Λ^k ↔ Λ^{n+1−k} on A_n, the
two half-spins on D_odd, 27 ↔ 27̄ on E₆. On the 56 both are present:
ι fixes all seven simple reflections, while the sheet reversal w₀(E₆)
of SM-059 flips the six E₆ reflections (0↔5, 2↔4) and conjugates the
seventh to a non-simple reflection (registered guess, CONFIRMED).

**(c) The bridge copy's normaliser [C; registered guess CONFIRMED
exactly].** For the bridge PSL(2,7) = P of SM-013/SM-054:
C_{W(E₇)}(P) = ⟨ι⟩ and N_{W(E₇)}(P) has order 672, so N/C ≅ PGL(2,7).
W(E₇) contains every automorphism of P and no further symmetry of it.
The outer coset holds 56 involutions — 28 of cycle type 2²⁴1⁸ on the
56 (the guess from x ↦ 1/x fixing ±1 on the projective line) and 28
fixed-point-free — 112 elements of order 6 and 168 of order 8. N =
⟨ι⟩ × PGL(2,7), with a PGL(2,7) complement inside Sp₆(2) = W⁺ (the
fixed-point-free one) and one outside (SM-023's lemma seen).

**(d) C ≠ T on the grammar [C, forced by SM-054/SM-059 given (c)].**
ι commutes with every element of P. Any c inducing the outer
automorphism is a Weyl element, hence commutes with no power of the
clock and reverses none of them; measured: cΨc⁻¹ agrees with Ψ at four
states and with Ψ⁻¹ at two. Inside the whole normaliser the only
reverser of Ψ is ι and the only element commuting with Ψ is 1.

**(e) What the flavour conjugation has to act on [C, SM-013 cited].**
P acts on the 28 antipodal pairs with fixed points 28/4/1/0/0, whose
character is χ₁ + 2χ₆ + χ₇ + χ₈; the ι-even half of the 56 is this
representation and the ι-odd half is isomorphic to it. No χ₃ or χ̄₃
occurs. The outer automorphism therefore acts on the group P and on no
triplet of states.

**(f) Two observations beyond the brief [obs].** On the five self-dual
boards where −1 ∉ W (A₃ ω₂, A₅ ω₃, A₇ ω₄, D₅ ω₁, D₇ ω₁) the antipode
is a permutation of the weights that reverses the clock and is not a
Weyl element: a non-linear reverser, beside the linear ones. On those
boards the isometry group of the weight configuration is W × ⟨−1⟩, so
the isometry criterion for W-membership overcounts by the antipode;
the sealed stones use the criterion on E₇ alone, where SM-054 makes it
a theorem (checked).

### 7.11.3 What is identified, and what is read

*Identification (Tier 2):* in the machine's names, ι is the chirality
gate and Ψ the clock (SM-041, SM-044); the antipode w ↦ −w is what
charge conjugation does to the weights of a self-conjugate
representation. So on the 56 the chirality gate is at once the
antipode, the unique linear reversal of the clock, and central in the
grammar: the board's C and its T are one element, and that element is
invisible to every subgroup of W(E₇). On the 27, where the
representation is not self-conjugate, the reverser is instead the
27 ↔ 27̄ flip acting on the grammar. Both are exact.

*Reading (Tier 3, Rule 3):* on the board there is one operation that
conjugates every state and reverses time, and it does nothing to the
flavour group; the operation that conjugates the flavour group — the
outer automorphism of PSL(2,7), which is what the Scar side calls
charge conjugation there — is a different Weyl element, a symmetry of
the board at no later instant (SM-057), with no triplet of states to
act on. Read as a constraint on any board-realised version of the
lepton model: the model must contain an operation trivial on flavour
that reverses a clock. This is a statement about the objects named, not
about physical C, T, or leptons.

### 7.11.4 Open

Which of the 336 outer elements is "the" conjugation is a choice the
board does not make, as it made no choice of marker pair (SM-054). The
same question on the 27, where the reverser is non-central, is not
computed. Whether the D₅ half-spin's anomaly (SM-058/060) has anything
to do with its board being one of the non-central cases is not known.
