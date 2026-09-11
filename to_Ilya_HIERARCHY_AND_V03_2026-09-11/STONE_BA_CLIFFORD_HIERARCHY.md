# STONE BA — THE CLOCK'S CLIFFORD HIERARCHY

**Stenberg side · with Claude · 2026-09-11. Brief
`BRIEF_STONE_BA_CLIFFORD_HIERARCHY.md` sha-locked 89960a6d… BEFORE code,
two lemmas proved in the brief, no new exploration. Verifier
`verify_stone_ba_clifford_hierarchy.py`, log: 7 PASS + 0 FAIL — every
registered guess CONFIRMED, including the one named exception. The
first run kept as `_FIRSTRUN.log` (one printout used the wrong
coordinate reader on the D₅ board; instrumentation, no check touched).
About two minutes. Machines: Stone AQ's `Minuscule`, Stone AT's BFS,
Stone AV's e-coordinate boards, all VERBATIM. E₇ cited from SM-057, not
run. Own cache `_stone_ba_cache/witnesses_ba.json`. Registry row SM-065.
Merkabit-side mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "Clifford", "Pauli", "T-gate", "hierarchy" are
labels for a chain of subgroups; no quantum circuit is claimed; nothing
here is about a lepton. The reading in §5 is marked as a reading.

## 1. One paragraph

The merkabit's open problem asked whether the clock is a T-gate for the
Weyl group as Clifford group. The T-gate sends Paulis into the Clifford
group without being Clifford; the grammar two instants share,
I_k = {g ∈ W : R^{−k}gR^k ∈ W}, is exactly the set of Weyl elements the
clock at lag k sends back into W. So the clock's hierarchy at lag k is
the chain P₁ = W, P_{j+1} = {g ∈ P_j : R^{−k}gR^k ∈ P_j}. **Lemma F:** P_j
is the grammar shared by j consecutive instants at stride k (the
intersection of the first j clock-conjugates of W), so the chain stops
at the largest subgroup of W the clock power normalises — the *core*.
**Lemma G:** it stops at the second level exactly when a reverser of the
clock normalises I_k, because conjugating I_k by R^k and by any reverser
both give I_{−k}. From the sealed record that predicted the whole
family: depth 1 on the chains (R ∈ W), depth 2 everywhere else — the
cores being C_W(R^k) on the rich boards, C_W(R^{2k}) on the vectors
(SM-064), the dihedral I₄ on the 4-cube — **with one exception, the D₅
half-spin at lags 3 and 5**, where SM-063 had found I₃ ≠ I₅, so no
reverser normalises I₃ and the chain drops once more, to the trivial
group. The machine confirmed all of it on 278 (board, lag) pairs across
44 boards. The Pauli group of the analogy, the core, is trivial or ±1 on
every rich board and on the 56: there is nothing in W the clock carries
along. Where it is not trivial it is never normal in W, and the core of
W in the group the clock generates with it is trivial on every board
where that group could be enumerated (⟨W, R⟩ is A₆ on the D₃ vector, A₈
on the D₄ vector and on the B₃ spinor). The analogy holds one level and
no further.

## 2. The lemmas

| lemma | statement | status |
|---|---|---|
| F | P_j(k) = ⋂_{i<j} R^{ik}WR^{−ik}; the core is the largest R^k-normalised subgroup of W and ⊇ Core_{⟨W,R^k⟩}(W) | proved; checked on all 278 pairs (BA1) |
| G | P₃ = P₂ ⟺ R^k normalises I_k ⟺ I_k = I_{−k} ⟺ any reverser in W normalises I_k | proved; checked on all 278 pairs (BA2) |

## 3. Bars

| bar | content | outcome |
|---|---|---|
| BA0 | brief locked | PASS (89960a6d…) |
| BA1 | Lemma F numerically | PASS |
| BA2 | Lemma G numerically | PASS |
| BA2b | reversers number \|C_W(R)\| on every board (SM-062 re-seen) | PASS |
| BA3 (guess) | depth ≤ 2 everywhere except the D₅ half-spins at lags 3, 5 (depth 3, trivial core); depth 1 exactly where I_k = W; the cores as named | PASS — CONFIRMED, all 278 pairs |
| BA4a (guess) | wherever 2 < \|core\| < \|W\| the core is not normal in W | PASS — 44 cores, none normal |
| BA4b (guess) | Core_{⟨W,R⟩}(W) trivial on the D₃ and D₄ vectors, strictly below P_∞(1) (orders 4 and 6); B₃ recorded | PASS; on B₃ both are trivial |
| BA5 [obs] | the tables; the 4-cube's and D₅'s chains element by element | recorded |
| BA6 [I] | the reading | recorded |

## 4. The table, compressed

| boards | depth by lag | core |
|---|---|---|
| chains A_n ω₁, ω_n | 1 | W |
| rich boards (A_n ω_k off the ends, E₆, D₆/D₇ half-spins, B₅) | 2 | C_W(R^k): trivial, or 2 at the half-turn where −1 ∈ W (A₅ω₃, A₇ω₄, D₆/D₇ half-spins, E₆, B₅), 4 on the D₆ half-spins |
| D_n vectors (D₃ = A₃ω₂, D₄..D₇) | 2, and 1 at the half-turn | C_W(R^{2k}) (SM-064); W at the half-turn |
| B₃ spinor | 2 | 1, 2, 16, 2, 1 |
| B₄ spinor | 2 | 1 except the dihedral 8 at lag 4 |
| D₅ half-spins ω₄, ω₅ | 2, **3 at lags 3 and 5** | 1 except 8 at lag 4; chains 1920 ⊃ 2 ⊃ 1 at lags 3, 5 |
| the 56 (SM-057, cited) | 2 | 1, and {1, ι} at lag 9 |

⟨W, R⟩: A₆ (order 360) on the D₃ vector, A₈ (20,160) on the D₄ vector
and on the B₃ spinor — the clock generates the alternating group with
W here as on the D₅ half-spin (A₁₆, SM-060) and the 56 (A₅₆, SM-057).

## 5. What was learned, and the reading

- The hierarchy is the run of shared grammars along the clock: two
  instants, three, all. On every board but one the grammar two instants
  share is already the grammar all instants share. The one place where
  a third instant forgets more than the second is the D₅ half-spin at
  lags 3 and 5 — the lag-3 survivor of SM-058, which SM-063 showed is
  carried to a different element at lag 5.
- Lemma G is the reason: the chain stops early exactly when time
  reversal preserves the shared grammar. It always does on boards with
  a central reverser, on the vectors, and on the rich boards; it fails
  only for that one survivor.
- Read [I]: the Pauli group of the T-gate analogy is the core. On every
  rich board and on the 56 it is trivial or ±1: the clock is beyond
  every level of the hierarchy, there is nothing in W it carries along.
  On the vectors and the 4-cube it is C_W(R^{2k}) and the dihedral I₄:
  there the clock is a level-three gate for that group (it maps it into
  W by an automorphism, outer when n is odd, SM-064), and W contains it
  without normalising it. The analogy holds for one level and no
  further; SM-057's "Clifford-like W with one non-Clifford Ψ" is exact
  in the sense that no Pauli-like subgroup of W(E₇) is normalised by Ψ.

## 6. Not claimed

Nothing about ⟨W, R⟩ beyond the three boards where it was enumerated.
No hierarchy in the other direction (which powers of R lie at which
level relative to a fixed subgroup): not defined here. Nothing about
the clock as an actual gate on an actual Hilbert space.

## 7. Synthesis line

Two instants share what all instants share, everywhere but in one
place; and what they share the clock can carry but never keep — no
part of the board's symmetry is the clock's own.
