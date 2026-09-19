"""
build_v1.py — builds Roof_and_Clock_v1.0.md from Roof_and_Clock_DRAFT.md (v0.8) and the .docx.

Every change is an exact-match replacement asserted to occur exactly once, so the diff
v0.8 -> v1.0 is this file. Nothing computational is touched. Then pandoc renders the
markdown (LaTeX math -> native Word equations; ## -> Heading 1) to Roof_and_Clock_v1.0.docx.

Run from joint_paper/:  python build_v1.py
"""
import re, subprocess, sys, hashlib, pathlib

SRC = pathlib.Path("Roof_and_Clock_DRAFT.md")
OUT_MD = pathlib.Path("Roof_and_Clock_v1.0.md")
OUT_DOCX = pathlib.Path("Roof_and_Clock_v1.0.docx")
s = SRC.read_text(encoding="utf-8")
print("source", SRC, hashlib.sha256(s.encode()).hexdigest()[:16], len(s), "chars")

edits = []
def rep(old, new, count=1):
    edits.append((old, new, count))

# ---------------------------------------------------------------- header + status
old_header = s[: s.index("**Status.**")]
new_header = '''---
title: "The Roof and the Clock"
subtitle: "A verified computational model of W⁺(E₈), O₈⁺(2).3 and rowmotion on the E₇ minuscule poset, with three theorems on the non-linearity of rowmotion, and what the symmetry group and the clock share"
author:
  - Selina Stenberg
  - Ilya Balashov
  - "with Claude (Anthropic)"
date: "Version 1.0 — 19 September 2026"
---

'''
rep(old_header, new_header)

old_status = s[s.index("**Status.**") : s.index("## Abstract")]
new_status = '''**Status.** Version 1.0, prepared on the Stenberg side from the sealed
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

'''
rep(old_status, new_status)

# ---------------------------------------------------------------- §1 item 3
rep('''   give the exact per-pair rule on the E₇ board (§7.2). Three
   non-specialist literature searches found no match; we claim these as
   "not found" until a specialist search has been made (§7.4).''',
'''   give the exact per-pair rule on the E₇ board (§7.2). A literature
   search — four targeted searches, the complete arXiv rowmotion corpus to
   September 2026, zbMATH Open, and the primary texts read for the question
   (§7.4, Appendix B) — found no match; we claim these as "not found", not
   as new.''')

# ---------------------------------------------------------------- §7.2 rule as an equation
rep('''Write δ(u) = u + Ψu; δ is the XOR of the simple-root masks toggled by
rowmotion at u''',
'''Write $\\delta(u) = u + \\Psi u$; $\\delta$ is the XOR of the simple-root masks toggled by
rowmotion at $u$''')
rep('''```text
type(u,u′) is kept under Ψ   ⟺   t₁ + t₂ + t₃ is even
```''',
'''$$\\operatorname{type}(u,u')\\ \\text{is kept under}\\ \\Psi \\iff t_1 + t_2 + t_3 \\equiv 0 \\pmod 2 .$$''')

# ---------------------------------------------------------------- §7.3
rep('''B is bilinear and the type of a non-antipodal pair is B(u, u′). Hence
B(Ψu, Ψu′) − B(u, u′) = B(δu, u′) + B(u, δu′) + B(δu, δu′). With δ the sum
of the toggled simple roots β_c, B(β_c, w′) = ⟨α_c, w′⟩ mod 2 = |label_c(w′)|
for minuscule labels in {−1, 0, 1}, and B(β_c, β_c′) is the Cartan entry
mod 2, i.e. Dynkin adjacency. The three terms are t₁, t₂, t₃.''',
'''$B$ is bilinear and the type of a non-antipodal pair is $B(u, u')$. Hence
$$B(\\Psi u, \\Psi u') - B(u, u') = B(\\delta u, u') + B(u, \\delta u') + B(\\delta u, \\delta u').$$
With $\\delta$ the sum of the toggled simple roots $\\beta_c$,
$B(\\beta_c, w') = \\langle \\alpha_c, w' \\rangle \\bmod 2 = |\\mathrm{label}_c(w')|$
for minuscule labels in $\\{-1, 0, 1\\}$, and $B(\\beta_c, \\beta_{c'})$ is the Cartan entry
mod 2, i.e. Dynkin adjacency. The three terms are $t_1, t_2, t_3$.''')

# ---------------------------------------------------------------- §7.4 rewritten
old_74 = s[s.index("### 7.4 Literature status") : s.index("### 7.5 The E₆ control")]
new_74 = '''### 7.4 Literature status

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

'''
rep(old_74, new_74)

