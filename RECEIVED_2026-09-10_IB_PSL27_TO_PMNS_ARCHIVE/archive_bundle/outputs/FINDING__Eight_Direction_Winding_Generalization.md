# FINDING: φ₁'s Proximity to D=0 Is Genuinely Structural — Not One of Eight Equally-Close Directions

**Status:** POSITIVE — φ₁ confirmed as a real outlier, with one genuine surprise (a double zero in χ₃)
**Method:** for each of the 8 VEV components, hold the other 7 at physical values, get D as an exact single-variable polynomial (symbolic, not approximated), find all roots, nearest distance, and winding number via direct contour integration.

---

## 1. Full table — all 8 directions

| Direction | Degree of D(x) | Nearest root | Distance | Winding w |
|---|---|---|---|---|
| **φ₁** | 3 (cubic) | +2.8355×10⁻⁵ | **2.835×10⁻⁵** | **1** |
| φ₂ | 1 (linear) | 0 | 6.000×10⁻² | 1 (far, not "close") |
| χ₁ | 0 (constant) | — none — | ∞ | N/A |
| χ₂ | 2 (quadratic) | +1.9314×10⁻³ | 1.931×10⁻³ | 1 |
| χ₃ | 2 (quadratic) | 0 (double root) | 1.931×10⁻³ | **2** |
| ξ₁ | 0 (constant) | — none — | ∞ | N/A |
| ξ₂ | 2 (quadratic) | −1.213×10⁻³+0.627×10⁻³i | 1.366×10⁻³ | 1 |
| ξ₃ | 2 (quadratic) | −1.366×10⁻³ | 1.366×10⁻³ | 1 |

## 2. Is φ₁ special, or one of several equally-close directions?

**Genuinely special.** φ₁'s distance (2.84×10⁻⁵) is **48–68× closer** than the next-closest group (χ₂/χ₃ at 1.93×10⁻³, ξ₂/ξ₃ at 1.37×10⁻³). This is not a marginal difference easily attributed to noise or an arbitrary choice of "closeness threshold" — it's roughly two orders of magnitude, a clean outlier by any reasonable standard.

## 3. Two structural surprises beyond the main question

**χ₁ and ξ₁: no root at all.** D, restricted to varying only χ₁ (or only ξ₁) with the other 7 fixed at physical values, is a **constant** — degree 0. This means D has *zero linear sensitivity* to χ₁ or ξ₁ alone at this point (every term in the full polynomial that involves χ₁ or ξ₁ also requires at least one other currently-zero variable, so it drops out entirely once the other 7 are frozen at the physical point). There is no nearby zero to find in these two directions specifically — a qualitatively different situation from all other 6.

**χ₃: a genuine double zero (w=2), the only one of its kind.** D(χ₃) = c·χ₃² *exactly* (verified: linear and constant coefficients are both exactly zero) — meaning the nearest root is at χ₃=0 with **multiplicity 2**, confirmed directly by contour integration (w=2.0000, stable at two different radii). This is qualitatively different from every other close direction (all of which give simple, w=1 zeros). Physically: χ₃ is the *only nonzero* component of Φ₃ at this vacuum, and D vanishes to *second* order as it's tuned toward zero, not first order — a stronger degeneracy than a generic zero.

## 4. Is the pattern structural or coincidental?

Three independent pieces of evidence point toward "structural, not coincidental":

- φ₁'s distance is a clean **outlier** by 1–2 orders of magnitude — not part of a continuum of "somewhat close" directions where φ₁ merely happens to be at the near end.
- φ₁=0 is not a free choice made for this test — it is the **independently-established value** from the exact charged-lepton mass fit (§3 of the master summary), so its proximity to D=0 is a genuine, unplanned property of the fitted vacuum, not something arranged to produce this result.
- The winding numbers are **not uniform** (five w=1, one w=2, two undefined) — if the closeness pattern were a numerical artifact of the polynomial's generic shape, there would be no reason for one specific direction (χ₃, the one *nonzero* Φ₃ component) to show a qualitatively different, higher-order degeneracy. That χ₃ — a physically meaningful, nonzero VEV — is the one with the double zero (rather than, say, an arbitrary zero-valued direction) is suggestive of real structure, though the precise reason was not investigated further here.

## 5. Verdict

```text
PATTERN CONFIRMED: phi1 is not one of several similarly-close directions
-- it is the unique, dramatic outlier (48-68x closer than any other),
consistent with the earlier single-direction finding, now shown to be
genuinely non-generic across the full 8-dimensional VEV space rather
than an artifact of only having checked one direction.

TWO NEW, UNPLANNED FACTS: chi1 and xi1 show NO root at all in this
slicing (D is locally insensitive to them alone); chi3 -- the single
nonzero Phi3 component -- shows a genuine DOUBLE zero (w=2), the only
higher-order winding found among all 8 directions.

STRUCTURAL vs COINCIDENTAL: the weight of evidence (outlier magnitude,
phi1's independently-fixed origin, non-uniform winding numbers landing
specifically on the physically nonzero chi3 direction) favors STRUCTURAL
-- but this is an inference from the pattern's shape, not a derivation
of WHY it happens. The underlying cause (if any) was not identified in
this test and remains open.
```

---

END OF FINDING
