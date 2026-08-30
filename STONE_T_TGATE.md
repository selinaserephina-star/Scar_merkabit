# STONE T — FIRST CONTACT WITH THE T GATE
**Scar_merkabit joint lane · 2026-08-30 · SM-017**
**Brief:** `BRIEF_STONE_T_TGATE.md`, sha-locked `fa6816e9…6a93` before the
verifier existed; pre-reveal amendment `AMENDMENT_STONE_T_2026-08-30.md`
(locked `4ffaed1e…`) instantiated the TB4 sample at T-count ≤ 3 and the
BFS cap at K = 9. **Verifier:** `verify_stone_t_tgate.py` — **11/11**.
**THREE fail-first logs kept** (`_FAILFIRST{,2,3}.log`): a sort sentinel,
the improper-rotation error, and the denominator-scale error — the last
two are mathematically instructive (see §5).

## §0 Discipline

Compute, never assert. The registered headline bar resolved as its own
refutation and is recorded as such; the post-hoc repair ALSO failed and is
recorded at equal prominence. Matsumoto–Amano normal forms, KMM-style
exact synthesis, and the channel representation are classical — cited,
then rebuilt from scratch and verified on range. Rule 3; not RH/GRH; no
physics. ONE LOCK.

## §1 One paragraph

The program crossed the boundary located by Stones Q and R: cheap =
Clifford, magic = the genuine T gate, group infinite. On exhaustive
1-qubit ground truth (all 36,816 Clifford+T unitaries of T-count ≤ 9 mod
phase, exact ℤ[ω] arithmetic), three things are now measured. **The
skeleton survives**: T-count layers grow exactly as 72·2^{k−1} — the same
rate-2 free-monoid geometry as the crystal's Cayley spheres 4·2^{ℓ−1}
(CN-012), and the Matsumoto–Amano words reproduce every BFS layer as a
set (uniqueness + T-optimality verified on range). **The certificate
currency does NOT survive**: the locked denominator-exponent invariant is
refuted at the first diagonal (S and T share it; 6 collisions), the
residue-refined version fails too (8 collisions), and the sde only
*brackets* T-count in a width-4 window — at n = 1 the certificate is the
normal form itself, word structure rather than entry arithmetic. **The
table shape DOES survive**: the C·U·C double-coset invariant is exactly a
channel matrix modulo proper signed permutations at canonical √2-scale —
the Clifford+T contingency table — verified perfectly on 528 elements,
where each layer k ≤ 3 is a SINGLE double coset. And at n = 3 the loop
closes: preserving the 64 phase points ⟺ Clifford, so **the bitangent
skeleton is exactly the T-free stratum**; one T gate exits it at
sup-distance 0.541. The two magics — the clock's (inside S₅₆) and T's
(off every finite skeleton) — differ in kind, which is the final honest
form of open problem #3's boundary.

## §2 Bars resolved

| bar | registered content | verdict |
|---|---|---|
| TB1 | exact ℤ[ω] ring + unitaries; \|Cliff₁\| = 24 | **PASS** |
| TB2 | BFS = MA as sets ∀k ≤ K; growth 72·2^{k−1} | **PASS** (K = 9, 36,816 elements) [classical, verified on range] |
| TB3 | locked fit/test of (sde, entry-depths) | **RESOLVED AS REFUTATION** — the registered outcome branch: invariant not single-valued even on the fit window; witnesses printed |
| TB4 | channel canon ⟺ double coset on declared sample | **PASS** (after two instructive implementation refutations; 528 elements, 4 double cosets) |
| TB5 | phase points = T-free stratum | **PASS** ([P] normalizer + [C] spot checks) |

## §3 The failed certificates (the headline, at equal prominence)

1. **Locked candidate (sde, sorted entry-depths): REFUTED.** First
   collision at the diagonal: S (T-count 0) and T (T-count 1) share
   invariant (0,(0,0,0,0)); 6 colliding invariants over the full range.
