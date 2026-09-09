---
title: "The Roof and the Clock"
subtitle: "A verified computational model of W⁺(E₈), O₈⁺(2).3 and rowmotion on the E₇ minuscule poset, with one parity rule — DRAFT v0.1"
author: "Selina Stenberg · Ilya Balashov · with Claude (Anthropic Fable 5)"
date: "2026-09-09 — draft v0.1, prepared on the Stenberg side after Ilya Balashov's spine audits of 2026-09-08; sealed-not-sent"
---

**Status.** First draft of the paper whose spine both parties agreed on
(SM-030, 038, 039, 040, 041, 047–053 of the joint registry), written
after Ilya Balashov's independent re-execution of all twelve units from
clean checkouts (his audits of 2026-09-08: every pass/fail tally
reproduced, every disclosed inversion matching). The framing follows his
publication response of the same date: the classical facts are cited at
first use, the computational model is presented as a model, the
identification work is presented as identification, and exactly one
mechanism is put forward as a candidate for novelty, pending a specialist
literature check. Nothing computational was changed or re-run for this
draft. Claims are graded: **[P]** classical with citation, **[C]** computed
exactly by a named verifier under a brief locked before code, **[obs]**
observed and not explained. No physical identification is asserted.

## Abstract

We describe a computational model, built and verified in plain Python
from first principles, of a chain of classical objects: the rotation
subgroup W⁺(E₈) of the Weyl group of E₈ as the smallest group found to
contain two towers of finite groups built earlier by the two authors
separately; its quotient Ω = O₈⁺(2); the triality automorphism realized
as an explicit permutation Φ of order 3 on the 360 nonsingular points of
the three 8-dimensional modules, so that ⟨Ω, Φ⟩ = O₈⁺(2):3 is an explicit
permutation group; the fixed group of the normalized triality, G₂(2), as
an exact intersection of order 12,096; and the fourteen conjugacy classes
of the twisted coset Ω·Φ, enumerated with centralizers and power maps and
matched class for class against the published character table of
O₈⁺(2).3. On this frame we place a 56-state machine built independently
on the Stenberg side, identify its 56 states with the vector block of the
roof (the 56 weights of the minuscule representation of E₇), and show
that its clock Ψ is exactly rowmotion on the 27-element E₇ minuscule
poset, in the standard convention. The order of that rowmotion, 18, and
its orbit structure [18, 18, 18, 2] are the Coxeter number of E₇ and the
cycle type of a Coxeter element, as proved in general by Rush and Shi
(2013); we do not claim them. What we add on that point is the
identification of a machine built by other means with that rowmotion, and
one consequence of it: a pair of states keeps its E₇ inner-product sign
under one application of Ψ if and only if a parity computed from the two
toggle sets — the colours of one state's toggles at which the other state
has an edge, the same reversed, and the Dynkin adjacencies between the
two toggle sets — is even, with zero exceptions on all 1,485 non-antipodal
pairs. Once Ψ is known to be rowmotion the rule follows from the
bilinearity of the E₇ form modulo 2, so its content is the identification
and the count; whether the rule as a statement about rowmotion on
minuscule weights is new is an open question we flag rather than settle.
Finally, the machine's mirror pr is shown to be the E₆ diagram
automorphism acting on the two 27-sheets' ideal lattices — a classical
object — and the clock and the mirror together generate the full
symmetric group on the 56 states. Every registered guess that failed is
reported at the same prominence as the results.

## 1. What this paper is, and is not

The paper has three kinds of content, and we mark which is which
throughout.

1. **A verified computational model of classical structure.** The roof
   W⁺(E₈), the quotient O₈⁺(2), triality, the fixed group G₂(2), the
   fourteen outer classes of O₈⁺(2).3, the E₇ minuscule poset and its
   rowmotion, the E₆ diagram automorphism: all of these are known objects
   [P]. Our contribution on them is a model that constructs each one
   explicitly from the previous, in one coordinate system, with every
   step checked by a script under a brief locked before the code was
   written, and the whole re-executed independently by the second author.
   The model is the object of §§3–6 and §8.