# ---------------------------------------------------------------- §7.6 typeset
rep('''Let λ be a simply-laced minuscule weight with poset P = P_λ, Coxeter
number h, rowmotion R carried to the weights Wλ. For λ = ω_k write c_k
for the multiplicity of colour k in P (the coefficient of α_k in λ + λ*),
s_j for the number of elements of P of rank j (0 ≤ j ≤ h − 2), and
σ = (s₀, …, s_{h−2}, c_k), the *extended rank sequence*, of length h.''',
'''Let $\\lambda$ be a simply-laced minuscule weight with poset $P = P_\\lambda$, Coxeter
number $h$, rowmotion $R$ carried to the weights $W\\lambda$. For $\\lambda = \\omega_k$ write $c_k$
for the multiplicity of colour $k$ in $P$ (the coefficient of $\\alpha_k$ in $\\lambda + \\lambda^*$),
$s_j$ for the number of elements of $P$ of rank $j$ ($0 \\le j \\le h-2$), and
$$\\sigma = (s_0, \\dots, s_{h-2}, c_k),$$
the *extended rank sequence*, of length $h$.''')

rep('''**Lemma.** (a) R(λ) = w₀λ; the bottom w₀λ = −λ* has a single nonzero
label, −1 at the dual node k*, hence a single cover p₀ = w₀λ + α_{k*},
which is the unique minimal element of P, and R(w₀λ) = p₀. Consequently''',
'''**Lemma.** (a) $R(\\lambda) = w_0\\lambda$; the bottom $w_0\\lambda = -\\lambda^*$ has a single nonzero
label, $-1$ at the dual node $k^*$, hence a single cover $p_0 = w_0\\lambda + \\alpha_{k^*}$,
which is the unique minimal element of P, and R(w₀λ) = p₀. Consequently''')

rep('''*Proof.* (a) ∅ ↦ the ideal generated by min P = {p₀}; and ⟨λ, λ − w₀λ⟩ =
Σ c_i ⟨ω_k, α_i⟩ = c_k. (b) The minimal elements of P ∖ P_{<j} are the
rank-j elements and generate P_{<j+1}; w(j+1) − w(j) is the sum of their
colours' simple roots, each added at a label −1 of w(j), so the inner
product drops by s_j; the wrap-around step λ → w₀λ drops by c_k by (a);
all weights have equal norm. ∎''',
'''*Proof.* (a) $\\emptyset \\mapsto$ the ideal generated by $\\min P = \\{p_0\\}$; and
$\\langle \\lambda, \\lambda - w_0\\lambda \\rangle = \\sum_i c_i \\langle \\omega_k, \\alpha_i \\rangle = c_k$.
(b) The minimal elements of $P \\setminus P_{<j}$ are the
rank-$j$ elements and generate $P_{<j+1}$; $w(j+1) - w(j)$ is the sum of their
colours' simple roots, each added at a label $-1$ of $w(j)$, so the inner
product drops by $s_j$; the wrap-around step $\\lambda \\to w_0\\lambda$ drops by $c_k$ by (a);
all weights have equal norm. ∎''')

rep('''*Proof.* If R ∈ W it is an isometry, so by Lemma (a) on the pair
(λ, w₀λ) ↦ (w₀λ, p₀), ⟨λ,λ⟩ − c_k = ⟨λ,λ⟩ − 1, i.e. c_k = 1. From the
classification, c_k = min(k, n+1−k) for A_n ω_k, 2 for D_n ω₁, ⌊n/2⌋ for
D_n ω_n (n ≥ 4), 2 for E₆ ω₁, 3 for E₇ ω₇; so c_k = 1 only for A_n with
k ∈ {1, n}, whose poset is a chain. Conversely on the chain the ideals
are the initial segments and R is the cyclic shift, a permutation matrix
in W(A_n) = S_{n+1}. ∎''',
'''*Proof.* If $R \\in W$ it is an isometry, so by Lemma (a) on the pair
$(\\lambda, w_0\\lambda) \\mapsto (w_0\\lambda, p_0)$, $\\langle \\lambda,\\lambda \\rangle - c_k = \\langle \\lambda,\\lambda \\rangle - 1$, i.e. $c_k = 1$. From the
classification, $c_k = \\min(k, n+1-k)$ for $A_n\\,\\omega_k$, $2$ for $D_n\\,\\omega_1$, $\\lfloor n/2 \\rfloor$ for
$D_n\\,\\omega_n$ ($n \\ge 4$), $2$ for $E_6\\,\\omega_1$, $3$ for $E_7\\,\\omega_7$; so $c_k = 1$ only for $A_n$ with
$k \\in \\{1, n\\}$, whose poset is a chain. Conversely on the chain the ideals
are the initial segments and $R$ is the cyclic shift, a permutation matrix
in $W(A_n) = S_{n+1}$. ∎''')

