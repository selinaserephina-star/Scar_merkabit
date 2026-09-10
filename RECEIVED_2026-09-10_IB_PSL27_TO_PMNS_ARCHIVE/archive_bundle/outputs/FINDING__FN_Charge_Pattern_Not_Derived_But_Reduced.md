# FINDING: FN-Charge Split (Φ₃=2, Φ₃′=1) Reduces to One Rule, Not Derived From S₄ Alone

**Status:** PARTIAL — genuine reduction in arbitrariness, explicitly NOT a first-principles derivation
**Origin:** checking whether the established FN charges (φ₂:1, Φ₃:2, Φ₃′:1) follow from a single organizing principle rather than three independent choices
**Epistemic standard:** same as applied to κ=1 in the neutrino cross-term — state plainly what is and isn't shown

---

## 1. Why a strict derivation is impossible from S₄ alone

The magnitude-fixing driving-field condition κ·(ΦΦ)₁ = f(η) uses **(ΦΦ)₁**, which is an S₄ singlet by construction (that is what the subscript "1" means). S₄ invariance therefore permits **any** power of η on the right-hand side — η¹, η², η⁴, anything — with equal validity. The specific power (equivalently, the FN charge) is fixed by the details of whatever messenger diagram actually generates the term, which is not specified by S₄ representation theory and was not derived here, exactly as with κ in the neutrino sector.

## 2. What can be shown: one rule reproduces all three charges

Using the established fact that generation transforms as 3′ (the reference grading), and that 3 = sign⊗3′ while 2 = sign⊗2 (self-dual — verified earlier this session via direct character computation):

```text
Rule: FN charge = 1 + [1 if field's S4 grading is sign-twisted relative
                        to generation (3'), else 0]

phi2      = 2   (self-dual, untwisted relative to 3')   -> charge 1+0=1   [established: 1, MATCHES]
Phi3'     = 3'  (same grading as generation)             -> charge 1+0=1   [established: 1, MATCHES]
Phi3      = 3 = sign x 3' (twisted relative to generation) -> charge 1+1=2 [established: 2, MATCHES]
```

All three previously-separate charge assignments follow from **one binary fact per field** (its sign-twist relative to the generation grading), and that fact is fully fixed by S₄ representation theory alone — no new number was introduced to make this match; the "twisted / untwisted" classification was already determined in §2 of the earlier basis-matching work (the sign(g) = ρ₃′(g)⁻¹ρ₃(g) relation).

## 3. What this is, honestly

This is **not** a derivation of *why* twisted fields cost one extra power of the messenger scale — that "+1" is itself an assumed rule (equivalent to assuming a companion Z₂-odd field, order ε, mediates the extra suppression), not derived from anything more fundamental in this session. What **is** shown is that the three previously-independent integers collapse to **one** organizing choice ("twist costs +1") applied to a **fully S₄-determined** classification. This is the same *kind* of result as the κ=1 check: not a proof, but a genuine, checkable reduction in the number of free assumptions — from 3 arbitrary integers to 1 arbitrary rule.

## 4. Verdict

```text
FN-CHARGE ASYMMETRY: not derived from S4 alone (impossible in principle,
per SS1) -- but reduced from 3 independent integer choices to 1 minimal
rule ("sign-twist relative to generation costs one extra power"),
verified to reproduce all three established charges (1,1,2) exactly,
using only representation-theoretic facts already established elsewhere
in this project (no new input beyond the twist classification itself).

This sits alongside the kappa=1 result as the same category of honest
partial progress: an assumption that is economical and falls out of a
single simple rule, not an assumption pulled from nowhere -- but still
an assumption, not a proof.

RECOMMENDATION: state the model's free assumptions as TWO minimal rules
going forward (kappa=1 for the neutrino cross-term; "twist costs +1"
for the FN-charge pattern) rather than as four unrelated numerical
choices (kappa, n_phi2, n_Phi3, n_Phi3'). This is the honest, current
floor of the model's economy of assumptions.
```

---

END OF FINDING
