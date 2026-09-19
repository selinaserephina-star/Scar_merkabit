---
title: "The Roof and the Clock"
subtitle: "A verified computational model of W⁺(E₈), O₈⁺(2).3 and rowmotion on the E₇ minuscule poset, with three theorems on the non-linearity of rowmotion, and what the symmetry group and the clock share"
author:
  - Selina Stenberg
  - Ilya Balashov
  - "with Claude (Anthropic)"
date: "Version 1.0 — 19 September 2026"
---

**Status.** Version 1.0, prepared on the Stenberg side from the sealed
joint record for the second author's final review; submission requires both
authors' word. The paper describes the spine both parties agreed on (SM-030,
038, 039, 040, 041, 047–053 of the joint registry) and the units added since
(SM-054–066, §11), every one of which is JOINT: re-executed or re-derived
independently by the second author and accepted on his word (Appendix A). The
framing follows his publication response of 2026-09-08: classical facts are
cited at first use, the computational model is presented as a model, the
identification work as identification, and the one mechanism put forward as
new is stated as theorems (§7.6) with the family of numbers behind it (§7.7)
and a literature search behind the word "not found" (§7.4, Appendix B).
Version history: v0.1 (2026-09-09, the spine); v0.2 (09-09, §§7.6–7.7,
approved by the second author 09-10); v0.3 (09-11, §§7.8–7.13); v0.4–0.5
(09-13, §§11–12); v0.6 (09-13, §7.12.4); v0.7 (09-14, the second author's
acceptances and references); v0.8 (09-14, §11.9); v1.0 (09-19, stale status
lines removed, Appendix B added, display formulas typeset; nothing
computational changed or re-run since v0.3; §7.12.4's B₈ paragraph added the
same day, SM-067).
Claims are graded: **[P]** classical with citation or proved
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

