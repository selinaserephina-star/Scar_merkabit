# RECEIVED — 2026-09-14 — IB consolidated acceptance (SM-057..066) + Fano sextet v3

Two items received from Ilya Balashov (with Claude), 2026-09-14, filed here.

## 1. `TO_SELINA_STONES_057_066_CONSOLIDATED_2026-09-14.md`
His consolidated reply gathering the two earlier separate passes (the
§§7.8–7.13 review and the SM-066 note) into one place, plus the §11
bibliography.

**Standing, in his words:** *"All ten — SM-057 through SM-066 — accepted
on my word, explicitly, gathered here in one place."*

- SM-057 spot-checked against his own 2.9M-element W(E₇) closure (0 hits, consistent).
- SM-058/059 reversal theorem checked by logic; resolves his own earlier w₀ confusion.
- SM-060/061 homomesy corollary credited and derived; honest negatives accepted.
- SM-062 point (e) — his independent χ₁+2χ₆+χ₇+χ₈ re-derivation cross-checks §11.3.
- SM-063 Lemma B correct; auditor's-error transparency accepted.
- SM-064 Lemmas F/G clean.
- **SM-065 (Stone BA)** — named explicitly, accepted.
- **SM-066 (Stone BB, half-turn)** — checksums verified (outer zip, inner
  SHA256SUMS, brief-lock a5fab2bf…), Lemma BB-A rebuilt from scratch
  (W(B₄)=𝔽₂⁴⋊S₄ order 384; rank(w(x))=wt(x⊕u) on 200 random triples;
  contradiction worked by hand). Accepted.

§11 bibliography: he proposes King–Luhn 0912.1344, King–Luhn 0905.1686,
Luhn–Nasri–Ramond 0709.1447 — checked not already present under other
entries; closed on his side pending placement at points of use. (These
three were already adopted into the draft at v0.7 and are cited in place
in §11.9 and the References block — see registry v1.27.)

## 2. `to_Selina_FANO_SEXTET_2026-09-14_v3.zip` (sha256 76f60f50…, 36,923 B)
Third, most-developed version of the Fano-sextet package (the first
version — Results 1–2 only — is filed under
`RECEIVED_2026-09-14_IB_ROOF_CLOCK_REPLY_FANO/`). This v3 carries
**Results 1–7**, all twelve inner checksums verified OK
(`SHA256SUMS.txt`). New over the filed stub:

- Result 3 — S4-breaking vacuum found; χ₆|_S4 = 1⊕2⊕3₁; degeneracy relation 3κ_g2 = 2κ_mixed.
- Result 4 — V4 family, 12 critical points (honestly none stable at tested couplings).
- Result 5 — stability inequality 2κ_mixed > 12κ_line + 105κ_prod; one genuine stable min found.
- Result 6 — coexistence window: S4 and S2 vacua both stable in one potential (interpolation, not derived).
- **Result 7** — the intertwiner S FOUND by group-averaging (after the
  earlier null_space attempt failed for numerical reasons); verified on
  all 168 elements (residual 1.24×10⁻¹⁵); Fano S4 vacuum, transformed
  through S, reproduces Luhn–Nasri–Ramond's own stated singlet vev
  exactly up to a fully-characterized diagonal η-twist. **This closes the
  un-converged change-of-basis open end flagged at registry v1.25.**

Rule 3 note: the King–Luhn flavon-potential / vacuum-alignment physics
remains PARKED and out of the joint draft; only Result 1's χ₆-as-Fano
identity is in the paper (§11.9). Results 2–7 are the physics extension,
held here.

No code re-run on this side for v3 (v1's `fano_sextet_six_invariants.py`
was already re-run at v1.25). Checksums verified only.
