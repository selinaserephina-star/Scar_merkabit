# BRIEF — STONE V: THE ROOF (the W(E₈) containment run)

**Staged 2026-09-01 on the ADOPTED joint work-item (both parties' word,
registry v0.33: IB — "W(E₈) containment is the next work-item. We go up.").
Locked before code (`BRIEF_STONE_V_LOCK.sha256`). EXECUTES ON SELINA'S WORD.
Deviations = dated AMENDMENT, sha'd before any reveal.**

## Question

The choice theorem (JOINT, SM-023 + SM-027): no single ±-extension of Sp₆(2)
contains both towers. SM-027 exhibited both extensions inside W(E₈) — the
split 2×Sp₆(2) (vector type) and the non-split 2·Sp₆(2) (spin type). Stone V
asks the roof question in three parts:

1. Does W(E₈) contain BOTH towers in full — the spine (PSL(2,7), C₆×ℤ₂, A₅,
   S₄, A₄, ℤ₂) AND the Schur tower (SL(2,7), SL(2,5)=2I, GL(2,3), 2O,
   SL(2,3)=2T, plus the split covers and 2·W(E₆))?
2. What is a MINIMAL overgroup: the smallest subgroup of W(E₈) found to
   contain both towers — is it W(E₈) itself, the index-2 rotation subgroup
   W⁺(E₈), the derived subgroup, ⟨C, H⟩ for the sealed vector-complement C
   and spin-preimage H, or something smaller?
3. Where does each tower member sit relative to the TWO centres in play —
   the W(E₈) centre ⟨−1_{E₈}⟩ and H's own stem centre — i.e. does the roof
   preserve the hinge structure or dissolve it?

## Bars

- **VB1 (assembly, mostly from sealed parts):** both towers ⊂ W(E₈),
  witnessed — spine inside the vector-type complement C ≅ Sp₆(2) (SM-023
  witnesses transported / re-verified in C), Schur tower inside H ≅ 2·Sp₆(2)
  (SM-027 UB5 witnesses re-verified from cache). Every tower member gets an
  explicit witness subgroup of W(E₈) with order + iso fingerprint checked.
  Any member without a witness: FAIL for that member, full prominence.
- **VB2 (the minimal roof):** compute K = ⟨C, H⟩ ≤ W(E₈) by BSGS closure —
  its order and its position (K = W(E₈)? K = W⁺(E₈) = the rotation half?
  index?). Registered expectation (auditor, on the record): **K is at most
  W⁺(E₈)** — both C and H should sit inside the rotation subgroup if their
  generators are even words; verify rather than assume, and if K = W(E₈) or
  something unexpected, record INVERTED. Then MINIMIZE: search for proper
  subgroups of K still containing both towers — at minimum test the derived
  subgroup [K,K] and the subgroup ⟨one spine chain, one Schur chain⟩
  (generators of a full spine witness set + a full Schur witness set only);
  report the smallest overgroup FOUND with the honest scope statement
  (minimal-found, not proven-minimal, unless a lattice argument closes it).
- **VB3 (the two centres):** locate −1_{E₈} relative to K and to each
  witness; locate H's stem centre z_H (the central involution of H, ≠ or =
  −1_{E₈}? — SM-027's H was built as π⁻¹(K_spin) so z_H = −1_{E₈}; verify)
  — state exactly which ℤ₂ each Schur witness sits over, so the hinge
  bookkeeping survives into the roof statement.
- **VB4 (the roof theorem, final form):** one theorem-shaped paragraph: the
  smallest verified roof R (with order), both towers inside it with named
  witnesses, the hinge structure of R, and what remains open (true
  minimality; canonicality of R up to W(E₈)-conjugacy). Successor questions
  named, not computed.

## Discipline

Compute, never assert; registered expectation resolvable INVERTED at equal
prominence; fail-first logs kept; exhaustive claims scoped ("minimal-found"
never silently upgraded to "minimal"); grades [C]/[P cited] unblended.
Verifier `verify_stone_v_we8_roof.py`, log + findings doc `STONE_V_WE8_ROOF.md`.
Stone U cache read-only; write own cache. No registry/git writes by the
executor. Not RH/GRH; no physical identification (Rule 3).
