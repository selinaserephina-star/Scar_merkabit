# FINDING: Loop-Adjacent Mechanisms (Non-Universal Heavy Mass) Tested — Still No (2,0) Preference, But a Genuine New Pattern Found

**Status:** Third genuinely different construction tested, third failure to favor (2,0) — but with an informative, consistent meta-pattern across all three
**Context:** completes the "loop corrections" candidate class flagged as untested in the previous finding — rather than building a full radiative model (Zee/scotogenic with explicit loop integrals, a much larger undertaking), tested the specific structural ingredient most likely to introduce genuinely new physics: a **non-universal heavy Majorana mass matrix**, since a universal M_N (as used in the plain seesaw test) makes any loop prefactor just an overall rescaling with no new flavor structure.

---

## 1. Construction

```text
M_N = M0*I + M1*Y3(Phi3)     <- genuinely non-universal, S4-covariant heavy mass
Y_D = yD1*Y3(Phi3) + yD2*Y3(chi x xi)
M_nu = -loopfac * (Y_D . M_N^-1 . Y_D^T)
```
This is structurally representative of what a scotogenic-type loop model would produce if the right-handed neutrino masses are *not* assumed degenerate (a physically reasonable, S4-covariant relaxation) — the `loopfac` parameter stands in for the actual loop integral, left free since its precise value depends on UV masses not fixed in this exercise.

## 2. Results — all 6 axis pairs, target Σm_ν=0.06 eV

```text
chi  xi    cost      th12    th23    th13   Sum_mnu
 0   1   0.06287    36.40   39.35    6.92    0.0592   <- best overall
 0   2   0.10179    37.15   37.65    6.48    0.0592
 1   0   2.67943    86.83   38.95    8.45    0.0590   <- theta13 near-exact...
 1   2   0.55431    33.43   11.60    8.92    0.0591
 2   0   2.67943    86.83   38.95    8.45    0.0590   <- (2,0): tied with (1,0), still
 2   1   0.52333    36.28   77.15    8.25    0.0592
```

**A new, genuinely different failure mode:** (2,0) [tied exactly with (1,0), same structural degeneracy as the plain seesaw] achieves the *closest* θ₁₃ of any axis pair (8.45° vs 8.5° target, essentially exact) — but this is completely swamped by a badly-missed θ₁₂ (86.83° vs 33° target), driving its overall cost far above (0,1) and (0,2), which have worse θ₁₃ but much better θ₁₂,θ₂₃.

## 3. The meta-pattern across all three seesaw-adjacent constructions tried

```text
Minimal seesaw (prev. finding):    best = (0,2), cost=0.290
Extended seesaw (prev. finding):   best = (0,2)-ish, cost~6.9 (all poor)
Non-universal M_N (this finding):  best = (0,1), cost=0.063
```

**(2,0) has not won on overall cost in any of the three genuinely-different constructions tested** — (0,1) or (0,2) consistently do better, even though (2,0) occasionally nails one individual target impressively (θ₁₃ here). This is worth noting as a genuine, consistent observation, **not** as evidence that (2,0) is "wrong" — the established, working model uses a *linear* M_ν (not a seesaw/loop ratio), where (2,0) is decisively preferred (§ established earlier in this project). These seesaw-family constructions are a different physical hypothesis, and their own internal axis-preference simply doesn't happen to coincide with (2,0) — an informative, self-consistent fact about *this* candidate family, not a challenge to the established linear-model result.

## 4. Verdict on the full loop-corrections candidate class

```text
Tested the one structural ingredient (non-universal heavy Majorana mass)
most likely to make a loop-suppressed mass behave differently from a
plain seesaw. It does behave differently (new failure mode: theta13
nailed, theta12 destroyed, rather than theta13 missed uniformly) -- but
still does not favor (2,0), consistent with (not contradicting) the
minimal and extended seesaw results.

Did NOT construct a full explicit radiative model (Zee, Zee-Babu, or
scotogenic with actual loop integrals and physical mass spectra) --
that remains a larger undertaking beyond this test's scope. What WAS
tested is the specific structural feature (non-degenerate heavy masses)
most likely to matter for the flavor question at hand, and it does not
change the qualitative conclusion.

CUMULATIVE STATUS across all Sum(m_nu)-reduction attempts (this finding
plus the two seesaw variants plus the three original operator-based
attempts): SIX distinct constructions tried, ZERO succeed at satisfying
precision + Sum(m_nu)<0.072 + axis(2,0)-uniqueness simultaneously. Three
different qualitative failure modes identified (overfit-every-axis;
seesaw-degenerate-axis-pairs-none-preferred; seesaw-with-good-theta13-
but-destroyed-theta12). This is now a well-characterized, multi-angle
negative result, not a single untested guess.

HONEST BOTTOM LINE: the structural tension between precision, Sum(m_nu),
and axis uniqueness survives contact with a materially different physical
mechanism (loop-adjacent, non-universal masses), not just repeated
variations on the original linear operator. This strengthens rather than
merely repeats the standing assessment. A genuinely exhaustive test would
still require the full explicit loop-integral construction, which remains
open -- but the evidence so far gives no reason to expect it would behave
differently from what's already been found here.
```

---

END OF FINDING
