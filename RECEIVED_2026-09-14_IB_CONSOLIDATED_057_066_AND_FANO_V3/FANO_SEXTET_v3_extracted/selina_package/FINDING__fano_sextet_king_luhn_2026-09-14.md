# FINDING — χ₆ (King–Luhn sextet) = Fano-plane deleted permutation module; all six quartic invariants reproduced from Fano geometry alone (2026-09-14)

**Status:** five results, each independently verified or symbolically
derived. Two open ends, stated honestly, not papered over.

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

This is a complete proof by character theory. **Independently
corroborated in the literature**: Luhn, Nasri & Ramond (arXiv:0709.1447,
§7) state the same fact outright ("7^Fano = 1+6"), found here before
that paper was consulted.

*(2026-09-14 update: Selina's side independently confirmed that this
same 7-point Fano set — appearing as both the "Fano points" and "Fano
planes" orbits of the bitangent/W(E7) board's §11.3 — is literally the
same plane as this construction, not a structural look-alike. Folded
into the joint draft as §11.9.)*

## Result 2 — all six of King–Luhn's quartic invariants, built explicitly from Fano combinatorics

King–Luhn state the flavon potential's quartic part has **six
independent invariants**, from (6⊗6)ₛ⊗(6⊗6)ₛ = (1+6+6+8)⊗(1+6+6+8).
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
confirmed real to machine precision) that these are **linearly
independent — rank exactly 6**, matching King–Luhn's count exactly.

## Result 3 (follow-on) — the S4 vacuum, found explicitly, and a principled degeneracy relation

**The S4-breaking vacuum, found explicitly.** The subgroup of PSL(2,7)
stabilizing one Fano line (order 24 = S4) has an exactly
1-dimensional fixed subspace in the sextet: **+4 on the line's 3
points, −3 on the complementary 4** — the direct Fano-coordinate
analogue of King–Luhn's "3–3 aligned" top-Yukawa vacuum.

**χ₆ restricted to this S4, decomposed exactly.** Character inner
products over all five S4 classes give **χ₆|_S4 = 1 ⊕ 2 ⊕ 3₁** exactly.

**Hessian at the vacuum, computed symbolically.** By Schur's lemma,
the doublet (2) and triplet (3₁) blocks each get a scalar Hessian
eigenvalue:

```
doublet:  336κ_g1 + 192κ_g2 + 96κ_line + 360κ_mixed − 2240κ_prod − 2m²
triplet:  336κ_g1 + 108κ_g2 + 96κ_line + 416κ_mixed − 2240κ_prod − 2m²
```

Requiring doublet = triplet collapses to exactly **3κ_g2 = 2κ_mixed** —
derived, not searched for; the cancellation of five of the seven terms
was not assumed going in.

## Result 4 (follow-on) — the V4 family: structurally explained, twelve critical points found, none stable at the tested couplings

King–Luhn's neutrino/TB-mixing vacuum is stated to preserve only two
of S4's three named generators ("S, U"), generating a Klein
four-group V4 ⊂ S4 — the natural next object.

**V4, found and explained.** The index-3 subgroup of the same S4
(order 4: identity plus the three double-transpositions of the 4
complement points) fixes all **3 line-points individually** (unlike
S4, which permutes them via S4/V4≅S3). This gives a **3-dimensional**
invariant subspace — 3 free line values + 1 forced-equal complement
value − 1 sum-zero constraint = 3.

**Twelve critical points found** (60 random starts, one illustrative
coupling choice κ=1 each), including one exactly rational point,
(a,b,c)=(1,−1,0) at m²=14 exactly (gradient zero to machine precision).

**Honest result: every point checked is a saddle at this coupling
choice** (3 negative Hessian eigenvalues each, on the two points
checked in detail). Not a search failure — the correct, informative
answer that stability depends sensitively on the actual coupling
values, not fixed by group theory alone, exactly as King–Luhn
acknowledge for their own potential.

## Result 5 (follow-on) — the stability inequality, and a genuine stable point found

