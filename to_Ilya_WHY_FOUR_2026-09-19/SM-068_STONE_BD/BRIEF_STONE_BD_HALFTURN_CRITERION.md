# BRIEF — STONE BD: THE HALF-TURN CRITERION (WHY THE 4-CUBE, IN ONE SENTENCE)

**Staged 2026-09-19 on Selina's word ("do 1 first then 2"), after SM-067 (Stone
BC). Locked before code (`BRIEF_STONE_BD_LOCK.sha256`); the verifier re-checks
this file's hash as its first test. Registered guesses below are guesses and
will be reported INVERTED at equal prominence if the data says so. Builds on
SM-060 (Stone AV), SM-063 (Stone AY, Lemma B), SM-066 (Stone BB), SM-067
(Stone BC). Merkabit-side mathematics. Registry row SM-068. Rule 3: "clock",
"half-turn", "grammar" are labels for permutations and subgroups.**

## 0. What SM-067 exposed

On the B₄ spinor board the half-turn R⁴ agrees with the Weyl element −τ on the
orbit O₂, the correction c = (−τ)⁻¹R⁴ is an involution, and C_W(c) = I₄ has
order 8 against |C₄| = 4 (SM-063). On B₈ the half-turn R⁸ agrees with the
Weyl element w = −(e₂e₃)(e₄e₅)(e₆e₇) on two orbits — the same shape — but the
correction c = w⁻¹R⁸ is **not** an involution (cycle type 8⁸ 4¹² 3¹² 2²⁸ 1⁵²)
and C_W(c) = {±1} = C₈ (SM-067). The difference between the two boards is not
in the mechanism (Lemma B holds on both) but in the correction. This stone
asks for the reason in one sentence, proves what proves, and tests the rest on
every B_n spinor board that is enumerable, n = 3..8.

## 1. Setting and notation [P, sealed]

Board Wλ with Weyl group W, clock R of even order h, m = h/2, so R^m is an
involution and R^{−m} = R^m. I_k = W ∩ R^k W R^{−k}, C_k = C_W(R^k), C_k ⊆ I_k.
For w ∈ W the *correction* is c = w⁻¹R^m and Y = Fix(c) = {x : w(x) = R^m(x)},
the agreement set of w with the half-turn. **Lemma B (SM-063):** if the
pointwise stabilizer of Y in W is trivial (on the spinor boards: Y affinely
spans 𝔽₂ⁿ), then I_m ∩ Stab_W(Y) = C_W(c), and on this set the transport
g ↦ R^{−m} g R^m is conjugation by w. Since C_W(c) preserves Fix(c) = Y, always
C_W(c) ⊆ Stab_W(Y).

A *nearest Weyl element* to R^m is a w ∈ W maximising |Fix(w⁻¹R^m)|; on B₈ it
was unique and equal to the carrying element (SM-067 BC4b).

## 2. The lemmas (proved here; the verifier checks them as computations)

**Lemma BD-A (when the correction is an involution).** c² = 1 if and only if
R^m w R^m = w⁻¹. If w is an involution this says exactly w ∈ C_W(R^m).

*Proof.* c² = w⁻¹R^m w⁻¹R^m = 1 ⇔ R^m w⁻¹ R^m = w ⇔ (inverting both sides,
R^m being an involution) R^m w R^m = w⁻¹. For w² = 1 the last condition reads
R^m w R^m = w. ∎

**Lemma BD-B (the extras when w commutes with the half-turn).** Let
w ∈ C_W(R^m) and c = w⁻¹R^m. Then w, R^m and c pairwise commute, and for
g ∈ W any two of the three statements "g commutes with w", "g commutes with
R^m", "g commutes with c" imply the third. Consequently, when Y = Fix(c) has
trivial pointwise stabilizer,

  I_m ∩ Stab_W(Y) = C_W(c) ⊇ C_W(w) ∩ C_m,   and   (I_m ∩ Stab_W(Y)) ∖ C_m = C_W(c) ∖ C_W(w);

w itself lies in C_W(c) ∩ C_m and is never an extra.

*Proof.* c w = w⁻¹R^m w = w⁻¹ w R^m = R^m = w w⁻¹ R^m = w c, so w and c
commute, and both commute with R^m = wc. If g commutes with two of w, c and
R^m = wc, it commutes with the product or the quotient that is the third. The
rest is Lemma B together with the observation that, for g ∈ C_W(c), "g ∉ C_m"
is the same as "g ∉ C_W(w)". ∎