rep('''*Proof.* (Obstruction.) If R^m ∈ W, it is an isometry with R^m(w(j)) =
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
n−1 (n odd) sign changes, even either way. ∎''',
'''*Proof.* (Obstruction.) If $R^m \\in W$, it is an isometry with $R^m(w(j)) =
w(j+m)$, so by Lemma (b) $\\sigma_{j+m} = \\sigma_j$ for all $j$: $\\sigma$ is $m$-periodic, and
since $\\sigma_0 = s_0 = 1$, $\\sigma_m = 1$ is necessary. For $A_n\\,\\omega_k$ with $1 < k < n$
($n$ odd, $m = (n+1)/2$), $P$ is the $k \\times (n+1-k)$ rectangle and $s_m =
\\min(k, n+1-k) \\ge 2$. For $D_n\\,\\omega_n$, $n \\ge 5$ ($m = n-1$), $P$ is the shifted
staircase $\\{(i,j): 1 \\le i \\le j \\le n-1\\}$ with rank $i+j-2$, and $s_{n-1} =
\\lfloor (n+1)/2 \\rfloor - 1 \\ge 2$. For $E_6\\,\\omega_1$ ($m = 6$) the ranks are $1,1,1,2,2,2,2,2,1,1,1$
and $s_6 = 2$; for $E_7\\,\\omega_7$ ($m = 9$) they are $1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1$
and $s_9 = 2$. For $D_n\\,\\omega_1$ ($m = n-1$), $P$ is a chain of $n-2$ above the
antichain $\\{e_n, -e_n\\}$ above a chain of $n-2$, with $c_1 = 2$, and $\\sigma =
(1^{n-2}, 2, 1^{n-2}, 2)$ is $(n-1)$-periodic; the triality images at $n = 4$
and the chains pass likewise. (Sufficiency.) On $D_n\\,\\omega_1$ the ideals are $\\emptyset$,
the prefixes of the lower chain, the three ideals adding $e_n$, $-e_n$, or
both, and the extensions along the upper chain; rowmotion cycles
$\\emptyset \\to \\dots \\to P$ in $2n-2$ steps and swaps the two one-sided ideals. On weights:
$$-e_1 \\to -e_2 \\to \\dots \\to -e_{n-1} \\to e_{n-1} \\to \\dots \\to e_1 \\to -e_1, \\qquad e_n \\leftrightarrow -e_n.$$
Hence $R^{\\,n-1}(\\pm e_i) = \\mp e_{n-i}$ for $i \\le n-1$ and $R^{\\,n-1}(e_n) =
(-1)^{n-1} e_n$: the coordinate permutation $i \\leftrightarrow n-i$ with $n$ ($n$ even) or
$n-1$ ($n$ odd) sign changes, even either way. ∎''')

rep('''*Proof.* (D_n ω₁) Types are 0 and −1 (the n antipodal pairs). By the
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
intersecting, so (n−1)(n−2) pairs change. Total 3n² − 9n + 4. ∎''',
'''*Proof.* ($D_n\\,\\omega_1$) Types are $0$ and $-1$ (the $n$ antipodal pairs). By the
cycle above, $\\{e_n, -e_n\\}$ is the only antipodal pair $R$ keeps; the other
$n-1$ become non-antipodal and, $R$ permuting the pairs, $n-1$ non-antipodal
pairs become antipodal: $2(n-1)$ of $n(2n-1)$ pairs change. ($A_n\\,\\omega_2$) Weights
are 2-subsets $\\{a<b\\}$ of $[n+1]$; a pair's type is $|S\\cap T| \\in \\{0,1\\}$. The ideals
$(x_1 \\ge x_2)$ of the $2 \\times (n-1)$ rectangle correspond to $\\{n-x_1, n+1-x_2\\}$, and
rowmotion on the rectangle gives
$$R\\{a,b\\} = \\{a-1,\\, b-1\\} \\qquad (a \\ge 2,\\ b \\ge a+2),$$
$$R\\{a,a+1\\} = \\{a-1,\\, n+1\\} \\qquad (a \\ge 2),$$
$$R\\{1,b\\} = \\{b-2,\\, b-1\\} \\qquad (b \\ge 3),$$
$$R\\{1,2\\} = \\{n,\\, n+1\\}.$$
With $\\rho$ the rotation $i \\mapsto i-1 \\pmod{n+1}$, a Coxeter element and
an isometry, $R = \\rho\\circ\\varphi$ where $\\varphi$ fixes every 2-subset outside
$T = \\{\\{a,a+1\\}: 2 \\le a \\le n\\} \\cup \\{\\{1,b\\}: 2 \\le b \\le n+1\\}$ and permutes $T$ by
$\\{a,a+1\\} \\mapsto \\{1,a\\}$, $\\{1,b\\} \\mapsto \\{b-1,b\\}$ ($b \\ge 3$), $\\{1,2\\} \\mapsto \\{1,n+1\\}$; so
$\\kappa(R) = \\kappa(\\varphi)$. A pair ($S \\in T$, $G \\notin T$) changes type iff $a+1 \\in G$
($S = \\{a,a+1\\}$), iff $b-1 \\in G$ ($S = \\{1,b\\}$, $b \\ge 3$), or iff exactly one of
$2, n+1$ lies in $G$ ($S = \\{1,2\\}$): $2(n-2)^2 + 2(n-3)$ pairs. Inside $T$, of the
$(n-2) + 2(n-1) + \\binom{n}{2}$ intersecting pairs exactly $4n-5$ stay
intersecting, so $(n-1)(n-2)$ pairs change. Total $3n^2 - 9n + 4$. ∎''')

