# RECEIVED — 2026-09-19 — IB's Fano-sextet finding, Results 1–20 (eight saves of one document)

From Ilya Balashov (with Claude); arrived in Selina's Downloads 2026-09-19 08:36
as eight zips all named `to_Selina_FANO_SEXTET_2026-09-14*.zip`. Filed here as
data. Two items that arrived in the same batch belong to other lanes and are
filed there: the Klein-quartic Jacobian note → `Desktop/BSD/RECEIVED_2026-09-15_IB_KLEIN_JACOBIAN_CM/`;
the Sp(6,2) Katz–Sarnak package → `Desktop/Conductor21_Companion/RECEIVED_2026-09-19_IB_SP6_2_KATZ_SARNAK/`.

## What the eight zips are

Not duplicates. One document, `FINDING__fano_sextet_king_luhn_2026-09-14.md`,
saved eight times as it grew from Results 1–11 to Results 1–20; the cover note
is byte-identical in all eight (frozen at Result 11). Ordered by the FINDING's
size:

| zip (as received) | zip sha256 (16) | FINDING bytes | FINDING sha256 (12) | state |
|---|---|---|---|---|
| `… (4).zip` | 2e0de0f6ef789244 | 24,242 | 4944049b9ba4 | complete |
| `…-28.zip` | 496f5d9c8fdb22d0 | 29,460 | 7d895dcfca22 | **truncated download** (no central directory; 13 local entries, last one partial) |
| `… (5).zip` | 2e6845daa200fa3d | 32,704 | dd2428058512 | complete |
| `… (6).zip` | cdf07ca4962e2a20 | 44,925 | 0548c9bd82a1 | complete |
| `… (7).zip` | 3479cfbc57f2080d | 47,954 | 198858a31275 | complete |
| `… (8).zip` | a6231d5bf3173f4a | 51,003 | 5ba9ab29d33e | complete |
| `… (9).zip` | c8685924348d28b3 | 54,006 | 57862b8791b4 | complete |
| `…-18.zip` | 982b16bbbef34f0e | **58,189** | **b03fba6dec1c** | **truncated download — the newest** |

The `-18` zip is the definitive version (Results 1–20 and the fullest
SHA256SUMS, 27 entries). Its local file headers are intact through 22 of the
27 files; I recovered those by raw-deflate, and reconstructed the rest by
sha256 lookup across the other seven versions (every script it lists except
one exists byte-identically in an earlier save).

**`FANO_SEXTET_R1-20_reconstructed/selina_package/` verifies 26 of 27 against
the `-18` package's own `SHA256SUMS.txt`.** The one file missing is
**`scripts/fano_degenerate_vacuum_family_DISCOVERED.py`** (sha bbbc2082…) —
the script of **Result 20**, the finding's single substantial open item. It
exists in no received zip; a resend is asked for in the reply envelope.

`salvage_notes/` keeps the one partially-recovered file from `-28` for the
record (its complete copy is in the reconstruction).

## What is in Results 1–20 (his headings, our reading)

- **1–2** χ₆ = Fano deleted permutation module (in the draft as §11.9); the six
  invariants — Result 2 now carries his own correction banner pointing to 12.
- **3–6** the S4 vacuum, the V4 family, the stability inequality, the
  coexistence window. **6 is marked RETRACTED by him (→ 15).**
- **7–11** the intertwiner; the SO(6) transform; the true cause (0905.1686, not
  LNR); κ₂=κ₃=κ₄+κ₅/√7 verified against King–Luhn's own Θ,Θ'; χ_TB verified;
  h₁..h₅ exact.
- **12 — our FANO-QUARTIC-CORRECTION envelope (registry v1.28/v1.29),
  cross-verified on his own infrastructure**: Iprod sextic ✓; `Q_miss` ≡ I₅
  with an exactly constant ratio (−0.472206, std/mean 2×10⁻¹⁴) ✓; the √7
  metric geometry ✓; the κ-relations *necessary* ✓. Our coexistence
  explanation he marks "plausible, not re-run".
- **13–14** Results 3 and 4 redone on the 4-term real quartic potential
  (Q_miss vanishes on real fields): both survive.
