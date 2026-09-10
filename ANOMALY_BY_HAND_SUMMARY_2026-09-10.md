# THE ANOMALY BY HAND AND THE DOUBLED CLOCK — SUMMARY OF SM-063 AND SM-064 (2026-09-10)

**Stenberg side · with Claude. Written as §7.12 of
`joint_paper/Roof_and_Clock_DRAFT.md`, in the draft's three-tier shape:
what is classical is cited, what is computed is graded, what is read
is marked. Sources: Stone AY (`STONE_AY_D5_BY_HAND.md`, brief locked
bc815042… before code; 20 PASS + 5 FAIL) and Stone AZ
(`STONE_AZ_DOUBLED_CLOCK.md`, brief locked 45d75b30… before code;
11 PASS + 2 FAIL). One error in the auditor's own mathematics (Stone
AY's Lemma A) is reported in §7.12.2(c) at full size. Not RH/GRH.
Rule 3 throughout.**

## 7.12 The anomaly by hand, and the doubled clock

### 7.12.1 What is classical

The spin representation of B_n is minuscule; its poset is the shifted
staircase δ_n, its weights the 2^n sign patterns (±½)^n, its Weyl group
the hyperoctahedral group of signed permutations, which is also the
symmetry group of the n-cube on those vertices. Rowmotion on J(δ_n)
has order 2n = h(B_n) (Rush–Shi 2013, for minuscule posets in general;
here that is the statement, not a reframing). The D_{n+1} half-spin has
the same poset and the same rowmotion, with W(B_n) ⊂ W(D_{n+1}). On
the D_n vector representation (weights ±e_i, minuscule, h = 2n − 2)
the poset is the double-tailed diamond and rowmotion is a
(2n−2)-cycle on ±e₁..±e_{n−1} times the transposition of ±e_n.

W(B_n) acting on the 2n points ±e_i is the centralizer in Sym(2n) of
the antipode ι = −1, the stabilizer of the pairing {e_i, −e_i}; its
conjugacy classes are the signed cycle types; a positive j-cycle of a
signed permutation is two j-cycles on the 2n points and a negative
j-cycle is one 2j-cycle, so the sign character of Sym(2n) restricted to
W(B_n) is (−1)^{number of negative cycles}, and W(D_n) = W(B_n) ∩
Alt(2n). W(B₄) acts on the 4-cube's vertices, read as F₂⁴, as the
affine maps x ↦ πx + v with π a coordinate permutation. A dihedral
group of order 2m has two conjugacy classes of reflections when m is
even and one when m is odd; when m is even the outer automorphisms
that swap the two classes are not inner.

### 7.12.2 What was computed (SM-063, SM-064)

**(a) The 4-cube's half-turn is a Weyl element on one orbit [P + C].**
Notation from §7.9: I_k = {g ∈ W : R^{−k}gR^k ∈ W} the grammar two
instants share, C_k = C_W(R^k), and the *transport* g ↦ R^{−k}gR^k on
I_k. SM-058 found the one exception in the family to I_k = C_k off the
chains and vectors: the D₅ half-spin, located by SM-060 on the B₄
spinor (the 4-cube, W of order 384, R of order 8 with two free orbits
O₁ ∋ λ and O₂), with |I₄| = 8 against |C₄| = 4. The mechanism, derived
by hand and then checked (AY3–AY8):

- R⁴ coincides on the whole of O₂ with −τ, τ = (e₂e₃)·(−e₄), an
  element of C₄; on O₁ it coincides with no Weyl element (the nearest
  agrees on at most 4 of its 8 points).
- O₂ affinely spans F₂⁴, so its pointwise stabilizer in W is trivial:
  a Weyl element is determined by what it does on O₂.
- **Lemma B.** If w ∈ W and Y = Fix(R^k w⁻¹) has trivial pointwise
  stabilizer in W, then I_k ∩ Stab_W(Y) = C_W(R^k w⁻¹) and there the
  transport is conjugation by w. (Proof: for g ∈ I_k preserving Y,
  c⁻¹gc ∈ W agrees with g on Y.)
- Hence I₄ = C_W(c) for the correction c = (−τ)R⁴, an involution that
  is the identity on O₂ and fixed-point-free on O₁: eight elements,
  the four extras being those that commute with c but not with τ. The
  transport on I₄ is conjugation by τ, which explains SM-060's recorded
  permutation of the extras (the two reflections swap, the signed
  4-cycle and its inverse swap), and [E1, R⁴] = −1: an extra commutes
  with the half-turn up to the antipode.
- By hand: Stab_W(O₁) is sixteen affine maps whose image in S₄ is the
  dihedral stabilizer of the pairing {14|23}, kernel ±1; I₄ is the
  preimage of the Klein four-group; sixteen Weyl elements swap the two
  orbits and none is in I₄. In binary phases along each orbit, C₄ acts
  by translations {000,111,001,110} on O₁ and {000,111,011,100} on O₂,
  and R⁴ is the translation 100 on both — in C₄'s image on O₂ only.
- The D₅ lag-3 survivor (e₁e₃)(e₂e₅) falls to the same lemma with the
  nearest Weyl element w₃ (unique at Hamming distance 7; its agreement
  set of nine points determines W(D₅)): it commutes with R³w₃⁻¹, and
  its lag-5 partner is its transport. Registered guess, CONFIRMED.
- The anomaly sits on B₄, where the reverser −1 is central: it is not
  tied to D₅'s non-central reverser (the question left in §7.11.4).

