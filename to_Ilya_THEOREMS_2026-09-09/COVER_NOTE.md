# TO ILYA — THE NON-LINEARITY THEOREMS (2026-09-09)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `THEOREMS_SUMMARY_2026-09-09.md` — the three theorems of SM-056
with proofs, written as §7.6 of the draft; **SM-056 Stone AR** with brief
+ pre-code lock + verifier + log + findings + cache
(`caches/_stone_ar_cache/witnesses_ar.json`); registry snapshot v0.92;
SHA256SUMS.txt (LF). **Cache dependencies of the verifier:** it loads the
`Minuscule` class of SM-055's verifier verbatim from that file
(`verify_stone_aq_rush_shi_defect.py`, in the DEFECT envelope you hold;
its sha256 is logged) and nothing else. Third envelope of today; nothing
in it changes the asks of the first two.

---

## 1. What this is

You asked for the right object behind SM-041's rule; SM-055 gave it 42
numbers; this stone gives it three theorems, and the proofs were written
into the brief before the code, so the verifier only re-checks what the
proofs use.

**Theorem 1.** Rowmotion on a minuscule poset is a Weyl element exactly
when the poset is a chain, the standard representation of A_n and its
dual; there it is the Coxeter element itself. One inner product: the
clock sends top to bottom and bottom to its unique cover, and an
isometry would force the top's colour to appear once in the poset,
which the classification allows only on chains.

**Theorem 2.** For even Coxeter number, the half-turn of rowmotion is a
Weyl element exactly on the chains and on the vector representations of
D_n. The clock carries the bottom up the ranks one level per tick, and
consecutive weights on that orbit have inner product fixed by the rank
sizes; an isometric half-turn forces the rank-size sequence, extended by
the top's colour count, to be periodic with half the Coxeter number,
which every other minuscule poset violates at its middle rank. On the
vector representation the half-turn is written out: it reverses and
negates the coordinates with an even number of signs. A corollary you
will recognize: the linear powers of the clock are the periods of that
sequence, so on the 56-board there are none — SM-054's C_W(Ψ) ∩ ⟨Ψ⟩ = 1
by hand.

**Theorem 3.** The kept fraction has closed forms on two families:
κ(D_n ω₁) = 1 − 2(n−1)/(n(2n−1)) and κ(A_n ω₂) = 1 − (3n²−9n+4)/C(C(n+1,2),2),
the second by writing rowmotion on 2-subsets as a rotation composed with
a permutation of 2n−1 boundary subsets and counting what it moves across
types. Both exact to n = 9. A registered guess that the ω₃ count is a
degree-4 polynomial was confirmed to n = 10.

## 2. For the draft — v0.2 enclosed

`Roof_and_Clock_DRAFT.md` **v0.2** is in this envelope and supersedes the
v0.1 you hold from the framing envelope. It differs only in the abstract,
§1 (tier three restated), §7 (new §7.6 with the three theorems and their
proofs, new §7.7 with SM-055's table), §11–13 and Appendix A; nothing in
the spine moved. Tier three now says, with proofs, for which minuscule
posets the Rush–Shi bijection is an isometry (chains), for which its
half-turn is (vectors), and what the defect is on two families; the E₇
clock is at the far end of every statement. `THEOREMS_SUMMARY_2026-09-09.md`
is the same §7.6 as a standalone note. If your review pass agrees, v0.2
is the text; if a specialist finds these in the literature, they become
citations and the tier shrinks again, which is the honest outcome either
way.

## 3. Nothing new is asked

The three asks stand in the framing envelope. This one adds SM-056 to
the table for your audit at your pace, beside SM-055.

## In your cadence

The table said it; the theorems say why.
One inner product between the top and the bottom of the poset,
and the clock cannot be linear — on the board, not even halfway.

— S. (with Claude), 2026-09-09
