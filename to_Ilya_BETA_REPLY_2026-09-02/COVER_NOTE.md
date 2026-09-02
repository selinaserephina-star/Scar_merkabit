# TO ILYA — THE β-REGISTER, YOUR AUDIT, AND THE NAME OF THE STONE (2026-09-02)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** This answers your
batch of 2026-09-02: the reproducibility audit, the model-frame response
and addendum, the β-pattern proposal, the β-chain prompt, the subgroup-
diversity prompt with its addendum, and the roof-work prompt. Package:
this cover + the sha-locked Stone Y brief + lock (locked BEFORE code) +
`verify_stone_y_beta_register.py` + log (17/17) + `STONE_Y_BETA_REGISTER.md`
+ registry snapshot v0.55 + your own turn-point prompt file (so SM-032
task 2 is reproducible on your side) + SHA256SUMS.txt.

---

## 1. Your audit — five seals go JOINT

Your clean-room rerun of SM-029, SM-030, SM-032, SM-033, SM-034 — caches
rebuilt from the sent zips, every count and value reproduced — is your word
on those five. They are **JOINT** in the registry as of v0.54. Thank you
for doing it the hard way.

One item returned as a question, not adopted. Your auditor reports SM-029
at 31 checks. The log in the frozen ROOF envelope and our local log are the
same file (sha fd5a343f…) and both read **32 PASS** over the check IDs
1a–1e, 2a–2h, 3a–3g, 4a, 5a–5h, 6a–6b, 7a. Your text says the ID set was
identical, which cannot be so at 31. Which ID did the sandbox drop? Until we
know, the registry count stands at 32.

SM-032 task 2 could not be rerun on your side because its input was your
own file, `PROMPT_ Operationalizing the Turn Point.md`, which we had not
placed in the envelope. It is in this one.

## 2. The frame, the pick, and the name

**TWO_REGISTER_MODEL v0.1: accepted** — it is now the joint frame. Your
storing-invariant pick is **β**, the commutator sign named in SM-033.
Neither of our two candidates; a third, drawn from our own lift law. Good.

**The name.** You proposed the β test as "Stone X". Our Stone X is the
turner (SM-036): its brief was sha-locked on 2026-09-01, before your mail,
and the package went to you this morning. So your proposal is filed as
**Stone Y: the β-register**, and everything below is Stone Y.

## 3. Stone Y — what the register says

Brief locked before code; eight registered expectations; all eight PASS;
no inversion; 0.9 s from the sealed Stone U cache.

**First, a repair, because the object as written is not defined.**
β(g,h) = [ĝ,ĥ] is lift-independent (central signs cancel) — it is a
well-defined ELEMENT of 2·Sp₆(2) lifting [g,h]. It is a ±1 only when g and
h commute. Your S₃ generators (1 2), (2 3) and your PSL(2,7) generators a, b
do not commute; the machine shows the lift-commutators are non-central
elements of order 3 and 4/8. So "β(s₁,s₂)" and "β(a,b)" have no sign value.

**The object that survives:** for an embedded S = ⟨X⟩ with presentation
relators R, each relator evaluates on the lifts to a sign σ_w = w(X̂) ∈ {±1};
the generator sign gauge X̂ ↦ ±X̂ acts through exponent-sum parities;
**M_S := the gauge orbit** — the restriction of the extension class to S.
A power relator gⁿ gives ε(g); a commutator relator gives β. And
**π⁻¹(S) splits ⟺ M_S is trivial** — machine-checked against SM-033's
closure test on all 105 subgroup instances of the run. Note that M lives on
the EMBEDDED class, not on Γ as an abstract group (SM-029 already showed
the two L₂(7) classes lift differently).

**The tables, in your format.**

```text
S₃ = ⟨s₁,s₂ | s₁², s₂², (s₁s₂)³⟩      gauge-invariant: s₁², s₂²  →  M = ε(s)
  in the bridge-class L₂(7):   (+,+,·)  SPLIT      preimage S₃×C₂
  in the Fano-class  L₂(7):    (−,−,·)  NON-SPLIT  preimage Dic₃
  sweep, all four involution classes:  315⁺, 3780⁺ → S₃×C₂ ; 945⁻, 63⁻ → Dic₃

D₄ = D₈ = ⟨r,s | r⁴, s², (rs)²⟩      gauge-invariant: all three  →  M = (ε r, ε s, ε rs)
  Sylow-2 of the five GL(2,3)-lifting S₄'s:  SD₁₆     (−,+,−) / (−,−,+)
  Sylow-2 of the 2O-lifting S₄:               Q₁₆      (−,−,−)
  60-sample sweep in Sp₆(2): 6 of 8 triples met —
    (+,+,+) D₈×C₂  (+,+,−) C₂²⋊C₄  (−,+,+) D₁₆  (−,+,−) SD₁₆  (−,−,+) SD₁₆  (−,−,−) Q₁₆
  split ⟺ all-plus, every time

PSL(2,7) = ⟨a,b | a², b³, (ab)⁷, [a,b]⁴⟩   gauge-invariant: a², [a,b]⁴  →  M = ε(a)
  the two invariant signs coincide on every witness;
  bridge class (+) split, Fano class (−) non-split — SM-029 falls out

C₄×C₂ = ⟨a,t | a⁴, t², [a,t]⟩         gauge-invariant: all three  →  M = (ε a, ε t, β(a,t))
  a = element #256464 (order 4, ε+);
  t = involution #82:      (+,+,−)  NON-SPLIT
  t = involution #256350:  (+,+,+)  SPLIT
  same a, same ε-profile on all eight elements, same preimage order profile — opposite β
```

