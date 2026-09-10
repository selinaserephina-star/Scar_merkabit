# FINDING: Full Yukawa Matrix with Fixed PSL(2,7) Ratios Fits Any Lepton Masses — Verdict is FIT, Not PREDICTION

**Status:** COMPUTATION COMPLETE — negative result on predictivity, with two clean structural sub-theorems
**Origin:** independent numerical verification, given task inputs (y2:y3:y3′ = √3:1:√2 fixed, y1 = 0)
**Subject:** whether Y_T with fixed PSL(2,7) Yukawa ratios reproduces m_τ:m_μ:m_e without fine-tuning y2, y3, y3′ separately

---

## 1. Two rigorous sub-results (proven, not fitted)

### 1a. Diagonal sector alone (Φ₃ = Φ₃′ = 0) is IMPOSSIBLE

With y₁ = 0, the three diagonal entries of Y⁽²⁾ always sum to exactly zero:

```text
d1 + d2 + d3 = 2φ1 + (-φ1+√3φ2) + (-φ1-√3φ2) = 0
```

for **any** φ1, φ2 (real or complex). Physical masses require |d1|, |d2|, |d3| = (λ_τ, λ_μ, λ_e) in some order; three (signed or complex) numbers with these magnitudes can sum to zero only if the largest magnitude does not exceed the sum of the other two (triangle inequality). Numerically:

```text
λ_τ           = 0.0102057490
λ_μ + λ_e     = 0.0006098028
λ_τ > λ_μ+λ_e  →  violated by a factor of 16.7
```

**The diagonal sector cannot reproduce the lepton hierarchy for any φ1, φ2 whatsoever.** This is a proof, not a fit failure — verified by exhaustive sign/permutation search.

### 1b. Diagonal + Φ₃ only (Φ₃′ = 0, i.e. Y_T real symmetric) is ALSO IMPOSSIBLE

Y⁽³⁾ has zero diagonal by construction, so trace(Y_T) = 3y₁ = 0 still holds with Φ₃ turned on. Since Y_T is now real **symmetric** (Hermitian), its eigenvalues are real and its singular values equal |eigenvalues| exactly. The same trace-zero / triangle-inequality obstruction in §1a applies verbatim to the full eigenvalue spectrum, **for any χ1, χ2, χ3, however large**. Confirmed numerically (symmetric case: eigenvalues sorted = |eigenvalues| sorted = singular values, exactly, to machine precision).

**Consequence:** Φ₃′ (the antisymmetric triplet) is not optional — it is the *only* way to escape the trace obstruction, because it is the only ingredient that makes Y_T non-normal, decoupling its singular values (= physical masses via bi-unitary SVD) from its eigenvalues (which must always sum to 3y₁ = 0).

---

## 2. Full sector (Φ₃′ ≠ 0): masses ARE reproduced — but so is anything else

With Φ₃′ turned on, Y_T becomes a general traceless real 3×3 matrix, and an exact fit is trivial. One explicit solution:

```text
y2  = 1.550704     y3  = 0.895299     y3' = 1.266145   (ratio √3:1:√2 exact)
phi1 = -1.0912e-03   phi2 = 6.3678e-04
chi  = [-0.0034828, -0.0024859, -0.0008342]
xi   = [ 0.0020440, -0.0016827, -0.0029842]

Y_T =
[[-0.0033843  -0.0045253  -0.0000950]
 [ 0.0030316   0.0034025  -0.0005302]
 [-0.0043562  -0.0057060  -0.0000182]]

trace(Y_T)        = 2.4e-20  (exactly zero, as proven above)
eigenvalues(Y_T)   = [ 1.1040e-03,  1.4724e-05, -1.1187e-03]   (sum = 0, NOT the masses)
singular values    = [ 0.0102057,   0.0006069,   0.0000029 ]   (= the physical masses)

masses (MeV)  = [1776.86,  105.658,  0.5111]
PDG targets   = [1776.86,  105.658,  0.510999]
rel. error    = [-1.2e-06,  4.6e-06,  2.9e-04]
```

A higher-precision refinement of the same ansatz drives the fit to machine precision (relative errors ~10⁻¹⁴), so **χ² ≈ 0 exactly, trivially**, for essentially any starting point.

**The eigenvalues of Y_T are NOT the masses** — this is the key technical point the naive "read off the eigenvalues" framing misses. Because Φ₃′ makes Y_T non-normal, eigenvalues and singular values genuinely differ (shown numerically above: eigenvalues are ~10⁻³, small and centered near zero; singular values match the real hierarchical masses). Physical Dirac masses always come from bi-unitary (SVD) diagonalization of a general Yukawa matrix, not from its eigen-decomposition — this is standard SM flavor-physics practice, not a modification introduced here.

---

## 3. Why this is a FIT, not a PREDICTION

This is the central finding. Once Φ₃′ ≠ 0 is allowed, **the fixed ratio y2:y3:y3′ = √3:1:√2 constrains nothing about the achievable mass spectrum.**

Proof: for any fixed nonzero y2 (hence fixed y3, y3′), the linear map

```text
(φ1, φ2, χ1, χ2, χ3, ξ1, ξ2, ξ3)  →  Y_T
```

