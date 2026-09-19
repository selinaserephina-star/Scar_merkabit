# FINDING — χ₆ (King–Luhn sextet) = Fano-plane deleted permutation module; all six quartic invariants reproduced from Fano geometry alone (2026-09-14)

**Status:** twenty results (two corrections/retractions, seventeen
confirmed/derived, one substantial open finding), each independently
verified or symbolically derived — including a direct, from-scratch
confirmation of King-Luhn's entire Section 4 vacuum-alignment program,
a cross-verified correction + three completions contributed by Selina,
a full redo of the affected earlier results on the corrected potential,
resolution of every earlier open item, a from-scratch derivation of the
mass-hierarchy mechanism itself, an independently-built 28-bitangent
correspondence, three "forced uniqueness" checks from Ilya's own notes,
and — most recently — the discovery of a genuine, unresolved degeneracy
in the sextet-only potential (Result 20) that the earlier "why this
vacuum" question was, in hindsight, circling. Stated as honestly as
every correction before it: this is a real gap, not smoothed over.

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

**⚠ Corrected 2026-09-14 (Result 12) — see there.** The rank-6 claim
below is right (six *independent functions*), but one of the six
(`Iprod`) turns out to be degree 6 (sextic), not degree 4 — so this
does not, as originally claimed, identify a basis for King–Luhn's
6-dimensional space of *quartic* invariants. The corrected basis
(the other five quartics here + the genuine sixth quartic Q_miss) is
given in Result 12. Left as originally written below for the record.

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
| \|Σ_lines χᵢχⱼχₖ\|² | products over lines — **degree 6, see correction** |
| Σ_lines \|Σ_L\|²·(complement norm) | line vs. rest |
| Σ_{i<j} \|χᵢ\*χⱼ−χⱼ\*χᵢ\|² | antisymmetric pairs |

Verified numerically (10 random complex sample points, all six values
confirmed real to machine precision) that these are **linearly
independent — rank exactly 6**, matching King–Luhn's count exactly.
**This rank statement is correct but, per the correction above, does
not by itself establish a quartic-invariant basis** — see Result 12.

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

**⚠ RETRACTED 2026-09-14 (Result 15) — see there.** This result used
`κ_prod`, later confirmed sextic (Result 12), not a genuine quartic
coupling. A thorough search (210 sample points) on the corrected
4-term real quartic potential found **zero** cases of genuine
coexistence — the effect below does not survive and was most likely
an artifact of the invalid extra coupling. Left as originally written
below for the record.

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

## Result 8 (2026-09-14, session 2) — the orthogonal transform found; Θ,Θ' finally covariant

Applying Result 7's basis directly to King-Luhn's own Θ, Θ', Ω
formulas (arXiv:0912.1344, eqs. 4.2–4.4 — re-verified letter-for-letter
against a clean, direct PDF upload, ruling out an extraction error)
failed: Θ(A_real·χ) ≠ A_real·Θ(χ), by a large margin, not numerical
noise. Three lines of attack across two further sessions — index
reversal, block-diagonal rotation pairings for the order-7 element (15
pairings × 720 angle orderings, exhaustive), and a 2×2 "mixing matrix"
between Θ and Θ' — all failed to close the gap.

**The actual fix: numerical search over the full orthogonal group.**
Parametrizing O=exp(K) for skew-symmetric K (so the search is over
ℝ¹⁵=dim 𝔰𝔬(6), unconstrained) and minimizing
Σ_g Σ_χ‖Θ(gOχ)−gOΘ(χ)‖² by direct optimization (Powell's method)
converges to machine precision (cost ~3×10⁻¹⁷, from an initial
~3×10⁵). **Independently verified** on group elements and sample
points not used in the optimization: max residual 8.7×10⁻¹⁰. O is
confirmed genuinely orthogonal (OOᵀ=I) and proper (det=+1).

**Also fixed in passing:** the Fano→A_real step in Result 7 had taken
the real part of a complex intertwiner — valid only for the one
specific vacuum vector tested there, not in general (confirmed: the
transformed vacuum's imaginary part was exactly −6× its real part, a
coincidence of that specific vector, not a general property). Replaced
with a **direct, genuinely real** group-averaging intertwiner
Fano→A_real (real random seed, real output by construction),
independently verified equivariant to ~3×10⁻¹⁶. By Schur's lemma the
two constructions are necessarily proportional (the intertwiner space
for an irreducible real representation is 1-dimensional), so this
correction does not change any physical conclusion — it removes a
fragile step, not an error in the results already banked.

**Open end found this session, not yet resolved:** comparing the six
quartic invariants on *real* fields specifically reveals a **rank
asymmetry**. This correspondence's five (the sixth, antisymmetric,
vanishes identically on real fields): rank 4 — one linear relation.
King–Luhn's five I₁,I₂,I₃,I₄,I₆ (I₅ vanishes the same way): rank **3**
— two relations. A naive 6-parameter linear fit between the two sides
therefore cannot match well (~15% residual) — the correct comparison
is between their 3-dimensional real subspace and the corresponding
3-dimensional slice of this correspondence's 4-dimensional one, not a
same-size match. Not attempted here; a well-posed, concrete next step.

## Result 9 (2026-09-14, session 4) — the real cause found: wrong reference paper, not a typo; near-complete resolution

Three sessions (Results 7–8) searched for a rotation or a transcription
error to reconcile King–Luhn's Θ, Θ' (arXiv:0912.1344, eqs. 4.2–4.3)
with the basis built from Luhn-Nasri-Ramond's A^[6],B^[6]
(arXiv:0709.1447) via their S=VP transform. Every approach — index
reversal, exhaustive block-rotation pairings, 2×2 mixing matrices, a
full numerical SO(6) search, an exhaustive sign-flip search over
Θ'-terms — failed or landed on a mathematically real but ultimately
irrelevant structure (an eigenvalue of a connecting matrix equal to
exactly −b₇/b̄₇, a beautiful but, it turns out, beside-the-point
coincidence).

