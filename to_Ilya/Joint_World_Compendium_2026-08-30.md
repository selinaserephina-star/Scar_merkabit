---
title: "The Joint World — Complete Findings Compendium"
subtitle: "Every theorem, refutation, instrument, and open problem of the Scar–Merkabit lane, in one report"
author: "Selina Stenberg, with Claude (Anthropic Fable 5) · for Ilya Balashov"
date: "2026-08-30"
---

Dear Ilya,

You have seen the bridge — the Bitangent Bridge draft and its report. This
compendium is everything else: the joint lane grew far past the bridge in a
single day, and rather than send twelve documents I am sending one map plus
the complete sealed archive. Every claim below is a passing check of a named
script in the enclosed package (Python 3 + numpy, no GAP; ~150 automated
checks plus 3,718 explicit witnesses); the registry (`SCAR_MERKABIT_REGISTRY.md`,
v0.10, rows SM-001..SM-014) is the single source of truth, and the lane
governs itself by a machine-readable KCP (`knowledge.yaml` — note its
authority clause: external sharing of joint material requires both our words).

**Reading order if you have one hour:** this letter → the verification
report (about your registry — you have not seen it yet, and §2 below is its
summary) → `STONE1_CERTIFICATE.md` → `STONEF_FIELD.md` → the machine
(ask Selina for the link; it now has a Waves view).

---

## 1. What you already have

The bridge (registry rows SM-003, SM-008): our two frameworks meet inside
Sp₆(2) = W(E₇)/± on the 28 bitangents of your Klein quartic; W(E₆) is the
stabilizer of one bitangent, PSL(2,7) is transitive on all 28, and the
intersection is S₃ = N(⟨z₃⟩) — your universal stabilizer. The 2:1 map from
your 3A class onto the bitangents; the two Lie branchings of the 27
(3χ₁⊕3χ₈ and 6χ₁⊕3χ₇); the cyclotomic shadow (√−7 yours, √−3 ours, √21
the handshake). Co-authored draft awaiting your pass.

## 2. What you have NOT yet seen — the audit of your registry (SM-001/002)

Before the bridge, your master registry was audited the way Selina's corpus
was audited: PSL(2,7) rebuilt from scratch (character table *derived* by
Burnside–Dixon, verified exactly over ℚ(√−7)), **35+ of your GAP rows
independently confirmed**, 9 classical, your note-7 credited in full — and
five corrections, each with a GAP one-liner in the enclosed verification
report: **C1** T4's Higgs channel count is 4 not 5 (⟨χ₃²,χ₁⟩ = 0);
**C2** MOLIEN-REC fails for χ₆ (char.poly typo included); **C3** χ₃³
contains χ̄₃ not χ₃; **C4** row 125's "7×ℤ₇⋊ℤ₃" should be 8; **C5** λ = 1/8
predicts m_H = 123.11 GeV — a ≈13σ hidden failure in exactly your note-7
sense. The report proposes the backport rule we now both run on.

## 3. The resurrection theorem (SM-005) — your favourite will be this one

The E₆-branching of the E₇ minuscule 56 is **27 ⊕ 27̄ ⊕ 1 ⊕ 1**, and the
odd diagram gate pr (cycle type 1²·2²⁷) fixes exactly the two singlets
while its 27 transpositions pair the sheets point-for-point. Selina's
original dual-spinor picture — *refuted* as a description of the E₆
crystal — is **true one floor up**. Corollary: pr and the antipode ι are
*bilingual* (zero magic in both grammars); the clock Ψ is the sole magic
source. An interactive instrument ("The 56-State Machine": mirrored
two-sheet board, 28-frame view, both magic meters exact, and now the
standing waves) realizes all of it.

## 4. The depth theorems (SM-009/010/014) — the machine's price list

- **Transportation certificate (Young/wreath typing):** the double coset of
  a program is its block-transport contingency table, and "writable with k
  magic gates" ⟺ an integer flow problem. Exact results: 27-machine depth
  3 (Young) / **2** (wreath); 56 branch grammar depth 5 (Young) / **2**
  (with the sheet-swap — which is pr, and free). *Symmetries have exchange
  rates: the S₃ is worth one magic gate, the mirror three.*
- **Hyperoctahedral calculus (frame grammar):** your Gelfand pair
  (S₂ₙ, Bₙ) — coset types on p(28) = 3,718 partitions. Triangle
  inequalities proven necessary (exhaustive n ≤ 7); two candidate
  sufficiency laws refuted on exact data; **the general support law is
  open, and our exact n ≤ 7 tables are enclosed as its data — this problem
  is yours if you want it.** The depth theorem was closed anyway:
  **frame-grammar magic-depth = exactly 2**, by explicit machine-verified
  witnesses for all 3,718 types (cache enclosed).
