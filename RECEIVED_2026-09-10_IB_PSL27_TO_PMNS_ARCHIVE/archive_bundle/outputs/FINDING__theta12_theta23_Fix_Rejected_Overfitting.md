# FINDING: θ₁₂/θ₂₃ Precision Cannot Be Restored Without Destroying the Axis-Selection Result — Keep the Imperfect 4-Parameter Fit

**Status:** IMPORTANT NEGATIVE RESULT — a numerically "perfect" fix exists but must be rejected
**Origin:** attempt to recover θ₁₂=33°, θ₂₃=45° while keeping θ₁₃=8.5°, following up on the Φ₃⊗Φ₃′ cross-term fix
**Bottom line:** the earlier imperfect result (θ₁₂=32.71°, θ₂₃=42.24°, θ₁₃=8.45°) should stand as the honest answer. A "fix" exists but it is a textbook overfitting trap, not a real improvement.

---

## 1. Why θ₂₃ shifted the most

`Y_cross = Y3(χ×ξ)` has the explicit form (winning vacuum):

```text
[[ 0, -1,  0],
 [-1,  0,  0],
 [ 0,  0,  0]]
```

In the (τ, μ, e) generation-index ordering used throughout, this is **literally a τ–μ mixing term at the Lagrangian level** — nonzero only in the (τ,μ) block. θ₂₃ is exactly the atmospheric τ–μ mixing angle. The term that was needed to fix θ₁₃ mechanically injects τ–μ mixing as a side effect; there is no way to add it and expect θ₂₃ to sit still. This is the direct, structural answer to task step 1.

## 2. Candidates checked (per task step 2–3)

| Candidate | Nonzero at winning vacuum? | Usable in symmetric M_ν? | Result |
|---|---|---|---|
| Φ₃′² (channel 3) | No (proven previously) | — | excluded |
| (Φ₃⊗Φ₃′)₂ | **No** — checked again here, still zero (no shared nonzero index) | — | excluded |
| (Φ₃⊗Φ₃′)₃′ (symmetric) | Yes | **No** — transforms as 3′, needs the antisymmetric Y₃′ embedding, would break M_ν's required symmetry | excluded |
| Higher orders | not attempted | — | out of scope here |
| **Free φ₂ direction** | — | — | **works numerically, but see §4** |

## 3. First result: an exact 7-target simultaneous fit exists

Allowing φ₂'s direction to float (not fixed at (0,ε)) and re-solving **all 8 parameters together** (θ_φ, y₂, c₃, c₃′, m₀, m₂, m₃, m_cross) against **all 7 targets** (3 charged-lepton masses + θ₁₂, θ₂₃, θ₁₃, mass ratio) simultaneously:

```text
cost = 1.25e-19  (machine precision)

theta_phi = 85.22 deg   (phi2 direction: (0.0833, 0.9965)*eps -- a small
                          tilt away from the previous exact (0, eps))
y2=0.04871  c3=-3.4024  c3'=-2.1580
m0=-12.9905  m2=19.4266  m3=-13.4618  m_cross=-11.3536

Results:
  charged-lepton masses = [1776.86, 105.658, 0.510999] MeV  -- exact
  theta12 = 33.00000 deg   (target 33.0)
  theta23 = 45.00000 deg   (target 45.0)
  theta13 = 8.50000 deg    (target 8.5)
  ratio   = 0.030000       (target 0.03)
```

Every target matched to 5 decimal places. This directly answers task step 4 ("can varying φ₂ improve θ₂₃?") — yes, completely.

## 4. Why this must be rejected: it is not a fit, it is overfitting

The critical check (task step 6, applied to *this* new mechanism): does the axis degeneracy survive? **It does not — it is completely destroyed.** Running the *identical* 8-parameter joint optimization for **all 6 non-degenerate axis combinations** (not just the two winners):

```text
chi_ax xi_ax   best combined cost
  0     1         9.92e-18
  0     2         5.59e-18
  1     0         1.24e-19   <- previous "winner"
  1     2         5.82e-18
  2     0         2.82e-20   <- previous "winner"
  2     1         1.75e-19
```

**Every single one of the 6 combinations achieves machine-precision agreement with all 7 targets.** With 8 free parameters chasing 7 numbers, this is exactly what should be expected — a 1-parameter family of exact solutions exists for essentially any starting structure. The ability to fit perfectly no longer distinguishes anything; it is no longer evidence for (1,0)/(2,0) or against any other axis. **The entire discriminating power that was the actual result of the neutrino cross-check (the previous session's central finding) is erased by this fix.**

This is not a subtle statistical point — it is the textbook definition of overfitting: adding a free parameter until the residual vanishes, at the cost of the fit meaning anything.

## 5. Verdict

```text
theta12/theta23 PRECISION: recoverable numerically, but the fix is
REJECTED. It works via the free phi2 angle, which adds exactly enough
freedom (8 params vs 7 targets) to fit ANY axis choice perfectly,
destroying the axis-selection result this whole line of investigation
was built to establish.

DECISION: do not adopt the free-phi2-angle fit. Keep the previous,
axis-discriminating result:

  theta12 = 32.71 deg  (target 33.0,  off by 0.3 deg)
  theta23 = 42.24 deg  (target 45.0,  off by 2.8 deg)
  theta13 =  8.45 deg  (target 8.5,   off by 0.05 deg)
  ratio   = 0.0300     (target 0.03,  exact)

  combined cost (charged lepton + neutrino) = 3.9e-3 for (1,0)/(2,0),
  vs 3.98 for every other axis combination -- a genuine, three-orders-
  of-magnitude discriminating margin that the "improved" fit does not
  have.

This is the honest, current state of the model: 4 real parameters
(m0, m2, m3, m_cross) reproduce 4 neutrino targets to within a few
percent -- not exactly -- while the axis choice remains meaningfully
fixed by the combination of both sectors. That is a weaker but far
more credible claim than "exact fit," and it is the one to report.
```

## 6. What would be needed to close the gap honestly

Any further fix must add **structure that is *itself* fixed by the same symmetry/vacuum already established** (not a free continuous parameter like an arbitrary φ₂ angle), so that it cannot simply absorb the difference between axis choices. Candidates in that spirit, not attempted here:
- A specific higher-dimension operator with a *calculable* (not free) coefficient relative to m₃, m_cross (e.g., from a common messenger loop).
- Extending the axis-selection logic itself to also fix φ₂'s exact direction dynamically (recall: φ₂'s own alignment was never derived from an F-term in this project — flagged as an open item as far back as the original vacuum-alignment session), rather than allowing it to float as a free fitting parameter now.

Both are substantial, separate pieces of work — not attempted in this session.

---

END OF FINDING