One correction on the way: ⟨a,b | a², b³, (ab)⁷⟩ is the (2,3,7) triangle
group, which is infinite; PSL(2,7) needs [a,b]⁴ = 1. The register was
computed with the full presentation.

**Your decision rule, item by item.**

```text
M_Γ well-defined on each level:    YES — after the repair, per embedded class
M_Γ reproduces the ε-table:        YES — power relators carry ε exactly
detects a non-split all-plus case: YES — C₄×C₂, and only via a commutator relator
at S₃ and D₄:                      a RELABELING of the ε-table
```

And the finding that frames it: **no spine group contains a C₄×C₂** (all
twenty sealed witness closures of PSL(2,7), C₆×ℤ₂, A₅, S₄, A₄; ℤ₂ and {e}
trivially), and every spine level's standard presentation has only power
relators. So on the spine, M_Γ IS the ε-restriction. The register's new
word lives off the spine, where two things commute downstairs and refuse to
upstairs. "Memory" stays your [I] label; the mathematics is as above.

## 4. The β-chain — three things to fix before it can run

1. **Which D₄?** Your prompt says "the D₄ object from the existing model"
   and then writes the dihedral presentation. The model's D₄ (SM-034) is
   Lie-type D₄ — Weyl group of order 192, three 8-crystals — not the
   dihedral group of order 8. Stone Y took the dihedral reading, as your
   presentation says. Say which you mean.
2. **Which finite group at "G₂"?** G₂ is a Lie group. Candidates: W(G₂)
   (order 12), or the automorphisms of the G₂ 7-crystal (SM-035). Name it.
3. **What is "M_Γ embeds in M_Δ"?** A generator map must carry relators to
   relators before signs can be compared. Under that reading the first step
   already fails on order: D₈ has no element of order 3, so no map S₃ → D₈
   exists. β is never consulted.

The chain is not run beyond that datum.

## 5. Subgroup diversity and the narrowing addendum

The counts are already sealed and in your hands (SM-026, the blind engine,
`blind_engine_OURS.md` in the CONTAINMENT package):

```text
level  group      |G|   #subgroups  #conj classes
  7    PSL(2,7)   168      179          15
  6    C₆×ℤ₂       12       10          10
  5    A₅          60       59           9
  4    S₄          24       30          11
  3    A₄          12       10           5
  2    ℤ₂           2        2           2
  1    {e}          1        1           1
```

Not monotone: the sequence dips to 10 at level 6 and rises to 59 at level
5. By your own decision rule, "diversity narrowing" is **not supported as
stated** — and the culprit is the level-6 label you already flagged as
unsealed. Maximal and normal counts are a small verifier; say if you still
want the full table after this. The addendum's "transition magnitudes"
168→144→16→12→14→10→1 are your σ-Unified F(n) values (your row 125); they
are physics-side numbers and would enter any such table as [I].

## 6. Total work of the roof = 6037 — parked

S = Σ g(n)σ(n) = 6037 is your row 14.6. Our audit (T-SC, in the COMPLETE
package) graded it untestable as stated: σ is defined outside the registry.
The three vectors — pull, surface integrity, pulse — are not group objects,
and "identify which vector contributes to each g(n)" is not a computation
we can run. This sits on the physics-identification path both of us parked
on 2026-08-31 when we adopted the group-theory-only target (Rule 3). If
you send all six σ(n), we will check the arithmetic of the sum; that is
the whole of what can be verified here.

## 7. Your floor-extraction bundle

Received in the same batch (code index, six scripts, report, spectral
density). Filed in the Riemann lane, not this one; the reply on the four
open asks there comes from that lane.

## In your cadence

You asked the register what it remembers.
On the spine it answered with the table we already had.
Its own word it keeps for the pairs
that commute below and refuse above —
and the spine has no such pair.

## Standing asks

1. Which check ID your SM-029 rerun dropped (§1).
2. Your word on SM-036 (the turner, sent this morning) and on SM-037
   (Stone Y, this envelope); SM-035 (the still point) still awaits.
3. The three β-chain instantiations (§4) — or the chain is withdrawn.
4. Whether you want the maximal/normal subgroup table run (§5).
5. The roof-clock hunt (find Φ with footprint τ′) as the next joint
   work-item — yes/no, carried from the turner envelope.

— S. (with Claude), 2026-09-02
