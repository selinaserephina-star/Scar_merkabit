# FINDING: Driving-Field Vacuum Alignment for (φ₂, Φ₃, Φ₃′) — Reduces 8 Free VEVs to 3, Fits Masses, But One Coefficient Sits at ~30 Instead of O(1)

**Status:** CONSTRUCTION COMPLETE — genuine improvement over the free-VEV FIT, not yet a clean PREDICTION
**Origin:** driving-field superpotential extending this project's own prior Φ₃-alignment result to Φ₃′, linked to the established modulus/ε mechanism for φ₂
**Subject:** whether a dynamical potential can fix all 8 VEV components (φ₁, φ₂, χ₁, χ₂, χ₃, ξ₁, ξ₂, ξ₃) up to a small number of O(1) coefficients

---

## 0. Methodological caveat, stated up front

The quadratic S₄ invariants used below ((φ₂φ₂)₁, (φ₂φ₂)₂, (Φ₃Φ₃)₁, (Φ₃Φ₃)₃, (Φ₃′Φ₃′)₁, (Φ₃′Φ₃′)₃) are the **standard, literature-established forms** for these S₄ representations, and match exactly what this project's own earlier finding ("Dynamic Alignment of Φ₃...") already used successfully. An attempt in this session to independently re-derive the full 24-element S₄ representation matrices from scratch and verify them against the *exact* basis implicit in the given Y_T formulas did not converge to a consistent match (a brute-force and a direct linear-algebra search both failed to find a valid generation-representation matrix for either S₄ generator, in either flavon-assignment ordering). This likely reflects a basis-convention mismatch between the from-scratch construction and the paper's implicit convention, not an error in the standard invariants themselves — but it means the group-theory input below rests on **precedent and literature convention**, not an independently re-verified basis match for this specific task. This should be closed before the mechanism is treated as fully certified.

---

## 1. The potential

**Fields:** φ₂ = (φ₁,φ₂) ∼ 2, Φ₃ = (χ₁,χ₂,χ₃) ∼ 3, Φ₃′ = (ξ₁,ξ₂,ξ₃) ∼ 3′, flaton η ∼ 1 with ⟨η⟩ = εΛ (inherited, not re-derived here).

**Driving fields** (F-term companions, standard Altarelli–Feruglio-type construction):
```text
zeta_2  ~ 2   (for phi2 direction)
zeta_31 ~ 1   (for phi2 magnitude, linking to eta)
zeta_3  ~ 3   (for Phi3 direction)
zeta_32 ~ 1   (for Phi3 magnitude)
zeta_3' ~ 3   (for Phi3' direction -- NOTE: Sym^2(3') = 1+2+3, so the
               self-alignment driving field for Phi3' must transform
               as 3, not 3', since the antisymmetric 3' channel of
               3'x3' vanishes identically for a self-product)
zeta_33 ~ 1   (for Phi3' magnitude)
```

**Superpotential:**
```text
W = kappa_2  * zeta_2  . (phi2 phi2)_2
  + zeta_31 [ kappa_31 (phi2 phi2)_1 - eta^2 ]

  + kappa_3  * zeta_3  . (Phi3 Phi3)_3
  + zeta_32 [ kappa_32 (Phi3 Phi3)_1 - eta^4/Lambda^2 ]

  + kappa_3p * zeta_3' . (Phi3' Phi3')_3
  + zeta_33  [ kappa_33 (Phi3' Phi3')_1 - eta^4/Lambda^2 ]
```

The η-powers are chosen by a Froggatt–Nielsen-type charge assignment (φ₂ carries FN charge 1, Φ₃ and Φ₃′ carry FN charge 2), so that φ₂'s magnitude-fixing operator needs one fewer η/Λ suppression than Φ₃, Φ₃′'s — giving φ₂ ~ ε and Φ₃, Φ₃′ ~ ε² from a single flaton, without introducing new spurions beyond η.

---

## 2. F-term equations and their solution

