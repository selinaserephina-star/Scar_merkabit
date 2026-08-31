# DRAFT — SM-019 registry row (NOT yet committed)

**Staging file. This row is NOT in `SCAR_MERKABIT_REGISTRY.md` yet.** Reasons to
hold: (1) it is a verification of Ilya's received material, not a run under a
pre-locked brief; (2) JOINT status needs Ilya to see the verification; (3) the
"level" labels must be reconciled first (Flag A below). Append on Selina's word
once (2)/(3) are settled. Filing the received files was done; that is not a send.

## Proposed row (table columns: id | unit | result | grade | artifacts)

| id | unit | result | grade | artifacts |
|---|---|---|---|---|
| SM-019 | **Mediator-descent verification** (IB's 7↔6..2↔1 chain, received 2026-08-31, filed sha in `RECEIVED_2026-08-31_IB_MEDIATOR_DESCENT/`) | Ilya's group-descent chain rebuilt from scratch (perm groups + SL(2,5)/SL(2,7) mod p): **44/44 computed checks PASS.** **6↔5:** both order-120 extensions built — A₅×ℤ₂ (split; 7 involutions, no order-4 element) and SL(2,5) (non-split; unique involution, centre {±I}, quotient A₅); the DOUBLE mediator confirmed by a clean invariant — **Dic₃ needs an order-4 element ⇒ only in SL(2,5); D₆=S₃×ℤ₂ has ≥3 involutions ⇒ only in A₅×ℤ₂** ("the mediator is doubled because the extension is doubled"); the four rejects fail for the stated reasons (S₄ no C₆; D₁₂ needs order-12 vs max 10; GL(2,3)/2O order 48 ∤ 120). **5↔4:** A₅∩S₄ = A₄ **as a set identity in S₅**; A₄ has no order-6 subgroup ⇒ only C₃ survives simultaneous membership. **4↔3:** V₄ normal in both, the unique proper nontrivial normal subgroup of A₄, S₄/V₄≅S₃. **3↔2:** A₄/V₄≅C₃, no index-2 subgroup (one-way door). **2↔1:** prime closure. **7↔6:** PSL(2,7) order 168, element orders {1,2,3,4,7} (no order-6); the rung is **our own sealed SM-003 (bitangent bridge) + SM-015 (Stone Q)** — PSL(2,7)/W(E₆) inside Sp₆(2)=W(E₇)/±, 28 bitangents, ∩=S₃=N(⟨z₃⟩), 56=2×28. Schur multiplier A₅=ℤ₂ **[P, cited]**; geometric readings + the BRIDGE-SPECIFICATION T1–T6 framework **[I], ungraded**. **TWO refutations at equal prominence:** (A) "level 6" names three different groups across the files (A₅×ℤ₂ / W(E₆) / C₆×ℤ₂) — the descent is not one tower; (B) the quantum-gap "PSL(2,7) and C₆×ℤ₂ have no common subgroup" overstates — they share ℤ₂, ℤ₃, ℤ₂²; only "no C₆ mediator" holds. | [C]/[P cited] | `verify_mediator_descent.py`, `verify_mediator_descent.log`, `RECEIVED_2026-08-31_IB_MEDIATOR_DESCENT/` (8 files) |

## Proposed changelog entry (head; append on commit)

- **v0.18 (2026-08-31)** — **Inbound from the ship: Ilya's mediator descent
  (8 files) received + filed + independently verified** (`SM-019` draft;
  `verify_mediator_descent.py` 44/44). The 7↔6 rung is our own SM-003/SM-015.
  Two flags returned at equal prominence (level-label inconsistency;
  overstated "no common subgroup"). Not yet a sealed JOINT unit — awaiting the
  level reconciliation and Ilya's sight of the verification. No send.

## Flag A — the level labels are not one tower (blocks sealing)

| step | file's "level 6" (or endpoints) | group | order |
|---|---|---|---|
| 6↔5 | level 6 = Ih | A₅×ℤ₂ (and 2I=SL(2,5)) | 120 |
| 7↔6 bridge | level 6 = W(E₆) | W(E₆) | 51840 |
| quantum gap | level 6 = C₆×ℤ₂ | C₆×ℤ₂ | 12 |

Three different "level 6"s. Either (i) the levels index a *family of pairwise
bridges*, not a chain, or (ii) one consistent tower must be chosen and the
files re-cast. This is the question to put to Ilya before SM-019 is sealed.

## Flag B — corrected quantum-gap statement

Replace "no common subgroup" with the exact fact: **PSL(2,7) has no element of
order 6, hence no C₆ mediator**; PSL(2,7) *does* share ℤ₂, ℤ₃, and ℤ₂² with
C₆×ℤ₂ (verified). The "meet only above, inside Sp₆(2)" reading then stands on
the *mediator* level, which is the intended one.

## Not-claims

Not RH/GRH. The [I] geometric readings and the T1–T6 bridge typology are
frameworks, not theorems, and are not graded. SM-019 is a verification of
received material, not a pre-registered discovery; JOINT status and any send
remain both parties' word.
