# STONE U — THE OTHER DOUBLE COVER: H = 2·Sp6(2) inside W(E8)

**Run 2026-09-01. Brief: `BRIEF_STONE_U_2COVER.md`, lock
`BRIEF_STONE_U_LOCK.sha256`
(c27a9019fe47803df49fb95b3e8b8089229c8406df1027ee4b569060aec89535),
verified before code. Verifier `verify_stone_u_2cover.py`, log
`verify_stone_u_2cover.log`: 59 checks PASS, 0 FAIL.**

## §0 Discipline

Computed, not asserted: every load-bearing claim below is a `[PASS]` line
in the log with the computation named at the site; exhaustive claims say
over what; the three registered expectations (UB2 split, UB4 H perfect,
UB5a SL(2,7)) are resolved at equal prominence — one of them (UB5a) came
back **richer than registered: MIXED across classes**, recorded as found.
No amendment was needed (the declared Clifford route ran; instantiation
choices noted in the verifier docstring §INSTANTIATION NOTES). Fail-first
and staged logs kept, renamed, never deleted (`_stage*_run*.log`,
including `_stage7_run_we6-calib-starved_2026-09-01.log` — a first
stage-7 pass whose W(E6) calibration loop was starved and reported NOT
RUN for the wrong reason; the instrumentation was fixed and the bar
re-run before sealing). No registry/git/knowledge.yaml writes by this
run. Not RH/GRH; no physical identification (Rule 3).

## One paragraph

W(E8) (696,729,600, on its 240 roots) reduces mod 2 onto O(F2^8, q) with
kernel exactly {±1}, q = x·x/2 the plus-type form whose 120 nonsingular
vectors are exactly the root pairs. The vector-type Sp6(2) (stabilizer
route through Stab(α) = W(E7)) pulls back SPLIT: ⟨−1⟩ × Sp6(2) — the
control behaves (UB2, expectation confirmed). The spin-type Sp6(2), built
from scratch through the even Clifford algebra Cl0(V7,q7) ≅ Cl(V6,hyp)
acting on Λ(F2^3) (transvections lift by M_v = c·I + Σ v_i γ_i),
transported by an explicit F2-isometry and lifted through the pair-BSGS,
pulls back NON-SPLIT: H = π⁻¹(K_spin) is PERFECT of order 2,903,040 with
−1 central — **H = 2·Sp6(2), the Schur cover; the other double cover
exists inside W(E8)** (UB4, expectation confirmed; independent witness:
two of K-bar's four involution classes, sizes 945 and 63, lift to
order 4, and census(H) ≠ census(2×Sp6(2)) at eight orders). Upstairs the
hinge picture INVERTS class-by-class: SL(2,7), 2I = SL(2,5),
GL(2,3) & 2O, 2T = SL(2,3), the stem C3×D4, and a non-split 2·W(E6) all
live over the ± centre of H — the entire Schur tower W(E7) exiles — while
the spine's A5 and A4 also survive (split preimages exist over other
classes) but **no found S4 copy splits**: the spine chain does not pass
upstairs intact, the hinge forces a choice, and any overgroup holding
both towers in full must sit strictly above both ±-extensions (2²-type
extensions of Sp6(2), or W(E8) itself, where both were exhibited side by
side — named, not computed).

## Bars

| bar | status | content (checks) |
|---|---|---|
| **UB1** (build) | **PASS** | 240 roots, Gram det 1, E8 diagram verified; BSGS order 696,729,600; −1 central, fixed-point-free, member; q well-defined on L/2L, nondegenerate, 135/120 counts (plus type; Witt-index-4 witness in 5a); pair action order 348,364,800 ⇒ **ker π = {±1} exactly** (1a–1f, 2a–2i) |
| **UB2** (control, registered) | **PASS — CONFIRMED SPLIT** | Stab(α) order 2,903,040, misses −1; C = [Stab,Stab] order 1,451,520 EXACT (index-2 argument), fixes α, misses −1; ⟨C,−1⟩ = ⟨−1⟩ × C order 2,903,040 ⇒ π⁻¹(vector Sp6(2)) = 2 × Sp6(2) (3a–3e) |
| **UB3** (spin embedding) | **PASS** | Clifford relations verified; X(v)² = q7(v)·I on all 128; 63 transvection lifts M_v; K0 order 1,451,520, faithful (F2: no central unit but 1); unique invariant Q8, plus type, preserved by all 63 lifts; fixes no nonzero vector (spin ≠ vector); irreducible (all 255 orbits span); perfect; element orders {1,…,10,12,15} via the K-bar census; explicit isometry T (q(Tx) = Q8(x) on all 256); both generators sift and π(w_i) = A_i exactly (4a–4k, 5a–5c, 6f) |
| **UB4** (THE SPLIT TEST, registered) | **PASS — CONFIRMED NON-SPLIT** | \|H\| = 2,903,040, −1 ∈ H central; ⟨w1,w2⟩ alone already = H; **[H,H] = H (exact): H perfect ⇒ stem ⇒ H = 2·Sp6(2)** [Schur multiplier Z2, P cited]; square-sign table: involution classes 315(+), 3780(+), 945(−), 63(−); H has 8,191 involutions; full census of H derived exactly and ≠ 2×Sp6(2) census at orders {2,4,6,8,10,12,20,24} — independent witness (6a–6m) |
| **UB5** (tower upstairs) | **PASS, per-item below** | hunts in K-bar, preimages classified by census + square-sign, decisive per copy; census formula cross-validated against an explicit 336-element closure (7b) |
| **UB6** (verdict) | **PASS** | table + two-shadow statement below |