rep('''which is the unique minimal element of P, and R(w₀λ) = p₀. Consequently
⟨λ, w₀λ⟩ = ⟨λ,λ⟩ − c_k and ⟨w₀λ, p₀⟩ = ⟨λ,λ⟩ − 1. (b) The R-orbit of
w₀λ is the sequence of rank truncations P_{<j}; writing w(j) for their
weights, ⟨w(j), w(j+1)⟩ = ⟨λ,λ⟩ − σ_j for all j (indices mod h).''',
'''which is the unique minimal element of $P$, and $R(w_0\\lambda) = p_0$. Consequently
$$\\langle \\lambda, w_0\\lambda \\rangle = \\langle \\lambda,\\lambda \\rangle - c_k, \\qquad
\\langle w_0\\lambda, p_0 \\rangle = \\langle \\lambda,\\lambda \\rangle - 1 .$$
(b) The $R$-orbit of
$w_0\\lambda$ is the sequence of rank truncations $P_{<j}$; writing $w(j)$ for their
weights,
$$\\langle w(j), w(j+1) \\rangle = \\langle \\lambda,\\lambda \\rangle - \\sigma_j \\quad \\text{for all } j \\ (\\text{indices mod } h).$$''')

rep('''**Theorem 1.** R ∈ W ⟺ P is a chain ⟺ λ ∈ {ω₁, ω_n} of A_n; then R is
the Coxeter element s₁ ⋯ s_n, the cyclic shift of e₁, …, e_{n+1}.''',
'''**Theorem 1.**
$$R \\in W \\iff P \\text{ is a chain} \\iff \\lambda \\in \\{\\omega_1, \\omega_n\\} \\text{ of } A_n;$$
then $R$ is the Coxeter element $s_1 \\cdots s_n$, the cyclic shift of $e_1, \\dots, e_{n+1}$.''')

rep('''**Theorem 2.** Let h be even and m = h/2. Then R^m ∈ W ⟺ P is a chain
or λ is the vector representation of D_n, n ≥ 3 (with D₃ ω₁ = A₃ ω₂ and,
for D₄, the triality images ω₃, ω₄). In the vector case, on the weights
±e_i,

  R^{n−1}(e_i) = −e_{n−i} (1 ≤ i ≤ n−1),  R^{n−1}(e_n) = (−1)^{n−1} e_n,

a signed permutation with an even number of sign changes, in W(D_n).''',
'''**Theorem 2.** Let $h$ be even and $m = h/2$. Then
$$R^m \\in W \\iff P \\text{ is a chain, or } \\lambda \\text{ is the vector representation of } D_n,\\ n \\ge 3$$
(with $D_3\\,\\omega_1 = A_3\\,\\omega_2$ and, for $D_4$, the triality images $\\omega_3, \\omega_4$).
In the vector case, on the weights $\\pm e_i,$
$$R^{\\,n-1}(e_i) = -e_{n-i} \\ (1 \\le i \\le n-1), \\qquad R^{\\,n-1}(e_n) = (-1)^{n-1} e_n ,$$
a signed permutation with an even number of sign changes, in $W(D_n)$.''')

