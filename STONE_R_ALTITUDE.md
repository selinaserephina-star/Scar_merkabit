# STONE R — THE ALTITUDE
**Scar_merkabit joint lane · 2026-08-30 · SM-016**
**Brief:** `BRIEF_STONE_R_ALTITUDE.md`, sha-locked `57db98a7…f7a5` before the
verifier existed. **Verifier:** `verify_stone_r_altitude.py` — **17/17**
(two fail-first logs kept: `_FAILFIRST.log`, `_FAILFIRST2.log` — each holds
a guess dying on its own data).

## §0 Discipline

Compute, never assert. TWO of the auditor's guesses refuted this run, both
on the record at equal prominence (§3). Rule 3; not RH/GRH; no physical
claim; ν is OUR definition (a Hamming distance to a subgroup, in the μ
family), not claimed standard. ONE LOCK.

## §1 One paragraph

Stone Q showed the machine's priced structure lives strictly above its
Clifford quotient. Stone R measures the altitude. Define the **linearity
gap** ν(g) = min over all 2,903,040 Weyl elements w of d_H(g, w) — the
distance from a gate to the Clifford floor, computed EXACTLY by full
enumeration. Result: the floor is not uniformly far away. **The odd mirror
grazes it: ν(pr) = 2**, and the unique nearest Weyl element differs from pr
exactly at the two E₆ vacua — **pr ∘ (vacuum swap) IS a Weyl element**: the
mirror is one vacuum-trade away from linear (the very swap SM-009's typed
group needed for depth 2). **The clock family flies high**: ν(Ψ) = 38,
ν(Ψ⁹) = 36, ν(Ψ²) = ν(Ψ⁶) = 44, ν(Ψ³) = 46 — and the clock's nearest
linear neighbours are NOT its own disguised Coxeter class (registered guess
refuted: minimizers have type [2¹⁰,6⁶], char poly x⁷+2x⁶−3x⁴−3x³+2x+1,
distance 38, while the Coxeter class sits at 42). En route: every
conjugator g with Ψ = g c g⁻¹ scrambles chirality (none lies in B₂₈), yet
g c⁹ g⁻¹ = Ψ⁹ independent of g — **the clock's own antipode is Ψ⁹**, and
its matching touches ι's on exactly the 4 axis pairs, turning SM-004's
refuted guess into the right theorem. Finally both Stone Q opens close:
the one-spectrum [obs] is explained (Paulis translate phase-point labels
and mix the Arf classes — the full Clifford group has ONE orbit of 64;
the 36/28 split is a choice of Pauli sign gauge), and sign flips are not
merely expensive but **unitarily impossible** downstairs (tr A_c = 1 is
conserved) — chirality in the quotient's Hilbert space is a gauge bit,
not an operator.

## §2 The altitude table (exact, full enumeration)

| gate | ν = min d_H to W(E₇) | agreement | minimizers | nearest class |
|---|---|---|---|---|
| pr | **2** | 54/56 | 1 | pr∘(vacuum swap), even, IN W(E₇) |
| Ψ⁹ | 36 | 20/56 | 1 | — |
| Ψ | **38** | 18/56 | 2 | type [2¹⁰,6⁶], char poly x⁷+2x⁶−3x⁴−3x³+2x+1 |
| Ψ² | 44 | 12/56 | 1 | — |
| Ψ⁶ | 44 | 12/56 | 3 | — |
| Ψ³ | 46 | 10/56 | 2 | — |

Contact geometry of Ψ's minimizers: agreement points spread (2,4,5,7) over
the clock's orbits [2,18,18,18] — scattered, not orbit-aligned (measured
after the single-orbit guess died; see §3). Direct anchors:
d_H(Ψ, c) = 42; d_H(Ψ⁹, ι) = 48.

**Reading:** the depth ladder (Ψ-depth 2 < W-depth 4) prices gates by the
machine's own grammars; ν prices them by distance to the LINEAR world.
The two orders disagree: pr (free in both grammars) is almost linear;
the clock (the sole magic source) is almost maximally nonlinear, and its
powers are farther still. *Structure is free and nearly linear; time is
expensive and deeply nonlinear.*

