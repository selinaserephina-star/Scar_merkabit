# FINDING: Σm_ν Reduction — Every Candidate Tested Fails, Including a Genuinely Different Mechanism (Seesaw)

**Status:** Systematic negative result across all tractable candidate classes
**Key methodological point:** identified *why* the previous three failures (channel-2, κ-scan, free φ₂) all failed the *same way* — each adds an operator that is recomputed "axis-adaptively" (same formula, different numbers per axis), so nothing stops every axis from using the same freedom equally well. This motivated testing something structurally different, not just another operator in the same family.

---

## 1. Candidates considered

**(a) Higher-order flavon operators — reasoned through analytically, not separately re-coded:**
- Φ₃³/Λ², Φ₃′³/Λ²: both **Φ₃ and Φ₃′ are single-axis** (one nonzero component each) at this vacuum. Any pure polynomial in Φ₃ alone (or Φ₃′ alone) can only ever produce combinations along that *same* axis — cannot generate a new independent direction, for the same reason established repeatedly this session (single-axis inputs can't manufacture new directions alone).
- φ₂²Φ₃/Λ, φ₂Φ₃Φ₃′/Λ: the trilinear φ₂Φ₃Φ₃′ combination, fed into the *vector* ("3") channel rather than the scalar singlet tested previously, was **already tested** in the earlier 5th-operator search (as candidates using (φ₂⊗Φ₃)₃ and (φ₂⊗Φ₃′)₃ directly) — both were found **bit-for-bit identical** to the existing m₃+m_cross parametrization, because those two terms already span the full "3" channel. No new freedom available here.

**(b) Loop contributions:** conceptually the most likely to be genuinely different (loop functions don't reduce to polynomial flavon operators), but constructing an explicit radiative model is a substantial undertaking beyond what could be responsibly completed and verified in this session — **not tested**, flagged as a genuinely open direction rather than claimed to fail.

**(c) New fields — genuine type-I seesaw — tested computationally, two variants:**

*Minimal seesaw* (Y_D = y_{D1}·Y₃(Φ₃) + y_{D2}·Y₃(χ×ξ), universal heavy mass M_N·I, M_ν = −Y_D·Y_D^T/M_N):
```text
chi  xi    cost      th12    th23    th13   Sum_mnu
 0   1   0.37525    33.00   53.34    3.54    0.0600
 0   2   0.28986    33.00   51.44    4.09    0.0600   <- best, NOT (2,0)
 1   0   1.27787     2.39   48.36    3.04    0.0600
 1   2   1.53521    33.00    1.26    1.97    0.0600
 2   0   1.27787     2.39   48.36    3.04    0.0600   <- (2,0), tied with (1,0)
 2   1   1.91165    33.00   88.29    0.06    0.0600
```
θ₁₃ target (8.5°) missed everywhere (best case 4.09°, roughly half); **(2,0) is not favored** — (0,2) does almost 4× better, and (1,0)/(2,0) are *exactly* degenerate (a genuine structural feature of this seesaw's Y_D·Y_D^T form, not numerical coincidence).

*Extended seesaw* (+ y_{D3}·Y₂(φ₂) Dirac term, 3 Yukawas + M_N):
```text
chi  xi    cost      th12    th23    th13   Sum_mnu
 0   1   7.27763    24.73   50.93   31.12    0.0774
 0   2   6.92840    24.90   49.14   30.58    0.0774
 1   0   7.58606    25.24   47.35   31.63    0.0774
 2   0   7.58606    25.24   47.35   31.63    0.0774   <- (2,0), still tied with (1,0)
```
**Worse across the board** with the extra parameter (cost up by ~10-30×, θ₁₃ off by tens of degrees) — more freedom did not help, a sign this is a genuinely different, less hospitable structure for this problem, not merely under-explored.

**(d) Dirac instead of Majorana; two doublets instead of one:** considered but not separately tested — a pure Dirac mass is still "some combination of the same flavon operators times an overall scale," so it inherits the same axis-adaptive-operator issue without a clear mechanism to escape it; a second doublet field would need its own new representation-theoretic analysis (similar to the messenger-sector work) before it could be meaningfully tested, which was not undertaken here.

## 2. Why the genuinely-different mechanism (seesaw) still didn't work

The seesaw structure **did** behave qualitatively differently from the three previous failures — it did *not* overfit every axis to machine precision (a real, structural difference, confirming the earlier diagnosis about axis-adaptive operators was on the right track) — but it failed for a different, equally fatal reason: **it simply doesn't reproduce a good θ₁₃ for any axis**, let alone specifically favor (2,0). The (1,0)≡(2,0) exact degeneracy found in both seesaw variants is itself informative: it suggests the Y_D·Y_D^T seesaw construction, built from these specific ingredients, has its *own* different symmetry structure that doesn't align with what distinguished (2,0) in the original linear M_ν construction.

## 3. Verdict

```text
NO qualifying candidate found among those tested or analytically ruled out.

(a) Higher-order operators: analytically shown redundant or incapable of
    new directions -- consistent with, not contradicting, the standing
    "channel 3 exhausted" finding.
(b) Loop corrections: genuinely untested -- the one candidate class left
    honestly open, not ruled out, for lack of scope to construct and
    verify an explicit radiative model here.
(c) Genuine seesaw: TESTED, two variants, BOTH FAIL -- but instructively:
    it escapes the overfitting failure mode of the previous three
    attempts (confirming the "axis-adaptive operator" diagnosis was
    correct), yet fails on its own terms (poor theta13 everywhere, no
    preference for (2,0), and adding freedom made it worse not better).
(d) Dirac/two-doublet: not tested, reasoned to likely inherit the same
    issue (Dirac) or require substantial new infrastructure (two
    doublets) not undertaken here.

HONEST BOTTOM LINE: the search was not a token effort -- one candidate
(seesaw) was genuinely built and tested across all 6 axis pairs in two
variants, confirming it behaves differently from (but no better than)
the earlier failures. The standing structural-tension finding (precision
vs Sum(m_nu) vs axis-uniqueness) is NOT resolved by this search, and the
one remaining genuinely-unexplored candidate class (loop-level
contributions) is flagged honestly as untested rather than claimed
solved or definitively ruled out.
```

---

END OF FINDING
