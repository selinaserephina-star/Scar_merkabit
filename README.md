# Scar_merkabit — the joint world (Stenberg × Balashov)

**Self-governing since 2026-08-30**: single source of truth =
[`SCAR_MERKABIT_REGISTRY.md`](SCAR_MERKABIT_REGISTRY.md) (units SM-001..);
machine-readable governance = [`knowledge.yaml`](knowledge.yaml) — the lane
KCP, with joint authority (external sharing requires both parties' word).

**Founded 2026-08-30** (moved out of `Corpus_triage`, threads T-SC and T-BR).
Everything that concerns *both* programs — the Scar-Cat/PSL(2,7) framework
(Ilya Balashov) and the Merkabit/E₆-crystal framework (Selina Stenberg) —
lives here: audits of the other side, the bridge mathematics, and the
packages prepared for sending.

House rules inherited from the audit lane: **compute, never assert;
refutations at equal prominence; mathematics split from identification
(Rule 3); every decimal match is a fit until proven derived.**

## Contents

| file | what it is |
|---|---|
| `TSC_SCARCAT.md` + `verify_tsc_scarcat.py` | **Thread T-SC** — independent audit of the Scar-Cat master theorem registry (v4.9, 196 claims). PSL(2,7) rebuilt from scratch, character table derived by Burnside–Dixon, verified exactly in ℚ(√−7). 35+ "GAP" rows confirmed; 9 classical; five refutations/corrections (R-SC-1..5), incl. a new 13σ hidden failure (λ = 1/8 ⇒ m_H = 123.11 GeV). 48 checks. |
| `TBR_BRIDGE.md` + `verify_tbr_bridge.py` | **Thread T-BR** — how the two frameworks fit together. Field level: the cyclotomic bridge ℚ(ζ₂₁) verified + sharpened (√−7 = Scar-Cat's character field, √−3 = the trit field, √21 forced; linearly disjoint). E₆ level: no-go (7 ∤ 51840). E₇ level: inside Sp₆(2) = W(E₇)/± on the Klein quartic's 28 bitangents, W(E₆) = stabilizer of one bitangent, PSL(2,7) transitive on all 28, **intersection = S₃ = N(⟨z₃⟩)** — Ilya's universal stabilizer = T4's canonical strata S₃; 3A → bitangents exactly 2:1 (56 = 2×28). Lie level: 27\| = 3χ₁⊕3χ₈ (trinification via Klein's χ₃) or 6χ₁⊕3χ₇ (G₂/octonions); the Bridge conjecture row closed. 20 checks. |
| `to_Ilya/` | The sendable packages: `Scar_Cat_Verification_Report_2026-08-30` (.md/.docx — the T-SC audit as a letter, corrections C1–C5 each with a GAP one-liner) and `The_Bridge_Report_2026-08-30` (.md/.docx — T-BR as a letter), plus both verifiers. **Send decision is Selina's; nothing here is published.** |

Both verifiers run with plain Python 3 + numpy (no GAP):

    python -X utf8 verify_tsc_scarcat.py
    python -X utf8 verify_tbr_bridge.py

## Registry

Thread verdicts and changelogs remain recorded in
`../Corpus_triage/TRIAGE_REGISTRY.md` (T-SC at v0.20–21, T-BR at v0.22,
the move at v0.23); this lane holds the artifacts. The related bedrock:
`../Merkabit_crystal/` (15 verifiers) and
`../Crystal_information/CRYSTAL_NATIVE_v2/` (the architecture paper),
private repo `selinaserephina-star/E6_ternary_architecture`; the public
audit of the Stenberg corpus:
`github.com/selinaserephina-star/Merkabit_corpus_audit`.

*Status: everything DRAFT / sealed-not-sent.*

## Added 2026-08-30 (second wave)

| file | what it is |
|---|---|
| `verify_fano_syndrome.py` | **The Fano-syndrome check** (14 checks): the E₆ architecture's 7-channel syndrome is NOT Fano-organized (motion group = S₃, native incidence = the affine E₆ tree) but is exactly ONE BIT away — its symmetry narrows the 30 Fanos to a chiral pair sharing the 3 centre-lines, exchanged by the inner/outer duality. Includes one refuted auditor guess (Ψ⁹-pairing ≠ antipodal pairing on the 56, 4/28 shared). |
| `56_MACHINE_BRIEF.md` | **Design brief for the joint architecture**: the E₇ minuscule 56 as the first object carrying both frameworks natively — her gates (Ψ order 18, odd pr, antipode ι), his grading (PSL(2,7) on the 28 frames, per-frame S₃), two-axis magic (μ_typed, μ_SC), design questions DQ-1..5. |
| `joint_paper/Bitangent_Bridge_DRAFT.md/.docx` | **Joint paper draft v0.1** — "The Bitangent Bridge", proposed co-authors Stenberg & Balashov: the no-go, the field shadow, the Sp₆(2) home, the S₃, the 2:1 double cover, both branchings, the chiral Fano pair; honest §8 separating classical skeleton from new observations. **Co-authored Stenberg–Balashov (confirmed by Selina 2026-08-30); sealed-not-sent pending Ilya's review pass.** |
