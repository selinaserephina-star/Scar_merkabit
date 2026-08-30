# T-SC — The Scar-Cat registry (Ilya's side of the merged corpus)

**Thread:** T-SC · **Date:** 2026-08-30 · **Verifier:** `verify_tsc_scarcat.py`
**Source under audit:** `Desktop/Ilya/theorem_master_registry-27 (1).md`
(Scar-Cat Master Theorem Registry, Ilya Balashov, v4.9, May 2026; 196 claimed
proven theorems, PSL(2,7) framework), read together with
`scar_merkabit_session_note-7.md` (Ilya's own predictions audit, 2026-05-22)
and the May 2026 registry-merge documents.

**Commissioned by Selina:** "now do Ilyas side? … take an audit look at his
stuff as well like the session." Same house rules as every thread: compute
never assert; refutations at equal prominence; split mathematics from
identification (Rule 3); decimal matches are *fit until proven derived*.

**Method.** No GAP, no lookup tables. PSL(2,7) was rebuilt twice from
scratch — as GL(3,𝔽₂) (168 matrices over 𝔽₂) and as 2×2 matrices over 𝔽₇ —
and its character table was **derived** by the Burnside–Dixon class-algebra
method (class-multiplication constants counted from the actual group, common
eigenvectors → central characters), then verified **exactly** (orthogonality
in ℚ(√−7) with Fraction arithmetic) and cross-checked against the
independently computed permutation character on the 7 Fano points. Every
Hom-count below is an exact rational computation. 48 checks pass; the 2
FAILs are refutations of registry rows.

---

## 1. Verdict at a glance

Same portrait as the Stenberg corpus, sharpened: **right numbers, wrong
addresses — and here, even the right numbers have bookkeeping errors.**

| Layer | Verdict |
|---|---|
| Representation-theory core (the "GAP" rows) | **VERIFIED-HERE** — 35+ rows recomputed exactly and independently; the algebra is real and solid |
| Three specific math rows | **REFUTED / CORRECTED** (T4 Higgs channels, MOLIEN-REC, 140's conjugate label, 125's subgroup count) |
| Physical identifications (SM sectors, DM, gravity, M-theory) | **PARKED** (Rule 3) — the bijection to physics is asserted, never derived |
| Decimal predictions | **fit until proven derived**; one **new 13σ hidden failure found here** (λ = 1/8); note-7's failures (M_Z 210σ, sin²θ_W 11σ, η_B) never backported |
| Planetary / DNA / consciousness / biology rows | **UNTESTABLE-AS-STATED or PARKED**; maximal look-elsewhere exposure |
| Registry hygiene | **NEEDS REPAIR** — corrupted changelog, stale header counts, duplicate rows with conflicting status, policy violations |

Ilya's own `session_note-7` (2026-05-22) is credited in full: it is a genuine
self-audit in the same spirit as this lane, and it found the M_Z / sin²θ_W /
η_B failures before we did. The problem is that the registry (frozen
2026-05-15) still asserts what the note killed a week later.

---

## 2. VERIFIED-HERE: the algebra core (recomputed exactly)

Character table of PSL(2,7), **derived** here (classes 1A,2A,3A,4A,7A,7B;
sizes 1,21,56,42,24,24):

| | 1A | 2A | 3A | 4A | 7A | 7B |
|---|---|---|---|---|---|---|
| χ₁ | 1 | 1 | 1 | 1 | 1 | 1 |
| χ₃ | 3 | −1 | 0 | 1 | (−1+i√7)/2 | (−1−i√7)/2 |
| χ̄₃ | 3 | −1 | 0 | 1 | (−1−i√7)/2 | (−1+i√7)/2 |
| χ₆ | 6 | 2 | 0 | 0 | −1 | −1 |
| χ₇ | 7 | −1 | 1 | −1 | 0 | 0 |
| χ₈ | 8 | 0 | −1 | 0 | 1 | 1 |

Rows reverified exactly (registry IDs): **138/Final-3** (Σd²=168, Σd=28),
**113** (FS = [1,0,0,1,1,1]), **112** (Galois pair), **80** (χ₆²), **81/141**
(Sym²χ₃=χ₆; χ₃⊗χ̄₃=χ₁⊕χ₈), **82**, **83/T2/T3** (W vertices unique; gluon
multiplicity 3), **132** (No-Extension), **133** (EOM), **FERM-3/146**
(⟨χ₈³,1⟩=3), **DARK-6** (⟨χ₃⁶,1⟩=6), **MOLIEN-EXACT's pentaquark**
(⟨χ₃⁵,1⟩=0), **OBS** ([0,1,2,15]), **Final-2** (χ₈³→χ₆ = 18), **77**, **94**,
**114**, **143** (25/15/10), **Bell** (3 and 1), **144**, **100** (commuting
triples = 5376 = 168·32), **97** (8 subgroups ℤ₇⋊ℤ₃; the 14 order-24
stabilisers constructed explicitly), **98** (χ₈|ℤ₇ = [2,1,1,1,1,1,1]),
**ν-struct** (χ₈|A₄ = [0,1,1,2]), **CONF** (⟨χ₃ⁿ,1⟩ = 0,0,1), **4/3**
(8/6 = 4/3, trivially exact), **10.8** (A₄ has no order-4 elements),
**152/154** (|3A| = 56), **135 & E-7 arithmetic**, **118 & Ext-4 arithmetic**
(744·7 = 168·31; 196884 ≡ −12 mod 168; 16744 = 299·56), **E-3** (the Cayley
graph over {S,T,T⁻¹} is 3-regular with second eigenvalue 2.7913 < 2√2 —
Ramanujan, classical LPS 1988, confirmed numerically here).

**This core deserves the same respect as the Stenberg crystal verifiers: it
is real, checkable mathematics, and it checks out.**

Classical-fact rows (correct but not new): 149 (L(1,χ₋₇)=π/√7 is the class
number formula), 150 (h(ℚ(√−7))=1), 147 (Peter–Weyl), 135 (Hurwitz 84(g−1)),
E-4, E-7, 128, 129 (Schur multiplier ℤ/2), 157 (Aut(Fano) = PSL(2,7)).
Verdict **CLASSICAL** — true, citable, not framework-specific evidence.

---

## 3. REFUTED / CORRECTED (mathematics, not interpretation)

**R-SC-1 · T4 "Higgs-Guardian" — refuted as stated.** Claim:
Hom_G(χ₁, χᵢ⊗χᵢ) = 1 for i = 8,3,7,6,1, "exactly 5 = g(3) Higgs decay
channels". Computed exactly: ⟨χ₃²,χ₁⟩ = **0** (χ₃ is complex; χ₃² = χ̄₃⊕χ₆
has no singlet — the singlet lives in χ₃⊗χ̄₃). The channel count as stated is
**4, not 5**, and the "= g(3)" numerology collapses with it.

