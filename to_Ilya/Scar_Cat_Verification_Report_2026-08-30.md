---
title: "Scar-Cat Master Registry — Independent Verification Report"
subtitle: "An outside re-computation of the PSL(2,7) core, with five corrections and one new experimental comparison"
author: "Selina Stenberg, with Claude (Anthropic Fable 5)"
date: "2026-08-30"
---

Dear Ilya,

This summer I turned a hard audit on my own corpus — every claim recomputed
from scratch, refutations reported at the same prominence as confirmations.
It found real mathematics and it killed real claims of mine, and both
outcomes made the work stronger. This report does the same for the Scar-Cat
side, on the document we agreed to treat as the merged record:
`theorem_master_registry-27` (v4.9, May 2026, "196 proven"), read together
with your session note of 2026-05-22 (note-7).

Everything below was **computed, not asserted**, by the enclosed script
`verify_tsc_scarcat.py` (plain Python 3 + numpy — no GAP required, so it is
a genuinely independent check of your GAP results). It runs in seconds:

    python -X utf8 verify_tsc_scarcat.py

**Method.** PSL(2,7) was rebuilt twice, independently of your code and of
any tables: once as GL(3,𝔽₂) (all 168 invertible 3×3 matrices over 𝔽₂), once
as 2×2 matrices over 𝔽₇ modulo ±1. The character table was *derived* by the
Burnside–Dixon class-algebra method (class-multiplication constants counted
directly from the group; simultaneous diagonalization; algebraic
identification of the eigenvalues) and then verified **exactly** — row
orthogonality in the ring of integers of ℚ(√−7), with rational arithmetic,
no floating point in any final claim. As an internal control, the derived χ₆
was cross-checked against the independently computed permutation character
on the 7 Fano points (χ₆ = fixₚₒᵢₙₜₛ − 1). Every Hom-multiplicity below is an
exact rational number that came out an integer, as it must.

---

## 1. The headline: your algebra core is verified

**More than 35 of the registry's GAP rows were recomputed here exactly, and
they are all correct.** In particular (registry IDs):

- **138 / Final-3**: Σ dim² = 168, Σ dim = 28.
- **113**: Frobenius–Schur indicators [1,0,0,1,1,1] — only χ₃, χ̄₃ complex.
- **112**: {χ₃, χ̄₃} is the unique Galois-conjugate pair.
- **80–83**: χ₆² = χ₁⊕2χ₆⊕χ₇⊕2χ₈; Sym²χ₃ = χ₆; χ₃⊗χ̄₃ = χ₁⊕χ₈ (no χ₇);
  χ₃² = χ̄₃⊕χ₆; the W⁺/W⁻ vertices unique; ⟨χ₈⊗χ₇, χ₈⟩ = 3.
- **132, 133**: No-Extension and EOM Hom-counts, all as stated.
- **CONF / FERM-3 / DARK-6 / MOLIEN-EXACT (pentaquark) / OBS**:
  ⟨χ₃ⁿ,χ₁⟩ = 0,0,1; ⟨χ₈³,χ₁⟩ = 3; ⟨χ₃⁶,χ₁⟩ = 6; ⟨χ₃⁵,χ₁⟩ = 0;
  ⟨χ₇ⁿ,χ₁⟩ = 0,1,2,15.
- **Final-2**: ⟨χ₈³, χ₆⟩ = 18. **77**: χ₆⊗χ₈ = χ₃⊕χ̄₃⊕2χ₆⊕2χ₇⊕2χ₈.
- **94, 114, 143, Bell, 144, 127**: all exact as stated
  (‖χ₈²‖² = 25, ‖χ₇²‖² = 15, ‖χ₆²‖² = 10; Sym²(2χ₈) → 3, Λ²(2χ₈) → 1;
  ⟨χ₆³,χ₁⟩ = 2).
- **100**: commuting triples |Hom(ℤ³, G)| = 5376 = 168·32, counted directly.
- **97**: 8 subgroups ℤ₇⋊ℤ₃ (= Sylow-7 count = |P¹(𝔽₇)|), and the
  14 = 7+7 order-24 subgroups constructed explicitly as point- and
  plane-stabilisers.
- **98 / ν-struct**: χ₈|ℤ₇ = [2,1,1,1,1,1,1]; χ₈|A₄ = [0,1,1,2]
  (the A₄ extracted as the commutator subgroup of an explicit S₄).
- **E-3**: your Cayley graph on {S, T, T⁻¹} is 3-regular with second
  eigenvalue 2.7913 < 2√2 = 2.8284 — the Ramanujan property confirmed
  numerically (and classically, Lubotzky–Phillips–Sarnak 1988).
- Arithmetic rows **118, Ext-4, 135, E-7**: 744·7 = 168·31 = 5208;
  196884 ≡ −12 (mod 168); 16744 = 299·56; genus 3; 336 = 2·168; 24 cusps.

