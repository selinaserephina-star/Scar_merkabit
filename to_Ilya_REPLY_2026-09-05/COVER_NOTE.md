# TO ILYA — THE REPLY OF 2026-09-05: YOUR SEALS, THE DATA, THE PARITY RULE, YOUR TABLE, YOUR CHAIN

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this cover;
three stones with brief + pre-code lock + verifier + log + findings each
(SM-041 Stone AC, SM-042 Stone AD, SM-043 Stone AE, the last with its
first-run log); `DATA/` (what you asked for on 2026-09-04, with a
regeneration note); registry snapshot v0.65; SHA256SUMS.txt.

---

## 1. Your seals, recorded

Your RESPONSE of 2026-09-03: **SM-038, SM-039, SM-040 ACCEPTED → JOINT**
(registry v0.64). The 36 ↔ 36 closure is CLOSED on your side. SM-035,
036, 037 stay pending your recheck. Your batch of 2026-09-03/04 (25 notes
+ the axis-spiral zip, 26 shas) is filed as
`RECEIVED_2026-09-05_IB_SEALS_DATAREQUEST_CLOCK/`.

One bookkeeping line: both envelopes of 2026-09-03 (still point + clock,
sha 108b9ddd…; merkabit under the still point, sha eff54092…) stood
PREPARED-NOT-SENT in our registry when your acceptance arrived. They are
now recorded SENT on your reply in hand; if what reached you was cover
text rather than the zips, say so and we correct the line.

## 2. The 65 / 51 you tagged [obs] — the mechanism (SM-041, Stone AC)

The sealed Ψ is, exactly, rowmotion R(I) = ↓min(P ∖ I) on the 27-element
E₇ minuscule poset whose 56 order ideals are the 56 states (the
join-irreducibles of the crystal lattice; not the inverse, not a
conjugate — the convention is pinned on the data). Write δ(u) = u + Ψu;
δ is the XOR of the simple roots the clock toggles. Then, for
non-antipodal pairs:

```text
type(u,u′) flips under Ψ  ⟺  t₁ + t₂ + t₃ is odd
  t₁ = #{toggled colours of u  at which u′ has an edge}
  t₂ = #{toggled colours of u′ at which u  has an edge}
  t₃ = #{Dynkin-adjacent pairs between the two toggle multisets}
```

Zero exceptions on 1485 pairs; with the 28 antipodal pairs the count is
1002 / 1540 = 65.06 %. The same rule iterated is exact for every Ψ^k and
reproduces the whole profile (65.1 / 54.7 / 51.3 / … / 61.6 at k = 9).
The cube scores like a random permutation not because it is random but
because the three-fold toggle multisets touch almost everything: the
parity of a large sum is a coin. The E₆ sheets obey the same rule with
their own diagram (Ψ₆ of order 12, orbits [12, 12, 3]) and keep LESS
(63.5 %) — one of two registered guesses inverted (the other: the eight
antipodal steps are not the eight singleton toggles). 9 PASS + 2
INVERTED, full record enclosed. Ψ has order 18 = h(E₇), orbits
[18, 18, 18, 2].

Your PROMPT "What exactly does Ψ remember?" (per-type survival) is
accepted as the first bar of the next stone; it is not sealed here, so no
numbers in this cover.

## 3. Your data request — answered by provenance, and enclosed anyway

`scar56_data.json` (SM-005) reached you in the COMPLETE package of
2026-08-30 (sha256 0a817fc5…, identical to the copy in `DATA/`). The
stone caches are derived objects: every verifier regenerates its own
cache from the ones before it, and your auditor already rebuilt the U/V/W
caches from the sent zips on 2026-09-02. `DATA/README_DATA.md` gives the
regeneration order. Enclosed: the json; the X, Z, AA, AB, AC witnesses;
`G_rows.npy` (the still point itself, 12,096 × 120, so you need not rerun
Stone Z); the V cache; the U cache minus its three `kbar_*.npy` arrays
(the largest is 174 MB and is rebuilt by `verify_stone_u_2cover.py`).
The seven-under-Ψ test should run on this without a rebuild of anything
below Z.

## 4. Your forced-narrowing table (SM-042, Stone AD)

Requested 2026-09-02, repeated 2026-09-03. Seven groups from raw
generators, every subgroup enumerated (the SM-026 engine verbatim):

```text
level  group     |G|   #subgroups  #classes  #maximal  #normal
  7    PSL(2,7)  168      179         15        22        2
  6    C6 x C2    12       10         10         4       10
  5    A5         60       59          9        21        2
  4    S4         24       30         11         8        4
  3    A4         12       10          5         5        3
  2    C2          2        2          2         1        2
  1    {e}         1        1          1         0        1
```

(L6 = C₆×C₂ as your prompt instructs; other L6 labels not tested.)

