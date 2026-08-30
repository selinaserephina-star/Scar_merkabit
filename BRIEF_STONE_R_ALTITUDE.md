# BRIEF — STONE R: THE ALTITUDE
**Scar_merkabit joint lane · staged 2026-08-30 · Selina's word: "lets
continue with this remarkable direction. Open up the exploration."**
**SHA-locked before one line of the verifier exists.**

## 0. Discipline

Compute, never assert; refutations at equal prominence, including this
brief's own registered guesses; Rule 3; not RH/GRH; no physical claim;
classical facts cited as classical. Deviations = dated AMENDMENT before
reveal. ONE LOCK.

## 1. The question

Stone Q proved the 56-machine's priced structure lives strictly ABOVE its
Clifford quotient: Ψ is nonlinear, pr is odd, ι is erased, depth collapses
to 1 downstairs. Stone R measures the altitude — how far above the
Clifford floor each gate actually flies — and locates the mechanism of the
two Stone Q surprises (the census coincidence and the one-spectrum [obs]).

Define the **linearity gap** of a gate g on the 56:
  ν(g) = min over w in W(E7) of d_H(g, w)   (Hamming distance on 56 points,
  minimum over all 2,903,040 Weyl elements, computed by full enumeration).
ν(g) = 0 iff g has a Clifford shadow. This is a third distance axis after
μ_typed (branch) and μ_frame — distance to the LINEAR world.

## 2. Constructions

R1. **The disguise.** Ψ and the Coxeter element c share cycle type
    [18,18,18,2] on the 56 (Stone Q), so they are conjugate in S₅₆.
    Construct an explicit conjugator g with Ψ = g c g⁻¹ and verify.
    Corollary to prove alongside: NO conjugator lies in C(ι) = B₂₈
    (else Ψ would commute with ι, contradicting ιΨι = Ψ⁻¹) — every
    disguise necessarily scrambles chirality.
R2. **The measurement (headline).** Full enumeration of W(E7) (2,903,040
    permutations of the 56 via the BSGS transversal chain, composed in
    numpy). Exact ν for the gate panel {Ψ, Ψ², Ψ³, Ψ⁶, Ψ⁹, pr}, with
    argmax witnesses (the nearest Weyl elements) recovered and
    characterized (cycle type; characteristic polynomial of the induced
    7×7 weight matrix, solved from 7 independent weights).
R3. **The clock's hidden matching.** τ(Ψ) coset type from M₀ ∪ Ψ(M₀)
    must reproduce SM-009's [9,9,9,1] (anchor). The conjugated matching
    M_Ψ = g(M₀) is the clock's OWN pairing (the one it preserves, being
    conjugate-to-linear); report its overlap with ι's M₀.
R4. **The two mechanisms.**
    (a) Pauli translations on form labels: conjugating T_x by a Pauli T_a
    multiplies by (−1)^{ω(a,x)}, i.e. translates the label; verify the
    translation action MIXES the Arf classes and makes the full Clifford
    group (with Paulis) TRANSITIVE on all 64 phase points — the mechanical
    explanation of Stone Q's one-spectrum [obs], and the exact sense in
    which the 36/28 split is a choice of Pauli sign gauge.
    (b) The trace obstruction: tr A_c = 1 for all 64 (Stone Q), and
    unitary conjugation preserves trace, so NO unitary realizes
    A_c ↦ −A_c on phase points. The 56 = 28 odd forms × sign exists only
    as a set; ι (the global sign flip) and the beam-splitter machine
    (SM-014) have NO unitary-conjugation realization on phase points —
    chirality downstairs is a gauge bit, not an operator.

## 3. Registered bars and expectations

**RB1 [construction].** An explicit g with Ψ = g c g⁻¹ verifies; the
no-B₂₈-conjugator corollary holds (one-line proof + spot checks).
EXPECT PASS.

**RB2 [REGISTERED HEADLINE — the measurement].** The six ν values and
witnesses, exact, by full enumeration. No numeric prediction is
registered — the values ARE the result. One REFUTABLE GUESS registered:
for Ψ, some minimizer has cycle type [18,18,18,2] with Coxeter
characteristic polynomial Φ₁₈·Φ₂ (i.e. the clock's nearest linear
neighbours include its own disguised class). If the minimizer class is
something else, that refutation is the finding.

**RB3 [anchor + new object].** τ(Ψ) = [9,9,9,1] reproduced from
M₀ ∪ ΨM₀ (SM-009 anchor gate); M_Ψ = g(M₀) computed; overlap |M_Ψ ∩ M₀|
reported [obs].

**RB4 [mechanisms].** (a) label-translation orbit = all 64 (transitivity
of Clifford-with-Paulis on phase points; Arf mixed) — EXPECT PASS;
(b) trace obstruction as stated — EXPECT PASS. Both mostly classical
bookkeeping; graded [P]/[C], claimed as explanation of the Stone Q [obs],
nothing more.

## 4. Honest scope

ν is OUR definition (a Hamming distance to a subgroup, like μ); no claim
it is standard. Conjugacy-class language for the witnesses is softened to
characteristic-polynomial evidence (S₅₆-conjugacy is by cycle type;
W-conjugacy is NOT claimed from cycle type alone). The R4 facts are
elementary/classical once stated; their value here is that they close the
two questions Stone Q opened. No Clifford+T claim; no physics.

## 5. Deliverables

verify_stone_r_altitude.py; STONE_R_ALTITUDE.md (bars resolved, grades,
not-claims); registry SM-016 + changelog v0.14; KCP units; git commit;
memory + one-sentence synthesis line. Send remains Selina's word.
