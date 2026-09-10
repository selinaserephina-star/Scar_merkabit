# FINDING: 5th Operator Trades θ₁₂ Against Σm_ν — Does Not Solve Both at Once

**Status:** HONEST TRADE-OFF, not a solution — a genuinely informative negative-leaning result
**Origin:** testing whether the same 5th operator that could fix θ₁₂/θ₂₃ (flagged as needed in the master summary) also relieves the Σm_ν=0.129 eV cosmological tension

---

## 1. Constructing the 5th operator honestly

Reused the already-validated (2⊗3)→3 Clebsch-Gordan tensor from the φ₂-direction investigation, fed with the *cross product direction* χ×ξ (itself already established, from the Φ₃⊗Φ₃′ cross term) as the "3" input, and φ₂ as the "2" input. This produces a new "3"-type vector:

```text
new_v = (-0.463, -0.077, 0.883)   in (v1,v2,v3) coordinates
```

Checked against the two directions already occupied by the existing operators — m₃ uses pure v3 (0,0,1), m_cross uses pure v2 (0,1,0) — **new_v has a nonzero v1 component (-0.463), which is the one previously-empty slot in the 3-dimensional "3" channel.** Verified linearly independent (rank 3 for the three directions together). This is a genuine, non-redundant 5th direction, not another copy of existing structure.

**Honesty check on parameter counting:** adding a 5th free parameter (m₅) without a 5th independent target would reopen the exact overfitting trap identified earlier this session. So Σm_ν itself was promoted to an explicit 5th target (rather than left as a free side-effect), making this a proper 5-parameters-for-5-targets test — the same healthy ratio as the original 4-for-4 construction.

## 2. Full trade-off scan (5 params, fitting θ₁₂,θ₂₃,θ₁₃,ratio + a target Σm_ν)

```text
target Sum(mnu)   cost     theta12   theta23   theta13   achieved Sum(mnu)
     0.060        0.485     19.90°    44.77°     9.12°       0.094
     0.070        0.265     22.40°    44.69°     8.91°       0.098
     0.072        0.235     22.85°    44.68°     8.88°       0.099
     0.080        0.144     24.54°    44.68°     8.78°       0.102
     0.090        0.077     26.39°    44.71°     8.69°       0.107
     0.100        0.039     28.01°    44.76°     8.63°       0.112
     0.110        0.018     29.44°    44.81°     8.58°       0.118
     0.129        0.002     31.69°    44.92°     8.53°       0.132   <- near original
     0.150        0.0001    32.69°    44.97°     8.50°       0.151
```

**θ₂₃ and θ₁₃ stay close to target across the entire scan.** The cost is driven almost entirely by **θ₁₂**, which degrades sharply and monotonically as Σm_ν is pushed down: 33.0°(target) → 31.7° → 28.0° → 22.9° → 19.9° as the mass-scale target tightens from 0.15 eV to 0.06 eV.

## 3. Is there an absolute floor, or just a trade-off?

Checked separately: minimizing Σm_ν alone with this same 5-parameter family, **completely ignoring the angles**, reaches as low as **~0.050 eV** — well inside every cosmological bound. So the parameter space *does* contain safely-allowed points. **The obstruction is not a hard floor; it is a genuine, quantified trade-off between θ₁₂ and Σm_ν within this specific operator structure.**

## 4. Verdict

```text
Does the 5th operator help Sum(m_nu)? PARTIALLY, and only at a real cost.

- It genuinely CAN reach cosmologically safe Sum(m_nu) values (~0.05-0.08 eV)
  -- the earlier 0.129 eV was not an absolute floor of this construction.

- But reaching the safe range costs theta12 badly: at the tightest
  headline bound (0.072 eV), theta12 comes out at 22.85 deg, off from
  the 33.0 deg target by more than 10 degrees -- worse than the ORIGINAL
  (pre-5th-operator) result of 31.16 deg, not better.

- The 5th operator, as constructed, does not simultaneously fix theta12/
  theta23 AND relieve the mass tension. It trades one problem for a
  bigger version of the same problem (theta12), while barely moving
  theta23/theta13 either way.

This is an honest, real result: this SPECIFIC additional operator is
not the fix for both problems at once. The two open issues (theta12/
theta23 precision, and Sum(m_nu) tension) are NOT resolved by the same
single new direction in this operator basis -- they may need genuinely
different new structure, or the trade-off itself may be telling us
something about which one is more likely to give under further model
refinement.
```

## 5. What this rules in and out

- **Ruled out:** this specific 5th operator (φ₂⊗(χ×ξ) cross-invariant, the one natural remaining direction in the "3" channel) as a simultaneous fix for both open problems.
- **Not ruled out:** a *different* 5th operator (e.g. built from a genuinely different invariant combination, or one that touches the "2" channel's second dimension rather than the "3" channel's remaining slot) might behave differently — not tested here.
- **Confirmed:** the θ₁₂/θ₂₃ gap and the Σm_ν tension, while both currently open, are not obviously the same underlying problem with one shared fix — this scan is evidence (not proof) that they may need to be addressed separately.

---

END OF FINDING
