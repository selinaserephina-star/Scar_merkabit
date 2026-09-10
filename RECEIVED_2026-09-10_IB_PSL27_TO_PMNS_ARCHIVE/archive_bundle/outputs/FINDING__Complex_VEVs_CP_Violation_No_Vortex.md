# FINDING: Complex VEVs Generate Real CP Violation (J≠0) — But No Mathematical "Vortex" Exists in Phase Space

**Status:** Steps 1–7 are genuine, verified physics (POSITIVE). Steps 8–9 (vortex interpretation) are RULED OUT by basic calculus, not just absent by inspection.
**Model:** established (2,0)-axis, computed-κ neutrino sector, now with complex VEVs

---

## 1. Complex VEVs

Only 3 of the nominal 8 phases are physically meaningful — the other 5 components (φ₁, χ₁, χ₂, ξ₂, ξ₃) are exactly zero at this vacuum, and a phase on a zero magnitude has no effect:

```text
phi2 = eps * e^{i*alpha2} * (0,1)   -- alpha2 on the nonzero component
chi  = eps^2 * c3  * e^{i*beta3}  * (0,0,1)   -- beta3 on chi3 (Phi3, axis 2)
xi   = eps   * c3' * e^{i*gamma1} * (1,0,0)   -- gamma1 on xi1 (Phi3', axis 0)

At alpha2=beta3=gamma1=0.1 rad:
  phi2 = 0.059700 + 0.005990j
  chi3 = 0.001922 + 0.000193j
  xi1  = 0.112488 + 0.011286j
```

Neutrino sector correctly rebuilt via **Takagi decomposition** (M_ν is now complex symmetric, not real symmetric — verified the recipe on an independent test matrix to machine precision before use).

## 2–3. Charged-lepton masses

Unchanged to displayed precision: 1776.86, 105.658, 0.511 MeV — expected, since singular values of Y_T are insensitive to an overall rephasing structure of this kind at this order.

## 4–6. PMNS, Jarlskog invariant, δ_CP

```text
At alpha2=beta3=gamma1=0.1 rad:
  theta12 = 31.46 deg  (baseline 31.16)
  theta23 = 49.54 deg  (baseline 49.57)
  theta13 =  8.42 deg  (baseline  8.51)

  J = 2.04e-3          (baseline: EXACTLY 0)
  delta_CP ~ 176.3 deg (or 3.7 deg -- arcsin two-fold ambiguity)
             (baseline: EXACTLY 180 deg)
```

**J ≠ 0 confirmed. δ_CP moved measurably away from the real-VEV value of 180°.** This is a real, mechanical consequence of complexifying the VEVs — no surprise mathematically (a real PMNS matrix requires real inputs; breaking that reality breaks J=0), but a genuine, computed confirmation, not an assumption.

## 7. Which phase drives J?

```text
dJ/d(alpha2) = -0.934   [phi2's phase]      -- 90.5% of the dominant scale
dJ/d(beta3)  = +1.033   [Phi3's phase]      -- 100% (largest)
dJ/d(gamma1) = -0.070   [Phi3''s phase]     --  6.8% (much weaker)
```

**β₃ (Φ₃'s phase) and α₂ (φ₂'s phase) dominate; γ₁ (Φ₃′'s phase) is almost an order of magnitude weaker.** This has a plausible structural reason: Φ₃′'s magnitude (ε¹) is already the dominant VEV in the cross-term construction, and its phase mostly rotates a term whose *magnitude* effect was already large, while φ₂ and Φ₃ sit in the specific combinations that directly build the CP-odd invariant.

One secondary note: the γ₁-only scan shows a sign change between phase 0.10 and 0.20 (not simple linear growth) — a real but currently unexplained non-monotonicity in the weakest-contributing phase; noted here rather than investigated further, since it doesn't affect the ranking.

## 8–9. Is there a "vortex" here? — No, and this time it's provable, not just absent

J(α₂,β₃,γ₁) is a **scalar** function of three real parameters. The only mathematically well-defined "vector field" one could construct from it is its own gradient, ∇J = (∂J/∂α₂, ∂J/∂β₃, ∂J/∂γ₁) — and:

```text
curl(grad f) = 0, IDENTICALLY, for any twice-differentiable scalar f.
```

This is Clairaut's theorem (equality of mixed partial derivatives) — a mathematical certainty, true for *any* scalar function whatsoever, not a property that depends on this model. **A gradient field cannot have circulation or a vortex, by definition — asking whether J's phase-space gradient has a "vortex" is asking whether a gradient can fail to be a gradient.** Numerically evaluating curl(∇J) gives small but nonzero noise (5×10⁻³ and 8×10⁻⁶ at two test points) — this is exactly the expected floating-point/truncation artifact of a *nested* finite-difference calculation (differentiating a numerically-differentiated quantity again), not a real effect; it should be read as confirmation of zero, not evidence against it.

**This is a stronger negative result than the previous vortex test.** That one found no vortex-type object *present* in the model. This one shows that even the most natural candidate construction (treating J as a potential and taking its gradient) is **mathematically guaranteed to be curl-free**, regardless of anything about this specific model's physics. There is no version of "circulation in phase space" available here to find.

## 10. Verdict

```text
PHYSICS (steps 1-7): REAL AND CONFIRMED.
  Complex VEVs -> J = 2.04e-3 (nonzero), delta_CP shifts from 180 deg by
  a few degrees, at O(0.1 rad) phases. Phi3's phase (beta3) and phi2's
  phase (alpha2) dominate; Phi3''s phase (gamma1) contributes ~7x less.
  Charged lepton masses and mixing angles stay close to the established
  real-VEV values, as expected for small phase perturbations.

VORTEX INTERPRETATION (steps 8-9): RULED OUT, not just unsupported.
  The natural candidate vector field (grad J) is PROVABLY curl-free by
  a basic calculus theorem, independent of any detail of this model.
  There is no mathematical sense in which J's variation over phase
  space constitutes a vortex or has circulation. This is a stronger,
  more definitive negative than the earlier "no vortex object found"
  result -- here, even the most favorable possible construction is
  ruled out on general grounds.

RECOMMENDATION: report J(alpha2,beta3,gamma1) and its phase-sensitivity
ranking as a genuine, useful physics result (a real, falsifiable
prediction for delta_CP once phases are specified by some future
mechanism) -- and drop the vortex framing entirely, now with a proof
rather than just an absence of evidence.
```

---

END OF FINDING
