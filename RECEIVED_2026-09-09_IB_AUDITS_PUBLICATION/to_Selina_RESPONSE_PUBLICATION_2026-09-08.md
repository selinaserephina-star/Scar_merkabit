# TO SELINA — RESPONSE ON PUBLICATION, AFTER FULL SPINE AUDIT

**From:** Ilya Balashov
**With:** Claude (independent audit sessions)
**Date:** 2026-09-08
**Subject:** the spine is computationally sound; publication is not yet ready on framing grounds

---

## 1. What we did

Independently re-ran all twelve proposed spine units from clean checkouts:

```text
SM-030  44 PASS / 0 FAIL
SM-038  19 PASS / 1 disclosed FAIL
SM-039  16 PASS / 0 FAIL
SM-040  14 PASS / 0 FAIL
SM-041   9 PASS / 2 disclosed FAIL
SM-047  15 PASS / 0 FAIL
SM-048  17 PASS / 0 FAIL
SM-049  14 PASS / 0 FAIL
SM-050  15 PASS / 2 disclosed FAIL
SM-051  15 PASS / 1 disclosed FAIL
SM-052  17 PASS / 0 FAIL
SM-053  11 PASS / 1 disclosed FAIL
```

Every disclosed failure is self-reported in the source and reproduced exactly.
No hidden error. No computational objection to the spine.

---

## 2. What that does NOT settle

Computational integrity is not the same as publishability.
A separate literature pass was run on the spine's actual claims.

Three findings control the publication decision.

---

## 3. Finding 1 — Rush–Shi (2013) is corpus-wide, not one citation

The base fact that rowmotion on an ADE minuscule poset has order equal to the Coxeter number, with cyclic sieving, is proven by:

```text
D. Rush and X. Shi,
"On Orbits of Order Ideals
of Minuscule Posets",
J. Algebraic Combin., 2013
```

This applies directly to the 56-element E₇ board used in SM-039/040/041.

The "clock ticks at the Coxeter number" framing recurs not only in SM-039/041 but across the registry synthesis lines and in the G₂ story (SM-035, where the verifier's own caveat already concedes the chain case is elementary).

Consequence: the paper needs an editorial pass across every passage that uses this framing, not a single citation added to SM-041.

---

## 4. Finding 2 — SM-041's parity rule is the strongest novelty candidate

Two targeted searches found no match for the specific mechanism:

```text
a pair of states preserves
pair type under one application
of Ψ iff

(toggled colours of one state
 active at the other)
+
(reversed)
+
(Dynkin-diagram adjacencies
 between the two toggle sets)

is even
```

This is not covered by the standard toggle-group literature (periodicity, homomesy, CSP).

Caveat stated plainly: this was two searches by a non-specialist. Before claiming novelty in the paper, this specific mechanism should be checked by someone with direct MathSciNet/zbMATH access.

---

## 5. Finding 3 — SM-053's mirror is classical

The fact that the E₆ diagram automorphism swaps the two dual 27-dimensional minuscule representations and induces an isomorphism between their posets is standard Lie theory and is explicit in the minuscule-representation literature (e.g. arXiv:2402.06732: minuscule representations "differ only by the corresponding automorphism," recoverable "up to diagram automorphisms").

What SM-053 contributes is the identification: that the specific operator pr built in this project's own machinery is this classical automorphism. That is real, but narrow.

---

## 6. Honest shape of the paper

The paper's actual contribution, as it now stands:

1. an independently verified computational model of a large and mostly classical piece of exceptional group theory;
2. one specific new mechanism — SM-041's parity rule — pending specialist confirmation;
3. identification work connecting the project's own constructed objects to the known classification.

This is publishable. It is not the same as "we discovered X, Y, Z."

---

## 7. What I need before I sign off on arXiv/OSF

1. An editorial pass across all "clock = Coxeter number" passages, with Rush–Shi cited at first use and the framing shifted to what is actually new.
2. A specialist check of SM-041's parity rule before it is claimed as novel.
3. The classical facts cited properly:
   - Rush–Shi (2013)
   - Conway (1971/1999)
   - ATLAS
   - Breuer CTblLib (already correctly cited in SM-052)
   - minuscule-representation literature for SM-053

---

## 8. What I am NOT asking for

- No new computation.
- No change to the spine's composition.
- No re-opening of sealed stones.

The spine stays. The framing changes.

---

## In your cadence

You asked whether it is time to name the first paper.
The stones are sound; I checked them all.
But the roof's clock was already chiming in Rush–Shi's paper,
and I will not sign a paper that calls an echo a first sound.

Fix the framing, check the one new rule by a specialist,
and the paper can go.

— I. (with Claude), 2026-09-08
