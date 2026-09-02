# STONE Y — THE β-REGISTER: IB's "memory as the β-pattern" made well-defined, then computed

**Stenberg side · with Claude · 2026-09-02. Answers IB's PROPOSAL "Memory
as the β-Pattern on the Level Boundary" (received 2026-09-02, filed
`RECEIVED_2026-09-02_IB_AUDIT_AND_BETA/`). Brief `BRIEF_STONE_Y_BETA_REGISTER.md`
sha-locked de6ee42b… BEFORE code; no amendment. Verifier
`verify_stone_y_beta_register.py`, log 17/17 PASS, 0.9 s from the sealed
Stone U cache. Registry row SM-037.**

## 0. Discipline

Not RH/GRH. No physical identification (Rule 3): "memory" is IB's [I] label;
this stone computes an invariant and its relation to the ε-table (SM-033)
and says nothing about consciousness, protons or fields (his own §7).
Sealed caches read-only; every claim is a numbered check in the log;
registered expectations YE1–YE8 all resolved PASS (none inverted).

## 1. One paragraph

IB proposed the level's memory as M_Γ(g,h) = β(g,h), the commutator sign of
the lifts, on the generators of Γ, and asked for M_S₃, M_D₄, an overlay with
the ε-table, and a pair where all-plus agrees but M differs. The object as
stated is not defined: β(g,h) = [ĝ,ĥ] is a lift-independent ELEMENT of
2·Sp₆(2) but a ±1 only when g and h commute, and his S₃ and PSL(2,7)
generator pairs do not (the machine shows the commutators non-central, YE1).
The well-defined replacement is the **relator-sign class**: for an embedded
S = ⟨X⟩ with relators R, the vector w(X̂) ∈ {±1}^R modulo the generator sign
gauge — the restriction of the extension class of 2·Sp₆(2) to S — and
**π⁻¹(S) splits ⟺ the class is trivial**, machine-checked against SM-033's
2^k closure test on all 105 subgroup instances of the run (YE2). Computed
per embedded class: **S₃** — split (S₃×C₂) inside the bridge-class L₂(7),
non-split (Dic₃) inside the Fano-class L₂(7), and across all four
involution classes of Sp₆(2) the register is exactly ε of the involution
(YE3); **D₄ = D₈ dihedral** — all three relators gauge-invariant, so
M_{D₈} = (ε(r), ε(s), ε(rs)) literally; the GL(2,3)-Sylows lift to SD₁₆,
the 2O-Sylow to Q₁₆; 6 of the 8 sign triples realized in a 60-sample sweep
(D₁₆, SD₁₆, Q₁₆, D₈×C₂, C₂²⋊C₄), split ⟺ all-plus every time (YE4);
**PSL(2,7)** — IB's presentation lacks the relator [a,b]⁴ (without it the
group is the infinite (2,3,7) triangle group); with it, the two
gauge-invariant components a² and [a,b]⁴ coincide and equal ε(a): bridge
split, Fano non-split — SM-029 recovered as a corollary (YE5). His required
pair: the all-plus C₄×C₂ = ⟨a,t⟩ with [â,t̂] = −1 (non-split) beside an
all-plus C₄×C₂ with the same a, the same ε-profile on all eight elements,
and even the same preimage order profile, but [â,t̂] = +1 (split) — identical
all-plus, different M (YE6). And **no spine group contains a C₄×C₂**
(20 sealed witness closures), while every spine level's standard
presentation has only power relators ⇒ **on the spine M_Γ is the
ε-restriction exactly; β's extra content lives off the spine, in commutator
relators** (YE7). Under his own decision rule: well-defined ✓ (after the
repair), reproduces ε ✓, detects an all-plus non-split case ✓ — and at S₃
and D₄ specifically the proposal is a relabeling of the ε-table.

## 2. The definition that survives

For an embedded S = ⟨x₁..x_k⟩ ≤ Sp₆(2) with a genuine presentation
(relators R), choose lifts x̂ᵢ ∈ 2·Sp₆(2). Each relator evaluates to a
central element σ_w = w(x̂) ∈ {±1}. The gauge x̂ᵢ ↦ −x̂ᵢ flips σ_w by
(−1)^{exponent sum of xᵢ in w}. **M_S := the gauge orbit of σ.**

