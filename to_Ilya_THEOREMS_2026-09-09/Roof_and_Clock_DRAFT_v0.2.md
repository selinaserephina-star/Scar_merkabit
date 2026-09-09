---
title: "The Roof and the Clock"
subtitle: "A verified computational model of W⁺(E₈), O₈⁺(2).3 and rowmotion on the E₇ minuscule poset, with three theorems on the non-linearity of rowmotion — DRAFT v0.2"
author: "Selina Stenberg · Ilya Balashov · with Claude (Anthropic Fable 5)"
date: "2026-09-09 — draft v0.2 (v0.1 of the same day plus §§7.6–7.7 on SM-055/056); prepared on the Stenberg side after Ilya Balashov's spine audits of 2026-09-08; sealed-not-sent"
---

**Status.** Draft of the paper whose spine both parties agreed on
(SM-030, 038, 039, 040, 041, 047–053 of the joint registry), written
after Ilya Balashov's independent re-execution of all twelve units from
clean checkouts (his audits of 2026-09-08: every pass/fail tally
reproduced, every disclosed inversion matching). The framing follows his
publication response of the same date: the classical facts are cited at
first use, the computational model is presented as a model, the
identification work is presented as identification, and the one
mechanism put forward as new is now stated as theorems (§7.6, SM-056)
with the family of numbers behind it (§7.7, SM-055), pending a
specialist literature check. v0.2 differs from v0.1 only in §§1, 7,
12–13 and the abstract; nothing computational in the spine was changed
or re-run. Claims are graded: **[P]** classical with citation or proved
here, **[C]** computed exactly by a named verifier under a brief locked
before code, **[obs]** observed and not explained. No physical
identification is asserted.

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
(2013); we do not claim them. What we add is the identification of a
machine built by other means with that rowmotion, and a study of how far
the Rush–Shi bijection is from an isometry. On the E₇ board a pair of
states keeps its inner-product sign under one tick if and only if a
parity computed from the two toggle sets is even, with zero exceptions
on 1,485 pairs, and the clock commutes with no element of W(E₇). Across
the whole simply-laced minuscule family we prove that rowmotion is a Weyl
element exactly on chains, that its half-turn is a Weyl element exactly
on the vector representations of D_n, and that the fraction of pair
types it keeps has closed forms on two families; the E₇ clock fails every
linearity condition at the first place it can. Finally, the machine's
mirror pr is shown to be the E₆ diagram automorphism acting on the two
27-sheets' ideal lattices, a classical object, and the clock and the
mirror together generate the full symmetric group on the 56 states. Every
registered guess that failed is reported at the same prominence as the
results.

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
   §§3–6 and §8.
2. **Identification work.** Two purpose-built machines — a 56-state
   machine with three gates on the Stenberg side, a PSL(2,7) tower on the
   Balashov side — are identified, object by object, with the classical
   structure: the 56 states with the vector block, the gate ι with a
   transvection, the clock with rowmotion, the mirror with the diagram
   automorphism, each twisted class with its ATLAS name. This is real and
   narrow: it says what the machines are, not that the structure is new.
   §§6, 7.1, 9, 10.
