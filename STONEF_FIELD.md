# Stone F(a) — the field machine: standing waves of the 56

**Scar_merkabit lane · 2026-08-30 · verifier:** `verify_stonef_field.py`
(13 checks, all passing). Rule 3 note: "field", "wave", "chirality" are
computational role names throughout — this is the linear lift ℂ⁵⁶ of the
token machine, nothing more and nothing less.

## 1. The spectrum — and the CSP census unmasked

The clock Ψ (orbits [18,18,18,2]) has standing-wave spectrum: **every 18th
root of unity, multiplicity 3, except +1 and −1 which have multiplicity 4**
(total 56) [C, exact + numerically confirmed]. Each eigenmode is a Fourier
wave on one clock orbit: a pattern the tick cannot move, only re-phase.

The machine's oldest invariant is thereby revealed: the CSP census
[56, 0, 2, 0, 2, …] **is the trace formula of the standing-wave spectrum**
— |Fix(Ψᵈ)| = Σ λᵈ over the 56 wave-eigenvalues [C]. The tamper-evident
checksum was spectral bookkeeping all along; the founding intuition "the
merkabit is about standing waves" is, in its computational reading, a
proved statement.

## 2. Sector masses — exact orbit arithmetic

Fourier modes are flat on their orbits (|amplitude|² = 1/L), so every
wave's mass in every grammar sector is exact fractions [C]:

| orbit | length | mass in 27 / 27̄ / vac₁ / vac₂ | frames |
|---|---|---|---|
| O0 | 18 | 9/18 · 9/18 · 0 · 0 | 9 |
| O1 | 18 | 9/18 · 9/18 · 0 · 0 | 9 |
| O2 | 18 | 8/18 · 8/18 · 1/18 · 1/18 | 9 |
| O3 | 2 | 1/2 · 1/2 · 0 · 0 | 1 |

Every wave is perfectly sheet-balanced (O2's waves carry the vacua, 1/18
each). **All 28 ι-frames lie inside single clock orbits** [obs] — the frame
grammar is subordinate to the clock's orbit structure.

## 3. The clock's axis, and DQ-4 closed

- **The 2-orbit {15, 40} IS an ι-frame straddling the two sheets** [obs] —
  the clock contains exactly one frame, which it merely flips: its **axis
  frame** (not the E₆ vacua; the auditor guessed otherwise — recorded).
- **DQ-4 fully explained** [C]: ιΨι = Ψ⁻¹ (the antipode reverses the
  clock), so ι preserves each orbit as a reflection; a reflection composed
  with the half-turn Ψ⁹ fixes exactly one antipodal pair per orbit. The
  mysterious "4/28 shared pairs" = **one axis pair per clock orbit**:
  (0,55), (4,51), (12,43) in the 18-orbits, plus the 2-orbit itself.
- **pr does NOT normalize the clock** (prΨpr ≠ Ψ±¹): the mirror — zero
  magic in *both* grammars — nevertheless **mixes standing-wave
  frequencies** (orbit-overlap matrix [[6,6,4,2],[6,8,4,0],[4,4,10,0],
  [2,0,0,0]]). Free gates can still shuffle the music: magic measures
  distance from the *grammar* groups, not from the clock's spectral frame —
  a third, inequivalent notion of "structured". [obs]
- pr and ι commute [C]; ι acts as **+1 on all four constant waves** (E₊₁)
  and **−1 on all four alternating waves** (E₋₁) [C].

## 4. The Scar field sectors — chirality-odd quarks [obs, character level]

Via the bridge (any bitangent identification; DQ-1 will fix the explicit
map), the field space splits under PSL(2,7) into the ι-even and ι-odd
halves, computed exactly from the derived character table:

> **ι-even (28) = χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈  ·  ι-odd (28) = χ₃ ⊕ χ̄₃ ⊕ 2χ₇ ⊕ χ₈**

The quark sectors χ₃, χ̄₃ occur **only in the chirality-odd half**; the
vacuum sector χ₁ **only in the even half**. In Ilya's dictionary: quark
fields are chirality-odd; the vacuum is chirality-even — a theorem of the
lift, not a physics claim, and a sharp new row for the merged registry.

**ERRATUM (same day, Stone F(b), backport rule T-SC-P1).** The paragraph
above is **REFUTED for the action that actually exists**. The sign-twisted
(ι-odd = Ind sgn) module is a valid abstract PSL(2,7)-module, but it is
*not realized by the Weyl group*: PSL(2,7) is perfect, so its lift into
W(E₇) = ℤ₂ × Sp₆(2) is **unique and untwisted**. Computed with the explicit
action (`verify_stonef_b_dq1.py`, 11/11): the canonical copy has orbits
**[28, 28]** on the 56 (two bitangent sheets interchanged by ι;
weight-stabilizer S₃ — DQ-1 answered, the single-orbit prediction refuted),
and **ℂ⁵⁶ = 2(χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈)** — the ι-odd half is *isomorphic* to
the even half, and **χ₃/χ̄₃ do not occur at all**: the quark sectors of the
27 come from Lie-group embeddings (trinification), never from the Weyl
action. Bonus [obs]: a **second conjugacy class** of PSL(2,7) in Sp₆(2)
acts on the crystal as *Fano geometry doubled* (orbits [7,7,21,21], perm
char 4χ₁ ⊕ 6χ₆ ⊕ 2χ₈ — two point-actions plus two flag-actions).

## 5. What Stone F opens

(b) the explicit PSL(2,7) action on the crystal 56 (DQ-1) to make §4's
sectors coordinate-level; (c) the honest quantum lift — permutation gates
plus one genuine superposition gate on ℂ⁵⁶ — where the methods note's
unitary open problem can be attacked on our own object; (d) the artifact
panel: the 56-machine singing (spectrum + sector masses are all exact
integers over 18 — trivially renderable).

*Sealed 2026-08-30; registry row SM-012.*
