# TO ILYA — THE CONTAINMENT RUN + FOUR ANSWERS (2026-08-31)

**Stenberg side · with Claude. Status: DRAFT (PREPARED-NOT-SENT; the send is
Selina's word).** Answers: your both-shadows confirmation + containment go,
your 7↔6 envelope open, the HINGE/COMPRESSION batch, and the BLIND BRIDGE
second-engine request. Four verifiers, 154 checks, 0 failures. Everything
below is computed; scripts and logs named per section.

---

## 1. The reading, confirmed — and then the run broke our candidate

Yes: both shadows are the two towers. Quotient shadow Sp₆(2); cover shadow
W(E₇); the ± centre the hinge. That reading is now bilateral.

Then we ran the containment against the sealed W(E₇) build
(`verify_overgroup_containment.py`, 32/32), and it refuted **our own sent
proposal** at equal prominence:

- **W(E₇) = ⟨−1⟩ × W⁺ ≅ ℤ₂ × Sp₆(2) — a SPLIT direct product.** W⁺ (even
  words in the simple reflections) has order 1,451,520 and misses −1.
- **Structure lemma** (two lines, verified on 48 subgroups): any subgroup of
  a split product either contains −1 — and then splits itself as ± × (its
  rotation part) — or embeds straight into Sp₆(2). Therefore **a non-split
  cover, whose unique involution IS its centre, can never sit over the ±
  hinge.** Not SL(2,7), not 2I, not 2T — none of them, ever, in W(E₇).
- What W(E₇) DOES hold over the hinge: **exactly the split covers** —
  ±A₅ ≅ Ih, ±A₄ ≅ Th, and 2×L₂(7) (which is precisely what our sealed
  Stone F(b) found the PSL(2,7)-preimage to be).
- Stronger, off the hinge too: **SL(2,7) is not a subgroup of W(E₇) at
  all** — the full element-order census of Sp₆(2) (exhaustive, all
  1,451,520) is {1,2,3,4,5,6,7,8,9,10,12,15}; no 14, and SL(2,7) needs 14.
  **2I = SL(2,5) and 2O are not subgroups either** — exhaustive
  presentation searches (⟨2,3,5⟩, ⟨2,3,4⟩ over every involution class):
  zero witnesses. **2T = SL(2,3) and GL(2,3) ARE inside** (explicit
  witnesses; 168 copies of 2T) — but their central involutions are
  non-central in W(E₇): present, never hinged.
- The spine: all six levels sit in W⁺ (witnesses in the log).

**Verdict.** W(E₇) is the *split-cover* shadow: spine plus Ih, Th, 2×L₂(7),
hinged on ±. The Schur tower SL(2,7) → 2I → GL(2,3)/2O → 2T does not fit —
provably, not for want of searching. The two-tower picture survives; the
name of the cover shadow does not. **Successor candidate: 2·Sp₆(2), the
NON-split double cover** (Sp₆(2) has Schur multiplier ℤ₂; it is a different
group from W(E₇) = 2×Sp₆(2)). Open question to chase jointly: does 2·Sp₆(2)
contain SL(2,7), 2I, 2O over its centre? That needs a 2·Sp₆(2) build —
proposed as the next work-item.

## 2. Your envelope open is closed: [N_G(H) : H] = 2

`verify_envelope_normalizer.py`, 19/19, exhaustive over all of Sp₆(2):

- C_G(H) = 1; **N_G(H) has order 336 and is PGL(2,7).** The outer
  automorphism of PSL(2,7) is ambient in Sp₆(2).
- So: the envelope is canonical **up to the outer flip** — anything natural
  in Sp₆(2) is PGL(2,7)-equivariant, not merely PSL(2,7)-equivariant.
- Your restriction reading verified as stated: H ∩ Stab_G(pt) = S₃, and
  PSL(2,7)/S₃ is the literal restriction of Sp₆(2)/P on the same 28 points.
- Contrast you may like: the SECOND conjugacy class of PSL(2,7) (the
  intransitive, Fano-doubled one from Stone F(b)) is **self-normalizing**
  (index 1). The ambient outer flip belongs specifically to your
  bitangent-transitive embedding.

## 3. The hinge operator: reproduced at 6↔5, and then the news

`verify_hinge_operator.py`, 48/48:

- **Your 6↔5 result stands**: [C₃] unique in A₅, N_{A₅}(C₃) ≅ S₃, preimage
  in SL(2,5) ≅ Dic₃ by presentation witness. C_hinge(C₆×ℤ₂, A₅) = (S₃,
  Dic₃), exactly as you recorded. Your C_max floors and its 6↔5 failure
  also recomputed and confirmed.
- **Your declared next step, executed — three findings:**
  1. At 5↔4 **C_hinge is cover-dependent**: S₄ has TWO double covers
     (GL(2,3) and 2O — our Tower B row), and the preimage of N_{S₄}(C₃)≅S₃
     is **C₂×S₃ in GL(2,3) but Dic₃ in 2O**. "The canonical double cover"
     is exactly what S₄ does not have.
  2. **Neither 5↔4 output matches the observed mediator** (A₄ = A₅∩S₄),
     and 4↔3 gives (C₃, C₆), not the observed V₄. So C_hinge is a genuine
     machine at 6↔5 but does not generalize as-is — recorded as a finding,
     full prominence.
  3. Your "undefined at 7↔6" is **confirmed with a sharper reason**: the
     Schur multiplier of C₆×ℤ₂ is C₂, so double covers EXIST — but C₃×D₄
     and C₃×Q₈ are both stem covers and non-isomorphic. What fails at 7↔6
     is **canonicality, not existence.** (Undefined at 3↔2 and 2↔1 too: no
     C₃ below A₄.)

## 4. Two engines, one answer

Your blind classification spec was run by an isolated second engine on our
side (`verify_blind_engine.py`, 55/55) — it never saw your run, our
registry, or T1–T6. The diff (`ENGINE_DIFF_BLIND_BRIDGE_2026-08-31.md`):

- **Factual agreement 6/6 pairs** — embeddings, shared types, normals,
  quotients, direction, reversibility: no discrepancy anywhere.
- Both engines cut (A₅, S₄) away from the top two pairs — yours by
  gcd-bound saturation (12/12 vs 4/12), ours by the appearance of
  nonabelian shared types (S₃, A₄). Two independent criteria, same cut.
- Ours refines your Class I three ways (normal+split / non-normal loose /
  retract) on predicates your own prose already records.
- Both blind runs rediscover the two-regime theorem from raw data.

## 5. Sorted, on our side

- **Parked** (Rule 3, with the physics path): SPIRAL DESCENT's genome
  comparison. The group-theory half becomes live the day the angles are
  derived from group invariants.
- **Parked as superseded** (by your own three-regime finding, now sharpened
  by §3): COMPRESSION UNIQUENESS LAW.
- **Awaiting formalization, then verifiable**: 7↔6 BOUNDARY (define C_local
  precisely — Cover of what, Norm in which ambient — and "max reachable
  336" becomes a checkable theorem); 7↔6 AS DIRECTED COMPOSITION (your own
  next step: define O(7↔6)).

## Standing asks

1. Your word on the refined two-shadow statement: cover shadow = W(E₇) for
   the SPLIT covers; Schur tower homeless until 2·Sp₆(2) is tested.
2. The 2·Sp₆(2) build as the next joint work-item — yes/no.
3. For C_hinge: which cover of S₄ your operator intends at 5↔4, or whether
   cover-dependence kills the middle regime as a single machine.

All verifiers rerun from the repo in seconds to minutes; logs carry every
witness and every exhaustion statement.

— S. (with Claude), 2026-08-31
