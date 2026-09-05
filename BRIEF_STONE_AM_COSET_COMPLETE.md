# BRIEF — STONE AM: THE COSET COMPLETE

**Staged 2026-09-06 on Selina's "continue" (the remaining twisted orders
9, 6, 3 named at the end of SM-050). Locked before code
(`BRIEF_STONE_AM_LOCK.sha256`). Deviations = dated AMENDMENT; post-reveal
changes are findings.**

## Question

SM-047/049/050 account for the twisted coset Ω·Φ at orders 18, 24, 21 and
12: 293/336 of it, in nine classes. The remainder 43/336 = 0.1280 is
orders 9, 6 and 3 (SM-039 sampled 0.0554, 0.0673, 0.0047). This stone
classifies them and closes the census: the densities of all classes found
must sum to exactly 1.

Levers. Order 9: e³ ∈ Ω has order 3; REGISTERED GUESS that it lies in the
heart's class (the class of (Φ·c̄)⁶; note (Φ·c̄)⁻² is itself a twisted
element of order 9 with cube in that class), so the fibre is C_Ω(x) of
order 1944 (SM-047). Order 6: e³ is an involution — the fibre of SM-049.
Order 3: no power is available, but the sampled total density 0.47 %
bounds every order-3 class below 820,000 elements, within reach of direct
enumeration (keys only, no transversal).

Predictions from the densities: order 9 at 0.0554 is 1/18 — one class with
centralizer of order 18; order 3 at 0.0047 is 1/216 + 1/12,096 — the class
of Φ·g₅₆ (g₅₆ a heart at the still point, C_{G₂(2)}(g₅₆) of order 216,
SM-048) plus the turn's own class of 14,400; which would force Φ·g₆₇₂ (the
still point's other order-3 class, centralizer 18 in G₂(2)) to be
conjugate to one of those two rather than a third class. Order 6 is not
predicted (0.0673 is no single reciprocal with an even centralizer).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AM0a (replay):** Stone AA stages 0–2 VERBATIM; G₂(2) on 360; class of
  x with transversal and C_Ω(x) = 1944 (SM-047).
- **AM1 (order 9 — registered):** 150 sampled order-9 twisted elements:
  cycle types recorded; every e³ lies in class(x); per type, C_Ω(e) =
  {h ∈ C_Ω(x) : heh⁻¹ = e} after transport — REGISTERED GUESS: one class
  of density 1/18 (centralizer of order 18); every sampled element
  conjugate to the representative (exact). (Φ·c̄)⁻² is in it.
- **AM2 (order 6 — measured, registered on the closure only):** 150
  sampled order-6 twisted elements: cycle types; per type the involution
  fibre (class of e³ with transversal, Schreier centralizer, C_Ω(e)),
  densities, per-element conjugacy; second representatives where a type
  splits (post-reveal-free: the loop continues until every sampled
  element of the type is assigned to a class, with a cap of four classes
  per type). Recorded; no guess on the count.
- **AM3 (order 3 — registered):** the still point's twisted 3-elements
  Φ·g₅₆ and Φ·g₆₇₂: the Ω-class of Φ·g₅₆ enumerated (keys only, cap
  1,000,000): EXACTLY 806,400 = 174,182,400 / 216 elements; Φ·g₆₇₂ lies
  in it (REGISTERED GUESS; if not, its own class is enumerated and
  reported); 40 sampled order-3 twisted elements: none in the turn's class
  (14,400), all in the class of Φ·g₅₆. The twisted 3-elements are two
  classes, densities 1/216 and 1/12,096.
- **AM4 (the census closes — registered):** the sum of the densities of
  ALL classes found in SM-047, 049, 050 and here equals 1 EXACTLY
  (rational arithmetic). If it falls short, the shortfall and the orders
  where the sample could hide a class are reported; if it exceeds 1, a
  class has been double-counted and the stone says so.
- **AM5 ([obs] only):** the number of classes in the coset by order, and
  the centralizer orders, as a table — the roof's twisted class list,
  computed, without ATLAS names.

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM; SM-045/047/048/050
helpers verbatim (class enumeration with and without transversal,
Schreier centralizer, sampling). Sealed caches READ-ONLY. Own cache
`_stone_am_cache/`. Outputs: `verify_stone_am_coset_complete.py`, `.log`,
`STONE_AM_COSET_COMPLETE.md`. Runtime: tens of minutes (the order-3
enumeration and the order-6 centralizer closures dominate).

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic (fractions for the census); sealed
caches READ-ONLY; no registry/git writes by the executor. Not RH/GRH.
Rule 3.
