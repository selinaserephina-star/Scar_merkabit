# FINDING — the Fano-sextet quartic bridge: a correction and its completion (2026-09-14)

**Stenberg side, with Claude. Free exploration (not a sealed stone).**
Follows the Fano-sextet v3 package (Results 1–7). Rule 3 stands: the
King–Luhn flavon **physics** remains parked out of the joint paper; this is a
mathematics note on the invariant-theory bridge, for the correspondence.

All King–Luhn equations below were checked **verbatim against the arXiv PDF of
0912.1344** (eqs 2.5, 2.10, 4.1–4.10), not a summariser.

---

## 0. Summary

One correction and three completions, each independently verified in code:

1. **Correction to Result 2.** The claim "six invariants built from Fano
   combinatorics, rank 6, matching King–Luhn's six quartic invariants exactly"
   is a **coincidence of mixed degrees**, not an identification. Five of the
   six are genuinely quartic; the sixth (`I_prod = |Σ_line χχχ|²`) is
   **sextic**. The five quartics span only a **5-dimensional** subspace of
   King–Luhn's 6-dimensional quartic space.
2. **The missing sixth quartic, explicit.** It is the unique conjugation-odd
   (chiral) quartic `Q_miss = Im⟨χ², χ⋆χ⟩` — the Hermitian pairing of the
   pointwise-square map with the line-collinearity map on the Fano plane. It
   **is** King–Luhn's antisymmetric cross channel ℐ₅.
3. **The √7 is geometric.** King–Luhn's √7 (in κ₂=κ₃=κ₄+κ₅/√7) has two
   independent first-principles origins, both derived here.
4. **The coexistence window (open end from Result 6) is explained** as an
   exchange-of-stability bifurcation, and is shown **not** to require the
   sextic.

---

## 1. Correction: Result 2's six are five quartics + one sextic

The space of PSL(2,7)-invariant quartic (2,2) forms is exactly 6-dimensional
(`⟨Sym²(6), Sym²(6)⟩ = 6.0000`), matching King–Luhn. Testing the homogeneity
degree of each of the second author's six invariants (scaling χ → 2χ):

| invariant | ratio | degree |
|---|---|---|
| Ig1, Ig2, Iline, Imixed, Iantisym | ×16 | 4 (quartic) |
| **Iprod = \|Σ_line χχχ\|²** | ×64 | **6 (sextic)** |

So `rank = 6` is true (six independent functions), but of **mixed degree**.
The five genuine quartics span a 5-dim subspace of King–Luhn's quartic space
(fit residual to the quartic span: 2e-15 for the five, 0.44 for `Iprod`).
`Iprod` cannot be one of King–Luhn's quartic invariants, and one genuine
quartic direction is absent from the second author's basis. This is why the
naive real construction returned five and reached for the sextic as its
"sixth". *(script: `_explore_fano_degree_check`)*

## 2. The missing sixth quartic, made explicit

The missing direction lies entirely in the doubled-sextet (6–6') block — zero
on the singlet |1|² and octet |8|² channels — and is intrinsically **chiral**
(odd under χ → χ̄), so no real point/line/pair monomial-sum can reach it. Four
natural real Fano quartics were tested and all fail to supply it.

The two independent PSL(2,7)-equivariant symmetric maps 6→6 on the Fano plane
have concrete meanings: the **pointwise square** `s_i = χ_i²` and the
**line-collinearity map** `ℓ_i = Σ_{L∋i} χ_j χ_k`. Their Hermitian pairing's
imaginary part,

> **`Q_miss(χ) = Im Σ_i conj(χ_i²) · ( Σ_{L∋i} χ_j χ_k )`**,

is the missing quartic. Verified: degree 4; `Q_miss(χ̄) = −Q_miss(χ)` exactly;
lies in the quartic space (residual 1e-14); `rank(Ilya's 5 + Q_miss) = 6`; and
`{Ilya's 5, Q_miss}` spans the whole quartic space. So the corrected Fano
quartic basis is **the second author's five real quartics + `Q_miss`**.
*(scripts: `_explore_fano_missing_quartic`, `_explore_fano_chiral_quartic`)*

`Q_miss` is the unique conjugation-odd quartic invariant, and it **is**
King–Luhn's ℐ₅ (eq 4.6, the antisymmetric cross term). Confirmed in two ways:
the space splits canonically as **5 conjugation-even (= the five real quartics)
⊕ 1 conjugation-odd (= `Q_miss`)**, and King–Luhn's own Hessian for κ₅ (their
eq 4.16, `h₅ = [[0, h̃₅],[h̃₅, 0]]`) is purely Re–Im off-diagonal — exactly the
structure `Q_miss` produces at a real vacuum.

