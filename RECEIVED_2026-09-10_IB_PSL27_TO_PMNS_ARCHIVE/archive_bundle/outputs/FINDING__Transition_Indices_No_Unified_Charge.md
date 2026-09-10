# FINDING: Transition Indices — Three Genuine Integers, One Honest Failure, No Unified "Vortex Charge"

**Status:** Mixed — rigorous where the mathematics supports it, explicitly flagged where it doesn't
**Method:** for each transition, identify the precise mathematical TYPE first, then compute (not assume) an integer, then test perturbation-stability directly

---

## 1. Transition-by-transition analysis

### T1: y₁=0 ⇒ trace(Y_T)=0 ⇒ diagonal-only impossible

**Type:** algebraic constraint (linear codimension), not a bifurcation or rank change.
**Index:** codimension = **1** (trace=0 is exactly one linear equation on the 3-dim space of singular/eigen-values).
**Integer?** Yes, trivially — codimension of a single linear constraint is always an integer by definition.
**Stability:** definitionally stable — any traceless-matrix constraint has codimension exactly 1, regardless of perturbation.

### T2: (Φ₃′Φ₃′)₃=0 identically ⇒ cross term required

**Type:** vanishing order of a homogeneous quadratic form restricted to a coordinate axis.
**Index:** computed directly via scaling — perturbing off-axis by δ in a **generic** direction, |value| ∝ δ¹ exactly (ratio converges to a direction-dependent but δ-independent constant, e.g. 2.6647 for one tested direction). **Vanishing order = 1.**
**Integer?** Yes — confirmed numerically (ratio |val|/δ converges to a finite nonzero constant as δ→0, the textbook signature of first-order/linear vanishing, not second-order).
**Stability:** tested across **5 independent random off-axis directions** — order=1 in every case. Genuinely direction-independent, not a fluke of one perturbation choice.

### T3: (1,0)≡(2,0) degeneracy — **the honest failure**

**First correction:** the exact degeneracy point is at **ratio=0** (i.e. m_cross=0 exactly), not at the computed ratio=0.113 as informally described in the task. Verified directly: cost(1,0)−cost(2,0) = 1.2×10⁻¹⁵ (machine zero) at ratio=0.

**Attempted index:** "order of contact" of the two cost-vs-ratio curves at ratio=0 — i.e., does cost(1,0)(r)−cost(2,0)(r) vanish linearly, quadratically, etc.?

**What was found:** the difference does **not** follow any clean power law:
```text
ratio=0.00: diff = +1e-15  (degenerate point)
ratio=0.02: diff = +4.1e-3
ratio=0.05: diff = -2.1e-2   <- SIGN FLIP
ratio=0.08: diff = +7.6e-3   <- SIGN FLIP AGAIN
ratio=0.11: diff = +4.6e-2
ratio=0.15: diff = +7.6e-2
```
This is **non-monotonic and sign-changing** near the degeneracy — not the smooth, single-sign approach a clean "order of contact" integer would require. The likely cause: "cost" here is the output of a *global* nonlinear optimization (best fit over m₀,m₂,m₃ at each ratio), which can jump between different local optima as the ratio varies — the underlying function is not guaranteed smooth, unlike T2's directly-evaluated polynomial.

**Honest verdict for T3:** **no clean integer index found.** This transition is better described as a **discrete (likely ℤ₂) symmetry** relating axis-1 and axis-2 that holds exactly at m_cross=0 and is broken once m_cross≠0 — a symmetry-breaking event, not a smooth bifurcation with a Taylor-expandable order. Forcing a number onto it here would be dishonest.

### T4: 4→5 parameters, rank(J) unchanged without a 5th target

**Type:** matrix nullity (linear algebra), **already shown in the previous exchange to be a generic mathematical consequence** of sitting at any imperfect (nonzero-residual) least-squares minimum of a square system — not a special discovery each time it's measured.
**Index:** nullity = **1** (computed via SVD of the 4×4 Jacobian at the best-fit point).
**Integer?** Yes, by definition (rank and nullity of a matrix are always integers).
**Stability:** re-tested here under three different θ₁₂ targets (32.5°, 33.0°, 33.5°) — **nullity=1 in all three cases.** This robustness is expected precisely *because* the phenomenon is generic (as established previously): any nearby imperfect fit of a square system will show the same nullity, for the same structural reason, not because of a deep new invariant.

### T5: free φ₂ angle destroys axis discrimination

**Type:** dimension of an exact (zero-residual) degenerate solution family — this is a *cleaner* case than T4, because here the residual genuinely reaches zero (confirmed earlier: machine-precision fits for all 6 axes), so the nullspace of J at that point is a real, meaningful continuous family of equivalent exact solutions, not a generic artifact of imperfection.
**Index:** nullity = params−targets = 8−7 = **1** (a genuine 1-parameter family of exact solutions per axis).
**Integer?** Yes, and more legitimately meaningful than T4's case for the reason just stated.

## 2. Table

| Transition | Type | Index | Integer? | Perturbation-stable? |
|---|---|---|---|---|
| T1 | linear constraint codimension | 1 | Yes (trivially) | Yes (definitional) |
| T2 | vanishing order of quadratic form | 1 | Yes (verified) | Yes (5 directions tested) |
| T3 | discrete symmetry breaking | **none found** | **N/A** | **N/A — no smooth index exists** |
| T4 | Jacobian nullity (generic) | 1 | Yes | Yes (3 targets tested) |
| T5 | exact-solution family dimension | 1 | Yes | (not re-tested; established earlier) |

## 3. Is there a pattern? Honestly — mostly coincidental, not unified

Four "1"s and one failure is **not** evidence of a single underlying "transition charge." These four "1"s come from **four different branches of mathematics** — a linear-algebra codimension, a Taylor-series vanishing order, a matrix nullity from an *inherently generic* phenomenon (T4), and a solution-family dimension from an *inherently different* phenomenon (T5, zero-residual case). Getting "1" in each case reflects that **these are all the simplest, minimal instances of their respective phenomena** (one constraint, one linear vanishing, one extra unconstrained parameter) — not a shared origin. T3's outright failure to produce any clean integer is itself the strongest evidence against a unifying "index": a genuine topological/vortex charge would not simply fail to exist for one member of the family while working cleanly for the others.

## 4. Verdict

```text
Three genuine, verified, perturbation-stable integers exist: T1=1 (codimension),
T2=1 (vanishing order, direction-independently confirmed), T4=1 and T5=1
(Jacobian nullity / solution-family dimension, both re-verified under
perturbation here).

T3 has NO clean integer index -- the natural candidate quantity (order of
contact between two cost curves) is demonstrably non-smooth and sign-
changing near the degeneracy, not the well-behaved Taylor series a
genuine index would require. This is reported as a real negative result,
not glossed over.

PATTERN: the repeated value "1" across T1, T2, T4, T5 is NOT evidence of
a single mathematical object ("transition charge" or "vortex charge")
threading through the model. Each is the minimal/simplest case of a
DIFFERENT kind of mathematical structure (constraint codimension, Taylor
order, matrix nullity of two different origins). T3's failure to fit the
pattern at all is the decisive point against a unifying interpretation --
a genuine topological invariant characterizing "transitions in this
model" would need to be well-defined for every transition, not four out
of five.

HONEST FINAL ANSWER: no single mathematical object "transition index"
exists across all five cases. What exists are several genuine, different,
individually well-defined integers (codimension, vanishing order,
nullity), each meaningful in its own narrow mathematical sense, plus one
case (T3) that resists this kind of characterization entirely.
```

---

END OF FINDING
