# TO ILYA — 2·Sp₆(2) IS BUILT, AND THE HINGE FORCES A CHOICE (2026-09-01)

**Stenberg side · with Claude. Status: DRAFT (PREPARED-NOT-SENT; the send is
Selina's word).** Answers your THREE ANSWERS batch same-day. Two runs: Stone U
(brief sha-locked before code, 59/59) and the verification of your normalizer
mechanism (19/19). Everything computed; scripts and logs named.

---

## 1. Your "future work-item" is done: 2·Sp₆(2), explicit

Your existence note said: *build its explicit structure if possible.* It was
possible the same day (`BRIEF_STONE_U_2COVER.md` locked c27a9019… before code;
`verify_stone_u_2cover.py`, 59/59):

- Ambient: **W(E₈)** on its 240 roots (order 696,729,600; the mod-2 kernel is
  exactly {±1}; the 120 nonsingular vectors of the plus-type 𝔽₂⁸ form are
  exactly the root pairs).
- Control: the **vector-type** Sp₆(2) (nonsingular-point stabilizer) lifts
  SPLIT — π⁻¹ ≅ 2×Sp₆(2). That is W(E₇)'s story repeating.
- Target: the **spin-type** Sp₆(2), built from scratch via the even Clifford
  algebra of the 7-dim 𝔽₂ quadratic space (spin module Λ(𝔽₂³); 63
  transvection lifts; irreducible, unique invariant plus-type form),
  transported by an explicit isometry and lifted into W(E₈). Its preimage H
  is **PERFECT — [H,H] = H exactly — so H ≅ 2·Sp₆(2), the non-split Schur
  cover**, order 2,903,040, exhibited inside W(E₈) beside the split cover.
  Independent witnesses: 1008 involutions of the quotient lift to order 4;
  H's element orders include 14, 18, 20, 24, 30 (the order 14 whose absence
  exiled SL(2,7) from W(E₇) is present upstairs, as it must be).

## 2. The tower over the new centre — your Tower B comes alive, with a twist

Preimages in H = 2·Sp₆(2), classified copy by copy:

| downstairs | lifts to |
|---|---|
| L₂(7) | 2×L₂(7) (3 copies) / **SL(2,7)** (1 copy) |
| A₅ | A₅×ℤ₂ (3) / **2I = SL(2,5)** (3) |
| S₄ | **GL(2,3)** (5) / **2O** (1) — **no split 2×S₄ found** |
| A₄ | **2T = SL(2,3)** (8) / A₄×ℤ₂ (1) |
| C₆×ℤ₂ | **C₃×D₄** — a nonabelian stem cover (the very object from the 7↔6 canonicality result) |
| W(E₆) | **non-split 2·W(E₆)** [obs] |
| PGL(2,7) = N(L₂(7)) | 2×PGL(2,7), split [obs] |

Two headlines:

1. **The Schur tower lives over the centre of 2·Sp₆(2)** — SL(2,7), 2I,
   GL(2,3) and 2O, 2T, all present as central lifts. Your Tower B finally
   has a hinge that holds it.
2. **The lift type is CLASS-dependent.** The same abstract subgroup lifts
   split over some conjugacy classes and Schur over others. New joint
   sub-question: is the bitangent-transitive bridge class the SL(2,7)-lifting
   one? (Not yet computed; posed, not asserted.)

## 3. The choice theorem — the two-shadow picture in final form

Because **S₄ never lifts split** over any found copy, S₄ does not embed in
2·Sp₆(2) at all: the spine breaks exactly where the Schur tower comes alive.
Combined with the sealed containment run:

> **W(E₇) = 2×Sp₆(2) holds the whole spine and only the split covers.**
> **2·Sp₆(2) holds the whole Schur tower and breaks the spine.**
> **No single ±-extension of Sp₆(2) contains both towers.
> The ± hinge forces a choice.**

So the exact overgroup lives strictly above both. **Named candidate: W(E₈)**
— the group where Stone U just exhibited the split and non-split doubles side
by side (order 696,729,600). Proposed next joint work-item: the W(E₈)
containment run (does it hold the full spine AND the full Schur tower
simultaneously — and what is the smallest subgroup of W(E₈) that does?).

## 4. Your normalizer mechanism: verified, and it is the bridge class

`verify_ib_normalizer_mechanism.py`, 19/19:

- Your H = {diag(M, (M⁻¹)ᵀ)} ≤ Sp₆(2) ✓ (all 168 preserve Ω); your outer
  element realized by the **block swap J**: J·diag(M,M⁻ᵀ)·J⁻¹ =
  diag(M⁻ᵀ,M) for all M — and M ↦ M⁻ᵀ verified OUTER. ⟨H,J⟩ closes at
  exactly 336 with the full PGL(2,7) order census; the linear centralizer
  solve gives C = 1, capping N at 336. **N = PGL(2,7), [N:H] = 2 — exactly
  our exhaustive 1,451,520-element answer.** Two engines, one theorem, and
  yours supplies what brute force cannot: the outer flip IS the symplectic
  duality X ↔ X* on the Lagrangian split.
- **Which class:** your embedding is transitive on the 28 Arf-1 forms with
  stabilizer S₃ and even-orbit structure [1,7,7,21] — the bitangent bridge
  class, not the Fano-doubled one. Consistent with our contrast result: the
  Fano-doubled class is self-normalizing; the ambient duality belongs to
  your embedding specifically.

## 5. One small flag: the two twos, kept separate

Your Q2 answer says "locally, the double is PGL(2,7)." By your own TWO TWOS
section those are different twos: PGL(2,7) is the **outer** turn
(normalizer), SL(2,7) the **central** cover. The local piece of the central
question is SL(2,7) — and §2 shows it does live over the centre of
2·Sp₆(2), for one of the two L₂(7) classes. So: Q2 outer part closed
(bilateral, mechanism verified), Q2 central part now also closed — by the
build.

## 6. Q3 absorbed

With your word that C_hinge means **GL(2,3)**, the 5↔4 output is determinate:
C_hinge(A₅, S₄) = (S₃, C₂×S₃). Our recorded finding stands as a finding:
that output does not name the observed 5↔4 mediator (A₄ = A₅∩S₄). Note the
resonance with §2: inside 2·Sp₆(2), the ambient chooses GL(2,3) for 5 of 6
S₄-copies — your choice of cover is the ambient's majority choice.

## Standing asks

1. Your word on the choice theorem (§3) — then it goes JOINT.
2. The **W(E₈) containment run** as the next joint work-item — yes/no.
3. The class-dependence question (§2): shall we pin which classes lift
   Schur, starting with whether the bridge class lifts to SL(2,7)?

All verifiers rerun from the repo (Stone U resumes from cache in seconds).

— S. (with Claude), 2026-09-01
