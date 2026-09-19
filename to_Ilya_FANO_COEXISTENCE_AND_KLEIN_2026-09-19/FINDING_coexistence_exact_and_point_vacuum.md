# FINDING — the S4/S2 coexistence window survives the sextic correction (exact 6-dim Hessians), and the "S2" vacuum is the Fano point-S4 vacuum

**Stenberg side (with Claude), 2026-09-19. Free exploration, not a sealed
stone. Mathematics of a toy potential on the Fano sextet; King–Luhn physics
parked (Rule 3).** Script: `_explore_fano_coexistence_exact_2026-09-19.py`.

## 0. The disagreement

- Our envelope of 2026-09-14 (§4 of `FINDING_fano_quartic_correction.md`):
  along the original A→B interpolation the coexistence window is an exchange
  of stability with edges at the two eigenvalue zero-crossings, and it
  **persists at κ_prod = 0** (pure quartic in the five real invariants).
- IB's Result 15 (2026-09-14, session 6): on the corrected 4-term potential
  {I_g1, I_g2, I_line, I_mixed}, "zero coexistence in 210 samples"; along
  "the interpolation path" a handoff with a gap (S4 lost at t≈0.08, S2-type
  appears at t≈0.12). Result 6 retracted.

Both scripts (`_explore_fano_coexistence_why_2026-09-14.py`,
`fano_result6_CORRECTED.py`) use the same seven lines, the same
`build_phi(a,b,c)` V4-slice, the same four/five invariants, the same 7×7
finite-difference Hessian and comparable tolerances. The difference is
**where they look**:

| | our path | his path |
|---|---|---|
| A | κ=(1, ⅔, 0.1, [0], 1), m² by S4 criticality | κ=(1, ⅔, 0.1, 1) |
| B | κ=(1.933, 0.890, 0.697, [−0.055], 1.699), m²=4.368 | κ=(1, 1, 1, 1) |
| m² | interpolated (Q1) / refixed at scale 1 (Q2, Q2b) | refixed by S4 radial criticality |
| random search | none | 150 points in k1∈(0.2,3), k2∈(−1,3), kline∈(−1,2), kmixed∈(0.2,3) |

His path A′B′ is a different line through coupling space; his box contains
our point but 150 samples in four dimensions do not resolve a region of
width ≈0.014 in t.

## 1. The exact check

Differences from both sides' scripts: the Hessian is **symbolic** (sympy),
evaluated at critical points refined to 30 digits (mpmath), and **restricted
to the 6-dimensional sum-zero sextet** through an explicit orthonormal basis
Q₆ (7×6, Q₆ᵀ𝟙 = 0), so the all-ones direction of ℝ⁷ — present in both FD
Hessians, harmless here (its eigenvalue is +25…+33) — is excluded and
reported separately. Criticality is taken in the slice, exactly as both
scripts do (a gradient proportional to 𝟙 is allowed, and the slice is the
V4-fixed subspace, so slice-critical ⇒ sextet-critical by symmetric
criticality).

**(a) The original Result-6 point** (t = 0.125, κ_prod = −0.006875 kept, m²
interpolated = 21.70642):

```
line-S4   a=b=c=0.872109143246      eigs {0.2012 x2, 0.3223 x3, 86.65}   strict minimum   V=-43.30808
second    a=1.84898464208 b=c=-0.308164107014   eigs {0.1349 x2, 0.2645 x3, 86.82}   strict minimum   V=-43.28782
```

**(b) Our claim: same κ with κ_prod := 0, m² refixed so the S4 point is
critical at scale 1** (m² = 28.5966979):

```
line-S4   a=b=c=1                    eigs {0.10442 x2, 0.26367 x3, 114.39}   strict minimum   V=-75.06633
second    a=2.12221068467 b=c=-0.353701780779   eigs {0.19368 x2, 0.33250 x3, 114.39}   strict minimum   V=-75.12936
```