rep('''**Corollary.** R^j ∈ W implies σ is j-periodic; so the linear powers of
rowmotion are among the periods of σ. For E₇, σ has no period below 18:
no power of the clock but the identity is a Weyl element (SM-054's
C_W(Ψ) ∩ ⟨Ψ⟩ = 1, by hand).''',
'''**Corollary.** $R^j \\in W$ implies $\\sigma$ is $j$-periodic; so the linear powers of
rowmotion are among the periods of $\\sigma$. For $E_7$, $\\sigma$ has no period below 18:
no power of the clock but the identity is a Weyl element (SM-054's
$C_W(\\Psi) \\cap \\langle \\Psi \\rangle = 1$, by hand).''')

rep('''**Theorem 3.** Let κ(R) be the fraction of unordered pairs {w, w′} with
⟨Rw, Rw′⟩ = ⟨w, w′⟩. Then κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1)) for n ≥ 3, and
κ(A_n ω₂) = 1 − (3n² − 9n + 4)/C(C(n+1,2), 2) for n ≥ 3.''',
'''**Theorem 3.** Let $\\kappa(R)$ be the fraction of unordered pairs $\\{w, w'\\}$ with
$\\langle Rw, Rw' \\rangle = \\langle w, w' \\rangle$. Then, for $n \\ge 3$,
$$\\kappa(D_n\\,\\omega_1) = 1 - \\frac{2(n-1)}{n(2n-1)}, \\qquad
\\kappa(A_n\\,\\omega_2) = 1 - \\frac{3n^2 - 9n + 4}{\\binom{\\binom{n+1}{2}}{2}} .$$''')

rep('''polynomial in n was confirmed to n = 10 (12·D₃(n) = 15n⁴ − 110n³ + 165n²
+ 314n − 432), suggesting degree 2k − 2 for ω_k [obs].''',
'''polynomial in $n$ was confirmed to $n = 10$,
$$12\\,D_3(n) = 15n^4 - 110n^3 + 165n^2 + 314n - 432,$$
suggesting degree $2k - 2$ for $\\omega_k$ [obs].''')

# ---------------------------------------------------------------- §7.8
rep('''  W ∩ Ψ^k W Ψ^{−k} = {1}      for k = 1, …, 8 and 10, …, 17;
  W ∩ Ψ⁹ W Ψ^{−9} = {1, ι}.''',
'''$$W \\cap \\Psi^k W \\Psi^{-k} = \\{1\\} \\quad (k = 1, \\dots, 8,\\ 10, \\dots, 17), \\qquad
W \\cap \\Psi^9 W \\Psi^{-9} = \\{1, \\iota\\}.$$''')
rep('''  ⟨W, Ψ⟩ = A₅₆,      ⟨W, pr⟩ = 2²⁸ ⋊ Sp₆(2),      ⟨W, Ψ, pr⟩ = S₅₆.''',
'''$$\\langle W, \\Psi \\rangle = A_{56}, \\qquad \\langle W, \\mathrm{pr} \\rangle = 2^{28} \\rtimes \\mathrm{Sp}_6(2), \\qquad \\langle W, \\Psi, \\mathrm{pr} \\rangle = S_{56}.$$''')

# ---------------------------------------------------------------- §7.9
rep('''w₀, acting on weights as −σ (σ the diagram automorphism, trivial when
−1 ∈ W), reverses rowmotion: w₀ R w₀ = R^{−1}.''',
'''$w_0$, acting on weights as $-\\sigma$ ($\\sigma$ the diagram automorphism, trivial when
$-1 \\in W$), reverses rowmotion:
$$w_0 R w_0 = R^{-1}.$$''')
rep('''    pr = ι ∘ w₀(E₆) ∘ t,   t = the swap of the two poles,
''',
'''  $$\\mathrm{pr} = \\iota \\circ w_0(E_6) \\circ t, \\qquad t = \\text{the swap of the two poles},$$
''')

# ---------------------------------------------------------------- §7.9.5 stale phrase (the reason is §7.12)
rep('''  Spin(10) — is the one board in the family that shares more, for a
  reason not yet found.''',
'''  Spin(10) — is the one board in the family that shares more; the
  mechanism is given in §7.12.2 and the reason in §7.12.4.''')

# ---------------------------------------------------------------- §7.10
rep('''  #(+1) = #(−1) = |P|/h,   #(0) = r − 2|P|/h,
''',
'''$$\\#(+1) = \\#(-1) = \\frac{|P|}{h}, \\qquad \\#(0) = r - \\frac{2|P|}{h},$$
''')