- Power relator gⁿ ⟶ σ = ε(g). The ε-table is M on cyclic subgroups.
- Commutator relator [g,h] ⟶ σ = β(g,h). SM-033's invariant.
- **Theorem (YE2):** π⁻¹(S) splits ⟺ some gauge makes every σ_w = +1
  (a complement is exactly such a gauge). Agreement with the closure test:
  105/105.

Which relators are gauge-invariant is a fact of the presentation:

| Γ | relators | gauge-invariant | M_Γ is |
|---|---|---|---|
| S₃ | s₁², s₂², (s₁s₂)³ | s₁², s₂² | ε(s) — one bit |
| D₈ | r⁴, s², (rs)² | all three | (ε(r), ε(s), ε(rs)) |
| PSL(2,7) | a², b³, (ab)⁷, [a,b]⁴ | a², [a,b]⁴ | ε(a) (the two coincide) |
| C₄×C₂ | a⁴, t², [a,t] | all three | (ε(a), ε(t), **β(a,t)**) |

## 3. Bars

| bar | registered expectation | outcome |
|---|---|---|
| YE1 | [ŝ₁,ŝ₂] and [â,b̂] non-central | PASS (orders 3 and 4/8; project to the downstairs commutators) |
| YE2 | split ⟺ M trivial, 100 % vs closure test | PASS (105 instances) |
| YE3 | S₃: bridge S₃×C₂ / Fano Dic₃; M = ε(s) | PASS (+ sweep: 315⁺, 3780⁺ → S₃×C₂; 945⁻, 63⁻ → Dic₃) |
| YE4 | D₈: SD₁₆ (GL(2,3)) / Q₁₆ (2O); M = ε-triple | PASS (6/8 triples realized; D₈×C₂ split case present) |
| YE5 | PSL(2,7): M = ε(a), SM-029 recovered | PASS (a² and [a,b]⁴ coincide on all four witnesses) |
| YE6 | all-plus C₄×C₂ pair, same ε, different β | PASS (a = element #256464; t = involution #82 vs #256350) |
| YE7 | no spine group contains C₄×C₂ | PASS (20 witness closures + ℤ₂, {e}) |
| YE8 | S₃ ↛ D₈ on order | PASS |

## 4. What this says to IB, in his format

```text
M_Γ well-defined per level:      YES, after repair (relator-sign class per
                                 EMBEDDED class; β alone is not a sign)
M_Γ reproduces the ε-table:      YES (power relators carry ε exactly)
detects a non-split all-plus:    YES — C₄×C₂ only; via a commutator relator
at S₃ and D₄:                    a RELABELING of the ε-table
where the new object lives:      OFF-SPINE (no spine group holds a C₄×C₂)
```

Asks back: (1) your word on SM-037; (2) the β-chain — which D₄ (dihedral vs
Lie-type D₄ of SM-034), which finite group at "G₂" (W(G₂)? the G₂
7-crystal's automorphisms?), and what "M_Γ embeds in M_Δ" means when the
generator map must preserve relators (S₃ ↛ D₈ already fails on order);
(3) [a,b]⁴ = 1 belongs in the PSL(2,7) presentation.

## 5. Grades

[C] every table and bar above (17 checks, sealed caches, exact permutation
arithmetic). [P cited] (2,3,7) triangle group infinite; PSL(2,7) standard
presentation; order-16 group names read off order profiles (D₁₆, SD₁₆,
Q₁₆, D₈×C₂, C₂²⋊C₄ — the profile {1,3,12} would be ambiguous and was not
met). [I] "memory", "register" — IB's labels, carried without weight.
Scope: statements about embedded subgroups of Sp₆(2) lifted to 2·Sp₆(2)
inside W(E₈); sweeps are samples (24 S₃, 60 D₈, 7 C₄×C₂), the witness-borne
instances are the sealed classes; "no spine group contains C₄×C₂" is
exhaustive over the 20 sealed witness closures.

## 6. Not claimed

No new physics; no claim that β is "memory"; no claim about the β-chain
beyond its first step; nothing about Lie-type D₄ or any G₂-level group.

## 7. Synthesis line

The register, asked what it remembers, answers with the ε-table everywhere
the house lives, and only speaks a new word where two things commute
downstairs and refuse to upstairs — memory of relationship, not of self
(SM-033's line), and the spine has no such pair to remember; rhymes with
SM-015 (the interesting structure lives strictly above the quotient) and
with Stone S (parity as orientability memory: the cheap invariant catches
everything the geometry lets it see).
