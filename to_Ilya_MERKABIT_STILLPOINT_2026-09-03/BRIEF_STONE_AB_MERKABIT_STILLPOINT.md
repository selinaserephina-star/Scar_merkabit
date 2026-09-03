# BRIEF — STONE AB: THE MERKABIT UNDER THE STILL POINT

**Staged 2026-09-03 on Selina's "do this" (the merkabit under the still
point). Successor to SM-038/SM-039; re-reads the Clifford trilogy
(SM-015/016/017) with the roof in hand. Locked before code
(`BRIEF_STONE_AB_LOCK.sha256`). Deviations = dated AMENDMENT, sha'd before
any reveal; post-reveal changes are findings.**

## Question

Where does the merkabit's 56-machine sit in the roof's state space, and
what does the still point G₂(2) do to it? The trilogy placed the bridge in
Sp₆(2) = the 3-qubit Clifford quotient and proved Ψ has no shadow there.
Stone Z/AA gave the roof a still point and a turn acting on 360 states.
Stone AB places the board, the bitangents, the thetas and the chirality
bit inside the V-block by exact identification, and measures the still
point's action on each.

## Identification (declared)

- **The board.** The 56 E₇ weights = the 56 roots r of E₈ with ⟨r, α⟩ = 1
  (α = the sealed A₁ root, v = its mask); their masks are exactly the 56
  nonsingular vectors u with B(u,v) = 1. The sealed 56-machine data
  (`scar56_data.json`, SM-005) gives the weights as Dynkin labels and the
  crystal edges by colour; the E₇ base inside α^⊥ is chosen, its Cartan
  matrix aligned to the data's by node relabeling (E₇ has no diagram
  automorphism), and each of the 56 vertices is matched to its root by
  its label vector. The match must be a bijection or the stone stops.
- **The dictionary.** 120 nonsingular = {v} ⊔ 63 (B(u,v)=0: the Paulis)
  ⊔ 56 (the board); 135 singular = 63 (B=0) ⊔ 72 (B=1). The 128 vectors x
  with B(x,v) = 1, modulo v, are the 64 quadratic forms of Stone Q: the
  56 nonsingular give the 28 odd forms (bitangents = ι-pairs), the 72
  singular give the 36 even thetas.
- **The chirality bit.** ι = −1 of E₇ acts on the 56 roots as r ↦ α − r;
  mod 2 this is u ↦ u + v = t_v(u). So ι is the transvection of the
  shadow's defining vector, Dickson 1, outside Ω.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AB1 (the identification):** the 56 masks with B(u,v) = 1 ↔ the 56
  vertices of the sealed machine, bijectively, with every crystal edge of
  colour i realized as subtraction of the i-th E₇ simple root; the
  sealed IOTA permutation equals u ↦ u+v under the match; the sealed PSI
  and PR transported to masks are permutations of the 56 that do NOT
  extend to elements of Stab(v) (Ψ nonlinear, pr odd — SM-015/016
  re-seen through the roof).
- **AB2 (the dictionary counts):** 1 + 63 + 56 and 63 + 72 as stated;
  the 56 pairs {u, u+v} are 28 = the odd forms, the 72 singular mod v are
  36 = the even forms (Arf read off q on the coset: q(x) = 1 odd, 0 even).
- **AB3 (THE STILL POINT ON THE BOARD — registered expectations):**
  G₂(2) acts on the 28 bitangents TRANSITIVELY with stabilizer of order
  432, and on the 36 even thetas TRANSITIVELY with stabilizer of order
  336; on the 63 Paulis transitively with stabilizer of order 192; on the
  56 itself: MEASURED (transitive with stabilizer 216, or 28 + 28).
- **AB4 (THETA ↔ SEVEN — registered expectation):** the stabilizer in
  G₂(2) of each even theta is a PGL(2,7) whose derived subgroup is one of
  the 36 PSL(2,7)'s of SM-038, and each PSL(2,7) fixes exactly ONE even
  theta: an exact bijection {36 even thetas} ↔ {36 sevens at the still
  point}. The bridge copy's fixed theta (SM-003's [1,7,7,21] orbit
  structure) is its own.
- **AB5 (two intersections as data):** |W(E₆) ∩ G₂(2)| (the bitangent
  stabilizer meeting the still point) — by AB3 this is the 432 group;
  identify it. And the raw turner's 192 (SM-038, the triple intersection
  under τ′): is it the stabilizer in G₂(2) of one Pauli? MEASURED.
- **AB6 (Ψ against the roof's incidence — the well-posed substitute):**
  the request "measure ν-style how far Ψ sits from the twisted Coxeter's
  action, restricted to the 56" is ill-posed as stated: Φ·c̄ moves the
  blocks and stabilizes no 56-set, and the only order-18 elements of
  Aut(Ω) that preserve the board are in W(E₇), where SM-016 already
  measured ν(Ψ) = 38 with the Coxeter class at 42. The substitute
  measured here: the roof's incidence on the board — for u ≠ u′ in the
  56, u + u′ ∈ v^⊥ is a Pauli (nonsingular), a singular point, or v — and
  the fraction of pairs whose type is preserved by Ψ, Ψ², Ψ³, Ψ⁹, pr, ι,
  a Weyl element (100 % by linearity, the control) and 200 random
  permutations (the baseline). REGISTERED: ι and every Weyl element score
  100 %; Ψ and pr score strictly below 100 % (they are not linear) and
  above the random baseline; the exact numbers are the finding.

## Machinery (reuse; sealed caches READ-ONLY)

Stone X / SM-038 replay verbatim (as in SM-039); `scar56_data.json`
(SM-005) for verts / EDGES / PSI / PR / IOTA; `_stone_z_cache/` for G.
Own cache `_stone_ab_cache/`. Outputs: `verify_stone_ab_merkabit.py`,
`.log`, `STONE_AB_MERKABIT_STILLPOINT.md`. Expected runtime: a few minutes.

## Discipline

Compute, never assert; every registered expectation resolvable INVERTED at
equal prominence; fail-first logs kept; exact arithmetic; [P] separated
from [C]; no registry/git/knowledge.yaml writes by the executor. Not
RH/GRH. Rule 3: "board", "Pauli", "theta" are labels for orbits and
cosets in (V, q); no physics, no qubit claim beyond SM-015's sealed
identification.
