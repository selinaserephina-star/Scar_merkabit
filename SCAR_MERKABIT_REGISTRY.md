# SCAR–MERKABIT JOINT REGISTRY

**The single source of truth for the joint world. Founded 2026-08-30.**
Parties: **Selina Stenberg** (Merkabit / E₆-crystal lane) and **Ilya Balashov**
(Scar-Cat / PSL(2,7) lane), with Claude. This lane is where the two programs
meet; it governs itself (see `knowledge.yaml`, the lane KCP) and inherits the
shared house rules both sides now run on:

> **Compute, never assert. Refutations at equal prominence — including the
> auditor's own. Mathematics split from identification (Rule 3). Every
> decimal match is a fit until proven derived. Every emergence claim needs a
> control. Backport rule (T-SC-P1): a downstream falsification must reach
> the upstream registry within one revision.**

Grades: [P] proved here/classical (cited) · [C] computed exactly by a named
script · [obs] observation not located in the literature · [I] role/
interpretation · [OPEN]. Joint-lane rule: **a unit is JOINT once both
parties have seen it; sends and publication require both parties' word.**

## Sealed units

| id | unit | result | grade | artifacts |
|---|---|---|---|---|
| SM-001 | **Scar-Cat registry audit** (T-SC) | PSL(2,7) rebuilt twice from scratch; character table DERIVED (Burnside–Dixon) and verified exactly in ℚ(√−7); **35+ "GAP" rows of Ilya's registry independently confirmed**, 9 classical; his note-7 self-audit credited in full. 48 checks. | [C] | `TSC_SCARCAT.md`, `verify_tsc_scarcat.py` |
| SM-002 | **Corrections R-SC-1..5** | T4-Higgs channel count 4 not 5 (⟨χ₃²,χ₁⟩=0); MOLIEN-REC fails for χ₆ (+ char.poly typo); 140's cube contains χ̄₃; 125's "7×ℤ₇⋊ℤ₃" → 8; **λ=1/8 ⇒ m_H=123.11 GeV ≈13σ hidden failure**. Each with a GAP one-liner in the report. | [C] | same + `to_Ilya/Scar_Cat_Verification_Report` |
| SM-003 | **The bitangent bridge** (T-BR) | Field level: ℚ(ζ₂₁) = compositum of the two character fields (√−3, √−7; √21 forced), linearly disjoint. E₆ level: no-go (7∤51840; no transitive 27-action). E₇ level: in Sp₆(2)=W(E₇)/± on the Klein quartic's 28 bitangents, **W(E₆) = stabilizer of one bitangent, PSL(2,7) transitive on all 28, intersection = S₃ = N(⟨z₃⟩)** — Ilya's universal stabilizer = the T4 strata S₃ = the E₆ machine's type group; 3A → bitangents exactly 2:1 (56=2×28); PSL fixes one even theta char (stab 8!; even orbits **[1,7,7,21]** [obs]); π₂₈ = χ₁⊕2χ₆⊕χ₇⊕χ₈. Lie level: 27\| = 3χ₁⊕3χ₈ (trinification/Klein χ₃) or 6χ₁⊕3χ₇ (G₂); "=2χ₈" refuted. **Closes Ilya's open "Bridge" conjecture row.** 20 checks. | [C]/[P] | `TBR_BRIDGE.md`, `verify_tbr_bridge.py`, `to_Ilya/The_Bridge_Report` |
| SM-004 | **The chiral Fano pair** | The E₆ architecture's 7-channel syndrome is NOT Fano-organized (motion group = S₃: pr rotates legs, ξ flips, Ψ inert; incidence = affine E₆ tree) but is **one bit away**: of 30 Fanos exactly 2 invariant — a chiral pair sharing the 3 centre-lines, swapped by inner/outer duality [obs]. 14 checks. | [C] | `verify_fano_syndrome.py` |
| SM-005 | **THE RESURRECTION THEOREM** (DQ-6) | E₆-branching of E₇'s 56 = **27 ⊕ 27̄ ⊕ 1 ⊕ 1**; the odd gate pr (1²·2²⁷) fixes exactly the two singlets and cross-pairs the sheets; the antipode ι is a second, inequivalent duality (3/27 pairings shared); Ψ crosses the wall. **v1's dual-spinor picture, refuted at E₆ (Thm 3.3), is TRUE at E₇.** Corollary (DQ-2, partial): **pr and ι are bilingual** (μ_branch = μ_frame = 0); the clock is the sole magic source (μ_branch(Ψ)=21/56, μ_frame(Ψ)=27/56) — *structure is free; only time is expensive.* 12 checks. Includes one refuted auditor guess (Ψ⁹-pairing ≠ ι-pairing, 4/28). | [C] | `verify_dq6_resurrection.py`, `scar56_data.json` |
| SM-006 | **The 56-State Machine** (instrument) | Interactive simulator of the joint architecture: mirrored two-sheet board hinged on the pr-axis vacua; frame view (28 ι-frames × chirality); both magic meters exact (μ_frame via true 28×28 assignment, validated against scipy); parity lamp; clock census. All tables emitted by the DQ-6 verifier. Published (private) at claude.ai/code/artifact/a7d069f2-be97-45fa-b5af-6524e858eb82. | [C] instrument | `artifact_56/machine56.html` |
| SM-007 | **The 56-machine design brief** | The joint architecture: 28 frames × chirality bit; three gate families (clock / odd mirror / antipode); two-axis resource theory (μ_typed, μ_SC); design questions DQ-1..5 (DQ-6 answered → SM-005; DQ-2 partial). | [I]+[C] anchors | `56_MACHINE_BRIEF.md` |
| SM-008 | **Joint paper draft v0.1** | *The Bitangent Bridge* — Stenberg · Balashov (co-authorship confirmed by Selina 2026-08-30): §§1–9 incl. §7½ resurrection + bilingual gates; §8 separates classical skeleton from [obs] items. Awaiting Ilya's review pass + joint bibliography. | draft | `joint_paper/Bitangent_Bridge_DRAFT.md/.docx` |
| SM-009 | **Stone 1: the transportation certificate generalizes** | Abstract certificate stated (Young double cosets = contingency tables; depth-k = finite table-closure; exact, no parity lemma over full Young/wreath). Anchor: 27-wreath depth 2 ✓ = CN-012; NEW: 27-Young depth = **3** (auditor's expectation refuted — the typed S₃ is worth one magic gate). THE EXPERIMENT: 56 branch grammar — Young depth = **5**; with sheet-swap (= pr, bilingual) typed: depth = **2** (the mirror is worth three magic gates). Frame grammar mapped to the Gelfand-pair frontier (Ψ coset type [9,9,9,1]; pr, ι type-trivial). Open: is wreath-depth 2 generic? 9 checks. | [C] | `STONE1_CERTIFICATE.md`, `verify_stone1_certificate.py` |
| SM-010 | **Stone 1b: hyperoctahedral calculus + the second depth-2 theorem** | Frame grammar reduced to coset-type dynamics on p(28)=3718 partitions (Gelfand pair (S₂ₙ,Bₙ)). Triangle inequalities proven NECESSARY (exhaustive n≤7); two auditor law-guesses refuted (triangle-exact; d-interval — 258 exact-table failures like (2,2)∘(2,2)↛(3,1)); reduction validated vs matching-BFS 4/4; exact n≤7 support tables = data for the open (S₂ₙ,Bₙ) connection-coefficient support problem. **THEOREM: frame-grammar magic-depth of the 56-machine = EXACTLY 2**, by 3718 explicit machine-verified witnesses (1606 sampled + 2039 annealed + 73 by dual-direction orbit sampling; 0 invalid; cache `stone1b_witnesses.json`). Combined with SM-009: **depth 2 in BOTH grammars** — two ticks of the clock reach every grammar class either way. | [C] | `STONE1B_HYPEROCT.md`, `verify_stone1b_hyperoct.py`, `verify_stone1b_stragglers.py`, `verify_stone1b_close73.py`, `stone1b_witnesses.json` |
| SM-011 | **Methods note draft v0.1** | *Magic Depth by Transportation Certificates and Witness Campaigns* — Stenberg · Balashov (same review protocol as the bridge paper): the abstract certificate (Thm 2.1), the four depth results with symmetry exchange rates, the frame-grammar theorem by 3718 witnesses, the four lessons, released benchmarks/tables/witness cache, three open problems (support law; wreath-depth-2 genericity; unitary generalization). Companion paper to *The Bitangent Bridge*. | draft | `joint_paper/Magic_Depth_Methods_DRAFT.md/.docx` |
| SM-012 | **Stone F(a): the field machine** | The linear lift ℂ⁵⁶: standing-wave spectrum of Ψ exact (all 18th roots, mult 3; ±1 mult 4); **the CSP census = the spectral trace formula** — the founding standing-wave intuition proved in its computational reading. Sector masses exact (all waves sheet-balanced; O2 carries the vacua 1/18 each); **all 28 frames live inside single clock orbits** [obs]; **the clock's 2-cycle IS a cross-sheet ι-frame — its axis** [obs, auditor guess refuted]; **DQ-4 CLOSED** (ιΨι=Ψ⁻¹; the 4 shared pairs = one axis pair per orbit); **pr does not normalize the clock** — bilingual yet frequency-mixing: a third notion of "structured" [obs]; ι = +1 on E₊₁, −1 on E₋₁; **Scar field sectors: ι-even = χ₁⊕2χ₆⊕χ₇⊕χ₈, ι-odd = χ₃⊕χ̄₃⊕2χ₇⊕χ₈ — quarks are chirality-odd, vacuum chirality-even** [obs, character level]. 13 checks. | [C] | `STONEF_FIELD.md`, `verify_stonef_field.py` |
| SM-013 | **Stone F(b): DQ-1 ANSWERED + the SM-012 erratum** | W(E₇) built on the 56 weights from simple reflections (order 2903040 verified; ι = −1 central); explicit **bridge-class PSL(2,7)** hunted down in the pair action (transitive on 28) and lifted canonically (perfect part of 2×L₂(7)). **DQ-1: orbits [28,28]** — two bitangent sheets interchanged by ι, weight-stabilizer S₃; the registered single-56-orbit prediction REFUTED. **Erratum to SM-012** (backport rule): ℂ⁵⁶ = 2(χ₁⊕2χ₆⊕χ₇⊕χ₈) — the untwisted lift is UNIQUE (PSL(2,7) perfect), the ι-odd half ≅ even half, **quark sectors χ₃/χ̄₃ do not occur in the Weyl action at all** (they belong to Lie-group embeddings only). Bonus [obs]: **second conjugacy class** of PSL(2,7) found — acts on the crystal as Fano geometry doubled (orbits [7,7,21,21]; 4χ₁⊕6χ₆⊕2χ₈). 11 checks. | [C] | `verify_stonef_b_dq1.py`, erratum in `STONEF_FIELD.md` |
| SM-014 | **Stone F(c): the quantum lift — first unitary certificate** | The chirality-beam-splitter machine on ℂ⁵⁶ (cheap = frame permutation unitaries; magic = W = Hadamard on every ι-pair). Exact local algebra ⟨H,X⟩ = D₁₆ over ℤ[√2] (H-lengths [0²,1⁴,2⁴,3⁴,4²]; k(−I)=4; H-parity a homomorphism). **CERTIFICATE: W-depth = max local H-length, with a global H-parity superselection charge** — verified for EVERY element of the n=2 (256) and n=3 (6144) machines vs ground-truth BFS. 56-theorems: group = parity-locked (D₁₆)²⁸⋊S₂₈, order 2·8²⁸·28! ≈ 1.18e55; **W-depth = exactly 4**. Frontier located: Ψ moves the Hadamard blocks off the ι-pairs — the MIXED regime (clock + beam-splitter) is where open problem #3 lives, now precisely posed. Depth ladder of the day: Ψ-depth 2 (both grammars) < W-depth 4. 12 checks. | [C] | `STONEF_C_QUANTUM.md`, `verify_stonef_c_quantum.py` |
| SM-015 | **Stone Q: the Clifford transport** | Sp₆(2) = W(E₇)/± **IS the 3-qubit Clifford group mod phases and Paulis** — identity exhibited computationally (both sides from scratch, same matrix group in shared coordinates). The bridge transported: 28 bitangents = the 28 **odd Pauli sign-functions**; W(E₆) = the Clifford stabilizer of one; PSL(2,7) = a Clifford subgroup transitive on all 28 (fingerprint [28]/[1,7,7,21]/S₃ lands intact); the Coxeter clock = the 7-gate circuit **H1·CX13·S1·H2·H3·CX23·CX12**. MEMBERSHIP BOUNDARY: **Ψ has NO Clifford shadow** (ιΨι=Ψ⁻¹ vs central ι — the true clock is nonlinear, it does not even act on the 28 pairs), pr ∉ W(E₇) (odd vs even image), ι ↦ 1 (chirality erased). **SHADOW COLLAPSE: shadow magic-depth = 1** (H-orbits [1,27], two double cosets, 51840+51840·27=1451520 exact) — the depth-2/W-depth-4 structure lives STRICTLY ABOVE the Clifford quotient ⇒ open problem #3 cannot be won in the quotient; certificates for Clifford+T must engage the unitary level. Auditor's registered expectation q(r)=ℓ_v(r)=0 **REFUTED**: both = 1, the pair forms descend by CANCELLATION (the 56 weights are exactly the shifts that repair the descent). [obs]: all 64 phase-point operators share one spectrum — the Arf split is orbit-theoretic, not spectral. 35 checks. | [C]/[P] | `STONEQ_CLIFFORD.md`, `verify_stoneq_clifford.py`, `BRIEF_STONEQ_CLIFFORD.md` (+lock), fail-first log |
| SM-016 | **Stone R: the altitude** | The **linearity gap** ν(g) = min d_H(g, W(E₇)) computed EXACTLY by full enumeration (2,903,040 elements, BSGS transversal chain [56,27,16,10,6,2]). **ν(pr) = 2**: the unique nearest Weyl element differs at pr's two fixed points = the E₆ vacua — **pr∘(vacuum swap) ∈ W(E₇)**, the mirror is one vacuum-trade from linear (the same swap SM-009's typed group needed). **Clock family flies high**: ν(Ψ)=38, ν(Ψ⁹)=36, ν(Ψ²)=ν(Ψ⁶)=44, ν(Ψ³)=46. TWO auditor guesses refuted on the data (equal prominence, fail-first logs kept): Ψ's minimizers are NOT the disguised Coxeter class (they are [2¹⁰,6⁶], char poly x⁷+2x⁶−3x⁴−3x³+2x+1, at 38 vs Coxeter 42) and their 18 contact points are NOT one orbit (spread (2,4,5,7)). **The clock's own antipode**: every conjugator g (Ψ=gcg⁻¹, none in B₂₈ — all scramble chirality) gives gc⁹g⁻¹ = Ψ⁹ independent of g; its matching meets ι's in exactly the 4 axis pairs (SM-004's refuted guess becomes the right theorem); [obs] ι∘Ψ⁹ = involution [1⁸,2²⁴] fixing the 8 axis points. **Stone Q's two opens CLOSED**: one-spectrum [obs] explained (Pauli translations mix Arf classes — Clifford-with-Paulis transitive on all 64 phase points; the 36/28 split = a Pauli sign gauge choice); sign flips UNITARILY IMPOSSIBLE downstairs (tr A_c = 1 conserved) — chirality is a gauge bit, not an operator; the beam-splitter machine is purchasable only in the ℂ⁵⁶ lift. 17 checks. | [C]/[P]/[obs] | `STONE_R_ALTITUDE.md`, `verify_stone_r_altitude.py`, `BRIEF_STONE_R_ALTITUDE.md` (+lock), two fail-first logs |

