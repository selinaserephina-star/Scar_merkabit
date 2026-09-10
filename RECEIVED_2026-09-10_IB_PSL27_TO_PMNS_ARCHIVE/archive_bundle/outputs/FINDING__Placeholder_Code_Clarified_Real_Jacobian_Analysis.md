# FINDING: Shared Code Was an Unfilled Placeholder — Rigorous Jacobian Analysis Redone on the Actual Model

**Status:** Corrects a misunderstanding, then delivers genuine new information via a better method
**Origin:** the shared Sage/Python code's `Mnu(p)` and `Ml(p)` functions are explicitly labeled placeholders in their own docstrings and were never connected to this project's PSL(2,7)/S₄ construction. Re-ran the same (good) Jacobian-rank/null-direction methodology on the actual model instead.

---

## 1. Why the shared code's results are not about this project

```python
def Mnu(p):
    """
    INSERT YOUR ACTUAL NEUTRINO MASS MATRIX HERE.
    ...
    The matrix below is ONLY a runnable placeholder.
    """
    return np.array([[m0, mcross, 0], [mcross, m2, 0], [0, 0, m3]])

def Ml(p):
    return np.diag([abs(y2), abs(c3), abs(c3p)])
```

Neither function uses Y₂(φ₂), Y₃(Φ₃), or the Φ₃⊗Φ₃′ cross product — `Ml` treats y₂,c₃,c₃′ as the three lepton masses directly, not as VEV/coupling parameters feeding an SVD. `A_fixed` sets m₃=0.3, m_cross=0.05 arbitrarily (not derived). Targets differ (θ₂₃=49.20° vs the 45.0° used throughout this project). The reported Variant A result (rank 4, nullity 1, null direction (0,0,0,1/√2,1/√2) meaning δm₀=δm₂) is fully explained by this placeholder's own structure: y₂,c₃,c₃′ biject onto the 3 mass targets trivially, leaving 2 parameters (m₀,m₂) chasing 1 leftover target (θ₁₂) — a textbook 2-into-1 flat direction, with no connection to the real model.

**This is not a criticism of the methodology — it's genuinely good (Jacobian rank + explicit null-direction scan is better than my earlier random-restart approach). It just wasn't pointed at the right matrix.**

## 2. Redone properly, on the actual model

Same method, `Mnu = m₀I + m₂Y₂(φ₂) + m₃Y₃(Φ₃) + m_cross·Y₃(χ×ξ)` (the real, established construction), χ-axis=2/ξ-axis=0.

**Baseline (4 params, 4 targets: θ₁₂,θ₂₃,θ₁₃,ratio):**
```text
best cost = 3.884e-3  (matches every earlier random-restart result exactly)
Jacobian singular values: [0.309, 0.0299, 0.00137, 1.5e-13]
rank = 3, nullity = 1   <- a genuine flat direction, not previously isolated explicitly

null direction (m0,m2,m3,mcross) = (0.051, 0.995, -0.007, 0.088)
   -- almost pure m2 (the Y2(phi2) diagonal-term coefficient)

Scan along this direction: cost UNCHANGED to 15 significant figures
(3.88368485e-03 at every t from -0.5 to +0.5) -- a textbook flat direction.
```

**This is a genuine, new, useful result about the already-established model**: even the "healthy" 4-parameters-for-4-targets construction has one exactly flat direction, dominated by m₂. This explains, precisely, why cost never reached zero even with nominally matched parameter/target counts — something the earlier random-restart scans showed empirically (cost floor ≈0.0039) but never diagnosed structurally.

**Variant-B analog (5 params — adding m₅ — 5 targets: angles+ratio+Σm_ν=0.07 target):**
```text
best cost = 0.265  (poor -- consistent with the earlier honest trade-off finding)
Jacobian singular values: [0.0396, 0.00573, 0.00180, 0.000202, 5.9e-14]
rank = 4, nullity = 1   <- STILL a flat direction, not lifted
```

**The specific 5th operator (φ₂⊗(χ×ξ)) does not lift the degeneracy** — confirmed now with a smallest singular value of 5.9×10⁻¹⁴ (numerically exactly zero), not just "still a bit uncertain from random restarts." This matches and sharpens the earlier trade-off finding (§ *5th Operator Trade-off*): it isn't only that θ₁₂ suffers when Σm_ν is pushed down — the Jacobian shows the underlying map is still rank-deficient by one, meaning there's a whole direction in the 5-parameter space that this specific operator combination cannot control at all.

## 3. Verdict

```text
The shared Sage code's Variant A result is real and internally consistent
-- but for an unfilled placeholder matrix, not this project's model.
Nothing about it should be carried over.

Applying the SAME (good) method to the actual model gives a genuinely new
result: the baseline 4-parameter neutrino fit has an exact flat direction
dominated by m2, previously known only as "cost floors at 0.0039" without
a structural explanation. The 5th operator tested earlier does not lift
this -- confirmed rigorously now, not just empirically.

This means: whatever new operator eventually fixes theta12/theta23 (or
the mass tension) needs to specifically engage the m2/phi2-related flat
direction identified here, not just add another generic term. That is
new, actionable information this exercise produced -- a genuine byproduct
of chasing down what turned out to be a false lead.
```

---

END OF FINDING
