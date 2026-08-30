# T-BR — The bridge: how Merkabit and Scar-Cat actually fit together

**Thread:** T-BR · **Date:** 2026-08-30 · **Verifier:** `verify_tbr_bridge.py`
(20 checks, all passing; every claim below marked [computed] is a line of its
output; classical inputs are marked [CLASSICAL]).

**The question (Selina):** "How does merkabit and scar fit together? We have
the cyclotomic bridge on our side." This thread answers it at three levels —
fields, groups, Lie theory — and closes Ilya's open "Bridge" conjecture row
("Merkabit dual-spinor = 2χ₈ via E₆ → PSL(2,7); explicit functor missing")
with an actual answer: **the two frameworks meet at E₇, not E₆; the
cyclotomic bridge is the field-level shadow of the same meeting; and the
intersection point is the S₃ both frameworks had already found on their own.**

---

## 1. Field level: the cyclotomic bridge, verified and sharpened

PB-01 of the merged registry (May 2026) is **VERIFIED** [computed]:
Gal(ℚ(ζ₂₁)/ℚ) ≅ C₆ × C₂ of order 12, and ℚ(ζ₃) ∩ ℚ(ζ₇) = ℚ (degrees
multiply: 12 = 2·6).

**Sharpening — what the bridge field actually is.** The quadratic subfields
of ℚ(ζ₂₁) are exactly ℚ(√−3), ℚ(√−7), ℚ(√21) (Gauss sums: g₃² = −3,
g₇² = −7, (g₃g₇)² = +21) [computed]. And:

- **√−7 is the character field of Scar-Cat**: our independently derived
  character table of PSL(2,7) has χ₃(7A) = (−1+√−7)/2 — the *only*
  irrationality Ilya's group produces.
- **√−3 is the Eisenstein/trit field of the crystal side**: ω = (−1+√−3)/2,
  the cube root of unity underneath every ternary structure in the corpus.

