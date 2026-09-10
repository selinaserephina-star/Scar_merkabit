# Audit — Scar-Merkabit Verification Session (2026-09-08)

**Auditor:** Claude (Sonnet 5), independent session
**Date:** 2026-09-08
**Subject:** integrity and computational reproducibility of five sealed "stones" from the Selina/Claude ↔ Ilya Balashov correspondence (SM-027, SM-031, SM-035, SM-036, SM-037), plus the earlier Stone AP (SM-054)

---

## 1. Scope

This audit covers every computational claim independently re-executed in this session:

| Stone | Name | Package | Role |
|---|---|---|---|
| SM-054 | Stone AP — the clock's linear centralizer | `to_Ilya_CLOCK_CENTRALIZER_2026-09-07.zip` | Primary target (first audit) |
| SM-035 | G₂ still point | `to_Ilya_STILLPOINT_2026-09-01.zip` | Primary target (this audit) |
| SM-036 | Stone X — the turner | `to_Ilya_TURNER_2026-09-01.zip` | Primary target (this audit) |
| SM-037 | Stone Y — the β-register | `to_Ilya_BETA_REPLY_2026-09-02.zip` | Primary target (this audit) |
| SM-031 | Stone W — third shadow | `to_Ilya_THIRD_SHADOW_2026-09-01.zip` | Re-run as a dependency of SM-036 |
| SM-027 | Stone U — the choice theorem | `to_Ilya_STONE_U_2026-09-01.zip` | Re-run as a dependency of SM-037 |

It does not cover the correctness of framework-level premises cited from stones outside this list, nor any of the physical-interpretation material (crystal transitions, 1/π framing, flavon model) elsewhere in the correspondence — all explicitly parked or unsourced in the source documents themselves.

## 2. Method

For each target:
1. Verified the package's SHA256 against the sender's stated hash (whole-zip level, where available) and, where the package's own `SHA256SUMS.txt` was present, checked every file inside.
2. Read the verifier script to identify its inputs (cache files, data files) not shipped in the same package.
3. Located each missing dependency in whichever earlier package actually contained it, or — where no package contained a ready-made cache — regenerated it by running the earlier stone's own verifier script from a clean checkout.
4. Ran the target script fresh, independent of the machine it was authored on (Python 3.12, numpy, sympy).
5. Diffed the resulting output against the shipped `.log` file line-by-line.

## 3. Summary

| Stone | Result | Matches shipped log | Dependency needed | Dependency status |
|---|---|---|---|---|
| SM-054 (Stone AP) | 22 PASS / 2 disclosed FAIL | pass/fail set and key values match | `scar56_data.json` | found in `REPLY_2026-09-05` package |
| SM-035 | 32 PASS / 0 FAIL | **byte-identical** | none | — |
| SM-036 (Stone X) | 29 PASS / 1 disclosed FAIL | **byte-identical** | `_stone_u_cache`, `_stone_v_cache`, `_stone_w_cache/ts_subspaces.npz` | first two found in `REPLY_2026-09-05/DATA`; third **regenerated** by re-running SM-031's own verifier |
| SM-037 (Stone Y) | 17 PASS / 0 FAIL | **byte-identical** | `_stone_u_cache/kbar_120.npz` + 3 large `kbar_*` files | **regenerated** by re-running SM-027's own verifier (files were deliberately excluded from every shipped DATA envelope) |
| SM-031 (Stone W, dependency run) | 36 PASS / 0 FAIL | not compared (no shipped log available for this incidental run) | `_stone_u_cache`, `_stone_v_cache` | found in `REPLY_2026-09-05/DATA` |
| SM-027 (Stone U, dependency run) | 59 PASS / 0 FAIL | not compared (no shipped log available for this incidental run) | none (self-contained; rebuilds its own cache) | — |

"Byte-identical" means a line-by-line diff against the shipped `.log` file showed no differences other than line-ending style (CRLF vs LF), a UTF-8 BOM on the first line, and per-line timing annotations (`[t=…s]`).

## 4. Detailed findings

### 4.1 SM-054 — Stone AP (the clock's linear centralizer)

