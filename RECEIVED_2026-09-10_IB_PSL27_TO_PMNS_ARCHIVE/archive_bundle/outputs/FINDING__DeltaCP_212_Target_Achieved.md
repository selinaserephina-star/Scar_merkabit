# FINDING: δ_CP ≈ −133.7° (NO-Window) Found — With a Critical Bug Caught and Fixed Along the Way

**Status:** SUCCESS — genuine target-window point found with essentially perfect θ₁₂,θ₂₃,θ₁₃,ratio — but only after catching and fixing a serious methodological error
**The error (must be flagged prominently):** the neutrino-sector fits in this exchange initially used `numpy.linalg.eigh` on the complex Majorana mass matrix M_ν. **`eigh` is for Hermitian matrices; M_ν is complex *symmetric*, not Hermitian, once phases are nonzero.** This silently produced mathematically well-defined but *physically meaningless* "masses," which the optimizer could fit to ratio=0.03 too easily and unrealistically — the true (Takagi-decomposition) ratio at those same points was ≈0.90, wildly off. **Every result before this fix is unreliable and superseded here.** Fixed by using proper Takagi decomposition *inside* the optimization loop, not just for post-hoc display.

---

## 1–2. Search setup

Local search in the box α₂∈[5.06±0.5], β₃∈[2.43±0.5], γ₁∈[1.81±0.5], warm-started from the previously-found region. At each phase point: re-fit (y₂,c₃,c₃′) to exact charged-lepton masses, then re-fit (m₀,m₂,m₃,m_cross) to the 4 neutrino targets **using the corrected Takagi-based residual**.

## 3. A second degeneracy discovered — and resolved

Even with the fix, re-optimizing at a *fixed* phase point sometimes landed on **different δ_CP values with identical cost** — traced this directly: **δ_CP and 180°−δ_CP are exactly degenerate** in this construction (verified: cost=3.773×10⁻⁷ for both δ_CP=46.26° and δ_CP=−133.74° at the *same* phase point — and 46.26+133.74=180.00, exact). This is a genuine structural feature of the model (a discrete two-fold degeneracy in the real 4-parameter neutrino fit), not a numerical artifact — confirmed by finding the same paired pattern (θ,180−θ) across multiple cost levels (e.g., −32.39°/147.61°, −4.08°/175.92°, 71.40°/−108.60°). Out of 259 good solutions (cost<0.001) collected via 400 restarts at the winning phase point, **41 land in the target δ_CP window** — this is exactly the "other half" of the degenerate pairs landing where wanted.

## 4. THE WINNING POINT

```text
Phases:      alpha2=5.281, beta3=2.007, gamma1=2.201

Charged-lepton parameters: y2=8.1208, c3=-0.6317, c3p=2.3470
  (masses exact: cl_cost = 5.0e-32)

Neutrino parameters: (m0,m2,m3,mcross) = (-1.1477e7, 1.2496e8, 1.3422e6, 2.6458e6)
  (nu_cost = 3.77e-07 -- essentially exact)

OBSERVABLES:
  theta12 = 32.9999 deg   (target 33,  match to 0.0001 deg)
  theta23 = 45.0276 deg   (target 45,  match to 0.03 deg)
  theta13 = 8.5000 deg    (target 8.5, exact)
  ratio   = 0.03000       (target 0.03, exact)
  deltaCP = -133.745 deg  (target window [-174,-122]: INSIDE, comfortably)
  Sum(m_nu) = 0.12421 eV  (below the original 0.129 eV reference; still
                            above the separately-tracked 0.072 eV target,
                            which this task did not ask to fix)
```

**This is a genuinely excellent point** — four of five neutrino-sector observables (θ₁₂,θ₂₃,θ₁₃,ratio) match to 4 significant figures or better, and δ_CP sits solidly inside the requested NO window, roughly at its center-left.

## Winding numbers at this specific point

```text
w(alpha2) = 1.000000
w(beta3)  = 2.000000
w(gamma1) = -0.000000
```
**Identical to the pattern found everywhere else this session** (§8 of the master summary) — confirms these winding numbers are a genuine, *point-independent* structural property of the model (tied to which matrix positions each phase enters, not to the specific phase values), not a coincidence of the earlier reference point.

## Verdict

```text
TARGET ACHIEVED: delta_CP = -133.7 deg, solidly inside [-174,-122]
(NO-favored 212 deg region), with theta12/theta23/theta13/ratio all
matching targets to high precision, exact charged-lepton masses
maintained throughout.

CRITICAL METHODOLOGICAL NOTE: this result required catching a real bug
(eigh vs Takagi for a complex symmetric matrix) that had silently
produced unreliable numbers earlier in this exchange. All earlier
delta_CP / ratio values from the complex-VEV work in this and the
previous task should be considered superseded by this corrected
treatment.

SECONDARY FINDING: a genuine delta_CP <-> 180-delta_CP degeneracy exists
in the neutrino-sector fit at fixed phases -- not a bug, a real feature
of this construction's parameter space, worth remembering for any
future work in this sector (a "good fit" is generically found in pairs,
not uniquely).

Sum(m_nu)=0.124 eV at the winning point is close to, not below, the
0.072 eV target from other parts of this project -- this task did not
ask to jointly solve that constraint, and it was not attempted here.
```

---

END OF FINDING