2. **Identification work.** Two purpose-built machines — a 56-state
   machine with three gates on the Stenberg side, a PSL(2,7) tower on the
   Balashov side — are identified, object by object, with the classical
   structure: the 56 states with the vector block, the gate ι with a
   transvection, the clock with rowmotion, the mirror with the diagram
   automorphism, each twisted class with its ATLAS name. This is real and
   narrow: it says what the machines are, not that the structure is new.
   §§6, 7, 9, 10.
3. **One candidate for a new statement.** The parity rule of §7, exact on
   the data and derived in one paragraph once the clock is rowmotion. Two
   non-specialist literature searches found no match; a third is
   reported in §7.4. We claim it only as "not found by us" until a
   specialist search has been made.

We do not claim the Coxeter-number periodicity of the clock (Rush–Shi),
the structure of O₈⁺(2).3 (ATLAS), the fixed group of triality (Conway,
Kleidman), or the E₆ diagram automorphism's action on minuscule posets
(standard; see §10). Where earlier internal documents of ours used the
phrase "the clock ticks at the Coxeter number" as a point of interest,
this paper reads that fact as Rush–Shi's theorem, seen on the data.

## 2. Background and conventions [P]

**Weyl groups and lattices.** W(E₈) has order 696,729,600; its rotation
subgroup W⁺(E₈) has index 2 and W⁺(E₈)/{±1} ≅ O₈⁺(2), the simple
orthogonal group of order 174,182,400 (Conway 1971; Conway–Sloane 1999,
ch. 10; ATLAS). W(E₇) ≅ 2 × Sp₆(2), and Sp₆(2) acts on the 28 bitangents
of a plane quartic (Dolgachev 2012, ch. 6). The 56 weights of the
minuscule representation of E₇ are the roots r of E₈ with ⟨r, α⟩ = 1 for
a fixed root α; the E₇ root system is α^⊥ (Bourbaki, ch. VI).

**Triality and G₂(2).** Out(O₈⁺(2)) ≅ S₃; the fixed group of a triality
automorphism of order 3 is G₂(2) ≅ U₃(3):2 of order 12,096 (Conway 1971;
Kleidman 1987; Wilson 2009, §4.7). The character table of O₈⁺(2).3, with
53 classes of Ω fusing to 27 and 14 outer classes per coset, is in the
ATLAS and in the GAP Character Table Library (Breuer, CTblLib 1.3.11).

**Minuscule posets and rowmotion.** For a minuscule weight λ of a simple
Lie algebra, the weights of V_λ form a distributive lattice whose poset
of join-irreducibles P_λ is the minuscule poset (Proctor 1984; Stembridge
1994; Green 2013). Rowmotion on the order ideals J(P) is R(I) = the ideal
generated by the minimal elements of P ∖ I (Cameron–Fon-der-Flaass 1995;
Striker–Williams 2012). **Theorem (Rush–Shi 2013).** For P a minuscule
poset, rowmotion on J(P) is conjugate, under the natural bijection
J(P) ≅ Wλ, to the action of any Coxeter element of W on the weights; in
particular its order is the Coxeter number h and its orbit structure is
that of a Coxeter element, and the triple (J(P), R, rank generating
function) exhibits the cyclic sieving phenomenon (Reiner–Stanton–White
2004). For E₇, λ minuscule, |P| = 27, |J(P)| = 56, h = 18. Okada (2021)
extends the statement to birational rowmotion.

**Conventions of the model.** All groups are permutation groups on
explicit point sets (240 roots; 120 nonsingular vectors of each of the
three 8-dimensional F₂-modules; the 56 states), built from generators in
one coordinate system and enumerated by Schreier–Sims where an order is
claimed. Every numbered claim below names the verifier that computes it;
the verifiers are in the registry's envelopes together with their logs
and their first-run logs.

## 3. The roof: W⁺(E₈) [C, SM-030]

