# Stone 1, step 1 — the transportation certificate generalizes

**Scar_merkabit lane · 2026-08-30 · verifier:** `verify_stone1_certificate.py`
(9 checks, all passing; every number below is a line of its output).

## The abstract certificate (now stated once, for any machine)

For a **full Young (block) subgroup** H = S_{B₁}×…×S_{B_r} ≤ S_n and any
magic permutation m, the double coset HgH is exactly the block-transport
contingency table T(g) (classical), and — because the middle typed gates can
re-sort every block freely —

> **g is writable with exactly k magic gates ⟺ T(g) lies in the k-fold
> table-composition of T(m)**, where one composition step is an integer
> 3-tensor transportation-feasibility problem with margins T(previous),
> T(m), T(candidate).

So MAGIC-DEPTH(⟨H,m⟩; H, m) — a question about ~n! objects — reduces to a
finite closure computation on contingency tables. Wreath typing (allowed
block permutations) enters by closing the table sets under row/column
permutations. Over full Young/wreath groups the certificate is **exact with
no parity lemma** (CN-012's junction-repair was only needed because its H
was cut to even permutations).

## Results of the first runs

| machine | typed side | tables | magic gate | **depth** |
|---|---|---|---|---|
| 27 (X/Y/Z legs) | Young S₉³ | 1540 | Ψ⁴ | **3** |
| 27 | wreath S₉≀S₃ | 1540/sym | Ψ⁴ | **2** ✓ = CN-012 |
| 56 (27/27̄/1/1) | Young S₂₇² | 908 | Ψ | **5** |
| 56 | + sheet-swap (= pr) & vacuum-swap | 908/sym | Ψ | **2** |

1. **The anchor holds and sharpens.** The wreath run reproduces CN-012's
   depth-2 exactly. The Young run refutes the auditor's expectation
   (recorded per house rules: depth is 3, not 2) — yielding a new corollary:
   **the typed S₃ leg-rotation is worth precisely one magic gate** (3 → 2).
2. **The certificate generalizes** — first contact with a new machine
   produced exact theorems, not approximations: ⟨S₂₇×S₂₇̄×1×1, Ψ⟩ = S₅₆
   (Schreier–Sims, order 56!), and the branch-grammar magic-depth is
   **exactly 5** in the plain-Young typing.
3. **The headline new theorem:** with the sheet-swap in the typed side —
   and the sheet-swap *is* pr, which DQ-2 proved bilingual (free in both
   grammars) — the 56-machine's branch magic-depth collapses to **2**:
   *every* program class in S₅₆ is `typed · Ψ · typed · Ψ · typed`. The
   mirror is worth **three** magic gates. In machine language: *two ticks
   of the clock reach every grammar class, provided you may flip the
   mirror — and the mirror is free.*
4. **The recurring 2.** Both machines land on depth 2 relative to their
   natural wreath typing. Open question (next stone step): is wreath-depth
   2 generic for crystal clocks — equivalently, is there a positivity
   condition on T(m) that forces two-step coverage? A yes would be a small
   theorem about this whole family of architectures.
5. **The frontier mapped.** The frame grammar's typed group is
   hyperoctahedral — a Gelfand pair, whose "tables" are matching-union
   coset types. Computed: Ψ has type [9,9,9,1] (the clock's [18,18,18,2]
   orbit structure, halved); pr and ι are type-trivial [1²⁸] — the
   bilingual result again, now in the third formalism. Frame-grammar depth
   needs the matching-composition analogue: the next genuinely new
   mathematics this stone requires.

## Why this matters for the application

The compiler-benchmark half of Stone 1 just got its product line: we can now
generate, for **two** machines and **two** typings each, instance families
where the optimal magic-depth is a theorem — plus a worked demonstration
that the certificate method transfers to a new (typed-group, magic-gate)
pair without modification in the Young/wreath regime. The honest boundary
also showed itself: hyperoctahedral typing (and, beyond it, true
Clifford+T) needs a genuinely different composition calculus. That boundary
line — Young: solved; Gelfand pairs: open; unitary: open — is exactly the
shape of a publishable methods note.

*Sealed 2026-08-30; registry row SM-009.*
