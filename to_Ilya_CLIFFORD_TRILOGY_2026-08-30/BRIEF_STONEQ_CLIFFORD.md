# BRIEF — STONE Q: THE CLIFFORD TRANSPORT
**Scar_merkabit joint lane · staged 2026-08-30 · Selina's word: "Yes - go"**
**This brief is SHA-locked before one line of the verifier exists.**

## 0. Discipline

Compute, never assert. Refutations at equal prominence, including the
auditor's own registered expectations below. Rule 3 (mathematics split from
identification). Not RH/GRH; the wall untouched; no physical claim; no
novelty claim beyond flagged [obs] items. Classical facts cited as classical.
Any deviation from this brief discovered mid-run = dated AMENDMENT file,
sha-locked BEFORE the relevant reveal; post-reveal changes are findings.

## 1. The question

SM-003 (the bitangent bridge) lives in Sp₆(2) = W(E₇)/{±1}, order 1,451,520.
That group is **exactly the 3-qubit Clifford group modulo Paulis and phases**
(classical bookkeeping: the tableau representation C₃/⟨i·I, P₃⟩ ≅ Sp₆(𝔽₂)).
The corpus has never written the word "Clifford" next to the bridge. Stone Q
makes the identification explicit and computes what of the 56-machine
survives the trip:

- **Q-A (transport)**: exhibit computationally the isomorphism
  C₃/(phases·Paulis) ≅ Sp₆(2), and the equivariant dictionary
  {28 ι-pairs of the 56} ↔ {28 odd quadratic forms} ↔ {28 odd 3-qubit
  Pauli sign-functions / phase-point operators}, carrying W(E₆) (= stabilizer
  of one) and the bridge-class PSL(2,7) (= transitive on all 28).
- **Q-B (membership boundary)**: which of the machine's gates {Ψ, pr, ι}
  actually live in W(E₇) — i.e. have a Clifford shadow at all.
- **Q-C (the depth question, the registered headline)**: does any two-tier
  depth statement (Ψ-depth 2 in both grammars, W-depth 4) pull back to the
  Clifford quotient — or does the depth structure collapse there?

## 2. Constructions (all from scratch, Python 3 + numpy only)

C1. **Clifford side.** Tableau symplectic images of the 12 generators
    {H₁,H₂,H₃, S₁,S₂,S₃, CNOT_ij (6 ordered pairs)} as 6×6 𝔽₂ matrices on
    (x|z) coordinates, matching TBR's convention (V = bits 0–2 = X-part,
    V* = bits 3–5 = Z-part; ω((x|z),(x'|z')) = x·z' + x'·z;
    q0(x) = Σ xᵢzᵢ).

C2. **Forms.** The 64 refinements q_c = q0 ⊕ ⟨c,·⟩, Arf split, Clifford
    orbits and stabilizers. Additionally the 64 Hermitian phase-point
    operators A_c = (1/8) Σ_x (−1)^{q_c(x)} T_x (T_x the Hermitian Pauli
    i^{a·b} X^a Z^b) — spectra reported per Arf class [obs].

C3. **Weyl side and the map φ.** W(E₇) on the 56 weights from the 7 simple
    reflections (construction of SM-013, scar56_data.json). φ: W(E₇) →
    Sp(Q/2Q̄) via the reflection action on the root lattice mod 2:
    B(x,y) = xᵀC₇y mod 2, radical dim 1 (det C₇ = 2), quotient 𝔽₂⁶;
    canonical quadratic form q(x) = (xᵀC₇x)/2 mod 2. Weight pairs
    {v,−v} ↦ q_v := q + ℓ_v with ℓ_v(x) = v·x mod 2 (ω-basis pairing).
    **Computed gates, not assumed**: q(r) ≡ 0 and ℓ_v(r) ≡ 0 on the radical
    generator r (descent), q_v well-defined, all 28 distinct, all odd,
    W-equivariant. Then a symplectic basis change T into C1's standard
    coordinates (symplectic Gram–Schmidt adapted to q; Arf of q computed,
    reference form matched).

C4. **PSL(2,7).** The bridge-class copy K (168 elements on the 56) rebuilt
    by SM-013's hunt (seed 728); its image φ(K) fingerprinted on the forms.

## 3. Registered bars and expectations

**QB1 [gate, classical].** C1's 12 matrices preserve ω and generate order
1,451,520 = |Sp₆(2)|. EXPECT PASS.

**QB2 [gate, classical].** Arf split 36 even + 28 odd; Clifford orbits
[36],[28]; stab orders 40,320 / 51,840. Spectra of A_c constant per Arf
class, reported [obs]. EXPECT PASS.

