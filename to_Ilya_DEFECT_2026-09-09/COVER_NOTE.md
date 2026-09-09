# TO ILYA — THE RUSH–SHI DEFECT, AND THE SUMMARY TO DATE (2026-09-09)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `FINDINGS_SUMMARY_2026-09-09.md` — all findings SM-001..055 with
grades, superseding the 09-06 summary; **SM-055 Stone AQ** with brief +
pre-code lock + verifier + log + first-run log + findings + cache
(`caches/_stone_aq_cache/table_aq.json`); registry snapshot v0.89;
SHA256SUMS.txt (LF). Companion to the framing envelope of the same day
(the draft, the framing pass, the three asks), which this one does not
repeat. **Cache dependencies of the verifier: none** — it builds
everything from the Cartan matrices; the E₇ numbers it reproduces are
compared by value to SM-041/044/054, not read from `scar56_data.json`.

---

## 1. What the stone does

Your Finding 2 said SM-041's parity rule is the one candidate for
novelty and asked what the right object is. Rush–Shi make rowmotion
conjugate to a Coxeter element; a Coxeter element is an isometry;
rowmotion, carried to the weights by the natural bijection, is not. So
the right object is the size of that failure, and it is computable for
every minuscule representation, not only E₇. Stone AQ computes it for 42
cases from the Cartan matrices alone: the fraction of pair types kept
(κ), the best pointwise agreement with a Coxeter element (a), the Hamming
distance to the nearest Weyl element (ν), and the linear centralizer.

Three things came out, two of them against our registered guesses:

- **Rowmotion is a Weyl element exactly when the poset is a chain** — the
  standard representation of A_n and its dual — and then it is the
  Coxeter element itself. Everywhere else it is not in W. Confirmed.
- **The linear centralizer is trivial everywhere else except the vector
  representations of D_n.** Our guess said trivial everywhere; the table
  said order 2 for D₄..D₇ ω₁ (with A₃ ω₂ = D₃ and D₄'s two spinors by
  triality), and the post-reveal check named the element: the half-turn
  R^{h/2} of rowmotion itself. It is a Weyl element for the vector
  family and for nothing else; for the 56-board, Ψ⁹ is not (SM-054). The
  56-board's clock is as far from linear as a minuscule clock gets.
- **The kept fraction beats the random baseline in every non-chain case**
  (confirmed) **but does not grow with rank** as we guessed: up along
  D_n ω₁ and A_n ω₂, down along the half-spins. E₆ (0.635) and E₇ (0.651)
  sit where the D₅–D₇ spinors sit.

And one thing for the record: the machine, given only C(E₇) and ω₇,
returns the sealed board's numbers — 1002/1540, 14 of 56, trivial
centralizer, [18,18,18,2] — which is an independent second derivation of
"Ψ is rowmotion" that never touches the sealed data.

## 2. What it does for the paper

§7.4 of the draft claims the rule as "not found", and §7.3 says its
content is the identification and the count. Stone AQ turns the count
into a family: 42 exact fractions, three of them with a stated law
(chains linear; vectors half-linear; the rest not). That is the object
to put in front of the specialist: "for which minuscule posets is the
Rush–Shi bijection linear, and how far from linear is it otherwise?" If
that question is in the literature, we will know where the rule lives;
if not, the table is the paper's contribution on that point. Nothing
else in the draft moves.

## 3. Nothing new is asked here

The three asks stand in the framing envelope: your word on SM-035, 036,
037 and 054; the checkpoint audit; your review pass on the draft. This
envelope adds a fifth seal to the table, SM-055, for your audit at your
pace.

## In your cadence

You asked what the rule really is.
It is the distance between a bijection and an isometry —
zero on a chain, half on a vector, and the whole way on the board.

— S. (with Claude), 2026-09-09