# ---------------------------------------------------------------- §7.12.4
rep('''by rank (number of minus signs); W(B₄) = 𝔽₂⁴ ⋊ S₄ acts affinely, w(x) =
π(x) ⊕ v. **Lemma (Weyl rank-shift).** For w = (π,v), writing u = π⁻¹(v),
rank(w(x)) = wt(π(x)⊕v) = wt(x⊕u), so the rank-shift is Δ_w(x) = wt(u) −
2|x∩u| — a function of the single vector u.''',
'''by rank (number of minus signs); $W(B_4) = \\mathbb{F}_2^4 \\rtimes S_4$ acts affinely, $w(x) =
\\pi(x) \\oplus v$. **Lemma (Weyl rank-shift).** For $w = (\\pi,v)$, writing $u = \\pi^{-1}(v)$,
$\\operatorname{rank}(w(x)) = \\operatorname{wt}(\\pi(x)\\oplus v) = \\operatorname{wt}(x\\oplus u)$, so the rank-shift is
$$\\Delta_w(x) = \\operatorname{wt}(u) - 2\\,|x \\cap u|$$
— a function of the single vector $u$.''')

# ---------------------------------------------------------------- §7.13
rep('''**Lemma F [P].** P_j(k) = ⋂_{i<j} R^{ik}WR^{−ik}: the grammar shared by j
consecutive instants at stride k.''',
'''**Lemma F [P].**
$$P_j(k) = \\bigcap_{i<j} R^{ik}\\, W\\, R^{-ik}:$$
the grammar shared by $j$ consecutive instants at stride $k$.''')

# ---------------------------------------------------------------- §11
rep('''SM-024/028) and of the standalone note *The Bitangent Bridge* (SM-008); the
second author's own expansion of the representation-theoretic framework and
the joint bibliography are pending his review.''',
'''SM-024/028) and of the standalone note *The Bitangent Bridge* (SM-008),
independently re-verified by the second author (§11.8), with his own
contribution as §11.9.''')
rep('''with α = (−1+√−7)/2. The Balashov-side tower''',
'''with $\\alpha = (-1+\\sqrt{-7})/2$. The Balashov-side tower''')
rep('''Realize PSL(2,7) = GL(3,𝔽₂) on V ⊕ V* ≅ 𝔽₂⁶ with the symplectic form
ω((v,f),(w,h)) = f(w) + h(v).''',
'''Realize $\\mathrm{PSL}(2,7) = \\mathrm{GL}(3,\\mathbb{F}_2)$ on $V \\oplus V^* \\cong \\mathbb{F}_2^6$ with the symplectic form
$$\\omega\\big((v,f),(w,h)\\big) = f(w) + h(v).$$
''')

# ---------------------------------------------------------------- §12 outlook
rep('''and the "not found" status of §§7.2, 7.6, 7.7 (§7.4) awaits a specialist
literature search before it can be sharpened to a claim of novelty.''',
'''and the "not found" status of §§7.2, 7.6, 7.7 (§7.4, Appendix B) is
exactly that: a specialist reader with MathSciNet access may know these as
corollaries, and the reference would be welcome.''')

# ---------------------------------------------------------------- §14
rep('''No claim of novelty for §§7.2, 7.6, 7.7 beyond
"not found by three non-specialist searches" (§7.4).''',
'''No claim of novelty for §§7.2, 7.6, 7.7 beyond
"not found" (§7.4, Appendix B).''')
rep('''No claim of novelty for §§7.8–7.13 beyond "not found" (§7.4, four
searches);''',
'''No claim of novelty for §§7.8–7.13 beyond "not found" (§7.4,
Appendix B);''')

