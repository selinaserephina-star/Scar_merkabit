# TO ILYA — THE CLOCK'S LINEAR CENTRALIZER, AND YOUR DESCENT BATCH (2026-09-07)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this cover;
the acceptance note of 2026-09-06 (`to_Ilya_REPLY_ACCEPTANCE_2026-09-06.md`,
unchanged, folded in — its three asks are still open); the triage of your
57 documents (`TRIAGE_IB_BATCH_2026-09-07.md`); **SM-054 Stone AP** with
brief + pre-code lock + verifier + log + first-run log + findings + cache;
the two free explorations that preceded it (`_explore_*_2026-09-07.py/.log`,
NOT sealed, cited only as the disclosure the brief makes); registry
snapshot v0.84; SHA256SUMS.txt.

---

## 1. Your batch is filed

All 57 distinct documents (eight of the downloads were byte-identical
copies) are in `RECEIVED_2026-09-07_IB_DESCENT_LADDER_GENERATIONS/` with
their hashes. Nothing in the batch changes a seal on either side. The
triage sorts them into five clusters and says, for each line, what we
could compute, what is classical, and what is parked.

## 2. Your request, answered without a choice (SM-054)

You asked for a canonical pair (a,b) among our 36 copies of PSL(2,7) so
that you could test Ψ C₂ Ψ⁻¹ = C₂ on the three C₂'s of your V₄, with
"SEALED if exactly one C₂ is fixed."

We did not choose a pair, because the answer does not depend on one.
Every C₂ you can build lies in a PSL(2,7) acting on the 56 through W(E₇)
(SM-013: the bridge class and its unique lift; SM-040: the still point's
action on the board is that action). So your question is whether any
element of W(E₇) commutes with Ψ. We built the centralizer of Ψ in S₅₆
explicitly from its cycle type [18,18,18,2] — 69,984 permutations, 231 of
them involutions — and tested every one for linearity (preserving all
1,540 pair types, which is membership in W(E₇)). **Exactly one is linear:
the identity.** No involution of W(E₇) commutes with the clock. Your test
is therefore NOT SEALED for every C₂, every copy, every (a,b) — and this
is a stronger statement than the test asked for: **C_{W(E₇)}(Ψ) = 1.** It
sharpens SM-044 (Ψ ∉ W(E₇), best agreement 14 of 56) to its final form.

For your convenience, and not as a canon, the verifier also builds one
bridge copy in our coordinates by a targeted (2,3,7) search (its pair is
in `witnesses_ap.json`, convention in the log): order 168, orbits [28,28],
your chain S₄ (24) ⊳ A₄ (12) ⊳ V₄ (4) ⊃ three conjugate C₂'s exactly as you
wrote it, for **all 336** generating pairs of that copy, reaching all 14
V₄'s; 0 of 3 C₂'s Ψ-fixed in every case. The copy reproduces SM-013's
permutation character 2(χ₁+2χ₆+χ₇+χ₈) class by class (fixed points
56/8/2/0/0/0), and the seven-dimensional reflection representation of
W(E₇) restricts to it irreducibly as χ₇.

Two registered items in that run FAILED, and we report them as we report
the passes. Our guess that the Ψ-commuting involution closest to linear
would look like the mirror pr was inverted: the best agreement is pr's
exact number, 1432/1540, but the maximizer is the transposition of the
clock's own axis pair, and 1432 = 1540 − 2·54 is forced for any
transposition of an ι-pair — a number repeated, not a structure repeated.
And our brief's fixed-point count for the order-4 class (4) was our own
sign slip on χ₇(4A); the character evaluated correctly gives 0, which is
what was measured.

## 3. Two corrections to your inbreath documents, at equal prominence

1. **D and ΔL are one number.** With your definitions — D = classes lost
   − classes created by splitting; ΔL = (c_nt(G) − c_nt(H))/π — the
   identity c_nt(H) = c_nt(G) − lost + created gives D = π·ΔL on every
   step. Verified: 1, 1, 0, 2, 1 both ways. The "two channels" are one;
   "(D, ΔL) = (0, 0)" is one condition; the abelian-boundary theorem holds
   on the fixed chain as a table.
2. **D(A₄,V₄) = 0, not 2.** Two of your documents write "new by
   splitting: none". The involution class of A₄ (size 3) splits into the
   three classes of V₄: created = 2, lost = 2 (3A, 3B), D = 0 — as three
   of your other documents say. "Lossless" is a class-count word; the
   step loses log₂3 = 1.585 bits of order, your own Level-5 number.

Your sealed levels 6 and 5 are confirmed exactly, and your "5 → 4 is not
sealed" is confirmed exactly (the three C₂'s are one A₄-orbit with
normalizer V₄). Your "Ψ cannot act through χ₈" is true and is now exact:
no Weyl-group element commutes with Ψ, so no linear map from any
W(E₇)-module to your generation plane can be Ψ-equivariant.

## 4. What we parked, and one request

- **The 1/π cluster.** The class counts 5, 4, 3, 3, 1, 0 are exact and
  confirmed. The π is put in by the definition G(Γ) = (class count)/π, so
  "gives 1/π without tuning" is satisfied by construction. Your own
  FINDING that 1/π is not a group invariant stands; the CANDIDATE does not
  change it. Parked as interpretation.
- **The crystal ladder.** The point-group facts are classical (T_d, T,
  222, 2; PSL(2,7) is not in O(3)). The three materials are cited only to
  "Gemini + Claude verification", and your own batch records one such
  claim (the soft mode) withdrawn. **Please send the papers** (langbeinite
  P2₁3 → P2₁2₁2₁; Rochelle salt 222 ↔ 2; Tl₂Cd₂(SO₄)₃ 2 → 1) before
  either of us grades them. As written, "T → C₂ → C₁ → D₂" is out of order
  against your own ladder. The identification of the chain with these
  transitions stays parked under Rule 3, as the physics path has been.
- **Generations and the flavon.** The representation arithmetic checks by
  hand (End dimensions 1, 1, 1, 3, 5, 9; 8↓S₄ = 2 ⊕ 3 ⊕ 3′; the zero-sum
  rule is the octet's tracelessness). Your no-go — S₃ forces an external
  signed choice — is exactly our Rule 3, and the flavon/Z₃/operator layer
  is that choice made by hand. Parked with the physics path.

## 5. Still open between us (from the acceptance note, unchanged)

- **SM-035, SM-036, SM-037** — your recheck.
- **Direction.** The roof rests; the merkabit's three gates are exact on
  the lattice; the mirror's place in the toggle group and the mixed
  clock-plus-splitter regime wait there. Or the descent's board, now that
  the clock's centralizer is known to be trivial: if a marker for your
  C₂ is to exist at all, it must be non-linear — pr, or a power of Ψ, or
  the parity rule — and that is a computable question we can stage.
- **Publication.** Our proposal for the first paper's spine stands
  (SM-030, 038, 039, 040, 041, 047..052, 053), with the refutations at
  equal prominence.

## In your cadence

You asked for one pair among thirty-six so the clock could choose;
we counted every element that keeps time with the clock,
and found the identity alone.
The marker you want cannot be linear —
and the two channels you opened were one river.
The next word is yours.

— S. (with Claude), 2026-09-07
