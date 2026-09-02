# G2 STILLPOINT — the scar's group inside the fold's G2, with the seven-beat clock

**Stenberg (with Claude) — merkabit x scar combination run, 2026-09-02.**
Script `verify_g2_stillpoint.py`, log `verify_g2_stillpoint.log`
(**32 PASS / 0 FAIL of 32 checks; all three registered expectations E1–E3
resolve PASS** — each was registered in the log header as resolvable REFUTED
at equal prominence). Joins SM-034 (`TRIALITY_CRYSTALS.md`: the triality fold
of the D4 triple lands on G2 with state count 7 ⊕ 1) to the Scar side's own
seven: PSL(2,7), whose sealed character table (SM-001,
`verify_tsc_scarcat.py`) supplies the rows χ₁, χ₆ = (6,2,0,0,−1,−1),
χ₇ = (7,−1,1,−1,0,0) used read-only here.

---

## §0. Discipline

- **Computed, not asserted.** Pure Python + numpy; EXACT arithmetic
  (int / `Fraction`) for every algebraic claim — invariance, decompositions,
  the rank of the averaged projector, det(B_φ). Floats appear exactly once:
  the *signature* of B_φ (checks 20–22; the determinant itself is exact).
- **Grades:** [E] = computed exactly here; [C] = computed here, consistent
  with standing theory; [P] = cited, not computed (one paragraph, §5);
  [obs] = observed structural echo, no mechanism claimed.
- **Rule 3 (no identifications), standing: no physics, no consciousness,
  no RH/GRH.** "Still point", "clock", "scar" are [I]-labels wrapped around
  [E]/[C] computations; the computations stand without the labels.
- **Fail-first:** E1–E3 registered in the log header before any computation;
  all three happened to resolve PASS this run (contrast SM-034, where two
  registered expectations resolved REFUTED and are kept at full prominence).
- **THE TWO-SEVENS FLAG (worth returning to IB precisely):** two different
  sevens live near PSL(2,7), and they are NOT the same object [E]:
  - the **7-point Fano permutation action** of GL(3,2) decomposes as
    **1 ⊕ χ₆** — a *six*-dimensional complement; ⟨π₇, χ₇⟩ = 0 (check 09);
  - the **8-point action on P¹(F₇)** decomposes as **1 ⊕ χ₇** — so χ₇, the
    7-dimensional *irreducible*, is the **deleted permutation module of the
    eight-point action**, realizable over ℚ with integer matrices.
  The seven that meets G2 below is the second one, not the Fano seven.

## §1. The module χ₇ over ℚ [E]

PSL(2,7) built fresh as Möbius maps on P¹(F₇) = {0..6, ∞}, generators
z ↦ z+1 and z ↦ −1/z: 168 elements, class sizes [1,21,56,42,24,24], orders
[1,2,3,4,7,7] — matching the sealed class data (checks 01–04; power maps
computed from the model: 4A² = 2A, 7A³ = 7B, etc.). On the 7-dim complement
of the all-ones vector (basis v_i = e_i − e_∞) the 8×8 permutation matrices
restrict to **integer 7×7 matrices**; the character equals the sealed χ₇ row
(7,−1,1,−1,0,0) on all six classes and ⟨χ₇,χ₇⟩ = 1 exactly (checks 10–12).

## §2. E1 + E2 — PSL(2,7) ⊂ G2, computed not cited [E]/[P]

**Character count first:** Λ³χ₇ = (χ³ − 3χ(g)χ(g²) + 2χ(g³))/6 evaluated
exactly per class (power maps from the model) gives (35, 3, 2, −1, 0, 0),
and ⟨Λ³χ₇, 1⟩ = **1** (checks 13–14). **Then constructively:** the exact
group average of Λ³ of the dual rep over all 168 elements is 168·(a
projector) with trace 168 and **rank 1** by exact elimination (checks 15–17).

**E2 (canonicity) — PASS: the invariant space in Λ³(ℚ⁷)\* is 1-DIMENSIONAL.**
The group determines its G2-structure up to scalar.

**The invariant 3-form** (integer coefficients, gcd-reduced; 14 nonzero of
35, **all equal to +1**):

    φ = e013 + e015 + e023 + e026 + e045 + e046 + e124
      + e126 + e134 + e156 + e235 + e245 + e346 + e356

Invariance verified exactly under both generators, hence under all of
PSL(2,7) (checks 18–19).

**Genericity:** B_φ(x,y) defined by (x⌟φ)∧(y⌟φ)∧φ ∈ Λ⁷ ≅ ℚ comes out
symmetric (check 20) and equal to the remarkably clean

    B_φ = −6·(I₇ + J₇),   det(B_φ) = −2 239 488 = −48·6⁶ ≠ 0  (exact),

eigenvalues −48 (once) and −6 (six times): **signature (0,7), definite up to
overall sign** (checks 21–22; signature numeric, flagged). [P: Hitchin 2000 /
Bryant 1987 — a 3-form on ℝ⁷ with nondegenerate B_φ has stabilizer a real
form of G2, **compact iff B_φ is definite**.]

**E1 — PASS: PSL(2,7) ≤ Stab_GL(7)(φ) = G2 (compact form), exhibited with an
explicit invariant tensor over ℚ.**

