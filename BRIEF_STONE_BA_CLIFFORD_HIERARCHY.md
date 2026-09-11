# BRIEF — STONE BA: THE CLOCK'S CLIFFORD HIERARCHY

**Staged 2026-09-11 on Selina's "do 1." (the merkabit's open problem #3,
the clock as a T-gate, from `56_MACHINE_BRIEF.md`). Locked before code
(`BRIEF_STONE_BA_LOCK.sha256`). No new exploration: the hand work below
is from the sealed record (SM-057, SM-058, SM-059, SM-063, SM-064).
Deviations = dated AMENDMENT; post-reveal changes are findings.
Merkabit-side mathematics. Registry row SM-065.**

## Question

In the quantum-computing picture the T-gate is not a Clifford gate, but
it sends every Pauli into the Clifford group; the Clifford hierarchy is
the chain of such levels. SM-057 called the Weyl group Clifford-like and
the clock Ψ its one non-Clifford element. SM-058/063/064 computed the
grammar two instants share, I_k = {g ∈ W : R^{−k}gR^k ∈ W} — exactly
"the Weyl elements the clock sends back into W", the shape of the
hierarchy's next level. What is the clock's hierarchy on every board:
how deep does the chain go, where does it stop, and is what it stops at
anything like a Pauli group?

## Definitions

For a board (W, R) and a lag k, the *hierarchy at lag k* is the chain
P₁(k) = W, P_{j+1}(k) = {g ∈ P_j(k) : R^{−k}gR^k ∈ P_j(k)}. So P₂ = I_k.
The *depth* d(k) is the first j with P_{j+1} = P_j; the *core*
P_∞(k) = P_{d}(k).

## What was derived by hand (proved here, before code)

**Lemma F (the chain is the run of shared grammars).**
P_j(k) = ⋂_{i=0}^{j−1} R^{ik} W R^{−ik}: the grammar shared by j
consecutive instants at stride k. *Proof.* P_{j+1} = P_j ∩ R^kP_jR^{−k},
by induction. ∎ Hence P_∞(k) is the largest subgroup of W normalised by
R^k (a subgroup H ≤ W with R^{−k}HR^k ⊆ H has R^{−k}HR^k = H, and the
intersection of all conjugates of W under ⟨R^k⟩ is such an H containing
every other), and P_∞(k) ⊇ Core_{⟨W,R^k⟩}(W).

**Lemma G (when the chain stops at the second level).** Let r ∈ W be
any reverser of the clock (rRr⁻¹ = R⁻¹; w₀ is one by SM-059, and they
form the coset w₀·C_W(R) by SM-062). Then
P₃(k) = P₂(k) ⟺ R^k normalises I_k ⟺ I_k = I_{−k} ⟺ r normalises I_k.
*Proof.* P₃ = I_k ∩ R^kI_kR^{−k}, and |R^kI_kR^{−k}| = |I_k|, so P₃ = P₂
iff R^kI_kR^{−k} = I_k. Now R^{−k}I_kR^k = W ∩ R^{−k}WR^k = I_{−k}, and
rI_kr⁻¹ = W ∩ rR^kWR^{−k}r⁻¹ = W ∩ R^{−k}WR^k = I_{−k} since r reverses R
and r ∈ W. ∎ (Whether r normalises I_k does not depend on which reverser
is taken.)

**Consequences, board by board (from the sealed record).**
- Chains (R ∈ W): P_j = W for all j; depth 1; core W.
- Rich boards (SM-058: I_k = C_W(R^k)): w₀C_kw₀ = C_W(R^{−k}) = C_k, so
  depth ≤ 2 and core C_k (trivial except at the half-turn where −1 ∈ W).
- D_n vectors (SM-064: I_k = C_W(R^{2k})): w₀ normalises it (same
  argument), depth ≤ 2, core C_W(R^{2k}).
- Boards with −1 ∈ W (w₀ central): depth ≤ 2 always, core I_k. This
  covers B₄ lag 4 (core the dihedral I₄ of order 8) and the 56 (SM-057:
  I₉ = {1, ι}, all other I_k trivial).
