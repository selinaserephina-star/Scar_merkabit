# BRIEF — STONE AJ: THE HEART AT THE STILL POINT

**Staged 2026-09-05 on Selina's "continue the run" (the next open named at
the end of SM-047: is the roof clock conjugate to Φ·g for a g at the
still point?). Locked before code (`BRIEF_STONE_AJ_LOCK.sha256`).
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

SM-047 made the order-18 twisted elements one class. So "is Φ·c̄ conjugate
to Φ·g for some g in the still point G₂(2)" is a census question: the
still point commutes with the turn (SM-038/039: Φ P(g) Φ⁻¹ = P(g) for
g ∈ G₂(2)), so Φ·g has order lcm(3, ord g), and G₂(2)'s orders are
{1, 2, 3, 4, 6, 7, 8, 12} (SM-038 census). No 9, no 18. The deeper
questions are where the heart x = (Φ·c̄)⁶ and the cube (Φ·c̄)³ sit
relative to the still point, and whether the vector shadow C̄ can turn
into an eighteen.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AJ0a (replay):** Stone AA stages 0–2 VERBATIM (as SM-045–047); G₂(2)
  = the sealed 12,096 (SM-038's G_list) lifted to 360-point permutations
  by closure from a few generators (each element's vector-block part
  identifies it in G_list; 12,096 distinct); class(x) with transversal
  and C_Ω(x) of order 1944 re-derived (SM-047).
- **AJ1 (the still point commutes with the turn, and its twisted orders —
  registered):** Φ P(g) = P(g) Φ for ALL 12,096 g; the orders of Φ·g over
  G₂(2) are exactly {3, 6, 12, 21, 24} with multiplicities following the
  census (3: 1+728, 6: 315+2520, 12: 756+3024, 21: 1728, 24: 3024) — no
  eighteen: by SM-047's one class, **Φ·c̄ is conjugate to no Φ·g with g at
  the still point**; the maximal twisted order 24 IS at the still point:
  Φ·g₈ for every element of order 8. The cycle types on 360 of the 3,024
  elements Φ·g₈ — which of the two sealed order-24 types they realise,
  and in what numbers — recorded; REGISTERED GUESS: both types appear.
- **AJ2 (the heart at the still point — registered guess):** of the 728
  elements of order 3 in G₂(2) (two G₂(2)-classes, sizes 56 and 672 [P
  cited: U₃(3) has 3A of size 56 and 3B of size 672; both survive in
  G₂(2)] — measured as the orbit sizes under G₂(2)-conjugation), exactly
  the class of 56 lies in class(x) and the class of 672 does not. Fixed
  dimensions on V of both classes recorded; the number of G₂(2)-elements
  in class(x) is then 56, and C_Ω(x) ∩ G₂(2) has order 216 for such an
  element (recorded).
- **AJ3 (the cube of the eighteen at the still point — registered
  guess):** among the 2,520 elements of order 6 in G₂(2), those with
  square in class(x) are transported into the fibre over x (transversal)
  and conjugated by C_Ω(x): at least one is conjugate to (Φ·c̄)³. If none,
  INVERTED and recorded: the eighteen's cube is not at the still point.
- **AJ4 (the vector shadow turns into an eighteen — registered):** 3,000
  random elements g of C̄ = Stab_Ω(v) (from the sealed generators
  `_stone_u_cache/stab_derived_gens.npz`, as Stone Z): the order
  histogram of Φ·g contains 18; hence (one class) the class of Φ·c̄ meets
  Φ·C̄ — the clock can be turned out of the vector shadow though not out
  of the still point. [obs] the orders of Φ·c̄₇² and Φ·c̄₇⁶ (c̄₇² ∈ C̄, SM-045).
- **AJ5 ([obs] only):** the block cycle types of the order-6 elements of
  G₂(2) whose square is in class(x), against {6: 16, 3: 7, 1: 3}.

## Machinery

`verify_stone_aa_roofclock.py` lines 71–696 VERBATIM; SM-045/047 helpers
verbatim (cycle types, class enumeration with transversal, Schreier
closure); G_list from the replayed Stone Z sift; sealed caches READ-ONLY.
Own cache `_stone_aj_cache/`. Outputs: `verify_stone_aj_heart_stillpoint.py`,
`.log`, `STONE_AJ_HEART_AT_STILLPOINT.md`. Runtime: a few minutes.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3: "heart", "still
point", "turn" are labels; the mathematics is orders, classes and
membership.
