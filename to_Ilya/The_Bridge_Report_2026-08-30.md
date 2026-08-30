---
title: "The Bridge — Where Scar-Cat and Merkabit Actually Meet"
subtitle: "Closing the 'Bridge' conjecture row: an E₆-level no-go, an E₇-level home, and the S₃ we both already knew"
author: "Selina Stenberg, with Claude (Anthropic Fable 5)"
date: "2026-08-30"
---

Dear Ilya,

Your registry keeps an open conjecture row that has been sitting between us
since May:

> **Bridge** | Merkabit dual-spinor = 2χ₈ via E₆ → PSL(2,7) | *Explicit
> functor missing*

This report closes it. Not the way either of us guessed — the answer is
better than the guess. Everything below is computed by the enclosed
`verify_tbr_bridge.py` (Python 3 + numpy, 20 checks, all passing; classical
inputs are labelled as such), companion to the verification report you
already have.

The one-sentence answer first:

> **Our two frameworks do not meet at E₆. They meet at E₇ — inside
> Sp₆(2) = W(E₇)/{±1}, the symmetry group of the 28 bitangents of your own
> Klein quartic. There, my W(E₆) is the stabilizer of a single bitangent,
> your PSL(2,7) is the group permuting all 28, and the intersection is
> exactly S₃ = N(⟨z₃⟩) — your "universal stabilizer", which my audit's T4
> thread had independently proved canonical on my side.**

Both of us had already found the meeting point. Neither of us knew what it
was.

---

## 1. Why the bridge was never at E₆ (you proved this first)

Your S-15 row disproved PSL(2,7) ⊂ W(E₆) — 7 ∤ 51840. It goes further than
you noted: the automorphism group of the 27-lines incidence structure *is*
W(E₆), so your group cannot act on the 27 lines/states preserving anything
E₆-flavoured; and since 168/27 ∉ ℤ, PSL(2,7) has no transitive action on 27
objects at all. Every direct 168-on-27 attempt was arithmetically dead
before it started. S-15 was not a defeat; it was the signpost saying
*go up one level*.

## 2. The cyclotomic bridge was the field-level shadow

Our merged registry's PB-01 (ℚ(ζ₂₁), Galois group C₆×C₂ of order 12,
ℚ(ζ₃) ∩ ℚ(ζ₇) = ℚ) is verified — and it sharpens into something worth
saying precisely. The three quadratic subfields of ℚ(ζ₂₁) are computed to
be:

- **ℚ(√−7)** — *your character field*: the only irrationality PSL(2,7)
  produces is χ₃(7A) = (−1+√−7)/2, and your curve X(7) has CM by ℚ(√−7)
  (your note-7 §5.5, Hecke/Elkies);
- **ℚ(√−3)** — *our field*: the Eisenstein ω, the trit, the E₆/A₂ ternary
  world;
- **ℚ(√21)** — their forced product ((g₃g₇)² = +21), the compositum's own
  signature, and notably *real*.

So the cyclotomic bridge is exactly the two frameworks' character fields
laid side by side, **linearly disjoint** — at field level we touch only in
ℚ. That disjointness is not a disappointment; it is the arithmetic preview
of the group-level answer: small, precise intersections, not identity.

## 3. The E₇-level home, computed

Classical setting: a genus-3 curve (yours included) has H₁(X,𝔽₂) ≅ 𝔽₂⁶ with
a symplectic form; the 64 quadratic refinements split into 36 even + 28 odd
theta characteristics; the odd ones are the 28 bitangents; the symmetry of
this configuration is Sp₆(2) ≅ W(E₇)/{±1}, order 1,451,520.

Now the computation (your group realized as GL(3,𝔽₂) acting on V ⊕ V*,
everything counted explicitly):

1. The 64 refinements split **36 + 28** by zero-counts, as they must.
2. **Your group fixes exactly one even form** — and the stabilizer of an
   even form in the full Sp₆(2) has order 1451520/36 = 40320 = **8!**
   (O₆⁺(2) ≅ S₈). This is where your 8 points of P¹(𝔽₇) live: your 8-point
   world is the unique even theta characteristic PSL(2,7) preserves. Your
   orbits on the 36 evens come out **[1, 7, 7, 21]** — the fixed form, the
   Fano plane's 7 points, its 7 lines, and its 21 flags. (A small new fact;
   yours if you want it.)
3. **Your group is transitive on the 28 odd forms** — Klein's group
   permuting the bitangents of its own quartic — with stabilizer of order
   6, nonabelian: an S₃, computed to be **exactly N(⟨z₃⟩)**. Your
   "Bijection" row (odd theta characteristics ≅ PSL(2,7)/S₃, unique
   homogeneous G-set) was describing the bitangent action all along; its
   permutation character is χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈.