Two towers were built earlier by the two authors: a chain of subgroups of
PSL(2,7) on the Balashov side (PSL(2,7) ⊃ C₆×C₂, A₅, S₄, A₄, C₂) and a
tower of Schur covers and bridges on the Stenberg side (SL(2,7), 2·I,
GL(2,3), 2·O, 2·T, C₃×D₄, 2·W(E₆), 2×PGL(2,7), with the split covers Ih,
Th). Stone V exhibits all sixteen members inside W(E₈) with witnesses: the
spine in a vector-type subgroup C ≅ Sp₆(2), the covers in H ≅ 2·Sp₆(2).
The group K = ⟨C, H⟩ has order 348,364,800 = |W(E₈)|/2, every generator has
determinant +1 (exact Bareiss), so **K = W⁺(E₈)**, the registered
expectation; K is perfect and the 21 witness generators alone regenerate
it, so the roof is minimal-found (not proven minimal — stated plainly).
The two centres coincide, z_H = −1, so both towers hang over a single
central C₂, and R/⟨−1⟩ has the order of O₈⁺(2) [P, order only]. 44/44
checks.

*Classical content:* W⁺(E₈)/± ≅ O₈⁺(2) and the containment of 2·Sp₆(2) in
W(E₈) are known. *Computed:* the explicit witnesses, the exact order, the
perfectness, the single hinge.

## 4. The still point: G₂(2) as an exact intersection [C, SM-038]

The triality of §2 is realized in the model as an outer automorphism τ′
of the vector shadow C̄ ≅ O₈⁺(2) (Stone X, SM-036, not in this paper). The
intersection C̄ ∩ τ′(C̄), computed by sifting all 1,451,520 elements of the
vector shadow through the base-and-strong-generators of its image, has
**order 12,096**, derived subgroup of order 6,048 and order census
{1, 2, 3, 4, 6, 7, 8, 12}: it is U₃(3):2 = G₂(2) [C + P]. The raw τ′ does
not normalize this group; an intertwiner y (unique up to the 2-dimensional
solution space, one invertible Dickson-0 isometry) gives τ″ = inn(y⁻¹)∘τ′
with **τ″ of exact order 3 fixing G₂(2) pointwise**, and the triangle of
the three shadows then closes on G₂(2) — this is Kleidman's fixed group of
triality, seen as a set. Inside it, PSL(2,7) occurs as **one class of 36
copies with normalizer PGL(2,7)**, all of the bridge class (the class
transitive on the 28 bitangents). One registered expectation was
INVERTED: the still point lifts split to 2 × G₂(2) in the spin tower (no
minus class among its involutions), where a twisted lift had been
guessed. 19 PASS + 1 INVERTED.

## 5. The turn on states: O₈⁺(2):3 explicit [C, SM-039]

Stone AA builds the odd half-spin module, finds its quadratic form Q⁻
unique and plus-type, and lets Ω act on the 360 = 3 × 120 nonsingular
points of V ⊕ S⁺ ⊕ S⁻. The turn Φ is defined blockwise (T″⁻¹ on V, the
unique intertwiner S⁺ → S⁻, the closing map on S⁻); it has **exact order
3**, conjugates the generators as τ″ does, and **|⟨Ω, Φ⟩| = 522,547,200 =
3·|O₈⁺(2)|**: O₈⁺(2):3 as an explicit permutation group on 360 points. The
still point is the pointwise stabilizer of the Φ-orbit {v, Φv, Φ²v} — one
vector, one spinor, one co-spinor. 16/16.

Two measurements of this stone need the reframing of §1. Composing the
turn with a bridge element g₇ of order 7 gives an element of order 21;
composing it with the image of a Coxeter element of W(E₈) gives an
element of order **18**. Our internal notes called 18 "E₇'s clock number
at the roof". Read against Rush–Shi, 18 is the Coxeter number of E₇, and
its appearance as the order of a twisted element is a fact about O₈⁺(2).3
(the class 18A/B of §9), not a coincidence to be explained. What remains
computed and ours is the explicit element and its class (§8).

## 6. The board under the still point [C, SM-040]