Does the degeneracy relation (Result 3) also give a **stable** vacuum,
not merely a critical point with equal transverse eigenvalues?
Imposing κ_g2=(2/3)κ_mixed and eliminating m² via the scale-fixing
equation, the now-5-fold transverse eigenvalue reduces to a clean
closed form:

```
transverse eigenvalue = -(224/3) · (12κ_line − 2κ_mixed + 105κ_prod)
```

**Stability condition (derived): 2κ_mixed > 12κ_line + 105κ_prod.**
κ_prod's coefficient (105) dwarfs κ_line's (12) — stability is
disproportionately sensitive to the line-product invariant
specifically, a concrete, non-obvious fact.

Verified numerically (Hessian projected onto the 5-dimensional
transverse subspace directly) across four coupling choices, including
one genuinely satisfying the inequality:
**(κ_g1,κ_line,κ_prod,κ_mixed)=(1, 0.1, 0, 1) gives transverse
eigenvalue +59.73 — a real, stable local minimum**, the first found in
this search. The other three tested points (violating the inequality)
all come back negative, exactly as predicted.

This gives two principled conditions on the five couplings — one
equality (degeneracy) and one inequality (stability) — both derived
directly from the Fano-invariant potential, neither fit to an external
target.

## Result 6 (follow-on) — a coexistence window: both vacuum types simultaneously stable

Result 4 found the S4 vacuum stable at one coupling choice and the V4
family's critical points all unstable there; a separate exploratory
coupling choice was later found where a genuine S2-type point (a≠b=c,
breaking S4 further than V4 alone) is stable but the S4 point is not.
This raises the natural question: can the *same* potential support
both simultaneously — one fully S4-symmetric vacuum (King–Luhn's
"top-Yukawa" type) and one only S2-symmetric (a natural home for a
distinct, second vacuum)?

Linearly interpolating both the five couplings and m² between the two
known points (A: κ=(1, 2/3, 0.1, 0, 1), m²=24.183; B: κ=(1.933, 0.890,
0.697, −0.055, 1.699), m²=4.368) and checking stability of both vacuum
types at each step finds a genuine **coexistence window at t≈0.12–0.13**
of the interpolation. Representative point (t=0.125):

```
κ_g1=1.117, κ_g2=0.695, κ_line=0.175, κ_prod=−0.007, κ_mixed=1.087, m²=21.71
```

At this point, **both** the S4 point (a=b=c≈0.872) **and** a genuine
S2 point (a≈1.849, b=c≈−0.308) are simultaneously stable local minima
of the same potential — confirmed directly (not merely inferred from
the interpolation) by computing the full Hessian at each and checking
all eigenvalues positive.

**This is a computational discovery, not a first-principles
derivation** — found by interpolating between two exploratory points,
not derived from a stated physical requirement (unlike Results 3 and
5). It demonstrates concretely that the Fano-invariant potential is
*capable* of supporting two structurally distinct simultaneous vacua —
consistent with what a genuine two-sector (charged-lepton/neutrino)
flavour model needs — but does not explain why this particular
coupling window does it, nor connect it to King–Luhn's own values. A
natural further question, not pursued here.

## Result 7 (2026-09-14) — the intertwiner found; the Fano vacuum matches Luhn-Nasri-Ramond's own formula exactly

The earlier attempt to find an explicit similarity transformation
between the Fano-plane sextet and Luhn-Nasri-Ramond's c_n-based
A^[6], B^[6] (arXiv:0709.1447, eqs. 29, 35) failed to converge. Two
things were checked and ruled out as the cause: (a) a transcription
error in B^[6] — re-verified letter-for-letter against the paper,
found to match the earlier code exactly (difference ~1e-16); (b) the
character match itself — re-verified across **all 168 group
elements** (not just the 6 class representatives), exact to machine
precision. The problem was the METHOD: solving for the intertwiner via
`null_space` on the 36×36 Kronecker-product system was numerically
fragile.

