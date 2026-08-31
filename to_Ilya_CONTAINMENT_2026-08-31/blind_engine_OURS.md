# BLIND ENGINE — independent derivation (second engine)

**Date:** 2026-08-31 · **Engine:** `verify_blind_engine.py` (pure Python, raw group data only) · **Log:** `verify_blind_engine.log`

**Blindness protocol:** no registry, no received documents, no prior classifications consulted. All seven groups were built from raw generators (Moebius maps on P1(F7) for the order-168 group; permutation generators for the rest). Subgroup lattices, iso types, normal subgroups, quotients, embeddings, splittings, retracts, classes: all computed. Every iso-type identification is backed by an explicitly constructed isomorphism (numbered checks in the log). **55 checks, 55 PASS, 0 FAIL.**

## Group census (computed)

| group | order | #subgroups | #conj. classes | subgroup iso-types | normal subgroups | quotient types |
|---|---|---|---|---|---|---|
| PSL(2,7) | 168 | 179 | 15 | 1, C2, C3, C2xC2, C4, S3, C7, D4, A4, F21, S4, PSL(2,7) | 1, PSL(2,7) | 1, PSL(2,7) |
| C6xC2 | 12 | 10 | 10 | 1, C2, C3, C2xC2, C6, C6xC2 | 1, C2, C2, C2, C3, C2xC2, C6, C6, C6, C6xC2 | 1, C2, C2xC2, C3, C6, C6xC2 |
| A5 | 60 | 59 | 9 | 1, C2, C3, C2xC2, C5, S3, D5, A4, A5 | 1, A5 | 1, A5 |
| S4 | 24 | 30 | 11 | 1, C2, C3, C2xC2, C4, S3, D4, A4, S4 | 1, C2xC2, A4, S4 | 1, C2, S3, S4 |
| A4 | 12 | 10 | 5 | 1, C2, C3, C2xC2, A4 | 1, C2xC2, A4 | 1, A4, C3 |
| C2 | 2 | 2 | 2 | 1, C2 | 1, C2 | 1, C2 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## P1 — (PSL(2,7), C6xC2)

*Orders (168, 12).*

1. **Embedding.** C6xC2 does **not** embed in PSL(2,7) (no subgroup of order 12 is isomorphic to C6xC2 (14 candidate subgroup(s) exhaustively tested)).
   Reverse: PSL(2,7) does not embed in C6xC2 (order 168 does not divide 12).
2. **Shared subgroup types:** {1, C2, C3, C2xC2}.
3. **Normal subgroups.** PSL(2,7): {1, PSL(2,7)} · C6xC2: {1, C2, C2, C2, C3, C2xC2, C6, C6, C6, C6xC2}.
4. **Quotients.** PSL(2,7): {1, PSL(2,7)} · C6xC2: {1, C2, C2xC2, C3, C6, C6xC2} · common non-trivial: **none**.
5. **Lost:** {C4, S3, C7, D4, A4, F21, S4, PSL(2,7)} · **Appeared:** {C6, C6xC2}.
6. **Direction:** none — no non-trivial homomorphism either way.
7. **Reversibility:** irreversible (no embedded copy has a normal complement).
8. **Class:** **SEVERED** — no monomorphism and no epimorphism in either direction; the pair touches only through shared subgroup iso-types (a shadow overlap, not a map).

## P2 — (C6xC2, A5)

*Orders (12, 60).*

1. **Embedding.** A5 does **not** embed in C6xC2 (order 60 does not divide 12).
   Reverse: C6xC2 does not embed in A5 (no subgroup of order 12 is isomorphic to C6xC2 (5 candidate subgroup(s) exhaustively tested)).
2. **Shared subgroup types:** {1, C2, C3, C2xC2}.
3. **Normal subgroups.** C6xC2: {1, C2, C2, C2, C3, C2xC2, C6, C6, C6, C6xC2} · A5: {1, A5}.
4. **Quotients.** C6xC2: {1, C2, C2xC2, C3, C6, C6xC2} · A5: {1, A5} · common non-trivial: **none**.
5. **Lost:** {C6, C6xC2} · **Appeared:** {C5, S3, D5, A4, A5}.
6. **Direction:** none — no non-trivial homomorphism either way.
7. **Reversibility:** irreversible (no embedded copy has a normal complement).
8. **Class:** **SEVERED** — no monomorphism and no epimorphism in either direction; the pair touches only through shared subgroup iso-types (a shadow overlap, not a map).

## P3 — (A5, S4)

*Orders (60, 24).*

1. **Embedding.** S4 does **not** embed in A5 (order 24 does not divide 60).
   Reverse: A5 does not embed in S4 (order 60 does not divide 24).
2. **Shared subgroup types:** {1, C2, C3, C2xC2, S3, A4}.
3. **Normal subgroups.** A5: {1, A5} · S4: {1, C2xC2, A4, S4}.
4. **Quotients.** A5: {1, A5} · S4: {1, C2, S3, S4} · common non-trivial: **none**.
5. **Lost:** {C5, D5, A5} · **Appeared:** {C4, D4, S4}.
6. **Direction:** none — no non-trivial homomorphism either way.
7. **Reversibility:** irreversible (no embedded copy has a normal complement).
8. **Class:** **SEVERED** — no monomorphism and no epimorphism in either direction; the pair touches only through shared subgroup iso-types (a shadow overlap, not a map).

