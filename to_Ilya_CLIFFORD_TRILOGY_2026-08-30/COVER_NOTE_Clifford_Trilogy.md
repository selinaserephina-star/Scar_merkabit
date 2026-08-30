# The Clifford Trilogy — Stones Q, R, T
**Scar–Merkabit joint lane · sealed 2026-08-30 · registry rows SM-015, SM-016, SM-017 (v0.15)**
**Stenberg · Balashov · with Claude (Anthropic Fable 5)**

Ilya — these three stones postdate the COMPLETE package you hold (which
ended at SM-014). They grew out of one observation about YOUR group, and
they close the boundary question the methods note left open. Everything
below is computed, sealed under sha-locked pre-registered briefs, and
reproducible from this folder alone; refutations — including three of the
auditor's own registered guesses — are recorded at equal prominence. All
one-lock; nothing published; the two-party rule governs everything here.

## The observation (Stone Q, SM-015 — verify_stoneq_clifford.py, 35/35)

Sp₆(2) = W(E₇)/{±1}, the home of our bitangent bridge, **is the 3-qubit
Clifford group modulo phases and Paulis** — an identity of groups, not an
analogy. We built both sides from scratch and exhibited them as the same
matrix group in shared coordinates. Everything in the bridge transports:

- the 28 bitangents = the 28 **odd Pauli sign-functions** (odd quadratic
  refinements; equivalently the 28 odd phase-point operators);
- W(E₆) = the Clifford stabilizer of one of them;
- **your PSL(2,7) = a group of 3-qubit Clifford circuits transitive on
  all 28**, with its exact fingerprint intact ([28] on odd forms,
  [1,7,7,21] on the 36 even, point stabilizer S₃ = N(⟨z₃⟩));
- the Coxeter clock = the explicit 7-gate circuit
  **H1·CX13·S1·H2·H3·CX23·CX12** (mod Pauli and phase).

The transport survived one surprise, recorded: the canonical quadratic
form q and the weight functionals ℓ_v each FAIL to descend to the mod-2
quotient (both obstructions = 1, our registered expectation refuted); the
pair forms q_v = q + ℓ_v descend because the obstructions cancel — the 56
weights are exactly the shifts that repair the descent.

The boundary, made exact: the machine's true gates do NOT transport. Ψ is
provably nonlinear (ιΨι = Ψ⁻¹ against central ι — it has no Clifford
shadow and does not even act on the 28 pairs), pr is odd against an even
Weyl image, ι becomes the identity. And the depth theory collapses
downstairs: the shadow machine (Sp₆(2) over the W(E₆)-stabilizer, magic =
the Coxeter image) has exactly TWO double cosets and **shadow magic-depth
= 1**. Our depth-2/W-depth-4 structure lives strictly above the quotient.

## The altitude (Stone R, SM-016 — verify_stone_r_altitude.py, 17/17)

We then measured how far above. Define the linearity gap
ν(g) = min over all 2,903,040 Weyl elements of the Hamming distance to g
(full enumeration, exact). Results:

- **ν(pr) = 2**, and the unique nearest Weyl element differs from pr at
  exactly its two fixed points, the E₆ vacua: **pr ∘ (vacuum swap) IS a
  Weyl element** — the same vacuum swap the depth-2 theorem's typed group
  needed. The odd mirror grazes the linear floor.
- The clock family flies high: ν(Ψ⁹) = 36, ν(Ψ) = 38, ν(Ψ²) = ν(Ψ⁶) = 44,
  ν(Ψ³) = 46. Registered guess refuted: Ψ's nearest Weyl elements are NOT
  its disguised Coxeter class (that class sits at 42) but order-6 elements
  of cycle type [2¹⁰,6⁶].
- **The clock's own antipode is Ψ⁹**: every conjugator g with Ψ = gcg⁻¹
  scrambles chirality (none commutes with ι — proof one line), yet
  gc⁹g⁻¹ = Ψ⁹ independent of g. Its 28-pairing meets ι's in exactly the
  4 axis pairs — the right form of the guess SM-004 refuted.