## Open questions (the joint program)

- ~~DQ-1~~ CLOSED by SM-013: orbits [28,28]; the ± doubling is equivariantly trivial.
- **DQ-2** (remainder): magic growth curves; the (μ_typed, μ_SC) trade-off surface.
- **DQ-3**: the 8-channel affine-E₇ syndrome vs the P¹(𝔽₇) action.
- ~~DQ-4~~ CLOSED by SM-012 (ιΨι=Ψ⁻¹; 4 = one axis pair per clock orbit).
- **DQ-5**: frame-fixing as a literal 56→27 descent operation.
- **NEW (F-c)**: the mixed regime ⟨cheap, W, Ψ⟩ — magic depth when scrambling and superposition interleave (open problem #3, now concretely posed).
- **SHARPENED by SM-015**: open problem #3 cannot be won inside the Clifford quotient (shadow depth = 1); a Clifford+T certificate must engage the unitary level, where SM-014's W-certificate is the existing foothold.
- Inherited crystal opens: exact Cayley diameter (conj. 91–95), shortest pr/Ψ⁴ relation.

## Sends & publication status

- **CORRECTED 2026-08-30 (Selina's word: "I never sent anything besides
  the bitangent drafts and bridge drafts")**: sent to Ilya = **The Bridge
  Report + the Bitangent Bridge paper draft ONLY**. NOT yet sent: the
  Scar-Cat verification report (R-SC corrections), the 56-machine brief
  and artifact, the methods note, and all stone results (SM-009..SM-014).
  The earlier "most pieces sent" line was overstated; superseded here.
- **Publication intent recorded** (Selina, 2026-08-30: "publishing this is
  the way"): the paper to arXiv/OSF after Ilya's review pass; the lane to a
  public repo on the joint go. Until both words are in: DRAFT /
  sealed-not-sent.
- **SENT 2026-08-30 (Selina's word: "sent")**: the COMPLETE package
  (`Scar_merkabit_COMPLETE_2026-08-30.zip`, sha256 d74cdb64…d539, with
  cover note and compendium) went to Ilya. He now holds the full joint
  world: audit + corrections C1–C5, all theorems SM-001..SM-014, both
  paper drafts, all verifiers, the open problems. Awaiting his review
  pass and his word on publishing.
- The 56-Machine artifact is private; sharing its link is a send (not
  included in the package — Selina's separate call).

## Changelog

- **v0.14 (2026-08-30)** — **Stone R run on Selina's "open up the
  exploration"**: SM-016 sealed (brief locked 57db98a7… before code;
  verifier 17/17; two fail-first logs). The altitude measured: ν(pr)=2
  (pr∘vacuum-swap ∈ W(E₇)) vs clock family 36–46; two auditor guesses
  refuted on the data; the clock's own antipode ι_Ψ = Ψ⁹ theorem; Stone
  Q's one-spectrum [obs] explained (Pauli sign gauge) and the unitary
  sign-flip obstruction proved (chirality = gauge bit downstairs). New
  distance axis ν (linearity gap) joins μ_typed/μ_frame/μ_SC.
- **v0.13 (2026-08-30)** — **Stone Q run on Selina's "Yes - go"**: SM-015
  sealed (brief sha-locked bb7a6822… BEFORE code; verifier 35/35;
  fail-first log kept). The bridge is now a 3-qubit Clifford statement;
  the true gates {Ψ, pr} proven to live above the quotient; shadow depth
  collapses to 1 ⇒ the depth program's boundary with genuine Clifford+T
  located as a theorem. One registered expectation refuted and recorded
  (descent by cancellation). ALSO staged this session: the tare-seals
  audit brief for the Coherence_tare lane
  (`../Merkabit_Scar/Coherence_tare/AUDIT_BRIEF_TARE_SEALS.md`, locked
  a63657ff…) — the audit session over TR-001..TR-017 is now executable
  by a fresh session on Selina's word.
- **v0.12 (2026-08-30)** — **The lane is on GitHub**: pushed to
  Selina's own PRIVATE repo github.com/selinaserephina-star/Scar_merkabit
  (created by her; 42 files incl. the sent zips and their recorded
  hashes; staging dirs excluded). Private = a version-controlled home,
  not a send — the two-party rule governs any future flip to public
  (Ilya's word required). Local folder remains the working copy;
  re-push after edits.
- **v0.11 (2026-08-30)** — **THE SEND MADE.** Complete package delivered
  to Ilya on Selina's word. The joint world is now fully two-party:
  everything sealed here is in both authors' hands.
- **v0.10 (2026-08-30)** — **Sends ledger CORRECTED on Selina's word**
  (only the two bridge documents were ever sent) and the **COMPLETE
  package built**: `package/Scar_merkabit_COMPLETE_2026-08-30.zip`
  (36 files, 1,305,365 bytes staged; zip 464,611 bytes, **sha256
  d74cdb6400ddc28ff431fe0025e64f0a074d589fcc3aa70496d4d0430f0d1539**),
  entry point = the NEW `to_Ilya/Joint_World_Compendium_2026-08-30`
  (.md/.docx): the full theorem compendium written for a reader who has
  seen only the bridge — audit summary, resurrection, depth theorems,
  field theorems, the auditor's six-refutation ledger, open problems,
  invitations. Manifest with all hashes + the 11 verification commands
  inside; zip hash in `package/COVER_COMPLETE_SHA256.txt`. Supersedes
  the v0.2 zip. Handing it over is the send — Selina's to make.
- **v0.9 (2026-08-30)** — **Stone F(d) done: the machine sings.** The
  56-State Machine artifact gained the **Waves view**: pick a clock orbit
  and harmonic, the standing wave is phase-painted onto the mirrored board
  (hue = phase; ▶ tick animates the global phase, reduced-motion
  respected); the axis frame O3 labelled; spec panels carry the day's
  depth ladder (Ψ-depth 2 / W-depth 4) and the field facts; the census
  strip is now captioned as the trace formula it is. Functionally
  verified live (orbit switching, harmonic re-capping, eigenvalue
  read-outs incl. ζ₁₈⁹ on the axis mode, gates unaffected). Same URL,
  version 'waves-view'. **Stone F complete: (a) spectrum, (b) DQ-1 +
  erratum, (c) quantum lift, (d) the panel.**
- **v0.8 (2026-08-30)** — **Stone F(c) done** (SM-014): the quantum lift.
  Parallel-magic unitary certificate PROVED-and-verified (max + parity
  superselection); 56 frame-quantum group order 2·8²⁸·28!, W-depth
  exactly 4; the mixed clock+splitter regime identified as the true open
  frontier. Remaining in Stone F: (d) the spectral artifact panel.
- **v0.7 (2026-08-30)** — **Stone F(b) done** (SM-013): DQ-1 closed
  ([28,28]); SM-012's chirality-odd-quarks claim REFUTED and errata'd in
  place (backport rule honoured same-day); second PSL(2,7) class found
  (Fano-doubled action). Two auditor predictions died in one stone —
  both recorded.
- **v0.6 (2026-08-30)** — **Stone F(a) done** (SM-012, "Stone F — go"):
  the field lift; CSP = standing-wave trace formula; the clock's axis
  frame; DQ-4 closed; pr frequency-mixing; chirality-odd quark sectors.
  Next: F(b) DQ-1 explicit action; F(c) the honest quantum lift; F(d)
  the artifact's spectral panel.
- **v0.5 (2026-08-30)** — **Methods note drafted** (SM-011) on Selina's
  word: Stones 1a+1b assembled into the second joint paper; awaiting
  Ilya's review pass alongside the bridge paper. KCP updated (methods
  note, stone docs, campaign scripts wired in).
- **v0.4 (2026-08-30)** — **Stone 1b done** (SM-010): the hyperoctahedral
  composition calculus built and validated; two law-guesses refuted on
  exact data; the (S₂ₙ,Bₙ) support law identified as the real open problem
  (our n≤7 tables = its data); and the SECOND depth-2 theorem — frame
  grammar, 3718/3718 verified witnesses. The 56-machine is depth-2 in both
  grammars. New open: the hyperoctahedral support law.
- **v0.3 (2026-08-30)** — **Stone 1 run on Selina's "lets run it"**: SM-009
  sealed (see row). Three new theorems on first contact: 27-Young depth 3,
  56-Young depth 5, 56-wreath depth 2; the S₃ buys one gate, the mirror
  buys three; certificate method transfers unchanged in the Young/wreath
  regime; hyperoctahedral frontier mapped. New open added: "is wreath-depth
  2 generic for crystal clocks?"
- **v0.2 (2026-08-30)** — **Package for Ilya prepared** on Selina's word:
  `package/Scar_merkabit_2026-08-30.zip` (20 files, 267,442 bytes staged;
  zip 144,023 bytes, **sha256
  c4194b93ac8bc58afe4b046da5e582058ab8e259937bd52c37eea0f8cfaf727b**),
  containing the full lane + `MANIFEST_SHA256.txt` (per-file hashes + the
  94-check verification commands); zip hash kept outside the archive in
  `package/COVER_SHA256.txt`. Handing the zip to Ilya is a send — Selina's
  to make; recorded here when made.

- **v0.1 (2026-08-30)** — Registry founded; units SM-001..SM-008 consolidated
  from Corpus_triage changelog v0.20–v0.25 (where this lane's history lived
  before it became self-governing); KCP `knowledge.yaml` created (joint
  authority: external sharing requires BOTH parties). Prior history remains
  readable in `../Corpus_triage/TRIAGE_REGISTRY.md`; from v0.1 on, this lane
  records itself here.
