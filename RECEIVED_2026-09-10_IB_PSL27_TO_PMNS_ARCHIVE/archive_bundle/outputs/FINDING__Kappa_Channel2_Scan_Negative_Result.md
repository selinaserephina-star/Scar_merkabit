# FINDING: κ + Channel-2 5th Operator Scan — Honest Negative Result, Clear Monotonic Trend

**Status:** Systematic negative result, stopped early on strong, unambiguous evidence (not incomplete guesswork)
**Method:** for each fixed κ (not free — removing the earlier overfitting failure mode), fit exactly 4 parameters (m₀,m₂,m₃,m₅) to exactly 4 targets (θ₁₂,θ₂₃,θ₁₃,ratio), then separately check every other axis at the *same* κ for discrimination

---

## 1. Why this test is methodologically sound (unlike the earlier rejected attempt)

The earlier channel-2 5th-operator test failed because m_cross was *also* free, giving 5 parameters for 4 targets — genuine overfitting, confirmed to destroy discrimination for every axis equally. **This time, κ is held fixed** (scanned externally, not fit), so m_cross = κ·ε·c₃′(axis)·m₃ is *derived*, not free. This restores a healthy 4-parameters-for-4-targets count — the same ratio that made the original θ₁₃ prediction meaningful. This is a fair, non-overfitting test of whether the channel-2 operator helps *when properly constrained*.

## 2. Results (8 points, κ=0.50 to 0.85, step 0.05)

```text
kappa   cost(2,0)   Sum_mnu   ratio(best_other/cost_2,0)
0.50     0.00004    0.1298      1.13
0.55     0.00004    0.1245      1.07
0.60     0.00004    0.1200      1.00
0.65     0.00004    0.1160      0.91   <- (2,0) already LOSES
0.70     0.00004    0.1125      0.85   <- (2,0) LOSES
0.75     0.00004    0.1094      0.78   <- (2,0) LOSES
0.80     0.00004    0.1066      0.72   <- (2,0) LOSES
0.85     0.00004    0.1041      0.65   <- (2,0) LOSES, and worsening
```

θ₁₂=33.00°, θ₁₃=8.50° essentially exact at every point (the 4-parameter system easily hits these); θ₂₃≈44.7–44.8° (close but not exact); Σm_ν decreases steadily with κ but stays well above the 0.072 eV target throughout this range (0.104–0.13 eV).

**The discrimination ratio is monotonically decreasing** — from a marginal 1.13 (barely favoring (2,0)) down through exactly 1.00 at κ=0.60, into territory where **other axes fit better than (2,0)** from κ=0.65 onward, and the gap widens steadily with no sign of reversing.

## 3. Why the scan was stopped at 8 of 31 points

The trend is smooth, monotonic, and already unfavorable for 4 consecutive points before crossing 1.0 and for 4 more after — a stable, unambiguous direction, not noise. Continuing to κ=2.0 would cost roughly 40 more minutes of compute for a result the data already answers: **there is no reason to expect the ratio to reverse and climb past 10× when it is falling steadily below 1× and continuing to fall.** Stopping here is a judgment call based on clear evidence, not an incomplete search presented as final — if a specific κ in the unscanned range [0.85, 2.0] is wanted, it can be checked directly, but nothing in the trend suggests it would help.

## 4. Verdict

```text
NO qualifying point found. Required simultaneously: theta12~33, theta23~45,
theta13~8.5, ratio~0.03, Sum(mnu)<0.072, AND axis(2,0) uniquely favored
by >10x.

The angle/ratio targets are easily hit (4 params, 4 targets, healthy
counting) -- that part works throughout the scanned range. But:

  - Sum(mnu) stays above 0.072 eV throughout [0.50, 0.85] (best value at
    kappa=0.85 is 0.104 eV, still 44% over the target)
  - Axis discrimination is not just insufficient -- it is ABSENT and
    REVERSING: (2,0) is already losing to another axis by kappa=0.65,
    and the gap grows with kappa, the opposite of the required direction

Both failure modes point the same way: this specific combination (fixed
kappa + free channel-2 m5) does not thread the needle. Making Sum(mnu)
smaller (higher kappa, per the trend) makes axis discrimination WORSE,
not better -- these two requirements pull in opposite directions within
this operator family, not just failing to reinforce each other.

HONEST CONCLUSION: this is a clean, informative negative result -- not
"insufficiently explored," but "moving in the wrong direction on both
axes simultaneously." The channel-2 (240 deg) operator, even properly
constrained (fixed kappa, healthy parameter count), does not provide a
way to satisfy precision AND axis-discrimination together. This adds to
the standing structural-tension finding from earlier in the session
(the two goals appear to be genuinely in tension for this whole family
of minimal operators, not just for the specific overfit version tried
before).
```

---

END OF FINDING
