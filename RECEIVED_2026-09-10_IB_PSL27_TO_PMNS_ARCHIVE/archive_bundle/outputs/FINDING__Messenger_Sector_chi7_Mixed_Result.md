# FINDING: Minimal Messenger Sector from χ₇ of PSL(2,7) — One Genuine Success, Two Honest Failures

**Status:** Mixed, with the failures being as informative as the success
**Method:** rather than assuming a messenger sector by fiat, select it from an *actual, computed* PSL(2,7) representation — reduces "which messenger" to a single well-motivated choice instead of an arbitrary one, while being explicit that the choice itself, and the mixing couplings, are still model input, not derivations from nothing.

---

## 1. Messenger representation — computed, not assumed

PSL(2,7) has irreps of dimension 1,3,3̄,6,7,8 (verified: sum of squares 1+9+9+36+49+64=168=|PSL(2,7)|). Computed the S₄ branching of the two not-yet-used ones directly (character inner products against the already-established S₄ character table):

```text
chi6 = Sym^2(3)  [verified irreducible, <chi,chi>=1]  -->  S4: 1 + 2 + 3
chi7 = (perm. rep on P^1(F7), 8 points) - 1            -->  S4: 1' + 3 + 3'
chi8 = (already used for phi2, Phi3, Phi3')            -->  S4: 2 + 3 + 3'
```

**χ₇ is the natural choice**: it is the *only* one of the three containing a **1′** component — exactly the Z₂-odd "companion field" speculated about (but never constructed) when the FN-charge pattern was first examined. Selected on this basis: **N ≡ χ₇ → (σ, ρ₃, ρ₃′) ~ (1′, 3, 3′) of S₄.**

**Already worth flagging:** neither χ₆ nor χ₇ contains a **second copy of "2"** — the representation φ₂ itself lives in. This is a structural fact, not a choice, and it already limits what this messenger can do (see §4a).

## 2. W_mess — forced, not chosen

χ₇ is a **real** representation (character values 7,-1,1,-1,0 are all real), so a single PSL(2,7)-invariant mass term N·N exists and is essentially unique. Decomposed under S₄:

```text
W_mess = (M_N/2) [ sigma^2 + (rho3.rho3)_1 + (rho3'.rho3')_1 ]
```

All three messenger components share the **same** mass M_N — this is forced by PSL(2,7) invariance, not a modeling choice.

## 3. W_mix — where genuine choices enter, and one fails on contact with the vacuum

**Direct couplings (work, generically nonzero):**
```text
W_mix superset g3 * Phi3 . rho3   +   g3' * Phi3' . rho3'
```
(using the ordinary 3⊗3→1 and 3′⊗3′→1 dot products, both nonzero for any nonzero Φ₃,Φ₃′). Integrating out ρ₃,ρ₃′ (linear EOM from W_mess+W_mix) gives effective mass terms:
```text
W_eff superset -(g3^2 / 2M_N) (Phi3.Phi3)_1  -  (g3'^2 / 2M_N) (Phi3'.Phi3')_1
```
— exactly the κ(ΦΦ)₁ structure already used for the flavon magnitude-fixing driving fields, now with **κ_Φ₃/κ_Φ₃′ = (g₃/g₃′)²** expressed in terms of messenger couplings.

**The σ-mediated cross term (the one meant to explain the FN asymmetry) fails at the vacuum:**
```text
W_mix superset g_sigma * sigma * (Phi3 . Phi3')_1'
```
is the natural, S₄-invariant candidate (σ~1′ pairs with the "1′" channel of Φ₃⊗Φ₃′ — the ordinary dot product χ·ξ). **This is identically zero at the established vacuum** — the same axis-mismatch obstruction found repeatedly throughout this session (Φ₃, Φ₃′ on different axes ⇒ no shared nonzero index ⇒ dot-product-type invariants vanish). σ decouples from Φ₃, Φ₃′ entirely at this vacuum; it cannot mediate the asymmetry it was introduced for.

## 4. Checking the five requested points

**a) φ₂'s direction — NO, structurally, not just "not found":** χ₇ contains no second "2" — φ₂ has no messenger partner to couple to via a renormalizable term with this N. This messenger cannot address φ₂'s direction *by construction*, independent of any coupling choice. Consistent with — and now explaining part of — the exhaustive earlier failure of five other mechanisms.

**b) κ=1 — NOT derived:** the effective κ_Φ₃/κ_Φ₃′ ratio is (g₃/g₃′)², expressed in terms of messenger Yukawa couplings that are themselves free parameters — this only *relocates* where the assumption lives (from "κ=1 for the neutrino cross-term" to "g₃=g₃′ for the messenger"), it does not remove it. No mechanism found here forces g₃=g₃′.

**c) The "+1 twist" rule — NOT derived, and the specific proposed mechanism fails:** the σ-mediated term meant to realize this vanishes identically at the vacuum (§3). The qualitative motivation (σ~1′ exists, is a genuine, computed part of χ₇) survives, but the concrete realization attempted here does not work.

**d) Σm_ν — unaffected (by construction, not verified further):** this messenger only modifies *how* Φ₃, Φ₃′'s magnitude-fixing coefficients arise (UV origin of c₃, c₃′), not the neutrino operator structure itself (M_ν's form, or the established c₃,c₃′ values, are untouched if the messenger is tuned to reproduce them). No new prediction for Σm_ν follows from this construction.

**e) Axis (2,0) — preserved, by construction, not because it was checked against a full re-fit:** this messenger sector only touches the *magnitude*-fixing sector (via effective (ΦΦ)₁ terms), not the *direction*-fixing sector (the separate (ΦΦ)₃=0 driving fields that set the axes). Since it doesn't introduce new dependence on which axis Φ₃/Φ₃′ occupy, there's no mechanism here for it to disturb axis selection — but this is an inference from the construction's structure, not a re-verified numerical fact.

## 5. Verdict

```text
ONE genuine success: chi7 of PSL(2,7) is a real, computed, non-arbitrary
messenger candidate containing exactly the 1' companion field motivated
earlier -- this is better grounded than simply asserting a Z2-odd field
exists.

TWO honest failures, both structural rather than "not tried hard enough":
  - phi2's direction: chi6 and chi7 both lack a second "2" -- this
    messenger family cannot touch phi2 by representation-theoretic
    necessity, not by bad luck in the coupling choice.
  - The specific sigma-mediated mechanism for the "+1 twist" rule
    vanishes at the established vacuum -- the same axis-mismatch
    obstruction encountered in essentially every cross-invariant
    attempted this session.

kappa=1 and "+1 twist" are NOT derived by this construction -- they are
relocated to equally-free messenger-coupling ratios (g3/g3', and the
now-broken sigma mechanism), consistent with the standing honest
assessment that these require UV input beyond S4 representation theory,
which a specific messenger CHOICE provides a home for, without removing
the need for input.

HONEST BOTTOM LINE: constructing a real messenger sector was a genuine,
worthwhile exercise -- it is more principled than asserting kappa=1 and
"+1 twist" by hand, and it cleanly explains WHY phi2's direction has
resisted five independent attempts (no messenger of this family can
reach it). But it does not deliver derivations of kappa, the twist
rule, or phi2's direction. This narrows the space of viable future
constructions (any messenger addressing phi2 needs a second copy of
"2", ruling out chi6 and chi7 -- chi8 itself, or a reducible messenger
combining multiple PSL(2,7) irreps, would need to be tried next) rather
than closing the question.
```

---

END OF FINDING