3. **Three theorems and one rule on the non-linearity of rowmotion.**
   Rush–Shi make rowmotion on a minuscule poset conjugate to a Coxeter
   element; a Coxeter element is an isometry of the weights and rowmotion
   in general is not. We prove for which minuscule posets rowmotion, or
   its half-turn, is itself a Weyl element, give the defect in closed
   form on two families (§7.6), tabulate it for 42 cases (§7.7), and
   give the exact per-pair rule on the E₇ board (§7.2). Three
   non-specialist literature searches found no match; we claim these as
   "not found" until a specialist search has been made (§7.4).

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
1994; Green 2013); each join-irreducible is coloured by the simple root
of its unique cover, and the multiplicity of colour i in P_λ is the
coefficient of α_i in λ − w₀λ. Rowmotion on the order ideals J(P) is
R(I) = the ideal generated by the minimal elements of P ∖ I
(Cameron–Fon-der-Flaass 1995; Striker–Williams 2012). **Theorem
(Rush–Shi 2013).** For P a minuscule poset, rowmotion on J(P) is
conjugate, under the natural bijection J(P) ≅ Wλ, to the action of any
Coxeter element of W on the weights; in particular its order is the
Coxeter number h and its orbit structure is that of a Coxeter element,
and (J(P), R, rank generating function) exhibits the cyclic sieving
phenomenon (Reiner–Stanton–White 2004). For E₇, λ minuscule, |P| = 27,
|J(P)| = 56, h = 18. Okada (2021) extends the statement to birational
rowmotion. The simply-laced minuscule weights are ω_k of A_n; ω₁,
ω_{n−1}, ω_n of D_n; ω₁, ω₆ of E₆; ω₇ of E₇. We normalize ⟨α, α⟩ = 2, so
that ⟨w, α_i⟩ is the i-th Dynkin label of w.

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

## 7. The clock is rowmotion; the parity rule; the non-linearity theorems

### 7.1 The identification [C, SM-041]

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
Stone AQ (§7.7) re-derives the same numbers from the Cartan matrix of E₇
alone, without the sealed data — an independent second derivation of the
identification.

### 7.2 The rule [C, SM-041]

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

### 7.3 Why it holds [P]

B is bilinear and the type of a non-antipodal pair is B(u, u′). Hence
B(Ψu, Ψu′) − B(u, u′) = B(δu, u′) + B(u, δu′) + B(δu, δu′). With δ the sum
of the toggled simple roots β_c, B(β_c, w′) = ⟨α_c, w′⟩ mod 2 = |label_c(w′)|
for minuscule labels in {−1, 0, 1}, and B(β_c, β_c′) is the Cartan entry
mod 2, i.e. Dynkin adjacency. The three terms are t₁, t₂, t₃. **The
content of the rule is therefore the identification of §7.1 and the
count of §7.2**, not the algebra; once Ψ is rowmotion the rule is a
one-line consequence of the bilinear form. The right object for the
novelty question is therefore the one §§7.6–7.7 study: how far the
Rush–Shi bijection is from an isometry, for which minuscule posets it is
one, and what the defect is.

### 7.4 Literature status

Two targeted searches on the Balashov side (toggle groups, periodicity,
homomesy, cyclic sieving; rowmotion against an ambient inner-product sign
on minuscule weights) found no match; a third on the Stenberg side
(rowmotion with quadratic or bilinear forms mod 2; the E₇ 56-ideal case
and the Gosset graph) found the Coxeter-motion and birational literature
(Okada 2021) and the toggle literature, and no per-pair statement and no
study of when the Rush–Shi conjugacy is realized by a Weyl element. All
three were made by non-specialists without MathSciNet or zbMATH access.
**We therefore claim §§7.2, 7.6, 7.7 as "not found", not as new**, and
ask a specialist reader to say whether they are known corollaries of
Rush–Shi's conjugacy or of the toggle description of rowmotion.

### 7.5 The E₆ control and two inversions [C, SM-041]

