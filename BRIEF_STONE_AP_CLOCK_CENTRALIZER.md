# BRIEF — STONE AP: THE CLOCK'S LINEAR CENTRALIZER

**Staged 2026-09-07 on Selina's "do 1 and 2" (IB's REQUEST TO SELINA —
Canonical Pair for the Ψ-Marker Test, his date 2026-09-06, filed
`RECEIVED_2026-09-07_IB_DESCENT_LADDER_GENERATIONS/`). Locked before code
(`BRIEF_STONE_AP_LOCK.sha256`). Disclosure: the answer was seen in a free
exploration the same day (`_explore_psi_marker_enumeration_2026-09-07.py`,
NOT sealed); this run re-derives it under registered bars, adds the
consistency and universality bars, and adds one genuinely registered guess
(AP7). Deviations = dated AMENDMENT; post-reveal changes are findings.**

## Question

IB asks for a canonical generating pair (a,b) of one of the 36 PSL(2,7)
copies of the still point so that he can build his chain S₄ ⊃ A₄ ⊃ V₄ ⊃
{C₂⁽¹⁾, C₂⁽²⁾, C₂⁽³⁾} and test whether the clock Ψ fixes exactly one C₂
(Ψ C₂ Ψ⁻¹ = C₂). The house answers without a choice: every C₂ he can
build is an element of W(E₇) acting on the 56 (SM-013: the bridge class
and its unique lift; SM-040: the still point's action on the board is
that action), so his question is whether ANY element of W(E₇) commutes
with Ψ. Compute the centralizer of Ψ in S₅₆ in full and intersect it with
W(E₇); instantiate his exact test on a bridge copy built in our
coordinates for every (2,3,7) pair; and settle the bookkeeping of his
"two channels" D and ΔL on the chain.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AP0:** the brief is sha-locked.
- **AP1 (the board, VERBATIM from Stone AC/AF):** pair type = sign of the
  E₇ inner product (P ↔ +1/2: 1512 ordered pairs, S ↔ −1/2: 1512, v ↔
  −3/2: 56); ι preserves all pair types with trace −7 on the seven; the
  seven simple reflections preserve all pair types with trace 5; a
  permutation of the 56 lies in W(E₇) iff it preserves every pair type
  (the weights span, an isometry of the weight set is linear, Aut of the
  E₇ lattice is W(E₇) ∋ −1) — [P], stated in the log.
- **AP2 (the centralizer):** Ψ has cycle type [18,18,18,2] (SM-012); the
  centralizer of Ψ in S₅₆ is constructed explicitly (three shifts, a
  permutation of the three 18-cycles, the 2-cycle's swap): 18³·3!·2 =
  69,984 distinct permutations, every one commuting with Ψ, and this is the
  whole centralizer [P: |C(σ)| = ∏ mᵢ! · ℓᵢ^{mᵢ}]. Its involutions number
  231 = 15 + 3·72.
- **AP3 (REGISTERED — the answer):** the intersection of that centralizer
  with W(E₇) is {1}: of the 69,984 exactly one preserves every pair type,
  the identity; in particular 0 of the 231 involutions is linear. Hence no
  element of W(E₇) — no C₂ of any PSL(2,7) copy under any generating pair —
  is normalized by Ψ. Best pair-type agreement among the 231 recorded
  [obs] (AP7). Also recorded: Ψ⁹ and ι·Ψ⁹ are not linear (SM-016 re-seen).
- **AP4 (a bridge copy in our coordinates — SM-013 re-seen; registered):**
  a PSL(2,7) transitive on the 28 ι-pairs is built by a (2,3,7) search
  inside W(E₇) restricted to the cycle types SM-013's permutation
  character 2(χ₁+2χ₆+χ₇+χ₈) predicts (involutions 2²⁴1⁸, order-3 elements
  3¹⁸1²); order 168; orbits [28,28] on the 56; its class census 1/21/56/42/
  24/24 with fixed points on the 56 exactly 56/8/2/4/0/0 (1A/2A/3A/4A/7A/7B)
  and traces on the seven 7/−1/1/−1/0/0 = χ₇ (registered: the seven
  restricts irreducibly to the bridge class).
- **AP5 (his test, instantiated for every pair):** in that copy all 336
  (2,3,7)-generating pairs (a,b) give, by his words X = ABAB⁻¹,
  Y = B⁻¹ABAB⁻¹AB, P = X², Q = XY: |⟨X,Y⟩| = 24, |⟨P,Q⟩| = 12 normal in it,
  |⟨P, QPQ⁻¹⟩| = 4 normal in the 12 with quotient of order 3, three
  distinct C₂'s forming one A₄-orbit with normalizer of order 4; the V₄'s
  reached are the 14 V₄'s of the copy; and for every pair 0 of the 3 C₂'s
  is normalized by Ψ (each of the copy's 21 involutions fails). With AP3
  this is universal over the 36 copies of the still point and every
  PSL(2,7) in W(E₇) [P, one line]: **NOT SEALED, for every (a,b).**
- **AP6 (his two channels — registered):** on the chain PSL(2,7) ⊃ S₄ ⊃ A₄
  ⊃ V₄ ⊃ C₂ ⊃ {e} (in the copy), nontrivial class counts 5, 4, 3, 3, 1, 0;
  per step (lost, created-by-splitting) = (2,1), (2,1), (2,2), (2,0),
  (1,0); D = lost − created = 1, 1, 0, 2, 1 = c_nt(G) − c_nt(H) at every
  step — identically, since c_nt(H) = c_nt(G) − lost + created [P]. His
  D(A₄,V₄) = 2 ("new by splitting: none") is refuted: A₄'s involution class
  splits into V₄'s three, created = 2, D = 0.
- **AP7 (REGISTERED GUESS, resolvable INVERTED):** the best pair-type
  agreement among the 231 Ψ-commuting involutions is exactly 1432/1540
  (= the mirror pr's kept fraction of SM-040/SM-053, 92.99 %), and every
  maximizer has pr's cycle type 2²⁷1². If the maximum differs from
  1432/1540 or the maximizers have another type, INVERTED and recorded.
- **[obs]:** fixed-point spectrum of involutions of W(E₇) on the 56 as
  sampled (expected values 0, 8, 16, 32 from the reflection class and the
  bridge class; recorded as seen).

## Machinery

`scar56_data.json` READ-ONLY (Ψ, ι, the 56 vertices); the E₈-root /
E₇-weight / pair-type replay VERBATIM from
`verify_stone_af_three_eighteens.py` (itself verbatim from Stone AC);
seven simple reflections as permutations of the 56 (AF2); trace on the
seven by the Gram-sum identity (7·Σ⟨p(w),w⟩ / (56·|w|²)), validated on ι
and the reflections in AP1. Permutation-group closure by BFS with a cap;
conjugacy classes of the small groups by brute force. Own cache
`_stone_ap_cache/witnesses_ap.json` (the (a,b) found, its V₄'s, the
centralizer count, the AP7 value). Outputs:
`verify_stone_ap_clock_centralizer.py`, `.log`,
`STONE_AP_CLOCK_CENTRALIZER.md`. Runtime: under a minute.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic (integers and fractions; the trace
formula is exact in rationals); sealed caches READ-ONLY; no registry/git
writes by the executor. Not RH/GRH. Rule 3: "marker", "descent",
"inbreath" are his labels; the mathematics is a centralizer computation
and a subgroup chain with class counts.