**The actual cause, found from the official arXiv LaTeX source of
0912.1344 (supplied by Selina/Ilya directly, sidestepping PDF
extraction entirely):** the text states explicitly "for χ given in the
real sextet basis of [King:2009mk]" — and **King:2009mk is King &
Luhn's own earlier paper, Nucl. Phys. B820 (2009) 269, arXiv:0905.1686,
not Luhn-Nasri-Ramond.** 0905.1686 builds its own explicit real sextet
generators 𝒮,𝒯,𝒰,𝒱 directly from the symmetric square of the triplet
representation (χᵢ~ψᵢψ'ᵢ etc., their eq. 4.1) — a genuinely different
construction, not related to the A,B/η-based one by any simple
rotation, which is exactly why three sessions of searching for one
found nothing.

**Rebuilding S,T,U,V explicitly from 0905.1686 eqs. 4.9–4.12 and
testing Θ,Θ' against them succeeds immediately and exactly** — no
search, no fix, nothing to correct. Both are covariant to machine
precision (≤1.8×10⁻¹⁴) across the full 168-element group. A fresh,
directly-verified intertwiner (Fano → this correct basis, equivariance
2.2×10⁻¹⁶) was built the same way as Result 7's.

**The payoff:** translating this correspondence's five real Fano
invariants through this intertwiner and comparing to King–Luhn's
I₁,I₂,I₃,I₄,I₆ gives a **perfect match — max fit error 7.8×10⁻¹⁶,
machine precision.** This is the first complete, successful
correspondence between the two invariant bases.

**Genuinely still open (at time of Result 9):** the complex/
antisymmetric piece (this correspondence's sixth invariant vs.
King–Luhn's I₅ — both vanish identically on real fields) does not show
fixed proportionality; the ratio varies across sample points
(std≈0.07 on a mean≈0.01), meaning I₅ most likely depends on a
*combination* of this correspondence's invariants, not a single one.
Resolved directly in Result 10, below, by sidestepping the translation
entirely.

## Result 10 (2026-09-14, session 4 continued) — κ₂=κ₃=κ₄+κ₅/√7 verified directly, independently

Rather than resolve the Result 9 I₅-translation gap, this checks
King–Luhn's central vacuum-alignment claim (§4.2.2, eqs. 4.24–4.26)
**directly against their own formulas** — since the claim is stated
entirely in terms of their own I₁..I₅, the Fano-side translation isn't
needed for this specific check.

**Method:** build f = (I₀+κ·I₁+κ'·(I₂+I₃+I₄)+κ''·(I₄−√7·I₅))/I₀ (their
eq. 4.24) from the now fully-verified Θ,Θ'; evaluate its 12-component
real gradient (∂/∂Re χᵢ, ∂/∂Im χᵢ) numerically at their stated χ_top
(eq. 2.10), for five different (κ,κ',κ'') choices spanning positive,
negative, and mixed signs.

**Result: the gradient vanishes at χ_top (≤1.9×10⁻⁸, floating-point
noise) for every (κ,κ',κ'') tested** — exactly matching King–Luhn's
claim that once their two relations (κ₂=κ₃=κ₄+κ₅/√7, built into this
I,I',I'' parametrization by construction) are imposed, χ_top is a
critical point for *any* values of the three remaining free couplings.
A smaller consistency check en route: I₁=0 and I₂=I₃ *exactly* at
χ_top (both structurally expected, neither assumed).

**This is a direct, from-scratch, independent confirmation of
King–Luhn's central result** — not a restatement, since Θ,Θ' were
re-derived and cross-checked against their own cited basis
(arXiv:0905.1686) rather than assumed correct. It does not (yet)
translate into this correspondence's own Fano-built κ-basis — Result
9's real-field match is exact and complete, but the I₅-translation gap
noted there remains open for that specific further purpose. For
directly verifying King–Luhn's own claim, as attempted here, it is not
needed.

## Result 11 (2026-09-14, session 4 continued) — χ_TB alignment also verified directly; both of King-Luhn's vacua now confirmed

Completes the direct verification by checking King-Luhn's OTHER stated
vacuum, χ_TB^[0]=(0,0,0,0,0,1) (their eq. 2.7, §4.2.1) — structurally
simpler than χ_top, since they claim first derivatives of *every*
individual Iₐ/I₀ vanish here, with no relations among the κ's needed.

**Gradient check:** confirmed directly — vanishes (≤2.8×10⁻⁸) for
arbitrary random (κ₁..κ₅), exactly as claimed.

**Both of their stated stability examples confirmed exactly:**
Example 1 (κ₁=5∈(−2,10), κ₂=1, rest 0) and Example 2
(κ₃=−0.03∈(−1/50,0), rest 0) each give a 12×12 real Hessian with
**exactly 2 zero eigenvalues** (the stated overall complex-scaling
freedom) **and 10 strictly positive** — genuine local minima in both
cases, matching their claims precisely.

**Full h₁..h₅ structural check, now exact:** revisited with the
correct 10-dimensional restriction (Re/Im of χ₁..χ₅, with χ₆ — the
scale direction — properly excluded, matching their own convention
exactly) rather than the full 12-real-dimensional space. All five
Hessian matrices match their stated h₁..h₅ (eqs. 4.12–4.16) to
finite-difference precision (max abs diff ≤2×10⁻⁵, i.e. exactly, not
merely in eigenvalue multiplicity) — resolving the earlier "labeling
difference" caveat completely. See `fano_chiTB_hessian_VERIFIED.py`.

**Together with Result 10, this completes an independent, from-scratch
confirmation of King–Luhn's entire Section 4 vacuum-alignment
program** — both χ_top and χ_TB, gradients and Hessians, using Θ,Θ',Ω
re-derived from their own cited source rather than assumed correct.

## Result 12 (2026-09-14, session 5) — a correction and three completions, from Selina, cross-verified independently

Selina (via her own Claude instance) sent a package identifying a real
error in Result 2 and completing three open threads. All four claims
independently cross-verified here using this correspondence's own,
separately-built infrastructure (the S_final intertwiner and the
Result-9 Θ,Θ' — not by re-running Selina's scripts as-is).

**1. Correction: Result 2's `Iprod` is sextic, not quartic.**
`Iprod = |Σ_lines χᵢχⱼχₖ|²` involves a degree-3 product inside a
modulus-squared — degree 6 overall. Confirmed directly by field
rescaling: χ→2χ gives ×16 for the other five (genuinely quartic) but
**×64** for `Iprod`. The five genuine quartics span only a
**5-dimensional** subspace of King–Luhn's 6-dimensional quartic space
— Result 2's "rank 6 matching King–Luhn's six quartics" conflated a
count of independent *functions* (correct) with a basis for the
quartic *space specifically* (not established, since one was the
wrong degree).

**2. The correct sixth quartic, Q_miss — confirmed to equal King–Luhn's I₅.**
The two independent PSL(2,7)-equivariant symmetric maps 6⊗6→6 have
concrete Fano meanings: the *pointwise square* sᵢ=χᵢ² and the
*line-collinearity map* ℓᵢ=Σ_{L∋i}χⱼχₖ. Their Hermitian pairing's
imaginary part, `Q_miss(χ)=Im Σᵢ conj(χᵢ²)·ℓᵢ`, is odd under
conjugation, lies exactly in the quartic space, and completes the five
genuine quartics to rank 6. **Cross-verified here directly:** pulling
Q_miss through this correspondence's own S_final intertwiner and
comparing to King–Luhn's I₅ (via the Result-9 Θ,Θ') gives an **exactly
constant ratio** (−0.472206, std/mean 2×10⁻¹⁴ across 15 samples) — not
merely correlated, genuinely proportional. Q_miss **is** King–Luhn's I₅.
(An internal check in Selina's own package had found only weak
correlation via a Hessian-eigenvalue comparison — resolved here: that
was an artifact of comparing unpaired eigenvalues from different
matrices, not a problem with the underlying identification, which the
direct point-by-point test above confirms cleanly.)

**3. √7 has a clean geometric origin.** The Fano sextet is the
sum-zero subspace of ℝ⁷ with the plain permutation metric; in the
one-point-deleted coordinate frame used throughout this
correspondence, that metric is I+𝟙𝟙ᵀ, with eigenvalues **{1×5, 7×1}**
— the eigenvalue-7 direction being the deleted point's own axis.
Confirmed directly: this correspondence's own S_final intertwiner
(built independently, by group-averaging, with no reference to this
explanation) has singular values in *exactly* the ratio √7:1
(0.724456 vs. 0.273819×5) — the same numbers as Result 9's
verification, now understood structurally rather than just observed.

**4. κ₂=κ₃=κ₄+κ₅/√7 is *necessary*, not just sufficient — strengthens
Result 10.** Result 10 showed these relations are sufficient (imposing
them, the gradient vanishes at χ_top for arbitrary remaining
couplings). Selina's method is stronger: build the 12×7 gradient
matrix (12 real directions × couplings on I₀..I₅ and the mass term) at
χ_top directly, with *no relations assumed*, and take its null space —
the full family of couplings for which χ_top is critical. Every
null-space basis vector satisfies both relations to ~10⁻¹² (rank 3,
null-space dimension 4, reproduced independently here). The relations
are *forced* by top-vacuum criticality, completing the logical picture
left open by Result 10's one-directional check.

**Bonus, not independently re-verified here:** Selina's package also
explains the Result 6 coexistence window as an exchange-of-stability
bifurcation (S4 minimum's doublet mode softening through zero at
t≈0.135 while the S2 minimum's hardens through zero at t≈0.115, the
window being their overlap), and shows it persists at κ_prod=0 (i.e.
survives the Iprod correction above, living entirely in genuine
quartic channels). Plausible and consistent with everything else
checked, but not run independently in this pass.

## Result 13 (2026-09-14, session 6) — Results 3 and 5 redone on the corrected real-quartic potential

Follow-on to Result 12's correction. Since `Iprod` is sextic, the
*real*-vacuum, *real*-perturbation stability analysis behind Results 3
and 5 needs redoing on the genuine quartic set. First checked whether
`Q_miss` (Result 12's correct sixth quartic) could simply replace
`Iprod`: **no** — Q_miss's Hessian, restricted to purely real
perturbations around the real S4 vacuum, is exactly zero (confirmed
directly). This makes sense: Q_miss is odd under conjugation, so it
can only affect stability against genuinely complex/phase
perturbations, not this real-direction analysis. So the corrected real
potential for this specific question has only **four** independent
terms: Ig1, Ig2, Iline, Imixed.

**Result 3 — confirmed unchanged.** Redone with only these four terms:
the doublet−triplet Hessian difference is 84κ_g2−56κ_mixed (κ_g1's
coefficient cancels to numerical precision), giving the *same*
3κ_g2=2κ_mixed. Reason: κ_prod's contribution was identical (−2240) in
both the doublet and triplet blocks in the original calculation, so it
cancelled out of the difference regardless of whether it's present —
Result 3 stands, now on the correct footing.

**Result 5 — structure changes, replaced with a verified condition.**
Imposing the degeneracy relation and fixing m² by radial criticality
(same method as before), the transverse structure is no longer a
single clean 5-fold eigenvalue (that relied specifically on κ_prod's
presence) — it splits into a genuine 5-fold eigenvalue
(446κ_g2−1616κ_line) plus two further directions. Their eigenvalues
involve a square root, but its argument is an **exact sum of two
squares** — (56κ_g1+55κ_g2+32κ_line)²+12(37κ_g2−120κ_line)² — confirmed
symbolically, guaranteeing real eigenvalues (as any genuine Hessian
must have) and giving a clean, well-defined stability condition even
though it's no longer a single linear inequality. **The same
illustrative point as the original Result 5** (κ_g1=1, κ_line=0.1,
κ_mixed=1, hence κ_g2=2/3) **remains genuinely stable** under this
corrected analysis (5-fold=135.7, smaller single=415.9, both positive)
— reassuring continuity despite the changed structure.

**Not yet redone:** Results 4 (the V4 family) and 6 (the coexistence
window) both use the full potential away from the S4 point specifically
(general a,b,c, not just the S4 line) and need their own separate
rework — not attempted in this pass.

## Result 14 (2026-09-14, session 6 continued) — Result 4 redone: qualitative conclusion survives, plus a new side observation

Follow-on to Result 13. First confirmed Q_miss vanishes identically not
just at the S4 vacuum but at *every* real point (a general consequence
of its chirality, not a coincidence of one vacuum) — so the 4-term
reduction (Ig1, Ig2, Iline, Imixed only) applies uniformly to any
real-vacuum question, including this one.

**Degeneracy-respecting regime (the physically relevant one, matching
Results 3/5's setup):** with κ_g1=1, κ_line=0.1, κ_mixed=1 (hence
κ_g2=2/3) and m² fixed by Result 13's correct radial-criticality
formula, an 80-point random search finds the S4 point **stable**
(min_eig=53.9, at a rescaled location t≈3.80 — the vacuum's overall
scale shifts once κ_prod is removed, as expected) and **every other
critical point found is a saddle**. This directly confirms original
Result 4's qualitative conclusion — only the S4 direction achieves
stability under natural conditions — now on the corrected potential.

**Side observation (a different, non-degenerate coupling regime,
κ=1 uniformly for all four terms — not the regime King–Luhn's own
analysis singles out):** finds 6 stable S2-type critical points (two
of the three line-values equal) among 21 found. This differs from the
original Result 4 (which reported all saddles at its own κ=1 choice,
which included κ_prod) — not a contradiction, since it's a genuinely
different coupling choice, but a new structural feature worth noting.
Not pursued further here.

## Result 15 (2026-09-14, session 6 continued) — Result 6 retracted: coexistence does not survive the correction

Follow-on to Result 14. Checked whether Result 6's coexistence window
survives on the corrected potential. **It does not.**

**Method:** at each sampled (κ_g1, κ_g2, κ_line, κ_mixed), fixed m² by
direct radial criticality at the S4 point, checked its stability, and
if stable, searched broadly for any S2-type critical point (two of
a,b,c equal, one different) and checked whether it was *also* stable
at the same couplings.

**A fine scan along the same kind of interpolation path used to
originally discover the window** (from a degeneracy-respecting point
with S4 stable, to a κ=1-uniform point with S2-type stable) shows a
clean **handoff, not an overlap**: S4 stability is lost around t≈0.08,
S2-type stability appears around t≈0.12 — a *gap* where neither is
stable, not a window where both are.

**A broad random search (150 additional points, spanning wider
coupling ranges)** found 13 points with S4 confirmed stable; **none**
showed a simultaneously-stable S2-type point. Combined with an earlier
60-point pass, **zero coexistence cases in 210 total samples**.

**Conclusion: unlike Results 3 and 4 (whose qualitative conclusions
survived the correction), Result 6's coexistence phenomenon does not
survive.** It was most likely an artifact of the incorrectly-included
sextic κ_prod term — being a genuinely different-degree coupling, it
could access curvature combinations the true quartic potential cannot.
This is reported as a considered negative result (a substantial,
targeted search, not a failure to look hard enough), not swept under
the rug. Result 6 is retracted as originally stated.

**What is unaffected:** this was always a self-contained exploratory
side-investigation into this correspondence's own toy potential, never
a King-Luhn claim — Results 1–2's Fano/King-Luhn correspondence and
Results 7–11's independent verification of King-Luhn's actual paper
stand entirely apart from this retraction.

## Result 16 (2026-09-14, session 6 continued) — the last open item resolved: degeneracy was our own choice, not King-Luhn's requirement

Follow-on to Result 15, closing open item 2 (whether "doublet=triplet
degeneracy" is King–Luhn's actual condition).

**First, a clean confirmation:** this correspondence's genuine 4-term
real quartic basis (Ig1, Ig2, Iline, Imixed — Iprod correctly excluded
per Result 12) matches King–Luhn's I₁,I₂,I₃,I₄,I₆ to machine precision
(1.9×10⁻¹⁵) — confirming Result 9's original perfect match was never
actually relying on the (invalid) Iprod term; it was redundant in that
fit all along.

**The decisive check:** King–Luhn's own χ_TB stability requirement,
using their own verified h₁..h₅ (Result 11), tested directly on their
own stated Example 1 (κ₁∈(−2,10), κ₂=1, rest 0, their eq. 4.25) across
the whole range. The ten eigenvalues stay **strictly positive
throughout** — confirming their stated stability claim — but are
**never all equal**. E.g. at κ₁=1: {56,56,56}, {72,72,72}, {100,100},
{140,140} — four distinct values, not two matching blocks.

**Conclusion:** King–Luhn's actual requirement for χ_TB is the weaker
condition "all ten eigenvalues positive" — achievable, as their own
examples show, across a wide coupling range with no equality
constraint at all. This correspondence's original 3κ_g2=2κ_mixed
(Results 3/5) was an additional, aesthetic choice made here — imposing
exact doublet=triplet degeneracy to get one clean, single stable-point
formula — not a requirement King–Luhn's own physics imposes. Both are
legitimate: theirs is the actual necessary-and-sufficient condition;
this correspondence's was a convenient special case within it, useful
for having one clean illustrative point rather than a full parameter
region, but never claimed as more than that in Results 3/5's own
"whether this matches their actual condition" caveat — now answered
plainly: it doesn't, and didn't need to.

## Result 17 (2026-09-14, session 7) — the "crater" mechanism: mass hierarchy origin, floor and walls, built from scratch

Follow-on to Results 10–11, prompted by a direct question: not "what
formula gives the right numbers" but "what is a mass, mechanistically,
and why does the hierarchy have exactly this shape." King–Luhn's
Yukawa texture ([[0,ε³,−ε³],[ε³,aε²,−aε²],[−ε³,−aε²,1]]) has a precise
structure — the suppression power depends on the *shallowest-forbidden*
generation index involved, not a symmetric pairwise distance: generation
3 sits at the "crater floor" (unsuppressed), generation 1 at the rim
(ε³), generation 2 partway (ε²). This session derived — not quoted —
*why*, using only explicitly-built PSL(2,7) matrices.

**The crater floor.** Built King–Luhn's explicit 3×3 matrix χ̂_top(eq.
2.4) from this correspondence's own χ_top (independently proven a
genuine critical point in Result 10). Result: **χ̂_top = diag(0,0,1)
exactly** — every one of the other eight entries vanishes to machine
precision (5×10⁻¹⁷). Generation 3 alone couples at leading order — a
computed consequence of the vacuum this correspondence proved, not an
assumption.

**The crater walls.** Built the octet representation S^[8],T^[8],
U^[8],V^[8] explicitly from King–Luhn's Appendix C and confirmed it
satisfies the full PSL(2,7) presentation (element orders 2,3,7,4,
exact). Using this:
- the symmetric octet built from χ_TB^[1],χ_TB^[2] reduces to
  **exactly** the single direction (0,0,0,1,0,0,0,0);
- the antisymmetric octet reduces to **exactly** (0,0,1,0,0,0,0,0);
- the anti-triplet's own octet (eq. C.7), contracted against the first
  direction, reproduces **exactly** the functional form of King–Luhn's
  stated Δ_Vs (eq. 4.3) — φ̄₁(φ̄₂+φ̄₃)+φ̄₂(φ̄₁+φ̄₃)+φ̄₃(φ̄₁+φ̄₂) — up to an
  overall constant (√6, absorbed into the coupling α_s, not a
  discrepancy).

**What this establishes:** the same kind of Hom_G-forcing mechanism
that fixes χ_top's diagonal structure (which components of a
Clebsch-Gordan contraction survive) is shown, by direct computation,
to *also* fix the anti-triplet potential's functional form — and hence
(via King–Luhn's own elementary sign-of-α argument, eq. 4.7, not
re-derived here) the φ̄∝(1,1,1) and φ̄∝(0,1,−1) alignments that generate
the ε²,ε³ suppressions. The hierarchy's *shape* is not assumed; it is
forced, at every step checked, by representation theory.

**What remains genuinely open** — *updated, both continuations closed in
this same session, and the alignment now proved UNIQUE, not merely
found*: the antisymmetric octet's antitriplet-side contraction (→Δ_Va)
was built explicitly and matches King–Luhn's stated form exactly (ratio
−√2, pure normalization) — the same structural mechanism as Δ_Vs. The
final alignment was then **proved algebraically unique**, not just
numerically located: 3|φ̄|²−|Σφ̄|² and 2|φ̄|²−|φ̄₂−φ̄₃|² were each shown to
equal a **manifest sum of real squares** — (x₁−x₂)²+(x₂−x₃)²+(x₃−x₁)²+
(same in y) for the first, 2|φ̄₁|²+(x₂+x₃)²+(y₂+y₃)² for the second —
proving each bound is saturated **only** at φ̄∝(1,1,1) and φ̄∝(0,1,−1)
respectively, exactly, with no other critical direction possible for
α₁,α₂<0. **The full chain is now a proof, not a numerical
demonstration**: crater floor, both crater-wall contractions, and the
uniqueness of the final vacuum directions are each either an exact
computed consequence of explicit PSL(2,7)/octet matrices, or an
algebraic sum-of-squares uniqueness proof. Only the deeper question
remains: *why* these specific χ_TB, χ_top directions (themselves unique
only up to the full PSL(2,7) orbit, per King–Luhn's own stated 168- and
7-fold degeneracies) are the ones nature — or the D-term potential's
own κ-couplings — picks in the first place. A speculative but concrete
connection to the 28-bitangent structure (session's discussion) is
flagged as a promising, unverified direction for future work.

## Result 18 (2026-09-14, session 8) — the 28-bitangent action built from scratch; a clean 7×4 correspondence found

Follow-on to Result 17's flagged open question: is the "2×χ6" seen in
the 28-bitangent permutation character (χ1+2χ6+χ7+χ8) the same
multiplicity space as King–Luhn's Θ,Θ' ambiguity in Sym²(χ6)? Pursued
by building the bitangent action **entirely from scratch** — not
re-running the TBR_BRIDGE script, but constructing V⊕V*=𝔽₂⁶ with its
symplectic form, verifying PSL(2,7) preserves it and the reference
hyperbolic quadratic refinement q₀ exactly, computing all 64 quadratic
refinements' Arf invariants directly (confirming the 36/28 split),
and verifying transitivity on the 28 odd ones (bitangents).

**Independent re-confirmation:** the resulting 28×28 permutation
character is exactly χ₁+2χ₆+χ₇+χ₈ — matching the TBR_BRIDGE claim, now
derived from the raw construction rather than cited.

**The 2×χ6 made explicit:** group-averaging (the same method as
Result 9's K1,K2) gives two equivariant maps χ6→ℂ²⁸, rank exactly 2,
equivariance to machine precision (4.4×10⁻¹⁶).

**A clean, unexpected structural bonus — the 7×4 correspondence:** a
single bitangent's stabilizer has order 6, class structure [1,2,2,2,
3,3] (an S3), and is found to sit **entirely inside** the S4 stabilizer
of one specific Fano point. Checking all 28 bitangents: **every one**
has its stabilizer contained in exactly one Fano-point's S4, with
**exactly 4 bitangents per point** (7×4=28, confirmed by direct
enumeration). This is expected once seen (S4 has exactly four
conjugate S3 point-stabilizers in its own natural 4-point action) —
not a new mystery number — but it gives a clean, verified, geometric
correspondence between the two structures this correspondence has
worked with all session: each Fano point (each χ_TB-orbit
representative) ↔ a specific quartet of bitangents.

**What remains open, honestly:** whether the 2-dimensional "which copy
of χ6" freedom inside the bitangent module is *canonically identified*
with Θ,Θ'-freedom inside Sym²(χ6) — and whether such an identification
(if it exists) would explain *why* nature picks the specific χ_top,
χ_TB directions among their PSL(2,7) orbits — was not established here.
The 7×4 correspondence is a concrete, promising structural fact to
build on, not a resolution of the deeper question.

**Follow-up, same session — this specific avenue explored and closed
negatively.** Checked directly whether Sym²(χ6) embeds naturally into
ℂ²⁸ (it does: 21+7=28, dim Hom_G(Sym²χ6,ℂ²⁸)=6 exactly matching
multiplicities, confirmed by direct group-averaging). Built the proper
metric-corrected Hermitian adjoint (via the genuinely G-invariant
inner products on both χ6 and Sym²χ6, obtained by group-averaging
M†M — the naive Hermitian adjoint fails, since neither representation
is unitary in its raw coordinate basis) relating K1,K2 (Sym²χ6→χ6) to
a canonical J1,J2 (χ6→Sym²χ6), then pushed these through the Sym²χ6→
ℂ²⁸ embedding and compared to L1,L2 directly. **Result: the resulting
2×2 mixing matrix C is not unitary (C†C≠scalar·I) — no distinguishing
structure emerges.** Pure representation theory (multiplicity,
invariant Hermitian metric) does not, by itself, pick out a canonical
identification between King–Luhn's Θ,Θ' freedom and the bitangent
module's own 2×χ6 freedom. The "2" appearing in both places remains a
genuine structural coincidence (Sym²χ6 does embed in the 28-dim
bitangent module) without yet explaining King–Luhn's specific choice.
This closes this particular avenue — not with a proof of impossibility,
but as a considered negative result, so the same path isn't
re-explored without a genuinely new idea (e.g. bringing in the Arf
invariant's own quadratic structure directly, which was not attempted).

**Cross-checked from four independent angles (same session), no error
found in the 7×4 correspondence itself:** (1) an entirely different
construction — find any order-6 subgroup H of PSL(2,7) directly (no
symplectic form, no quadratic refinements, no Arf invariant anywhere),
build G/H's 28 cosets, act by left multiplication — gives the
*identical* character (28,4,1,0,0,0) and the same χ1+2χ6+χ7+χ8
decomposition; (2) the Arf invariant of q₀ confirmed independently by
direct zero-counting (36/64 zeros, matching the standard Arf=0 formula
2²·9=36, not the Arf=1 formula 2²·7=28); (3) exhaustive enumeration of
*all* order-6 subgroups of PSL(2,7) — exactly 28 found, all contained
in some Fano-point's S4, exactly 4 per point, confirmed without
reference to bitangents or quadratic forms at all; (4) the underlying
textbook fact re-confirmed in isolation — abstract S4 (permutations of
4 letters, no PSL(2,7) involved) has exactly 4 distinct order-6
point-stabilizers. All four agree exactly with the original
construction; the 7×4=28 correspondence is a robust finding, not an
artifact of one specific construction choice.

## Result 19 (2026-09-14, session 8 continued) — three "forced uniqueness" checks from Ilya's own notes

Prompted by Ilya's own review notes (not Selina's) identifying the
"forced uniqueness" pattern running through this whole correspondence
(Hom_G-forcing / sum-of-squares saturation / structural survival of
specific Clebsch-Gordan components) and proposing six concrete places
it might extend further. Checked the three cheapest, per the notes'
own prioritization.

**√7's metric uniqueness (positive).** dim Hom_G(Sym²χ₆, trivial) = 1
exactly (direct character computation). Since the χ6-invariant metric
is therefore unique up to scale, the specific I+𝟙𝟙ᵀ structure (and
hence the √7 eigenvalue ratio, Result 12) is not merely *derived* —
it is the *only* possible invariant metric, making √7 unavoidable
rather than a computed coincidence.

**Result 17's functional uniqueness (positive).** dim Hom_G(Sym²χ₈,
trivial) = 1 exactly, by the same direct computation. The octet
contraction that produces Δ_Vs and Δ_Va (Result 17) is therefore the
*only* possible G-invariant pairing of this type — not one choice
among several that happened to work.

**The Q_miss/I5 constant −0.472206 (nuanced, partially negative).**
Checked whether this specific constant (Result 12) is itself forced,
as the notes suggested testing. Found: rescaling the S_final
intertwiner by a factor λ scales the constant by exactly λ⁴ (checked
directly: λ=2 gives −7.555, λ=0.5 gives −0.0295 — exact λ⁴ scaling,
since Θ,Θ' are themselves quadratic in χ, making I5 quartic, not
quadratic). **The proportionality is forced (confirmed to machine
precision, Result 12); the specific numerical constant is not** — it
depends on S_final's normalization, which Schur's lemma leaves free
(the metric-uniqueness result above fixes only the *ratio* 1:7 of
eigenvalues, not the intertwiner's overall scale). This constant
remains a convention, not a theorem — an honest, useful clarification
of what "forced uniqueness" does and does not reach in this specific
case.

**Not yet attempted:** the notes' highest-value, highest-difficulty
item — testing dim Hom_G(28-bitangent module, χ_top-orbit) to see
whether it could force a *specific point* within χ_top's 168-fold
orbit, which would close this correspondence's one remaining
substantial open question (Result 17/18's "why this vacuum, not just
that it's stable"). Flagged for a future session, not pursued here.

## Result 20 (2026-09-14, session 8 continued) — a substantial, unexpected gap: the potential alone does not select chi_top's texture

Follow-on to Result 19's flagged item 1. Started from a conceptual
clarification: "which point within χ_top's regular (trivial-
stabilizer) orbit" is a category error — no G-invariant structure can
distinguish points a symmetry permutes transitively (basic fact about
spontaneous symmetry breaking, verified directly: no additional
structure, bitangent-derived or otherwise, can break a regular orbit's
symmetry). Reformulated as: is χ_top's *orbit* uniquely selected as the
minimizing critical value of the I₀..I₅-built potential — this turned
into a substantial, previously unflagged finding.

**χ_top is not even a minimum for generic couplings.** At a generic
small (κ,κ')=(0.02,0.03), κ''=−0.01: f(χ_top)=1.233, but the genuine
global minimum (constrained search, unit sphere) is 1.076 — a
different, non-χ_top point entirely. χ_top is special only at the
exact κ=κ'=0 locus King–Luhn use for their illustrative example.

**At κ=κ'=0 exactly, χ_top shares its critical value with a whole
family of physically inequivalent vacua.** Ten independent random-start
searches (κ''=−0.01, well inside King–Luhn's own stated stable range)
all converge to genuine critical points (|gradient|<5×10⁻⁸) sharing
χ_top's *exact* value (0.53333...). Their invariants I₁..I₅ match
χ_top's to ~10⁻⁹, and their Hessian eigenvalue *spectrum* matches
χ_top's exactly (same 10 nonzero numbers, same multiplicities) — yet
the actual physical Yukawa texture χ̂ (King–Luhn's eq. 2.4, Result 17's
formula) is **completely different**: χ_top gives the clean diag(0,0,1)
(crater floor), the found points give generic, fully-populated
matrices with **no mass hierarchy at all**. A "(3,3)-dominance" measure
ranges continuously from 0.000 to 0.432 across ten found points, all
exactly energy-degenerate with χ_top.

**Implication, stated carefully.** King–Luhn's own construction —
extremizing f built purely from I₀..I₅ — does not, by itself, single
out χ_top's hierarchical texture over these hierarchy-free
alternatives: they are exactly degenerate in the potential these six
invariants define. Something beyond I₀..I₅-extremization is needed to
select χ_top specifically. **This is a genuine, substantial gap, not
resolved here** — reported for further scrutiny, not smoothed over.

**Important caveat, stated as plainly as the finding itself:** this
uses only the six invariants and the (κ,κ',κ'')-parametrization from
Results 10/16 — the sextet-only D-term potential as reconstructed and
verified in this correspondence. King–Luhn's complete physical model
may contain additional structure (constraints from the anti-triplet
sector, higher-order terms, or an explicit vacuum-selection input) not
captured here that could lift this degeneracy. This finding concerns
what this correspondence has actually built and verified, not
necessarily a flaw in King–Luhn's full published physics.

## What remains open — stated plainly

Most items originally listed here were resolved (Results 12, 15, 16).
One substantial new open item emerged in Result 20. Kept for the record:

1. ~~Translating King–Luhn's I₅ into this correspondence's own
   Fano-built invariant basis~~ — **resolved in Result 12**: Q_miss
   (the corrected sixth quartic) is exactly proportional to I₅.
2. ~~Whether "doublet=triplet degeneracy" and the stability inequality
   are King–Luhn's actual conditions~~ — **resolved in Result 16**:
   they are not; King–Luhn's actual requirement is the weaker "all
   eigenvalues positive," achievable across a wide coupling range with
   no equality constraint. This correspondence's degeneracy condition
   was an additional, aesthetic choice made here.
3. ~~Why the Result 6 coexistence window sits where it does~~ — **moot
   after Result 15**: the window itself was retracted (did not survive
   the Iprod correction).
4. ~~Result 6 has not yet been redone on the corrected quartic
   potential~~ — **done in Result 15: retracted**.
5. **Result 20's degenerate-vacuum-family finding is unresolved and is
   currently the single most substantial open item.** Whether King–
   Luhn's full physical model (beyond the sextet-only I₀..I₅ potential
   reconstructed and verified in this correspondence) contains
   additional structure that lifts this degeneracy — selecting χ_top's
   hierarchical texture over the found hierarchy-free, energy-
   degenerate alternatives — is a genuinely open question.

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
- `fano_orthogonal_transform_found.py` — Result 8, self-contained
  (numpy + scipy). Finds O by direct optimization over SO(6),
  independently verifies it, fixes the Result-7 real-intertwiner step
  properly, and confirms (with assertions) the rank-4-vs-3 finding
  that motivates the next step.
- `fano_correct_STUV_basis_found.py` — Result 9, self-contained
  (numpy only). Builds King-Luhn's own S,T,U,V (arXiv:0905.1686),
  confirms Θ,Θ' covariance on all 168 elements, builds the correct
  intertwiner, and confirms (with an assertion) the perfect real-field
  invariant match.
- `fano_kappa_relation_VERIFIED.py` — Result 10, self-contained
  (numpy only). Directly, independently verifies King-Luhn's central
  vacuum-alignment claim (κ₂=κ₃=κ₄+κ₅/√7) by checking the gradient of
  their own potential f vanishes at their own stated χ_top, for
  several different coupling choices (all via assertions).
- `fano_chiTB_alignment_VERIFIED.py` — Result 11, self-contained
  (numpy only). Directly verifies the χ_TB alignment: gradient
  vanishing for arbitrary couplings, and both of King-Luhn's stated
  stability examples via full 12×12 Hessian eigenvalue checks (all
  via assertions).
- `fano_chiTB_hessian_VERIFIED.py` — Result 11 follow-up, self-contained
  (numpy only). The precise version of the h₁..h₅ structural check:
  correctly restricts to their own 10-dimensional (non-scaling)
  convention and confirms all five Hessians match their eqs. 4.12–4.16
  exactly (not just in eigenvalue multiplicity), resolving the
  "labeling difference" caveat from the first pass.
- `fano_quartic_correction_CROSSVERIFIED.py` — Result 12, self-contained
  (numpy only). Independently cross-verifies Selina's correction
  (Iprod is sextic) and three completions (Q_miss=I₅ exactly, the √7
  singular-value geometry, and the degree-check itself), all via
  assertions, using this correspondence's own infrastructure rather
  than re-running her scripts.
- `fano_result5_CORRECTED.py` — Result 13, self-contained (numpy +
  sympy). Redoes Results 3 and 5 on the corrected 4-term real quartic
  potential: confirms Q_miss's real-direction Hessian is exactly zero,
  re-derives Result 3's degeneracy condition unchanged, and replaces
  Result 5 with a verified sum-of-squares-based stability condition
  (same illustrative point remains stable).
- `fano_result4_CORRECTED.py` — Result 14, self-contained (numpy +
  scipy). Confirms Q_miss vanishes at general real points (not just
  the S4 vacuum), then redoes Result 4's critical-point search on the
  corrected potential in both the degeneracy-respecting regime
  (S4 stable, others saddles — original conclusion confirmed) and a
  side-note non-degenerate regime (new stable S2-type points found).
- `fano_result6_CORRECTED.py` — Result 15, self-contained (numpy +
  scipy). Searches 210 coupling points on the corrected potential for
  the Result 6 coexistence window; finds none — a fine interpolation
  scan shows a clean S4→S2 handoff with a stability gap in between,
  not an overlap. Result 6 retracted as originally stated.
- `fano_degeneracy_question_RESOLVED.py` — Result 16, self-contained
  (numpy only). Closes the last open item: confirms the genuine
  4-quartic basis still matches King-Luhn's I1,I2,I3,I4,I6 exactly,
  then shows directly (via King-Luhn's own verified h1,h2 and their
  own stated Example 1) that their actual chi_TB stability requirement
  is "all eigenvalues positive," never "doublet=triplet degenerate."
- `fano_crater_mechanism_VERIFIED.py` — Result 17, self-contained
  (numpy + sympy). Derives the mass-hierarchy mechanism from scratch:
  chi_hat_top=diag(0,0,1) exactly (the "crater floor"), then builds
  the full octet representation from Appendix C and confirms it
  structurally forces the anti-triplet potential's functional form
  (the "crater walls") — all via assertions, nothing quoted unchecked.
  Also proves the final vacuum alignments are algebraically UNIQUE
  (manifest sum-of-squares), not merely numerically located.
- `fano_bitangent_correspondence_EXPLORED.py` — Result 18, self-contained
  (numpy only). Builds the 28-bitangent action from scratch (symplectic
  form, quadratic refinements, Arf invariant), independently
  re-confirms chi1+2chi6+chi7+chi8, extracts the two chi6 copies
  explicitly, and finds a clean 7x4 Fano-point/bitangent correspondence
  — flagged honestly as a promising structural fact, not (yet) a
  resolution of why nature picks the specific chi_top/chi_TB vacua.
- `fano_forced_uniqueness_checks.py` — Result 19, self-contained
  (numpy only). Three checks from Ilya's own notes: dim Hom_G(Sym^2
  chi6/chi8, trivial)=1 (both positive — metric uniqueness forces
  sqrt(7) and Result 17's functional), and a check on whether the
  Q_miss/I5 constant itself is forced (nuanced: proportionality is,
  the specific number isn't — it's an S_final normalization artifact).
- `fano_bitangent_crosscheck_INDEPENDENT.py` — Result 18 cross-check,
  self-contained (numpy only). Verifies the 7x4 correspondence from
  four genuinely independent angles (a from-scratch G/H coset
  construction with no symplectic form at all; independent Arf-invariant
  zero-counting; exhaustive order-6-subgroup enumeration; the abstract
  S4 fact in isolation) — all agree exactly, no error found.
- `fano_degenerate_vacuum_family_DISCOVERED.py` — Result 20,
  self-contained (numpy + scipy). Finds, reproducibly across ten
  random seeds, a family of genuine critical points sharing chi_top's
  exact value and Hessian spectrum at King-Luhn's own stated simplest
  coupling regime, but with completely different (hierarchy-free)
  Yukawa textures — a substantial, honestly-flagged gap in what the
  six-invariant potential alone determines.
- `verify_fano_sextet.py`, `find_intertwiner.py`, `build_gl32_and_check.py`,
  `check_sym2.py` — earlier working scripts (including the two failed
  naive attempts — V⊕V* and Sym²(V), both reducible in characteristic
  2 — kept for the record, not because they succeeded).

---
END OF FINDING