**R-SC-2 · MOLIEN-REC — refuted as stated.** Claim: "ALL irreps follow
a(n) = d·a(n−1) + a(n−2) − d·a(n−3) … Confinement = initial conditions, not
different recurrence! Verified n=1..13 all." Computed n = 1..13: the
recurrence holds for χ₁, χ₇, χ₈ and **fails for χ₆** (a = 0,1,2,10,50,286,…;
χ₆ takes the value 2 on 2A, so the recurrence needs the root 2) **and for
χ₃/χ̄₃**. The row also contradicts MOLIEN-EXACT one line above it (which
says χ₃ has a *different* recurrence). And the annotated characteristic
polynomial "(x−d)(x²+1)" is wrong for its own recurrence — 
x³−dx²−x+d = (x−d)(x²−1); the roots must be character values {d, ±1},
which is exactly why χ₆ (value 2) escapes. The correct general statement:
a(n) obeys the linear recurrence whose roots are the distinct values of χ —
order 3 for χ₇/χ₈, order 4 for χ₆.

**R-SC-3 · Row 140/Final-1 — label correction.** χ₃³ = χ₁ ⊕ **χ̄₃** ⊕ χ₇ ⊕
2χ₈ (computed exactly). The registry writes χ₃ for the 3-dimensional summand;
the cube of χ₃ contains its *conjugate*, in either labelling convention.
Colour-singlet existence and dim 27 stand.

**R-SC-4 · Row 125 vs row 97 — internal contradiction, 125 wrong.** 125 says
"7 × Z₇⋊Z₃"; 97 says 8. Computed: the Sylow-7 count is exactly **8**
(= |P¹(𝔽₇)|), so there are 8 order-21 maximal subgroups. Row 97 is right.

**R-SC-5 · "Higgs-Rig" λ = 1/8 — NEW hidden failure (13σ).** The registry
carries "λ_SM = δ₃·δ₄ = 1/8, protected — Status A — LHC" (and 141 again as
"GAP-proved"). With m_H² = 2λv²: λ = 1/8 predicts **m_H = 123.11 GeV** vs
measured 125.25 ± 0.17 — **≈13σ**. (Measured λ ≈ 0.129, i.e. 3.5% above 1/8.)
This failure is *not* in note-7's list of eleven tested predictions — the
same "percent-level agreement masks experimental incompatibility" trap note-7
itself diagnosed for M_Z. The Hom-count parts of 141 are true; the physical
equality λ = 1/8 is experimentally dead at current precision.

---

## 4. The registry vs. Ilya's own note-7 (the backporting gap)

Note-7 (2026-05-22) is the best document in the folder: it reports
falsifications at equal prominence (no PSL(2,7) signature around Riemann
zeros; wells are universal Gaussians; the RH "bridge" identity is classical
Riemann–von Mangoldt; M_Z fails at 210σ; sin²θ_W at 11σ; η_B at 3.4–5.3σ;
Theorem 160 at 613×; Ω_Λ = 28/41 in ~2σ tension with DESI DR2). **House
credit, in full.**