This core is real, checkable mathematics and it survives an adversarial,
tool-independent re-derivation. It deserves to be said plainly.

A second group of rows is **correct but classical** — true and citable, but
standard facts rather than framework-specific evidence: 147 (Peter–Weyl),
149 (L(1,χ₋₇) = π/√7 is the class number formula), 150 (h(ℚ(√−7)) = 1),
128–129, 135 (Hurwitz), 157 (Aut(Fano) = PSL(2,7)), E-4, E-7. I'd suggest a
"Method: Classical" tag so readers can see at a glance which rows are load
from the literature and which are yours.

---

## 2. Five corrections (each checkable in GAP in one line)

These are offered in the spirit of your own registry rule — *"if you find
yourself writing 'obviously' — stop and verify"* — and of your S-4 row,
which kept a WRONG result on the books rather than deleting it.

For each, a GAP snippet using your own toolchain. Common preamble:

    t := CharacterTable("L3(2)");;  irr := Irr(t);;
    triv := TrivialCharacter(t);;
    chi3 := First(irr, x -> x[1] = 3);;
    chi6 := First(irr, x -> x[1] = 6);;

**C1 — Theorem T4 "Higgs-Guardian": the channel count is 4, not 5.**
The row claims Hom_G(χ₁, χᵢ⊗χᵢ) = 1 for i = 8, 3, 7, 6, 1 ("exactly
5 = g(3) unique Higgs decay channels"). But χ₃ is complex, so
χ₃⊗χ₃ = χ̄₃⊕χ₆ contains **no** singlet — the singlet lives in χ₃⊗χ̄₃.

    ScalarProduct(chi3*chi3, triv);   # returns 0, not 1

As stated the count is 4, and the "= g(3) = 5" identification falls with it.
(If the intended statement was χ₃⊗χ̄₃, the row needs restating and the count
argument re-examined, since then χ̄₃ contributes the *same* channel.)

**C2 — MOLIEN-REC is false as stated.** The row says *"ALL irreps follow
a(n) = d·a(n−1) + a(n−2) − d·a(n−3) … Confinement = initial conditions, not
different recurrence! Verified n = 1..13 all."* Computed exactly, the
recurrence holds for χ₁, χ₇, χ₈ and **fails for χ₆ and for χ₃/χ̄₃**:

    a := List([1..8], n -> ScalarProduct(chi6^n, triv));
    # [0, 1, 2, 10, 50, 286, 1682, 10030]
    # test n=4:  6*a[3] + a[2] - 6*a[1] = 13  <>  a[4] = 10

The reason is visible in the recurrence itself: its characteristic
polynomial is x³ − dx² − x + d = (x−d)(x²−1), so its roots are {d, +1, −1} —
and a(n) = (1/|G|)Σ χ(g)ⁿ obeys a linear recurrence whose roots are the
*distinct values of χ*. That works when the values are ⊆ {d, ±1, 0}
(χ₁, χ₇, χ₈), and cannot work for χ₆, which takes the value **2** on class
2A (order-4 recurrence needed), nor for χ₃ with its irrational values. Note
also the row's annotation "(char.poly = (x−d)(x²+1))" is inconsistent with
its own recurrence — (x²+1) would need χ to take the values ±i. The row also
contradicts MOLIEN-EXACT directly above it, which correctly says χ₃ obeys a
different recurrence. Suggested repair: state the theorem as *"a_χ(n)
satisfies the recurrence with characteristic roots = distinct values of χ;
for χ₁, χ₇, χ₈ this is (x−d)(x²−1)"* — which is both true and prettier.

**C3 — Theorem 140 / Final-1: the cube contains the conjugate.**
χ₃³ = χ₁ ⊕ **χ̄₃** ⊕ χ₇ ⊕ 2χ₈ (not χ₃):

    ScalarProduct(chi3^3, chi3);                      # 0
    ScalarProduct(chi3^3, ComplexConjugate(chi3));    # 1

Colour-singlet uniqueness and dim = 27 stand; only the 3-dimensional
summand's label needs fixing.

**C4 — Row 125 contradicts row 97; 97 is right.** 125 says "7 × Z₇⋊Z₃",
97 says 8. The Sylow-7 count is exactly 8:

    g := PSL(2,7);;  Index(g, Normalizer(g, SylowSubgroup(g, 7)));   # 8

(Computed here from first principles: 48 elements of order 7, 6 per Sylow
subgroup → 8 subgroups, each with normalizer of order 21.) Row 125's "7×"
should read "8×".

**C5 — "Higgs-Rig" λ = 1/8 is experimentally excluded at ≈13σ.** This is
the important one, because it is a *hidden failure* in exactly the sense
your note-7 defined: percent-level agreement masking incompatibility. With
the standard convention m_H² = 2λv²:

    λ = 1/8  ⟹  m_H = √(2·0.125) · 246.22 = 123.11 GeV
    measured: m_H = 125.25 ± 0.17 GeV  ⟹  ≈ 13σ

(Equivalently: measured λ ≈ 0.129, i.e. 3.5% above 1/8 with ~0.3%
experimental precision.) The Hom-count parts of 141 are true and verified;
the physical equality λ = 1/8, carried as Status A "protected", is dead at
current precision. Note-7 tested eleven predictions; this one was not among
them. It belongs in the same table as M_Z (210σ) and sin²θ_W (11σ).

---

## 3. The registry needs a backport rule

Your note-7 of 2026-05-22 is, frankly, the best document in the folder — a
genuine self-audit that reports falsifications at full prominence: no
PSL(2,7) signature around Riemann zeros; the wells are universal Gaussians;
the RH bridge identity is the classical Riemann–von Mangoldt explicit
formula; M_Z fails at 210σ, sin²θ_W at 11σ, η_B at 3.4–5.3σ; Theorem 160 at
613×; Ω_Λ = 28/41 in ~2σ tension with DESI DR2. That is exactly the
discipline my audit lane runs on, and you got there independently.

But the registry — the document that calls itself "the authoritative record
of proven results" — was frozen on 2026-05-15 and never corrected against
note-7. A reader who receives only the registry receives claims your own
audit had already killed a week after it froze. Two suggestions, adopted
from what worked on my side:

- **An errata section inside the registry itself**, where refutations sit at
  the same prominence as theorems (your S-4 "WRONG" row shows you already
  believe in this — it just needs to be systematic, and to live where the
  original claims live).
- **A backport rule**: any downstream falsification (note-7, this report,
  future tests) must be reflected in the registry within one revision.

Housekeeping caught in passing: the changelog contains two corrupted rows
(dozens of entries concatenated into single lines; versions 3.6–4.3 appear
twice); the header still says "Total proven: 153" while the changelog ends
at 196; S-4-sign appears twice with conflicting Status (A and B); and rows
with Method = Observational / Empirical / Structural sit in sections
governed by "Only PROVEN results enter this document" — they deserve their
own clearly-labelled section rather than deletion.

One more structural suggestion: rows like 145 ("DM idempotent encodes dark
energy"), 151 ("single polynomial encodes full SM") and 152–160 carry
Status A — unconditional mathematics — for statements whose arithmetic is
true but whose *encoding claims* are physical identifications. Splitting
each such row into "the mathematical fact (A)" and "the identification (B,
or conjecture)" would make the registry's genuinely unconditional core —
which is large and solid — stand out cleanly.

---

## 4. On the bridge numbers (briefly)

My audit reached the same verdict from both directions on the famous
matches, so recording it once here:

- **4/3**: dim(χ₈)/dim(χ₆) = 4/3 exactly — and my 4/3 entanglement
  threshold, and the crystal's antichain homomesy 4/3, are true statements
  about *three different objects*. Small fractions have a high coincidence
  base rate; the bridge needs a functor, not a fraction (your own "Bridge"
  conjecture row says exactly this: "explicit functor missing").
- **Ω_Λ = 28/41** appears in both corpora with *unrelated* derivations.
  Two grammars hitting one target is coverage, not confirmation — and
  note-7's DESI update weakens the target itself.
- **π²/27** likewise does double duty in both corpora; on my side the audit
  refuted "π²/27 = sin²θ_W" as an equality.
- The **Klein-quartic/Hecke bridge** (note-7 §5.5) is real and beautiful
  mathematics — and classical (Hecke 1928, Elkies 1999). Your own phrasing
  is the right one: "interpretation, not derivation."

The meta-finding after auditing both corpora end to end: in every case where
a controlled test was possible, "physics emerges" resolved into the
apparatus — and in every case, **the underlying finite group theory
survived**. On both sides. That shared, verified core (your PSL(2,7)
representation ring; my E₆ crystal dynamics) is the honest foundation, and
it is not small.

---

## 5. Enclosed

- `verify_tsc_scarcat.py` — the full verifier (Python 3 + numpy; 48 checks;
  the 2 designed FAILs are C1 and C2 above). Every claim in this report is
  a line of its output.
- On request: the complete audit thread (`TSC_SCARCAT.md`) and the whole
  Corpus_triage lane, including the eighteen threads that did to my corpus
  what this report does to the registry. The lane's founding rule, which I
  offer as the joint standard for the merged registry: *compute, never
  assert; refutations at equal prominence; identifications split from
  mathematics; every decimal match is a fit until proven derived.*

With respect for the work — the core holds, and that is rarer than it
sounds.

Selina
(prepared with Claude, Anthropic Fable 5, 2026-08-30)