## P4 — (S4, A4)

*Orders (24, 12).*

1. **Embedding.** **A4 embeds in S4**: 1 conjugate copy, 1 normal, index 2, **split** (complement of type C2). Explicit isomorphism constructed (see log).
   Reverse: S4 does not embed in A4 (order 24 does not divide 12).
2. **Shared subgroup types:** {1, C2, C3, C2xC2, A4}.
3. **Normal subgroups.** S4: {1, C2xC2, A4, S4} · A4: {1, C2xC2, A4}.
4. **Quotients.** S4: {1, C2, S3, S4} · A4: {1, A4, C3} · common non-trivial: **none**.
5. **Lost:** {C4, S3, D4, S4} · **Appeared:** none (pure loss).
6. **Direction:** A4 >--> S4 (inclusion).
7. **Reversibility:** irreversible (no embedded copy has a normal complement).
8. **Class:** **ONE-WAY SPLIT DESCENT** — second member sits inside the first as a normal, complemented subgroup, but is NOT a quotient of it: inclusion exists, projection does not.

## P5 — (A4, C2)

*Orders (12, 2).*

1. **Embedding.** **C2 embeds in A4**: 3 conjugate copies, 0 normal, index 6. Explicit isomorphism constructed (see log).
   Reverse: A4 does not embed in C2 (order 12 does not divide 2).
2. **Shared subgroup types:** {1, C2}.
3. **Normal subgroups.** A4: {1, C2xC2, A4} · C2: {1, C2}.
4. **Quotients.** A4: {1, A4, C3} · C2: {1, C2} · common non-trivial: **none**.
5. **Lost:** {C3, C2xC2, A4} · **Appeared:** none (pure loss).
6. **Direction:** C2 >--> A4 (inclusion).
7. **Reversibility:** irreversible (no embedded copy has a normal complement).
8. **Class:** **LOOSE FRAGMENT** — second member embeds only as a NON-normal subgroup and is not a quotient: no invariant copy, no projection, conjugation smears the image around.

## P6 — (C2, 1)

*Orders (2, 1).*

1. **Embedding.** **1 embeds in C2**: 1 conjugate copy, 1 normal, index 2, **split** (complement of type C2). Explicit isomorphism constructed (see log).
   Reverse: C2 does not embed in 1 (order 2 does not divide 1).
2. **Shared subgroup types:** {1}.
3. **Normal subgroups.** C2: {1, C2} · 1: {1}.
4. **Quotients.** C2: {1, C2} · 1: {1} · common non-trivial: **none**.
5. **Lost:** {C2} · **Appeared:** none (pure loss).
6. **Direction:** 1 >--> C2 (inclusion); C2 -->> 1 (projection).
7. **Reversibility:** reversible (retract exists).
8. **Class:** **RETRACT COLLAPSE** — second member embeds with a NORMAL complement: G = N x| H, so the inclusion H >--> G has a left inverse G -->> H; the step is reversible.

## Summary table

| pair | orders | embedding | shared types | common quotients | direction | reversible | CLASS |
|---|---|---|---|---|---|---|---|
| P1 (PSL(2,7), C6xC2) | (168, 12) | none (either way) | 1, C2, C3, C2xC2 | none | none | no | SEVERED |
| P2 (C6xC2, A5) | (12, 60) | none (either way) | 1, C2, C3, C2xC2 | none | none | no | SEVERED |
| P3 (A5, S4) | (60, 24) | none (either way) | 1, C2, C3, C2xC2, S3, A4 | none | none | no | SEVERED |
| P4 (S4, A4) | (24, 12) | A4 in S4 (index 2, normal, split) | 1, C2, C3, C2xC2, A4 | none | A4 >--> S4 (inclusion) | no | ONE-WAY SPLIT DESCENT |
| P5 (A4, C2) | (12, 2) | C2 in A4 (index 6, non-normal) | 1, C2 | none | C2 >--> A4 (inclusion) | no | LOOSE FRAGMENT |
| P6 (C2, 1) | (2, 1) | 1 in C2 (index 2, normal, split) | 1 | none | 1 >--> C2 (inclusion); C2 -->> 1 (projection) | yes | RETRACT COLLAPSE |

## Derived classes (definitions invented from the data)

- **SEVERED** (P1, P2, P3): no monomorphism and no epimorphism in either direction; the pair touches only through shared subgroup iso-types (a shadow overlap, not a map).
- **ONE-WAY SPLIT DESCENT** (P4): second member sits inside the first as a normal, complemented subgroup, but is NOT a quotient of it: inclusion exists, projection does not.
- **LOOSE FRAGMENT** (P5): second member embeds only as a NON-normal subgroup and is not a quotient: no invariant copy, no projection, conjugation smears the image around.
- **RETRACT COLLAPSE** (P6): second member embeds with a NORMAL complement: G = N x| H, so the inclusion H >--> G has a left inverse G -->> H; the step is reversible.