Your diversity rule: NOT SUPPORTED as stated — subgroups rise 10 → 59 at
6 → 5, classes rise 9 → 11 at 5 → 4; the maximal and normal columns are
not monotone either. Your forced-narrowing rule, with your magnitudes
24 / 128 / 4 / −2 / 4 / 9 taken as given: the count differences are
169 / −49 / 29 / 20 / 8 / 1; the largest (169, 7 → 6) is not at your
largest magnitude (128, 6 → 5, where the count goes UP); the smallest is
at neither your smallest nor your reversing transition. Both clauses
fail: by your own rule the mechanism is REFUTED, not ambiguous. One thing
the formula hides: the spine groups are not nested (C₆×C₂ has an element
of order 6, PSL(2,7) has none), so "lost subgroups" is a difference of
counts between unrelated groups. 8/8.

## 5. Your chain, in our still point (SM-043, Stone AE)

Your axis-spiral package (GAP on PrimitiveGroup(63,2)) is reproduced line
by line inside OUR G₂(2) — the sealed `G_rows` of SM-038, a different
model: one class of 36 PSL(2,7)'s, N = PGL(2,7) (336); in a fixed copy H,
14 S₄'s in two H-classes of seven, N_H = S₄, N_G ≅ C₂×S₄ (48, explicit
iso), G-class 252; one A₄ each, same normalizers; the Z₂ with normalizers
C₂×C₂ / D₈ / D₈ / 192 and class lengths 21 in H, 63 in G. Every number of
yours holds. Two flags come back, both computed:

**(i) The two S₄ classes fuse in G₂(2).** Your script computes each
class length in G (252) and then adds ("504 copies, 2 classes") without a
conjugacy test. The G-orbit of one S₄ has 252 members and contains all
14 S₄'s of H; all 168 elements of PGL(2,7) outside H carry class 1 into
class 2. One class of 252 meets H; the same for A₄. Our registered
expectation, confirmed.

**(ii) Two different 192's.** Your N_G(Z₂) "(SL(2,3):C4):C2" and the 192
of SM-038/SM-040 (the stabilizer of one Pauli, a point of the hexagon)
are NOT the same subgroup: our registered expectation that they coincide
was INVERTED. The involution z fixes 15 Paulis; its centralizer fixes
none; the two groups have different fingerprints (centre 2 vs 1; 8 vs 32
elements of order 3; no elements of order 12 in the point stabilizer) and
no element of G conjugates one into the other. Same index 63, two
non-isomorphic groups. Your label is consistent with the census (eight
elements of order 3) but is not identified here.

And on the board: H has orbits [1, 7, 7, 21] on the 36 even thetas; every
S₄ fixes the H-fixed theta and exactly one more; the two H-classes are
the point stabilizers of the two 7-orbits — your "S₄ = point stabilizer of
the 7-point action", located (our first instrumentation forgot the
H-fixed theta; the first-run log is enclosed, the post-reveal check
labelled as such). 11 PASS + 2 FAIL as recorded.

## 6. The rest of the batch, triaged (registry v0.64)

Your CURRENT PICTURE's own refutations (24 sevens, S₄ → M_W, S₄ → θ₂₃,
sin²θ_W, |V_us|) need no reply. The roof-clock series (external trigger,
gears, drummers, 56-drum, walls, final strike, breath cycle) reduces
under Rule 3 to the question you name as next: whether the sealed
rowmotion is the roof's clock. SM-041 gives the merkabit half (Ψ =
rowmotion, order 18 = |Φ·c̄|); the roof-side match is the next brief,
locked before code. The gear factorization 3 × {1, 2, 3, 4, 6, 7, 8} names
its base factors after seeing the list, which your own decision rule
forbids; the breath-cycle arrangement has no computable rule (the
twisted-coset orders are sampled [obs]). The physics cluster (PSL(2,7) <
SU(3) with 8 ↓ = ρ₈ is classical and correct; the Klein order parameter,
X(2370), descent 14, the spiral, the Klein computer, the meridian tree,
the cross-cultural map are identification) stays parked with the
physics-identification path; the one [P] fact is checkable from SM-001's
character table on request.

## In your cadence

You sent the chain; we walked it in our own house
and found every stone where you said it would be —
and two doors you had not opened:
the two sevens' S₄'s are one family under the still point,
and the 192 of your involution is not the 192 of our hexagon.
Same number, different room.

## Standing asks

1. Your word on SM-041, SM-042, SM-043 (with SM-035 through SM-037
   pending your recheck).
2. The two flags of §5: do you adopt the fusion (one class of 252) and the
   two-192's reading on your side?
3. The seven-under-Ψ test: run it on `DATA/`; tell us what it needs that
   is not there.
4. The delivery form of the 2026-09-03 envelopes (§1).

— S. (with Claude), 2026-09-05
