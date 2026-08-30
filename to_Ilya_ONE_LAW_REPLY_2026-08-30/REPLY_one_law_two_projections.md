# REPLY — ONE LAW / TWO PROJECTIONS, executed
**Scar–Merkabit joint lane · 2026-08-30 · SM-018 · Stenberg · Balashov ·
with Claude**
**Your document was filed at receipt (sha adb17c49…0016) and executed the
same day under a sha-locked brief (45031dd4…7082, locked before code).
Verifier: verify_stone_s_rigidity.py, 14/14, exhaustive and exact for
n ≤ 7. Refutations at equal prominence — yours and three of ours.**

## Your rule, your verdict

```text
Both equal 3:        NO.
Do they differ:      YES — but in ONE DIRECTION,
                     and they agree exactly for n <= 5.
```

Executed on the two projections our tables support — your document's
"B_n" is the braid group, ours is the hyperoctahedral group; the braid
side has no tables here (returned below). What we CAN compare exactly:

```text
projection 1 (orientable):      S_n conjugacy classes on cycle types
projection 2 (non-orientable):  (S_2n, B_n) coset types on matchings

same index set (partitions of n), same distance d = n - #parts.
```

## What the tables say (n = 4..7, exhaustive)

```text
1. Your ladder is refuted as stated.
   Rigidity events occur at EVERY depth.
   The hardest target is not the first knot.
   It is HOME:

       identity in supp(lam, tau)  <=>  lam = tau.

   You can only come home by exact retracing.
   (Your min_support = 3, under the part reading,
    measures as 1 — the identity — for every n.)

2. Our inversion died too.
   We registered: rigidity lives at the swap.
   False. Events at every depth. Recorded.

3. The swap law, exact:

       supp(lam, swap) = cut-or-join(lam) + {lam itself}.

   Cut and join are the two orientable moves.
   The third move is the TWIST:
   a swap inside a cycle can reverse a segment
   and change nothing.
   The twist is the non-orientable move.
   It is what your projection-forgetting erases.

4. Parity.
   Upstairs (S_n): d(mu) = d(lam) + d(tau) mod 2. A law. The sign.
   Downstairs (matchings): refuted — (4) o (4) reaches (2,1,1).
   Orientability IS the parity memory.

5. The comparison, identity mechanisms excluded,
   each side inside its own soft laws:

       n=4:  events even-sector  3 = 3   EQUAL
       n=5:                      0 = 0   EQUAL
       n=6:  matchings 57 < S_n 63      DIVERGE (6 witnesses)
       n=7:  matchings 99 < S_n 102     DIVERGE (3 witnesses)

   CONTAINMENT at every n: whatever the orientable world
   reaches, the matching world reaches.
   The matching world alone owns the whole odd sector
   (6 / 15 / 105 / 219 events).

   The divergence witnesses are ALL built from all-even types:

       (2,2,2) o (2,2,2) -> (4,2)
       (3,3)   o (3,3)   -> (4,2)     ... and their symmetries.

   Upstairs these are parity-locked rigid.
   Downstairs the twist dissolves them.
```

## One law, corrected

```text
Not one threshold.
One DIRECTION:

the world that remembers its path
is the rigid one.
The world that forgets
is uniformly softer —
never harder, at any n we measured.

Your line survives, mirrored:
a permutation is what remains
when the matching forgets its twists.
```

## Returned to you

```text
1. Your B_n is the braid group. Ours is hyperoctahedral.
   Which braid table do you want built,
   and which invariant plays the coset type?
   (Classical, cited not computed: trefoil crossing 3;
    B_3 the first braid group with a knotted closure.)

2. Which translation of min_support is yours:
   the distance d, or the largest part?

3. The twist: is it your "path memory", inverted —
   the move you GAIN by forgetting orientation?
```

## Verify

```
python -X utf8 verify_stone_s_rigidity.py     # 14 checks, ~2 min
```
Brief + lock, both fail-first logs, and SHA256SUMS in this folder.
Everything ONE LOCK, sealed-not-sent, two-party rule as always.
