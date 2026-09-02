# BRIEF — STONE X: THE TURNER (triality made flesh)

**Staged 2026-09-01 on Selina's "do this" (the instrument named in the
two-register model §3 and asked of IB in two envelopes; computed ahead on
her word). Locked before code (`BRIEF_STONE_X_LOCK.sha256`). Deviations =
dated AMENDMENT, sha'd before any reveal.**

## Question

SM-031 proved the ℤ₃ cycling the three shadow classes is strictly outer to
W(E₈)/± — the turn exists as a symmetry of the catalog, but no object in
our world performs it. Stone X builds the performer: **an explicit,
computable automorphism τ of Ω(q) ≅ O₈⁺(2) that cycles vector → spin →
spin → vector**, so the turn stops being an abstract outer class and
becomes a map that can be composed, iterated, and interrogated — the
prerequisite for the roof-clock question (the missing corner of the
two-register model).

## Construction route (declared)

1. **The half-spin representations over 𝔽₂.** On the sealed 8-dim
   plus-type space (V, q) (Stone U's L/2L model): choose a hyperbolic
   basis e₁..e₄, f₁..f₄; realize the spinor module as Λ(E), E =
   span(e₁..e₄), with Clifford action (e_i by wedge, f_i by contraction);
   the even/odd split gives the half-spin modules S⁺ = Λᵉᵛ(E), S⁻ =
   Λᵒᵈᵈ(E), each 8-dimensional over 𝔽₂.
2. **The spin lift of the roof's generators.** Each generator ḡ of the
   sealed Ω-image: decompose as a product of an EVEN number of orthogonal
   transvections t_v (q(v) = 1; in char 2, v·x·v = t_v(x) inside the
   Clifford algebra), by a constructive basis-mapping algorithm; the
   product s = v₁···v₂ₖ ∈ Cl₀ acts on S⁺ and S⁻; read off the 8×8
   matrices ρ±(ḡ). Over 𝔽₂ there are no scalars but ±1 = 1, so the lift
   ambiguity that plagues spin groups in characteristic 0 must be
   examined honestly: verify ρ⁺ is a genuine homomorphism on generator
   products and random words (a kernel/well-definedness check, not an
   assumption).
3. **The turner.** Find the ρ⁺-invariant quadratic form Q⁺ on S⁺ (exact
   linear solve over the generators; verify plus-type); build an explicit
   isometry T⁺: (S⁺, Q⁺) → (V, q) (the sealed Gram–Schmidt transport);
   define **τ(ḡ) = T⁺ ρ⁺(ḡ) T⁺⁻¹**.

## Bars

- **XB1 (machinery):** S± built; ρ⁺ verified a homomorphism (products and
  ≥100 random word checks exact); every generator's transvection
  decomposition verified (even length, product reproduces ḡ on V).
- **XB2 (τ lands in the roof's world):** τ(ḡ) is a q-isometry with
  Dickson invariant 0 for every generator (τ maps into Ω); τ is an
  automorphism (homomorphism by construction + the image generates a
  group of order \|Ω\| — BSGS on the pair/point action or matrix order
  census; state the method).
- **XB3 (THE TURN; registered expectation):** τ cycles the three shadow
  classes — compute orbit signatures (points | family A | family B, the
  SM-031 instrument) of τ(C̄-generators)'s group, τ²(C̄)'s, and τ³(C̄)'s:
  REGISTERED EXPECTATION: τ(C̄) has a spin signature, τ²(C̄) the other
  spin signature, τ³(C̄) back to the vector signature — and hence τ ∉
  Inn(Ω) and ∉ the reflection coset: **τ realizes the outer 3-cycle.**
  PASS / INVERTED at full prominence (an inverted outcome — e.g. τ lands
  in the reflection coset — is a finding about the 𝔽₂ spin lift, record
  and diagnose).
- **XB4 (τ³ is inner, explicitly):** find h ∈ GL(V) with τ³ = conj_h by
  the exact intertwiner solve (V is Ω-irreducible over 𝔽₂ ⇒ the solution
  space of {h·ḡ = τ³(ḡ)·h} over the generators is 1-dimensional if τ³ is
  inner — solve the stacked linear system exactly); verify h is a
  q-isometry and τ³(ḡ) = hḡh⁻¹ on all generators. Then ⟨τ⟩ ≅ ℤ₃ modulo
  inner: **the turn constructed, order three on the nose.**
- **XB5 (the roof-clock question, posed with the turner in hand):** state
  the final form — sought: an operator (promotion/rowmotion-like, on a
  state space the roof acts on) whose induced action on subgroup classes
  is τ, the way Ψ's footprint at E₇ is ι. Compute any CHEAP first datum
  (e.g. τ's action transported to the 405-point geometry via T⁺ as a
  correspondence between points and one solid family, if it falls out of
  the machinery; else NOT RUN with reason). The full hunt is the
  successor — named, not computed.

## Discipline

Compute, never assert; the registered expectation resolvable INVERTED at
equal prominence; fail-first logs kept; exact 𝔽₂/ℚ arithmetic for all
algebraic claims; sealed caches READ-ONLY (Stone U/V/W); own cache
`_stone_x_cache/`. Outputs: `verify_stone_x_turner.py`, `.log`, findings
`STONE_X_TURNER.md`. No registry/git writes by the executor. Not RH/GRH;
no identifications (Rule 3).