# ---------------------------------------------------------------- §7.12.4: B₈ (SM-067, Stone BC)
rep('''reducing to the fact that the shift is exactly ±n/2 (verified at B₄; B₈ next).''',
'''reducing to the fact that the shift is exactly ±n/2 (verified at B₄ and at B₈,
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
of the middle rank ({3,4,5}; on B₄, O₂\'s {1,2,3}), equivalently those on which
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
|I₁₆| itself is not decided.

**Why four — the commutation theorem [P, SM-070].** For even n ≥ 4 the
element w_n = −(e₂e₃)(e₄e₅)…(e_{n−2}e_{n−1}) commutes with the half-turn Rⁿ
if and only if n = 4. The proof rests on a one-line recursion for rowmotion on
the shifted staircase in "excess" coordinates d_k = c_k − k (c_k the plus
positions), from which the orbit of λ is written in closed form for every n:
R^{2j}λ = [n] ∖ {n, n−2, …, n−2j+2}, R^{2j+1}λ = [n] ∖ {n−1, …, n−2j+1}, ranks
0, n, n−1, n−1, …, 1, 1 around the clock — so the half-turn shifts every rank
on the full-height orbit by exactly ±n/2 for every even n, and the hypothesis
of the rank-shift theorem above is now proved for all n rather than verified
at 4, 8 and 16. On that orbit w_n acts by i ↦ 2 − i (even clock positions)
and i ↦ −i (odd), both commuting with i ↦ i + n; on a carrying orbit
commutation is automatic (wHx = x = Hwx). At n = 4 those two orbits are the
whole board, which is why −τ commutes with R⁴. For even n ≥ 6 the point e₂
(one minus sign, at position 2) is a witness: the closed forms
Rⁿ(e₂) = {1, 2} ∪ {5, 7, …, n−1} and Rⁿ({3, n}) = [n] ∖ {4, 6, 7, 9, …, n−1}
(both by induction along the orbit in excess coordinates) give 2 ∈ w_n Rⁿ e₂
but 2 ∉ Rⁿ w_n e₂, since w_n e₂ = −{3, n}. Together with the criterion this
is the reason for the 4-cube: the mechanism is present on every free clock;
its consequence needs a commutation that only the smallest board allows. Still
open: that w_n is the nearest Weyl element for n > 8, and C_W(Rⁿ) = {±1} in
general.''')

# ---------------------------------------------------------------- §13: SM-067\'s inversions
rep('''SM-062 once, SM-063 twice), each reported in its row. SM-057, SM-059 and
SM-065 had every registered guess confirmed.''',
'''SM-062 once, SM-063 twice), each reported in its row. SM-057, SM-059 and
SM-065 had every registered guess confirmed.

In SM-067 (§7.12.4, B₈): the guesses that the half-turn anomaly recurs on the
8-cube (|I₈| > |C₈|, ratio 2) and that it marks the boards with a free clock
(inverted: I_k = C_k at every lag on B₈, the D₉ half-spin, B₆ and B₇), that
−1 exchanges the two carrying orbits (it fixes each), and that D₉ carries a
survivor at a lag coprime to 16 (none); two scoring slips of the executor\'s
own (the rank list read against the clock\'s direction; a containment bar that
demanded extras which do not exist), both kept in the first-run log. In
SM-068 (the criterion): that the agreement set on B₈ has no Weyl symmetry
beyond ±1 (it has ⟨−1, w⟩), that the criterion explains B₃ from inside W(B₃)
(no spanning agreement set exists there), and that the nearest element is
unique only up to the antipode (it is unique outright). In SM-069 (the
16-cube): that two orbits carry the half-turn (sixteen do, −1 swapping four
pairs of them) and that every orbit spans (61 do not); one instrumentation
error in the centralizer search, fixed and cross-checked, in the first-run
log.''')

# ---------------------------------------------------------------- Appendix A closed
rep('''(Stone AZ, 11 + 2); SM-065 (Stone BA, 7/7, 2026-09-11) sent, awaiting his word.''',
'''(Stone AZ, 11 + 2); SM-065 (Stone BA, 7/7, 2026-09-11) — JOINT on his word
of 2026-09-14.''')
rep('''lemma; prepared on the Stenberg side, awaiting the second author's word.
''',
'''lemma — JOINT on the second author's word of 2026-09-14 (Lemma BB-A rebuilt
from scratch on his side: W(B₄) = 𝔽₂⁴ ⋊ S₄ of order 384, the rank identity on
200 random triples, the contradiction by hand).

Added in v0.8 (§11.9): the second author's model of χ₆ as the Fano plane's
deleted permutation module, his construction re-run on the Stenberg side; the
identity with §11.3's size-7 orbits verified (`verify_fano_bitangent_identity.py`).
All thirty-six units cited above are JOINT as of 2026-09-14.

Added 2026-09-19 (§7.12.4, the B₈ paragraphs): SM-067 (Stone BC, 14 + 4
inverted), SM-068 (Stone BD, 7 + 3), SM-069 (Stone BE, 9 + 2), SM-070 (Stone
BF, 8/8) — the 8-cube, the criterion, the 16-cube and the commutation theorem,
prepared on the Stenberg side under briefs locked before code; the second
author's re-execution is invited. They are the four units cited in this paper
that are not yet JOINT.
''')

