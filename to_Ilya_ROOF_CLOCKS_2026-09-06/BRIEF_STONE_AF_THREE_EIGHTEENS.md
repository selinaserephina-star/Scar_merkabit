# BRIEF — STONE AF: THE THREE EIGHTEENS (what Ψ remembers, and whether the roof's clock is rowmotion)

**Staged 2026-09-05 on Selina's "then start the next stone" (after the reply
package). Locked before code (`BRIEF_STONE_AF_LOCK.sha256`). Answers IB's
PROMPT "What exactly does Ψ remember?" (2026-09-04) as its first bar and
his gear-train / rowmotion question ("test whether Φ·c̄ (order 18) or an
order-24 element is rowmotion on a roof poset", RESPONSE 2026-09-03) as
the rest. A free exploration preceded this brief (house rule: exploration
is not gated); the brief registers what the sealed run must reproduce.
Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

Three objects carry the number 18 = h(E₇): the merkabit's clock Ψ (SM-041:
rowmotion on the E₇ minuscule poset, order 18, orbits [18, 18, 18, 2]);
the E₇ Coxeter element c₇ acting on the 56 weights (the board); and the
roof's Φ·c̄ (SM-039: the turn times the E₈ Coxeter image, order 18 on 360
points). Which of these are the same object, and does the roof's one have
any rowmotion in it?

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AF0a:** the pair type is the sign of the E₇ inner product (SM-041's
  AC0a, re-run: P ↔ +½ (1512 ordered pairs), S ↔ −½ (1512), v ↔ −3/2 (56)).
- **AF1 (his prompt — per-type survival under Ψ^k, registered):** at k = 1,
  v-pairs kept 1 / 28, P-pairs 504 / 756, S-pairs 497 / 756; the random
  baseline per type (200 permutations, fixed seed) is near 1/56, 1/2, 1/2.
  P and S survive equally within 2 points and v is destroyed: NO type is
  privileged — his decision rule ("one type survives much better") is NOT
  met. At k = 9 all 28 v-pairs are kept and P = S = 460 / 756 exactly. The
  full table k = 1..17 and the 3 × 3 type-transition matrix at k = 1 are
  printed. Ψ⁹ commutes with ι, is fixed-point-free, and is NOT ι.
- **AF2 (the E₇ Coxeter element on the board, registered):** the seven
  simple reflections of E₇ (the BETA base of SM-040) act on the 56 roots
  with ⟨r, α⟩ = 1; the products over all 7! orderings give exactly 64
  distinct Coxeter elements (2⁶: the acyclic orientations of the E₇
  diagram [P cited: Shi]); every one has order 18 and cycle type
  [18, 18, 18, 2] on the board — the SAME orbit structure as Ψ (Rush–Shi's
  equality of orbit structures, [P cited], seen on the data); and c⁹ = ι
  for every Coxeter element (the exponents of E₇ are all odd, so c⁹ = −1
  on the weights). Ψ is NOT in W(E₇): the 56 board masks span V (F₂-rank
  8) and the linear map defined by Ψ on a basis of eight board points
  disagrees with Ψ somewhere (SM-040's "no linear extension", re-seen).
- **AF3 (how far Ψ is from a Coxeter element, registered):** the maximum
  number of board points on which Ψ (or Ψ⁻¹) agrees with any of the 64
  Coxeter elements is 14 of 56; the agreement distribution is recorded;
  the type-score of Ψ∘c⁻¹ for a best c is recorded [obs]. Ψ shares the
  Coxeter element's orbit structure and nothing else of it.
- **AF4 (the E₇ Coxeter element seen from the roof, registered):** its
  mod-2 image c̄₇ = the product of the seven transvections t_β acts on the
  120 nonsingular vectors fixing v, with Dickson invariant 1 — OUTSIDE Ω =
  W⁺(E₈)/±, in the coset of ι = t_v (SM-040); cycle type on the 120:
  one fixed point (v), one 2-cycle and three 18-cycles on the board, seven
  9-cycles on the 63 Paulis.
- **AF5 (the roof's 18 is not rowmotion — [P] on computed inputs +
  sealed data):** Φ·c̄ lies in the coset Ω·Φ (⟨Ω,Φ⟩ = Ω:3, SM-039); c̄₇
  lies in Ω·ι; in Ω:S₃ (SM-036) conjugation preserves the S₃-class of the
  coset, a 3-cycle is not a transposition, so Φ·c̄ and c̄₇ are NOT
  conjugate. Orbit structure (Φ·c̄'s cycle type on 360 read from the
  sealed SM-039 log, not recomputed here; the order-24 twisted elements'
  types likewise) against the rowmotion orbit structures in hand
  ([18, 18, 18, 2] on 56 for E₇; [12, 12, 3] on 27 for each E₆ sheet,
  SM-041): no match, and no roof poset is named. REGISTERED: under IB's own
  decision rule ("rowmotion does not match / no poset is found → not
  supported"), "Φ·c̄ or an order-24 element is rowmotion on a roof poset"
  is NOT SUPPORTED as stated. The only 18-clock that IS rowmotion is the
  merkabit's.

## Machinery

`scar56_data.json` (SM-005) READ-ONLY; the E₈-root replay, the label
matching and the pair-type function VERBATIM from
`verify_stone_ac_parity_rule.py` (its lines 55–108, minus its check call,
which is re-issued as AF0a); the E₇ base BETA from the same block; the
sealed SM-039 log `verify_stone_aa_roofclock.log` read for AA5a/AA5c
cycle types. Pure combinatorics and F₂ arithmetic; no group caches. Own
cache `_stone_af_cache/`. Outputs: `verify_stone_af_three_eighteens.py`,
`.log`, `STONE_AF_THREE_EIGHTEENS.md`. Runtime: seconds.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; no registry/git writes by the
executor. Not RH/GRH. Rule 3: "clock", "gear", "remember" are labels; the
mathematics is orbit structures, agreement counts and a coset argument.
