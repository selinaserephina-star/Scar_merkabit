# TO ILYA — THE ROOF IS W⁺(E₈), AND THE SPINOR WEARS THE FANO COAT (2026-09-01)

**Stenberg side · with Claude. Status: SEALED 2026-09-01 (PREPARED-NOT-SENT;
the send is Selina's word, recorded in the registry when made).** Package:
this cover + both verifiers with logs (pinning 32/32; Stone V 44/44) + the
Stone V brief with its pre-code lock + the Stone V findings doc + registry
snapshot v0.35 + SHA256SUMS.txt. (Both runs resume from repo caches in
seconds.) Your two adopted work-items are both answered, same day.
Two runs: the class pinning (32/32, three independent routes) and Stone V —
the W(E₈) containment (brief sha-locked before code, 44/44, registered
expectation confirmed). Everything computed; scripts and logs named.

---

## 1. Work-item #3 answered — and the answer inverted our hope

**Pin which classes lift Schur.** Done. My registered hope was that the
bitangent bridge class lifts to SL(2,7). **The data refuted it, decisively:**

- **The bridge class** (your Lagrangian diag(M,(M⁻¹)ᵀ); involutions in the
  315/+ class) **lifts SPLIT** — 2×L₂(7).
- **The Fano-doubled class** (involutions in the 945/− class; the
  self-normalizing one) **lifts to SL(2,7)** — it is the spinorial
  embedding.

Three independent routes agree (`verify_schur_class_pinning.py`, 32/32):
intrinsic involution-class fingerprints matched across both models; an
explicit isomorphism built from the 63-transvection class transporting the
copies directly (gold standard); and fresh exhaustive normalizer scans
reproducing the sealed pattern (SL(2,7)-lifter self-normalizing, split-lifter
N = PGL(2,7)). Canonicality: Out(Sp₆(2)) = 1 [P cited].

**The observation this uncovers — your "familiar two", split between twins:**

> The bridge class carries the OUTER ℤ₂ (N = PGL(2,7), your symplectic
> duality) and no central lift.
> The Fano class carries the CENTRAL ℤ₂ (SL(2,7)) and no outer symmetry.
> **The two twos are distributed — exactly one per conjugacy class.**

Your "once as an outer turn, once as a central cover" is realized as a
computed dichotomy between the only two PSL(2,7) classes in Sp₆(2). Bonus
census: the same 945/− signature marks the 2I- and 2T-lifting copies of A₅
and A₄; the all-945 S₄ copy is the one that lifts to 2O.

## 2. Work-item #2 answered — the roof theorem (Stone V, minimal-found)

**W(E₈) containment.** Run under a brief locked before code (da1d02c2…),
44/44:

- **All 16 tower members** sit inside W(E₈) with explicit witnesses: the
  full spine in the vector-type C ≅ Sp₆(2); the full Schur tower —
  SL(2,7), 2I, GL(2,3), 2O, 2T, the stem C₃×D₄, non-split 2·W(E₆),
  2×PGL(2,7) — in H ≅ 2·Sp₆(2); the split covers Ih, Th over the hinge.
- **The roof:** ⟨C, H⟩ = **W⁺(E₈), the rotation subgroup, exactly** —
  order 348,364,800, index 2 in W(E₈) (every generator determinant +1,
  verified exactly). It is PERFECT, and the 21 witness generators alone
  regenerate all of it. Scope stated honestly: **minimal-found**, not
  proven-minimal.
- **One hinge only:** the stem centre of H IS −1 of E₈ (Z(H) = ⟨−1⟩
  exactly), every Schur witness sits over that same ⟨−1⟩, and the spine
  meets it trivially. The choice theorem's fork closes one floor up
  without multiplying hinges.
- **R/⟨−1⟩ has order 174,182,400 = |O₈⁺(2)|** [P cited, order-only for
  now] — the roof's own shadow looks like the triality group's home, which
  would make your vector/spin distinction (our C vs H) a triality
  statement. Named as the next question, not claimed.

**The theorem, one breath:** the exact overgroup of the full 7→1 descent and
both shadows, minimal-found, is **the rotation half of W(E₈)** — both
towers hanging from a single ± hinge inside one perfect group.

## 3. The arc, in your cadence

The hinge forced a choice.
One floor up, the choice dissolves —
not in a bigger pair,
but in one perfect rotation group.
And the spinor, all along,
wore the Fano coat.

## Standing asks

1. Your word on SM-029 (the pinning + the two-twos dichotomy) — then JOINT.
2. Your word on SM-030 (the roof theorem, minimal-found) — then JOINT.
3. Next work-item proposal: **verify R/⟨−1⟩ ≅ O₈⁺(2)** (beyond order) and
   read the vector/spin pair through **triality** — yes/no?
4. Open flags kept honest: true minimality of the roof and canonicality of
   the (C,H) pair are NOT proven; on the table if you want them chased.

All verifiers rerun from the repo (both runs resume from caches in seconds).

— S. (with Claude), 2026-09-01
