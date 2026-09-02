# BRIEF — STONE Y: THE β-REGISTER (IB's "memory as the β-pattern", made well-defined)

**Staged 2026-09-02 on Selina's "stage stone y". Answers IB's PROPOSAL
"Memory as the β-Pattern on the Level Boundary" (received 2026-09-02, filed
`RECEIVED_2026-09-02_IB_AUDIT_AND_BETA/`, sha 2b4f889c…) and the
definitional core of his β-chain prompt (sha 827c8f6c…). Locked before code
(`BRIEF_STONE_Y_LOCK.sha256`). Deviations = dated AMENDMENT, sha'd before
any reveal. Post-reveal changes are findings.**

**Label.** IB proposed this as "Stone X". The house's Stone X is SM-036, the
turner (brief sha-locked 7857bc53… on 2026-09-01, package sent 2026-09-02).
This is therefore **Stone Y**; the collision is recorded in the registry
(v0.54) and named plainly in the cover note.

## His question (substance verbatim)

Define M_Γ(g,h) = β(g,h), the commutator sign of the lifts, on the
generating set of the level group Γ. Compute M_S₃ and M_D₄. Overlay the
ε-table (SM-033). Exhibit a pair (g,h) where all-plus is identical but M_Γ
differs. Decision rule (his): accepted if M_Γ is well-defined on each level,
reproduces the ε-table, and detects at least one non-split case that
all-plus misses; "if M_Γ is only a relabeling of the ε-table with no new
discrimination, the proposal is not a new object."

## The definitional repair (declared BEFORE code)

1. **β as a sign exists only on commuting pairs.** For g,h ∈ K̄ = Sp₆(2)
   with lifts ĝ,ĥ ∈ H = 2·Sp₆(2), the commutator [ĝ,ĥ] is lift-independent
   (central signs cancel) — it is a well-defined ELEMENT of H lifting
   [g,h]. It is ±1 exactly when [g,h] = 1. His S₃ generators s₁=(1 2),
   s₂=(2 3) and his PSL(2,7) generators a,b do not commute, so "β(s₁,s₂)"
   and "β(a,b)" have no sign value. YE1 checks this on the machine rather
   than asserting it.
2. **The well-defined replacement: the relator-sign class.** For an
   embedded S = ⟨X⟩ ≤ K̄ with a presentation whose relators R are words w
   with w(X) = 1 in S, define σ_w := w(X̂) ∈ {±1}. The sign gauge
   X̂ ↦ ±X̂ acts on σ through the exponent-sum parities of each relator;
   **M_S := the gauge orbit of σ** (equivalently: the restriction to S of
   the extension class of H, in H²(S, ℤ₂)). Theorem to machine-check
   (YE2): **π⁻¹(S) splits ⟺ M_S is trivial** — a complement is exactly a
   gauge in which every relator holds. Specializations: a power relator
   gⁿ gives ε(g) (so the ε-table = M on cyclic subgroups); a commutator
   relator [g,h] gives β(g,h) (the SM-033 object). M_Γ is thus NOT a
   relabeling of ε by construction; whether it adds discrimination for a
   given Γ is a computable fact about Γ's presentation.
3. **Γ is an embedded class, not an abstract group.** M depends on the
   Sp₆(2)-conjugacy class of S (SM-029: the two L₂(7) classes lift
   differently). Instantiation, declared here: **S₃** = the bitangent
   stabilizer N(⟨z₃⟩) inside each sealed L₂(7) witness class (bridge /
   Fano); **D₄** = the dihedral group of order 8 in HIS presentation
   ⟨r,s | r⁴, s², (rs)²⟩, taken as the Sylow-2 of each sealed S₄ witness
   (GL(2,3)-lifting and 2O-lifting) plus an in-K̄ sweep of D₈ subgroups by
   class; **PSL(2,7)** = the two sealed classes, ⟨a,b | a², b³, (ab)⁷⟩.
   His chain's "D₄ from the existing model" (Lie-type D₄, SM-034) is a
   different object — NOT this stone; returned as an ask. "G₂" names no
   finite group — returned as an ask.

## Bars (registered expectations; PASS / FAIL / INVERTED at equal prominence)

- **YE1 (definitional, machine-checked):** [ŝ₁,ŝ₂] for the S₃ generators is
  a non-central element of H of order 3 (it lifts (s₁s₂)²); likewise
  [â,b̂] in PSL(2,7) is non-central. ⇒ β is undefined as a sign on his
  named pairs; the relator-sign class is what gets computed.