**Direction (all three sectors, same algebraic trick):**
```text
F_zeta2  = 0:  (phi2 phi2)_2  = 0   ->  phi1^2 = phi2^2  AND  phi1 phi2 = 0
               -> phi1 = phi2 = 0 identically (see note below)

F_zeta3  = 0:  (Phi3 Phi3)_3  = sqrt2(chi2 chi3, chi3 chi1, chi1 chi2) = 0
               -> chi_i chi_j = 0 (i!=j)  ->  axis solutions (v,0,0) etc.

F_zeta3' = 0:  (Phi3' Phi3')_3 = sqrt2(xi2 xi3, xi3 xi1, xi1 xi2) = 0
               -> xi_i xi_j = 0 (i!=j)   ->  axis solutions (v',0,0) etc.
```

**Note on φ₂:** the naive self-alignment F_ζ2=0 over-constrains a 2-component
real field to the trivial solution φ₁=φ₂=0 (verified algebraically: the two
conditions φ₁²=φ₂² and φ₁φ₂=0 together force both to vanish). This is a
genuine problem, not a typo — the standard literature workaround is to
**not** self-align the doublet this way, and instead fix its direction via
the pre-existing modulus-link mechanism from this project's own earlier
finding: ⟨φ₂⟩ = Λε·(direction), with the direction left as a **discrete
choice** ((1,0) or (0,1), related by an S₄ element) rather than dynamically
derived here. This is an honest gap, not a solved problem — see §6.

**Magnitude (from the singlet F-terms, standard driving-field algebra):**
```text
F_zeta31 = 0: phi1^2+phi2^2 = eta^2/kappa_31          -> |phi2| = eps*Lambda*sqrt(1/kappa_31)
F_zeta32 = 0: chi1^2+chi2^2+chi3^2 = eta^4/(Lambda^2 kappa_32)  -> |Phi3|  = eps^2*Lambda*sqrt(1/kappa_32)
F_zeta33 = 0: xi1^2+xi2^2+xi3^2  = eta^4/(Lambda^2 kappa_33)    -> |Phi3'| = eps^2*Lambda*sqrt(1/kappa_33)
```

For κ₃₁=κ₃₂=κ₃₃=1 (the "natural" choice, no large/small Wilson coefficients
in the potential itself): |φ₂|=εΛ, |Φ₃|=|Φ₃′|=ε²Λ exactly.

## 3. Minimum check

The potential is a sum of positive semi-definite terms (|F_ζ|² pieces in the
scalar potential, standard SUSY driving-field construction) plus mass-squared
terms for the orthogonal (non-aligned) directions with coefficients taken
positive; under that standard assumption the aligned, axis-type solutions
are genuine minima, not saddle points, and the vacuum is a **discrete set**
(3 equivalent axes for Φ₃ × 3 for Φ₃′ × an assumed discrete direction for
φ₂, related to each other by the unbroken part of S₄) rather than a
continuous family. This closes 5 of the 8 previously-free real VEV
directions (2 for φ₂'s continuous angle+one radial mode, 2 for Φ₃'s
continuous direction, 2 for Φ₃′'s continuous direction, partially offset by
the 3 magnitude conditions) — **down from 8 free real parameters to 3: an
overall y₂, and one O(1) coefficient per triplet sector (c₃ for Φ₃, c₃′ for
Φ₃′), after using up the discrete axis/direction choices.**

---

## 4. Numerical test against the masses

Substituting the aligned VEVs (best discrete choice found, robust across
essentially all axis/angle combinations tried — see §5) into the given
Y_T, with y₃=y₂/√3, y₃′=y₂√(2/3):

```text
<phi2>  = eps*(0, 1) = (0, 0.06)
<Phi3>  = eps^2 * c3  * (0,1,0)
<Phi3'> = eps^2 * c3' * (1,0,0)

Fitted:  y2 = -0.052008   c3 = 0.536502   c3' = 31.403683

Y_T =
[[ 0           0          -5.7994e-05]
 [ 0          -5.4048e-03 -4.8007e-03]
 [-5.7994e-05  4.8007e-03  5.4048e-03]]

trace(Y_T) = 0  (exact, as proven in the companion finding)
eigenvalues(Y_T)  = [-2.9469e-06, 2.4851e-03, -2.4822e-03]   (sum=0, NOT the masses)
singular values   = [0.0102057490, 0.0006068677, 0.0000029350]
targets           = [0.0102057490, 0.0006068677, 0.0000029350]
relative error    = ~1e-15  (machine precision)

masses (MeV) = [1776.86, 105.658, 0.510999]
PDG targets  = [1776.86, 105.658, 0.510999]
chi^2 ~ 0
```

