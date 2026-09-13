# COVER — the half-turn on the full-height orbit (SM-066, Stone BB)

**Selina + Claude · 2026-09-13.** One stone, one open question closed. No new
asks; nothing here needs your word beyond the sealing you already owe on
SM-057..065. Registry v1.21.

## 1. What this is

SM-063 (Stone AY) established, by a search, that on the 4-cube the half-turn
R⁴ is a Weyl element on the clock orbit O₂ (equal to −τ there) and on no Weyl
element on O₁, and listed as the first of its §7.12.4 open items: *why the
orbit not containing λ is the one on which the half-turn is a Weyl element — a
proof, not a computation.* **SM-066 (Stone BB) is that proof.**

## 2. What it found

A one-vector obstruction. Grade the spinor weights by rank (number of minus
signs); W(B₄) = 𝔽₂⁴ ⋊ S₄ acts affinely, w(x) = π(x) ⊕ v.

- **Lemma (Weyl rank-shift).** For w = (π,v), writing u := π⁻¹(v),
  rank(w(x)) = wt(π(x)⊕v) = wt(x⊕u), so Δ_w(x) = wt(u) − 2|x∩u| — a Weyl
  element's rank-shift is controlled by the single vector u.
- **Theorem.** R⁴ agrees with no Weyl element on O₁ and with −τ on O₂. On O₁
  the half-turn shifts every rank by ±2 (O₁ is the full-height orbit, ranks
  0,1,1,2,2,3,3,4, R⁴ pairing positions that differ by 2); at λ the shift is
  +2, forcing wt(u)=2, whereupon |Δ|=2 forces even overlap ⟨x,u⟩=0 for all
  x∈O₁, and O₁ spans 𝔽₂⁴, so u=0 — contradiction. On O₂ the shifts are ±1,
  realised by u=1110 (= −τ).

**λ is the cause:** the top weight pins wt(u) at rank 0, and only an orbit
avoiding the extreme ranks can carry the half-turn as a symmetry. The argument
is dimension-free (Δ_w(x) = wt(u) − 2|x∩u| in every B_n): on the full-height
orbit of B_n the half-turn shifts rank by ±n/2, so for every n ≥ 4 the
extreme-weight orbit's half-turn is not a Weyl element — the n>4 case reducing
to the fact that the shift is exactly ±n/2 (verified at B₄; B₈ is the next
computation).

6 PASS + 0 FAIL. Honest provenance is stated in the brief: this was found by
exploration on our side this session; the brief records the completed proof
and the verifier re-checks its ingredients — there are no registered guesses,
so the lock certifies the proof text, not the outcome of a search.

## 3. Standing

In the draft this closes §7.12.4: it now states the theorem, and the remaining
open items of Stone AY move to §7.12.5. (The draft itself is not in this
envelope; the section is enclosed as the summary, written for the merge, so
you can review the mathematics without the whole manuscript.) Nothing new is
asked. Seals still pending your word: SM-057..065 (sent), and now SM-066 (this
envelope).

## 4. How to re-run

`verify_stone_bb_halfturn_fullheight.py` is self-contained (plain Python 3, no
numpy, no caches): it re-computes the brief's SHA-256 against the lock, takes
SM-063's H3 clock verbatim, and asserts BB1–BB5. It builds only on SM-063's
sealed clock and SM-060's identification of the 4-cube as the B₄ spinor board;
no external inputs.

## Contents

`COVER_NOTE.md` (this file); `HALFTURN_FULLHEIGHT_SUMMARY_2026-09-13.md`
(§7.12.4 as merged); the stone complete — `BRIEF_STONE_BB_HALFTURN_FULLHEIGHT.md`
(+ `BRIEF_STONE_BB_LOCK.sha256`), `verify_stone_bb_halfturn_fullheight.py`
(+ `.log`, `_FIRSTRUN.log`), `STONE_BB_HALFTURN_FULLHEIGHT.md`;
`REGISTRY_SNAPSHOT_v1.21.md`; `SHA256SUMS.txt` (LF).