- **15 — Result 6 retracted**: "zero coexistence in 210 samples" on the
  corrected potential. **This contradicts our envelope**, which showed the
  window survives at κ_prod = 0. **Checked exactly on our side — see below;
  our claim stands, his negative is a sampling miss.**
- **16** our 3κ_g2 = 2κ_mixed was an aesthetic choice, not King–Luhn's
  condition (theirs: all eigenvalues positive). No dispute.
- **17** the "crater" mechanism: χ̂_top = diag(0,0,1) exactly; octet
  contractions force Δ_Vs, Δ_Va; sum-of-squares uniqueness of the alignments.
- **18** the 28-bitangent action rebuilt from scratch; **7×4 correspondence**
  (each Fano point's S4 contains exactly four bitangent stabilizers S₃), cross-
  checked four independent ways. Board mathematics, not physics — the one
  item that could touch the draft (a one-line remark at §11.9, his word asked).
- **19** three forced-uniqueness checks: dim Hom_G(Sym²χ₆,1)=1 and
  dim Hom_G(Sym²χ₈,1)=1 (positive); the −0.472206 constant is a normalization
  convention (negative, correctly).
- **20 — new, open, substantial**: at King–Luhn's κ=κ'=0 locus a family of
  critical points exactly energy-degenerate with χ_top, same Hessian
  spectrum, hierarchy-free Yukawa textures. Script missing (above).

## What was run on our side this pass

1. **His `fano_result6_CORRECTED.py` (Result 15)** re-run as received: output
   reproduced exactly (handoff at t≈0.07/0.12 on *his* path A′=(1,⅔,0.1,1) →
   B′=(1,1,1,1); 13/150 random points with S4 stable, 0 coexisting).
2. **Our exact check, `../_explore_fano_coexistence_exact_2026-09-19.py`
   (+ `.log`)**: symbolic Hessian restricted to the 6-dim sum-zero sextet,
   critical points refined to 30 digits, at the point our envelope named
   (t = 0.125 on the *original* A→B path, κ_prod := 0, m² refixed):
   κ = (1.116625, 0.694583, 0.174625, 0, 1.087375), m² = 28.596698.
   **Both vacua are strict minima**: line-S4 at a=b=c=1, eigenvalues
   {0.1044 ×2, 0.2637 ×3, 114.39}; the second at a = 2.122211, b = c =
   −0.353702, eigenvalues {0.1937 ×2, 0.3325 ×3, 114.39}. Window on that path
   with κ_prod ≡ 0: t ∈ [0.1155, 0.129]. Verdict unchanged under rescaling
   m² (homogeneity check). His path is a different line through coupling
   space and his random box (150 points in 4 dims) did not hit the thin
   region; both scripts use identical invariant definitions, so this is not a
   convention dispute.
3. **Found from the digits**: the coexisting "S2" vacuum has b = c = d and
   a = −6b to 10⁻¹² — it is the **point-stabilizer S4 vacuum
   (6,−1,−1,−1,−1,−1,−1)**, the Fano dual of the line vacuum
   (4,4,4,−3,−3,−3,−3). The two S4 classes of PSL(2,7) are swapped by the
   outer automorphism (Fano duality), which the potential does not respect
   (I_line is not self-dual) — hence the different energies (−75.066 vs
   −75.129) and the 2+3+1 Hessian pattern at both. Neither side had noticed.
4. Nothing else of his re-run this pass (Results 7–11, 13–14, 16–19 held as
   received; his Result 12 is *his* re-run of *our* scripts).

## Standing

- Result 1 in the draft (§11.9) — untouched. Nothing in this batch changes the
  joint paper (v0.8); Results 2–20 remain **PARKED under Rule 3**.
- Our three cover asks of v1.29: (1) Result 2 correction — accepted in
  substance (his banner on Result 2, his Result 12); (2) travel beyond the
  note — he keeps it inside the finding, proposes no registry row → parked, as
  defaulted; (3) nothing else — closed.
- Reply envelope: `../to_Ilya_FANO_COEXISTENCE_AND_KLEIN_2026-09-19/` (PREPARED,
  the send is Selina's word).
