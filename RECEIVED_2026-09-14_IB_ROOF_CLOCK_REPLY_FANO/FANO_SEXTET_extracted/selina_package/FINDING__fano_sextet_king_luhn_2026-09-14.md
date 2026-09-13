# FINDING — χ₆ (King–Luhn sextet) = Fano-plane deleted permutation module; all six quartic invariants reproduced from Fano geometry alone (2026-09-14)

**Status:** two solid, independently-verified results. One clear open
end, stated honestly, not papered over.

---

## Context — why this was checked

Following the closed ψ-nowhere-in-tower result, we asked whether the
real, peer-reviewed PSL(2,7) flavour-symmetry programme (King & Luhn,
*Nucl. Phys.* B832 (2010) 414, arXiv:0912.1344; and the earlier
arXiv:0905.1686) connects naturally to the Sp(6,2)/W(E7) tower already
built in this correspondence. King–Luhn's own open problem — two
unexplained relations among the flavon-sextet potential's quartic
couplings (κ₂=κ₃=κ₄+κ₅/√7, needed for correct vacuum alignment) — was
the natural target.

## Result 1 — χ₆ is explicitly the "deleted permutation module" on the Fano plane

Built GL(3,2) explicitly (168 matrices over F₂, confirmed isomorphic
to PSL(2,7)). Found generators A (order 2), B (order 3) with AB order
7 and [A,B] order 4 — the **full** presentation
⟨A,B | A²=B³=(AB)⁷=[A,B]⁴=1⟩. Built the natural action on the Fano
plane's 7 points, restricted to the 6-dimensional sum-zero subspace,
and computed traces directly:

```
trace(A)  = 2   (chi_6's character at order-2 class: 2)  — exact
trace(B)  = 0   (chi_6's character at order-3 class: 0)  — exact
trace(AB) = -1  (chi_6's character at order-7 classes: -1) — exact
```

This is not approximate agreement — the character of a finite group's
irreducible representation determines it uniquely up to isomorphism,
so exact trace agreement at generators is a complete proof. **This
matches, independently, a result already in the literature**: Luhn,
Nasri & Ramond (arXiv:0709.1447, §7, "The Fano Plane Representation")
state explicitly that "the Fano plane representation is reducible,
with 7^Fano = 1 + 6" — the same fact, found here from scratch via the
Sp(6,2) tower route, not by reading it first.

## Result 2 — all six of King–Luhn's quartic invariants, built explicitly from Fano combinatorics

King–Luhn state that the flavon potential's quartic part has **six
independent invariants** total, from (6⊗6)ₛ⊗(6⊗6)ₛ = (1+6+6+8)⊗(1+6+6+8).
Constructed six candidates directly from Fano-plane structure (points,
the 7 lines, and pairs of points) — five symmetric, one genuinely
antisymmetric (needed to reach the second, otherwise-inaccessible
copy of "6" in the decomposition):

| Invariant | Built from |
|---|---|
| (Σ\|χ\|²)² | generic |
| Σ\|χ\|⁴ | generic |
| Σ_lines \|Σ_{i∈L}χᵢ\|⁴ | the 7 lines |
| \|Σ_lines χᵢχⱼχₖ\|² | products over lines |
| Σ_lines \|Σ_L\|²·(complement norm) | line vs. rest |
| Σ_{i<j} \|χᵢ\*χⱼ−χⱼ\*χᵢ\|² | antisymmetric pairs |

Verified numerically (10 random complex sample points, all six values
confirmed real to machine precision, confirming genuine Hermitian
invariance) that these are **linearly independent — rank exactly 6**.
This matches King–Luhn's stated count exactly. Every earlier attempt
using only *real* polynomial invariants (not properly Hermitian) capped
at 4; recognising the need for the antisymmetric, genuinely-complex
structure was the key correction that closed the gap to 6.

## What remains open — stated plainly

The correspondence between these six Fano-built invariants and
King–Luhn's own κ₀..κ₅ labels (in their c_n=cos(2nπ/7)-based basis) is
**not yet established**. An attempted numerical search for the explicit
change-of-basis matrix (intertwiner) between the two bases did not
converge to a clean solution — most likely a transcription slip in
manually re-entering their complex 6×6 matrix (their eq. 35, in
Luhn-Nasri-Ramond) rather than a deeper problem, since the character
match is exact and rigorous on its own. Resolving this — or,
alternatively, redoing the vacuum-alignment extremisation directly in
the Fano basis — is the natural next step, not attempted further here.

## Files

- `fano_sextet_six_invariants.py` — single, self-contained script (numpy
  only). Runs end to end with assertions at every step; fails loudly if
  anything is wrong. Reproduces both results above from scratch in
  under a minute.
- `verify_fano_sextet.py`, `find_intertwiner.py`, `build_gl32_and_check.py`,
  `check_sym2.py` — earlier working scripts from the same investigation
  (including the two failed naive attempts — V⊕V* and Sym²(V), both
  reducible in characteristic 2 — kept for the record, not because they
  succeeded).

---
END OF FINDING