But the registry (frozen 2026-05-15, "authoritative record of proven
results") still asserts what note-7 killed, with no errata layer:

| Registry row | Registry status | Note-7 / this audit verdict |
|---|---|---|
| θ₂₃ primary prediction | B, "JUNO 2027 ✓" | still pending (1.1σ tension) — fine |
| Ω_Λ = 28/41 "error 0.26%" | B | borderline-fail vs DESI+Planck (2.04σ); also PARKED by our T7 (same fraction, other derivation!) |
| Higgs-Rig λ = 1/8 | **A**, "protected" | **13σ fail (this audit)** |
| Theorem 160 mass hierarchy | listed under O.1 lineage | 613× fail (note-7; "already rejected internally") |
| sin²θ_W corrections (V.1) | "0.013% error" | the *other* formula (3/13) fails at 11σ; the corrected one is a moved target (grammar tracked the data) — same pattern as our T5 α audit |
| RH claims (via merged-registry docs: "STT unconditional") | RIGOROUS in Mapping 2026-05-21 | note-7: "Not proven … exactly the explicit formula of Riemann–von Mangoldt (1895), not new content" |

**Prescription (T-SC-P1):** the registry needs the same discipline as ours —
an errata section where refutations live *at equal prominence*, and a rule
that a downstream falsification (note-7) must be backported to the upstream
"authoritative record" within one revision.

---

## 5. Hygiene findings (the document itself)

1. **Corrupted changelog**: two giant rows are dozens of entries concatenated
   into single lines (copy-paste accidents); versions 3.6–4.3 appear twice.
2. **Stale header**: "Total proven: 153" atop a document whose changelog ends
   at 196.
3. **Duplicate row, conflicting status**: S-4-sign appears twice — once
   Status B, once Status A.
4. **Policy violation**: "Only PROVEN results enter this document" — yet
   Section V-G contains rows with Method = Observational, Empirical,
   Structural, and Status B fits; S-4-note ("WRONG") sits inside a theorem
   table. (To Ilya's credit, the WRONG rows are *kept and labelled* — the
   instinct is right; the sectioning is not.)
5. **Status inflation**: rows like 145 ("DM idempotent encodes dark energy"),
   151 ("single polynomial encodes full SM"), 156–160 carry **Status A
   (unconditional math)** for what are identifications. The arithmetic in
   them is true; the *encoding claims* are Rule-3 material and should be B at
   most, with the identification split out.

---

## 6. Shared numerology across the two corpora (bridge audit)

The merged-registry project (May 2026) recorded "12 EXACT numerical matches
between registries". The audit's reading of the three load-bearing ones:

- **4/3**: dim(χ₈)/dim(χ₆) = 4/3 (exact, trivial) vs the Stenberg 4/3
  entanglement threshold vs the crystal's |P|/h = 4/3 homomesy. Our T2
  verdict stands: three true statements about **three different objects**;
  a small fraction with high coincidence base-rate. Bridge REFUTED as
  identification, exactly as before.
- **Ω_Λ = 28/41**: appears in *both* corpora with *different* derivations
  (Ilya: 28/41 from T₇/idempotents; corpus: from the 41-object count). Two
  unrelated grammars hitting the same target fraction is coverage
  compounding, not confirmation — same lesson as the four α routes (T7).
- **π²/27**: mτ/mμ = (π²/27)·46 here; π²/27 ≈ 0.2312 ≈ sin²θ_W claims in
  both corpora (our T9 refuted "π²/27 = 0.231" as an equality). The same
  small-number grammar generating hits in two frameworks is the
  look-elsewhere effect wearing two hats.
- The Klein-quartic/Hecke bridge (note-7 §5.5) is real mathematics and
  **CLASSICAL** (Hecke 1928, Elkies 1999) — the honest statement is already
  in note-7: "interpretation, not derivation".

**Meta-finding, now cross-framework:** apparatus-not-architecture goes
**6-for-6**. Every controlled emergence claim in the Stenberg corpus resolved
into apparatus (T-M, T10, T11, T-Λ, T8b); on the Scar-Cat side the RH lane
resolved into the classical explicit formula (note-7's own control) and the
SM lane's precision hits sit on unpriced grammar coverage. And in both
corpora, **the underlying finite group theory survives every test we can
throw at it.**

---

## 7. What to hand Ilya

1. This thread + `verify_tsc_scarcat.py` (runs anywhere, Python 3 + numpy,
   no GAP needed) — including the five R-SC corrections, which are the
   actionable part.
2. The suggestion to adopt the errata/backport rule (T-SC-P1) and fix the
   changelog corruption.
3. Credit where due: note-7 is a model self-audit; the registry core is
   sound; the "how to add a theorem" rule ("if you find yourself writing
   'obviously' — stop and verify") is house-discipline-grade.

Verdict tallies for the merged registry, Scar-Cat side: **VERIFIED-HERE 35+
rows · CLASSICAL 9 · REFUTED/CORRECTED 5 (R-SC-1..5) · PARKED all physical
identifications and decimal fits · UNTESTABLE-AS-STATED the Scar-Cat-functor
rows (F, g(n), σ(n), S = 6037 — internally consistent arithmetic, but the
functor's definition lives outside this registry) and the
planetary/DNA/consciousness family.**

*Draft; sealed-not-sent. Not pushed to the public audit repo: publishing an
audit of Ilya's work requires his (and Selina's) say-so first.*
