# FINDING: φ₂'s Direction Still Not Derivable from Simple 2⊗Φ₃(′) Cross Terms — Structural Reason Identified

**Status:** NEGATIVE, with a clean structural explanation (not a dead end from lack of trying)
**Origin:** third attempt to derive φ₂'s (0,ε) direction from an F-term, using properly-computed 2⊗3 and 2⊗3′ Clebsch-Gordan invariants (rather than guessing self-invariants)
**Supersedes:** the earlier (Φ₃Φ₃)₂ self-invariant attempt (also failed, reported previously)

---

## 1. Method

Built the genuine cross-invariants this time, not self-invariants: computed the explicit isotypic projectors for the "3" channel inside 2⊗3 and inside 2⊗3′, using the already-validated PSL(2,7) position-basis matrices (Hφ2, HΦ3, Hgen=HΦ3′). Found the intertwiners aligning each abstract channel to the established position-basis labeling (residuals 2–15 × 10⁻¹⁵, same rigor as the rest of this session's basis work). This gives explicit 3×2 matrices M(χ) and M(ξ) mapping φ₂ → the "3"-channel output, for each fixed Φ₃ or Φ₃′ axis.

## 2. Structural finding: rank 1, always

For every axis choice tested (all 3, both channels), **M is exactly rank 1** (second singular value ~10⁻¹⁶, not just small):

```text
(phi2 x Phi3, axis 2)_3:    rank 1, kernel direction (-0.510, -0.860)  [angle 239.4 deg]
(phi2 x Phi3', axis 0)_3:   rank 1, kernel direction ( 0.872,  0.490)  [angle 29.3 deg]
```

This is not a numerical accident — it follows because Φ₃ (or Φ₃′) has only **one** nonzero component (axis-aligned), and the bilinear map's image is confined to a single output-position matching that same axis index (verified: χ on axis k → output nonzero only in position k). A single-axis input can only ever extract **one** real linear combination of φ₂'s two components — never enough to pin down a 2-dimensional vector on its own.

## 3. Consequence: neither single channel, nor both together, can fix φ₂

- **One channel alone:** gives 1 constraint on a 2-dimensional φ₂ — a line, not a point. Insufficient by construction.
- **Both channels combined** (forcing both cross-terms to vanish simultaneously, the natural next attempt): the two kernel directions (239.4° and 29.3°) are **not parallel**, so requiring both is two independent linear conditions on 2 unknowns — which forces **φ₂ = 0 exactly**, the same dead end found for the naive self-alignment attempt at the start of the vacuum-alignment work.
- **Neither kernel direction, nor their orthogonal complements, land anywhere near the required 90°/270°** (they land at 239°/59° and 29° respectively) — so even a looser "align with the active direction instead of the kernel" version doesn't recover the target angle.

## 4. What this rules out, concretely

Any mechanism built from a **single bilinear invariant** of the form (φ₂ ⊗ Φ₃)_channel or (φ₂ ⊗ Φ₃′)_channel — self- or cross-coupling, channel 2, 3, or 3′ — is now checked (across this and the previous session's attempt) and found structurally unable to fix φ₂'s direction to the required point, either because it vanishes identically, is degenerate with an existing parameter, or (this session) is rank-deficient by one full dimension.

## 5. What remains untried

- **Trilinear invariants**: e.g., (φ₂ ⊗ Φ₃ ⊗ Φ₃′) contracted to a singlet, which could supply a genuinely 2-dimensional (rank-2) constraint on φ₂ by combining information from both flavons in a single term rather than two separate linear ones.
- **A dedicated messenger field** whose own alignment (via its own F-terms) happens to select 90° directly, with φ₂ then locked to it by a simple mass-mixing term — shifting the problem rather than solving it via Φ₃/Φ₃′ alone.
- Accepting that φ₂'s direction, unlike Φ₃'s and Φ₃′'s, may need a **qualitatively different symmetry input** (not S₄/V₄ representation theory alone) — e.g., tied to whatever breaks the modulus/racetrack sector that already fixes ε, rather than to the discrete flavon sector.

## 6. Verdict

```text
phi2 DIRECTION: still not derived. Three independent, honestly different
mechanisms have now been tried and rejected across two sessions:

  1. Self-alignment (phi2 phi2)_2 = 0        -> collapses to phi2=0
  2. phi2 ~ (Phi3 Phi3)_2 self-invariant     -> predicts 120 deg, wrong
  3. phi2 ~ (phi2 x Phi3(or Phi3'))_3 cross  -> rank-1, structurally
                                                 insufficient; combined,
                                                 collapses to phi2=0

This is now a well-characterized open problem, not an unexplored one.
The (0, eps) direction remains fixed by continuity with the exact
charged-lepton mass fit -- an input, not yet a derived output -- and the
next attempt should go outside simple bilinear S4-covariant invariants
of Phi3/Phi3' (see SS5), not repeat this family of mechanisms again.
```

---

END OF FINDING