- **The D₅ half-spin at lags 3 and 5 is the exception:** SM-063's AY9b
  found I₃ = {1, p} and I₅ = {1, p₅} with p₅ = R^{−3}pR^3 ≠ p; so I₃ ≠ I₋₃,
  w₀ does not normalise I₃, and P₃(3) = I₃ ∩ R^3I₃R^{−3} = {1}: depth 3,
  core trivial. Likewise lag 5. At lag 4 (R⁴ an involution) depth 2,
  core I₄ of order 8. This is the only place in the family where the
  grammar two instants share is not the grammar all instants share.

**The reading, stated once (marked [I] in the findings).** The Pauli
group of the analogy is the core: the largest subgroup of W the clock
normalises. On every rich board and on the 56 it is trivial (or ±1):
the clock is beyond every level of the hierarchy, there is nothing in
W it carries along. On the vectors and the 4-cube it is C_W(R^{2k}) and
I₄: there the clock is a level-three gate for that Pauli-like group
(it maps it into W by an automorphism, outer when n is odd), and W is
its Clifford group only in the weak sense that it contains it, since
(guess BA4) the core is not normal in W.

## Bars (registered; PASS / FAIL / INVERTED at equal prominence)

- **BA0:** the brief is sha-locked.
- **BA1 (Lemma F, [P] + check):** on every board and lag the chain
  computed by the definition equals the run of partial intersections of
  the clock-conjugates of W, and the core is normalised by R^k and equals
  the intersection over the whole ⟨R^k⟩-orbit of conjugates.
- **BA2 (Lemma G, [P] + check):** on every board and lag, P₃ = P₂ if and
  only if a reverser r ∈ W normalises I_k (r found by solving rR = R⁻¹r
  in W; the first solution used; the count of solutions recorded and
  compared with SM-062's |C_W(R)|).
- **BA3 (REGISTERED GUESS, resolvable INVERTED):** the depth is ≤ 2 on
  every board of the 42 (E₇ from SM-057, not re-run) and on the B₃, B₄,
  B₅ spinors, at every lag — with exactly one exception: the D₅ half-spins
  (ω₄ and ω₅) at lags 3 and 5, depth 3 with trivial core. Depth 1 exactly
  on the chains. The cores are: W on chains; C_W(R^k) on the rich boards;
  C_W(R^{2k}) on the D_n vectors; I₄ (order 8) on B₄ and the D₅ half-spins
  at the half-turn; 1 on the D₅ half-spins at lags 3, 5.
- **BA4 (REGISTERED GUESS, resolvable INVERTED):** wherever the core is
  neither W nor of order ≤ 2, it is not a normal subgroup of W (the
  Pauli-like group is not W-normal: the analogy holds one level and no
  further). Where ⟨W, R⟩ has order ≤ 4·10⁶ (the D₃ and D₄ vector boards
  and the B₃ spinor) the core of W in ⟨W, R⟩ is computed and compared
  with P_∞(1): guess: trivial, hence strictly smaller than P_∞(1), on D₃
  and D₄; on B₃ recorded as found (no guess).
- **BA5 [obs]:** the depth and core tabulated for every (board, lag);
  the 4-cube's and D₅'s chains written out element by element.
- **BA6 [I]:** the reading above, recorded as a reading.

## Machinery

Stone AQ's `Minuscule` and Stone AT's `enumerate_W_np`/`pow_arr`/`inv_arr`
VERBATIM (the 41 enumerable boards; membership by row bytes; E₇ cited,
not run — the SM-062 isometry caveat is moot since nothing here uses the
criterion); Stone AV's e-coordinate machine VERBATIM for B₃, B₄, B₅;
reversers found by solving rR = R⁻¹r over W. ⟨W, R⟩ by numpy BFS where
its order is ≤ 4·10⁶. Own cache `_stone_ba_cache/witnesses_ba.json`.
Outputs: `verify_stone_ba_clifford_hierarchy.py`, `.log`,
`STONE_BA_CLIFFORD_HIERARCHY.md`. Runtime: a few minutes.

## Discipline

Compute, never assert; registered guesses resolvable INVERTED at equal
prominence; no registry/git writes by the executor. Not RH/GRH. Rule 3:
"Clifford", "Pauli", "T-gate", "hierarchy" are labels for a group
chain; no quantum circuit is claimed; nothing here is about a lepton.
