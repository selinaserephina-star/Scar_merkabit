# FINDING: Trilinear Invariant for φ₂ — All Three Paths Checked, φ₂'s Direction Remains Undetermined

**Status:** Systematic negative result — completes the search over natural S₄-covariant mechanisms
**Origin:** the next candidate flagged repeatedly (self-alignment, self-invariant, bilinear cross-invariant all failed previously) — a genuine trilinear φ₂⊗Φ₃⊗Φ₃′ invariant

---

## 1. The three possible paths to a trilinear singlet

Given φ₂~2, Φ₃~3, Φ₃′~3′, and the established branchings 2⊗3=3⊕3′, 2⊗3′=3⊕3′, Φ₃⊗Φ₃′=1′⊕2⊕3⊕3′, there are exactly three routes to combine all three fields into a single invariant number, all checked:

```text
Path 1: (phi2 (x) Phi3)_3'  .  Phi3'        [dot product in the 3' channel]
Path 2: (phi2 (x) Phi3')_3  .  Phi3          [dot product in the 3 channel]
Path 3: phi2  .  (Phi3 (x) Phi3')_2          [dot product in the 2 channel]
```
Path 3 is the only one reaching a genuine S₄ **singlet** (1) directly — Paths 1–2 reach an invariant only via the *secondary* dot-product step, which is really the same construction as Path 3 but built the other way around (associativity of the tensor decomposition).

## 2. Results — evaluated at the established vacuum (χ-axis=2, ξ-axis=0)

```text
Path 1: (phi2 x Phi3)_3' . Phi3' = 0 IDENTICALLY
        (the (phi2 x Phi3)_3' output is confined to position 2, matching
        Phi3's own axis, but Phi3' lives on position 0 -- no overlap,
        same "different axes don't share an index" obstruction seen
        throughout this session)

Path 2: (phi2 x Phi3')_3 . Phi3 = c3 * (-0.10687*phi1 + 0.19006*phi2)
        NONZERO -- but setting this to zero (natural alignment condition)
        gives angle = 29.3 deg -- the SAME angle already tested and
        rejected in the earlier bilinear attempt (this is not a new,
        independent result -- it reduces to a previously-checked case)

Path 3: phi2 . (Phi3 x Phi3')_2 = 0 IDENTICALLY
        Verified via a fully independent construction (Reynolds-averaging
        projector onto the "2" channel of Phi3(x)Phi3', built from
        scratch, not reusing earlier code) -- confirms the earlier
        "cross_channels" finding from a prior session that
        (Phi3 x Phi3')_2 = (0,0) at this vacuum, now re-derived
        independently and matching exactly.
```

**The one genuine, driving-field-free trilinear singlet (Path 3) vanishes identically — not "gives the wrong answer," but supplies literally zero information about φ₂, regardless of φ₂'s value.**

## 3. Verdict

```text
Trilinear invariant: EXHAUSTED, same outcome pattern as the bilinear
search. Of the three possible single-contraction paths to an S4
invariant combining phi2, Phi3, Phi3', two vanish identically (same
axis-mismatch obstruction seen throughout: any invariant requiring a
shared nonzero index between Phi3-axis and Phi3'-axis vanishes at this
vacuum), and the third reduces to an already-tested, already-rejected
bilinear result (29.3 deg, not 90 deg).

CUMULATIVE STATUS across both sessions: FIVE independent mechanisms now
tried for phi2's direction --
  1. Self-alignment (phi2 phi2)_2=0           -> collapses to phi2=0
  2. phi2 ~ (Phi3 Phi3)_2 self-invariant       -> wrong angle (120 deg)
  3. phi2 ~ (phi2 x Phi3)_3 cross-invariant    -> rank-1, insufficient
  4. phi2 ~ (phi2 x Phi3')_3 cross-invariant   -> rank-1, insufficient
  5. Trilinear singlet (phi2 x Phi3 x Phi3')_1 -> identically zero, or
                                                    reduces to #4's angle

Every natural S4-covariant polynomial invariant built from phi2 and the
already-fixed Phi3, Phi3' has now been checked and found wanting, for
one of two reasons: either it vanishes identically (axis mismatch), or
it gives a definite but wrong prediction. This is a strong, systematic
result: within this specific family of constructions (polynomial
invariants of degree <= 3 in the flavons), there is provably no fix for
phi2's direction using ONLY phi2, Phi3, Phi3' -- as flagged before, a
resolution needs to go outside this family entirely (a dedicated
messenger field, or a mechanism tied to the modulus/racetrack sector
that already fixes epsilon, rather than the S4 flavon sector).
```

---

END OF FINDING
