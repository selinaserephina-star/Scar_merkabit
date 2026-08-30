# STONE Q — THE CLIFFORD TRANSPORT
**Scar_merkabit joint lane · 2026-08-30 · SM-015**
**Brief:** `BRIEF_STONEQ_CLIFFORD.md`, sha-locked `bb7a6822…b316` before the
verifier existed. **Verifier:** `verify_stoneq_clifford.py` — **35/35**
(fail-first log of the first run kept: `verify_stoneq_clifford_FAILFIRST.log`).

## §0 Discipline

Compute, never assert. Refutations at equal prominence — one registered
expectation of this stone's own brief is refuted below (§3). Rule 3. Not
RH/GRH; the wall untouched; no physical claim. Classical facts are cited as
classical; candidate-new items are flagged [obs]. ONE LOCK (single session):
nothing here outranks its verifier until audited.

## §1 One paragraph

SM-003's bitangent bridge lives in Sp₆(2) = W(E₇)/{±1}, and that group **is**
the 3-qubit Clifford group modulo phases and Paulis — an identity of groups,
not an analogy. Stone Q builds both sides from scratch, exhibits the
isomorphism in shared coordinates, and pushes the bridge through it: the 28
bitangents become the 28 odd 3-qubit Pauli sign-operators, W(E₆) their
one-form Clifford stabilizer, Ilya's PSL(2,7) a Clifford subgroup transitive
on all 28, and the shared S₃ a statement inside the 3-qubit Clifford group.
Then the boundary: the 56-machine's actual gates do NOT transport — Ψ is
provably nonlinear (no Clifford shadow at all), pr is odd (outside W(E₇)),
ι becomes the identity — and the depth theory collapses in the shadow:
**shadow magic-depth = 1** (two double cosets). The two-tier depth structure
of the joint program (Ψ-depth 2 in both grammars, W-depth 4, 3718 frame
classes) lives **strictly above the Clifford quotient**. Open problem #3
(certificates for genuine Clifford+T) is therefore not winnable inside the
quotient — a theorem-grade boundary for the methods paper.

## §2 Bars resolved

| bar | registered content | verdict |
|---|---|---|
| QB1 | tableau images of {H,S,CNOT} generate 1,451,520 = \|Sp₆(2)\| | **PASS** [classical] |
| QB2 | Arf split 36+28; orbits [36],[28]; stabs 8!, \|W(E₆)\| | **PASS** [classical] |
| QB3 | φ: W(E₇)→Sp₆(2), kernel {±1}; pairs↔odd forms bijective + equivariant; same group as C1 in std coordinates; PSL(2,7) fingerprint [28] / [1,7,7,21] / S₃ | **PASS** — with the sub-expectation q(r)=ℓ_v(r)=0 **REFUTED** (see §3) |
| QB4 | ι ∈ W(E₇); Ψ ∉ (proof + strip); pr ∉ (parity + strip); Ψ has no 28-shadow; Coxeter stand-in; explicit circuit for φ(c) | **PASS** — all expectations held; circuit found, length 7 |
| QB5 | shadow depth over (H = W(E₆)-stab, magic = φ(c)) | **PASS-COLLAPSE** — orbits [1,27], two double cosets, depth exactly 1 |

## §3 The refuted expectation, at equal prominence

The brief registered `q(r) = 0` and `ℓ_v(r) = 0` (descent of each piece to
the radical quotient). **Measured: both equal 1** — neither the canonical
quadratic form q(x) = (xᵀC₇x)/2 nor any weight functional ℓ_v descends
alone. The transport survives because the obstructions **cancel**:
q_v(x+r) = q_v(x) + q(r) + ℓ_v(r) = q_v(x). The 56 minuscule weights are
exactly the shifts that repair the descent — the pair forms exist on the
quotient only as combinations. First-run FAIL kept in the fail-first log;
the corrected gates (obstructions = 1, cancellation verified 28 pairs ×
all 128 lifts) are in the sealed verifier.

## §4 The dictionary (the transported bridge)

In shared standard coordinates (x|z on 𝔽₂⁶, ω, q₀ = Σxᵢzᵢ — TBR's own
model):