Each 27-sheet of the board (colour 6 deleted) is J(P₆) with |P₆| = 16; its
rowmotion has order 12 = h(E₆) with orbits [12, 12, 3] (Rush–Shi again,
and the sealed values of the machine's E₆ ancestor); its pair types are
the Schläfli adjacency; and the same rule with the E₆ diagram is exact
there. Two registered guesses failed and are reported as such: the eight
antipodal steps of Ψ are **not** the eight singleton toggles (two
different 8-sets), and the E₆ clock keeps **63.5 %**, less than the E₇
clock's 65.1 % — smaller toggle sets do not mean fewer flips.

### 7.6 The non-linearity theorems [P; checked C, SM-056]

Let λ be a simply-laced minuscule weight with poset P = P_λ, Coxeter
number h, rowmotion R carried to the weights Wλ. For λ = ω_k write c_k
for the multiplicity of colour k in P (the coefficient of α_k in λ + λ*),
s_j for the number of elements of P of rank j (0 ≤ j ≤ h − 2), and
σ = (s₀, …, s_{h−2}, c_k), the *extended rank sequence*, of length h.

**Lemma.** (a) R(λ) = w₀λ; the bottom w₀λ = −λ* has a single nonzero
label, −1 at the dual node k*, hence a single cover p₀ = w₀λ + α_{k*},
which is the unique minimal element of P, and R(w₀λ) = p₀. Consequently
⟨λ, w₀λ⟩ = ⟨λ,λ⟩ − c_k and ⟨w₀λ, p₀⟩ = ⟨λ,λ⟩ − 1. (b) The R-orbit of
w₀λ is the sequence of rank truncations P_{<j}; writing w(j) for their
weights, ⟨w(j), w(j+1)⟩ = ⟨λ,λ⟩ − σ_j for all j (indices mod h).

*Proof.* (a) ∅ ↦ the ideal generated by min P = {p₀}; and ⟨λ, λ − w₀λ⟩ =
Σ c_i ⟨ω_k, α_i⟩ = c_k. (b) The minimal elements of P ∖ P_{<j} are the
rank-j elements and generate P_{<j+1}; w(j+1) − w(j) is the sum of their
colours' simple roots, each added at a label −1 of w(j), so the inner
product drops by s_j; the wrap-around step λ → w₀λ drops by c_k by (a);
all weights have equal norm. ∎

**Theorem 1.** R ∈ W ⟺ P is a chain ⟺ λ ∈ {ω₁, ω_n} of A_n; then R is
the Coxeter element s₁ ⋯ s_n, the cyclic shift of e₁, …, e_{n+1}.

*Proof.* If R ∈ W it is an isometry, so by Lemma (a) on the pair
(λ, w₀λ) ↦ (w₀λ, p₀), ⟨λ,λ⟩ − c_k = ⟨λ,λ⟩ − 1, i.e. c_k = 1. From the
classification, c_k = min(k, n+1−k) for A_n ω_k, 2 for D_n ω₁, ⌊n/2⌋ for
D_n ω_n (n ≥ 4), 2 for E₆ ω₁, 3 for E₇ ω₇; so c_k = 1 only for A_n with
k ∈ {1, n}, whose poset is a chain. Conversely on the chain the ideals
are the initial segments and R is the cyclic shift, a permutation matrix
in W(A_n) = S_{n+1}. ∎

**Theorem 2.** Let h be even and m = h/2. Then R^m ∈ W ⟺ P is a chain
or λ is the vector representation of D_n, n ≥ 3 (with D₃ ω₁ = A₃ ω₂ and,
for D₄, the triality images ω₃, ω₄). In the vector case, on the weights
±e_i,

  R^{n−1}(e_i) = −e_{n−i} (1 ≤ i ≤ n−1),  R^{n−1}(e_n) = (−1)^{n−1} e_n,

a signed permutation with an even number of sign changes, in W(D_n).

*Proof.* (Obstruction.) If R^m ∈ W, it is an isometry with R^m(w(j)) =
w(j+m), so by Lemma (b) σ_{j+m} = σ_j for all j: σ is m-periodic, and
since σ₀ = s₀ = 1, σ_m = 1 is necessary. For A_n ω_k with 1 < k < n
(n odd, m = (n+1)/2), P is the k × (n+1−k) rectangle and s_m =
min(k, n+1−k) ≥ 2. For D_n ω_n, n ≥ 5 (m = n−1), P is the shifted
staircase {(i,j): 1 ≤ i ≤ j ≤ n−1} with rank i+j−2, and s_{n−1} =
⌊(n+1)/2⌋ − 1 ≥ 2. For E₆ ω₁ (m = 6) the ranks are 1,1,1,2,2,2,2,2,1,1,1
and s₆ = 2; for E₇ ω₇ (m = 9) they are 1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1
and s₉ = 2. For D_n ω₁ (m = n−1), P is a chain of n−2 above the
antichain {e_n, −e_n} above a chain of n−2, with c₁ = 2, and σ =
(1^{n−2}, 2, 1^{n−2}, 2) is (n−1)-periodic; the triality images at n = 4
and the chains pass likewise. (Sufficiency.) On D_n ω₁ the ideals are ∅,
the prefixes of the lower chain, the three ideals adding e_n, −e_n, or
both, and the extensions along the upper chain; rowmotion cycles
∅ → … → P in 2n−2 steps and swaps the two one-sided ideals. On weights:
−e₁ → −e₂ → ⋯ → −e_{n−1} → e_{n−1} → ⋯ → e₁ → −e₁, and e_n ↔ −e_n.
Hence R^{n−1}(±e_i) = ∓e_{n−i} for i ≤ n−1 and R^{n−1}(e_n) =
(−1)^{n−1} e_n: the coordinate permutation i ↔ n−i with n (n even) or
n−1 (n odd) sign changes, even either way. ∎

**Corollary.** R^j ∈ W implies σ is j-periodic; so the linear powers of
rowmotion are among the periods of σ. For E₇, σ has no period below 18:
no power of the clock but the identity is a Weyl element (SM-054's
C_W(Ψ) ∩ ⟨Ψ⟩ = 1, by hand).

**Theorem 3.** Let κ(R) be the fraction of unordered pairs {w, w′} with
⟨Rw, Rw′⟩ = ⟨w, w′⟩. Then κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1)) for n ≥ 3, and
κ(A_n ω₂) = 1 − (3n² − 9n + 4)/C(C(n+1,2), 2) for n ≥ 3.

