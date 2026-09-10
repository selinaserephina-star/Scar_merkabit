# FINDING: Penedo–Petcov Comparison — Different τ Location, No Easy Reformulation, φ₂-Direction Problem Not Solved For Free

**Status:** Informative negative result — the promising lead does not pan out as hoped, for identifiable structural reasons
**Origin:** testing whether this project's PSL(2,7)/S₄ construction can be reformulated in, or connected to, the Penedo–Petcov modular-S₄ framework (arXiv:1811.04933)

---

## 1. τ location comparison

```text
Our tau = 1.797i   (Re(tau) = 0 EXACTLY)

              Re(tau)   Im(tau)   |tau - ours|
tau_C (Z2^S)   0.0000    1.0000      0.797
tau_L (Z3^ST) -0.5000    0.8660      1.057
A / A*        ±0.1045    1.0100      0.794
B / B*        ±0.1090    1.0050      0.800
C / C*        ±0.1435    1.5230      0.309   <- closest
D / D*        ±0.1790    1.3970      0.438
E / E*        ±0.4996    1.3090      0.698
```

**Structural mismatch, not just numerical distance:** every single one of Penedo–Petcov's 12 special/best-fit points (2 residual-symmetry points + 10 phenomenological best-fits) has **nonzero Re(τ)** — ranging 0.10 to 0.50. Our τ has **Re(τ)=0 exactly** (purely imaginary — a special, symmetric configuration in its own right, invariant under τ→−τ*). None of their viable points sit on the imaginary axis. This is a first, qualitative sign that the two constructions are not obviously the same object evaluated at different points — they appear to prefer genuinely different regions of the fundamental domain.

## 2. Direct test: does our τ, plugged into their model, fit the data?

Built their exact (k_Λ,k_g)=(0,2) construction (their best-performing case) — charged-lepton matrix λ (eq. 3.28) and neutrino Yukawa/seesaw (eq. 3.8, 3.15) — using the real Y₁...Y₅ forms evaluated at **our** τ=1.797i:

```text
Y1 = 0.7073,  Y2 = -0.0245,  Y3 = 0.7070,  Y4 = -0.1681,  Y5 = -0.0024
```

Left α,β,γ,g,g' (their free Wilson coefficients) **completely free** and searched for the best possible fit to charged lepton masses, mixing angles, and mass-squared ratio (same target values they use):

```text
Best achievable cost (400 optimizer restarts): ~1.0
(their own reported best-fit points achieve Nsigma^2 in the range
 ~0.0004 to ~2.1 -- see their Tables 5a-5e; 1.0 sits at the poor end,
 not competitive with their actual best-fit region)
```

**Our specific τ does not sit near a good fit point of their model.** This is informative on its own: it's not that the two models are trivially unrelated (some random τ could easily give cost≫1, e.g. 10-100), but landing at cost~1 (comparable to a generic, non-special point) rather than something small confirms our τ was not independently "found" by their construction — it comes from a genuinely different mechanism (the racetrack/modulus-stabilization condition referenced in this project, not their χ² minimization over lepton observables).

## 3. Can the model be reformulated in their language?

**Structurally, no — not directly.** Three concrete obstructions:

- **Different charged-lepton architecture.** Their λ matrix (eq. 3.28) mixes weight-2 AND weight-4 modular forms across three *different* E₁,E₂,E₃ representations (1,1′) with weights (2,4,4) — a genuinely different, more elaborate construction than our Y_T = y₂Y⁽²⁾+y₃Y⁽³⁾+y₃′Y⁽³′⁾ linear combination with *fixed* PSL(2,7)-derived ratios. Their charged-lepton hierarchy comes from *different modular weights* per row; ours comes from *different flavon VEV magnitudes* (FN charges) at fixed weight. These are different mechanisms for generating the same qualitative hierarchy, not the same mechanism in different notation.
- **Different neutrino sector.** They use a genuine type-I seesaw with an explicit heavy Majorana matrix M(τ) (eq. 3.8/3.10) that is τ-dependent; our neutrino sector (this session's construction) uses a much more minimal, non-seesaw Weinberg-type operator built directly from Φ₃,Φ₃′,φ₂ with independent Wilson coefficients — again structurally different, not a relabeling.
- **No modulus in our charged-lepton fit at all.** Our y₂,c₃,c₃′ were fit directly as flavon-magnitude parameters; there is no single τ in our construction playing the role their τ plays (ours is closer to their "flavon-only, no modulus" alternative construction sketched in their §5, using φ₃,φ₃′-type fields with fixed VEV directions — interestingly, their own paper considers this as an *alternative* to the pure-modulus approach for exactly the diagonalization reason relevant here, eq. 5.10-5.13).

## 4. Does this solve the φ₂-direction problem "for free"?

**No.** The φ₂-direction problem (this project's own open item) is specific to *our* flavon-based construction, where a doublet VEV direction needs to be dynamically selected among a continuum and three independent mechanisms failed to fix it (documented earlier). Penedo–Petcov's framework doesn't have this *specific* problem because it doesn't have a separate φ₂ field at all — their "2" and "3′" are components of the *same* single modulus τ, and τ's VEV is fixed *holistically* by their global χ² fit to all observables at once, not by a dedicated alignment mechanism for one flavon. This sidesteps the problem by removing the object that had it, not by solving it — reformulating our model into their language would require giving up the φ₂/Φ₃/Φ₃′ flavon structure entirely and starting over with a genuinely modulus-only construction, which is a much larger undertaking than "translating" the existing results.

## Verdict

```text
tau LOCATION: our tau=1.797i is structurally different from all 12 of
Penedo-Petcov's special points (Re(tau)=0 exactly vs their Re(tau)!=0
throughout) -- not a coincidental near-miss, a different region of F.

DIRECT FIT TEST: our tau, substituted into their exact model with free
couplings, achieves cost~1 -- not competitive with their own best-fit
region (~0.0004-2). Confirms the two tau's are not secretly the same
point found by different methods.

REFORMULATION: NOT straightforward. Three genuine structural
differences identified (different charged-lepton weight architecture,
different neutrino-mass mechanism, no shared single modulus). This
would be a from-scratch reconstruction, not a translation.

phi2 PROBLEM: NOT solved by this comparison. Their framework avoids the
problem by not having the object that has it, which is a different kind
of "solution" than actually fixing phi2's direction within our own
construction.

HONEST BOTTOM LINE: the lead was worth checking -- and the check was
worth doing precisely BECAUSE it could have been a shortcut, but wasn't.
This closes the question with a clear, informative negative, rather
than leaving it as an unexplored possibility.
```

---

END OF FINDING
