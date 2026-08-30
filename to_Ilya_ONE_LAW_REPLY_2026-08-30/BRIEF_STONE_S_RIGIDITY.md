# BRIEF — STONE S: THE RIGIDITY THRESHOLD (Ilya's ONE LAW / TWO PROJECTIONS)
**Scar_merkabit joint lane · staged 2026-08-30 · trigger: received document
`RECEIVED_2026-08-30_IB_ONE_LAW_TWO_PROJECTIONS/` (sha adb17c49…0016),
Ilya's answer to the Stone 1b support-law invitation.**
**SHA-locked before one line of the verifier exists.**

## 0. Discipline

Compute, never assert; refutations at equal prominence; his rules
executed where defined, and where his document is under-specified the
instantiation is OURS, declared here before computing, with the choice
returned to him (precedent: the geometric-order reply). Rule 3; not
RH/GRH; ONE LOCK.

## 1. His claim and his ask

Ilya proposes: min_support(S₂ₙ) = min_support(Bₙ) = 3 — "support 2: a
swap… Soft. Sliding possible. support 3: first irreducible cycle. First
true knot. First rigid structure. This threshold should be
projection-independent." He asks three questions against our exact
tables: is min_support(S₂ₙ) constant or growing; same for Bₙ; are they
equal. Decision rule: both = 3 ⇒ one law, two projections; differ ⇒
different rigidity thresholds.

**Under-specifications, declared:** (a) his "B_n" reads as the braid
group (path-remembering); OUR Bₙ in the pair (S₂ₙ, Bₙ) is the
hyperoctahedral group — the tables he cites live on the Gelfand-pair
projection, and the braid projection has NO tables in this lane. We
execute on the projection we have and return the braid side as a
question. (b) "min_support" is not operationalized; we test TWO declared
translations (§3) and return the choice.

## 2. Constructions

Rebuild the exact support tables SUP[n][λ][τ] for the coset-type
composition of the Gelfand pair (S₂ₙ, Bₙ), n = 4..7, by exhaustion over
all matchings (the Stone 1b machinery, reused verbatim: mtype,
partner_of_type, all_matchings). ELIGIBLE(λ,τ) = the triangle d-interval
{μ : |d(λ)−d(τ)| ≤ d(μ) ≤ min(d(λ)+d(τ), n−1)}. A RIGIDITY EVENT is a
pair (λ,τ) with SUP ⊊ ELIGIBLE; its MISSING SET is ELIGIBLE ∖ SUP.

## 3. Registered bars

**SB1 [anchor].** Tables reproduce Stone 1b's sealed facts: triangle
inequalities NECESSARY at every n; the mined d-law ("support = full
d-interval whenever d(λ) ≥ 2 and d(τ) ≥ 2; failures only at
min(d) ≤ 1") re-verified; failure counts reported. EXPECT PASS.

**SB2 [parity mining].** Is d(μ) ≡ d(λ)+d(τ) (mod 2) a law of the
support? Tested over every entry, every n. Either outcome recorded; if
it holds, ELIGIBLE is refined accordingly before SB3.

**SB3 [REGISTERED HEADLINE — his decision rule, two translations].**
 (a) **d-translation** (support level ↦ distance d from the identity
 type: 1 ↦ d=0, 2 ↦ d=1 "a swap", 3 ↦ d=2): measure the exact rigidity
 threshold: R_d(n) = the set of min(d(λ),d(τ)) values over rigidity
 events. His picture predicts softness at d ≤ 1 and first rigidity at
 d = 2. The Stone 1b mined law suggests the INVERSE (rigidity exactly
 at min(d) ≤ 1, softness at d ≥ 2). The data decides; if inverted, the
 verdict is rendered in his own format: threshold shared, SIGN
 opposite.
 (b) **part-translation** (support level ↦ largest part: 3 = "first
 irreducible cycle"): P(n) = min over all missing μ (all rigidity
 events) of max-part(μ), and Q(n) = min over rigidity events of
 max(max-part(λ), max-part(τ)). His claim predicts P(n) = 3, constant.
 Constancy across n = 4..7 reported for every measured quantity (his
 Q1). No braid-side computation is attempted (his Q2 returned); his Q3
 (equality) is answerable on our side only as the pair (translation
 verdicts + the classical braid facts cited, not computed: trefoil
 crossing number 3, B₃ the first braid group with a knotted closure).

**SB4 [returned questions].** (i) the Bₙ terminology collision
(braid vs hyperoctahedral) — which object does he want tabled, and with
which invariant in the role of coset type? (ii) which translation of
"min_support" is his — d or part? (iii) whether "soft/sliding" for
swaps survives the measured polarity.

## 4. Honest scope

The tables are exhaustive and exact for n ≤ 7 only; all thresholds are
[C on range]. No braid computation; no claim about his braid-side
prediction beyond classical citations. If the polarity inverts, that is
a statement about THIS projection, not about his braid picture — the
comparison across projections is exactly what gets returned to him.

## 5. Deliverables

verify_stone_s_rigidity.py; STONE_S_RIGIDITY.md; registry: received row
+ SM-018 + changelog v0.17; KCP units; reply draft for Ilya
(prepared-not-sent); git commit; memory + synthesis line.
