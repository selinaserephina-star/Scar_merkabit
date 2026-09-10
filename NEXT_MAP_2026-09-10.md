# NEXT MAP — Scar_merkabit lane, written 2026-09-10 night for the next session

**Read first, in this order:** `SCAR_MERKABIT_REGISTRY.md` changelog head
(v1.11) and Sends section; then this map; then the memory file. The
registry is the single source of truth; this map is a pointer and goes
stale the moment the registry moves.

## 0. Where things stand

- Registry **v1.11**, rows SM-001..SM-062, last commit 239f9ec. KCP
  refreshed after every bump (only the registry pin moves; the refresh
  prints "a signature made before this refresh is now stale — re-sign":
  we have never signed; ignore unless Selina asks to start).
- **Sealed today (2026-09-10):** SM-060 (D₅ anomaly on the 4-cube),
  SM-061 (homomesy), SM-062 (C = T on the grammar).
- **Two things PREPARED-NOT-SENT, waiting on Selina's word "sent":**
  1. `to_Ilya_C_EQUALS_T_2026-09-10.zip` (29bd45bf…, 135,721 B) — SM-062
     + summary §7.11 + the CHANNEL reply folded in + chirality
     exploration. On "sent": registry Sends entry → SENT + FROZEN, the
     CHANNEL reply's status line → sent inside it, changelog, knowledge
     bump, KCP, commit, memory.
  2. `to_Ilya_REPLY_ARCHIVE_2026-09-10.md` (2acd3f9f…) — answers his
     lepton archive; closes the checkpoint-audit ask; offers the
     discriminant audit. Same recording on "sent".
- **Pending from Ilya:** his word on SM-035/036/037/054 (promised 09-10,
  not yet arrived), then SM-055..062; his review of draft v0.2; the
  Defant–Hopkins literature check on the toggle-size homomesy; formal
  division of labour (yes in substance); his answer to the discriminant
  offer.