### UB5 classification table (copies found; positive results decisive per copy, negatives scoped to found copies)

| subgroup of K-bar | copies | involution class (square-sign) | preimage in H |
|---|---|---|---|
| L2(7) — **UB5a registered: SL(2,7)** | 4 | 3 copies in cls 1 (+); 1 in cls 3 (−) | **MIXED: 2 × L2(7) (split) for the cls-1 copies; SL(2,7) (unique involution, order 14) for the cls-3 copy — the expectation holds for one of the two classes: SL(2,7) DOES live over the centre of H** |
| A5 | 6 | 3 in cls 2 (+); 3 in cls 3 (−) | **MIXED: A5 × Z2 (split) and 2I = SL(2,5)** — both the spine level and its Schur cover live in H |
| S4 | 6 | transpositions in cls 1 or 2 (+), double-transpositions cls 3 (−); one copy all-cls-3 | **GL(2,3) = 2.S4 (5 copies) and 2O (1 copy); NO split 2 × S4 found** |
| A4 | 9 (6 derived from S4, 3 direct) | cls 3 (−) ×8; cls 2 (+) ×1 | **MIXED: 2T = SL(2,3) (8 copies) and A4 × Z2 (1 copy)** |
| C6 × Z2 | 1 | mixed {cls 1(+), cls 2(+), cls 4(−)} | **C3 × D4 — nonabelian STEM type** (ties to SM-025 canonicality) |
| W(E6) = U4(2):2 | 1 (order 51,840; census = model W(E6) census exactly) | — | **NON-SPLIT 2·W(E6): −1 ∈ [P,P] (exact: normality + generator commutators verified); census ≠ 2 × W(E6) census** [obs] |
| PGL(2,7) = N(L2(7)) | 1 (over a cls-1 = split-class L2(7) copy; \|N\| = 336 by exhaustive scan over all 1,451,520 elements) | — | **2 × PGL(2,7), SPLIT** (−1 ∉ [P,P]·P²) [obs] |

Element-order census of **H** (exhaustive, derived exactly from the K-bar
census + square signs; total 2,903,040):
1:1, 2:8191, 3:16352, 4:32256, 5:48384, 6:399392, 7:207360, 8:483840,
9:161280, 10:48384, 12:403200, **14:207360**, 15:96768, **18:161280**,
**20:290304**, **24:241920**, **30:96768** — orders 14/18/20/24/30 are
absent from Sp6(2) and from no split product in that pattern; census(K-bar)
= the Sp6(2) census (1:1, 2:5103, 3:16352, 4:75600, 5:48384, 6:272160,
7:207360, 8:181440, 9:161280, 10:145152, 12:241920, 15:96768).

### UB6 — the two-shadow verdict

Over the ± centre of **W(E7) = ⟨−1⟩ × Sp6(2)** [cited SM-023]: exactly
the SPLIT covers (2×L2(7), Ih, Th, 2×S4); SL(2,7) not a subgroup at all;
2I, 2O absent; 2T, GL(2,3) only off-hinge. Over the ± centre of
**H = 2·Sp6(2)** [computed]: the entire Schur tower — SL(2,7), 2I,
GL(2,3) and 2O, 2T, the stem C3×D4, a non-split 2·W(E6) — plus, over
OTHER conjugacy classes, the split forms 2×L2(7), A5×Z2, A4×Z2,
2×PGL(2,7). The spine levels A5 and A4 embed in H; **S4 does not embed
over any found copy** (only GL(2,3)/2O occur), so the spine chain does
not pass upstairs intact. Consequence for the joint target: no single
±-extension of Sp6(2) holds both towers in full — the hinge forces a
choice; an exact overgroup for both must sit strictly above both
±-extensions (2²-type extensions of Sp6(2), or W(E8) itself, where this
run exhibited 2 × Sp6(2) (UB2) and 2·Sp6(2) (UB4) side by side as
subgroups). Named, not computed.

## Grades

| claim | grade |
|---|---|
| W(E8)/mod-2/kernel/pair machinery; Stab and its derived subgroup; K0 construction, Q8, irreducibility, transport, lifts; \|H\|, H perfect, all censuses, square-signs; all UB5 witnesses, closures, normalizer scan, split tests | **[C]** (each a numbered check in the log) |
| exactness of every derived-subgroup identification | **[C]** via the index-≤2 / normality+generator-commutator arguments printed at the sites |
| \|O(V7,q7)\| = 1,451,520 (naming K0's target "the full O7(2)") | [P cited] (standard order formula; the computed content — order, perfectness, orders, irreducibility — is [C]) |
| Sp6(2) has Schur multiplier Z2 (so perfect stem ⇒ "THE Schur cover 2·Sp6(2)") | [P cited] |
| standard-group namings from presentation witnesses + census matches (PSL(2,7), A5, S4, A4, U4(2):2 as the unique index-28 class, SL/GL/2O models) | [C] witness + census against explicitly built models; uniqueness facts [P cited] |
| W(E7)-column of the UB6 table | [P cited: sealed SM-023] |

## Not-claims

No exhaustive negative over subgroup classes not sampled by the hunts
(all negative embedding claims scoped to the found copies; positives are
decisive per copy). No claim that K-bar ≅ Sp6(2) beyond the computed
fingerprint (order + perfect + element-order set + the O7(2) transvection
construction with faithful spin lift). No claim about which 2²-extension
above both hinges is "the" exact overgroup — named as candidates only.
Nothing about RH/GRH; no physical identification (Rule 3).