## §3 Refutations, at equal prominence

1. **Registered guess (RB2) REFUTED**: "some Ψ-minimizer lies in the
   disguised Coxeter class." False — the Coxeter class is at 42, the true
   minimum 38 is achieved by order-6 elements of type [2¹⁰,6⁶] only.
2. **Post-hoc guess REFUTED on its own first run**: "the 18 agreement
   points form one full clock orbit." False — spread (2,4,5,7) over the
   four orbits. Both fail-first logs kept.

## §4 The clock's own antipode (RB3)

Ψ = g c g⁻¹ (explicit g by cycle alignment; verified). No conjugator lies
in C(ι) = B₂₈ — else Ψ would commute with ι against ιΨι = Ψ⁻¹: **every
disguise scrambles chirality.** But c⁹ = w₀ = ι gives g c⁹ g⁻¹ = Ψ⁹ for
EVERY conjugator: the clock carries its own antipode ι_Ψ = Ψ⁹,
conjugator-independent. Its matching M_Ψ shares exactly **4/28** pairs
with ι's M₀ — the axis pairs of DQ-4 — so SM-004's refuted "Ψ⁹-pairing =
ι" resolves into: Ψ⁹-pairing = the *conjugated* antipode, meeting ι only
on the axis. [obs]: ι and Ψ⁹ commute; their interference involution
ι∘Ψ⁹ has cycle type [1⁸,2²⁴], fixing exactly the 8 axis points.
τ(Ψ) = [1,9,9,9] reproduced from M₀ ∪ ΨM₀ (SM-009 anchor).

## §5 Gauge and obstruction (RB4 — Stone Q's two opens closed)

- **Why one spectrum:** conjugating T_x by a Pauli T_a gives
  (−1)^{ω(a,x)}T_x (verified on operators), which translates phase-point
  labels c ↦ c ⊕ swap(a). Translations are transitive on the 64 labels
  and MIX the Arf classes ⇒ the full 3-qubit Clifford group (with Paulis)
  has ONE orbit of phase points ⇒ all 64 spectra equal. The 36/28 split —
  the entire bitangent skeleton — is what remains after **choosing a Pauli
  sign gauge**; Sp₆(2) is the symmetry of that choice.
- **Why chirality dies:** tr A_c = 1 for all 64, and unitary conjugation
  preserves trace, so no unitary sends any A_c to −A_{c'}. The 56 = 28
  odd forms × sign exists only as a set downstairs: ι and the whole
  beam-splitter machine (SM-014) have no unitary-conjugation realization
  on phase points. k(−I) = 4 and W-depth 4 are purchases only the ℂ⁵⁶
  lift can even offer.

## §6 Grades

| unit | grade |
|---|---|
| conjugator + no-B₂₈ corollary | [C] with one-line proof |
| the six ν values, minimizer counts, witnesses | [C] exact, full enumeration |
| Coxeter-class guess refuted; single-orbit guess refuted | refutations, recorded |
| ι_Ψ = Ψ⁹ conjugator-independent; 4/28 axis overlap; interference [1⁸,2²⁴] | [C] / [obs] |
| Pauli gauge transitivity (one orbit of 64) | [P] classical mechanics of the Pauli group, verified here |
| trace obstruction (no unitary sign flip) | [C] (elementary once stated) |

## §7 Not-claims

ν is a house definition; no claim of standard status. No Clifford+T
claim. W-conjugacy of witnesses is not claimed from cycle type (char-poly
evidence only). The gauge/obstruction facts are elementary; their value
is closing Stone Q's opens, nothing more. No physics.

## §8 Reproduce

```
python -X utf8 verify_stone_r_altitude.py   # 17 checks, ~1 min
```
Requires `scar56_data.json`. Enumeration: BSGS transversal chain
[56,27,16,10,6,2], numpy composition, 56 chunks x 51,840 rows.
