# STONE S — THE RIGIDITY THRESHOLD
**Scar_merkabit joint lane · 2026-08-30 · SM-018 · answers Ilya's
ONE LAW / TWO PROJECTIONS v0.1 (received same day, sha adb17c49…0016)**
**Brief:** `BRIEF_STONE_S_RIGIDITY.md`, sha-locked `45031dd4…7082` before
code. **Verifier:** `verify_stone_s_rigidity.py` — **14/14** (two
fail-first logs kept; one registered expectation of the brief itself and
two working guesses refuted en route, all recorded).

## §0 Discipline

Compute, never assert; his rules executed where defined; two
under-specifications instantiated by us, declared in the locked brief,
choices returned to him. Refutations at equal prominence — including his
floor, our registered inversion, our mis-derived anchor, and our first
cut-or-join guess. Exhaustive and exact for n ≤ 7; everything [C on
range]. ONE LOCK.

## §1 One paragraph

Ilya proposed: min_support = 3 for both projections — "support 2: a swap,
soft; support 3: first true knot, first rigid structure" — and asked for
the check against our exact tables. Executed on the two projections our
tables support (α=1: Sₙ conjugacy classes; α=2: the (S₂ₙ, Bₙ) coset
types — both on partitions of n, same distance d), the verdict under his
own decision rule is **branch two, with structure**: the two worlds agree
EXACTLY at n = 4, 5 and diverge from n = 6 — but always in ONE direction
(containment: the non-orientable world reaches everything the orientable
one reaches, plus the entire parity-odd sector, plus finitely many even
extras — 6 witnesses at n = 6, 3 at n = 7). His soft/rigid ladder is
refuted as stated (rigidity events occur at every depth; the dominant
missing target is the IDENTITY, by the exact law "home only by exact
retracing"), and so is our registered inversion. The mechanism of the
divergence is a single new exact law: **the swap step is
cut-or-join-or-TWIST** — beyond the two classical moves, a matching swap
can reverse a segment inside a union cycle and preserve the type. The
twist is the microscopic non-orientable move; it is exactly what breaks
the parity law downstairs (upstairs, the sign homomorphism forces
d(μ) ≡ d(λ)+d(τ) mod 2 — verified as a law; downstairs, refuted by
(4)∘(4) ∋ (2,1,1)). Orientability IS the parity memory; "a permutation
is what remains when a braid forgets its path" lands on range as: the
Sₙ projection is what remains when the matching world forgets its twists.

## §2 The laws (all exhaustive, n = 4..7)

1. **Triangle necessity** (SM-010 anchor, re-verified) and the sealed
   **258** d-interval failures reproduced exactly.
2. **No parity law downstairs**; **parity IS a law upstairs** (sign
   homomorphism) — the cleanest separation of the projections.
3. **Identity return:** 1ⁿ ∈ supp(λ,τ) ⟺ λ = τ (both sides).
4. **Symmetry:** supp(λ,τ) = supp(τ,λ).
5. **Swap = cut-or-join-or-twist:** supp(λ, swap) = cut-or-join(λ) ∪ {λ}
   whenever λ has a part ≥ 2 (first guess, pure cut-or-join, refuted).
6. **The comparison** (identity mechanisms excluded, each side within
   its own soft laws): even-sector rigidity events — n=4: 3 = 3 equal;
   n=5: 0 = 0 equal; n=6: matchings 57 < Sₙ 63; n=7: 99 < 102;
   containment missing_B ⊆ missing_S at every n; odd-sector events exist
   only downstairs (6/15/105/219). Divergence witnesses (upstairs-missing,
   downstairs-reachable): n=6: (2,2,2)∘(2,2,2)→(4,2), (3,3)∘(3,3)→(4,2),
   (2,2,2)∘(4,2)→(2,2,2), (3,3)∘(4,2)→(3,3) + 2 symmetric; n=7 the
   (2,2,2,1)-family analogues — all built from ALL-EVEN types: exactly
   where upstairs parity-rigidity bites and twists dissolve it.

## §3 Refutations, at equal prominence

- His "support 2 soft / support 3 first rigid": FALSE on both
  projections as stated (his part-reading gives P(n) = 1, not 3 — the
  identity is the hard target, by law 3).
- Our registered inversion ("rigidity only at min(d) ≤ 1"): FALSE
  (events at every depth 0..n−2).
- Our brief's SB1 second anchor was MIS-DERIVED from a Stone 1b code
  comment; the sealed record in fact refutes that guess — corrected,
  and the honest anchor (the 258 count) reproduces exactly.
- Our first swap-law guess (pure cut-or-join): FALSE — the twist exists.

## §4 Returned to Ilya

(i) His "B_n" reads as braids; our Bₙ is hyperoctahedral — the braid
projection has no tables in this lane. Classical, cited not computed:
trefoil crossing number 3; B₃ the first braid group with a knotted
closure. Which braid-side table does he want, with what invariant in the
coset-type role? (ii) Which translation of "min_support" is his — d or
part? (iii) The reading of the odd sector and the twist: is the twist
his "path memory," inverted — the move you gain, not lose, by forgetting
orientation?

## §5 Grades

Laws 1–5, comparison 6: [C on range n ≤ 7]. Sₙ parity: [P] classical
(sign homomorphism), verified. The α=1/α=2 framing (orientable vs
non-orientable, Jack-parameter context): [I] role, cited as classical
context, no claim. All refutations recorded.

## §6 Reproduce

```
python -X utf8 verify_stone_s_rigidity.py   # 14 checks, ~2 min
```
Self-contained (stdlib + itertools; the Stone 1b matching machinery
reused verbatim inside).
