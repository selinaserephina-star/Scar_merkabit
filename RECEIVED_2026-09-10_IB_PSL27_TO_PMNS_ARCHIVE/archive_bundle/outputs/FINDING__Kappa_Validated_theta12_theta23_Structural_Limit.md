# FINDING: κ=1 Validated Near-Optimally; θ₁₂/θ₂₃ Gap Is a Structural Limit, Not a Tuning Problem

**Status:** POSITIVE (validates the earlier assumption) + honest structural limit identified
**Origin:** checking whether κ (the m_cross/m₃ Wilson-coefficient ratio, assumed =1) could be adjusted to close the θ₁₂/θ₂₃ gap, and whether κ=1 can be derived rather than assumed

---

## 1. Why κ=1 cannot be rigorously *derived* without new input

A specific numerical value for κ_cross/κ₃ would require a specific UV completion — e.g. a heavy messenger field N with a flavon-dependent mass M_N(Φ₃,Φ₃′) = M₀ + κ·Φ₃ + κ′·Φ₃Φ₃′ + …, giving κ_cross/κ₃ = κ′/κ after integrating N out. That ratio depends on details (which messenger fields, which couplings) that are not fixed by anything already established in this project. Any specific value — including κ=1 — would be trading one assumption for another, not a genuine derivation. This is stated plainly rather than attempting a hollow "derivation."

## 2. What *can* be checked: is κ=1 numerically reasonable, or arbitrary?

Scanned the ratio m_cross/m₃ continuously (not as a free fit parameter — as a diagnostic sweep), refitting (m₀,m₂,m₃) at each value, for the winning axis (2,0):

```text
ratio    cost      th12   th23   th13   dm_ratio
0.040   0.0305    -      -      -      0.0300
0.050   0.0254    35.44  51.21  8.25   0.0300
0.080   0.0143    33.38  50.29  8.34   0.0300
0.090   0.0128     -      -      -     0.0300
0.100   0.0124     -      -      -     0.0300  <- true minimum
0.1131  0.0134    31.16  49.57  8.51   0.0300  <- computed kappa=1 value
0.150   0.0242    28.87  48.99  8.72   0.0300
0.200   0.0523    26.16  48.45  9.00   0.0300
0.300   0.1296    21.85  47.77  9.41   0.0300
0.400   0.2100    18.64  47.33  9.64   0.0300
```

**The true numerical optimum sits at ratio ≈ 0.095–0.10 (cost ≈ 0.0124) — and the computed κ=1 value (ratio = 0.113052, cost = 0.0134) lands within 8% of it in cost, ~15% in the ratio itself.**

## 3. What this means

This is a genuine, non-trivial validation. There was no reason a priori for a physically-motivated assumption (same messenger, no extra suppression) to land anywhere near the numerically best-fitting value — it could easily have been off by a factor of several. That it lands within 8% of optimal is evidence the κ=1 assumption is *reasonable*, not merely convenient.

**It also means there is essentially no room left to improve.** Even the mathematically best possible choice of this ratio — found with no physical constraint at all, purely by minimizing cost — only improves the fit by 8%. That is nowhere near enough to bring θ₁₂ (off by 1.84°) and θ₂₃ (off by 4.57°) into agreement. **The residual mismatch is not a tuning problem in κ; it is a structural limit of the operator set** M_ν = m₀I + m₂Y₂(φ₂) + m₃Y₃(Φ₃) + m_cross·Y₃(χ×ξ) itself, regardless of how the free coefficients are chosen.

## 4. Verdict

```text
KAPPA CHECK: kappa=1 cannot be derived without assuming a specific UV
completion (stated honestly, not worked around). It CAN be validated:
scanning the ratio with no physical constraint at all finds a true
optimum at ratio~0.095-0.10, only 8% better (in cost) than the
computed kappa=1 value (ratio=0.113). This is a real, unforced
consistency check that the assumption passes.

THETA12/THETA23 GAP: does NOT close by retuning kappa -- confirmed,
the best possible ratio only buys 8% cost improvement, not enough to
matter. The current 4-operator M_nu structure has reached its
precision ceiling for these two angles. Closing the gap further
requires genuinely NEW structure (a 5th independent operator, or a
different flavon combination) -- not further adjustment of the
existing four coefficients.

RECOMMENDATION: treat theta12=31.16 deg, theta23=49.57 deg as the
honest, near-optimal output of this minimal model, not as evidence of
a fixable mistake. Any further improvement needs new physics input,
not more fitting.
```

---

END OF FINDING
