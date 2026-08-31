# Blind Bridge Classification — Independent Engine Run

Single-engine blind derivation. No preloaded labels used. Method: for each pair,
compute embedding, shared subgroups, normal subgroups, quotients, lost/appeared
types, direction, reversibility, then a class derived only from that data.

Orders: PSL(2,7)=168, C6×Z2=12, A5=60, S4=24, A4=12, Z2=2, {e}=1.
Key invariant used throughout: for any pair (G1,G2), a common subgroup H
satisfies |H| divides gcd(|G1|,|G2|). Whether the actual maximal common
subgroup *reaches* that bound turns out to be the load-bearing distinction.

---

## Pair 1 — (PSL(2,7), C6×Z2)

- **Embedding:** none, either direction. PSL(2,7) has element orders {1,2,3,4,7}
  only (no order-6 element exists in PSL(2,7)); C6×Z2 has exponent 6 and requires
  an order-6 element. 12 < 168 rules out the reverse trivially, but the real
  obstruction is the element-order mismatch, not size.
- **Shared subgroups (iso types):** {e}, C2, C3, V4. Not shared: C6 (PSL(2,7) has
  no order-6 element), C4/C7/A4/S4 (present in PSL(2,7), absent — or wrong type —
  in C6×Z2).
- **Normal subgroups:** PSL(2,7) simple → {e}, itself only. C6×Z2 abelian → all
  subgroups normal.
- **Quotients:** PSL(2,7) has none nontrivial (simple). C6×Z2 → C6, V4, C3, C2, {e}.
  No common nontrivial quotient.
- **gcd bound:** gcd(168,12)=12. Maximal common subgroup actually achieved: V4,
  order 4. **Bound not reached** (4 of 12).
- **Direction / reversibility:** none — symmetric absence of a map.
- **Derived class:** Class III — deficient indirect bridge (gap: connection exists
  only through minimal shared subgroups, well below the theoretical ceiling).

---

## Pair 2 — (C6×Z2, A5)

- **Embedding:** none, either direction. A5 element orders {1,2,3,5} — no order-6,
  no order-4 element, so C6×Z2 cannot embed; A5 too large to embed in C6×Z2.
- **Shared subgroups:** {e}, C2, C3, V4. A5's order-6 subgroup is S3 (nonabelian);
  C6×Z2's is C6 (abelian) — same order, different isomorphism type, **not** shared.
- **Normal subgroups:** A5 simple → {e}, itself. C6×Z2 abelian → all normal.
- **Quotients:** A5 none nontrivial. C6×Z2 → C6, V4, C3, C2, {e}. No overlap.
- **gcd bound:** gcd(12,60)=12. A5 does contain an order-12 subgroup (A4), but
  A4 ≇ C6×Z2, so it doesn't count as shared. Maximal common subgroup: V4, order 4.
  **Bound not reached** (4 of 12).
- **Direction / reversibility:** none.
- **Derived class:** Class III — deficient indirect bridge, structurally identical
  in kind to Pair 1 (same shared-type set {e,C2,C3,V4}, same 4/12 shortfall).

---

## Pair 3 — (A5, S4)

- **Embedding:** none, either direction. |S4|=24 does not divide |A5|=60, so S4
  cannot sit inside A5; |A5|=60 > |S4|=24 rules out the reverse.