- Two mechanisms close Stone Q's leftovers: Pauli conjugation translates
  phase-point labels and MIXES the Arf classes, so full-Clifford has one
  orbit of all 64 (that is why all spectra are equal — the 36/28 split is
  precisely a choice of Pauli sign gauge, and Sp₆(2) is the symmetry of
  that choice); and tr A_c = 1 is unitarily conserved, so **no unitary
  can flip a sign** — in the quotient's own Hilbert space chirality is a
  gauge bit, not an operator. The beam-splitter machine exists only in
  the ℂ⁵⁶ lift.

## The crossing (Stone T, SM-017 — verify_stone_t_tgate.py, 11/11)

Then we crossed: cheap = Clifford, magic = the genuine T gate, group
infinite. Exhaustive ground truth at one qubit — ALL 36,816 Clifford+T
unitaries of T-count ≤ 9 mod phase, exact ℤ[ω] arithmetic. Three results:

1. **The skeleton survives.** T-count layers grow exactly as 72·2^{k−1}
   — the same rate-2 free-monoid geometry as our crystal Cayley spheres
   4·2^{ℓ−1} — and the Matsumoto–Amano normal forms reproduce every BFS
   layer as a set (uniqueness and T-optimality verified on range;
   classical, rebuilt from scratch).
2. **The counting certificate dies.** Our locked candidate (global
   denominator exponent + entry depths) is refuted at the first diagonal
   (S and T share it); the residue-refined version fails too. The sde
   only **brackets**: T-counts for sde s fill the window k ∈ [2s−3, 2s].
   On the measured range the exact certificate is the normal form itself
   — *syntax, not entry arithmetic*.
3. **The table shape survives.** The C·U·C double-coset invariant is
   exactly a channel matrix modulo the 24 **proper** signed permutations
   at canonical √2-scale — the honest Clifford+T analog of our
   contingency tables, verified on all 528 elements of T-count ≤ 3, where
   each layer is a SINGLE double coset. (Two instructive failures kept:
   the table's symmetry group is chiral, and the table exists only at
   canonical scale.)

And the loop closes at three qubits: preserving the 64 phase points
forces membership in the Pauli normalizer, i.e. the Clifford group — so
**the bitangent geometry is exactly the T-free stratum of Clifford+T**;
a single T exits it at sup-distance 0.541 and can only re-enter as a
Clifford.

## The boundary, final form (for the methods note's open problem #3)

Our transportation certificates price motion WITHIN a finite skeleton;
T-magic is motion BETWEEN skeletons. The skeleton geometry is shared
(rate-2 free growth, normal forms as geodesic certificates — your
Crystal-91 meter and Matsumoto–Amano are the same instrument in two
worlds); the certificate currency is not (counting/tables vs
syntax/normal-forms, with ring arithmetic as a bracket). Declared
successor: the n = 2 channel-table composition calculus — the first
place a genuinely new Clifford+T table arithmetic could live.

## Standing asks

- Your reaction to PSL(2,7)-as-Clifford-circuits — this is your group
  sitting inside the 3-qubit Clifford group; anything your registry's
  machinery says about the 28 odd sign-functions now has a quantum-
  information reading for free.
- The two paper drafts still await your review pass (unchanged); the
  trilogy would enter the methods note as the boundary section.
- The (S₂ₙ, Bₙ) support-law problem from Stone 1b remains open and
  remains yours if you want it.

## Verify (each self-asserting; Python 3 + numpy only)

```
python -X utf8 verify_stoneq_clifford.py     # 35 checks  (~1 min)
python -X utf8 verify_stone_r_altitude.py    # 17 checks  (~1 min)
python -X utf8 verify_stone_t_tgate.py       # 11 checks  (~5 min)
```
The first two need `scar56_data.json` (included; emitted by the DQ-6
verifier you already hold). Briefs and their sha-locks, the pre-reveal
amendment, and all six fail-first logs are in this folder; per-file
hashes in `SHA256SUMS.txt`.