**The fix: standard representation-theoretic group-averaging.**
S = (1/|G|)Σ_g ρ_paper(g)·X·ρ_fano(g)⁻¹ for a single random matrix X,
summed over all 168 elements (each expressed as a consistent word in
one fixed generator pair, so both sides use the *same* abstract
elements). This is guaranteed nonzero when the characters match
exactly, which they do. Result: **S found, verified as a genuine
intertwiner on all 168 elements, residual 1.24×10⁻¹⁵.** All six
singular values of S are nonzero (S is invertible).

**Applying S to the Fano S4 vacuum reproduces their own formula
exactly.** Transformed (+4-on-line, −3-off-line) vacuum via S, and
compared to Luhn-Nasri-Ramond's own explicitly stated "singlet vev"
(√2, √2η, √2η³, b₇η⁴, b₇η⁵, b₇η²) (their §5, "Embeddings"). The two
agreed in magnitude everywhere (ratio std/mean ~10⁻¹⁵) but differed by
a per-component phase — tracked down to **exact integer multiples of
2π/7**, i.e. a diagonal twist by specific powers of η
(η⁰,η²,η⁶,η¹,η³,η⁴). This is a fully understood, characterized
relabelling (which primitive 7th root of unity is called "η"/which
order-7 element is called "AB"), not a discrepancy. Once corrected,
the two vectors agree to 1.45×10⁻¹⁵ relative precision.

**This closes the representation/vacuum half of the basis-matching
question.** Translating the six Fano-built quartic invariants through
this same S (and the diagonal correction) to check against King–Luhn's
actual κ₀..κ₅ labels in arXiv:0912.1344 — a different, later paper's
specific potential — is the natural next step, not attempted here.

## What remains open — stated plainly

1. **Matching the six Fano-built quartic invariants themselves to
   King–Luhn's own κ₀..κ₅ labels** in arXiv:0912.1344 (a different,
   later paper's specific potential) — the representation/vacuum-level
   basis match is now established rigorously (Result 7); extending
   this to the quartic invariants and checking κ₂=κ₃=κ₄+κ₅/√7 directly
   is the remaining step.
2. **Whether "doublet=triplet degeneracy" and the stability inequality
   above are King–Luhn's actual conditions** (vs., e.g., a flat
   direction, or a comparison against their second required vacuum) is
   not established.
3. **Why the Result 6 coexistence window sits where it does** is not
   explained — found by interpolation between two exploratory points,
   not derived.

## Files

- `fano_sextet_six_invariants.py` — Results 1–2, self-contained (numpy
  only). Runs end to end with assertions; fails loudly if wrong.
- `fano_vacuum_hessian_degeneracy.py` — Result 3, self-contained
  (numpy + sympy). Finds the S4 vacuum, confirms 1+2+3_1, derives
  3κ_g2=2κ_mixed.
- `fano_v4_family_critical_points.py` — Result 4, self-contained
  (numpy + scipy). Builds V4, confirms the 3-dim family, finds and
  checks the 12 critical points.
- `fano_stability_inequality.py` — Result 5, self-contained
  (numpy + sympy). Derives the stability inequality and confirms it
  numerically, including the one genuinely stable point found.
- `fano_coexistence_region.py` — Result 6, self-contained
  (numpy + scipy). Confirms points A and B, interpolates between them,
  and locates + directly verifies the coexistence window where both
  vacuum types are simultaneously stable.
- `fano_intertwiner_found.py` — Result 7, self-contained (numpy only).
  Finds the intertwiner S by group-averaging (robust, unlike the
  earlier null_space attempt), verifies it on all 168 elements, and
  confirms the Fano S4 vacuum matches Luhn-Nasri-Ramond's own stated
  formula exactly, up to a fully-characterized diagonal η-twist.
- `verify_fano_sextet.py`, `find_intertwiner.py`, `build_gl32_and_check.py`,
  `check_sym2.py` — earlier working scripts (including the two failed
  naive attempts — V⊕V* and Sym²(V), both reducible in characteristic
  2 — kept for the record, not because they succeeded).

---
END OF FINDING