- **Draft:** `joint_paper/Roof_and_Clock_DRAFT.md` is v0.2 (§7.6, §7.7
  in). Four summaries exist as separate files and are NOT merged:
  §7.8 `SHARED_GRAMMAR_SUMMARY_2026-09-09.md`, §7.9
  `REVERSALS_SUMMARY_2026-09-09.md`, §7.10
  `ANOMALY_HOMOMESY_SUMMARY_2026-09-10.md`, §7.11
  `C_EQUALS_T_SUMMARY_2026-09-10.md`. Merge into v0.3 after his review
  pass (or on Selina's word before it), then the framing pass rules
  (`joint_paper/FRAMING_PASS_2026-09-09.md`) re-applied to the new
  sections: Rush–Shi cited at first use; no "clock = Coxeter number"
  without the reframe.

## 1. Candidate next stones (merkabit side unless marked)

Ranked by how much they would settle, not by ease.

1. **The D₅ anomaly by hand on the 4-cube** (open since SM-058/060). Sixteen
   vertices, W(B₄) of order 384, clock of order 8, half-turn shared grammar
   dihedral of order 8 with four extras. Everything computed; nothing
   understood. A proof or a mechanism would close the family's one
   exception. Start from `STONE_AV_D5_ANOMALY.md` §4 and
   `_explore_d5_probes_2026-09-10.py`. Also open: whether the anomaly
   relates to D₅ being a non-central-reverser board (SM-062 §7.11.4).
2. **The discriminant audit** (Scar side, ONLY if Ilya says yes to the
   offer). Rebuild det(Y_T) from
   `RECEIVED_2026-09-10_IB_PSL27_TO_PMNS_ARCHIVE/archive_bundle/outputs/CANONICAL_BLOCK.md`
   (never run his code; reimplement from the stated matrices), recompute
   windings w(α₂)=1, w(β₃)=2, w(γ₁)=0 by the argument principle, test:
   β₃-dependence of degree exactly 2; D constant in γ₁ identically. Brief
   locked before code; guesses = his three numbers.
3. **C = T on the 27** (SM-062 §5): the reverser w₀(E₆) is non-central and
   induces 27 ↔ 27̄; what does it do to a PSL(2,7) or S₄ inside W(E₆)?
   Needs a PSL(2,7) copy in W(E₆) (order 51,840 = U₄(2).2 — does it contain
   PSL(2,7)? check: U₄(2) order 25,920 has no element of order 7 → NO
   PSL(2,7) in W(E₆); so the question becomes S₄/A₄ copies, or is void —
   settle that in the brief before staging).
4. **The clock as a T-gate** (merkabit open problem #3 from the 56-machine
   brief `56_MACHINE_BRIEF.md`): with SM-057 (⟨W,Ψ⟩ = A₅₆, Clifford-like W
   with one non-Clifford Ψ) the analogy is precise enough to brief.
5. **Non-linear reversers on the five boards** (A₃ω₂, A₅ω₃, A₇ω₄, D₅ω₁,
   D₇ω₁): the full reverser set in Sym(N) is w₀·C_Sym(R); the antipode's
   coset vs W's — small stone, mostly a table; low priority.
6. **Marker-as-orbit for Ilya** (offered earlier, never asked for): since
   no marker survives a tick and only orbit averages do (SM-057 + SM-061),
   compute which PSL(2,7)-invariant statistics are homomesic. Joint-flavoured.

## 2. House ritual, compressed (full version: skill `run-ritual`)

Brief → `BRIEF_STONE_XX_*.md` + `BRIEF_STONE_XX_LOCK.sha256` BEFORE code;
registered guesses resolvable INVERTED at equal prominence; deviations by
dated AMENDMENT locked before reveal; post-reveal checks labelled; first
run kept as `_FIRSTRUN.log`; findings `STONE_XX_*.md`; grades
[P]/[C]/[obs]/[I]; Rule 3; Not RH/GRH; covers declare cache dependencies;
SHA256SUMS LF; hash outside the zip in `COVER_*_SHA256.txt`; mirror to
`zips/`; SENT only on Selina's word, then FROZEN; registry edits by a
Python inserter with collision asserts (pattern: scratchpad
`registry_v1xx.py`, next is v1.12); `knowledge.yaml` title bump each
version; KCP refresh
`C:\Users\selin\OneDrive\Desktop\Ilya Riemanns\KCP_SETUP_2026-08-26\kcp_refresh.ps1 -LaneRoot <lane>`;
one commit per registry bump, Co-Authored-By Claude Fable 5.1; memory
file updated. Next stone letter: **AY**. Next row: **SM-063**.

## 3. Reusable machines (load VERBATIM, never retype)

- 56-board block: `verify_stone_ap_clock_centralizer.py` between the
  `# ===…` fences (`apsrc.split(fence)[2]`); defines roots, S7, IOTA, PSI,
  D["PR"], PAIRS, ptype, verts, C7, W2.
- 42-board `Minuscule` class: `verify_stone_aq_rush_shi_defect.py` between
  `# ---- Cartan matrices` and `# ---- the cases`. CAVEAT (SM-062): its
  `isometry()` is W-membership only on E₇ or where −1 ∈ W or the board is
  not self-dual; on A₃ω₂, A₅ω₃, A₇ω₄, D₅ω₁, D₇ω₁ it overcounts by the
  antipode — enumerate instead (all ≤ 322,560).
- numpy BFS of W: Stone AT `enumerate_W_np`; Stone AS's W(E₇) build (~35 s
  here); conjugation trick `H = Pki[G[:, Pk]]`; normaliser by row hashing
  (Stone AX).
- Sheet clock Ψ₆ and w₀(E₆): Stone AU. e-coordinate boards (D_n, B_n
  spinors): Stone AV.
- Bridge PSL(2,7) generators: `_stone_ap_cache/witnesses_ap.json`
  (bridge_pair_a/b). Its normaliser: `_stone_ax_cache/witnesses_ax.json`
  (element c).

## 4. Loose ends (housekeeping, no registry event)

- Untracked in git: `_explore_psi_memory_2026-09-05.py`,
  `_stone_aa_cache/phi360.npy`, `_stone_z_cache/G_rows.npy` — decide: add
  the exploration (it is a disclosed-style file) and gitignore the two
  npy caches, or leave. Ask Selina.
- 11 older envelopes' SHA256SUMS end CRLF (benign, noted in v0.87); do not
  touch frozen folders.
- The bridge-draft KCP pin was stale once (v0.83) and corrected; watch that
  only the registry pin moves on refresh.