- **Shared subgroups:** {e}, C2, C3, V4, S3, **A4**. Not shared: C4, D8 (S4 only —
  A5 has no order-4 elements at all); C5, D10 (A5 only — orders don't divide 24).
- **Normal subgroups:** A5 simple → {e}, itself. S4 → {e}, V4 (the normal Klein
  four), A4, S4.
- **Quotients:** A5 none nontrivial. S4 → S4/V4≅S3, S4/A4≅C2. No common quotient
  (A5 side is empty).
- **gcd bound:** gcd(60,24)=12. Maximal common subgroup: A4, order 12.
  **Bound reached exactly.**
- **Direction / reversibility:** no containment map in either direction, but the
  bridge is *saturated* — A4 embeds as index 5 in A5 and index 2 (normal) in S4.
- **Derived class:** Class II — saturated indirect bridge. Qualitatively different
  from Pairs 1–2: no direct containment either, but the bound is fully met, not
  merely approached.

---

## Pair 4 — (S4, A4)

- **Embedding:** A4 ↪ S4 directly, index 2, **normal**. Reverse impossible (24>12).
- **Shared subgroups:** everything in A4 — {e}, C2, C3, V4, A4 — is automatically
  in S4. S4 additionally has C4, D8, S3 (order-6 nonabelian), S4 itself — none of
  which A4 contains (A4 has no subgroup of order 6 at all, and no order-4 element).
- **Normal subgroups:** A4 ◁ S4. A4's own: {e}, V4, A4. S4's: {e}, V4, A4, S4.
- **Quotients:** S4/A4 ≅ C2 — clean quotient. A4/V4 ≅ C3.
- **gcd bound:** gcd(24,12)=12, achieved trivially since A4 ⊂ S4 outright.
- **Direction / reversibility:** one-directional embedding; the extension
  1→A4→S4→C2→1 **splits** (a transposition supplies a complement), so it is a
  genuine semidirect product S4 ≅ A4 ⋊ C2, not just an abstract extension.
- **Derived class:** Class I — direct containment, index 2, normal, split.

---

## Pair 5 — (A4, Z2)

- **Embedding:** Z2 ↪ A4, but **not normal** (A4's three order-2 elements form a
  single conjugacy class under the 3-cycles; only their union V4 is normal, a
  lone C2 is not). Reverse impossible (12>2).
- **Shared subgroups:** {e}, C2 only.
- **Normal subgroups:** A4 → {e}, V4, A4. Z2 → {e}, Z2 (trivially, abelian).
- **Quotients:** A4/V4≅C3 is the *only* nontrivial proper quotient of A4 — A4 has
  **no** quotient of order 2 (equivalently, no subgroup of index 2), so Z2 is not
  reachable as a quotient of A4 at all, only as a non-normal subgroup.
- **gcd bound:** gcd(12,2)=2, achieved trivially by the embedding itself.
- **Direction / reversibility:** one-directional, non-normal embedding, with no
  quotient counterpart in the other direction — asymmetric in a stronger sense
  than Pair 4 (which had a clean dual quotient).
- **Derived class:** Class I — direct containment, but non-normal and with no
  dual quotient map (distinguishes it from Pair 4's clean normal/quotient pair).

---

## Pair 6 — (Z2, {e})

- **Embedding:** {e} ↪ Z2 trivially; simultaneously Z2 ↠ {e} trivially (kernel =
  whole group). Both directions coincide at this pair.
- **Shared subgroups:** {e} only.
- **Normal subgroups:** {e} ◁ Z2 trivially (index 2, abelian).
- **Quotients:** Z2/{e}=Z2, Z2/Z2={e}.
- **gcd bound:** gcd(2,1)=1, achieved trivially.
- **Direction / reversibility:** terminal — subgroup and quotient relations
  coincide; this is the collapse endpoint of the whole list.
- **Derived class:** Class I — direct containment, terminal/trivial case.

---

## Summary table

| Pair | Direct embedding? | Shared/gcd bound | Class |
|---|---|---|---|
| PSL(2,7) – C6×Z2 | No | 4 / 12 (short) | III — deficient indirect |
| C6×Z2 – A5 | No | 4 / 12 (short) | III — deficient indirect |
| A5 – S4 | No | 12 / 12 (exact) | II — saturated indirect |
| S4 – A4 | Yes (normal, index 2, split) | 12 / 12 (trivial) | I — direct containment |
| A4 – Z2 | Yes (non-normal, no dual quotient) | 2 / 2 (trivial) | I — direct containment |
| Z2 – {e} | Yes (terminal) | 1 / 1 (trivial) | I — direct containment |

**Pattern that fell out of the data, unprompted:** the list is not a monotone
subgroup chain (orders go 168→12→60→24→12→2→1). The first two pairs are the
only ones where the maximal shared subgroup provably falls short of the
gcd-bound — every other pair either contains outright or saturates the bound.
That 2-pair anomaly at the top is a structural fact about these six groups,
independent of any external naming.

Ready to diff against a second independent run.
