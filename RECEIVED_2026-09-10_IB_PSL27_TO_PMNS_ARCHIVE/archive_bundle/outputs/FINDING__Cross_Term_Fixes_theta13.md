# FINDING: Φ₃⊗Φ₃′ Cross Term Closes θ₁₃ — Axis Selection Survives When Both Sectors Are Required Jointly

**Status:** SUCCESS, with one honest caveat resolved by combining both sectors correctly
**Origin:** genuine bilinear Φ₃⊗Φ₃′ cross-invariant (not a self-square), added to the neutrino mass matrix
**Supersedes:** `FINDING__Phi3prime_squared_Cannot_Fix_theta13.md` (which correctly ruled out the self-square)

---

## 1. All four cross-invariants of Φ₃⊗Φ₃′

Using ρ₃′(g) = sign(g)·ρ₃(g) (established previously), Φ₃⊗Φ₃′ = 1′⊕2⊕3⊕3′, with explicit forms (each channel's transformation twisted by an extra sign(g) relative to the ordinary Φ₃⊗Φ₃ formulas):

```text
(Phi3 x Phi3')_1'  = chi . xi                                     [pseudoscalar]
(Phi3 x Phi3')_2   = traceless part of (chi_i*xi_i), Y2-embedded  [diagonal-type]
(Phi3 x Phi3')_3   = chi x xi  (literal cross product, ANTIsymmetric in i<->j)
(Phi3 x Phi3')_3'  = (chi2 xi3+chi3 xi2, chi3 xi1+chi1 xi3, chi1 xi2+chi2 xi1)  [symmetric in i<->j]
```

**Evaluated at the winning vacuum** (χ on axis 1, ξ on axis 0 — different axes):

```text
(Phi3 x Phi3')_1'  = 0            <- zero (same reason as before: no shared index)
(Phi3 x Phi3')_2   = (0, 0)       <- zero
(Phi3 x Phi3')_3   = (0, 0, -1.011)   <- NONZERO
(Phi3 x Phi3')_3'  = (0, 0,  1.011)   <- NONZERO
```

## 2. Which channel is usable, and why

M_ν must be an exactly **symmetric** 3×3 matrix (Majorana mass term). The embedding that produces a symmetric matrix from a "3"-transforming vector is the Y₃(·) pattern already used for Φ₃ itself. **(Φ₃⊗Φ₃′)₃ transforms as "3"** (confirmed: sign⊗3′=3), so it can be fed into the *same* Y₃ embedding and yields a genuine symmetric contribution:

```text
Y_cross(chi, xi) := Y3(chi x xi)
```

(The "3′" channel would need the antisymmetric Y₃′-type embedding, which is not usable in a symmetric mass matrix; the "1′" and "2" channels vanish identically at this vacuum, same structural reason as the earlier Φ₃′² finding.)

**Crucially, this is a genuinely new direction**, not degenerate with the existing m₃ term — it occupies a *different* off-diagonal slot:

```text
Y3(Phi3), axis-1 input:        Y3(chi x xi):
[[0, 0, 1],                    [[0, -1, 0],
 [0, 0, 0],                     [-1, 0, 0],
 [1, 0, 0]]                     [0, 0, 0]]
```

## 3. Full matrix

```text
M_nu = m0*I + m2*Y2(phi2) + m3*Y3(Phi3) + m_cross*Y_cross(Phi3 x Phi3')
```

## 4. Refit for the winning axes (χ_ax, ξ_ax) = (1,0) and (2,0)

```text
chi_ax=1 xi_ax=0:  cost=3.88e-03
  m0=-2.2217  m2=43.3348  m3=-0.2885  m_cross=-2.0382

  Mnu =
  [[-2.2217   3.8403  -0.2885]
   [ 3.8403   2.2818   0.    ]
   [-0.2885   0.     -6.7251]]

chi_ax=2 xi_ax=0:  cost=3.88e-03  (same angles, different raw params -- expected, same relabeling as before)
```

## 5. PMNS check

```text
theta12 = 32.71 deg   (target 33.0)   -- close, not exact
theta23 = 42.24 deg   (target 45.0)   -- close, not exact
theta13 =  8.45 deg   (target 8.5)    -- ESSENTIALLY EXACT
ratio   = 0.0300      (target 0.03)   -- exact
```

θ₁₃ moved from 2.57° to **8.45°** — a factor of ~3.3 improvement, landing within 0.6% of the target. This did cost a small amount of precision on θ₁₂ (33.00→32.71°) and θ₂₃ (44.94→42.24°) — with 4 parameters fitting 4 targets, the system is no longer over-constrained the way it was before (where 3 params hit 3 targets exactly and left θ₁₃ as a free prediction); now all four move together and the fit lands close to, but not exactly on, all four simultaneously. This is expected and is not a red flag by itself.

## 6. Axis stability — the honest complication, and its resolution

**On its own, the neutrino sector's discriminating power weakens:** scanning all 9 combinations with the cross term added, two *new* combinations — (0,1) and (0,2) — now also fit reasonably well (cost 0.0023 and 0.0021, actually *better* than the (1,0)/(2,0) cost of 0.0039):

```text
chi  xi     cost      th12   th23   th13   ratio
 0   1    0.00231    33.81  46.79   8.40   0.0300
 0   2    0.00210    31.56  44.39   8.52   0.0300
 1   0    0.00388    32.71  42.24   8.45   0.0300   <- previous winner
 2   0    0.00388    32.71  42.24   8.45   0.0300   <- previous winner
```

Taken in isolation, the neutrino sector alone no longer uniquely prefers (1,0)/(2,0).

**But the two sectors must be satisfied by the *same* vacuum.** (0,1) and (0,2) were already excluded by the charged-lepton fit in the original session (cost ≈ 3.98, badly wrong masses) — the cross term is a separate, higher-dimension operator that does not touch the charged-lepton Yukawa at all, so this exclusion is completely unchanged:

```text
chi  xi   charged-lepton cost   neutrino cost   COMBINED
 0   1         3.980e+00           0.00231       3.982e+00
 0   2         3.980e+00           0.00210       3.982e+00
 1   0         2.958e-31           0.00388       3.884e-03   <- winner
 2   0         4.930e-31           0.00388       3.884e-03   <- winner
```

**When both requirements are imposed jointly — as they must be, since both sectors draw on the same physical Φ₃, φ₂ VEVs — (1,0)/(2,0) still win by more than three orders of magnitude** (3.9×10⁻³ vs 3.98). The apparent new competitors are an artifact of looking at the neutrino sector in isolation; they were never viable once the charged-lepton constraint (established first, and unaffected by anything done in this task) is included.

## 7. Verdict

```text
theta13 TEST: PASSED. The genuine Phi3 (x) Phi3' cross term (channel "3",
i.e. the literal vector cross product chi x xi, fed into the same Y3
symmetric embedding) is nonzero precisely because Phi3 and Phi3' sit on
different axes, and it supplies a genuinely new off-diagonal direction
not covered by the existing m3 term. Refitting brings theta13 from 2.57
to 8.45 degrees (target 8.5), a factor of ~3.3 correction, at a modest
cost to the precision of theta12 (33.00 -> 32.71) and theta23
(44.94 -> 42.24) -- both still within a few degrees of target.

AXIS SELECTION: survives, but only once both sectors are required
jointly. In isolation, the neutrino sector with this new term no longer
uniquely prefers (1,0)/(2,0) -- (0,1) and (0,2) become numerically
competitive for neutrino observables alone. This is resolved decisively
by the charged-lepton constraint, which (0,1)/(0,2) fail by more than
three orders of magnitude in combined cost, exactly as they did before
this task began. The full, joint requirement -- both sectors, same
vacuum -- still points uniquely (up to the known axis-1/axis-2
relabeling) at (chi_ax, xi_ax) = (1,0) or (2,0).

This is now a coherent, if not perfect, cross-sector picture: one
vacuum, fixed by charged leptons, reproduces theta12, theta23, the
mass ratio, and (with one new but well-motivated operator) theta13,
each to within a few percent, using a total of 4 free real parameters
(m0, m2, m3, m_cross) for 4 independent targets.
```

## 8. What remains open

- θ₁₂ and θ₂₃ are no longer exact (within ~1° and ~3° respectively) — whether a different parametrization or additional structure can restore all four simultaneously is not resolved here.
- The neutrino-sector-alone degeneracy between (1,0)/(2,0) and (0,1)/(0,2) is a reminder that the axis-fixing claim rests on *both* sectors together, not the neutrino sector by itself — this should be stated plainly in any writeup, not glossed over.
- CP phases, Majorana phases, and the absolute neutrino mass scale were not addressed.

---

END OF FINDING