## 3. The √7, derived two ways

**(a) Geometric.** The Fano sextet is the sum-zero subspace of ℝ⁷ with the
plain permutation metric. In the deleted-coordinate frame that metric is
`I + 𝟙𝟙ᵀ`, with eigenvalues **{1×5, 7×1}** — the eigenvalue-7 axis being the
deleted-point diagonal. The intertwiner S between the Fano and the LNR sextet
has singular-value ratio exactly √7 for this reason, and `S†S` equals the
group-averaged invariant metric to 4e-14. So the √7 is the norm ratio between
the one deleted point and the other six. *(script:
`_explore_fano_intertwiner_metric`)*

**(b) Analytic — King–Luhn's exact relation reproduced.** Building King–Luhn's
six invariants from the raw Υ, Θ, Θ' (eqs 4.1–4.6, PDF-verified) and imposing
that their top vacuum ⟨χ_top⟩ (eq 2.10, PDF-verified) is a critical point of
the general potential, **every** allowed coupling family satisfies, to machine
precision:

> `κ₂ − κ₃ = 0` (≤ 9e-12) and `κ₂ − (κ₄ + κ₅/√7) = 0` (≤ 2e-11).

i.e. **`κ₂ = κ₃ = κ₄ + κ₅/√7` is reproduced from first principles** — the √7
is forced by top-vacuum criticality. (Consistent with the √7 in King–Luhn's
own footnote-2 SU(3) combination `2ℐ₂+2ℐ₃+ℐ₄−√7 ℐ₅`.) *(script:
`_explore_kingluhn_sqrt7_derivation`)*

Our Hessian machinery was validated first by reproducing the second author's
Result-3 doublet/triplet coefficients exactly
(336/192/96/360/−2240 doublet; 336/108/96/416/−2240 triplet).
*(script: `_explore_fano_vacuum_hessian_corrected`)*

## 4. The coexistence window (Result 6 open end) — explained

Tracking both vacua's least Hessian eigenvalue along the A→B interpolation: the
S4 minimum **softens** monotonically (its S2-breaking doublet mode crosses zero
at t ≈ 0.135, destabilising) while the S2 minimum **hardens** monotonically
(crosses zero at t ≈ 0.115, stabilising). The coexistence window is exactly the
overlap `[0.115, 0.135]` — an **exchange of stability** (subcritical
bifurcation), its edges being this pair of eigenvalue zero-crossings. Nothing
arbitrary about "there".

Further: the window does **not** require the sextic. It persists at κ_prod = 0
(pure quartic-in-five), so coexistence lives in the five real quartics — which
are King–Luhn quartic channels — not in the extra sextic. And since `Q_miss` is
chiral (vanishes on real vacua), the corrected quartic potential gives the
identical real-vacuum coexistence: a genuine feature available to a proper
quartic flavour potential. *(script: `_explore_fano_coexistence_why`)*

---

## What stands, what is corrected

- **Unaffected:** Result 1 (χ₆ = Fano deleted permutation module, in §11.9);
  the intertwiner Result 7; the whole representation/vacuum basis match.
- **Corrected:** Result 2's "matching King–Luhn's six quartic invariants
  exactly" — it is five quartics + one sextic; the correct sixth quartic is the
  chiral `Q_miss` = King–Luhn ℐ₅.
- **Completed:** the √7 (geometric + analytic), and the Result-6 coexistence
  mechanism.

## Files (all self-contained, numpy/scipy; free exploration, not sealed)

- `_explore_fano_intertwiner_metric_2026-09-14.py` — the {1,7} metric / √7 geometry.
- `_explore_fano_kingluhn_channels_2026-09-14.py` — canonical 1/6/6'/8 channels; the failed 6↔6.
- `_explore_fano_degree_check_2026-09-14.py` — the degree correction (five quartics + one sextic).
- `_explore_fano_missing_quartic_2026-09-14.py` — the missing direction, pure 6–6' chiral.
- `_explore_fano_chiral_quartic_2026-09-14.py` — `Q_miss` explicit and verified.
- `_explore_fano_vacuum_hessian_corrected_2026-09-14.py` — validates Result 3; corrected-basis Hessian.
- `_explore_kingluhn_sqrt7_derivation_2026-09-14.py` — reproduces κ₂=κ₃=κ₄+κ₅/√7 from raw eqs.
- `_explore_fano_coexistence_why_2026-09-14.py` — coexistence = exchange of stability; sextic not needed.

(each with its `.log`)

---
END OF FINDING