- File integrity: all 15 files in the package matched `SHA256SUMS.txt`.
- Missing dependency: `scar56_data.json`, not bundled in this archive; found in `to_Ilya_REPLY_2026-09-05.zip` (`DATA/scar56_data.json`).
- Independent run: **22 PASS / 2 FAIL**, matching the shipped tally exactly (`RESULT: 22 checks passed, 2 failed  FAILED: ['AP7', 'AP4d']`).
- The two failures are not concealed errors — both are framed in the script itself as registered predictions that turned out wrong, and both resolutions matched:
  - **AP7:** predicted best-agreement involution would share pr's structure; measured maximizer has the same score (1432/1540) but a different structural origin (the transposition of Ψ's own axis pair).
  - **AP4d:** brief's stated fixed-point spectrum for one class had a typo (4 instead of 0); measured value matches the character-theoretic prediction.
- Central claim reproduced: `C_{S₅₆}(Ψ) ∩ W(E₇) = {1}` — of the 69,984-element centralizer of Ψ, exactly one element (the identity) is linear; none of its 231 involutions is linear.

### 4.2 SM-035 — the G₂ still point

- File integrity: clean (one file's checksum line had a trailing CR that broke automated parsing; manually verified — matched).
- No external dependencies; the script is self-contained (hardcoded sealed character-table rows, built fresh from `P¹(𝔽₇)` generators).
- Independent run: **32 PASS / 0 FAIL**, output byte-identical to the shipped log.
- Central claims reproduced exactly:
  - PSL(2,7) ⊂ compact G₂, exhibited via an explicit rational invariant 3-form φ (14 nonzero coefficients of 35; `det(B_φ) = −2,239,488 ≠ 0`).
  - The invariant space is exactly 1-dimensional (character count of 1 and constructive projector rank of 1 agree).
  - The "two sevens" are different objects: the 8-point action decomposes as `1 ⊕ χ₇`, the 7-point Fano action as `1 ⊕ χ₆`, with `⟨π₇, χ₇⟩ = 0` — G₂'s seven is the deleted 8-point module, not the Fano seven.
  - Rowmotion on the independently rebuilt G₂ 7-crystal is a single free 7-cycle (order 7), exceeding the Coxeter number h(G₂) = 6; the cyclic sieving phenomenon holds against the predicted generating function.

### 4.3 SM-036 — Stone X (the turner), with SM-031 as a re-run dependency

- File integrity: clean (same benign trailing-CR pattern on one line; manually verified — matched).
- Dependencies: `_stone_u_cache` and `_stone_v_cache` (both located in `REPLY_2026-09-05/DATA`), and `_stone_w_cache/ts_subspaces.npz`, which was **not present in any shipped package**. Regenerated it by re-running SM-031's own verifier (`verify_stone_w_third_shadow.py`, from `THIRD_SHADOW_2026-09-01`) against the same two caches.
  - That incidental run itself produced **36 PASS / 0 FAIL** for SM-031 — a full independent reproduction of a stone not originally in scope, with no shipped log available for direct comparison, but internally consistent (registered expectation WB3 confirmed as claimed).
- With the regenerated cache in place, the SM-036 verifier ran clean: **29 PASS / 1 FAIL**, byte-identical to the shipped log.
- The one failure (`X6c`) is the disclosed "registered expectation INVERTED": the brief predicted the constructed map τ would be a 3-cycle on the three shadow classes; the computed result shows τ is instead a third outer involution (swaps vector ↔ K_spin, fixes K₃). The script's own diagnosis then constructs the corrected map τ′ = (reflection) ∘ τ, and independently verifies τ′³ is inner via a unique explicit intertwiner — reproducing the claimed order-3 outer automorphism.

### 4.4 SM-037 — Stone Y (the β-register), with SM-027 as a re-run dependency

- File integrity: clean.
- Dependency: `_stone_u_cache/kbar_120.npz` plus three large derived files (`kbar_elements.npy`, 174 MB; `kbar_orders.npy`; `kbar_signrow.npy`). None of these were present in any shipped package — the `REPLY_2026-09-05/DATA/README_DATA.md` explicitly documents that they were deliberately excluded ("Stone U cache WITHOUT kbar_elements.npy (174 MB)…"). Regenerated all four by re-running SM-027's own verifier (`verify_stone_u_2cover.py`, from `STONE_U_2026-09-01`) from the partial cache that was shipped.
  - That incidental run produced **59 PASS / 0 FAIL** for SM-027, matching the registry's stated tally for that stone, with no shipped log available for direct comparison but internally consistent.
- With the regenerated files in place, the SM-037 verifier ran clean: **17 PASS / 0 FAIL**, byte-identical to the shipped log, all eight registered expectations confirmed with none inverted.
- Central claims reproduced: β(g,h) is well-defined only as a lift-independent element that collapses to ±1 on commuting pairs; the "relator-sign class" replacement is shown machine-equivalent to a genuine splitting criterion on 105 sampled subgroup instances; at S₃ and D₈ the register is shown to be exactly the ε-restriction relabeled; a discriminating C₄×C₂ pair is exhibited (identical all-plus ε-profile, opposite β); no spine group (20 sealed witnesses + trivial cases) contains a C₄×C₂, so the new content is confined off-spine.

## 5. Cross-cutting observations

- **Undocumented cross-package dependencies are the norm, not the exception.** Of the five primary/incidental verifiers re-run this session, four required cache files absent from their own package; in two cases (SM-036, SM-037) the needed file did not exist in *any* shipped package and had to be freshly regenerated by re-running an earlier stone's verifier. None of the cover notes flag these dependencies explicitly.
- **The `kbar_*` exclusion is deliberate and documented** (`README_DATA.md`), but its downstream effect — that SM-037 cannot be re-run from any combination of shipped material without also re-deriving ~180 MB of intermediate data — is not mentioned anywhere in the SM-037 package or cover notes.
- **A recurring benign artifact:** several `SHA256SUMS.txt` files across different packages have a stray trailing carriage return on their last data line, which breaks `sha256sum -c`'s automatic parsing for that one line. In every instance checked (four separate packages, four different files), manual verification confirmed the hash still matched — this is a line-ending quirk from the sending side, not evidence of tampering.
- **Duplicate uploads:** several zips uploaded to this conversation were byte-identical re-downloads of the same package under different filenames (`ROOF_CLOCKS_2026-09-06` / `-1`, `TWO_REGISTERS_2026-09-01` / `-1`, `THIRD_SHADOW_2026-09-01` / `-1`, `STONE_U_2026-09-01` / `-1`, `ROOF_2026-09-01` / `-1`, `CONTAINMENT_2026-08-31` / `-1`).

## 6. What this audit does and does not establish

**Established:** all five re-executed scripts are internally consistent, run cleanly on a machine independent of the one they were authored on, and reproduce their own claimed numeric output — including, in three of five cases, byte-for-byte identical console output. Where a script's own registered predictions failed (Stone AP's two, Stone X's one), the failures are self-disclosed in the code and documentation, not something this audit discovered independently — but re-execution confirms those disclosures are accurate rather than glossed over.

**Not established by this audit:**
- The correctness of framework-level premises these scripts cite from stones outside this list (e.g., SM-001's sealed character table, SM-012's cycle-type census) — those were taken as given inputs, not re-derived from scratch.
- Any interpretive or physical-identification material elsewhere in the correspondence, which the source documents themselves mark as parked, unsourced, or [I] (interpretive, not computed).

## 7. Verdict

All three previously-unreachable stones — SM-035, SM-036, SM-037 — are now independently reproduced from a clean checkout, including two additional dependency stones (SM-031, SM-027) reproduced as a byproduct. File integrity is clean across all six packages involved. Every self-reported failure or inversion in the source material matches what independent re-execution produces; nothing found here contradicts the packages' own account of their results.

## 8. Outstanding (not addressed by this audit)

- Direction and publication decisions — carried over unchanged from the 2026-09-06 acceptance note.
- The interpretive material parked under Rule 3 across the batches (1/π framing, crystal-ladder identifications, flavon/Yukawa layer) — untouched by this or the prior audit.
