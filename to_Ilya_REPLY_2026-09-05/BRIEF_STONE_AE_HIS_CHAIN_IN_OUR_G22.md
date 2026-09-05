# BRIEF — STONE AE: HIS CHAIN IN THE HOUSE'S STILL POINT

**Staged 2026-09-05 on Selina's "prepare the response package … 4"
(reciprocal audit). Locked before code (`BRIEF_STONE_AE_LOCK.sha256`).
Subject: IB's `axis_spiral_verification_package.zip` (sha c4856451…, filed
`RECEIVED_2026-09-05_IB_SEALS_DATAREQUEST_CLOCK/`): a GAP run on
PrimitiveGroup(63,2) verifying {e} ⊂ Z₂ ⊂ A₄ ⊂ S₄ ⊂ PSL(2,7) ⊂ G₂(2), five
PASS; his code is a declared reconstruction. Deviations = dated AMENDMENT;
post-reveal changes are findings.**

## Question

Reproduce every number of his report inside the house's OWN G₂(2) — the
sealed still point of SM-038, `_stone_z_cache/G_rows.npy`: 12,096
permutations of the 120 nonsingular vectors of the vector shadow (its
sha recorded in the log; if absent, run `verify_stone_z_stillpoint.py`
first — this run never regenerates a sealed cache) — and test the one line
his script did not compute: whether the two S₄ classes of PSL(2,7) stay
two classes in G₂(2).

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **AE0a (the model):** G_rows has 12,096 distinct rows, contains the
  identity, is closed under composition on 2,000 random pairs, and fixes
  the defining vector v (= the mask ALPHA of SM-040) — the house G₂(2).
- **AE1 (his §1 — registered):** the (2,3,7)+[a,b]⁴ scan (verbatim Stone
  Z) finds 36 copies of order 168 forming ONE G-class, N_G of order 336;
  the fixed copy H is PSL(2,7) by explicit isomorphism to the Möbius model
  (SM-026 engine). Matches his "order-168 subgroup classes = 1".
- **AE2 (his §2 — registered):** inside H, all subgroups enumerated (179,
  15 classes); exactly 14 subgroups of order 24, all S₄ by explicit iso,
  in two H-classes of 7; for each: N_H(S) = S (24); |N_G(S)| = 48 and
  N_G(S) ≅ C₂×S₄ by explicit iso; G-class length 12096/48 = 252.
- **AE2b (THE LINE HIS SCRIPT DID NOT COMPUTE — registered expectation):**
  the two H-classes of S₄ are FUSED in G — the G-conjugates of one S₄ (252
  subgroups) contain all 14 S₄'s of H — because N_G(H) = PGL(2,7) carries
  the outer automorphism that swaps the two classes. Hence his "Total S4
  copies = 504, Total S4 classes = 2" (an inference, not a computation in
  his script) double-counts: the S₄'s of G meeting H form ONE class of
  252. Resolvable INVERTED (if the classes stay distinct in G, his line
  stands and ours falls).
- **AE3 (his §3 — registered):** each S₄ has exactly one A₄ (its derived
  subgroup); N_{S₄}(A₄) = S₄, N_H(A₄) = S₄ (24), |N_G(A₄)| = 48 ≅ C₂×S₄,
  G-class length 252; the two H-classes of A₄ likewise FUSE in G
  (registered, same mechanism).
- **AE4 (his §4 — registered):** in the fixed A₄ the three involutions form
  one A₄-class; N_{A₄}(Z₂) = C₂×C₂ (4), N_{S₄}(Z₂) = D₈ (8), N_H(Z₂) = D₈
  (8), |N_G(Z₂)| = 192; class length 21 in H and 63 in G. REGISTERED: the
  63 G-conjugates of z are the 63 inner involutions of SM-038, and N_G(Z₂)
  = C_G(z) fixes exactly one Pauli u (a nonsingular vector ≠ v with
  B(u,v) = 0) and EQUALS the stabilizer of that Pauli in G — SM-040's 192
  read from his chain. Element-order census of N_G(Z₂) recorded [obs]
  against his "(SL(2,3):C4):C2".
- **AE5 (his §5 + the chain as containments):** {e} < Z₂ < A₄ < S₄ < H < G
  as actual subsets in one model, orders 1, 2, 12, 24, 168, 12096.
- **AE6 (the chain meets the still point's geometry — registered):** H
  acts on the 36 even thetas (the classes {x, x+v}, x singular, B(x,v)=1,
  via the matrix recovered from each permutation) with orbits [1, 7, 7,
  21] (SM-040); each S₄ of H is the stabilizer in H of exactly one theta,
  the seven S₄'s of one H-class being the stabilizers of the seven thetas
  of one 7-orbit and the other class of the other 7-orbit — his "S₄ =
  point stabilizer of the 7-point action", located on the board.

## Machinery

`_stone_z_cache/G_rows.npy` READ-ONLY; the F₂ / E₈-mask replay, mvec,
NONSING, perm_of / mat_of_perm VERBATIM from `verify_stone_ab_merkabit.py`;
the PSL scan VERBATIM from `verify_stone_z_stillpoint.py`; the group class
+ explicit-iso identifier VERBATIM from `verify_blind_engine.py` (library
extended by one model, C₂×S₄, built by direct_gens). Own cache
`_stone_ae_cache/`. Outputs: `verify_stone_ae_his_chain.py`, `.log`,
`STONE_AE_HIS_CHAIN_IN_OUR_G22.md`. Runtime: under a minute.

## Discipline

Compute, never assert; registered expectations resolvable INVERTED at
equal prominence; exact arithmetic; sealed caches READ-ONLY; no
registry/git writes by the executor. Not RH/GRH. Rule 3: "axis",
"spiral", "descent" are his labels; the mathematics is a subgroup chain
with normalizers and class lengths.