- **The quantum lift:** add one genuine superposition gate W (Hadamard on
  every ι-pair). Exact local algebra D₁₆; **certificate: W-depth = max
  local H-length + a global H-parity superselection charge** — verified
  exhaustively on small machines; the 56 frame-quantum group has order
  2·8²⁸·28! and **W-depth exactly 4**. The day's ladder: *scrambling costs
  2, superposition 4, sign flips are the dearest objects in the building.*

## 5. The field theorems (SM-012/013) — Stone F

- The clock's standing-wave spectrum: all 18th roots of unity (mult 3;
  ±1 mult 4), and **the CSP census is its trace formula** — the machine's
  oldest checksum was spectral bookkeeping all along.
- All 28 ι-frames live inside single clock orbits; the clock's own 2-cycle
  **is** an ι-frame straddling the sheets (its *axis*); the "4/28 shared
  pairs" mystery = one axis pair per orbit. ιΨι = Ψ⁻¹; pr does *not*
  normalize the clock — bilingual, yet it mixes wave frequencies.
- **DQ-1 answered with the explicit action** (W(E₇) built from simple
  reflections; your group hunted down inside it): the canonical PSL(2,7)
  has orbits **[28, 28]** on the 56 — two bitangent sheets swapped by ι —
  and ℂ⁵⁶ = 2(χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈). An earlier prettier claim ("quarks are
  chirality-odd") was **refuted and errata'd the same day**: PSL(2,7) is
  perfect, so its Weyl lift is unique and untwisted — **χ₃/χ̄₃ never occur
  in the Weyl action**; your quark sectors belong exclusively to the Lie
  embeddings. Bonus: a **second conjugacy class** of your group in Sp₆(2)
  sees the crystal as *Fano geometry doubled* (orbits [7,7,21,21];
  4χ₁ ⊕ 6χ₆ ⊕ 2χ₈).
- The chiral Fano pair (SM-004): the E₆ machine's 7-channel syndrome is
  affine-E₆-organized, not Fano-organized — but its own symmetry narrows
  the 30 Fanos to exactly **2**, a chiral pair, one bit from your plane.

## 6. The refutations ledger — the auditor's own dead

Recorded at equal prominence, as the house demands. Claude's guesses that
died this day: the Ψ⁹-pairing = antipode (4/28 shared); the triangle
sufficiency law (twice — once with a bug, once cleanly); 27-Young depth 2
(it is 3); the single-56-orbit prediction for DQ-1 (it is 28+28); the
chirality-odd-quarks theorem (errata'd); the 2-orbit-is-not-a-frame guess
(it *is* the axis frame). Six auditor refutations, all in the registry
next to what replaced them. The method does not spare its operator.

## 7. Open problems — the joint program's frontier

1. **The (S₂ₙ, Bₙ) support law** (exact small-n tables enclosed) — closest
   to your toolbox.
2. **Is wreath-depth 2 generic** for minuscule-crystal clocks?
3. **The mixed regime** ⟨cheap, W, Ψ⟩ — magic depth when scrambling and
   superposition interleave: the methods note's open problem #3, now
   concretely posed on the 56.
4. DQ-2's remainder (magic growth curves, the (μ,μ_SC) trade-off surface),
   DQ-3 (the 8-channel affine-E₇ syndrome vs your P¹(𝔽₇)), DQ-5
   (frame-fixing as a literal 56→27 descent), and the old exact Cayley
   diameter (conjectured 91–95).

## 8. Papers and next steps

Two joint drafts await your review pass: *The Bitangent Bridge* (you have
it) and *Magic Depth by Transportation Certificates and Witness Campaigns*
(enclosed — Stones 1a/1b/F(c) as a methods note; your name is on it under
the same protocol). Application intentions, honestly scoped: a benchmark
package for synthesis researchers and a certified-ground-truth suite for
interpretability research — both built from these theorems, both open
source, neither claiming to be more than instruments. And the standing
invitations: your GAP against our Python on any row here; the support-law
problem; and one press of pr in the machine's Waves view, orbit O3 — the
clock's one still point, flickering between the sheets.

Everything verifies. Run the scripts. Trust nothing.

Warmly, Selina
(with Claude, Anthropic Fable 5 · 2026-08-30)