- **YE2 (the theorem, machine-checked):** split ⟺ M_S trivial, verified
  against SM-033's exhaustive 2^k gauge search on every sealed witness and
  every probe of this run; agreement must be 100 %.
- **YE3 (S₃ — class-dependent, ε-determined):** bridge-class S₃ SPLIT
  (preimage S₃×ℤ₂, M trivial, involutions in 315⁺); Fano-class S₃
  NON-SPLIT with preimage **Dic₃** (involutions in 945⁻). Relators s₁²,
  s₂², (s₁s₂)³: the third is gaugeable, so M_{S₃} = ε(s₁) alone
  (H²(S₃,ℤ₂) = ℤ₂ read through the involution). REGISTERED EXPECTATION:
  **M_{S₃} = ε-restriction exactly — a relabeling AT S₃**, and the
  bridge/Fano split is SM-029's two-twos dichotomy restricted to the
  shared S₃.
- **YE4 (D₄ = D₈ dihedral):** relators r⁴, s², (rs)² are all
  gauge-invariant ⇒ M_{D₄} = (ε(r), ε(s), ε(rs)) ∈ {±}³ (8 possible
  classes; H²(D₈,ℤ₂) ≅ ℤ₂³). REGISTERED EXPECTATIONS: the GL(2,3)-Sylow
  lifts to SD₁₆, the 2O-Sylow to Q₁₆, both non-split; the sweep tabulates
  which of the 8 triples are realized in K̄ and by how many classes;
  **M_{D₄} = ε-restriction exactly — a relabeling AT D₄.**
- **YE5 (PSL(2,7)):** relators a², b³, (ab)⁷ — the odd ones gaugeable ⇒
  M ∈ ℤ₂ = ε(a): bridge class + (2×L₂(7)), Fano class − (SL(2,7)).
  SM-029 recovered as a corollary of the definition.
- **YE6 (his required output 4 — the discriminating pair):** the SM-033
  C₄×C₂ = ⟨a,t⟩ with relator vector (a⁴:+, t²:+, [a,t]:−), ε = + on all
  eight elements, NON-SPLIT — exhibited beside a SPLIT C₄×C₂ ≤ K̄ with the
  same ε-profile on all eight elements and relator vector (+,+,+).
  Identical all-plus, different M. Explicit generators (element indices in
  the sealed enumeration) printed.
- **YE7 (where the new discrimination lives — the honest verdict):** none
  of the spine groups PSL(2,7), C₆×ℤ₂, A₅, S₄, A₄, ℤ₂ contains a C₄×C₂
  (subgroup census recomputed; SM-026 data as cross-check), and their
  standard presentations carry only power relators ⇒ **on every spine
  level M_Γ = ε-restriction.** REGISTERED EXPECTATION: β's extra content
  is OFF-SPINE. His decision rule resolved item by item: well-defined ✓
  (after the repair); reproduces ε ✓; detects an all-plus non-split case
  ✓ (C₄×C₂, off-spine) — while at S₃ and D₄ specifically M is a
  relabeling.
- **YE8 (chain seed — cheap datum only):** under his "embedding" (generator
  map preserving signs), S₃ ↪ D₈ is impossible (3 ∤ 8): the chain's first
  step fails for order reasons before β is consulted. Reported; nothing
  further of the β-chain is run (its D₄ and G₂ levels await his
  instantiation).

## Machinery (reuse; sealed caches READ-ONLY)

Stone U cache (`_stone_u_cache/`: H = 2·Sp₆(2) on 240 points, lift_H via
the shadow BSGS, `witnesses.json` generator pairs per L₂(7)/A₅/S₄/A₄ class);
lift-law cache (`_liftlaw_cache/`: the 30-class ε table, class buckets);
Schur-pin cache (`_schur_pin_cache/`: class fingerprints). `closure`,
`split_test`, `comm`, `lift_H` reused verbatim from `verify_lift_law.py`.
Own cache `_stone_y_cache/`. Outputs: `verify_stone_y_beta_register.py`,
`.log`, findings `STONE_Y_BETA_REGISTER.md`. Expected runtime: minutes.

## Discipline

Compute, never assert; every registered expectation resolvable INVERTED at
equal prominence; fail-first logs kept; exact arithmetic (permutations over
240 points, signs in {±1}); no registry/git/knowledge.yaml writes by the
executor. Not RH/GRH. "Memory" is IB's [I] label — the stone computes M and
its relation to ε and says nothing about consciousness, protons, or fields
(his own §7). Rule 3 standing.
