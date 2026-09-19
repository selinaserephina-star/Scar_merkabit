# NEXT MAP — Stone BC (SM-067), for a fresh context window

**Read in this order, then start.** Nothing else is needed to begin.

1. `BRIEF_STONE_BC_B8_HALFTURN.md` — the brief. Locked:
   `BRIEF_STONE_BC_LOCK.sha256`. Your verifier's first test is that the
   brief's SHA-256 equals the lock. Do not edit the brief; if it is wrong,
   write an `AMENDMENT_STONE_BC_<date>.md` with its own lock (see
   `AMENDMENT_STONE_AT_2026-09-09.md` for the form).
2. `joint_paper/Roof_and_Clock_v1.0.md` §§7.9–7.13 — the anomaly's story as
   the paper tells it (§7.9.2 found, §7.10.1 located, §7.12.2(a) mechanism,
   §7.12.4 reason, §7.12.5 open). Twelve minutes.
3. `BRIEF_STONE_BB_HALFTURN_FULLHEIGHT.md` and
   `verify_stone_bb_halfturn_fullheight.py` — the rank-shift lemma and its
   tiny verifier (`reproducing_us`, `linear_span`, `affine_linear_part`):
   the pieces you generalise from n = 4 to n = 8.
4. `verify_stone_av_d5_anomaly.py` — `B_spin(n)`, `D_half(n)`, `board(...)`,
   `IC(R, Wset, k)`: the board builders and the I_k/C_k computation as used
   on B₃/B₄/B₅ and D₅. **Do not call `closure(...)` on W(B₈)** — 10.3M
   elements as 256-tuples will not fit; use the affine (π, v) form as the
   brief's §3 says. `IC` enumerates over a materialised W; you will write
   its affine replacement.
5. `verify_stone_aq_rush_shi_defect.py` — the `Minuscule` class (board from
   a Cartan matrix); D₉ ω₉ through it gives the same clock as `B_spin(8)`
   under the sign-pattern identification; use it as the cross-check (AV1's
   pattern).
6. `SCAR_MERKABIT_REGISTRY.md` rows SM-058, SM-060, SM-063, SM-064, SM-066
   for the exact numbers already sealed (B₄: |I₄| = 8, |C₄| = 4, −τ =
   (e₂e₃)(−e₄) on O₂; D₅: I₃ = I₅ = 2, I₄ = 8; the 83/15 dichotomy).

## House rules that apply (short form; `knowledge.yaml` is the long form)

- Brief locked before code; verifier checks the hash first; first-run log
  kept as `_FIRSTRUN.log` whatever it says; registered guesses reported
  INVERTED at equal prominence when the data says so.
- Compute, never assert. Every number in the summary names the bar that
  produced it.
- Rule 3: no physics. "256 of Spin(17)" names a representation.
- Nothing is sent. Sealing = registry row SM-067 + summary + logs +
  commit. Packaging for Ilya is Selina's word.
- Registry: append the row to the sealed-units table after SM-066, add a
  changelog entry (next version after the head of the changelog), re-pin
  `knowledge.yaml` (title line "…REGISTRY vX.YY…" and `updated:`), commit
  with the message form used in `git log`.

## What "done" looks like

- `verify_stone_bc_b8_halfturn.py` + `.log` + `_FIRSTRUN.log`, all bars
  BC0–BC8 printed with numbers.
- `STONE_BC_B8_HALFTURN.md`: one page — question, guesses vs outcomes (a
  table), the extras listed, what it means for §7.12.4 (one sentence to
  replace "B₈ next"), not claimed.
- Registry row SM-067 + changelog + KCP pin + commit.
- If BC3 holds, the paper gets a sentence in §7.12.4 and a line in §13/§14;
  do that through `joint_paper/build_v1.py` (add a `rep(...)`, re-run — it
  regenerates the .md and the .docx), not by editing the .md directly.

## Expected cost

B₆, B₇: seconds. B₈ full enumeration of I_k for one lag: minutes with numpy
over (π, v); all 15 lags: budget an hour, or derive I_k = C_k for k ≠ 8 by
the cheap necessary test first (the conjugate must commute with −1, which
is central) and enumerate fully only at k = 8 and at any lag the cheap test
does not settle. D₉: lemma and sampling only.

## Provenance

Staged 2026-09-19 after the joint paper reached v1.0 (registry v1.32). The
stale phrase "for a reason not yet found" in §7.9.5 was corrected in the
same session (registry v1.33); the anomaly's reason is §7.12.4. This stone is
the "B₈ next" of SM-066.
