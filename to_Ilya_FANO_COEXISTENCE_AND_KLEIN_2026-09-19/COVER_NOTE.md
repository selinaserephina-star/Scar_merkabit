# COVER — your Results 12–20 received; the coexistence window stands (exact check); the Klein Jacobian is E³; the Sp(6,2) scripts reproduce

**Stenberg side (with Claude), 2026-09-19. Free exploration, not a sealed
stone. Rule 3 holds — the King–Luhn physics stays parked out of the joint
paper; nothing here changes draft v0.8.**

Your eight saves of the Fano finding arrived together (Results 1–11 through
1–20). Two of the zips were truncated downloads; the newest (`…-18.zip`,
Results 1–20) I rebuilt file-by-file from its own SHA256SUMS — 26 of 27
verify. Thank you for Result 12: the correction and the three completions
cross-verified on your own infrastructure is exactly what the envelope asked
for, and your finding that `Q_miss`/I₅ is an exactly constant ratio is
stronger than our Hessian comparison was.

## 1. Result 15 — the coexistence window survives; please look again

Your retraction of Result 6 says zero coexistence in 210 samples on the
corrected 4-term potential. Our envelope said the window survives at
κ_prod = 0. Both cannot stand, so I checked the one point we named **exactly**
— symbolic Hessian restricted to the 6-dim sum-zero sextet (no
finite differences, no spurious all-ones direction), critical points refined
to 30 digits:

```
kappa = (g1 = 1.116625, g2 = 0.694583333, line = 0.174625, prod = 0, mixed = 1.087375)
m^2   = 28.5966979   (S4 critical at a=b=c=1)

line-S4 vacuum   a=b=c=1                     eigs {0.1044 x2, 0.2637 x3, 114.39}   strict minimum
second vacuum    a=2.12221068, b=c=-0.35370178  eigs {0.1937 x2, 0.3325 x3, 114.39}   strict minimum
```

Window on the original A→B path with κ_prod ≡ 0: **t ∈ [0.1155, 0.129]**. Your
scan ran a *different* line (A′=(1,⅔,0.1,1) → B′=(1,1,1,1)), where there is
indeed a gap, and 150 random points in a 4-dimensional box did not hit the
thin region. Our two scripts share every definition (lines, `build_phi`, the
four invariants, the 7×7 FD Hessian), so this is a sampling miss, not a
convention dispute. Your own `is_stable` at the point above returns True for
both. Script and log enclosed.

**And a thing neither of us had seen:** the second vacuum has **b = c = d and
a = −6b** to 10⁻¹² — it is the **point-stabilizer S4 vacuum
(6,−1,−1,−1,−1,−1,−1)**, the Fano dual of your line vacuum (4,4,4,−3,−3,−3,−3).
So the coexistence is between the two S4 classes of PSL(2,7), which the outer
automorphism (Fano duality) swaps and the potential does not (I_line is not
self-dual) — hence the different energies and the identical 2+3+1 eigenvalue
pattern at both. It also reads your Result 14's "stable S2-type points" and
your Result 15 handoff as line-S4 ↔ point-S4.

## 2. Result 20 — the script is missing

`fano_degenerate_vacuum_family_DISCOVERED.py` (sha bbbc2082…) is listed in the
`-18` SHA256SUMS but the download was cut before it. Could you resend that
zip, or the script alone? Result 20 is the one substantial open item in the
whole finding and we would like to run it.

## 3. Your Klein-quartic Jacobian note (2026-09-15)

The F₃₇ arithmetic is right; the reading "A a simple CM surface, Hom(E,A)=0"
is F₃₇-rational only. Geometrically **J(X(7)) ~ E³**, E = 49a1, with the
isogeny defined over ℚ(ζ₇)⁺. Point counts (enclosed, no tables): at p ≡ 1
(mod 7) — 29, 43, 71, 113, 127 — a₁(J) = 3·a_p(49a1) exactly; at p of order 3
mod 7 — 37, 53, 79 — a₁ = 0 and P_J is a polynomial in T³ (your −450T³ is
−(α³+ᾱ³)). Your "9 classes" is rank NS(E³) = 3 + 3·2 = 9, six of them the
cross classes from End(E) that the E × A picture sets to zero. The cycles are
the graphs of the CM endomorphisms between the three factors.

## 4. Sp(6,2) Katz–Sarnak package

Both Python scripts re-run here and reproduce your output exactly (branch
point ≈ −2.8744e12; 1225/1225 primes matched, 0 unmatched). Magma not run on
this side. Filed in the Companion lane, where the family test lives.

## Asks

1. Your word on **Result 15**: reverse the retraction of Result 6 (or restate
   it as "gap on path A′B′, overlap on path AB"), and the identification of
   the second vacuum as the point-S4 vacuum.
2. **Resend** the `-18` zip or `fano_degenerate_vacuum_family_DISCOVERED.py`.
3. **Result 18's 7×4 correspondence** is board mathematics, not physics. Do
   you want it as a one-line remark in §11.9 of the draft (JOINT)? Our default
   if you do not say: leave the draft at v0.8.
4. The Klein note is your lane's; nothing asked beyond your word that the E³
   correction is received.

## Contents

- `FINDING_coexistence_exact_and_point_vacuum.md` — §1 in full.
- `KLEIN_JACOBIAN_E3_note.md` — §3 in full.
- `scripts/_explore_fano_coexistence_exact_2026-09-19.py` + `.log`
- `scripts/klein_jacobian_pointcount_2026-09-19.py` + `.log`
- `scripts/RERUN_sp6_2_python_scripts_2026-09-19.log`
- `SHA256SUMS.txt` (LF).
