# MASTER SUMMARY — ACTIVE — PSL(2,7) to PMNS Lepton Program

**Read [CANONICAL_BLOCK.md](CANONICAL_BLOCK.md) first for verified constants and conventions.**
**Full historical reasoning, all findings, all epistemic tags: see [MASTER_SUMMARY_ARCHIVE.md](MASTER_SUMMARY_ARCHIVE.md).**

This file is the current-status snapshot only — what the best model is right now, and what's still open. It should stay short. New findings go into the archive; only update this file's numbers when the canonical best-fit point itself changes.

---

## Current best model (corrected, matches CANONICAL_BLOCK.md)

```text
Vacuum:  chi-axis = 2, xi-axis = 0  (UNIQUE among 6 combinations, established
         independently of the operator-search work below)

Charged leptons: y2=8.043031, c3=0.64085776, c3'=2.38809204  -- masses EXACT
  (cost~5e-32; corrected this session from an earlier wrong y2~0.052)

Neutrinos (Majorana): m0=41327.05, m2=-806652.33, m3=-70752.39, mcross=5261.89
  (best of 3000 restarts; this IS the structural floor, not a search gap)

Results:
  theta12 = 32.73 deg  (target 33.0,  off -0.27 deg)
  theta23 = 42.32 deg  (target 45.0,  off -2.68 deg -- structural floor)
  theta13 =  8.46 deg  (target 8.5,   off -0.05 deg -- essentially exact)
  Dm21/Dm31 = 0.0300   (target 0.03,  exact)
  cost = 0.003646      (confirmed structural limit of this 4-param neutrino
                         operator set, not a fitting failure)

  delta_CP = 0 deg (forced at real VEVs)
  Sum(m_nu) = 0.1519 eV  -- IN TENSION with cosmological bound (0.072 eV)

Free parameters: 7 (y2,c3,c3',m0,m2,m3,mcross) for 7 independent observables,
plus the axis choice as a non-tunable discrete output, plus TWO stated
organizing assumptions (kappa relationship for mcross; "twist costs +1"
FN-charge rule) -- neither derived from first principles (7+ messenger/
invariant attempts all failed, see archive).
```

**With complex VEV phases** (α₂,β₃,γ₁ — see archive §8/§9 for the full story, including a serious eigh-vs-Takagi bug caught, fixed, and the whole scan redone): once corrected, **θ₁₂,θ₂₃,θ₁₃,ratio match targets to ~4 significant figures at essentially every tested phase point** (not just one), and **56% of a 9-point representative re-scan land inside the NO-favored δ_CP window** [−174°,−122°] — e.g. δ_CP=−133.7° at phases (5.281, 2.007, 2.201), or −150.2° at (4.29, 0.88, 1.26). Winding numbers are point-independent and structural: w(α₂)=1, w(β₃)=2, w(γ₁)=0 everywhere checked.

---

## Open items, ranked

1. **Σm_ν = 0.1519 eV tension with cosmology** — still open. Six distinct reduction mechanisms tried (3 operator-based, 3 seesaw-family), zero succeed at reducing it while keeping axis discrimination AND precision. **Now provably closed for the entire class of degree-2 flavon-bilinear candidates** (via the exact linearity of Y₂/Y₃ — any such candidate reduces to a mechanism already tested and already failed; see archive §4). Only two categories remain genuinely untested: loop-integral radiative models, and degree≥3 flavon combinations.
2. **φ₂'s direction** — still open. Seven mechanisms tried and failed (five direct invariants up to trilinear order; two messenger constructions from the only PSL(2,7) irreps available). A working mechanism, if one exists, needs something outside this whole family.
3. **θ₁₂/θ₂₃ residual** — still open, confirmed structural (not a fitting artifact) at the corrected reference point too. Four 5th-operator attempts either redundant or axis-discrimination-destroying.
4. **Deriving κ (the mcross/m3 ratio) and the "+1 twist cost" FN rule from a UV mechanism** — still open. Messenger attempts relocate the assumption rather than removing it.
5. **δ_CP away from {0,180}, and specifically the NO-favored ~212° region** — **ACHIEVED** (see above) — no longer open, though the mechanism (specific complex phases) is itself not derived from anything, just shown consistent.
6. **Whether the tensions above are artifacts of treating φ₂,Φ₃,Φ₃′ as independent VEVs** — **RESOLVED, no**: a full modular-form (single-τ) reformulation was tried and found strictly worse, not better (fails to even reproduce the exact charged-lepton fit). Tensions appear to be structural to this operator content, not a parametrization artifact.

## Reusable infrastructure

S₄ representation-matching code (V₄-diagonalization, Frobenius–Schur real-structure construction, validated position bases for 2/3/3′/generation), the χ6/χ7/χ8 branching computations, the Takagi-decomposition-based complex-VEV pipeline (see CANONICAL_BLOCK §5 for the critical eigh-vs-Takagi warning) — all reusable for future questions in this project, independent of which specific open item they address.

---
END OF ACTIVE SUMMARY — see ARCHIVE for full reasoning and all dated findings.