**(b) The vector boards' grammar is the centralizer of the doubled
clock [P + C].** Three lemmas, proved before code and checked exactly:

- **Lemma C.** If an involution ι centralizes W and reverses R, then
  I_k ⊆ C_W(R^{2k}). (The transport h is fixed by ι, so R^kgR^{−k} =
  R^{−k}gR^k.) Checked at every lag on the eleven boards with such an
  ι: the seven with −1 ∈ W (D₄ ×3, D₆ ×3, B₄) and the five whose
  antipode is not a Weyl element (A₃ω₂, A₅ω₃, A₇ω₄, D₅ω₁, D₇ω₁; §7.11).
- **Lemma D.** On the D_n vector boards (n ≥ 3, D₃ = A₃ω₂) it is an
  equality: I_k = C_W(R^{2k}). (For g commuting with R^{2k} the
  transport commutes with ι, hence lies in W(B_n), and has the sign of
  g on the 2n points, hence lies in W(D_n).) Checked as sets on D₃..D₇
  at every lag. SM-058's "gcd(k, n−1) pattern" on the vectors is this
  theorem: |I_k| = |C_W(ρ^{2k})|, and the guess I_k = C_k failed there
  exactly because C_W(R^{2k}) ⊋ C_W(R^k) off the half-turn.
- **Lemma E.** A transport preserves the unsigned cycle type and the
  sign, so it changes a signed cycle type only by trading two negative
  j-cycles for one positive 2j-cycle. No element of W(B_n) makes such
  a trade; and g is W-inner (its transport is w⁻¹gw for some w ∈ W)
  if and only if the signed types agree — the split D_n classes never
  separate g from its transport (registered, CONFIRMED). Every
  non-inner count of SM-063 is reproduced to the element: D₃ 2 of 4;
  D₅ 4 of 8 at the odd lags and 18 of 32 at lags 2, 6; D₇ 6 of 12 at
  the lags coprime to 6 and 252 of 384 at lags 3, 9; none on D₄, D₆.
- D₃ by hand: I₁ = W(D₂), the Klein group of coordinates 1, 2; the
  transport swaps the reflection s_{e₁−e₂} and the double flip — a
  transposition of S₄ traded for a double transposition.
- At every lag coprime to n − 1 the grammar is dihedral of order
  2(n−1) [obs, post-reveal]. The transport preserves its cyclic half.
  For n odd it is the outer automorphism swapping the two reflection
  classes, and the inner half is exactly the cyclic half; for n even
  there is one reflection class and the transport is conjugation by
  the half-turn R^{h/2} (a Weyl element, §7.6) or by w₀R^{h/2}. The
  reason is one line: on C_W(R^{2k}) the transport equals conjugation
  by any odd power of R^k, and h/2 = n − 1 is such a power exactly when
  n is even. A registered guess that the realising pair lies in
  C_W(R^{2k}) was INVERTED; the pair is {R^{h/2}, w₀R^{h/2}}.

**(c) The auditor's error, at full size.** Stone AY's brief stated and
"proved" a Lemma A: I_k = ⋃_{w∈W} C_W(R^k w⁻¹). The proof read
"R^{−k}gR^k ∈ W" as "R^{−k}gR^k = w⁻¹gw for some w ∈ W", which is only
the converse. The inclusion ⊇ holds; equality holds if and only if
every transport is W-conjugate to its element. Measured: equality on
B₄ and D₅ at every lag; failure on the B₃ spinor (8 of the 16 elements
of I₃), on A₃ω₂ and on the odd D_n vectors — the very elements of (b).
The machine found the error (the first run hung on the impossible set
cover it produced; that log is kept). Lemma B never used Lemma A and
stands. Two further post-reveal guesses in Stone AY (that the
non-inner transports are antipode-conjugation, or inner in W(B_n))
failed; Lemma E says why. Across the 98 anomalous (board, lag) pairs
of SM-058's table the picture is a dichotomy: on 83 a single Weyl
element realises the transport, on 15 some transports leave their
Weyl class outright; never does a pair need two. The B₃ spinor's
non-inner transports are inner in the overgroup W(D₄) ∋ R³ (SM-060);
the vectors' are inner nowhere below Sym(2n).

### 7.12.3 What is identified, and what is read

Identified (mathematics): the family's one exception has a mechanism
and the family's vector boards have a law. On the 4-cube the clock's
half-turn is a symmetry of the board on one of its two orbits, and one
orbit is enough to know a symmetry by; the shared grammar is the Weyl
centralizer of the correction that makes the half-turn a symmetry on
the other orbit too. On the boards whose only reverser is the antipode
the grammar two instants share is the grammar the clock's double
keeps, and the clock carries it forward by an automorphism that a
Weyl element can copy exactly when the half-turn is an odd step of
the clock.

Read [I], marked: SM-061 said no marker survives a tick and only orbit
averages do; SM-063 says that where a marker does survive the
half-turn (the four extras), it is because the half-turn is, for half
the board, one of the board's own symmetries. The exception is not a
crack in the rule; it is the rule seen from inside one orbit.

### 7.12.4 Open

Why the orbit not containing λ is the one on which the half-turn is a
Weyl element (a proof, not a computation). Boards without a W-central
reverser (the E₆ 27, the D_odd half-spins, A_n ω_k with 2k ≠ n + 1):
Lemma C does not apply and nothing is claimed. Whether C_W(R^{2k}) ⊆
I_k beyond the vectors: it is strict on A₅ω₃, A₇ω₄ and the D₆
half-spins at the half-turn. Which group the vectors' outer transports
are inner in, if any short of Sym(2n).