2. **Post-hoc residue refinement (adding per-entry ℤ[ω]/√2 residues):
   ALSO FAILS** — 8 colliding invariants; first witness at s = 1 maps to
   T-counts {1, 2}.
3. **What sde actually does** [obs on range]: it brackets. T-counts
   present per global sde: s=0:{0,1}, s=1:{0,1,2}, s=2:{1,2,3,4},
   s=3:{3,4,5,6}, s=4:{5,6,7,8}, s=5:{7,8,9}, s=6:{9} (range truncated
   at K=9) — i.e. k ∈ [2s−3, 2s] for s ≥ 2. Ring arithmetic gives a
   window, never the number.

**Conclusion:** at n = 1 the exact certificate is the Matsumoto–Amano
normal form — a WORD invariant, not an entry invariant. The currency
change conjectured by the brief is real, but sharper than conjectured:
even ring arithmetic is only a bracket; the certificate is syntax.

## §4 The table that survives (TB4)

Cliffords act on the 3 Pauli axes as the 24 **proper** signed
permutations; hence C·U·C double cosets = channel matrices modulo
(ROT24 × ROT24) at canonical √2-scale. Verified on all 528 elements of
T-count ≤ 3: the channel canonical form induces EXACTLY the double-coset
partition. Structure found: **each layer k = 0,1,2,3 is one single double
coset** — at n = 1, T-count ≤ 3 IS the double-coset label. This is the
genuine Clifford+T analog of SM-009's contingency tables, [C on range];
its composition calculus at n = 2 is the declared successor.

## §5 What the failures taught (kept, not hidden)

- **Improper rotations** (fail-first 2): minimizing over all 48 signed
  permutations merges cosets Cliffords cannot merge — conjugation is
  SO(3): det +1 only. The table's symmetry group is the CHIRAL
  octahedral group; chirality matters even in the bookkeeping.
- **Denominator scale** (fail-first 3): coset representatives carry
  different global sde (I at s=0, H at s=1), so channel numerators live
  at different scales; the table exists only at canonical √2-scale.
  Both errors are now theorems-about-the-invariant, verified by their
  fixes.

## §6 The skeleton theorem (TB5)

Every phase point A_c has all 64 Pauli coefficients ±1/8 (verified
exactly), so preserving the phase-point set forces mapping the signed
Pauli frame to itself — membership in the normalizer, which IS the
Clifford group by definition [P]. Spot-checks: T·A_c·T† leaves {±A_c'}
at min sup-distance 0.541. **The bitangent geometry of the joint program
is exactly the T-count-0 stratum of Clifford+T.** The 56-machine's
clock-magic never leaves S₅₆; T-magic leaves every finite skeleton at
the first gate. Open problem #3's boundary, final form: our
transportation certificates price motion WITHIN a finite skeleton;
Clifford+T pricing is motion BETWEEN skeletons, and its exact
certificates (on the range measured) are normal forms, with tables
(TB4) as the double-coset bookkeeping and sde as the bracket.

## §7 Grades

| unit | grade |
|---|---|
| ring, BFS ground truth, MA = BFS on range | [C]; MA/KMM classical, cited |
| rate-2 skeleton rhyme with CN-012 | [obs] language only |
| certificate refutations (locked + post-hoc) | refutations, recorded |
| sde bracket table | [obs on range] |
| Clifford+T table = double cosets (proper rotations, canonical scale) | [P] + [C on range] |
| single-coset-per-layer (k ≤ 3) | [C on range] |
| skeleton theorem | [P] + [C] |

## §8 Not-claims

No new Clifford+T synthesis result is claimed — MA optimality is
classical; this stone's contributions are the on-range verifications, the
two refuted certificate candidates with witnesses, the bracket table, the
verified table/coset identification with its two instructive symmetry
corrections, and the skeleton theorem's framing on the joint program's
own objects. n = 2 composition: declared successor. No physics.

## §9 Reproduce

```
python -X utf8 verify_stone_t_tgate.py   # 11 checks, ~4-6 min
```
Self-contained (numpy only; scar-data-free — the n=3 part rebuilds the
phase points from scratch).
