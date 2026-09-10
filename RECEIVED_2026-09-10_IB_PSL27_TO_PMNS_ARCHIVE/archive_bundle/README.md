# Archive Contents — PSL(2,7)→PMNS Lepton Project

## Start here
- `outputs/CANONICAL_BLOCK.md` — verified constants, conventions, critical
  bug warnings (READ FIRST before running or trusting any number below)
- `outputs/MASTER_SUMMARY_ACTIVE.md` — current status, best-fit model, open items
- `outputs/MASTER_SUMMARY_ARCHIVE.md` — full narrative history of every finding

## outputs/
All ~40 individual FINDING__*.md files (detailed methodology and results for
each investigation), plus the three files above, plus a few earlier AUDIT_*
files from the Scar-Merkabit verification workstream (a separate, earlier
part of this project — see ARCHIVE for context).

## code/
The actively-used, reusable Python code behind the later (most carefully
verified) work in this project. NOT a complete archive of every script run
this session — earlier exploratory directories (many one-off "run_*" folders)
are NOT included; they were superseded by the code here.

- `basis_match/` — PSL(2,7) group construction, S4 subgroup, character tables,
  representation branching (chi6/chi7/chi8), tensor-product projectors,
  position-basis alignment. The core group-theory infrastructure.
- `neutrino/` — charged-lepton and neutrino-sector fitting code, saved fit
  results (.pkl files) for various axis combinations.
- `cp_full/` — the complex-VEV / delta_CP pipeline, INCLUDING the corrected
  Takagi-decomposition treatment (see CANONICAL_BLOCK §5 for why plain eigh
  is wrong here) and the phase scans.
- `modular_reform/` — the Penedo-Petcov modular-form (tau) reformulation
  attempt and comparison code.
- `cp_test/`, `seesaw_test/` — smaller supporting scripts for the discriminant
  -locus/winding-number work and the seesaw-mechanism tests respectively.

## Known gaps (honest disclosure)
- This bundle does NOT include the original project knowledge documents
  (the preprints, theorem files, etc. that motivated the S4/PSL(2,7)
  framework itself) — those live in the Claude.ai Project's knowledge base,
  not in this session's working directory.
- Some very early exploratory code (before the project settled on its
  current conventions) was not preserved and is not reproducible from this
  bundle — only the final, established pipeline is included.
- File paths inside the .py scripts are hardcoded to this session's
  container layout (e.g. `/home/claude/neutrino/...`) — adjust paths if
  re-running elsewhere.