*Proof.* (D_n ω₁) Types are 0 and −1 (the n antipodal pairs). By the
cycle above, {e_n, −e_n} is the only antipodal pair R keeps; the other
n−1 become non-antipodal and, R permuting the pairs, n−1 non-antipodal
pairs become antipodal: 2(n−1) of n(2n−1) pairs change. (A_n ω₂) Weights
are 2-subsets {a<b} of [n+1]; a pair's type is |S∩T| ∈ {0,1}. The ideals
(x₁ ≥ x₂) of the 2 × (n−1) rectangle correspond to {n−x₁, n+1−x₂}, and
rowmotion on the rectangle gives R{a,b} = {a−1, b−1} for a ≥ 2, b ≥ a+2;
R{a,a+1} = {a−1, n+1} (a ≥ 2); R{1,b} = {b−2, b−1} (b ≥ 3); R{1,2} =
{n, n+1}. With ρ the rotation i ↦ i−1 (mod n+1), a Coxeter element and
an isometry, R = ρ∘φ where φ fixes every 2-subset outside
T = {{a,a+1}: 2 ≤ a ≤ n} ∪ {{1,b}: 2 ≤ b ≤ n+1} and permutes T by
{a,a+1} ↦ {1,a}, {1,b} ↦ {b−1,b} (b ≥ 3), {1,2} ↦ {1,n+1}; so
κ(R) = κ(φ). A pair (S ∈ T, G ∉ T) changes type iff a+1 ∈ G
(S = {a,a+1}), iff b−1 ∈ G (S = {1,b}, b ≥ 3), or iff exactly one of
2, n+1 lies in G (S = {1,2}): 2(n−2)² + 2(n−3) pairs. Inside T, of the
(n−2) + 2(n−1) + C(n,2) intersecting pairs exactly 4n−5 stay
intersecting, so (n−1)(n−2) pairs change. Total 3n² − 9n + 4. ∎

Every step of these proofs was re-checked on the data (SM-056, 10/10):
the lemma on all 42 cases of §7.7; c_k = 1 ⟺ chain ⟺ R ∈ W; the
principal orbit and the rank sequences; periodicity ⟺ R^{h/2} ∈ W with
exactly the predicted case list; the vector formula for n = 3..9; the
explicit rowmotion on 2-subsets and both κ formulas exactly for n = 3..9.
A registered guess that the analogous count on A_n ω₃ is a degree-4
polynomial in n was confirmed to n = 10 (12·D₃(n) = 15n⁴ − 110n³ + 165n²
+ 314n − 432), suggesting degree 2k − 2 for ω_k [obs].

