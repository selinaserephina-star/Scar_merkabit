# FINDING: δ_CP Passes (Trivially), Majorana Phases Computed, Σm_ν Predicted — and in Tension with Cosmology

**Status:** MIXED — one genuine pass, one honest caveat about *why* it passes, one real tension flagged
**Origin:** completing item 5 (δ_CP, Majorana phases, absolute mass scale) for the current best model, χ-axis=2/ξ-axis=0, computed κ=1

---

## 1. δ_CP

**[PROVEN]** The Jarlskog invariant J_CP = Im(U_e1 U_μ2 U*_e2 U*_μ1) = 0 exactly (machine precision) for this model's PMNS matrix. This is not a computed prediction of a specific phase — it is an automatic consequence of **every VEV and coupling in the model being real**, all the way from the PSL(2,7) Yukawa ratios through the charged-lepton and neutrino sectors. A real PMNS matrix has δ_CP ∈ {0°, 180°} with no freedom in between.

**Comparison to data (NuFit 6.0, September 2025, with SK atmospheric data):**
```text
delta_CP (Normal Ordering) = 212 (+26, -41) deg,  1-sigma range [171, 238] deg
```
**180° falls inside the 1σ range.** The model's forced δ_CP=180° is therefore *consistent* with current global fits — but this should not be reported as a successful prediction in the same sense as θ₁₃ or the mass ratio. The model didn't compute 180° from any input; it has no mechanism to produce anything else. It passes because current data does not yet exclude CP conservation for normal ordering (global fits are consistent with CP conservation within 1σ, per NuFit 6.0's own summary) — not because the model predicted the measured value.

**Honest framing:** this is a *risky, falsifiable* feature, not a free pass — if δ_CP is measured away from 0°/180° with future data (e.g. DUNE, Hyper-Kamiokande), the entire real-VEV construction is falsified at once, unlike a generic model with free phases that could accommodate any measured value.

## 2. Majorana phases

**[COMPUTED]** From the signed eigenvalues of M_ν (real symmetric, eigenvalues can be negative — the standard sign-to-phase convention absorbs a negative eigenvalue into a phase exp(iπ) on that mass eigenstate):

```text
Raw signed eigenvalues: m1=+160.63, m2=-165.90, m3=+288.38  (arbitrary units)

alpha_1 = 0 deg     alpha_2 = 180 deg     alpha_3 = 0 deg

Majorana phase differences (physical convention):
  alpha_21 = 180 deg
  alpha_31 = 0 deg
```

These are genuine outputs of the model (not tuned — they follow directly from which eigenvalue of the already-fit M_ν happens to be negative). No current experiment measures Majorana phases directly (they only affect neutrinoless double-beta decay rates in combination with other unknowns), so there is no data comparison possible yet — this is a prediction for future 0νββ experiments, contingent on the neutrino being Majorana (already assumed throughout).

## 3. Absolute mass scale

**[COMPUTED]** The model only fixes *ratios* (θ₁₂, θ₂₃, θ₁₃, Δm²₂₁/Δm²₃₁) — the overall scale of M_ν was never tied to a physical unit. Calibrating the one free overall scale to the measured Δm²₃₁ = 2.53×10⁻³ eV² (NuFit 6.0 + JUNO, normal ordering) fixes everything else:

```text
Raw masses (arbitrary units): m1=160.63, m2=165.90, m3=288.38
Scale factor: 2.100e-04 eV per raw unit

Physical masses:
  m1 = 33.74 meV
  m2 = 34.84 meV
  m3 = 60.56 meV

Check: Dm21^2 = 7.59e-5 eV^2  (target 7.49-7.53e-5 -- matches within ~1%,
       automatically, since only the ratio was fit and the ratio was
       already exact)

Sum(m_nu) = 129.1 meV = 0.1291 eV
```

**Comparison to current cosmological bounds:**
```text
DESI 2024 + Planck PR3/PR4 + ACT (headline, tightest):  Sum m_nu < 0.072 eV
Relaxed combinations (+ supernovae, weaker priors):     Sum m_nu < 0.10-0.14 eV
Minimum required by oscillation data alone (NO):        Sum m_nu > ~0.06 eV
```

**The model's prediction (0.129 eV) exceeds even the most relaxed commonly-cited cosmological combinations, and is nearly double the tightest headline bound (0.072 eV).**

## 4. Why this happens — a genuine, unplanned structural feature

m₁ (33.7 meV) and m₂ (34.8 meV) come out **close to each other** (m₂/m₁ ≈ 1.03), not m₁≈0 as in a maximally hierarchical spectrum. This is a **mild normal hierarchy**, not a strong one — and it is a direct, uncontrolled consequence of the specific (m₀,m₂,m₃,m_cross) values that came out of fitting θ₁₂/θ₂₃/θ₁₃/ratio. Nothing in this session's construction ever targeted or tuned the absolute mass scale or the degree of hierarchy — it fell out once Δm²₃₁ was used to fix units. This is exactly the kind of "unplanned consequence" that makes a model genuinely falsifiable rather than infinitely flexible.

## 5. Verdict

```text
delta_CP: PASSES current data (180 deg is within 1-sigma of NO best fit),
but honestly this is because the model has no other option, not because
a specific value was computed and happened to match. Falsifiable by
future precision delta_CP measurements.

Majorana phases: computed (alpha_21=180, alpha_31=0), no current data to
compare against -- a standing prediction for future 0vbb experiments.

ABSOLUTE MASS SCALE: Sum(m_nu) = 0.129 eV -- IN TENSION WITH cosmological
bounds. Exceeds the tightest current combination (DESI+Planck+ACT,
0.072 eV) by ~80%, and exceeds even the most relaxed cited combinations
(~0.10-0.14 eV) or sits at their upper edge. This is a real, unplanned,
falsifiable prediction of the current model -- not tuned to look good --
and as it stands, it is a genuine point of tension that should be
flagged prominently in any writeup, not glossed over.
```

## 6. What this means going forward

The Σm_ν tension is a new, independent stress test the model was not built to satisfy — same spirit as the honest θ₁₃/θ₁₂ trade-off found earlier. Options, not pursued here:
- Check whether the θ₁₂/θ₂₃-improving 5th operator (flagged as needed in the master summary, §4 item 2) also happens to reduce the mass-scale prediction — not guaranteed, would need to be checked explicitly once such an operator is constructed.
- Consider whether inverted ordering (not explored at all this session) fares better — cosmological bounds are typically *more* constraining for inverted ordering (higher minimum Σm_ν), so this is unlikely to help and was not attempted.
- Report the tension as-is: a real, falsifiable weak point of the current minimal model, not a reason to distrust the θ₁₂/θ₂₃/θ₁₃/ratio results, which came from an independent part of the fit (angles and mass-squared *ratios* don't depend on the overall scale at all).

---

END OF FINDING
