# Stone F(c) — the quantum lift: the chirality beam-splitter machine

**Scar_merkabit lane · 2026-08-30 · verifier:** `verify_stonef_c_quantum.py`
(12 checks, all passing; local algebra exact over ℤ[√2], small machines
exhaustively enumerated). This is the parallel-magic case of the methods
note's open problem #3 — *do certificates exist in the unitary world?* —
answered on our own object. "Quantum" here means real-orthogonal with
genuine superposition; no physics is claimed.

## The machine

Field space ℂ⁵⁶ = direct sum of the 28 ι-pairs (28 two-level cells).
**Cheap**: the frame grammar as permutation unitaries (pair swaps +
chirality flips X — the B₂₈ typing). **Magic**: one genuinely quantum
gate, **W = the chirality beam-splitter** — the 2×2 Hadamard applied to
every ι-pair simultaneously, rotating each frame's ± into superposition.

## The exact theory

1. **Local algebra [C, exact].** Per pair, ⟨H, X⟩ is the dihedral group of
   order 16. Every local element has an **H-length** k(g) (beam-splitter
   passes needed, X free): distribution [0², 1⁴, 2⁴, 3⁴, 4²], maximum
   **k(−I) = 4** — flipping a single sign costs four splitter passes.
   H-parity (k mod 2) is a homomorphism D₁₆ → ℤ₂.
2. **The certificate [C, exhaustively verified].** For the whole machine:

   > **W-depth(U) = max over pairs of the local H-length**, subject to one
   > global **superselection rule**: all pairs share the same H-parity,
   > equal to the number of W-layers mod 2.

   Verified for *every element* of the n = 2 (order 256) and n = 3 (order
   6144) machines against ground-truth 0/1-weight BFS — formula exact,
   orders matching the structure theorem (parity-locked (D₁₆)ⁿ ⋊ Sₙ,
   order 2·8ⁿ·n!).
3. **The 56 theorems.** The frame-quantum group has order 2·8²⁸·28!
   ≈ 1.18×10⁵⁵ (183 bits); its **W-depth is exactly 4** (the deepest
   citizens are the sign flips; depth 3 fails by parity + k(−I) = 4); and
   the H-parity charge is a conserved quantity the permutation machine
   never had.

## The picture the whole day assembled

| machine | expensive gate | depth |
|---|---|---|
| 56, branch grammar (permutation) | the clock Ψ | **2** |
| 56, frame grammar (permutation) | the clock Ψ | **2** |
| 56, frame-quantum lift | the beam-splitter W | **4** |

*Scrambling is cheap; superposition is dearer; sign flips are the dearest
of all.* And where the transportation certificate was a feasibility
problem and the hyperoctahedral one a witness campaign, the parallel-magic
unitary certificate collapses to a **max formula plus one parity charge** —
because the magic gate acts on all cells at once, cost stops adding and
starts maximizing.

## The frontier, precisely located [C]

Ψ does not commute with ι, so conjugating W by the clock moves the
Hadamard blocks off the ι-pairs: **sequential magic (the clock) escapes
the parallel-magic certificate's block structure.** The group ⟨cheap, W, Ψ⟩
leaves the monomial world entirely — and *that* mixed regime, where
scrambling and superposition interleave, is where the methods note's open
problem #3 genuinely lives. The honest map after today:

> parallel magic (W alone): **solved** — max certificate + superselection.
> sequential magic (Ψ alone): **solved** — depth 2, both grammars.
> the mix (Ψ and W together): **open** — and now precisely posed on a
> concrete 56-dimensional object with every ingredient exact.

*Sealed 2026-08-30; registry row SM-014.*