**QB3 [the transport].** φ well-defined with kernel exactly {±1} (image
order 1,451,520); the pair map {v,−v} ↦ q_v is a bijection onto the 28 odd
forms, equivariant under all 7 simple reflections; after T, φ(W(E₇)) and
C1's group are the SAME matrix group; pair-stabilizer image = stabilizer of
the matching odd form, order 51,840; φ(K) is transitive on the 28 odd forms
with point stabilizer of order 6 nonabelian (S₃) and orbits [1,7,7,21] on
the 36 even forms — the TBR fingerprint. EXPECT PASS.
RISK, disclosed: if ℓ_v or q fails to descend to the radical quotient the
transport FAILS AS INSTRUMENTED (RUN-8 wording, never "null") and the stone
records the obstruction; no silent re-normalization.

**QB4 [membership boundary].** On the 56:
 (a) ι ∈ W(E₇)-image — EXPECT YES (ι = −1, already SM-013).
 (b) Ψ ∉ W(E₇)-image — EXPECT NO-MEMBERSHIP, with proof: ι is central in
     W(E₇), so membership would force ιΨι = Ψ; but ιΨι = Ψ⁻¹ (SM-012,
     DQ-4) and ord(Ψ) = 18 > 2. Confirmed independently by BSGS strip.
 (c) pr ∉ W(E₇)-image — EXPECTED NO via parity (compute the cycle types of
     all 7 reflections on the 56; if all even and pr odd, done) + strip.
 (d) Ψ does not even act on the 28 pairs: ΨιΨ⁻¹ = ιΨ⁻² ≠ ι. The true
     clock has NO Clifford shadow; its linearizable stand-in is the Coxeter
     element c = s₁⋯s₇ (cycle type [18,18,18,2] on the 56, [9,9,9,1] on
     the pairs — same census as Ψ, different permutation).
 (e) Deliverable: an explicit H/S/CNOT word for φ(c) (bidirectional BFS
     over the 12 tableau generators; word printed).
Any surprise against (a)–(d) is a finding at equal prominence.

**QB5 [REGISTERED HEADLINE — the shadow depth].** In the shadow machine
(G = Sp₆(2) acting on the 28 odd forms; typed subgroup H = stabilizer of
one odd form ≅ W(E₆), the base form chosen NOT fixed by c; magic gate =
φ(c)):
 compute the H-orbit structure on the 28.
 REGISTERED EXPECTATION: orbits [1,27] (rank 2 — W(E₆) on the 27 lines),
 hence exactly TWO (H,H) double cosets, hence ⟨H,φ(c)⟩ = G and
 **shadow magic-depth = exactly 1** for every g ∉ H, certified by the
 counting identity |H| + |H|·27 = 1,451,520.
 VERDICT NAME if it holds: **PASS-COLLAPSE** — the two-tier depth structure
 of the 56-machine (depth 2 in both grammars, W-depth 4, 3718 frame
 classes) lives STRICTLY ABOVE the Clifford quotient; the quotient sees a
 depth-1 world with 2 classes.
 If orbits ≠ [1,27]: compute the exact double-coset depth profile by BFS
 and record it — either outcome is a theorem.

## 4. Honest scope, stated up front

- The identification Sp₆(2) ≅ C₃/(phases·Paulis) is classical; so are
  W(E₆) ≅ O₆⁻(2), S₈ ≅ O₆⁺(2), and the 36+28 Arf split. The candidate-new
  content is only: the explicit transported dictionary, the membership
  boundary (b)–(d), the phase-point spectra tagging [obs], and the QB5
  depth statement on our own objects.
- **No Clifford+T theorem is claimed.** The T gate lies outside the
  identification entirely; open problem #3 (certificates for genuine
  Clifford+T double cosets) is NOT resolved here. If QB5 lands PASS-COLLAPSE
  the boundary sharpens to: the certificate transport cannot be won inside
  the Clifford quotient — it must engage the unitary level. That boundary
  statement is the stone's contribution to the methods paper.
- No claim that the 56-machine "is" 3 qubits; the ℂ⁵⁶ beam-splitter machine
  (SM-014) is a direct sum of 28 cells, not a tensor product, and W does
  not transport (ι ↦ 1 kills the chirality bit in the quotient).

## 5. Deliverables

verify_stoneq_clifford.py (self-asserting, prints every gate);
STONEQ_CLIFFORD.md (findings; §0 discipline lines; every bar resolved
PASS / FAIL / INVERTED / INCONCLUSIVE / VOID / NOT RUN; grades table;
not-claims); registry row SM-015 + changelog v0.13; KCP unit; memory +
one-sentence synthesis line in the cross-pattern dictionary; git commit
mirroring the changelog. Natural piece for Ilya (his PSL(2,7) inside the
Clifford group) — send remains Selina's word under the two-party rule.