|∇V| ≤ 3×10⁻²⁹ at all four points.

**(c) Homogeneity control**: (b) rescaled to m² = 21.70642 — same verdict
(min eigenvalues 0.0793 / 0.1470), as it must be for a quartic-plus-mass
potential.

**(d) Scan along A→B with κ_prod ≡ 0, m² refixed, exact 6-dim Hessians:**

```
   t    S4 min eig   2nd min eig
 0.110    0.5399      -0.1090
 0.115    0.3947      -0.0086
 0.120    0.2496       0.0923   <== BOTH
 0.125    0.1044       0.1937   <== BOTH
 0.130   -0.0407       0.2955
```

Window **t ∈ [0.1155, 0.129]**. Left edge: the second vacuum's doublet mode
hardens through zero; right edge: the line-S4 doublet softens through zero —
the exchange of stability of our envelope, now with exact eigenvalues.

**Verdict.** Coexistence of two structurally distinct stable vacua is a
genuine feature of the real quartic potential in {I_g1, I_g2, I_line,
I_mixed}; it does not need the sextic. Result 15's negative is a sampling
miss; Result 6 should be reinstated (with the corrected potential and the
point below), or restated as "gap on A′B′, overlap on AB".

## 2. The second vacuum is the point-S4 vacuum

At every coexistence point found, the "S2-type" vacuum (a, b, b) satisfies

```
d = -(a+2b)/4 = b      and      a / b = -6        (both to 1e-12)
```

i.e. φ = s·(6, −1, −1, −1, −1, −1, −1): **+6 on one Fano point, −1 on the
other six** — the unique (up to scale) vector fixed by the **point-stabilizer
S4** of PSL(2,7), just as the line vacuum (4,4,4,−3,−3,−3,−3) is the unique
vector fixed by the line-stabilizer S4. In the V4-slice coordinates the point
vacuum of the line's point 0 happens to look like an S2 point (a ≠ b = c),
which is why both searches labelled it so.

Consequences, all elementary:

- χ₆ restricted to either S4 class is 1 ⊕ 2 ⊕ 3 (the two classes are swapped
  by the outer automorphism of PSL(2,7), which is Fano duality, and χ₆ is
  self-dual), so the Hessian at **both** vacua splits as 2 + 3 + 1 — exactly
  the pattern in §1 — and Schur's lemma gives one scalar per block at both.
- The potential is **not** duality-invariant (I_line sums over lines, not
  points), so the two vacua have different energies (−75.066 vs −75.129 in
  (b)); which is lower depends on the couplings, and the window is where both
  are locally stable.
- IB's Result 14 "6 stable S2-type critical points among 21" at κ = 1 uniform
  and his Result 15 handoff on A′B′ read as **line-S4 ↔ point-S4**: along
  A′B′ stability passes from one S4 class to the other with a gap; along AB
  the two overlap.
- Each S4 class has a 7-fold degenerate real vacuum orbit (7 lines / 7
  points). King–Luhn's χ_TB has a 7-fold degeneracy and an S4 stabilizer
  (Result 11's 3+3+2+2 Hessian multiplicities); which of the two Fano S4
  classes it is, is a one-line check through the intertwiner — **not done
  here, and parked** (physics).

## 3. What is and is not claimed

- Claimed [C]: (a)–(d) above, exact to the precision stated, script enclosed.
- Claimed [P]: §2's identification and the 2+3+1 pattern (character theory of
  the two S4 classes).
- Not claimed: anything about King–Luhn's model; the window's location is a
  property of this toy potential's coupling path, not of nature.
- Refutation at equal prominence: our 2026-09-14 envelope's numbers were
  finite-difference on ℝ⁷ with a lenient tolerance; they were right, but the
  exact check is what makes the statement safe. IB's Result 15 was a
  considered, substantial search; it missed a thin region. Both scripts are
  unchanged and enclosed by reference.