# ---------------------------------------------------------------- references added
rep('''- Green, R. M.; Xu, T. Branching rules of minuscule representations via a new partial order. arXiv:2402.06732 (2024), to appear in *Combinatorial Theory*.''',
'''- Garver, A.; Patrias, R.; Thomas, H. Minuscule reverse plane partitions via quiver representations. *Selecta Math.* 29 (2023), 37.
- Green, R. M.; Xu, T. Branching rules of minuscule representations via a new partial order. arXiv:2402.06732 (2024), to appear in *Combinatorial Theory*.
- Hopkins, S. Order polynomial product formulas and poset dynamics. arXiv:2006.01568 (2020); in *Open Problems in Algebraic Combinatorics*, Proc. Sympos. Pure Math. 110, AMS, 2024.''')
rep('''- Panyushev, D. I. Weight posets associated with gradings of simple Lie algebras, Weyl groups, and arrangements of hyperplanes. *J. Algebraic Combin.*; arXiv:1412.0987.''',
'''- Panyushev, D. I. Weight posets associated with gradings of simple Lie algebras, Weyl groups, and arrangements of hyperplanes. *J. Algebraic Combin.* 44 (2016) 325–351; arXiv:1412.0987.
- Pechenik, O. Minuscule analogues of the plane partition periodicity conjecture of Cameron and Fon-Der-Flaass. arXiv:2107.02679 (2021).''')
rep('''- Stembridge, J. R. On minuscule representations, plane partitions and involutions in complex Lie groups. *Duke Math. J.* 73 (1994) 469–490.''',
'''- Stanley, R. P. Promotion and evacuation. *Electron. J. Combin.* 16(2) (2009) R9.
- Stembridge, J. R. On minuscule representations, plane partitions and involutions in complex Lie groups. *Duke Math. J.* 73 (1994) 469–490.
- Stembridge, J. R. Minuscule elements of Weyl groups. *J. Algebra* 235 (2001) 722–743.''')
rep('''- Striker, J.; Williams, N. Promotion and rowmotion. *European J. Combin.* 33 (2012) 1919–1942.''',
'''- Striker, J.; Williams, N. Promotion and rowmotion. *European J. Combin.* 33 (2012) 1919–1942.
- Thomas, H.; Williams, N. Rowmotion in slow motion. *Proc. London Math. Soc.* 119 (2019) 1149–1178; arXiv:1712.10123.''')

# ---------------------------------------------------------------- apply
for old, new, count in edits:
    n = s.count(old)
    assert n == count, f"expected {count} occurrence(s), found {n}:\n{old[:120]!r}"
    s = s.replace(old, new)

# every display equation in its own paragraph (pandoc then emits a standalone oMathPara,
# which Word and LibreOffice both centre without disturbing the surrounding text)
lines = s.split("\n"); out = []; i = 0; n_disp = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^(\s*\$\$.*?\$\$)(\s*\S.*)$", ln)    # display followed by trailing prose: split
    if m:
        lines[i:i + 1] = [m.group(1), m.group(2).lstrip()]
        ln = lines[i]
    if re.match(r"^\s*\$\$", ln):                      # start of a display block
        j = i
        while not lines[j].rstrip().endswith("$$"):    # find its end (same line or later)
            j += 1
        if out and out[-1].strip() != "":
            out.append("")
        out.extend(lines[i:j + 1]); n_disp += 1
        if j + 1 < len(lines) and lines[j + 1].strip() != "":
            out.append("")
        i = j + 1
    else:
        out.append(ln); i += 1
s = "\n".join(out)
print("display equations isolated:", n_disp)

# ---------------------------------------------------------------- Appendix B
appendix_b = '''
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
  $t_{(i_1,\\dots,i_n)}$ are conjugate in the toggle group; Theorem 1.4:
  under Stembridge's bijection $J(P) \\to W^J$, that toggle product
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
'''
s = s.rstrip("\n") + "\n" + appendix_b

OUT_MD.write_text(s, encoding="utf-8", newline="\n")
print("wrote", OUT_MD, hashlib.sha256(s.encode()).hexdigest()[:16], len(s), "chars,", s.count("\n"), "lines,", len(edits), "edits applied")

# sanity: no stale status words remain
for bad in ["awaiting the second author", "pending his review", "pending the second author", "non-specialist searches", "DRAFT v0.8"]:
    assert bad not in s, f"stale phrase remains: {bad}"
print("stale-phrase check: clean")

# ---------------------------------------------------------------- pandoc
cmd = ["pandoc", str(OUT_MD), "-o", str(OUT_DOCX),
       "--from", "markdown+tex_math_dollars+pipe_tables+yaml_metadata_block+smart",
       "--shift-heading-level-by=-1"]
print(" ".join(cmd))
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stdout, r.stderr)
if r.returncode != 0:
    sys.exit(r.returncode)
print("wrote", OUT_DOCX, OUT_DOCX.stat().st_size, "bytes", hashlib.sha256(OUT_DOCX.read_bytes()).hexdigest()[:16])
