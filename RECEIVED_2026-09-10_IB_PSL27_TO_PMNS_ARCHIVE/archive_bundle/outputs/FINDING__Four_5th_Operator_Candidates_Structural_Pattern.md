# FINDING: Four 5th-Operator Candidates Tested Honestly — A Structural Pattern Emerges (Not Just Bad Luck)

**Status:** Systematic negative result with a genuine structural insight
**Method:** direct cost/scan on the full 5-target problem (θ₁₂,θ₂₃,θ₁₃,ratio,Σm_ν), no Jacobian shortcut, axis-stability checked for every candidate before accepting anything — per the corrected methodology from the previous exchange.

---

## 1. Four candidates tested

| # | Candidate | Channel | Result |
|---|---|---|---|
| 1 | φ₂⊗(χ×ξ) | "3" (new axis-1-ish direction) | Solves 4-target problem exactly; fails 5-target (Σm_ν) problem — genuine trade-off (established previously) |
| 2 | φ₂⊗Φ₃ (direct) | "3" | **Identical numbers to #1** at every target Σm_ν tested |
| 3 | φ₂⊗Φ₃′ (direct) | "3" | **Identical numbers to #1** at every target Σm_ν tested |
| 4 | (Φ₃Φ₃)₂ on Φ₃'s own axis | "2" (second, previously-unused direction) | Solves the FULL 5-target problem essentially exactly — **but for every axis combination tested**, not just the established winner |

## 2. Why candidates 2 and 3 collapsed into candidate 1

The existing operators already span the *entire* 3-dimensional "3" channel between them: m₃ occupies one pure direction (Φ₃'s own axis), m_cross occupies a second (the cross-product axis), and *any* third vector with a nonzero component along the remaining direction — regardless of which specific invariant produced it — is absorbed identically by the already-free (m₃, m_cross, m₅) coefficients. Verified directly: three geometrically different candidate vectors gave bit-for-bit identical fit results at every scanned target. This isn't a coincidence; it's linear algebra — searching for more "3"-channel invariants was exhausted after the very first one.

## 3. Why candidate 4 was rejected despite looking excellent

Cost ≈0 for target Σm_ν=0.07 across **every one of the 6 non-degenerate axis combinations** (7×10⁻⁹ to 8.5×10⁻⁴ — all "solved"), with (2,1) even edging out the established winner (2,0). Zero discriminating power — the same failure mode as the earlier free-φ₂-angle overfitting trap, now via a different mechanism (a genuinely new *channel*, not a genuinely new *parameter count* imbalance).

## 4. The structural pattern (the actual finding of this exercise)

Two *independent* routes to "more freedom" — floating φ₂'s angle (an earlier session), and opening the second dimension of the "2" channel (this one) — **both** destroyed axis discrimination completely, while multiple attempts to add a *third* direction within the already-exhausted "3" channel changed nothing at all (redundant). This is not consistent with "bad luck picking candidates" — it looks like a genuine structural feature: **the (2,0) axis preference established earlier is a property of the specific, minimal, exactly-4-real-parameter model — extending the parameter space in *any* direction that isn't already fully spanned tends to make every axis fit equally well.**

This is worth stating plainly: **the axis-selection result and a fully-fitting 5-target model may be in tension with each other as goals.** Pushing harder for a perfect 5-target fit keeps finding operators that erase the very discriminating result the neutrino cross-check was built to establish.

## 5. Verdict

```text
FOUR candidates tested honestly, by direct scan, axis-stability checked
every time. THREE were redundant with an already-explored channel
(genuine null result, not evidence of anything new). ONE opened real
new freedom and immediately reproduced the overfitting failure mode
already seen once before, via a different mechanism.

This raises the search from "which specific operator works" to a more
basic question: does ANY 5th operator exist that both (a) closes the
theta12/theta23/Sum(mnu) gaps and (b) preserves axis discrimination --
or are these two requirements structurally in tension for this class of
models? Two independent "roads to freedom" both broke discrimination;
this is now a real pattern, not an unlucky pair of tries.

RECOMMENDATION: before testing more candidate operators in the same
spirit (single new bilinear/quadratic invariant, free coefficient),
consider whether the axis-discrimination result and the precision-fit
goal need to be pursued as SEPARATE claims about the model rather than
chased simultaneously -- report the axis-selection result (still solid,
established independently of any of these attempts) and the precision
gaps (theta12/theta23, Sum(mnu)) as two separate open items, rather than
continuing to search for one operator that resolves both at once.
```

---

END OF FINDING