| joint-lane object | 3-qubit Clifford-side object |
|---|---|
| Sp₆(2) = W(E₇)/± | the Clifford group C₃ mod phases and Paulis [classical] |
| 28 bitangents / ι-pairs of the 56 | the 28 **odd** Pauli sign-functions q_c (Arf 1) |
| W(E₆) (order 51,840) | the Clifford stabilizer of ONE odd form [classical: O₆⁻(2)] |
| PSL(2,7), bridge class | a Clifford subgroup transitive on all 28 odd forms; orbits [1,7,7,21] on the 36 even |
| the shared S₃ = N(⟨z₃⟩) (SM-003) | the two-subgroup intersection, now inside C₃/P₃ |
| Coxeter element c (Ψ's census [2,18,18,18] / [1,9,9,9], linearized) | the 7-gate circuit **H1·CX13·S1·H2·H3·CX23·CX12** (mod Pauli, phase; rightmost first) |

[obs] The 64 Hermitian sign-operators A_c = (1/8)Σ_x(−1)^{q_c(x)}T_x all
share ONE spectrum (products of (1±√3)/2; trace 1): the 36/28 Arf split is
a Clifford-**orbit** distinction, invisible to the spectrum.

## §5 The membership boundary (what does NOT transport)

- **Ψ has no Clifford shadow.** ιΨι = Ψ⁻¹ (SM-012) with ord Ψ = 18 > 2,
  and ι is central in W(E₇) ⇒ Ψ ∉ W(E₇). Stronger: ΨιΨ⁻¹ = ιΨ⁻² ≠ ι, so
  Ψ does not even act on the 28 pairs. The machine's true clock is
  **nonlinear**; only its census-twin, the Coxeter element, is Clifford.
- **pr ∉ W(E₇)**: pr is odd (27 transpositions) and every reflection is
  even on the 56 (each: 32 fixed, 12 two-cycles) ⇒ W(E₇)'s image is even.
  The odd mirror lives above the quotient.
- **ι ↦ identity**: the chirality bit is erased by the quotient, so the
  beam-splitter machine (SM-014) does not transport either.

## §6 The shadow collapse (QB5)

Shadow machine: G = Sp₆(2) on the 28 odd forms, typed H = stabilizer of one
form (≅ W(E₆)), magic = φ(c) with the base form not fixed by c. Computed:
H-orbits on the 28 = **[1, 27]** ⇒ exactly two (H,H) double cosets;
⟨H, φ(c)⟩ = G; counting certificate 51,840 + 51,840·27 = 1,451,520 exactly.
**Shadow magic-depth = 1 for every non-typed element.** Against the ladder
above the quotient — Ψ-depth 2 (both grammars, SM-009/010), W-depth 4
(SM-014), 3,718 frame classes — the quotient sees 2 classes at depth 1.

**Consequence for open problem #3** (Magic_Depth_Methods, certificates for
genuine Clifford+T): the two-tier structure this program prices does not
survive into the Clifford quotient, so any certificate for Clifford+T
double cosets must engage the unitary level (where SM-014's W-certificate
already lives), not the symplectic shadow. The boundary is now a computed
statement, not a suspicion.

## §7 Grades

| unit | grade |
|---|---|
| Sp₆(2) ≅ C₃/(phases·Paulis); W(E₆) = O₆⁻(2); S₈ = O₆⁺(2); Arf 36/28 | [P] classical, verified here |
| the transported dictionary (§4), equivariance, labels | [C] |
| the cancellation mechanism (§3) | [C]; its registered expectation REFUTED |
| Ψ/pr non-membership, no-28-shadow (§5) | [C] with one-line proofs |
| φ(c) circuit word | [C] |
| shadow collapse, depth 1 (§6) | [C] |
| phase-point common spectrum | [obs] |

## §8 Not-claims

No Clifford+T theorem: the T gate is outside the identification; open
problem #3 remains open (sharpened, not solved). No claim the 56-machine
"is" 3 qubits — ℂ⁵⁶ is a direct sum of 28 cells, not a tensor product. No
physics. The identification Sp₆(2) ≅ C₃/P₃ and the O₆± facts are classical;
this stone's contribution is the explicit transported dictionary on OUR
objects, the membership boundary, and the collapse theorem.

## §9 Reproduce

```
python -X utf8 verify_stoneq_clifford.py   # 35 checks
```
Requires `scar56_data.json` (emitted by `verify_dq6_resurrection.py`).
Deterministic (seed 728 reuses Stone F(b)'s hunt).