**Corollary BD-C (the sentence).** On a board where Y = Fix(w⁻¹R^m) is
spanning and I_m ⊆ Stab_W(Y): *the shared grammar at the half-turn exceeds the
centralizer if and only if some Weyl element commutes with the correction but
not with the half-turn;* and if w is an involution commuting with the
half-turn this reads: *iff some Weyl element commutes with c but not with w.*
When w is an involution that does **not** commute with the half-turn, c is
not an involution (BD-A), and nothing forces C_W(c) beyond ⟨±1⟩ ∩ … — the
guess below is that it then collapses.

## 3. Registered guesses (before code)

- **BD1 [C, B₄].** With w = −τ: w ∈ C₄, c² = 1, |Stab_W(O₂)| = 16, I₄ ⊆
  Stab_W(O₂), I₄ = C_W(c) of order 8, and the four extras are exactly
  C_W(c) ∖ C_W(w) (SM-063's "commute with c but not with τ", now as BD-B).
- **BD2 [C, B₈].** With w = −(e₂e₃)(e₄e₅)(e₆e₇): w ∉ C₈, c² ≠ 1 (BD-A),
  C_W(c) = {±1}. **Guess:** Stab_W(Fix c) = {±1} as well — the agreement set
  of 52 points has no Weyl symmetry beyond the antipode, so the collapse is
  already in the stabilizer.
- **BD3 [C, B₃ inside W(B₃)].** R³ is a Weyl element of W(D₄) but not of
  W(B₃) (SM-060); |I₃| = 16, |C₃| = 8 in W(B₃). A nearest Weyl element
  w ∈ W(B₃) to R³ has a spanning agreement set, Lemma B applies, and
  **guess:** w ∈ C₃, c² = 1, and the eight extras are C_W(c) ∖ C_W(w) —
  the B₃ anomaly falls under the same sentence without invoking the overgroup.
- **BD4 [C, the clean boards B₅, B₆, B₇].** For every nearest Weyl element w
  to the half-turn: w ∉ C_{h/2} (guess), C_W(w⁻¹R^{h/2}) ⊆ C_{h/2}, and
  Lemma B's equality holds where the agreement set spans.
- **BD5 [C, the criterion across six boards — the main guess].** On B₃..B₈:
  I_{h/2} ⊋ C_{h/2} **iff** some nearest Weyl element to R^{h/2} commutes
  with R^{h/2}. (Two positive instances B₃, B₄; four negative B₅..B₈ if the
  guess holds.) Sub-guess BD5b: on every one of the six boards the nearest
  Weyl element is unique up to the antipode (w and −w).
- **BD6 [C, the lemmas as computations].** BD-A and BD-B verified on all six
  boards for every nearest w (and on B₄, B₈ for the carrying w): c² = 1 ⇔
  R^m w R^m = w⁻¹; for w ∈ C_m the "two imply the third" rule on all g ∈ W.

## 4. Method (compute, never assert)

1. Boards and clocks from Stone BC's machinery verbatim (`B_spin`, `rebase`,
   the affine (π, v) engine, `best_agreement`, `enum_commute`, names).
   B₃..B₇ are small; B₈ takes seconds per centralizer.
2. Nearest Weyl elements by the mode method (all attaining (π, v) listed).
3. For each w: c, Y = Fix(c), affine span of Y, C_W(c), Stab_W(Y) (by the
   engine: g with g(Y) = Y), C_W(w), C_m, I_m (from BC where sealed, else
   enumerated), and the set identities of BD-B checked as sets.
4. Fail-first: first run kept as `_FIRSTRUN.log`.

## 5. Bars

BD0 lock; BD1–BD6 as above; each PASS/FAIL/INVERTED with the numbers.

## 6. Not claimed

No statement about boards other than B₃..B₈; no proof that the collapse
(C_W(c) = {±1}) occurs whenever w ∉ C_m — that is BD2/BD4's computation, not a
theorem; nothing about lags other than the half-turn (the D₅ lag-3 survivor is
SM-063's, at a lag where R^{−k} ≠ R^k and BD-A does not apply); nothing
physical.

## 7. Files

`verify_stone_bd_halfturn_criterion.py`, `.log`, `_FIRSTRUN.log`,
`STONE_BD_HALFTURN_CRITERION.md`. Registry row SM-068 on seal; packaging for
Ilya on Selina's word.