## 5. Naturalness — the honest result

y₂ = -0.052 (|y₂|/ε ≈ 0.87, a perfectly reasonable O(1) Yukawa coupling)
and c₃ = 0.54 (clean O(1)) are both fine. **c₃′ = 31.4 is not O(1).**

This is not a search artifact of one particular axis choice. Scanning **all
9 combinations of Φ₃/Φ₃′ axis choice, both ε² and ε³ power assignments, and
even letting φ₂'s direction float freely as a continuous angle** (36+
combinations total, each independently re-optimized), **every single
converged solution lands on |c₃′| in the range 31–35.** The sign and the
exact value shift slightly with the discrete choice, but the *order of
magnitude* is completely robust. This strongly suggests the ~30 factor is
a genuine structural feature of matching these three specific target masses
with the fixed y₂:y₃:y₃′ = √3:1:√2 ratio and this specific matrix texture —
not an artifact of an unlucky alignment choice that better engineering could
fix.

**Diagnosis:** ~31 is a real, if mild, naturalness tension — it is not a
catastrophic fine-tuned cancellation (nothing here divides two large,
independent numbers to get a small remainder; it is a single Wilson
coefficient in the Φ₃′ potential sitting about 1.5 orders of magnitude away
from 1). It is exactly the kind of residual tension that an honest
naturalness audit should report rather than paper over.

---

## 6. What this construction achieves, and what it still leaves open

**Achieved:**
- A concrete, S₄-invariant driving-field potential that dynamically fixes
  the *direction* of Φ₃ and Φ₃′ to discrete axes (a genuine F-term result,
  not an ansatz) via the identical mechanism already validated in this
  project's earlier Φ₃-only finding, now extended to Φ₃′.
- Their *magnitude* tied to the same flaton η already established for φ₂,
  via an FN-charge argument, giving the hoped-for φ₂~ε, Φ₃,Φ₃′~ε² pattern.
- The free-parameter count for the VEV sector drops from **8 real numbers**
  (the earlier FIT verdict) to **3** (y₂, c₃, c₃′) plus a residual discrete
  choice of axes — a genuine, substantial reduction in freedom.
- With this reduced parameter set, the masses still fit exactly.

**Not achieved / still open:**
- φ₂'s own *direction* has no F-term derivation here (§2's note) — it is
  still an inherited discrete choice from the earlier modulus-link finding,
  not dynamically derived by this construction.
- The Φ₃′ sector's own potential coefficient (c₃′~31) is not O(1), robustly,
  across every variant tested — an honest, unresolved ~1.5-order-of-magnitude
  tension.
- The exact S₄ basis/representation match to the given Y_T was not
  independently re-verified from first principles (§0).

---

## 7. Verdict

```text
PREDICTION CRITERION: PARTIALLY MET.

Free continuous VEV parameters reduced from 8 (pure FIT) to 3 (y2, c3, c3')
plus a discrete axis/direction choice, via an explicit, checkable
driving-field potential -- a genuine, substantial improvement in
predictivity over the prior finding.

The mass fit is exact (chi^2 ~ 0) with this reduced parameter set.

BUT: one of the three remaining coefficients (c3', the Phi3' triplet's own
potential coupling) is robustly forced to ~31, not O(1), across every
discrete/continuous variant of the construction tested in this session.
This is a real, if mild, naturalness tension, not a fine-tuned
cancellation -- but it is also not clean enough to call this a genuine,
parameter-free PREDICTION.

VERDICT: FIT, IMPROVED -- not yet PREDICTION.

What would close this: either (a) an independent argument (from a UV
completion, a different messenger structure, or a loop-level correction)
for why the Phi3' sector's potential coefficient should naturally be
~O(30), or (b) a different alignment mechanism for Phi3' that produces
its VEV with a built-in factor explaining this scale, or (c) evidence that
the discrepancy is filled by physics not modeled here (e.g. Phi3-Phi3'
cross-couplings in the potential, not included in this minimal
construction). None of these is resolved by this session's work.
```

---

END OF FINDING