## Unprompted patterns (computed, not assumed)

- FORWARD MAPS: a forward projection G -->> H exists only in P6; a forward inclusion G >--> H exists in no pair. Backward inclusions H >--> G exist in P4, P5, P6. The chain as listed cannot be walked forward by any homomorphism until the final step.
- NO SHARED VOICE: no pair in the chain has any common non-trivial quotient. Adjacent members never project onto the same thing.
- FOREIGN BODIES: iso-types occurring in exactly ONE group of the chain: A5 only in A5; C5 only in A5; C6 only in C6xC2; C6xC2 only in C6xC2; C7 only in PSL(2,7); D5 only in A5; F21 only in PSL(2,7); PSL(2,7) only in PSL(2,7). In particular every type distinctive of the order-12 abelian member appears from nowhere in P1 and is gone by P2.
- PERSISTENT CORE: iso-types present in every group except the trivial terminus: {1, C2}. C2 survives the whole chain and is annihilated only at the last step.
- EROSION TAIL: pairs with pure loss (no appeared types): P4, P5, P6. From P4 on, the subgroup-type set only shrinks; P1-P3 each both lose and gain.
- THE CHAIN BECOMES CONCRETE AT S4: only in P4, P5, P6 is the second member actually a subgroup of the first; the first three links hold no subgroup relation in either direction despite divisible orders in P1 and gcd 12 in P2.
- ORDER-12 TWINS: the chain contains two groups of order 12 (C6xC2 and A4) which share only the types {1, C2, C3, C2xC2} and are not isomorphic (fingerprints differ: abelian vs non-abelian).

## Numbered checks

| # | check | result |
|---|---|---|
| 001 | order of Moebius group <z->z+1, z->-1/z> on P1(F7) equals 168 | PASS |
| 002 | order of C6xC2 construction equals 12 | PASS |
| 003 | order of A5 construction equals 60 | PASS |
| 004 | order of S4 construction equals 24 | PASS |
| 005 | order of A4 construction equals 12 | PASS |
| 006 | order of C2 construction equals 2 | PASS |
| 007 | order of trivial group equals 1 | PASS |
| 008 | abelian pipeline names the order-12 abelian input 'C6xC2' and an explicit isomorphism to the model C6 x C2 was found | PASS |
| 009 | Moebius group is non-abelian | PASS |
| 010 | A5 construction is non-abelian of order 60 | PASS |
| 011 | PSL(2,7): every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 012 | PSL(2,7): all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 013 | PSL(2,7): #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 014 | PSL(2,7): Sylow counts are congruent to 1 mod p for every prime | PASS |
| 015 | PSL(2,7): every quotient order equals |G|/|N| | PASS |
| 016 | C6xC2: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 017 | C6xC2: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 018 | C6xC2: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 019 | C6xC2: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 020 | C6xC2: every quotient order equals |G|/|N| | PASS |
| 021 | A5: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 022 | A5: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 023 | A5: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 024 | A5: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 025 | A5: every quotient order equals |G|/|N| | PASS |
| 026 | S4: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 027 | S4: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 028 | S4: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 029 | S4: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 030 | S4: every quotient order equals |G|/|N| | PASS |
| 031 | A4: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 032 | A4: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 033 | A4: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 034 | A4: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 035 | A4: every quotient order equals |G|/|N| | PASS |
| 036 | C2: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 037 | C2: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 038 | C2: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 039 | C2: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 040 | C2: every quotient order equals |G|/|N| | PASS |
| 041 | 1: every enumerated subgroup order divides |G| (Lagrange) | PASS |
| 042 | 1: all subgroup-class representatives identified with an explicit isomorphism (or verified abelian model) | PASS |
| 043 | 1: #(order-p subgroups) matches #(order-p elements)/(p-1) for all primes p | |G| | PASS |
| 044 | 1: Sylow counts are congruent to 1 mod p for every prime | PASS |
| 045 | 1: every quotient order equals |G|/|N| | PASS |
| 046 | PSL(2,7) construction is simple (exactly 2 normal subgroups) | PASS |
| 047 | A5 construction is simple (exactly 2 normal subgroups) | PASS |
| 048 | P1: non-embedding C6xC2 -/-> PSL(2,7) verified exhaustively over all order-12 subgroups | PASS |
| 049 | P4: explicit isomorphism between a subgroup of S4 and A4 found | PASS |
| 050 | P4: normality of the embedded copy verified by full conjugation | PASS |
| 051 | P4: splitting verified (complement K with |K||N|=|G|, K cap N = 1) | PASS |
| 052 | P5: explicit isomorphism between a subgroup of A4 and C2 found | PASS |
| 053 | P6: explicit isomorphism between a subgroup of C2 and 1 found | PASS |
| 054 | P6: normality of the embedded copy verified by full conjugation | PASS |
| 055 | P6: splitting verified (complement K with |K||N|=|G|, K cap N = 1) | PASS |

*55 checks: 55 PASS, 0 FAIL. Runtime 0.3 s.*