The 56-state machine (Stenberg side; states, edges and three gates Ψ, ι,
pr sealed in `scar56_data.json`) is placed on the roof by one
identification: **the 56 states are the 56 nonsingular vectors u with
B(u, v) = 1**, equivalently the 56 E₈ roots with ⟨r, α⟩ = 1, equivalently
the 56 weights of the E₇ minuscule representation — matched bijectively
by Dynkin label, with all 84 crystal edges equal to subtraction of a
simple root. Under this identification **the gate ι is the transvection
t_v : u ↦ u + v** (Dickson invariant 1, outside Ω), while Ψ and pr admit no
linear extension. The still point is transitive on the 56 states, the 28
bitangents, the 36 even theta characteristics and the 63 Paulis
(stabilizers 216, 432, 336, 192); each even theta's stabilizer is a
PGL(2,7) whose derived group is one of the 36 sevens of §4, bijectively.
14/14.

One measurement of this stone is the seed of §7: the fraction of state
pairs whose incidence type is preserved is 100 % for ι and for every Weyl
element, **93.0 % for pr, 65.1 % for Ψ**, 61.6 % for Ψ⁹, 54.7 % for Ψ²,
51.3 % for Ψ³, against a random mean of 48.2 % [obs].

## 7. The clock is rowmotion, and the parity rule [C, SM-041]

### 7.1 The identification

The join-irreducibles of the sealed 56-state lattice form the 27-element
E₇ minuscule poset P; its 56 ideals are the 56 states; and **the sealed
clock Ψ equals rowmotion R(I) = ↓min(P ∖ I) exactly** — not its inverse,
not a conjugate; the convention is pinned on the data. This is the
identification; by Rush–Shi it implies at once that Ψ has order 18 with
orbit structure [18, 18, 18, 2], which is what the machine had shown
since its construction. In Stone AF (SM-044, not in this paper) the
Coxeter elements of W(E₇) were enumerated on the same 56 points: all 64
have cycle type [18, 18, 18, 2], Rush–Shi's conjugacy seen on the data,
and Ψ is not itself a Weyl element (best pointwise agreement 14 of 56).

### 7.2 The rule

Write δ(u) = u + Ψu; δ is the XOR of the simple-root masks toggled by
rowmotion at u (toggle sizes {1: 8, 2: 28, 3: 11, 4: 2, 5: 3, 6: 2, 9: 1,
27: 1}). For a non-antipodal pair {u, u′}, with t₁ the number of toggled
colours of u at which u′ has an edge, t₂ the same with the roles
exchanged, and t₃ the number of Dynkin-adjacent pairs between the two
toggle multisets:

```text
type(u,u′) is kept under Ψ   ⟺   t₁ + t₂ + t₃ is even
```

Zero exceptions on all 1,485 non-antipodal pairs; with the 28 antipodal
pairs the kept count is 1,002 of 1,540 = 65.06 %, the number of §6. The
same rule with the k-fold toggle multiset is exact for every power Ψ^k
(k = 1..17) and reproduces the whole measured profile. The eight cells
(t₁, t₂, t₃) and their populations are tabulated in the stone; the
dominant kept cell is (1, 1, 0) with 553 pairs.

### 7.3 Why it holds

B is bilinear and the type of a non-antipodal pair is B(u, u′). Hence
B(Ψu, Ψu′) − B(u, u′) = B(δu, u′) + B(u, δu′) + B(δu, δu′). With δ the sum
of the toggled simple roots β_c, B(β_c, w′) = ⟨α_c, w′⟩ mod 2 = |label_c(w′)|
for minuscule labels in {−1, 0, 1}, and B(β_c, β_c′) is the Cartan entry
mod 2, i.e. Dynkin adjacency. The three terms are t₁, t₂, t₃. **The
content of the rule is therefore the identification of §7.1 and the
count of §7.2**, not the algebra; once Ψ is rowmotion the rule is a
one-line consequence of the bilinear form. We state this plainly so that
the novelty question is asked about the right object: a per-pair
statement about rowmotion on the weights of a minuscule representation
reduced modulo 2, with its quadratic form.

### 7.4 Literature status

