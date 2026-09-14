# COVER — Fano-sextet quartic bridge: a correction and its completion

**Stenberg side (with Claude), 2026-09-14. Free exploration, not a sealed
stone. Rule 3 holds — the King–Luhn physics stays parked out of the joint
paper; this is a mathematics note for the correspondence.**

Following your Fano-sextet v3 (Results 1–7), we took up the three open ends on
our side. One correction and three completions, each verified in code; your
King–Luhn equations were re-checked verbatim against the arXiv **PDF**.

## The one correction (Result 2)
Your "six invariants from Fano combinatorics, rank 6, matching King–Luhn's six
quartic invariants exactly" is a **coincidence of mixed degrees**: five of the
six are quartic, but `I_prod = |Σ_line χχχ|²` is **sextic** (scales ×64 under
χ→2χ, not ×16). The five quartics span only a **5-dim** subspace of King–Luhn's
6-dim quartic space. `rank = 6` is true, but they are not the six quartics.
Result 1 (χ₆ = Fano module) and Result 7 (intertwiner) are untouched.

## The three completions
1. **The missing sixth quartic, explicit:** the unique chiral (conjugation-odd)
   invariant `Q_miss = Im⟨χ², χ⋆χ⟩` = `Im Σ_i conj(χ_i²)(Σ_{L∋i} χ_jχ_k)` — the
   pairing of the pointwise-square and line-collinearity maps. It **is**
   King–Luhn's ℐ₅ (their eq 4.6). The corrected Fano quartic basis is your five
   real quartics **+ `Q_miss`**, which spans King–Luhn's whole quartic space.
2. **The √7, derived two ways:** (a) geometric — the Fano permutation metric's
   exact `{1,7}` eigenvalue split (the deleted-point axis; this is also the
   intertwiner's √7 singular-value ratio); (b) analytic — imposing King–Luhn's
   top vacuum (2.10) critical reproduces **κ₂=κ₃=κ₄+κ₅/√7 to 1e-11** from the
   raw Θ, Θ' (4.2–4.3). (Their footnote 2 carries the same √7 explicitly.)
3. **The Result-6 coexistence window, explained:** an exchange-of-stability
   bifurcation — the S4 minimum softens and the S2 minimum hardens along A→B,
   and the window is exactly the overlap of the two eigenvalue zero-crossings
   `[0.115, 0.135]`. It does **not** need the sextic (survives at κ_prod=0), so
   it is a genuine feature of the real quartic potential.

Cross-checks that landed on their own: King–Luhn's own κ₅ Hessian (their eq
4.16) is purely Re–Im off-diagonal — exactly `Q_miss`'s structure; and the 6/6'
labelling freedom we used is stated in their text.

## Asks
1. Your word on the **Result 2 correction** (five quartics + one sextic;
   corrected sixth = `Q_miss` = ℐ₅). We propose recording it as a correction to
   the received v3, physics still parked.
2. Whether you want `Q_miss` / the √7-derivation carried anywhere beyond this
   note (our default: parked with the rest of the flavon physics, Rule 3).
3. Nothing else pending from our side.

## Contents
- `FINDING_fano_quartic_correction.md` — the full write-up.
- `scripts/` — eight self-contained `_explore_*` scripts + their `.log`s.
- `SHA256SUMS.txt` (LF).
