# BRIEF — STONE AA: THE ROOF CLOCK, FIRST MEASUREMENT

**Staged 2026-09-03 on Selina's "do the clock". Successor to SM-038 (the
still point) and SM-036 (the turner). Locked before code
(`BRIEF_STONE_AA_LOCK.sha256`). Deviations = dated AMENDMENT, sha'd before
any reveal; post-reveal changes are findings.**

## Question

The two-register model has one empty cell: the roof's dynamics. At E₇ the
clock Ψ lives outside the grammar group W(E₇) and leaves ι as its
footprint (ιΨι = Ψ⁻¹). At the roof the footprint has to be the turn, and
SM-038 normalized the turn to τ″ of exact order three with fixed set G₂(2).
Stone AA builds **the turn as an operator on states** — a permutation Φ of
the 360 = 3 × 120 nonsingular points of the three 8-dimensional modules
(V, S⁺, S⁻) on which the roof acts — so that ⟨Ω, Φ⟩ = O₈⁺(2):3 becomes an
explicit permutation group, and takes the first measurements a clock would
have to satisfy: what orders the twisted elements reach, what the seven
does when composed with the turn, and where the still point sits in the
state space.

## Construction (declared)

1. **Three modules, three actions.** Ω acts on V by the sealed matrices,
   on S⁺ by ρ⁺ (Stone X) and on S⁻ by ρ⁻ (the odd half of the same 16×16
   spin matrices). Q⁻ := the ρ⁻-invariant quadratic form on S⁻ (exact
   nullspace; expected unique and plus-type: 120 nonsingular spinors).
2. **The turn as a map of states.** T″ := y⁻¹ s̄₁ T⁺ : S⁺ → V satisfies
   τ″(g) = T″ ρ⁺(g) T″⁻¹ (SM-038's normalized turner). Φ on the V-block is
   T″⁻¹; on the S⁺-block it is the exact intertwiner L : S⁺ → S⁻ with
   L ρ⁺(g) = ρ⁻(τ″²(g)) L (64 unknowns over 𝔽₂; expected dim 1, L an
   isometry (S⁺,Q⁺) → (S⁻,Q⁻)); on the S⁻-block it is the map that closes
   the cycle, T″ L⁻¹. Then Φ³ = id by construction, and Φ P(g) Φ⁻¹ =
   P(τ″²(g)) is a checkable identity on every generator, where P(g) is
   g's permutation of the 360 points.
3. **Measurements.** BSGS of ⟨Ω⟩ and ⟨Ω, Φ⟩ on 360 points; the point
   stabilizers of the three blocks; the still point as a joint
   stabilizer; the element orders and cycle types in the twisted coset
   Ω·Φ by sampling, plus two named elements: Φ·g₇ for g₇ ∈ G₂(2) of order
   7, and Φ·c̄ for the image of a Coxeter element of W(E₈).
4. **The seven's module at the still point.** The bridge PSL(2,7) of
   SM-038 acting on v^⊥ (7-dim) and on v^⊥/⟨v⟩ (6-dim symplectic).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AA1 (the three modules):** Q⁻ unique and plus-type (120 nonsingular
  spinors); the three 120-sets are three faithful Ω-orbits; BSGS of
  P(Ω) on 360 points has order 174,182,400.
- **AA2 (THE TURN ON STATES — registered expectation):** L exists, is
  unique, and carries Q⁺ to Q⁻; Φ³ = id on all 360 points; **Φ P(g) Φ⁻¹ =
  P(τ″²(g)) on all 26 generators exactly**; Φ ∉ P(Ω); |⟨P(Ω), Φ⟩| =
  522,547,200 = 3·|O₈⁺(2)|.
- **AA3 (the shadows are the point stabilizers):** Stab(v) in P(Ω) is C̄
  (order 1,451,520); the stabilizers of Φ(v) and Φ²(v) are the two
  spin-type shadows τ″²(C̄), τ″(C̄) (generator membership + order); Φ
  cycles the three block-stabilizer classes.
- **AA4 (THE STILL POINT IN THE STATE SPACE — registered expectation):**
  G₂(2) commutes with Φ on all 360 points (generator check) and **equals
  the pointwise stabilizer in Ω of one Φ-orbit {v, Φv, Φ²v}** — a vector,
  a spinor and a co-spinor, one of each (orbit-stabilizer on the 120
  spinors: C̄ transitive on the S⁺-block, so |Stab_C̄(Φv)| = 12096 = |G|,
  and G fixes all three points).
- **AA5 (the twisted coset — measurement, with one registered lower
  bound):** sampling ≥ 30,000 elements of Ω·Φ: the distribution of
  element orders and the maximal order found, with cycle types on the
  360 points for the maximal-order elements. REGISTERED: order 21 occurs
  (Φ·g₇ with g₇ ∈ G₂(2) of order 7, which commutes with Φ) — **the
  seven-beat clock composed with the turn** — with its cycle type
  recorded; and the order of Φ·c̄ for c̄ = the image of the standard
  Coxeter element of W(E₈) (order 15 in Ω) is recorded against h(E₈) = 30.
  No "clock" claim beyond these numbers: Φ is the turn on states, and the
  maximal twisted order is the roof's analogue of 18 at E₇ and 6 at D₄
  (SM-034) only as a measured number, tagged [obs].
- **AA6 (the seven's module — Brauer character and the Lagrangian
  split):** on v^⊥ the bridge PSL(2,7) of the still point has Brauer
  character (7, 1, 0) at orders (1, 3, 7), i.e. composition factors
  1 + 3 + 3̄ = χ₇ mod 2. Stated honestly in the same breath: 1 + χ₆
  (the Fano seven) has the SAME Brauer character, so the 2-modular
  character cannot tell the two sevens apart; the bridge-specific datum
  registered instead is the **Lagrangian split**: v^⊥/⟨v⟩ = U ⊕ U′ with U,
  U′ the two invariant totally isotropic 3-spaces (the kernels of the two
  cubic factors of x⁷ − 1 at g₇), each PSL(2,7)-invariant — SM-028's
  Lagrangian embedding diag(M, M⁻ᵀ) recovered at the still point. Not
  tested for a Fano-class copy here (scope).

## Machinery (reuse; sealed caches READ-ONLY)

Stone X replay (verbatim, as in SM-038), `_stone_z_cache/` (y, G) or its
7-second recomputation, `_stone_u_cache/` (C's generators, k0_pair),
`_stone_v_cache/` (orders). BSGS and vectorized sift verbatim from SM-038.
Own cache `_stone_aa_cache/`. Outputs: `verify_stone_aa_roofclock.py`,
`.log`, `STONE_AA_ROOFCLOCK.md`. Expected runtime: a few minutes (the
BSGS on 360 points and the 30,000-sample coset scan dominate).

## Discipline

Compute, never assert; every registered expectation resolvable INVERTED at
equal prominence; fail-first logs kept; exact 𝔽₂ and permutation
arithmetic; [P] separated from [C]; no registry/git/knowledge.yaml writes
by the executor. Not RH/GRH. Rule 3: "clock", "turn", "state" are labels;
the theorems concern O₈⁺(2):3 as a permutation group on 360 points.