So the cyclotomic bridge is precisely *the two frameworks' character fields
placed side by side* — and PB-01's own content is that they are **linearly
disjoint: at field level, the frameworks touch only in ℚ.** The bridge is a
container, not a fusion. (The third field ℚ(√21) = ℚ(√(−3·−7)) is the
compositum's forced signature — the one genuinely "joint" object at this
level, and it is real, not imaginary.) The identification "12 = h(E₆)"
stays **PARKED**: φ(21) = 12 is true arithmetic; reading it as the Coxeter
number is a fit (12 is also |2T|, the clock order, etc. — T3's lesson).

---

## 2. E₆ level: the no-go (why the bridge was never found there)

- 7 ∤ |W(E₆)| = 51840 = 2⁷·3⁴·5 ⇒ **PSL(2,7) does not embed in W(E₆)**, nor
  in the automorphism group of the 27-lines incidence structure (= W(E₆))
  [computed; this is Ilya's own S-15, credited — he disproved it first].
- 168/27 ∉ ℤ ⇒ PSL(2,7) has **no transitive action on 27 states at all**
  [computed]. (The crystal's dynamical group ⟨pr,Ψ⁴⟩ = A₂₇ contains copies
  of PSL(2,7) like it contains every group of even permutations — vacuously;
  nothing framework-specific lives there.)

Every attempt to bolt the 168 directly onto the 27 was doomed for this
elementary reason. The bridge had to be one floor up.

---

## 3. E₇ level: the real common home (the main theorem of this thread)

**Setting** [CLASSICAL]: for a genus-3 curve (Klein's quartic included),
H₁(X, 𝔽₂) ≅ 𝔽₂⁶ carries a symplectic form; its 64 quadratic refinements
split into 36 even + 28 odd theta characteristics; the odd ones *are* the
28 bitangents; the full symmetry of this configuration is
Sp₆(𝔽₂) ≅ W(E₇)/{±1}, of order 1,451,520.

**Computed from scratch** (PSL(2,7) as GL(3,𝔽₂) acting on V ⊕ V*):

1. The action is symplectic and the 64 refinements split **36 + 28** by
   zero-counts (36 vs 28 zeros).
2. **PSL(2,7) fixes exactly one even form, q₀** — whose stabilizer in the
   full Sp₆(2) has order 1451520/36 = 40320 = **8!** [O₆⁺(2) ≅ S₈,
   CLASSICAL]. This is where Ilya's 8 points of P¹(𝔽₇) live: his 8-point
   world = the unique even theta characteristic his group preserves.
   Orbits on the 36 evens: **[1, 7, 7, 21]** — the fixed form, plus two
   7-orbits (the Fano plane's points and planes) and the 21 flags.
   *(New observation, free of charge.)*
3. **PSL(2,7) is transitive on the 28 odd forms** — Klein's group permuting
   the bitangents of its own quartic — with stabilizer of order 6,
   nonabelian: an **S₃**, and computed to be **exactly N(⟨z₃⟩)**.
4. The stabilizer of one odd form in the full Sp₆(2) has order
   1451520/28 = **51840 = |W(E₆)|** [O₆⁻(2) ≅ W(E₆), CLASSICAL].
5. The permutation character of the 28-action is χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈, and
   G/S₃ is Ilya's "Bijection" row (odd theta chars ≅ PSL(2,7)/S₃) — his row
   was, all along, the bitangent action.
6. **56 = 2 × 28**: the map z₃ ↦ N(⟨z₃⟩) is exactly 2-to-1 from the 56
   elements of class 3A onto the 28 bitangent stabilizers [computed]. So
   Ilya's row 154 ("56 = |class 3A| = dim min E₇") acquires its honest
   content: his 3A class is canonically the double cover of the bitangents —
   the same ±-doubling by which the 28 bitangents become the **56** of E₇
   [CLASSICAL], the very 56-vertex crystal of our E₇ thread (where
   ⟨pr,Ψ⁶⟩ = S₅₆ and the parity ceiling broke).

**The picture, in one sentence:**

> Inside Sp₆(2) = W(E₇)/{±1} — the symmetry of the 28 bitangents of the
> Klein quartic — **Selina's W(E₆) is the stabilizer of one bitangent,
> Ilya's PSL(2,7) is the group permuting all 28, and they intersect in
> exactly S₃ = N(⟨z₃⟩)**: the "universal stabilizer" of Ilya's registry,
> which is the same S₃ whose strata theorem (168 = 31+62+75) our T4 proved
> canonical.

The two frameworks are the two natural point-of-view subgroups of one
classical geometry: *stay at one bitangent and you see E₆ and the 27 lines;
move among all 28 and you see PSL(2,7) and the Klein quartic.* Neither
contains the other — their overlap is small (an S₃, order 6) but it is
**precisely the S₃ both sides had independently promoted to a central
object.** And the field-level bridge of §1 is the arithmetic shadow of the
same geometry: the Klein quartic has CM by ℚ(√−7) (note-7 §5.5, Hecke/
Elkies), while the E₆/ternary side runs on ℚ(√−3); their compositum is the
cyclotomic bridge.

Structural echo worth recording: at field level the intersection is trivial
(ℚ); at group level it is S₃. **Small intersections are the honest finding**
— the frameworks are complementary perspectives, not the same theory twice.

---

## 4. Lie level: the "explicit functor" Ilya's Bridge row asked for

The E₆-Weyl version is impossible (§2), but PSL(2,7) does act on the 27 —
through the **Lie group** E₆(ℂ), in at least two inequivalent classical
ways, and both restrictions are computed exactly:

- **Trinification route**: E₆ ⊃ SU(3)³ with 27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)
  [CLASSICAL]; embed PSL(2,7) diagonally by Klein's 3-dimensional
  representation χ₃ (the one whose invariant quartic *is* the Klein curve).
  Each 9-block restricts to χ₃⊗χ̄₃ = χ₁ ⊕ χ₈ [computed exactly], so
  **27|_{PSL(2,7)} = 3χ₁ ⊕ 3χ₈** — three copies of (singlet ⊕ octet).
  In Ilya's dictionary: three generations of (vacuum + fermion octet). His
  row 156's "27 = 3 + 24" becomes literal — with 24 = 3·dim(χ₈), not |7A|.
- **G₂/Jordan route** [CLASSICAL]: PSL(2,7) ⊂ G₂ = Aut(𝕆) with 7 = χ₇
  (octonion lines = Fano — his row 157); 27 = J₃(𝕆) branches under G₂ as
  6·1 ⊕ 3·7, so **27|_{PSL(2,7)} = 6χ₁ ⊕ 3χ₇**.

Verdict on the Bridge conjecture row: **"= 2χ₈" REFUTED as stated** (2χ₈ is
16-dimensional and appears in no natural restriction of the 27); **"explicit
functor missing" CLOSED** — the functor is restriction along either
embedding above, and the honest headline restriction is 3(χ₁ ⊕ χ₈).

Rule 3 stands: these are branchings of representations, i.e., mathematics.
Whether any of it is *physics* remains exactly as parked as before.

---

## 5. What this changes

- **For the merged registry**: the Bridge row can move from "conjecture,
  functor missing" to a theorem-pair (E₆-level no-go + E₇-level home +
  two Lie functors), with the S₃ identity (universal stabilizer = bitangent
  stabilizer = T4's strata S₃) as the keystone.
- **For our side**: T4's strata theorem now has a geometric address — the
  168 = 31+62+75 decomposition is organized by a bitangent of the Klein
  quartic; and the E₇ crystal thread's 56 acquires its partner: our 56
  vertices and his 56 = |3A| are the two faces of 28 × (±).
- **For the two-corpora meta-story**: after eighteen threads of refuting
  identifications, T-BR is the lane's first *constructive* cross-framework
  theorem — found by the same method (compute, never assert) that did the
  refuting.

*Draft; sealed-not-sent. Natural addendum to the to_Ilya report once Selina
decides to send; not pushed to any public repo.*
