# THE CLOCK'S CLIFFORD HIERARCHY — SUMMARY OF SM-065 (2026-09-11)

**Stenberg side · with Claude. Written as §7.13 of
`joint_paper/Roof_and_Clock_DRAFT.md`, in the draft's three-tier shape:
what is classical is cited, what is computed is graded, what is read
is marked. Source: Stone BA (`STONE_BA_CLIFFORD_HIERARCHY.md`, brief
locked 89960a6d… before code; 7 PASS + 0 FAIL, every registered guess
confirmed). Not RH/GRH. Rule 3 throughout: "Clifford", "Pauli",
"T-gate" and "hierarchy" are labels for a chain of subgroups; no
quantum circuit is claimed.**

## 7.13 The clock's Clifford hierarchy

### 7.13.1 What is classical

In quantum computation the Clifford hierarchy (Gottesman–Chuang 1999)
is the chain of sets C₁ = the Pauli group, C_{j+1} = {U : UC₁U⁻¹ ⊆ C_j};
C₂ is the Clifford group and the T-gate lies in C₃ ∖ C₂: it is not a
Clifford gate, but it sends every Pauli into the Clifford group. In
group theory, for a subgroup H ≤ G and an element x ∈ G, the largest
subgroup of H normalised by x is the intersection of the conjugates of
H under ⟨x⟩, and the core of H in G is the intersection over all of G.

### 7.13.2 What was computed (SM-065)

**The definition.** For a board (W, R) and a lag k, the hierarchy at lag
k is the chain P₁(k) = W, P_{j+1}(k) = {g ∈ P_j : R^{−k}gR^k ∈ P_j}; so
P₂ = I_k, the grammar two instants share (§7.9), is the set of Weyl
elements the clock sends back into W — the shape of a hierarchy level
with W in the Clifford role. The depth d(k) is the first j with
P_{j+1} = P_j; the core P_∞(k) is where the chain stops.

**Lemma F [P].** P_j(k) = ⋂_{i<j} R^{ik}WR^{−ik}: the grammar shared by j
consecutive instants at stride k. Hence the core is the largest subgroup
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

### 7.13.3 What is identified, and what is read

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

### 7.13.4 Open

⟨W, R⟩ on the boards where it could not be enumerated (it is A₁₆ on the
D₅ half-spin by SM-060 and A₅₆ on the 56 by SM-057; the pattern
"alternating" is an observation on five boards, not a claim). A
hierarchy in the other direction, grading the powers of the clock
against a fixed subgroup of W, is not defined here. Nothing about the
clock as a gate on a Hilbert space.