### 7.7 The defect across the minuscule family [C, SM-055]

One machine built from the Cartan matrix alone (weights in Dynkin labels,
the lattice by w → w − α_i at label 1, its join-irreducibles, rowmotion
as the join of the minimal elements of the complement) computes for 42
cases — A_n, all ω_k, n ≤ 7; D_n, ω₁ and both half-spins, n = 4..7; E₆;
E₇ — the kept fraction κ, the random baseline κ₀ = Σ p_t², the best
pointwise agreement a(R) with a Coxeter element, the altitude ν(R)
(Hamming distance to the nearest Weyl element, W enumerated as
permutations of the weights where |W| ≤ 322,560; E₇ from SM-016), and
the linear centralizer C_W(R).

| case | \|Wλ\| | h | R cycle type | κ(R) | κ₀ | a(R) | ν(R) | \|C_W(R)\| |
|---|---|---|---|---|---|---|---|---|
| A_n ω₁, ω_n | n+1 | n+1 | (n+1) | 1 | 1 | n+1 | 0 | n+1 |
| A₃ ω₂ = D₃ ω₁ | 6 | 4 | 4·2 | 11/15 | 0.680 | 3 | 3 | 2 |
| A₄ ω₂ | 10 | 5 | 5² | 29/45 | 0.556 | 5 | 5 | 1 |
| A₅ ω₂ | 15 | 6 | 6²·3 | 71/105 | 0.510 | 6 | 9 | 1 |
| A₅ ω₃ | 20 | 6 | 6³·2 | 58/95 | 0.452 | 7 | 13 | 1 |
| A₆ ω₂ | 21 | 7 | 7³ | 76/105 | 0.500 | 10 | 11 | 1 |
| A₆ ω₃ | 35 | 7 | 7⁵ | 339/595 | 0.419 | 10 | 25 | 1 |
| A₇ ω₂ | 28 | 8 | 8³·4 | 145/189 | 0.506 | 15 | 13 | 1 |
| A₇ ω₃ | 56 | 8 | 8⁷ | 431/770 | 0.405 | 12 | 44 | 1 |
| A₇ ω₄ | 70 | 8 | 8⁸·4·2 | 417/805 | 0.380 | 12 | 56 | 1 |
| D₄ ω₁ (= ω₃, ω₄) | 8 | 6 | 6·2 | 11/14 | 0.755 | 4 | 3 | 2 |
| D₅ ω₁ | 10 | 8 | 8·2 | 37/45 | 0.802 | 5 | 5 | 2 |
| D₅ ω₅ | 16 | 8 | 8² | 19/30 | 0.556 | 5 | 10 | 1 |
| D₆ ω₁ | 12 | 10 | 10·2 | 28/33 | 0.835 | 6 | 5 | 2 |
| D₆ ω₆ | 32 | 10 | 10³·2 | 79/124 | 0.469 | 9 | 19 | 1 |
| D₇ ω₁ | 14 | 12 | 12·2 | 79/91 | 0.858 | 7 | 7 | 2 |
| D₇ ω₇ | 64 | 12 | 12⁵·4 | 295/504 | 0.432 | 13 | 48 | 1 |
| E₆ ω₁ | 27 | 12 | 12²·3 | 223/351 | 0.527 | 9 | 15 | 1 |
| E₇ ω₇ | 56 | 18 | 18³·2 | 501/770 | 0.482 | 14 | 38 | 1 |

