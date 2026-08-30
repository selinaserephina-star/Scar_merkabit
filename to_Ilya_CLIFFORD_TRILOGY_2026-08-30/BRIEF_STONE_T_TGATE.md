# BRIEF — STONE T: FIRST CONTACT WITH THE T GATE
**Scar_merkabit joint lane · staged 2026-08-30 · Selina's word: "fork 1 it is"**
**SHA-locked before one line of the verifier exists.**

## 0. Discipline

Compute, never assert; refutations at equal prominence, including this
brief's own registered protocol outcomes; Rule 3; not RH/GRH; no physical
claim; classical results (Matsumoto–Amano normal forms, Kliuchnikov–
Maslov–Mosca exact synthesis, the channel representation of Gosset–
Kliuchnikov–Mosca–Russo) cited as classical — this stone REBUILDS them
from scratch on its range and asks the house's own composition question
against them. Deviations = dated AMENDMENT before reveal. ONE LOCK.

## 1. The question

Stones Q and R proved the program's depth certificates live above the
Clifford quotient and located the boundary: any Clifford+T certificate
must engage the unitary level. Stone T crosses the boundary at the
smallest honest scale. Cheap = the Clifford group; magic = the genuine
T gate; the group ⟨Clifford, T⟩ is INFINITE — counting arguments die, and
the certificate currency must change. The stone asks, on exhaustively
enumerated ground truth:

1. What replaces the contingency table? (Candidate: the channel matrix up
   to signed permutations — Cliffords act on Pauli axes as signed
   permutations, so the C·U·C double-coset invariant has EXACTLY the
   "matrix modulo row/column symmetry" shape of SM-009's tables.)
2. What replaces the counting certificate? (Candidate: ring arithmetic —
   the denominator exponent of the entries over ℤ[ω], ω = e^{iπ/4},
   with √2 = ω − ω³.)
3. Does the machine's word geometry survive? (The crystal's gate graph is
   locally free with sphere growth 4·2^{ℓ−1}, CN-012. The 1-qubit
   Clifford+T world is conjectured — classically, via Matsumoto–Amano —
   to be a rate-2 free-monoid skeleton too. Same skeleton, different
   currency?)
4. Where does the bitangent world sit inside Clifford+T? (Candidate
   theorem: preserving the 64 phase points ⟺ Clifford — the skeleton is
   exactly the T-free stratum.)

## 2. Constructions (Python 3 + numpy, exact ring arithmetic, no CAS)

C1. **The ring.** ℤ[ω] as integer 4-tuples, ω⁴ = −1; multiplication,
    conjugation, multiplication and exact division by √2 = ω − ω³;
    unitaries as 2×2 matrices over ℤ[ω] with global denominator √2^s,
    fully reduced; global-phase canonicalization (mod ⟨ω⟩).
C2. **Ground truth by BFS.** Layer 0 = the 24 Cliffords mod phase
    (generated from H, S); layer k+1 = canon(Clifford·T·layer k) minus
    earlier layers — the exact T-count-k sets C(TC)^k, enumerated
    to depth K (K ≥ 7 targeted; the run declares the K it reaches, cap by
    element count; runtime is the only bound).
C3. **Matsumoto–Amano forms.** Words T^ε(HT | SHT)*·Clifford enumerated
    to the same depth; counts and SETS compared with the BFS layers.
C4. **The channel representation.** M(U) on the 3 Pauli axes, entries
    exact in ℤ[1/√2]; Clifford action = the 48 signed permutations;
    canonical form by minimization; double-coset ground truth by explicit
    576-product orbits on a declared sample (all elements with T-count ≤ 4).
C5. **The 3-qubit skeleton theorem.** The normalizer argument (preserving
    {±T_x} under conjugation ⟺ Clifford, by definition of the
    normalizer) + computational spot-checks that T·A_c·T† leaves the
    phase-point set (numpy, the Stone Q operators).

## 3. Registered bars and expectations

**TB1 [ring gates].** Exact-arithmetic self-checks: √2 multiply/divide
round-trip, unitarity of H, S, T, H² = S⁴ = I mod phase, |Cliff₁| = 24
mod phase. EXPECT PASS.

**TB2 [the skeleton].** BFS layers and Matsumoto–Amano words agree in
count AND as sets for every reached k (normal-form uniqueness = the
free-monoid skeleton, verified on range); asymptotic layer-growth ratio
→ 2. EXPECT PASS. The rhyme with CN-012 (crystal spheres 4·2^{ℓ−1}:
same rate-2 free skeleton, different world) is recorded as [obs]
LANGUAGE, not as a mathematical identification.

**TB3 [REGISTERED HEADLINE — the denominator certificate].** Protocol,
locked here: from the fit window T-count ≤ 3, build the map
(invariant → T-count) where the candidate invariant is (global sde s,
sorted per-entry √2-depths). If the map is single-valued on the fit
window, LOCK it and test on the window 4 ≤ k ≤ K: PASS = the invariant
determines T-count exactly on the whole test window; any collision or
exception is recorded at equal prominence as the finding (the certificate
located as incomplete, with the witnesses printed). No numeric law is
guessed in advance; the data speaks.

**TB4 [the table shape].** On the declared sample (k ≤ 4): channel
canonical forms coincide ⟺ same C·U·C double coset (ground truth by
explicit orbit). PASS = the "Clifford+T contingency table" is exact on
range. Graded [C on range]; the general claim stays open.

**TB5 [the skeleton theorem].** Preserving the 64 phase points under
conjugation ⟺ Clifford ([P] normalizer argument, stated with the
definition) + spot-checks: T·A_c·T† is not ±A_{c'} for any c'. EXPECT
PASS. Consequence recorded: the bitangent geometry is EXACTLY the T-free
stratum of Clifford+T; T-magic exits the finite skeleton instantly,
while the 56-machine's clock-magic stays inside S₅₆ — the two magics are
different in KIND (counting vs ring arithmetic), which is the honest
final form of open problem #3's boundary.

## 4. Honest scope

n = 1 exhaustively on range; n = 3 only for the [P] skeleton theorem and
spot-checks. NO n = 2 composition calculus this stone (declared
successor: the C₂ channel-table composition experiment). No claim of
novelty for MA/KMM/GKMR content — the stone's own contributions are: the
verified-on-range identification of the double-coset invariant with the
table shape (TB4), the locked fit/test protocol outcome (TB3), the
skeleton theorem framing on OUR objects (TB5), and the boundary statement
for the methods paper. No physics.

## 5. Deliverables

verify_stone_t_tgate.py; STONE_T_TGATE.md; registry SM-017 + changelog
v0.15 (tail checked: v0.14/SM-016 current, parallel session noted); KCP
units; git commit; memory + synthesis line. Send remains Selina's word.