Two targeted searches on the Balashov side (toggle groups, periodicity,
homomesy, cyclic sieving; rowmotion against an ambient inner-product sign
on minuscule weights) found no match; a third on the Stenberg side
(rowmotion with quadratic or bilinear forms mod 2; the E₇ 56-ideal case
and the Gosset graph) found the Coxeter-motion and birational literature
(Okada 2021) and the toggle literature, and no per-pair statement. All
three were made by non-specialists without MathSciNet or zbMATH access.
**We therefore claim the rule as "not found", not as new**, and ask a
specialist reader to say whether it is a known corollary of Rush–Shi's
conjugacy or of the toggle description of rowmotion.

### 7.5 The E₆ control and two inversions

Each 27-sheet of the board (colour 6 deleted) is J(P₆) with |P₆| = 16; its
rowmotion has order 12 = h(E₆) with orbits [12, 12, 3] (Rush–Shi again,
and the sealed values of the machine's E₆ ancestor); its pair types are
the Schläfli adjacency; and the same rule with the E₆ diagram is exact
there. Two registered guesses failed and are reported as such: the eight
antipodal steps of Ψ are **not** the eight singleton toggles (two
different 8-sets), and the E₆ clock keeps **63.5 %**, less than the E₇
clock's 65.1 % — smaller toggle sets do not mean fewer flips.

## 8. The twisted coset: fourteen classes, exactly [C, SM-047–051]

The conjugacy classes of O₈⁺(2).3 lying in the outer coset Ω·Φ are
classical data (ATLAS; CTblLib). Our model re-derives them from the
explicit permutation group of §5 by centralizer closures (Schreier
generators over transversals of the relevant fibres), with per-element
conjugacy tests on sampled elements, and finds:

```text
order   classes   centralizer in Ω        density
 24        2      8, 8                    1/8 + 1/8
 21        1      7                       1/7
 18        1      6                       1/6
 12        4      32, 4, 48, 96           5/16
  9        1      18                      1/18
  6        3      192, 24, 48             13/192
  3        2      12,096 (the turn), 216  1/12,096 + 1/216
                                    sum = 1 exactly
```

Fourteen classes whose densities sum to 1, so there is no fifteenth. Along
the way: the turn's centralizer in Ω is exactly G₂(2) (its class has
14,400 elements); the eighteen's centralizer is its own cube's group,
order 6; the "heart" x = e⁶ of the eighteen has centralizer of order 1,944
with centre of order 9; the still point holds the heart (56 of its
order-3 elements) and the eighteen's cube (504 of its order-6 elements)
but no eighteen; both twenty-fours are made from the still point's two
order-8 classes, one each. Four registered guesses were INVERTED across
these stones and each was settled exactly by a post-reveal computation:
the order-12 sample contains a third cycle type the still point never
produces, carrying a quarter of the coset; the still point's own
order-12 type splits into two classes (1/48 and 1/96); the heart of the
still point turns into a turn, while its other order-3 class turns into
the roof's commonest three-beat; and the first census overshot 1 by
exactly 1/12,096, the duplicate that forced the last correction.

*Framing:* this is a re-derivation of published data by an independent
route, presented as a check on the model, not as new group theory. Its
value is that every later identification (§9) is made against numbers the
model produced before the table was consulted.

## 9. The names [P cited + C, SM-052]

Against the GAP Character Table Library's table of O₈⁺(2).3 (Breuer,
CTblLib 1.3.11, `ctoorth2.tbl`; headers quoted verbatim with their source
and hash; no character values used): the outer class count 14 is forced
by the published class numbers (53 for Ω, 55 for Ω.3, a fusion fixing 14
and fusing 13 triples); the multiset of (order, centralizer order) of the
published outer classes equals ours tripled; all sixteen power-map
entries our fibres had recorded agree; three entries computed fresh agree.
The heart is class 3D of O₈⁺(2); the E₈ and D₄ Coxeter hearts are the
fused triple 3A/3B/3C; the involution fibres are 2A and 2E; the two
twenty-fours are told apart by their squares exactly as the table tells
them apart. 17/17.