In §§7.8–7.13 we then ask what the symmetry group and the clock share,
across the whole minuscule family. The Weyl group shares with any
clock-translate of itself only the centralizer of that clock power, with
the exceptions named and, by the end, explained; the longest element
reverses the clock; three label counts are homomesic (Rush–Wang's
antichain homomesy read in the board's letters) and so is the toggle
size, a corollary of Defant–Hopkins–Poznanović–Propp; the one anomaly in
the family has a mechanism — on the 4-cube the clock's half-turn is a
Weyl element on one of its two orbits — and the vector boards' shared
grammar is the centralizer of the clock at double speed; and the clock
normalises no nontrivial subgroup of W(E₇), so the Clifford-hierarchy
analogy for it holds for one level and no further.

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
   give the exact per-pair rule on the E₇ board (§7.2). A literature
   search — four targeted searches, the complete arXiv rowmotion corpus to
   September 2026, zbMATH Open, and the primary texts read for the question
   (§7.4, Appendix B) — found no match; we claim these as "not found", not
   as new.

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
PSL(2,7) on the Balashov side (PSL(2,7) ⊃ C₆×C₂, A₅, S₄, A₄, C₂; developed,
with its bridge into Sp₆(2), in §11) and a
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

Write $\delta(u) = u + \Psi u$; $\delta$ is the XOR of the simple-root masks toggled by
rowmotion at $u$ (toggle sizes {1: 8, 2: 28, 3: 11, 4: 2, 5: 3, 6: 2, 9: 1,
27: 1}). For a non-antipodal pair {u, u′}, with t₁ the number of toggled
colours of u at which u′ has an edge, t₂ the same with the roles
exchanged, and t₃ the number of Dynkin-adjacent pairs between the two
toggle multisets:

$$\operatorname{type}(u,u')\ \text{is kept under}\ \Psi \iff t_1 + t_2 + t_3 \equiv 0 \pmod 2 .$$

Zero exceptions on all 1,485 non-antipodal pairs; with the 28 antipodal
pairs the kept count is 1,002 of 1,540 = 65.06 %, the number of §6. The
same rule with the k-fold toggle multiset is exact for every power Ψ^k
(k = 1..17) and reproduces the whole measured profile. The eight cells
(t₁, t₂, t₃) and their populations are tabulated in the stone; the
dominant kept cell is (1, 1, 0) with 553 pairs.

### 7.3 Why it holds [P]

$B$ is bilinear and the type of a non-antipodal pair is $B(u, u')$. Hence

$$B(\Psi u, \Psi u') - B(u, u') = B(\delta u, u') + B(u, \delta u') + B(\delta u, \delta u').$$

With $\delta$ the sum of the toggled simple roots $\beta_c$,
$B(\beta_c, w') = \langle \alpha_c, w' \rangle \bmod 2 = |\mathrm{label}_c(w')|$
for minuscule labels in $\{-1, 0, 1\}$, and $B(\beta_c, \beta_{c'})$ is the Cartan entry
mod 2, i.e. Dynkin adjacency. The three terms are $t_1, t_2, t_3$. **The
content of the rule is therefore the identification of §7.1 and the
count of §7.2**, not the algebra; once Ψ is rowmotion the rule is a
one-line consequence of the bilinear form. The right object for the
novelty question is therefore the one §§7.6–7.7 study: how far the
Rush–Shi bijection is from an isometry, for which minuscule posets it is
one, and what the defect is.

### 7.4 Literature status

The question is whether the statements of §§7.2, 7.6 and 7.7 — for which
minuscule posets rowmotion, or a power of it, is itself a Weyl group
element; the per-pair parity rule; the defect κ — are stated or proved
anywhere. Seven searches were made; Appendix B records them. In brief:

- Two targeted searches on the Balashov side (toggle groups, periodicity,
  homomesy, cyclic sieving; rowmotion against an ambient inner-product sign
  on minuscule weights) and one on the Stenberg side (rowmotion with
  quadratic or bilinear forms mod 2; the E₇ 56-ideal case and the Gosset
  graph) found the Coxeter-motion and birational literature (Okada 2021)
  and the toggle literature, and no per-pair statement and no study of
  when the Rush–Shi conjugacy is realized by a Weyl element.
- A fourth (Balashov, 2026-09-10) followed the full citation trail of
  Rush–Shi (2013) on zbMATH Open — thirty citing documents, all read —
  with the same result.
- On 2026-09-19 (Stenberg side) the complete arXiv corpus of papers
  mentioning rowmotion — 57 documents, 2014 to September 2026, listed in
  Appendix B — was enumerated through the arXiv API and every title and
  abstract read; the zbMATH Open API was queried for the same term; and
  the primary texts were read for the specific question: Rush–Shi (2013),
  Okada (2021), Hopkins (2020) and Thomas–Williams (2019). None states
  that rowmotion on a minuscule poset is, or is not, an element of the
  Weyl group; none characterises the posets on which it or its half-turn
  is; none mentions an inner product, an isometry, or a per-pair rule.

Three adjacent results are cited for the specialist reader's benefit and
are not the same statement. Okada (2021) introduces *Coxeter-motion*, a
product of file toggles, and proves it conjugate to rowmotion in the
(birational) toggle group — two different maps related by conjugacy, the
same relation Rush–Shi establish between rowmotion and a Coxeter element
acting on W/W_J; neither paper asks when the conjugating element can be
taken trivial, which is the content of Theorems 1–2. Marczinzik–Thomas–
Yıldırım (2024) study a homological "Coxeter matrix" (built from the
incidence algebra's Cartan matrix) alongside rowmotion, proving a
different commutation identity. Panyushev (2016) gives a bijection
indexing lower ideals of weight posets by Weyl group elements, not an
identity between rowmotion and one. The easy half of Theorem 1 — on a
chain, rowmotion is the cyclic shift, hence a Coxeter element — is
classical (Rush–Shi attribute the chain and product-of-chains cases to
Stanley; Striker–Williams 2012, Thm 6.1).

**We therefore claim §§7.2, 7.6, 7.7 as "not found", not as new.** The
searches were made without MathSciNet access; a specialist reader who
knows these as corollaries of Rush–Shi's conjugacy or of the toggle
description of rowmotion is asked for the reference. The same status is
claimed for §§7.8–7.13.

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

Let $\lambda$ be a simply-laced minuscule weight with poset $P = P_\lambda$, Coxeter
number $h$, rowmotion $R$ carried to the weights $W\lambda$. For $\lambda = \omega_k$ write $c_k$
for the multiplicity of colour $k$ in $P$ (the coefficient of $\alpha_k$ in $\lambda + \lambda^*$),
$s_j$ for the number of elements of $P$ of rank $j$ ($0 \le j \le h-2$), and

$$\sigma = (s_0, \dots, s_{h-2}, c_k),$$

the *extended rank sequence*, of length $h$.

**Lemma.** (a) $R(\lambda) = w_0\lambda$; the bottom $w_0\lambda = -\lambda^*$ has a single nonzero
label, $-1$ at the dual node $k^*$, hence a single cover $p_0 = w_0\lambda + \alpha_{k^*}$,
which is the unique minimal element of $P$, and $R(w_0\lambda) = p_0$. Consequently

$$\langle \lambda, w_0\lambda \rangle = \langle \lambda,\lambda \rangle - c_k, \qquad
\langle w_0\lambda, p_0 \rangle = \langle \lambda,\lambda \rangle - 1 .$$

(b) The $R$-orbit of
$w_0\lambda$ is the sequence of rank truncations $P_{<j}$; writing $w(j)$ for their
weights,

$$\langle w(j), w(j+1) \rangle = \langle \lambda,\lambda \rangle - \sigma_j \quad \text{for all } j \ (\text{indices mod } h).$$

*Proof.* (a) $\emptyset \mapsto$ the ideal generated by $\min P = \{p_0\}$; and
$\langle \lambda, \lambda - w_0\lambda \rangle = \sum_i c_i \langle \omega_k, \alpha_i \rangle = c_k$.
(b) The minimal elements of $P \setminus P_{<j}$ are the
rank-$j$ elements and generate $P_{<j+1}$; $w(j+1) - w(j)$ is the sum of their
colours' simple roots, each added at a label $-1$ of $w(j)$, so the inner
product drops by $s_j$; the wrap-around step $\lambda \to w_0\lambda$ drops by $c_k$ by (a);
all weights have equal norm. ∎

**Theorem 1.**

$$R \in W \iff P \text{ is a chain} \iff \lambda \in \{\omega_1, \omega_n\} \text{ of } A_n;$$

then $R$ is the Coxeter element $s_1 \cdots s_n$, the cyclic shift of $e_1, \dots, e_{n+1}$.

*Proof.* If $R \in W$ it is an isometry, so by Lemma (a) on the pair
$(\lambda, w_0\lambda) \mapsto (w_0\lambda, p_0)$, $\langle \lambda,\lambda \rangle - c_k = \langle \lambda,\lambda \rangle - 1$, i.e. $c_k = 1$. From the
classification, $c_k = \min(k, n+1-k)$ for $A_n\,\omega_k$, $2$ for $D_n\,\omega_1$, $\lfloor n/2 \rfloor$ for
$D_n\,\omega_n$ ($n \ge 4$), $2$ for $E_6\,\omega_1$, $3$ for $E_7\,\omega_7$; so $c_k = 1$ only for $A_n$ with
$k \in \{1, n\}$, whose poset is a chain. Conversely on the chain the ideals
are the initial segments and $R$ is the cyclic shift, a permutation matrix
in $W(A_n) = S_{n+1}$. ∎

**Theorem 2.** Let $h$ be even and $m = h/2$. Then

$$R^m \in W \iff P \text{ is a chain, or } \lambda \text{ is the vector representation of } D_n,\ n \ge 3$$

(with $D_3\,\omega_1 = A_3\,\omega_2$ and, for $D_4$, the triality images $\omega_3, \omega_4$).
In the vector case, on the weights $\pm e_i,$

$$R^{\,n-1}(e_i) = -e_{n-i} \ (1 \le i \le n-1), \qquad R^{\,n-1}(e_n) = (-1)^{n-1} e_n ,$$

a signed permutation with an even number of sign changes, in $W(D_n)$.

*Proof.* (Obstruction.) If $R^m \in W$, it is an isometry with $R^m(w(j)) =
w(j+m)$, so by Lemma (b) $\sigma_{j+m} = \sigma_j$ for all $j$: $\sigma$ is $m$-periodic, and
since $\sigma_0 = s_0 = 1$, $\sigma_m = 1$ is necessary. For $A_n\,\omega_k$ with $1 < k < n$
($n$ odd, $m = (n+1)/2$), $P$ is the $k \times (n+1-k)$ rectangle and $s_m =
\min(k, n+1-k) \ge 2$. For $D_n\,\omega_n$, $n \ge 5$ ($m = n-1$), $P$ is the shifted
staircase $\{(i,j): 1 \le i \le j \le n-1\}$ with rank $i+j-2$, and $s_{n-1} =
\lfloor (n+1)/2 \rfloor - 1 \ge 2$. For $E_6\,\omega_1$ ($m = 6$) the ranks are $1,1,1,2,2,2,2,2,1,1,1$
and $s_6 = 2$; for $E_7\,\omega_7$ ($m = 9$) they are $1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1$
and $s_9 = 2$. For $D_n\,\omega_1$ ($m = n-1$), $P$ is a chain of $n-2$ above the
antichain $\{e_n, -e_n\}$ above a chain of $n-2$, with $c_1 = 2$, and $\sigma =
(1^{n-2}, 2, 1^{n-2}, 2)$ is $(n-1)$-periodic; the triality images at $n = 4$
and the chains pass likewise. (Sufficiency.) On $D_n\,\omega_1$ the ideals are $\emptyset$,
the prefixes of the lower chain, the three ideals adding $e_n$, $-e_n$, or
both, and the extensions along the upper chain; rowmotion cycles
$\emptyset \to \dots \to P$ in $2n-2$ steps and swaps the two one-sided ideals. On weights:

$$-e_1 \to -e_2 \to \dots \to -e_{n-1} \to e_{n-1} \to \dots \to e_1 \to -e_1, \qquad e_n \leftrightarrow -e_n.$$

Hence $R^{\,n-1}(\pm e_i) = \mp e_{n-i}$ for $i \le n-1$ and $R^{\,n-1}(e_n) =
(-1)^{n-1} e_n$: the coordinate permutation $i \leftrightarrow n-i$ with $n$ ($n$ even) or
$n-1$ ($n$ odd) sign changes, even either way. ∎

**Corollary.** $R^j \in W$ implies $\sigma$ is $j$-periodic; so the linear powers of
rowmotion are among the periods of $\sigma$. For $E_7$, $\sigma$ has no period below 18:
no power of the clock but the identity is a Weyl element (SM-054's
$C_W(\Psi) \cap \langle \Psi \rangle = 1$, by hand).

**Theorem 3.** Let $\kappa(R)$ be the fraction of unordered pairs $\{w, w'\}$ with
$\langle Rw, Rw' \rangle = \langle w, w' \rangle$. Then, for $n \ge 3$,

$$\kappa(D_n\,\omega_1) = 1 - \frac{2(n-1)}{n(2n-1)}, \qquad
\kappa(A_n\,\omega_2) = 1 - \frac{3n^2 - 9n + 4}{\binom{\binom{n+1}{2}}{2}} .$$

*Proof.* ($D_n\,\omega_1$) Types are $0$ and $-1$ (the $n$ antipodal pairs). By the
cycle above, $\{e_n, -e_n\}$ is the only antipodal pair $R$ keeps; the other
$n-1$ become non-antipodal and, $R$ permuting the pairs, $n-1$ non-antipodal
pairs become antipodal: $2(n-1)$ of $n(2n-1)$ pairs change. ($A_n\,\omega_2$) Weights
are 2-subsets $\{a<b\}$ of $[n+1]$; a pair's type is $|S\cap T| \in \{0,1\}$. The ideals
$(x_1 \ge x_2)$ of the $2 \times (n-1)$ rectangle correspond to $\{n-x_1, n+1-x_2\}$, and
rowmotion on the rectangle gives

$$R\{a,b\} = \{a-1,\, b-1\} \qquad (a \ge 2,\ b \ge a+2),$$

$$R\{a,a+1\} = \{a-1,\, n+1\} \qquad (a \ge 2),$$

$$R\{1,b\} = \{b-2,\, b-1\} \qquad (b \ge 3),$$

$$R\{1,2\} = \{n,\, n+1\}.$$

With $\rho$ the rotation $i \mapsto i-1 \pmod{n+1}$, a Coxeter element and
an isometry, $R = \rho\circ\varphi$ where $\varphi$ fixes every 2-subset outside
$T = \{\{a,a+1\}: 2 \le a \le n\} \cup \{\{1,b\}: 2 \le b \le n+1\}$ and permutes $T$ by
$\{a,a+1\} \mapsto \{1,a\}$, $\{1,b\} \mapsto \{b-1,b\}$ ($b \ge 3$), $\{1,2\} \mapsto \{1,n+1\}$; so
$\kappa(R) = \kappa(\varphi)$. A pair ($S \in T$, $G \notin T$) changes type iff $a+1 \in G$
($S = \{a,a+1\}$), iff $b-1 \in G$ ($S = \{1,b\}$, $b \ge 3$), or iff exactly one of
$2, n+1$ lies in $G$ ($S = \{1,2\}$): $2(n-2)^2 + 2(n-3)$ pairs. Inside $T$, of the
$(n-2) + 2(n-1) + \binom{n}{2}$ intersecting pairs exactly $4n-5$ stay
intersecting, so $(n-1)(n-2)$ pairs change. Total $3n^2 - 9n + 4$. ∎

Every step of these proofs was re-checked on the data (SM-056, 10/10):
the lemma on all 42 cases of §7.7; c_k = 1 ⟺ chain ⟺ R ∈ W; the
principal orbit and the rank sequences; periodicity ⟺ R^{h/2} ∈ W with
exactly the predicted case list; the vector formula for n = 3..9; the
explicit rowmotion on 2-subsets and both κ formulas exactly for n = 3..9.
A registered guess that the analogous count on A_n ω₃ is a degree-4
polynomial in $n$ was confirmed to $n = 10$,

$$12\,D_3(n) = 15n^4 - 110n^3 + 165n^2 + 314n - 432,$$

suggesting degree $2k - 2$ for $\omega_k$ [obs].

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

### 7.8 The shared grammar on the 56 [C, SM-057]

#### 7.8.1 Setting

W = W(E₇), order 2,903,040, acting on the 56 states of the board (the
weights of the minuscule representation). W is the board's *grammar*:
every symmetry, every Weyl-invariant selection rule, every descent
marker (the involutions of a bridge PSL(2,7)), and the mirror up to one
bit, lie in it. The clock Ψ is rowmotion on the E₇ minuscule poset
(SM-041); it is not in W (SM-044) and commutes with nothing in W
(SM-054). After k ticks the grammar is the conjugate W_k = Ψ^k W Ψ^{−k},
an isomorphic copy of W inside S₅₆.

#### 7.8.2 Result 1 (what two instants share)

$$W \cap \Psi^k W \Psi^{-k} = \{1\} \quad (k = 1, \dots, 8,\ 10, \dots, 17), \qquad
W \cap \Psi^9 W \Psi^{-9} = \{1, \iota\}.$$

Computed by conjugating every element of W by Ψ^k and testing linearity;
for k ≠ 9 the cheap necessary test (the conjugate still commutes with ι)
already leaves only the identity. The half-turn's ι is forced: Ψ⁹
commutes with ι (SM-044), and ι is central in W. Consecutive instants of
the machine share no symmetry at all; the eighteen instants are eighteen
copies of W(E₇) in S₅₆ meeting pairwise in the identity (in ⟨ι⟩ at
distance 9), all with one spectrum.

Corollaries checked directly: no reflection of W (0 of 63) is a symmetry
after any tick k = 1..17; none of the 21 involutions of a bridge
PSL(2,7) — the C₂'s of Ilya's descent — is a symmetry at any later
instant short of the full cycle. SM-054 said no marker is *fixed* by the
clock; this says no marker is even a *symmetry* one tick later.

#### 7.8.3 Result 2 (the clock is universal, the mirror is not)

$$\langle W, \Psi \rangle = A_{56}, \qquad \langle W, \mathrm{pr} \rangle = 2^{28} \rtimes \mathrm{Sp}_6(2), \qquad \langle W, \Psi, \mathrm{pr} \rangle = S_{56}.$$

Ψ, ι and the reflections are even permutations of the 56, pr is odd. The
clock with the grammar generates every even permutation of the states:
relative to the symmetry group, the clock is a universal gate — the
permutation-group form of "the Clifford group plus one non-Clifford gate
is universal". The mirror with the grammar generates a group of order
2²⁸·|Sp₆(2)| = 2³⁷·3⁴·5·7, and its structure is explicit: pr fixes
exactly the two poles, which form an antipodal pair; pr composed with
the swap of the poles is a Weyl element (SM-016's altitude ν(pr) = 2,
completed); W is transitive on the 28 antipodal pairs with image Sp₆(2)
and kernel ⟨ι⟩; so the normal closure of the pole swap in ⟨W, pr⟩ is the
full group of 2²⁸ pair-flips, meeting W in ⟨ι⟩, and ⟨W, pr⟩ = (2²⁸)·W.
The mirror is one Pauli-type flip times a Clifford-type element; it
lives in the sign-flip group of the 28 bitangents and cannot leave it.

#### 7.8.4 What it means

- The early resource theory of the machine — structure is free, time is
  expensive; Ψ-depth 2, W-depth 4 (SM-009..014) — is the shadow of a
  dichotomy that is now a theorem on the board: everything linear sits
  in one finite Clifford-type world, the mirror one bit outside it, and
  the clock is the single operation outside that world, universal with
  it, rewriting all of it at every step.
- What the clock preserves of the grammar is exactly what the earlier
  stones measured: the spectrum (Rush–Shi: the orbits and the period of
  a Coxeter element), and a parity's worth of the pairwise relations
  (SM-041: 65 %, by an exact rule). Nothing else: not one non-trivial
  symmetry.
- For the Scar side: a selection rule is a statement about one instant
  of the machine. A choice made in the grammar — a marker, a generation
  axis — does not exist as a symmetry at any other instant. If the clock
  is to carry such a choice, what it carries is not a symmetry but an
  orbit, and the orbit leaves the symmetry group at the first tick.

#### 7.8.5 Not claimed

Nothing about other minuscule boards (E₆'s sheets, D_n, A_n): the same
computation is possible there and is the next stone, with the registered
guess that W ∩ R^k W R^{−k} = C_W(R^k) in general (it fits every number
here, the half-turn included). The isomorphism type of ⟨W, pr⟩ beyond
"the 2²⁸ flips extended by W with ⟨ι⟩ amalgamated" is not claimed.


### 7.9 The shared grammar across the family, and the reversal theorem [C + P, SM-058, SM-059]

#### 7.9.1 Setting

As in §7.8: a minuscule board Wλ with Weyl group W (the grammar),
rowmotion R (the clock), Coxeter number h. For k = 1..h−1 let
I_k = W ∩ R^k W R^{−k} be the symmetry two instants k ticks apart share,
and C_k = C_W(R^k) the centralizer of the k-th power of the clock.
Always C_k ⊆ I_k. On E₇ (SM-057), I_k is trivial except I₉ = {1, ι}.

#### 7.9.2 The shared grammar across the family (SM-058)

Computed for the 42 boards of SM-055 with W enumerated in full.

**The centralizer law.** On every board where no power of R is a Weyl
element — the middle representations ω_k (1 < k < n) of A₄..A₇, the
half-spins of D₆ and D₇, E₆ and E₇ — I_k = C_W(R^k) as sets, for every
k: the symmetry two instants share is exactly the symmetry that commutes
with the time between them. This was registered as a guess for all
boards and INVERTED as a universal law: it fails on the chains (R ∈ W,
so I_k = W while C_W(c^k) is small), on the vector representations of
D_n (the half-turn is a Weyl element by SM-056, and |I_k| follows
gcd(k, n−1): on D₇, 12 / 72 / 384 / |W| for gcd 1 / 2 / 3 / 6, against
centralizers 2 / 12 / 16 / 384), and on one board it did not predict,
the D₅ half-spin.

**The half-turn survivor is the longest element.** On every rich board
with h even exactly one non-trivial symmetry survives the half-turn,
and it is w₀ — not "−1 when −1 ∈ W and nothing otherwise", as the
registered table had it. On D₆'s half-spins four survive (w₀ = −1 among
them), on D₅'s eight.

**The D₅ anomaly [obs].** On the D₅ half-spin (16 weights = the even
sign patterns of five axes, h = 8, R two free 8-cycles): I₃ = I₅ = 2
and I₄ = 8 against centralizers 1 and 4. The extra survivor at lags 3
and 5 is the pure coordinate permutation (e₁ e₃)(e₂ e₅); at the
half-turn the shared grammar is a dihedral group of order 8 containing
the centralizer's Klein four-group {1, −(e₁e₂e₃e₄), (e₂↔e₃, −e₄, −e₅),
their product}, with two signed 4-cycles on e₁, e₄, e₂, e₃. Two
subgroups of order 1,920 in S₁₆ meeting beyond the identity is not
chance. It is not a hidden F₂-linearity either: no power of the D₅
clock is affine on F₂⁴ (checked; the same for D₆, D₇). Open.

#### 7.9.3 The reversal theorem (SM-059)

**Theorem.** On every simply-laced minuscule board the longest element
$w_0$, acting on weights as $-\sigma$ ($\sigma$ the diagram automorphism, trivial when
$-1 \in W$), reverses rowmotion:

$$w_0 R w_0 = R^{-1}.$$

*Proof.* The antipode w ↦ −w reverses the root order on Wλ, and σ
preserves it; so w₀ is an antiautomorphism of the weight lattice, hence
of J(P). Rowmotion sends I to the ideal generated by the minimal
elements of P ∖ I; its inverse sends I to the ideal whose complement is
generated upward by the maximal elements of I. An antiautomorphism
exchanges ideals with filters and minimal with maximal elements, so it
exchanges these two recipes. ∎ (Checked on all 42 boards: w₀ ∈ W,
w₀(top) = bottom, w₀ R w₀ = R^{−1}.)

**Corollary 1.** w₀ commutes with R^k iff R^{2k} = 1; for h even, w₀ is
a half-turn survivor, the one the family always has.

**Corollary 2 (the clock never descends to the shadow).** On a self-dual
board the antipode ι is a permutation of Wλ, and R^k preserves the pair
{w, −w} iff R^{2k} w = w. So the antipodal pairs preserved at lag k
number fix(R^{2k})/2, and R^k induces a map on the shadow Wλ/± only when
R^{2k} = 1. On E₇: 1 pair for k = 1..8 (the axis), all 28 at k = 9 —
SM-044's measured column, re-derived. (Checked on the 12 self-dual
boards.)

#### 7.9.4 The 56-board: two reversals and the mirror (SM-059)

The node-7 coweight splits the 56 into two poles (±3/2) and two
27-sheets (±1/2). Each sheet carries its own clock Ψ₆, rowmotion on the
sheet (order 12, cycle type [12,12,3] per sheet), and its own reversal
w₀(E₆) ∈ W(E₆) ⊂ W(E₇), acting on the sheet's E₆-labels as −σ with σ
the E₆ diagram automorphism (0↔5, 2↔4). Then:

- w₀(E₆) reverses Ψ₆ and does not reverse Ψ; ι = w₀(E₇) = −1 reverses
  both.
- **The reversers are unique** (registered guess, CONFIRMED by full
  enumeration): exactly one element of W(E₇) reverses Ψ, namely ι;
  exactly one element of W(E₆) reverses Ψ₆, namely w₀(E₆).
- **The mirror is the product of the two reversals:**

  $$\mathrm{pr} = \iota \circ w_0(E_6) \circ t, \qquad t = \text{the swap of the two poles},$$

  exactly on all 56 states. Consequences, each previously a separate
  sealed observation: pr∘t = ι∘w₀(E₆) is the Weyl element SM-016 found
  at Hamming distance 2 from the mirror and could not name (a
  fixed-point-free involution of W(E₇)); pr commutes with the sheet
  clock (SM-053's inverted guess AO6a) because both its factors reverse
  it; pr's colour map is the E₆ diagram automorphism (SM-053 AO6b)
  because that is σ; and pr keeps exactly a transposition's 1432 of 1540
  pair types (SM-054's AP7) because it is an isometry times one
  transposition.

#### 7.9.5 What it says

- The three gates of the machine are now named exactly: Ψ is time, the
  one operation outside the symmetry group and universal with it
  (SM-057); ι is the reversal of time, unique, and it is the antipode —
  on this board reversing time is flipping every state's chirality; pr
  is the ratio of the board's reversal to the sheets' reversal, corrected
  at the poles. Time costs; both reversals are free.
- The shadow of the board — the 28 antipodal pairs, the classical
  Clifford world where SM-015 found ι acting trivially — has no clock.
  The clock preserves one pair per tick and needs the sign the shadow
  forgets. The board can reverse time only because it carries that sign.
- Across the family, what two instants share is the symmetry that
  commutes with the time between them, wherever time is genuinely
  non-linear; the longest word always survives the half-turn because it
  is the one Weyl element that runs the clock backwards; and the D₅
  spinor board — the sixteen pure spin-½ patterns, one chirality of
  Spin(10) — is the one board in the family that shares more; the
  mechanism is given in §7.12.2 and the reason in §7.12.4.

#### 7.9.6 Not claimed

No proof of the centralizer law (a computation on 21 boards); no
explanation of the D₅ anomaly; nothing about non-simply-laced boards;
nothing physical — "the 16 of Spin(10)" is named as a representation,
under Rule 3.


### 7.10 The D₅ anomaly on the 4-cube, and homomesy of the three letters [C, SM-060, SM-061]

#### 7.10.1 The D₅ anomaly, located (SM-060)

SM-058 found the one board in the simply-laced minuscule family where
the symmetry two instants share, I_k = W ∩ R^k W R^{−k}, exceeds the
centralizer C_W(R^k) without any power of rowmotion being a Weyl
element: the D₅ half-spin, the sixteen even sign patterns on five axes,
Coxeter number 8, the clock two free 8-cycles; I₃ = I₅ of order 2, I₄ of
order 8, against 1, 1, 4.

**Where it lives.** The B₄ spinor board — all sixteen sign patterns on
four axes, Weyl group the hyperoctahedral group Aut(Q₄) of order 384 —
has the same ten-element poset and, under dropping the fifth
coordinate, the identical rowmotion; W(B₄) sits inside W(D₅). The
half-turn anomaly is already there: |I₄| = 8 against |C₄| = 4, with the
same four extra elements, two signed 4-cycles e₁ → −e₄ → −e₂ → e₃ → e₁
and its inverse, and two involutions pairing (e₁, e₄) with (e₂, e₃).
Only the lag-3 survivor needs the fifth axis: it is the coordinate
permutation (e₁ e₃)(e₂ e₅), and it is the one survivor that mixes the
clock's two orbits; every half-turn survivor preserves them, and so does
w₀ = −(e₁e₂e₃e₄), which reverses the clock.

**What it is not.**
- Not a hidden F₂-linearity: no power of the D₅ (or D₆, D₇) clock is an
  affine map of the even code F₂^{n−1}; D₄'s half-turn is, being the
  linear half-turn of SM-056.
- Not a near-miss of linearity: the altitude of R⁴ against W(D₅) is 8 of
  16, of R³ 7; the correction from the nearest Weyl element moves half
  the board.
- Not the overgroup mechanism. The B₃ spinor shows the same signature
  (shared grammar 16 against centralizer 8 at its half-turn) for a
  visible reason: the B₃ board is the D₄ half-spin, whose half-turn is a
  Weyl element of the larger W(D₄) ⊃ W(B₃). On D₅ nothing of the kind:
  the half-turn generates the whole alternating group A₁₆ together with
  W(D₅). (On D₆'s half-spin, by contrast, ⟨W, R⁵⟩ stays inside the group
  preserving the sixteen antipodal pairs, as Corollary 2 of SM-059
  requires.)
- Not specific to the 4-cube in the naive sense: the B₅ spinor is clean
  (I_k = C_k for every k); the registered guess was inverted only by the
  B₃ case above.

**What it is, so far.** The half-turn's shared grammar on the 4-cube is
a dihedral group of order 8 generated by the centralizer (a Klein
four-group: w₀, and (e₂↔e₃, −e₄, −e₅), and their product) and one
signed 4-cycle; the half-turn acts on it by an automorphism fixing the
Klein subgroup and permuting the four extras among themselves, without
inverting them (the registered guess that it inverts them was wrong).
The anomaly is a statement about sixteen corners of a four-dimensional
cube, a group of order 384, and a clock of order 8 that visits eight
corners and then the other eight. It has resisted four explanations and
is open.

#### 7.10.2 Homomesy of the three letters (SM-061)

A statistic on states is *homomesic* under the clock if its average is
the same on every clock orbit (Propp–Roby 2015). Rush–Wang (2015,
arXiv:1509.08047) proved that on every minuscule poset the order ideal
cardinality and the antichain cardinality are homomesic under
rowmotion, and that the per-colour ideal cardinalities are (file
homomesy). On the weights the latter says that every rowmotion orbit has
mean weight zero; seen on all 42 boards.

**The dictionary.** A state's label at node i is +1 iff its ideal has a
maximal element of colour i, −1 iff the complement has a minimal element
of colour i, 0 otherwise. So #(+1 labels) = |max(I)|, the antichain
cardinality; #(−1 labels) = |min(P ∖ I)| = |max(R(I))|, the antichain
cardinality of the next state; #(0 labels) = rank − both.

**The theorem, read on labels.** On every simply-laced minuscule board
the three ternary counts are homomesic under the clock, with orbit means

$$\#(+1) = \#(-1) = \frac{|P|}{h}, \qquad \#(0) = r - \frac{2|P|}{h},$$

where |P| is the number of join-irreducibles, h the Coxeter number, r
the rank. E₇: 3/2, 3/2, 4. E₆: 4/3, 4/3, 10/3. The D₅ spinor: 5/4, 5/4,
5/2. The equality of the +1 and −1 means is Defant–Hopkins' 0-mesy of
T⁺ − T⁻ (2021, arXiv:2108.13227), which holds on every finite poset.

**One registered guess, confirmed.** The toggle size — the number of
elements of P that change between a state and the next, |I Δ R(I)| —
is homomesic on all 42 boards with mean 2|P|/h. This may follow from
known toggleability results; it is flagged, not claimed as new.

**Literature (Balashov, 2026-09-10): it does follow, in one line.**
Defant–Hopkins–Poznanović–Propp, Theorem 3.20, gives the antichain
cardinality as homomesic with mean |P|/h on every minuscule poset; the
toggle size splits as max(I) ∪ min(P∖I), and |min(P∖I)| = |max(R(I))|, so
toggle size = antichain-card(I) + antichain-card(R(I)), and the closure
properties they state (a homomesic statistic composed with the map, and
sums of homomesic statistics, are homomesic with the evident means) give
2|P|/h. It is presented here as a corollary of their theorem, not as a
finding of ours; the computation on 42 boards is its check.

**Negatives.** On every non-chain board three natural statistics are
NOT homomesic: the number of distinct colours toggled, the per-state
kept count of SM-041 (how many partners a state keeps its pair type
with under one tick), and the number of lattice elements below a state.
On the 56, under the mirror pr the ternary counts are not homomesic (a
state and its image differ), and under the sheet clock Ψ₆ they are
homomesic on the two 27-sheets alone (Rush–Wang on each E₆ sheet; the
two poles are fixed points and break the count if included).

**The reading [I].** With +1 as future, −1 as past and 0 as present:
over every full cycle of the clock the average amounts of future and
past are equal, and the average amount of present is conserved — on
every board, exactly. This is Rush–Wang's antichain theorem in the
board's own three letters. Time does not conserve which node carries
which letter; it conserves, on average, how many of each kind there
are.

#### 7.10.3 Not claimed

No explanation of the anomaly (it is given in §7.12); the toggle-size
homomesy is Defant–Hopkins–Poznanović–Propp's corollary, not a claim of ours; nothing about
non-simply-laced boards beyond B₃, B₄, B₅; nothing physical — "the 16
of Spin(10)" names a representation.


### 7.11 The reverser and the grammar [C + P, SM-062]

#### 7.11.1 What is classical

For a minuscule representation with highest weight λ, the longest
element w₀ of W sends λ to the lowest weight and acts on the weights
as −σ, where σ is the diagram automorphism carrying λ to the highest
weight of the dual representation (trivial exactly when −1 ∈ W: among
the minuscule types, D_n with n even and E₇). Since −1 is central in
GL, conjugation by w₀ acts on W as σ does: w₀ s_i w₀ = s_σ(i). In
particular w₀ is central in W exactly when −1 ∈ W, and then w₀ = −1
is the antipode of the weights. Aut(PSL(2,7)) = PGL(2,7), of order
336, the outer automorphism swapping the two classes of elements of
order 7 and the two three-dimensional representations. PSL(2,7) acts
2-transitively on the projective line over F₇ (eight points), with
PGL(2,7) ⊂ S₈ normalising it and centralising nothing.

#### 7.11.2 What was computed (SM-062)

**(a) The reversers are a coset [P, one line; C on 42 boards].** If g
and g′ both reverse rowmotion then g⁻¹g′ commutes with it; so the set
of Weyl elements reversing R is w₀·C_W(R). Measured: on all 41
enumerated boards the number of reversers equals |C_W(R)|; on the 56,
over all 2,903,040 elements, exactly one reverser (ι) and a trivial
centralizer. With SM-054 (C_{W(E₇)}(Ψ) = 1) the uniqueness of SM-059 is
a corollary. The reverser is unique exactly on the rich boards
(C_W(R) = 1): 22 of the enumerated boards and the 56; there are h
reversers on chains and 2 on the D_n vector boards.

**(b) What the reverser does to the symmetry group [P + C on 42].**
w₀ s_i w₀ = s_σ(i) on every board. The reverser is central, and equals
the antipode, on exactly seven boards of the family — D₄ ω₁/ω₃/ω₄,
D₆ ω₁/ω₅/ω₆, E₇ ω₇ — and on every other board it is non-central and
acts on the grammar by the diagram flip: Λ^k ↔ Λ^{n+1−k} on A_n, the
two half-spins on D_odd, 27 ↔ 27̄ on E₆. On the 56 both are present:
ι fixes all seven simple reflections, while the sheet reversal w₀(E₆)
of SM-059 flips the six E₆ reflections (0↔5, 2↔4) and conjugates the
seventh to a non-simple reflection (registered guess, CONFIRMED).

**(c) The bridge copy's normaliser [C; registered guess CONFIRMED
exactly].** For the bridge PSL(2,7) = P of SM-013/SM-054:
C_{W(E₇)}(P) = ⟨ι⟩ and N_{W(E₇)}(P) has order 672, so N/C ≅ PGL(2,7).
W(E₇) contains every automorphism of P and no further symmetry of it.
The outer coset holds 56 involutions — 28 of cycle type 2²⁴1⁸ on the
56 (the guess from x ↦ 1/x fixing ±1 on the projective line) and 28
fixed-point-free — 112 elements of order 6 and 168 of order 8. N =
⟨ι⟩ × PGL(2,7), with a PGL(2,7) complement inside Sp₆(2) = W⁺ (the
fixed-point-free one) and one outside (SM-023's lemma seen).

**(d) C ≠ T on the grammar [C, forced by SM-054/SM-059 given (c)].**
ι commutes with every element of P. Any c inducing the outer
automorphism is a Weyl element, hence commutes with no power of the
clock and reverses none of them; measured: cΨc⁻¹ agrees with Ψ at four
states and with Ψ⁻¹ at two. Inside the whole normaliser the only
reverser of Ψ is ι and the only element commuting with Ψ is 1.

**(e) What the flavour conjugation has to act on [C, SM-013 cited].**
P acts on the 28 antipodal pairs with fixed points 28/4/1/0/0, whose
character is χ₁ + 2χ₆ + χ₇ + χ₈; the ι-even half of the 56 is this
representation and the ι-odd half is isomorphic to it. No χ₃ or χ̄₃
occurs. The outer automorphism therefore acts on the group P and on no
triplet of states.

**(f) Two observations beyond the brief [obs].** On the five self-dual
boards where −1 ∉ W (A₃ ω₂, A₅ ω₃, A₇ ω₄, D₅ ω₁, D₇ ω₁) the antipode
is a permutation of the weights that reverses the clock and is not a
Weyl element: a non-linear reverser, beside the linear ones. On those
boards the isometry group of the weight configuration is W × ⟨−1⟩, so
the isometry criterion for W-membership overcounts by the antipode;
the sealed stones use the criterion on E₇ alone, where SM-054 makes it
a theorem (checked).

#### 7.11.3 What is identified, and what is read

*Identification (Tier 2):* in the machine's names, ι is the chirality
gate and Ψ the clock (SM-041, SM-044); the antipode w ↦ −w is what
charge conjugation does to the weights of a self-conjugate
representation. So on the 56 the chirality gate is at once the
antipode, the unique linear reversal of the clock, and central in the
grammar: the board's C and its T are one element, and that element is
invisible to every subgroup of W(E₇). On the 27, where the
representation is not self-conjugate, the reverser is instead the
27 ↔ 27̄ flip acting on the grammar. Both are exact.

*Reading (Tier 3, Rule 3):* on the board there is one operation that
conjugates every state and reverses time, and it does nothing to the
flavour group; the operation that conjugates the flavour group — the
outer automorphism of PSL(2,7), which is what the Scar side calls
charge conjugation there — is a different Weyl element, a symmetry of
the board at no later instant (SM-057), with no triplet of states to
act on. Read as a constraint on any board-realised version of the
lepton model: the model must contain an operation trivial on flavour
that reverses a clock. This is a statement about the objects named, not
about physical C, T, or leptons.

#### 7.11.4 Open

Which of the 336 outer elements is "the" conjugation is a choice the
board does not make, as it made no choice of marker pair (SM-054). The
same question on the 27, where the reverser is non-central, is not
computed. Whether the D₅ half-spin's anomaly (SM-058/060) has anything
to do with its board being one of the non-central cases is not known.


### 7.12 The anomaly by hand, and the doubled clock [P + C, SM-063, SM-064]

#### 7.12.1 What is classical

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

#### 7.12.2 What was computed (SM-063, SM-064)

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

#### 7.12.3 What is identified, and what is read

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

#### 7.12.4 Why the orbit without λ [P + C, SM-066]

The question left open above — *why* the half-turn is a Weyl element on the
orbit not containing λ — has a proof, not a search. Grade the spinor weights
by rank (number of minus signs); $W(B_4) = \mathbb{F}_2^4 \rtimes S_4$ acts affinely, $w(x) =
\pi(x) \oplus v$. **Lemma (Weyl rank-shift).** For $w = (\pi,v)$, writing $u = \pi^{-1}(v)$,
$\operatorname{rank}(w(x)) = \operatorname{wt}(\pi(x)\oplus v) = \operatorname{wt}(x\oplus u)$, so the rank-shift is

$$\Delta_w(x) = \operatorname{wt}(u) - 2\,|x \cap u|$$

— a function of the single vector $u$. **Theorem [SM-066].** R⁴ agrees
with no Weyl element on O₁ and with −τ on O₂. On O₁ the half-turn shifts every
rank by exactly ±2 (O₁ is the full-height orbit, its ranks reading 0,1,1,2,2,
3,3,4, and R⁴ pairs positions differing by 2); at λ the shift is +2, forcing
wt(u) = 2, whereupon |Δ| = 2 forces ⟨x,u⟩ = 0 for all x ∈ O₁, and O₁ spans
𝔽₂⁴, so u = 0 — contradiction. On O₂ the shifts are ±1, realised by u = 1110,
i.e. −τ. The cause is λ: the top weight pins wt(u) at rank 0, so only an orbit
avoiding the extreme ranks can carry the half-turn as a symmetry. The argument
is dimension-free (Δ_w(x) = wt(u) − 2|x∩u| in every B_n): on the full-height
orbit of B_n the half-turn shifts rank by ±n/2, so for every n ≥ 4 the
extreme-weight orbit's half-turn is not a Weyl element, the n > 4 case
reducing to the fact that the shift is exactly ±n/2 (verified at B₄ and at B₈,
SM-067).

**B₈: the anomaly does not recur [C, SM-067].** The clock acts freely on the
2ⁿ weights of the B_n spinor board, with orbits of size h = 2n, only when
2n | 2ⁿ, i.e. n a power of 2, so B₈ (256 weights, W of order 10,321,920,
h = 16) is the next board on which the two-orbit mechanism could recur and the
last one in reach. There the clock has sixteen free orbits of sixteen; the
orbit of λ is the full-height orbit, its half-turn shift exactly ±4, so
Lemma BB-B applies; exactly two orbits carry the half-turn as a Weyl element,
both by the same element −(e₂e₃)(e₄e₅)(e₆e₇) (negating e₁..e₇, fixing e₈),
the analogue of −τ, which is also the unique nearest Weyl element to R⁸
(agreement 52 of 256); each is preserved by −1. Lemma B applies, but the
correction c = w⁻¹R⁸ is no longer an involution (cycle type
8⁸ 4¹² 3¹² 2²⁸ 1⁵²) and its Weyl centralizer is {±1}: I₈ = C₈ = {±1}, and
I_k = C_k at every lag on B₈, on the D₉ half-spin (the same clock; W(D₉), of
order 92,897,280, enumerated in full as affine maps x ↦ π(x) ⊕ v on the even
code), and on B₆ and B₇. Among the spinor boards B₃..B₈ the shared grammar
exceeds the centralizer only on B₄ and, by the overgroup W(D₄), on B₃; the
conjecture that it does so exactly when n is a power of 2 is refuted at
n = 8. The two carrying orbits are exactly those whose ranks stay within one
of the middle rank ({3,4,5}; on B₄, O₂'s {1,2,3}), equivalently those on which
every half-turn rank-shift is ±1 — an observation on two boards, not a
theorem [obs]. One orientation slip in the record is corrected in passing:
R(λ) = w₀λ (§7.6, Lemma (a)), so the rank list 0,1,1,2,2,3,3,4 of SM-066 is
read in the direction of R⁻¹; nothing in Theorem BB depends on the direction.
Nothing about B₃₂ or beyond.

**The criterion, and the 16-cube [P + C, SM-068, SM-069].** Why B₄ and not
B₈ is one commutation. For w ∈ W and the correction c = w⁻¹R^m (m = h/2),
c² = 1 iff R^m w R^m = w⁻¹ — for an involution w, iff w commutes with R^m
[P]; and if w commutes with R^m then w, c and R^m pairwise commute, any two of
"g commutes with w / with R^m / with c" imply the third, and the extras of I_m
on Stab_W(Fix c) are exactly C_W(c) ∖ C_W(w) [P] (SM-063's "commute with c but
not with τ" as a lemma). Computed on B₃..B₈: the shared grammar at the
half-turn exceeds the centralizer exactly when the Weyl element nearest to
the half-turn commutes with it — −τ does on B₄; on B₅..B₈ the nearest element,
always of the shape −(e₂e₃)(e₄e₅)…, does not, its correction is not an
involution, and C_W(c) = {±1}; on B₃ no element of W(B₃) agrees with R³ on a
spanning set, so the criterion is a marker only and the B₃ excess is the
overgroup's (§7.10.1). On B₁₆ (65,536 weights, W not enumerated), computed at
the orbit level: the clock is free (2,048 orbits of 32), the orbit of λ shifts
by exactly ±8, **sixteen** orbits carry the half-turn as a Weyl element, all
by the same −(e₂e₃)…(e₁₄e₁₅) with e₁₆ fixed, and they are exactly the orbits
with ranks in {7,8,9} (the band, on three boards: 1, 2, 16 carrying orbits
[obs]); that element does not commute with R¹⁶, C_W(R¹⁶) = {±1}, the
stabilizer of its 1,900-point agreement set is ⟨−1, w⟩ and C_W(c) = {±1}, so
by Lemma B no half-turn survivor beyond ±1 preserves the agreement set;
|I₁₆| itself is not decided. Open, sharpened: why does −(e₂e₃)(e₄e₅)… commute
with the half-turn only at n = 4.

#### 7.12.5 Open

Boards without a W-central reverser (the E₆ 27, the D_odd half-spins, A_n ω_k
with 2k ≠ n + 1): Lemma C does not apply and nothing is claimed. Whether
C_W(R^{2k}) ⊆ I_k beyond the vectors: it is strict on A₅ω₃, A₇ω₄ and the D₆
half-spins at the half-turn. Which group the vectors' outer transports are
inner in, if any short of Sym(2n).


### 7.13 The clock's Clifford hierarchy [P + C, SM-065]

#### 7.13.1 What is classical

In quantum computation the Clifford hierarchy (Gottesman–Chuang 1999)
is the chain of sets C₁ = the Pauli group, C_{j+1} = {U : UC₁U⁻¹ ⊆ C_j};
C₂ is the Clifford group and the T-gate lies in C₃ ∖ C₂: it is not a
Clifford gate, but it sends every Pauli into the Clifford group. In
group theory, for a subgroup H ≤ G and an element x ∈ G, the largest
subgroup of H normalised by x is the intersection of the conjugates of
H under ⟨x⟩, and the core of H in G is the intersection over all of G.

#### 7.13.2 What was computed (SM-065)

**The definition.** For a board (W, R) and a lag k, the hierarchy at lag
k is the chain P₁(k) = W, P_{j+1}(k) = {g ∈ P_j : R^{−k}gR^k ∈ P_j}; so
P₂ = I_k, the grammar two instants share (§7.9), is the set of Weyl
elements the clock sends back into W — the shape of a hierarchy level
with W in the Clifford role. The depth d(k) is the first j with
P_{j+1} = P_j; the core P_∞(k) is where the chain stops.

**Lemma F [P].**

$$P_j(k) = \bigcap_{i<j} R^{ik}\, W\, R^{-ik}:$$

the grammar shared by $j$ consecutive instants at stride $k$. Hence the core is the largest subgroup
of W normalised by R^k, and contains the core of W in ⟨W, R^k⟩.

**Lemma G [P].** P₃(k) = P₂(k) if and only if I_k = I_{−k}, if and only
if a reverser of the clock in W (§7.9: w₀ is one, and they form the
coset w₀·C_W(R)) normalises I_k — because conjugating I_k by R^k and by
any reverser both give I_{−k}.

**The table [C, 44 boards, 278 (board, lag) pairs].** Both lemmas were
checked on every pair. Depth 1 exactly where I_k = W (the chains, and
the D_n vectors at the half-turn). Depth 2 everywhere else — two
instants already share what all instants share — **with exactly one
exception, the D₅ half-spin at lags 3 and 5,** where the survivor of
§7.9 is carried by the clock to a different element (§7.12), no
reverser normalises I₃, and the chain drops once more: 1920 ⊃ 2 ⊃ 1.
The cores: C_W(R^k) on the rich boards (trivial, or ±1 at the half-turn
where −1 ∈ W); C_W(R^{2k}) on the D_n vectors (§7.12); the dihedral I₄
of order 8 on the 4-cube and the D₅ half-spins at the half-turn; on the
56, from SM-057 without re-running, trivial at every lag but the
half-turn, where it is {1, ι}. Every one of these was a registered
guess, including the exception; all held.

**Normality [C].** Wherever the core is neither W nor of order ≤ 2 (44
cases) it is not a normal subgroup of W. Where ⟨W, R⟩ could be
enumerated (the D₃ vector, the D₄ vector, the B₃ spinor: A₆, A₈, A₈ of
orders 360, 20,160, 20,160) the core of W in ⟨W, R⟩ is trivial, strictly
below P_∞(1) (orders 4, 6, 1).

#### 7.13.3 What is identified, and what is read

Identified (mathematics): the run of shared grammars along the clock is
short. On every board but one, what two instants share is what all
instants share; the exception is the one survivor that time reversal
does not preserve. The largest part of the symmetry group that the
clock carries along unchanged is, on the rich boards and on the 56,
nothing (or the antipode alone).

Read [I], marked: if the clock is the T-gate of the analogy and W its
Clifford group, then the Pauli group is the core, and on the 56 there
is none. The clock is beyond every level of the hierarchy relative to
W(E₇): no subgroup of W(E₇), and in particular no copy of PSL(2,7), is
preserved by Ψ. On the vectors and the 4-cube the analogy holds for
exactly one level — the clock maps a Pauli-like group into W by an
automorphism, outer when n is odd (§7.12) — and W is not that group's
Clifford group in any stronger sense, since it does not normalise it.
SM-057's sentence, a Clifford-like W with one non-Clifford Ψ, is exact
in this sense and in no other.

#### 7.13.4 Open

⟨W, R⟩ on the boards where it could not be enumerated (it is A₁₆ on the
D₅ half-spin by SM-060 and A₅₆ on the 56 by SM-057; the pattern
"alternating" is an observation on five boards, not a claim). A
hierarchy in the other direction, grading the powers of the clock
against a fixed subgroup of W, is not defined here. Nothing about the
clock as a gate on a Hilbert space.


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

## 11. The other tower: PSL(2,7), the 28 bitangents, and the bridge into Sp₆(2) [P/C, SM-001, SM-003, SM-013, SM-015, SM-021–024]

Section 3 placed two towers inside W⁺(E₈); §§4–10 developed the Stenberg-side
machine on that frame. This section collects the Balashov-side tower — the
PSL(2,7) framework — and the classical geometry in which the two frameworks
meet: the 28 bitangents of a genus-3 curve, inside Sp₆(𝔽₂) ≅ W(E₇)/{±1}. It
is a collation, on the Stenberg side, of the bridge results already sealed in
the joint registry (SM-001, SM-003, SM-013, SM-015, SM-021, SM-022,
SM-024/028) and of the standalone note *The Bitangent Bridge* (SM-008),
independently re-verified by the second author (§11.8), with his own
contribution as §11.9.

### 11.1 The PSL(2,7) framework [P/C, SM-001]

PSL(2,7) ≅ GL(3,𝔽₂), order 168, with six conjugacy classes 1A, 2A, 3A, 4A,
7A, 7B of sizes 1, 21, 56, 42, 24, 24. Its character table, derived from
scratch by the Burnside–Dixon class-algebra method and verified exactly over
ℚ(√−7) (`verify_tsc_scarcat.py`, 48 checks; 35+ rows of the second author's
registry independently confirmed):

| | 1A | 2A | 3A | 4A | 7A | 7B |
|---|---|---|---|---|---|---|
| χ₁ | 1 | 1 | 1 | 1 | 1 | 1 |
| χ₃ | 3 | −1 | 0 | 1 | α | ᾱ |
| χ̄₃ | 3 | −1 | 0 | 1 | ᾱ | α |
| χ₆ | 6 | 2 | 0 | 0 | −1 | −1 |
| χ₇ | 7 | −1 | 1 | −1 | 0 | 0 |
| χ₈ | 8 | 0 | −1 | 0 | 1 | 1 |

with $\alpha = (-1+\sqrt{-7})/2$. The Balashov-side tower is the odd spine PSL(2,7) ⊃ A₅ ⊃
A₄ ⊃ C₂ with Schur covers SL(2,7), 2·I = SL(2,5), 2·T = SL(2,3) (each a
non-split central ℤ₂-extension) and the split covers Ih = A₅×ℤ₂, Th = A₄×ℤ₂,
GL(2,3) = 2·S₄; it is closed at the top by W(E₆) < Sp₆(2) at index 28
(SM-021, `verify_tower_b.py`, 22 checks) — the second of the two towers §3
hangs over the single central C₂.

### 11.2 No meeting at E₆; the field-level shadow [P/C, SM-003]

Because 7 ∤ |W(E₆)| = 51840 and 168/27 ∉ ℤ, PSL(2,7) embeds in no
W(E₆)-geometry and has no transitive action on 27: the two frameworks cannot
meet at the 27. At field level, Gal(ℚ(ζ₂₁)/ℚ) ≅ C₆ × C₂ has quadratic
subfields ℚ(√−3), ℚ(√−7), ℚ(√21) (Gauss sums g₃² = −3, g₇² = −7,
(g₃g₇)² = +21); ℚ(√−7) is the character field of PSL(2,7) — the unique
irrationality in the table, and the CM field of the Klein quartic — while
ℚ(√−3) is the Eisenstein field of the E₆ side. The two are linearly disjoint:
at field level the frameworks meet only in ℚ (`verify_tbr_bridge.py`).

### 11.3 The bitangent home [C, SM-003]

Realize $\mathrm{PSL}(2,7) = \mathrm{GL}(3,\mathbb{F}_2)$ on $V \oplus V^* \cong \mathbb{F}_2^6$ with the symplectic form

$$\omega\big((v,f),(w,h)\big) = f(w) + h(v).$$

 The 64 quadratic refinements of ω split by Arf
invariant into 36 even and 28 odd. Computed in `verify_tbr_bridge.py`
(20 checks):

- PSL(2,7) fixes exactly one even refinement; its orbits on the 36 even
  refinements are **[1, 7, 7, 21]** — the fixed form, the Fano points, the
  Fano planes, the flags [obs]. The stabilizer of an even form in Sp₆(2) is
  O₆⁺(2) ≅ S₈ (order 8! = 40,320), and PSL(2,7) sits inside it by its
  8-point action on P¹(𝔽₇).
- PSL(2,7) is transitive on the 28 odd refinements (the bitangents), with
  stabilizer S₃ = N(⟨z₃⟩) and permutation character χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈. The
  stabilizer of an odd form in Sp₆(2) is O₆⁻(2) ≅ W(E₆), order 51,840.

### 11.4 The bridge [C + P, SM-003, SM-024/028]

Inside Sp₆(2) ≅ W(E₇)/{±1}: **W(E₆) is the stabilizer of one bitangent,
PSL(2,7) is transitive on all 28, and PSL(2,7) ∩ Stab(bitangent) = S₃ =
N(⟨z₃⟩).** This S₃ is at once (i) the "universal stabilizer" of the Scar-Cat
registry (28 = 168/6), (ii) the canonical stabilizer of the strata
decomposition 168 = 31 + 62 + 75, and (iii) the type group S₃ of the E₆
architecture's typed algebra — the two frameworks are the two point-of-view
subgroups of one bitangent configuration, and the bridge closes the second
author's open "Bridge" conjecture. The embedding is canonical up to a single
outer flip: C_{Sp₆(2)}(PSL(2,7)) = 1 and N_{Sp₆(2)}(PSL(2,7)) = PGL(2,7) at
index 2, the outer automorphism realized as the symplectic duality X ↔ X*
(SM-024 by an exhaustive 1,451,520-element pass; SM-028 by the second
author's structural route — two engines, one answer).

### 11.5 The bridge lands on the board [C, SM-003, SM-013]

The map z ↦ N(⟨z⟩) is exactly 2-to-1 from the 56 elements of class 3A onto
the 28 bitangent stabilizers — the group-internal incarnation of the ±-doubling
by which the 28 bitangents index the 56 weights of the E₇ minuscule
representation. This is the same 56 the clock runs on (§§6, 7.1): PSL(2,7)
acts on it with orbits **[28, 28]**, the two bitangent sheets interchanged by
the antipode ι, weight-stabilizer S₃ (SM-013, answering design question DQ-1;
the registered single-orbit guess refuted). The Weyl-level content is
ℂ⁵⁶ = 2(χ₁ ⊕ 2χ₆ ⊕ χ₇ ⊕ χ₈), the untwisted lift unique because PSL(2,7) is
perfect; the quark sectors χ₃/χ̄₃ do not occur in the Weyl action, only in the
Lie-group embeddings of §11.6.

### 11.6 Branchings of the 27 [C, SM-003]

Two canonical restrictions of the 27 follow from the two embeddings:
trinification E₆ ⊃ SU(3)³ with PSL(2,7) diagonal by Klein's χ₃ gives
**27| = 3χ₁ ⊕ 3χ₈**; and PSL(2,7) ⊂ G₂ = Aut(𝕆) with 27 = J₃(𝕆) gives
**27| = 6χ₁ ⊕ 3χ₇**. The earlier conjecture "27 ↔ 2χ₈" is impossible, as
dimension 16 appears in no restriction of the 27.

### 11.7 The Clifford reading and the chiral Fano pair [C + obs, SM-015]

The bridge transports into quantum terms. Sp₆(2) = W(E₇)/± is the 3-qubit
Clifford group modulo phases and Paulis, exhibited computationally from both
sides in shared coordinates (`verify_stoneq_clifford.py`, 35 checks): the 28
bitangents are the 28 odd Pauli sign-functions, W(E₆) the Clifford stabilizer
of one, and PSL(2,7) a Clifford subgroup transitive on all 28, its fingerprint
[28] / [1,7,7,21] / S₃ landing intact. The clock Ψ has **no** Clifford shadow
(ιΨι = Ψ⁻¹ against central ι; it does not act on the 28 pairs) — the
group-theoretic face of the non-linearity of §7.6. Separately, on the E₆
architecture's 7-channel syndrome, exactly 2 of the 30 Fano structures on 7
labels are invariant under the syndrome's motion group S₃ — a chiral pair,
"one bit" (a chirality convention) from a full Fano labelling, compatible but
never forced [obs] (`verify_fano_syndrome.py`). The v1 "two counter-posed 27s"
intuition, refuted as a description of the E₆ crystal, is true one floor up as
the E₆-branching 27 ⊕ 27̄ ⊕ 1 ⊕ 1 of the 56, with the mirror gate pr the
diagram automorphism (§10).

### 11.8 What is the second author's, what is classical, what is joint

The skeleton — bitangents, theta characteristics, O₆± ≅ W(E₆) / S₈,
Sp₆(2) ≅ W(E₇)/± — is classical. The PSL(2,7) framework, its
representation-ring selection rules, and the registry under audit are the
second author's; SM-001 records that audit (35+ rows independently confirmed,
his own predictions audit credited). What the joint work adds is the
identification — that two independently built frameworks each singled out, for
internal reasons, the *same* S₃ at the same place in this classical geometry —
together with the [obs] items (the even-orbit structure [1,7,7,21], the chiral
Fano pair, the resurrection reading of §11.7) and audit-grade reproducibility.
This section is a Stenberg-side collation of the joint record; the second
author's independent re-verification of §11.3 (2026-09-14, the 36/28 split,
[1,7,7,21], the single 28-orbit and the χ₁+2χ₆+χ₇+χ₈ character, rebuilt from
scratch) and his own expansion (§11.9) are merged, and the bibliography is
completed.

### 11.9 The sextet χ₆ as the Fano plane's deleted permutation module [P + C, second author]

The second author contributes an explicit geometric model of the
6-dimensional irreducible χ₆: it is the **deleted permutation module on the
7 points of the Fano plane** (7 = 1 ⊕ 6, the singlet the overall labelling).
Realizing PSL(2,7) = GL(3,𝔽₂) on the 7 nonzero vectors of 𝔽₂³, the generators
A (order 2), B (order 3), AB (order 7) have traces 2, 0, −1 on the 6-dimensional
sum-zero subspace — exactly χ₆'s character at the classes 2A, 3A, 7A/7B — which
by character theory is a complete proof that this module is χ₆. The same fact
is stated, independently, in Luhn–Nasri–Ramond (2007, §7). His construction was
re-run on the Stenberg side, reproducing the trace match exactly.

**This is the same Fano plane as §11.3.** The two size-7 orbits of PSL(2,7) on
the 36 even refinements — the "Fano points" and "Fano planes" of §11.3 — both
carry permutation character 1 ⊕ χ₆ (verified: the fixed-point counts (7,3,1,1,
0,0) over the six classes agree with the point action's on the nose), so each
is a 7-element PSL(2,7)-set realizing χ₆ as its deleted permutation module: the
points and the lines of the one Fano plane, dual under the diagram
automorphism. The second author's χ₆-model is thus the "Fano points" orbit of
§11.3 exactly, and the "Fano planes" orbit is its dual — resolving the question
of whether these are the same object or a look-alike in favour of the same.

He further builds the six independent quartic invariants of χ₆ from the Fano
combinatorics (the 7 points, the 7 lines, and an antisymmetric pairing), rank 6
by an explicit computation — a representation-theoretic count. Their use in the
King–Luhn flavon-potential and vacuum-alignment programme is a physical
identification and is **not** taken up here (Rule 3).

## 12. Discussion

We collect here what the parts establish together. Nothing in this section
is a new claim; each sentence points back to a graded result above.

**One frame holds two machines.** The organizing fact of §§3–6 is that a
single classical group, the rotation subgroup W⁺(E₈), was found to contain
two towers built independently and for unrelated reasons — a chain inside
PSL(2,7) on the Balashov side, a tower of Schur covers on the Stenberg
side — over one central C₂ [C, SM-030]. Everything downstream lives on that
frame in one coordinate system: the quotient O₈⁺(2), the triality Φ realized
as an explicit order-3 permutation of the 360 points (§5), the still point
G₂(2) recovered as an exact intersection with PSL(2,7) sitting inside it as
the bitangent class (§4), and the fourteen outer classes of O₈⁺(2).3
enumerated and matched name-for-name to the published table before any
character value was read (§§8–9). The value of the construction is not that
these objects are new — they are not, and §14 says so — but that they are
built, not asserted, each from the last, and re-executed independently by
the second author (§15).

**The clock on that frame is rowmotion.** The 56-state machine, built by
other means on the Stenberg side, has its states identified with the vector
block of the roof — the 56 weights of the minuscule representation of E₇ —
and its clock Ψ shown to be exactly rowmotion on the 27-element E₇ minuscule
poset in the standard convention [C, SM-041]. That this rowmotion has order
18 with orbit structure [18, 18, 18, 2] is the Coxeter number and
Coxeter-element cycle type, and is Rush–Shi's theorem, not ours (§7.1). What
is ours is the identification of a machine with that rowmotion, and the
mirror gate pr with the E₆ diagram automorphism (§10), after which the two
gates and the clock generate the full symmetric group on the 56 states.

**The group and the clock share little, and exactly how little is the
theorem.** The question of §§7.8–7.13 — what a Weyl group shares with the
translates of itself by its own clock — has a sharp answer: the intersection
of W(E₇) with the centralizer of a clock power is the centralizer and
nothing more, meeting W(E₇) itself in the identity alone [C, SM-054]; the
longest element reverses the clock [C + P, SM-059]; three label counts and
the toggle size are homomesic, the last as a corollary of
Defant–Hopkins–Poznanović–Propp [C, SM-060/061]; the one anomaly in the
family carries a mechanism rather than an exception (on the 4-cube the
half-turn is a Weyl element on one orbit, §7.12); and the Clifford-hierarchy
analogy for the clock holds for exactly one level and no further [P + C,
SM-065]. Read together with the non-linearity theorems (§§7.6–7.7) — that
rowmotion is a Weyl element exactly on chains, its half-turn exactly on the
D_n vectors, with the defect in closed form on two families and tabulated
for 42 cases — the picture is consistent: the E₇ clock is as far from being
a symmetry of the board as it can be, and fails every linearity condition at
the first place it can (§7.6). The parity rule (§7.2) is the local face of
the same fact: a single tick preserves an inner-product sign iff a toggle-set
parity is even, exactly, on all 1,485 pairs.

**Method.** Two disciplines carried the work and are worth stating as
findings in their own right. Every unit was sealed under a brief whose
SHA-256 was fixed before its script existed, so that each identification in
§§9–10 is made against numbers the model produced before the reference table
was consulted; and every registered expectation that failed is reported at
the same prominence as those that held (§13), including the
second author's and our own — nineteen inversions and one lemma reported
false as stated (§7.12) across the run. The model's credibility rests on
those two rules more than on any single tally.

**Outlook.** Several directions are open and are named here as future work,
not as gaps in the present claims. The non-simply-laced minuscule weights
(B_n ω_n, C_n ω₁), promotion, and birational rowmotion (Okada 2021) are
untouched here; a closed form for the defect κ on the spinors, on E₆ and E₇,
and on A_n ω_k for k ≥ 3 beyond the observed degree at k = 3 is not known to
us; and the "not found" status of §§7.2, 7.6, 7.7 (§7.4, Appendix B) is
exactly that: a specialist reader with MathSciNet access may know these as
corollaries, and the reference would be welcome. Whether
the coincidence of the number 18 between the board's Coxeter number and the
roof's twisted classes (§§5, 8) is more than a coincidence is left as it was
found — two different objects (§7.1) — and any reading of the clock beyond
combinatorics remains marked [I] and unclaimed (§14).

## 13. Refutations, at equal prominence

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

In the nine units of §§7.8–7.13: SM-058's guess that the shared grammar
is the centralizer on every board (inverted on the chains, the D_n vectors
and the D₅ half-spin — the last explained in §7.12, the vectors made a
theorem there) and its predicted table; SM-060's guesses that the anomaly
is specific to the 4-cube (inverted on B₃) and that the half-turn inverts
the extras; SM-061's guess about the mirror and the sheet clock; SM-063's
guess that a single Weyl element realises the transport on every
anomalous pair (inverted on 15 of 98) and its Lemma A, stated as proved
and false as stated (§7.12.2(c)); SM-064's guess on where the even-n
realising pair lies; and five slips of the executor's own (SM-060 twice,
SM-062 once, SM-063 twice), each reported in its row. SM-057, SM-059 and
SM-065 had every registered guess confirmed.

In SM-067 (§7.12.4, B₈): the guesses that the half-turn anomaly recurs on the
8-cube (|I₈| > |C₈|, ratio 2) and that it marks the boards with a free clock
(inverted: I_k = C_k at every lag on B₈, the D₉ half-spin, B₆ and B₇), that
−1 exchanges the two carrying orbits (it fixes each), and that D₉ carries a
survivor at a lag coprime to 16 (none); two scoring slips of the executor's
own (the rank list read against the clock's direction; a containment bar that
demanded extras which do not exist), both kept in the first-run log. In
SM-068 (the criterion): that the agreement set on B₈ has no Weyl symmetry
beyond ±1 (it has ⟨−1, w⟩), that the criterion explains B₃ from inside W(B₃)
(no spanning agreement set exists there), and that the nearest element is
unique only up to the antipode (it is unique outright). In SM-069 (the
16-cube): that two orbits carry the half-turn (sixteen do, −1 swapping four
pairs of them) and that every orbit spans (61 do not); one instrumentation
error in the centralizer search, fixed and cross-checked, in the first-run
log.

## 14. What is not claimed

No physical identification of any object here. No claim that the
Coxeter-number periodicity, the fixed group of triality, the outer
classes of O₈⁺(2).3, or the action of the E₆ diagram automorphism on
minuscule posets are new. No claim of novelty for §§7.2, 7.6, 7.7 beyond
"not found" (§7.4, Appendix B). No claim that the
roof is minimal beyond minimal-found. Nothing about the non-simply-laced
minuscule weights (B_n ω_n, C_n ω₁), about non-minuscule posets,
promotion, or birational rowmotion. No formula for κ on the spinors, on
E₆, E₇, or on A_n ω_k with k ≥ 3 beyond the observed polynomial degree at
k = 3.

No claim of novelty for §§7.8–7.13 beyond "not found" (§7.4,
Appendix B); the toggle-size homomesy of §7.10 is Defant–Hopkins–Poznanović–
Propp's, not ours. "Clifford", "Pauli" and "T-gate" in §7.13 are labels
for a chain of subgroups; no gate on any Hilbert space is claimed. Stone
AY's Lemma A (§7.12) is false as stated and is used nowhere. Nothing
physical: no lepton, no flavour model, and no reading of the clock as time
beyond the paragraphs marked [I].

## 15. Reproducibility

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
| SM-057 | `verify_stone_as_shared_grammar.py` | SM-054's verifier file and cache `_stone_ap_cache/witnesses_ap.json`, `scar56_data.json` |
| SM-058 | `verify_stone_at_grammar_family.py` | the AQ verifier file (machine loaded verbatim) |
| SM-059 | `verify_stone_au_two_reversals.py` | SM-055's and SM-054's verifier files, `scar56_data.json` |
| SM-060 | `verify_stone_av_d5_anomaly.py` | none (boards built in e-coordinates) |
| SM-061 | `verify_stone_aw_homomesy.py` | the AQ verifier file |
| SM-062 | `verify_stone_ax_c_equals_t.py` | the AQ, AT, AP, AS and AU verifier files, `scar56_data.json`, `_stone_ap_cache/witnesses_ap.json` |
| SM-063 | `verify_stone_ay_d5_by_hand.py` | the AV, AQ and AT verifier files, `_stone_at_cache/table_at.json` |
| SM-064 | `verify_stone_az_doubled_clock.py` | the AV, AQ and AT verifier files, `_stone_at_cache/table_at.json` |
| SM-065 | `verify_stone_ba_clifford_hierarchy.py` | the AQ, AT and AV verifier files |

The `kbar_*` files of Stone U (~180 MB) are excluded from every envelope
and are regenerated by that stone's verifier.

## References

- Bourbaki, N. *Lie Groups and Lie Algebras, Chapters 4–6.* Springer, 2002.
- Breuer, T. *The GAP Character Table Library*, Version 1.3.11. RWTH Aachen. (Tables "O8+(2)" and "O8+(2).3", file `ctoorth2.tbl`.)
- Cameron, P. J.; Fon-der-Flaass, D. G. Orbits of antichains revisited. *European J. Combin.* 16 (1995) 545–554.
- Cohen, A. M.; Wales, D. B. Finite subgroups of G₂(ℂ). *Comm. Algebra* 11 (1983) 441–459.
- Conway, J. H. Three lectures on exceptional groups. In *Finite Simple Groups* (Oxford, 1969), Academic Press, 1971, 215–247. Reprinted in Conway–Sloane (1999), ch. 10.
- Conway, J. H.; Curtis, R. T.; Norton, S. P.; Parker, R. A.; Wilson, R. A. *ATLAS of Finite Groups.* Oxford University Press, 1985.
- Conway, J. H.; Sloane, N. J. A. *Sphere Packings, Lattices and Groups*, 3rd ed. Springer, 1999.
- Defant, C.; Hopkins, S.; Poznanović, S.; Propp, J. Homomesy via toggleability statistics. *Algebraic Combinatorics*; arXiv:2108.13227 (2021).
- Dolgachev, I. *Classical Algebraic Geometry: A Modern View.* Cambridge University Press, 2012.
- Elkies, N. D. The Klein quartic in number theory. In *The Eightfold Way: The Beauty of Klein's Quartic Curve* (S. Levy, ed.), MSRI Publications 35, Cambridge University Press, 1999, 51–101.
- Gottesman, D.; Chuang, I. L. Demonstrating the viability of universal quantum computation using teleportation and single-qubit operations. *Nature* 402 (1999) 390–393.
- Green, R. M. *Combinatorics of Minuscule Representations.* Cambridge Tracts in Mathematics 199, Cambridge University Press, 2013.
- Garver, A.; Patrias, R.; Thomas, H. Minuscule reverse plane partitions via quiver representations. *Selecta Math.* 29 (2023), 37.
- Green, R. M.; Xu, T. Branching rules of minuscule representations via a new partial order. arXiv:2402.06732 (2024), to appear in *Combinatorial Theory*.
- Hopkins, S. Order polynomial product formulas and poset dynamics. arXiv:2006.01568 (2020); in *Open Problems in Algebraic Combinatorics*, Proc. Sympos. Pure Math. 110, AMS, 2024.
- Kleidman, P. B. The maximal subgroups of the finite 8-dimensional orthogonal groups PΩ₈⁺(q) and of their automorphism groups. *J. Algebra* 110 (1987) 173–242.
- King, S. F.; Luhn, C. A new family symmetry for SO(10) GUTs. arXiv:0905.1686 (2009).
- King, S. F.; Luhn, C. A supersymmetric grand unified theory of flavour with PSL₂(7)×SO(10). *Nucl. Phys.* B832 (2010) 414–453; arXiv:0912.1344.
- Klein, F. Über die Transformation siebenter Ordnung der elliptischen Functionen. *Math. Ann.* 14 (1878) 428–471.
- Levy, S. (ed.). *The Eightfold Way: The Beauty of Klein's Quartic Curve.* MSRI Publications 35, Cambridge University Press, 1999.
- Luhn, C.; Nasri, S.; Ramond, P. Simple finite non-abelian flavor groups. *J. Math. Phys.* 48 (2007) 123519; arXiv:0709.1447. (§7: the Fano-plane representation is 1 ⊕ 6.)
- Marczinzik, R.; Thomas, H.; Yıldırım, E. On the interaction of the Coxeter transformation and the rowmotion bijection. *J. Comb. Algebra* 8 (2024) 359–374. doi:10.4171/JCA/101.
- Okada, S. Birational rowmotion and Coxeter-motion on minuscule posets. *Electron. J. Combin.* 28(1) (2021) P1.17; arXiv:2004.05364.
- Panyushev, D. I. Weight posets associated with gradings of simple Lie algebras, Weyl groups, and arrangements of hyperplanes. *J. Algebraic Combin.* 44 (2016) 325–351; arXiv:1412.0987.
- Pechenik, O. Minuscule analogues of the plane partition periodicity conjecture of Cameron and Fon-Der-Flaass. arXiv:2107.02679 (2021).
- Proctor, R. A. Bruhat lattices, plane partition generating functions, and minuscule representations. *European J. Combin.* 5 (1984) 331–350.
- Propp, J.; Roby, T. Homomesy in products of two chains. *Electron. J. Combin.* 22 (2015) P3.4.
- Reiner, V.; Stanton, D.; White, D. The cyclic sieving phenomenon. *J. Combin. Theory Ser. A* 108 (2004) 17–50.
- Rush, D. B.; Shi, X. On orbits of order ideals of minuscule posets. *J. Algebraic Combin.* 37 (2013) 545–569. doi:10.1007/s10801-012-0380-2.
- Rush, D. B.; Wang, K. On orbits of order ideals of minuscule posets II: Homomesy. arXiv:1509.08047 (2015).
- Stanley, R. P. Promotion and evacuation. *Electron. J. Combin.* 16(2) (2009) R9.
- Stembridge, J. R. On minuscule representations, plane partitions and involutions in complex Lie groups. *Duke Math. J.* 73 (1994) 469–490.
- Stembridge, J. R. Minuscule elements of Weyl groups. *J. Algebra* 235 (2001) 722–743.
- Striker, J.; Williams, N. Promotion and rowmotion. *European J. Combin.* 33 (2012) 1919–1942.
- Thomas, H.; Williams, N. Rowmotion in slow motion. *Proc. London Math. Soc.* 119 (2019) 1149–1178; arXiv:1712.10123.
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

Added in v0.2 (§§7.6–7.7): SM-055 (Stone AQ, 8 + 2 inverted, 2026-09-09) and
SM-056 (Stone AR, 10/10, 2026-09-09) — JOINT on the second author's word of
2026-09-10 (re-run and accepted on his side). Related: SM-054 (Stone AP,
22 + 2 disclosed, 2026-09-07) — the centralizer of Ψ in S₅₆ meets W(E₇) in
the identity alone — JOINT on his word of 2026-09-10, together with
SM-035, SM-036 and SM-037 of the earlier lane.

Added in v0.3 (§§7.8–7.13), **JOINT on the second author's word of 2026-09-14**
(he read all of §§7.8–7.13 and accepted each): SM-057 (Stone AS, 14/14),
SM-058 (Stone AT, 7 + 4 inverted or corrected), SM-059 (Stone AU, 10/10),
SM-060 (Stone AV, 9 + 4), SM-061 (Stone AW, 6 + 1), SM-062 (Stone AX, 21 + 1),
SM-063 (Stone AY, 20 + 5, including its own Lemma A reported false), SM-064
(Stone AZ, 11 + 2); SM-065 (Stone BA, 7/7, 2026-09-11) — JOINT on his word
of 2026-09-14.

Added in v0.6 (§7.12.4): SM-066 (Stone BB, 6/6, 2026-09-13) — the half-turn on
the full-height orbit, closing SM-063 §7.12.4 open #1 by the Weyl rank-shift
lemma — JOINT on the second author's word of 2026-09-14 (Lemma BB-A rebuilt
from scratch on his side: W(B₄) = 𝔽₂⁴ ⋊ S₄ of order 384, the rank identity on
200 random triples, the contradiction by hand).

Added in v0.8 (§11.9): the second author's model of χ₆ as the Fano plane's
deleted permutation module, his construction re-run on the Stenberg side; the
identity with §11.3's size-7 orbits verified (`verify_fano_bitangent_identity.py`).
All thirty-six units cited above are JOINT as of 2026-09-14.

Added 2026-09-19 (§7.12.4, the B₈ paragraphs): SM-067 (Stone BC, 14 + 4
inverted), SM-068 (Stone BD, 7 + 3), SM-069 (Stone BE, 9 + 2) — the 8-cube,
the criterion and the 16-cube, prepared on the Stenberg side under briefs
locked before code; the second author's re-execution is invited. They are the
three units cited in this paper that are not yet JOINT.

## Appendix B. The literature search behind "not found"

The claim of §7.4 is negative and is therefore only as good as the search
behind it. This appendix records the search so that a reader can judge it
or extend it.

**The question.** Is it stated or proved anywhere that rowmotion on a
minuscule poset, carried to the weights by the natural bijection, is or is
not itself an element of the Weyl group; for which minuscule posets it or
its half-turn is; that a pair of weights keeps its inner product under one
step of rowmotion according to a parity of toggle data; or what fraction of
pairs it keeps?

**Searches 1–3 (September 2026, both sides; keyword).** Toggle groups,
periodicity, homomesy, cyclic sieving; rowmotion and an ambient
inner-product sign on minuscule weights; rowmotion with quadratic or
bilinear forms mod 2; the E₇ 56-ideal case and the Gosset graph. Found:
the Coxeter-motion and birational literature (Okada 2021), the toggle
literature (Striker–Williams 2012; Striker 2016), the homomesy literature
(Propp–Roby 2015; Rush–Wang 2015; Defant–Hopkins–Poznanović–Propp 2021).
No match.

**Search 4 (Balashov, 2026-09-10; citation trail).** The thirty documents
citing Rush–Shi (2013) on zbMATH Open, all read. No match; the two nearest
(Marczinzik–Thomas–Yıldırım 2024; Panyushev 2016) are discussed in §7.4.

**Search 5 (Stenberg side, 2026-09-19; corpus).** The arXiv API query
`all:rowmotion` (title, abstract and full-text index), 200 results
requested, returned the complete corpus of **57 documents** (2014–2026).
Every title and abstract was read. Titles containing *minuscule*:
Hopkins 2016 (CDE property for minuscule lattices), Hopkins 2019
(minuscule doppelgängers), Okada 2020 (birational rowmotion and
Coxeter-motion), Pechenik 2021 (minuscule analogues of the
Cameron–Fon-Der-Flaass conjecture). Titles containing *Coxeter*: Okada
2020, Marczinzik–Thomas–Yıldırım 2022. Titles containing *Weyl*,
*isometry*, *orthogonal*, *inner product* or *E₇*: none. The remaining
titles concern Tamari and Cambrian lattices, fences, root posets and
rowvacuation, interval-closed sets, products of chains, birational and
piecewise-linear lifts, Markov chains, rooted trees, trapezoids, plane
partitions, semidistributive and trim lattices, alternating sign matrices,
and echelonmotion. The same query to the zbMATH Open API returned nine
documents (Einstein–Propp 2014, 2021; Grinberg–Roby 2015, 2016;
Striker–Williams 2012; Bernstein–Striker–Vorland 2021, 2024;
Defant–Hopkins–Poznanović–Propp 2023; Propp–Roby 2015), none with the
terms above in title or keywords. (The corpus query `all:rowmotion AND
all:minuscule`, sorted by date, returned Bernstein–Striker–Vorland 2022,
Pechenik 2021, Okada 2020, Hopkins 2019, Vorland 2017, Hopkins 2016.)

**Search 6 (Stenberg side, 2026-09-19; the primary texts).** Read for the
specific question:

- *Rush–Shi (2013).* Theorem 1.3: rowmotion and the toggle product
  $t_{(i_1,\dots,i_n)}$ are conjugate in the toggle group; Theorem 1.4:
  under Stembridge's bijection $J(P) \to W^J$, that toggle product
  corresponds to a Coxeter element $c$. They do not say that rowmotion
  itself is or is not a Coxeter element's action; the chain case is
  attributed to Stanley (Striker–Williams 2012, Thm 6.1); the D_n vector
  case receives no separate treatment; inner products, isometries and
  pairs of weights are not mentioned.
- *Okada (2021).* Coxeter-motion is defined as a product of file toggles
  (his eq. (10)) and shown conjugate to rowmotion in the birational toggle
  group (Thm 4.3): two maps, conjugate, not equal. The double-tailed
  diamond (D_n ω₁) is treated in his §5.2 with separate formulas for the
  two tails — the birational shadow of the same poset on which Theorem 2
  finds the half-turn linear — without any statement about Weyl group
  membership.
- *Hopkins (2020).* Records "the action of rowmotion is conjugate to the
  action of a Coxeter element" (§5.2.1) and the open conjectures on
  cyclic sieving (Conj. 5.8) and doppelgängers (Conj. 5.3); nothing on
  Weyl membership, isometry or pairs. Cites Rush–Shi, Grinberg–Roby,
  Garver–Patrias–Thomas 2023 and Okada on minuscule rowmotion.
- *Thomas–Williams (2019).* Trim lattices and rowmotion in slow motion;
  no statement about Weyl group membership or the weights.

**Search 7 (Stenberg side, 2026-09-19; phrasing).** Web searches for
rowmotion with "Weyl group element", "isometry", "signed permutation",
"vector representation", "half-spin", "E₇", "cyclic shift" and "Coxeter
element … coincide" returned only the documents above.

**What the search does not reach.** MathSciNet and the full text of
zbMATH's review database were not available; Google Scholar was reached
only through a general web index; work in progress and theses are not
indexed by the arXiv query. A reader with MathSciNet who finds the
statements of §§7.2, 7.6, 7.7 as known corollaries is asked to say so; the
paper's claims are worded to survive that.
