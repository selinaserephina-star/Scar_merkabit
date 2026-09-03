# BRIEF — STONE Z: THE STILL POINT OF THE ROOF TURN

**Staged 2026-09-03 on Selina's "do this. the still point of the roof
turn". Successor to SM-036 (the turner τ′) and SM-035 (the G₂ still point
at crystal level). Locked before code (`BRIEF_STONE_Z_LOCK.sha256`).
Deviations = dated AMENDMENT, sha'd before any reveal; post-reveal changes
are findings.**

## Question

SM-036 built τ′, an explicit outer automorphism of Ω = W⁺(E₈)/⟨−1⟩ ≅
O₈⁺(2) cycling the three shadow classes vector → K₃ → K_spin → vector,
with τ′³ inner by a unique intertwiner h′. SM-035 found that at crystal
level the still point of the three-turn is G₂, with PSL(2,7) inside it
canonically. Stone Z asks the finite, roof-level version: **what does the
turn hold still?** Take the sealed vector shadow C̄ and the canonical
triangle (C̄, τ′(C̄), τ′²(C̄)) the turner attaches to it. Compute the
intersection, name it, normalize the turner so that it fixes it pointwise
and has order exactly three, and find which seven sits inside.

## Route (declared)

1. **Replay** Stone X's τ′ machinery verbatim (frame, Λ(E), transvection
   decomposition, ρ⁺, Q⁺, T⁺, τ, τ′ = conj_{s̄₁}∘τ) and cross-check it
   against the sealed `_stone_x_cache/witnesses_x.json` (T⁺ columns, τ on
   the 26 generators, h′). Subgroups of Ω are handled as permutation
   groups on the 120 nonsingular vectors of (V,q) (a faithful action);
   BSGS verbatim from the Schur-pin / lift-law verifiers.
2. **G := C̄ ∩ τ′(C̄)** by exhaustive sift of all 1,451,520 elements of C̄
   through the BSGS of τ′(C̄). Then G′ := τ′(C̄) ∩ τ′²(C̄) and the triple
   intersection.
3. **Normalize the turner:** solve the intertwiner {y g = τ′(g) y} over
   generators of G (exact linear solve, 64 unknowns; enumerate the
   solution space, keep invertible Dickson-0 q-isometries); define
   **τ″ := inn(y⁻¹)∘τ′**, which fixes G pointwise by construction.
4. **PSL(2,7) at the still point:** enumerate G; search (2,3,7)-pairs with
   [a,b]⁴ = 1 generating order 168; fingerprint the copies by the class
   size of their involutions in C̄ (315 = bridge class, 945 = Fano class,
   sealed SM-029) and, separately, in τ′(C̄).
5. **The register of the still point:** the involution classes of G read
   in the vector shadow C̄ and in the spin-type shadow τ′(C̄), with the
   sealed ε-values (63⁻, 315⁺, 945⁻, 3780⁺) applied to the spin-type
   reading (SM-033: a minus involution forces a non-split preimage).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **ZB0 (replay):** τ on the 26 generators reproduces the sealed
  `tau_gen_cols`; T⁺ reproduces `Tplus_cols`; τ′³'s intertwiner
  reproduces `hprime_cols`. C̄ on the 120 nonsingular vectors has order
  1,451,520 and is enumerated.
- **ZB1 (THE STILL POINT — registered expectation):** |G| = **12096** =
  |G₂(2)| (index 120 in C̄: the vector shadow acts transitively on the
  120 nonsingular spinors, the classical rank-3 action of Sp₆(2) with
  stabilizer G₂(2) [P cited]). Identification by computation: [G,G] of
  order 6048 with G/[G,G] ≅ C₂ (U₃(3):2); element-order census
  {1,2,3,4,6,7,8,12}. Name G₂(2) = U₃(3):2 by these data + [P cited: the
  unique index-120 subgroup class of Sp₆(2)].