(Dual representations give equal rows.) Rush–Shi's conjugacy holds on the
data in all 42 cases. The E₇ row reproduces §§6–7.1 and SM-054 from the
Cartan matrix alone. Two registered guesses were inverted and are the
content of Theorem 2 and of an observation: the linear centralizer is not
trivial on the vector representations (it is the half-turn), and κ does
not increase with rank along every family (it does along D_n ω₁ and A_n
ω₂, and falls along the half-spins). κ exceeds κ₀ in every non-chain
case. E₆ and E₇ sit where the D₅–D₇ spinors sit; the 56-board's clock is
as far from linear as rowmotion on a minuscule poset gets.

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

Across the twelve spine units, the registered expectations that failed:

- SM-038: the still point lifts split, not twisted.
- SM-041: the antipodal steps are not the singleton toggles; the E₆ clock
  keeps less than the E₇ clock.
- SM-050: the order-12 twisted types are not the still point's two; the
  still point's type is two classes, not one.
- SM-051: the heart at the still point turns into a turn, not into the
  class first guessed.
- SM-053: the mirror commutes with the sheet clock rather than
  normalizing it into another power.

And in the two units of §§7.6–7.7: SM-055's guesses that the linear
centralizer is trivial off the chains (false on the vector
representations, where it is the half-turn) and that κ rises with rank
in every family (false on the half-spins). Each is recorded in its stone
with the first-run log kept. Nine first runs across the September stones
stopped on instrumentation errors of the executor; none touched a
registered result; every such log is shipped.

## 12. What is not claimed

No physical identification of any object here. No claim that the
Coxeter-number periodicity, the fixed group of triality, the outer
classes of O₈⁺(2).3, or the action of the E₆ diagram automorphism on
minuscule posets are new. No claim of novelty for §§7.2, 7.6, 7.7 beyond
"not found by three non-specialist searches" (§7.4). No claim that the
roof is minimal beyond minimal-found. Nothing about the non-simply-laced
minuscule weights (B_n ω_n, C_n ω₁), about non-minuscule posets,
promotion, or birational rowmotion. No formula for κ on the spinors, on
E₆, E₇, or on A_n ω_k with k ≥ 3 beyond the observed polynomial degree at
k = 3.

## 13. Reproducibility

Every unit is a Python 3 script with numpy (and sympy in one place), run
under a brief whose SHA-256 was recorded before the script existed; each
script re-checks the brief's hash as its first test. The second author
re-executed all twelve spine units from clean checkouts on an independent
machine (2026-09-08): every tally matched, and the logs of eight units
were byte-identical modulo line endings and timings. His audit found that
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
| SM-055 | `verify_stone_aq_rush_shi_defect.py` | none (Cartan matrices only) |
| SM-056 | `verify_stone_ar_nonlinearity_theorems.py` | the file `verify_stone_aq_rush_shi_defect.py` (its machine is loaded verbatim; hash logged) |

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

Spine: SM-030 (Stone V, 44/44), SM-038 (Stone Z, 19 + 1 inverted), SM-039
(Stone AA, 16/16), SM-040 (Stone AB, 14/14), SM-041 (Stone AC, 9 + 2
inverted), SM-047 (Stone AI, 15/15), SM-048 (Stone AJ, 17/17), SM-049
(Stone AK, 14/14), SM-050 (Stone AL, 15 + 2 inverted + 1 post-reveal),
SM-051 (Stone AM, 15 + 1 inverted + 1 post-reveal), SM-052 (Stone AN,
17/17), SM-053 (Stone AO, 11 + 1 inverted + 1 post-reveal). All twelve
JOINT on both parties' words as of 2026-09-06; all twelve re-executed on
the Balashov side 2026-09-08 with matching tallies.

Added in v0.2 (§§7.6–7.7), awaiting the second author's word: SM-055
(Stone AQ, 8 + 2 inverted, 2026-09-09) and SM-056 (Stone AR, 10/10,
2026-09-09). Related, not in this paper: SM-054 (Stone AP, 22 + 2
disclosed, 2026-09-07) — the centralizer of Ψ in S₅₆ meets W(E₇) in the
identity alone; reproduced on the Balashov side 2026-09-08.