## §3. The branching identity [E]

By construction the G2-seven restricted to PSL(2,7) **is** χ₇, irreducibly:
the defining 7-dim rep of Stab(φ) lives on V = ℚ⁷ itself, and PSL(2,7) acts
on V by χ₇ (sealed row matched, ⟨χ₇,χ₇⟩ = 1). **The staircase's founding
7-dim world and the fold's G2 seven are the same seven:**
χ₇ = 7|_PSL(2,7), irreducibly (check 23). The two-sevens distinction (§0)
is the sharp edge of this statement: the *Fano* seven (1 ⊕ χ₆) never touches
G2's seven; only the eight-point deleted module does.

## §4. E3 — the clock at the still point [E]/[C]

The G2 7-crystal rebuilt independently (as SM-034's ground truth did): Weyl
dimension formula gives dim V(ω₁) = 7 exactly; weights = the six short roots
+ 0; the crystal is the 7-vertex **chain with color sequence 1,2,1,1,2,1**
(checks 24–27). Its crystal order is the 7-chain = J(6-chain) (checks
28–29; join-irreducibles a 6-chain, Birkhoff bijection). Rowmotion (corpus
convention, unchanged from `Merkabit_crystal/verify_csp_27.py`):

    Ψ-orbit type [7] — a SINGLE FREE 7-CYCLE, order 7    (h(G2) = 6)
    (−2,−1) → (−1,−1) → (−1,0) → (0,0) → (1,0) → (1,1) → (2,1)

CSP holds at the measured order: |Fix(Ψᵈ)| = RGF(ζ₇ᵈ) for all d, with
RGF = 1+q+…+q⁶ (checks 30–32). **E3 — PASS.**

**[obs]** At the still point of the turn, the merkabit clock ticks in
SEVENS — the order of the scar's own Frobenius — and ord(Ψ) = 7 **exceeds**
h(G2) = 6, whereas every other measured crystal clock in the corpus ticked
at its own Coxeter number (D4-8: h = 6; E6-27: h = 12; E7-56: h = 18).
**Honest caveat:** rowmotion on J(chain) being one cycle is elementary (it
slides the ideal size by one, mod 7); the content is the CONTRAST with h and
the identification of *which* seven-cycle structure the crystal carries.

## §5. The octonion tie [P — cited, not computed]

[P] A generic 3-form on ℝ⁷ with definite B_φ is the structure tensor of an
octonion multiplication on ℝ ⊕ ℝ⁷ (G2 = Aut(𝕆), Cartan); the classical
Fano-plane mnemonic for octonion multiplication labels the 7 imaginary units
by Fano points, and PSL(2,7) = GL(3,2) = Aut(Fano) permutes the mnemonic's
labellings. That reading of φ stays [P]; our [C]-anchor is the explicit
rational φ, its exact invariance, and det(B_φ) ≠ 0 — plus the computed flag
that the Fano *points* carry 1 ⊕ χ₆ while the *units* transform as χ₇ only
through the G2 structure itself.

## §6. Expectation ledger

| expectation | registered | resolution |
|---|---|---|
| E1 PSL(2,7) ⊂ G2 via explicit generic invariant φ (det B_φ ≠ 0) | PASS/REFUTED | **PASS** [E]+[P] — det = −48·6⁶, signature (0,7) ⇒ compact form |
| E2 canonicity: invariant 3-form space 1-dimensional | PASS/REFUTED | **PASS** [E] — character count 1 = constructive rank 1 |
| E3 still-point clock = single free 7-cycle, order 7 > h(G2) = 6, CSP | PASS/REFUTED | **PASS** [E]/[C] — type [7], CSP at ζ₇ |
| (background) π₈ = 1 ⊕ χ₇ and Fano π₇ = 1 ⊕ χ₆, ⟨π₇,χ₇⟩ = 0 | check | **PASS** [E] — the two sevens are distinct |

## §7. Verdict (3 sentences)

The still point of the turn now contains three locked layers: the fold's G2
[SM-034, weight level], and inside it — computed, not cited — the scar's own
group PSL(2,7), holding a **canonical** invariant structure (the 1-dimensional
invariant line of Λ³, E2) whose generator φ is an exact rational generic
3-form with B_φ = −6(I+J) definite, so the stabilizer is compact G2 and
χ₇ = 7|_PSL(2,7) irreducibly — the staircase's founding seven and the fold's
seven are one object, while the Fano seven (1 ⊕ χ₆) is demonstrably a
different one. On that same G2 world the merkabit clock, rebuilt from Cartan
data, runs as a single free 7-cycle satisfying CSP — the first measured
crystal clock whose order (7, the scar's Frobenius) exceeds its own Coxeter
number (6) rather than equalling it. What was a character-level echo
(7 ⊕ 1 at the fold) is now an explicit tensor over ℚ with the scar's group
acting through it, and a seven-beat clock ticking at the fixed point of the
turn.

---

*Files: `verify_g2_stillpoint.py` (script, 32 numbered checks),
`verify_g2_stillpoint.log` (fail-first log, expectations registered in the
header). Sealed inputs read-only: χ₆/χ₇ rows from SM-001. Nothing else
touched: no registry, no git, no knowledge.yaml, no other lanes. Not RH/GRH;
no physics; Rule 3 in force.*