- **ZB2 (the triangle's intersections):** |G′| = 12096 as well
  (τ′ is an automorphism). The triple intersection C̄ ∩ τ′(C̄) ∩ τ′²(C̄)
  is MEASURED and τ′(G) = G is TESTED; registered expectation, stated
  conditionally: they coincide with G exactly when τ′ normalizes G —
  which the un-normalized τ′ (τ′³ = inn(h′), h′ ≠ 1) need not do. Either
  outcome is recorded; the normalization in ZB3 is what settles the
  geometry.
- **ZB3 (THE TURN OF ORDER THREE — registered expectation):** the
  intertwiner solve yields an invertible Dickson-0 isometry y; **τ″ =
  inn(y⁻¹)∘τ′ fixes every generator of G and satisfies τ″³ = identity on
  all 26 Ω-generators** — the turner normalized to exact order three,
  with the still point as its fixed set. Reason registered: τ″³ is inner
  by an element centralizing G, and C_Ω(G₂(2)) = 1 is expected; if τ″³ =
  inn(z) with z ≠ 1 that is the finding (and z is exhibited).
- **ZB4 (Fix(τ″) = G, as far as the machine reaches):** C̄ ∩ τ″(C̄) = G
  exactly (order 12096 with G inside); the triangle (C̄, τ″(C̄), τ″²(C̄))
  CLOSES: τ″³(C̄) = C̄ and the three pairwise intersections all equal G;
  a random sample of ≥ 1000 elements of Ω contains no τ″-fixed element
  outside G. The full statement Fix(τ″) = G₂(2) is [P cited] (the
  centralizer of a triality automorphism of order 3 in O₈⁺(2) is G₂(2)),
  with the machine-checked part scoped exactly.
- **ZB5 (THE SEVEN AT THE STILL POINT — registered expectation):** G
  contains PSL(2,7) (U₃(3) has L₂(7) as a maximal subgroup, index 36
  [P cited]); the copies found are G-conjugate with N_G(L₂(7)) of order
  336 = PGL(2,7). **Registered: the copy is the BRIDGE class of C̄
  (involutions in the 315-class), not the Fano class** — reason: SM-035
  found the seven that meets G₂ to be the P¹(𝔽₇) deleted module, and
  the bridge class is the one acting on the 28 bitangents = the 28 pairs
  of P¹(𝔽₇) points. Its class in the spin-type shadow τ′(C̄) is
  MEASURED alongside (does the label survive the turn?). An INVERTED
  outcome (Fano) is recorded at full prominence and read against SM-035.
- **ZB6 (the register of the still point):** table of G's involution
  classes by C̄-class size and by τ′(C̄)-class size, with ε. Registered
  expectation: G meets a minus class of the spin-type shadow (its 63
  U₃(3)-involutions are the symplectic transvections there) ⇒ the
  preimage of G in the spin tower 2·Sp₆(2) is NON-SPLIT (2·G₂(2)); in the
  vector shadow the preimage is split trivially (SM-023 structure lemma).
  If all of G's involutions are plus in the spin reading, the verdict is
  UNDECIDED by ε (SM-033: necessity only) and said so.

## Machinery (reuse; sealed caches READ-ONLY)

`_stone_u_cache/` (stab_derived_gens = the 24 generators of C, witnesses
k0_pair), `_stone_v_cache/` (K_240, K_pair_120 orders), `_stone_w_cache/`
(ts_subspaces for the signature instrument), `_stone_x_cache/`
(witnesses_x.json for the replay cross-check), `_liftlaw_cache/` (the
ε-table by class). Own cache `_stone_z_cache/`. Outputs:
`verify_stone_z_stillpoint.py`, `.log`, `STONE_Z_STILLPOINT.md`. Expected
runtime: ~10 min (two exhaustive 1.45M sifts dominate).

## Discipline

Compute, never assert; every registered expectation resolvable INVERTED
at equal prominence; fail-first logs kept; exact 𝔽₂ arithmetic and exact
permutation arithmetic throughout; every [P] fact cited and separated
from [C]; no registry/git/knowledge.yaml writes by the executor. Not
RH/GRH. No identification (Rule 3): "still point", "turn", "memory" are
labels; the theorems are about subgroups of O₈⁺(2) and their covers in
W(E₈).