## 10. The mirror is the E₆ diagram automorphism [C on a P fact, SM-053]

The node-6 coweight splits the 56 into two poles and two 27-sheets. The
machine's third gate pr swaps the sheets and fixes the poles, commutes
with ι and — our registered guess inverted — commutes with the sheet
clock Ψ₆. The reason is the post-reveal finding: **pr is an
order-isomorphism between the two sheets' ideal lattices J(P₆⁽⁰⁾) →
J(P₆⁽¹⁾)** (324/324 comparable pairs each way, principal ideals to
principal ideals) whose induced map on the join-irreducibles is the
colour map 0↔5, 2↔4, 1 and 3 fixed: **the E₆ Dynkin diagram automorphism.**
That the diagram automorphism swaps the two 27's and induces an
isomorphism of their minuscule posets is standard (Bourbaki; Green 2013;
see also Green–Xu 2024 for the statement "up to diagram automorphisms");
what is ours is that a gate built by other means is that automorphism.
The gates generate everything: |⟨Ψ, ι⟩| = 36, |⟨pr, ι⟩| = 4, and
**|⟨Ψ, pr⟩| = 56!** by Schreier–Sims, so ⟨Ψ, ι, pr⟩ = S₅₆; the Cayley
diameter of that generating set is at least 157 by counting [P]. 11 PASS
+ 1 INVERTED.

## 11. Refutations, at equal prominence

Across the twelve units, the registered expectations that failed:

- SM-038: the still point lifts split, not twisted.
- SM-041: the antipodal steps are not the singleton toggles; the E₆ clock
  keeps less than the E₇ clock.
- SM-050: the order-12 twisted types are not the still point's two; the
  still point's type is two classes, not one.
- SM-051: the heart at the still point turns into a turn, not into the
  class first guessed.
- SM-053: the mirror commutes with the sheet clock rather than
  normalizing it into another power.

Each is recorded in its stone with the first-run log kept. Nine first
runs across the September stones stopped on instrumentation errors of the
executor; none touched a registered result; every such log is shipped.

## 12. What is not claimed

No physical identification of any object here. No claim that the
Coxeter-number periodicity, the fixed group of triality, the outer
classes of O₈⁺(2).3, or the action of the E₆ diagram automorphism on
minuscule posets are new. No claim of novelty for the parity rule beyond
"not found by three non-specialist searches" (§7.4). No claim that the
roof is minimal beyond minimal-found. Nothing about non-minuscule posets,
promotion, or birational rowmotion.

## 13. Reproducibility

Every unit is a Python 3 script with numpy (and sympy in one place), run
under a brief whose SHA-256 was recorded before the script existed; each
script re-checks the brief's hash as its first test. The second author
re-executed all twelve from clean checkouts on an independent machine
(2026-09-08): every tally matched, and the logs of eight units were
byte-identical modulo line endings and timings. His audit found that
several verifiers depend on caches shipped in earlier envelopes and not
named in the cover notes; the dependency table below is the correction:

| unit | verifier | external inputs |
|---|---|---|
| SM-030 | `verify_stone_v_we8_roof.py` | `_stone_u_cache/` (Stone U, regenerable by its own verifier) |
| SM-038 | `verify_stone_z_stillpoint.py` | `_stone_u_cache/`, `_stone_v_cache/`, `_stone_w_cache/ts_subspaces.npz` (regenerable by Stone W's verifier), `_stone_x_cache/` |
| SM-039 | `verify_stone_aa_roofclock.py` | the above + `_stone_z_cache/` |
| SM-040 | `verify_stone_ab_merkabit.py` | `scar56_data.json`, `_stone_z_cache/G_rows.npy` |
| SM-041 | `verify_stone_ac_parity_rule.py` | `scar56_data.json` only |
| SM-047–051 | `verify_stone_ai..am_*.py` | Stone AA's caches (`_stone_aa_cache/`), `_stone_z_cache/`, the Stone U/V/X caches, each replayed from scratch at the head of the script |
| SM-052 | `verify_stone_an_atlas_names.py` | the above + the two cited CTblLib header files shipped in `_stone_an_cache/` |
| SM-053 | `verify_stone_ao_mirror_and_gates.py` | `scar56_data.json` only |

The `kbar_*` files of Stone U (~180 MB) are excluded from every envelope
and are regenerated by that stone's verifier.

## References

- Bourbaki, N. *Lie Groups and Lie Algebras, Chapters 4–6.* Springer, 2002.
- Breuer, T. *The GAP Character Table Library*, Version 1.3.11. RWTH Aachen. (Tables "O8+(2)" and "O8+(2).3", file `ctoorth2.tbl`.)
- Cameron, P. J.; Fon-der-Flaass, D. G. Orbits of antichains revisited. *European J. Combin.* 16 (1995) 545–554.
- Conway, J. H. Three lectures on exceptional groups. In *Finite Simple Groups* (Oxford, 1969), Academic Press, 1971, 215–247. Reprinted in Conway–Sloane (1999), ch. 10.
- Conway, J. H.; Curtis, R. T.; Norton, S. P.; Parker, R. A.; Wilson, R. A. *ATLAS of Finite Groups.* Oxford University Press, 1985.
- Conway, J. H.; Sloane, N. J. A. *Sphere Packings, Lattices and Groups*, 3rd ed. Springer, 1999.
- Dolgachev, I. *Classical Algebraic Geometry: A Modern View.* Cambridge University Press, 2012.
- Green, R. M. *Combinatorics of Minuscule Representations.* Cambridge Tracts in Mathematics 199, Cambridge University Press, 2013.
- Green, R. M.; Xu, T. Branching rules of minuscule representations via a new partial order. arXiv:2402.06732 (2024), to appear in *Combinatorial Theory*.
- Kleidman, P. B. The maximal subgroups of the finite 8-dimensional orthogonal groups PΩ₈⁺(q) and of their automorphism groups. *J. Algebra* 110 (1987) 173–242.
- Okada, S. Birational rowmotion and Coxeter-motion on minuscule posets. *Electron. J. Combin.* 28(1) (2021) P1.17; arXiv:2004.05364.
- Proctor, R. A. Bruhat lattices, plane partition generating functions, and minuscule representations. *European J. Combin.* 5 (1984) 331–350.
- Reiner, V.; Stanton, D.; White, D. The cyclic sieving phenomenon. *J. Combin. Theory Ser. A* 108 (2004) 17–50.
- Rush, D. B.; Shi, X. On orbits of order ideals of minuscule posets. *J. Algebraic Combin.* 37 (2013) 545–569. doi:10.1007/s10801-012-0380-2.
- Stembridge, J. R. On minuscule representations, plane partitions and involutions in complex Lie groups. *Duke Math. J.* 73 (1994) 469–490.
- Striker, J.; Williams, N. Promotion and rowmotion. *European J. Combin.* 33 (2012) 1919–1942.
- Wilson, R. A. *The Finite Simple Groups.* Graduate Texts in Mathematics 251, Springer, 2009.

## Appendix A. The registry units and their seals

SM-030 (Stone V, 44/44), SM-038 (Stone Z, 19 + 1 inverted), SM-039 (Stone
AA, 16/16), SM-040 (Stone AB, 14/14), SM-041 (Stone AC, 9 + 2 inverted),
SM-047 (Stone AI, 15/15), SM-048 (Stone AJ, 17/17), SM-049 (Stone AK,
14/14), SM-050 (Stone AL, 15 + 2 inverted + 1 post-reveal), SM-051 (Stone
AM, 15 + 1 inverted + 1 post-reveal), SM-052 (Stone AN, 17/17), SM-053
(Stone AO, 11 + 1 inverted + 1 post-reveal). All twelve JOINT on both
parties' words as of 2026-09-06; all twelve re-executed on the Balashov
side 2026-09-08 with matching tallies.

Related sealed unit not in this spine: SM-054 (Stone AP, 2026-09-07) —
the centralizer of Ψ in S₅₆ meets W(E₇) in the identity alone, so no
Weyl-group element commutes with the clock; awaiting the second author's
word.