4. **The stabilizer of one odd form in the full Sp₆(2) has order
   1451520/28 = 51840 = |W(E₆)|** (O₆⁻(2) ≅ W(E₆), classical). That is my
   framework's group, sitting inside the bitangent geometry as the
   point-of-view of a single bitangent — from where the remaining 27
   organize themselves into the 27 lines, my crystal's world.
5. **56 = 2 × 28, structurally.** The map z₃ ↦ N(⟨z₃⟩) is *exactly 2-to-1*
   from your 3A class (56 elements) onto the 28 bitangent stabilizers. So
   your row 154 — "56 = |class 3A| = dim(min rep E₇)", filed as Structural —
   acquires honest content: your 3A class is canonically the double cover of
   the bitangents, by the same ±-doubling that turns the 28 bitangents into
   the 56 of E₇. (On my side, the E₇ minuscule crystal has 56 vertices and
   its two-gate dynamics generates S₅₆ — the object your 154 was pointing
   at, one floor up from both of us.)

**The picture:** stay at one bitangent of the Klein quartic and you see
W(E₆) and the 27 lines — my framework. Move among all 28 and you see
PSL(2,7) — yours. The only symmetry compatible with both viewpoints is
S₃ = N(⟨z₃⟩): your universal stabilizer, my strata theorem's canonical S₃.
Neither framework contains the other. They are two subgroups of one
classical geometry, and their intersection is small, nontrivial, and
*exactly the object both registries had independently promoted.*

## 4. The explicit functor (your Bridge row, closed)

At Lie level, PSL(2,7) genuinely acts on the 27 — through E₆(ℂ), in two
inequivalent classical ways, and the restriction functor your row asked for
is computed in both:

- **Trinification route.** E₆ ⊃ SU(3)³ with 27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)
  (classical). Embed PSL(2,7) diagonally by *your own* representation χ₃ —
  the one whose invariant quartic is the Klein curve. Each 9-block restricts
  to χ₃⊗χ̄₃ = χ₁ ⊕ χ₈ (computed exactly), so

  **27 |_PSL(2,7) = 3χ₁ ⊕ 3χ₈ — three copies of (singlet ⊕ octet).**

  Your Jordan row 156 ("27 = 3 + 24") comes true in corrected form:
  3 singlets + 3×8, i.e. 24 = 3·dim(χ₈), not |7A|.
- **G₂/octonion route** (classical): PSL(2,7) ⊂ G₂ = Aut(𝕆) with 7 = χ₇ —
  your row 157, octonion multiplication from Fano lines — and
  27 = J₃(𝕆) branches as **6χ₁ ⊕ 3χ₇**.

Verdict on the row as written: "= 2χ₈" is refuted (16 dimensions fit no
natural restriction of the 27); "explicit functor missing" is closed — the
functor is restriction along either embedding, and the headline is
3(χ₁ ⊕ χ₈). Per the house rule we now share: these are theorems about
representations. Whether they are physics is a separate question, and it
stays parked.

## 5. What I'd propose we do with this

1. Move your **Bridge** row from open conjecture to a theorem-pair:
   *(a)* E₆-level no-go (your S-15, extended), *(b)* E₇-level common home in
   Sp₆(2) with intersection S₃, plus the two Lie functors — each backed by
   the enclosed verifier.
2. Upgrade rows **154** (3A ↦ bitangents, 2:1) and **Bijection** (= the
   bitangent action, permutation character χ₁⊕2χ₆⊕χ₇⊕χ₈) from Structural to
   computed statements; take the even-side orbit fact [1,7,7,21] as a new
   row if it pleases you.
3. Adopt the bridge as the *organizing frame* for the merged registry: your
   lane and mine as the two point-of-view subgroups of the bitangent
   geometry, meeting in S₃ — with the cyclotomic bridge as its field-level
   shadow (√−7 yours, √−3 mine, √21 the handshake).

After a summer in which my audit refuted most of what our frameworks
*claimed about the world*, this is the first genuinely constructive
cross-framework theorem — found with the same rule that did the refuting:
compute, never assert. It seems fitting that what survives of both
programs meets on your curve, at my Weyl group's doorstep, in the one
little S₃ we had each already circled.

Warmly,

Selina
(prepared with Claude, Anthropic Fable 5, 2026-08-30)

*Enclosed: `verify_tbr_bridge.py` (all claims above), alongside the earlier
`verify_tsc_scarcat.py` and verification report.*