is a **bijection onto the full 8-dimensional space of traceless real 3×3 matrices** (rank 8 out of 8, confirmed by direct construction: every random traceless matrix is exactly reproduced by some choice of the 8 VEV parameters). Since a general traceless 3×3 matrix can have *any* three singular values whatsoever (subject only to no constraint beyond non-negativity), the fixed Yukawa ratio is a bookkeeping relabeling, not a restriction — it holds for any nonzero y2, and the 8 VEV parameters absorb all the freedom that would otherwise sit in y2, y3, y3′ individually.

**Direct demonstration:** the identical ansatz and fitting code was run against four sets of completely random, PSL(2,7)-unrelated target masses. All four fit to machine precision (residual ~10⁻²¹) just as easily as the real lepton masses. The model has no discriminating power over what mass spectrum it can produce.

With 8 real VEV parameters against 3 real mass constraints, **5 flat directions remain in the solution space even after an exact fit.** "Naturalness" of any single point on that 5-dimensional flat locus (e.g. all VEVs landing near ε² ≈ 0.0036, as in the solution above) is not a discovery — it is a choice among infinitely many equally valid points, most of which do **not** look natural. A hierarchy-biased search (penalizing φ ≫ ε, χ/ξ ≫ ε²) does find solutions consistent with φ, χ, ξ ~ ε² and y2 ~ O(1), but a solution family with no discriminating power carries no predictive content regardless of which member looks tidiest.

---

## 4. Answers to the six requested items

1. **Substitution of y3 = y2/√3, y3′ = y2√(2/3) into Y_T:** done (§2); changes nothing about which mass spectra are reachable (§3).
2. **VEV choice for diagonal-good / off-diagonal-small / O(1)-or-natural / no fine-tuning:** achievable (§2 solution has all VEVs at or below ε² with an O(1) coefficient, no cancellation), but this is one arbitrary point among a 5-parameter continuum of equally exact fits (§3) — the "no fine-tuning" property does not make it a prediction.
3. **Can Y_T with fixed ratios reproduce m_τ:m_μ:m_e without fitting y2/y3/y3′ separately?** Yes trivially, but for the wrong reason: not because the ratios are compatible with the physical hierarchy, but because the VEV sector alone (8 real numbers) has more than enough freedom to fit any 3 numbers regardless of the Yukawa ratios (§3, proven by the bijection argument and the random-target control test).
4. **Is the diagonal sector alone sufficient?** No — proven impossible for any φ1, φ2 (§1a), and this failure is independent of y1 being exactly zero versus merely very small, as long as it is exactly zero.
5. **Do Φ₃, Φ₃′ need to be turned on, and at what scale?** Φ₃′ is structurally required (§1b); with it, natural-looking solutions exist at χ, ξ ~ ε² · O(1), φ1, φ2 ~ ε² · O(1) — but see §3 for why this scale choice is not unique or predictive.
6. **Full output (Y_T, singular values, masses, PDG comparison, χ², naturalness, verdict):** given in §2 and below.

---

## 5. Naturalness diagnostic

```text
No single dangerous cancellation was found in the exhibited solution
(all VEVs land within a factor of a few of eps^2, no O(1) numbers
divided by other O(1) numbers to cancel at the 10^-2 level or worse).

BUT: naturalness of one point in an underdetermined 5-flat-direction
solution family is not a meaningful naturalness statement. A solution
with wildly different, arbitrary-looking VEVs (e.g. chi2 = -0.068,
xi2 = -0.076, both bigger than eps itself) fits equally exactly
(see the first solution found in this session, before the
hierarchy-biased search).

Naturalness here is a STATEMENT ABOUT ONE CHOSEN POINT, not a
property of the model.
```

---

## 6. Final verdict

```text
PREDICTION CRITERION (as stated in the task): FAILED.

The exact PSL(2,7) Yukawa ratios y2:y3:y3' = sqrt(3):1:sqrt(2) are a
genuine, verified, non-trivial group-theoretic fact (see the companion
finding on the exact ratios). But by themselves, in this Yukawa-matrix
ansatz, with the flavon VEVs (phi1, phi2, chi1-3, xi1-3) left as free
real parameters, they place NO constraint whatsoever on the achievable
charged-lepton mass spectrum. The model fits the true masses and fits
four independent sets of random, unrelated masses with equal, exact
precision.

VERDICT: FIT, not PREDICTION.

What would upgrade this to a prediction: an INDEPENDENT vacuum-
alignment mechanism that fixes the ratios phi1:phi2:chi1:chi2:chi3:
xi1:xi2:xi3 (or at least removes enough of the 5 flat directions) on
grounds separate from just matching the observed masses -- e.g. a
messenger/flavon superpotential with its own PSL(2,7)-invariant
alignment condition, analogous to how the racetrack modulus T fixed
epsilon independently in the earlier charged-lepton benchmark. This
is exactly the "vacuum alignment problem" flagged as open in earlier
findings in this project (Generation Axis Selection Is The Vacuum
Alignment Problem; The Minimal Selector Is One S3-Breaking Direction) --
this task does not resolve it, and no computation of Y_T alone can.
```

---

END OF FINDING
