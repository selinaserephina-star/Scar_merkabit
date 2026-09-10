# FINDING: Φ₃′² Cannot Fix θ₁₃ — Structural Obstruction, Not a Fitting Failure

**Status:** NEGATIVE RESULT, with a concrete alternative identified
**Origin:** direct test of the Φ₃′² addition proposed to close the θ₁₃ gap in the neutrino sector
**Subject:** whether adding Φ₃′⊗Φ₃′ (symmetric part) to M_ν can bring θ₁₃ from 2.57° to 8.5° without disturbing θ₁₂, θ₂₃, the mass ratio, or the axis selection

---

## 1. Y₃′² as literally specified (channel "3" of Sym²(3′)) — identically zero

```text
(Phi3' Phi3')_3 = sqrt(2) * (xi2*xi3, xi3*xi1, xi1*xi2)
```

Each component is a product of **two different** components of ξ. The winning
vacuum has Φ₃′ aligned on a single axis (established in the charged-lepton
fit: ξ = ε·c₃′·(axis)), i.e. exactly one component of ξ is nonzero. Any
product of two *different* components of a one-component vector is zero —
this holds for **all three axis choices**, verified explicitly:

```text
xi = (0.113, 0, 0)  ->  (Phi3'Phi3')_3 = (0, 0, 0)
xi = (0, 0.113, 0)  ->  (Phi3'Phi3')_3 = (0, 0, 0)
xi = (0, 0, 0.113)  ->  (Phi3'Phi3')_3 = (0, 0, 0)
```

**m₃′² · Y₃′²(Φ₃′²), as specified, is identically zero at this vacuum, for any value of the coefficient m₃′².** This is an algebraic identity, not a numerical near-miss — no amount of retuning can make this term contribute anything.

## 2. Natural fallback: channel "2" of Sym²(3′) — nonzero, but degenerate with the existing m₂ term

The full branching is Sym²(3′) = 1⊕2⊕3; channel "2" (unlike channel "3") does **not** vanish for an axis-aligned ξ, since it's built from (ξ₁²,ξ₂²,ξ₃²) directly rather than cross-products:

```text
xi_axis=0: (Phi3'Phi3')_2 = (4.26e-3, 0)      -- nonzero
xi_axis=1: (Phi3'Phi3')_2 = (-2.13e-3, 3.69e-3) -- nonzero
xi_axis=2: (Phi3'Phi3')_2 = (-2.13e-3,-3.69e-3) -- nonzero
```

**Full matrix with this term added:**

```text
M_nu = m0*I + m2*Y2(phi2) + m3*Y3(Phi3) + m3'2*Y2((Phi3'Phi3')_2)
```

**Refit result for both winning axes (4 free parameters now: m0, m2, m3, m3'2):**

```text
chi_ax=1 xi_ax=0: cost=4.868e-01
  m0=-3.93   m2=-37.06   m3=-6.77   m3'2=908.09
  th12=33.000 (target 33.0)   th23=44.944 (target 45.0)
  th13=2.569  (target 8.5)    ratio=0.0300 (target 0.03)

chi_ax=2 xi_ax=0: cost=4.868e-01  [same angles, wildly different raw params]
  m0=-3802.27  m2=126.26  m3=0.35  m3'2=1058.03
  th12=33.000  th23=44.944  th13=2.569  ratio=0.0300
```

**θ₁₃ did not move at all** (2.569° vs 2.57° before, within fit noise) — despite going from 3 to 4 free parameters. The wildly different raw (m0,m2,m3,m3'2) values between the two axis choices, while producing *identical* angles, is itself the tell: **the new term is degenerate with the existing structure.**

**Why:** channel "2" of Φ₃′² only supplies a *diagonal* contribution — Y₂(a,b) for some (a,b). The existing φ₂ term, m₂·Y₂(φ₂), already supplies one full diagonal direction. Adding a second diagonal source just re-parametrizes the same 2-dimensional diagonal subspace with two numbers instead of one; it opens no new direction in the 6-dimensional space of symmetric 3×3 matrices. θ₁₃ is controlled by *off-diagonal* structure, which this term cannot touch.

## 3. Does either version disturb the axis selection?

No — because neither version changes anything. The channel-3 term is exactly zero everywhere (all 9 combinations, not just the winners), and the channel-2 term is degenerate with m₂ everywhere. The 9-combination ranking from the previous session is completely unchanged; (1,0) and (2,0) remain the unique winners on θ₁₂ and θ₂₃, and θ₁₃ = 2.57° for both, same as before, for the same reason it didn't move for the winners: the term simply doesn't reach the part of the matrix that matters.

## 4. What would actually work

Φ₃′² (in either available channel) is structurally incapable of fixing θ₁₃, because a *self*-quadratic invariant of a single-axis vector can only ever reconstruct diagonal-type structure (verified: channel 3, the only off-diagonal-capable channel, vanishes identically). What is needed is genuine **off-diagonal** structure connecting positions that Φ₃ alone (also single-axis) doesn't reach.

The natural candidate is a **Φ₃⊗Φ₃′ cross term** (not a self-square) — checked directly for the winning vacuum (χ on axis 1, ξ on axis 0):

```text
(Phi3 x Phi3')_3-type = (0, 0, 1.011)   -- genuinely nonzero, off-diagonal
```

Unlike the self-square, this is nonzero precisely *because* Φ₃ and Φ₃′ sit on **different** axes in the winning vacuum — the same fact that made same-axis combinations pathological for the charged-lepton fit now becomes the reason a cross term has something to work with. This is a different operator than what this task asked for (Φ₃′² alone), and testing it is a separate next step, not carried out here.

## 5. Verdict

```text
theta13 TEST: FAILED, for a structural (not numerical) reason.

Channel "3" of Phi3'^2 (as literally specified): identically zero at the
established vacuum, for all 3 axis choices -- no coefficient can make it
contribute.

Channel "2" of Phi3'^2 (the only other available piece): nonzero, but
degenerate with the already-present m2 parameter -- adds no new direction,
confirmed numerically (identical theta13 = 2.57 deg with 4 parameters as
with 3).

Axis selection: UNCHANGED. (1,0) and (2,0) remain the unique winners;
the added term does not affect any of the 9 combinations, since it is
either zero or redundant everywhere, not just for the winners.

theta12=33.00, theta23=44.94, ratio=0.0300 still hold exactly for the
winning axes -- nothing already working was broken, but nothing new was
gained either.

RECOMMENDATION: Phi3^2, Phi3'^2 self-couplings are exhausted as a source
of new structure. The next candidate is a genuine Phi3 (x) Phi3' cross
term, confirmed nonzero at the winning (different-axis) vacuum -- this
is a different construction from what was tested here and needs its own
pass.
```

---

END OF FINDING
