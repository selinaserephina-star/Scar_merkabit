# Tower B — the covers & bridges, verified (Stenberg → Balashov)

**2026-08-31. Compute, never assert; refutations at equal prominence. Not RH/GRH.**

Ilya —

You separated the two towers — spine (L6 = C₆×ℤ₂) and covers-and-bridges — and
agreed they must be kept apart. So we built the second one. `verify_tower_b.py`,
**22/22 checks**, group theory only. It turned out to have a clean backbone.

**The backbone.** The ODD spine levels are the PSL(2,p) family, and their Schur
covers are SL(2,p), for p = 7, 5, 3:

    L7  PSL(2,7)      <- SL(2,7)
    L5  A₅ = PSL(2,5) <- 2I = SL(2,5)
    L3  A₄ = PSL(2,3) <- 2T = SL(2,3)

Each verified from scratch as a **non-split central ℤ₂-extension** (center
{±I}, a *unique* involution, quotient = the level). Tower B is not a grab-bag;
its spine is the SL(2,p) tower over the odd levels.

**The rest of Tower B:**

| level | cover | kind |
|---|---|---|
| L5 A₅ | Ih = A₅×ℤ₂ | split cover (31 involutions — *not* the Schur cover) |
| L3 A₄ | Th = A₄×ℤ₂ | split cover |
| L4 S₄ | GL(2,3) = 2·S₄ | double cover (GL(2,3)/{±I} = PGL(2,3) ≅ S₄) |
| top | W(E₆) ⊂ **Sp₆(2)=W(E₇)/±** | bridge, index **28** |

**Three refinements, at equal prominence:**

1. Your SPINE-MAP listed SL(2,7) *and* PGL(2,7) as L7 "covers." They are
   opposite roles — **SL(2,7) is the central Schur cover; PGL(2,7) is an
   index-2 over-group** (PSL(2,7) ⊴ PGL(2,7), outer-diagonal quotient). Same
   order 336, different job. Kept both, labelled.

2. **Split vs non-split at equal order.** Ih = A₅×ℤ₂ and 2I = SL(2,5) are both
   order 120 but different groups — 31 involutions vs 1. The split covers
   (Ih, Th) are not the Schur covers (2I, 2T).

3. **S₄'s two double covers.** We built **GL(2,3) = 2·S₄** (transpositions lift
   to involutions). **2O**, the binary octahedral group, is the *sibling*
   double cover — order 48, non-isomorphic, transpositions lift to order 4. It
   is not an SL(2,q), so we cited it rather than rebuilding it. If you have a
   clean realization of 2O, that's the one gap to close.

**The top bridge** W(E₆) ⊂ Sp₆(2) = W(E₇)/± we closed by the index arithmetic
**[Sp₆(2) : W(E₆)] = 28** (the 28 bitangents; |Sp₆(2)| = |W(E₇)|/2 = 1451520),
against our sealed SM-003 / SM-015 — we did not rebuild the 2.9M-element W(E₇).

So both towers now stand machine-checked side by side: **Tower A** (spine,
SM-020) and **Tower B** (covers & bridges, SM-021). The one thing sitting
*above* Tower B is your open question — **is there an exact overgroup
containing the full spine (Sp₆(2), E₇, or above)?** That's the natural next
joint target, and it's pure group theory.

— Selina (with Claude)

*Enclosures: `verify_tower_b.py`, `verify_tower_b.log`, `SHA256SUMS.txt`. Not RH/GRH.*
