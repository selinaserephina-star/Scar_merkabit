# TO SELINA — LITERATURE: TOGGLE-SIZE HOMOMESY IS A ONE-LINE COROLLARY (2026-09-10)

**Ilya's side · with Claude.**

---

Your standing ask: check the toggle-size homomesy (SM-061/Stone AW: the
number of poset elements that change status per rowmotion tick is
homomesic, mean 2|P|/h) against Defant–Hopkins before it's called yours.

**Found it. It is not new — a direct, one-line corollary of a theorem
already in the toggleability-statistics literature, not something that
needs its own proof.**

## The paper

Defant, Hopkins, Poznanović, Propp, **"Homomesy via Toggleability
Statistics"** (arXiv:2108.13227, published version in *Algebraic
Combinatorics*). Their Theorem 3.20: for **every** minuscule poset P,
the antichain-cardinality statistic is ≡ #P/(rk(P)+2) — i.e.
homomesic with mean #P/(rk(P)+2) — where rk(P)+2 is exactly the
Coxeter number h in the minuscule setting.

## The derivation (one line, using only what's already in their paper)

Toggle-size, |I △ Row(I)|, splits as (elements toggled out) ∪ (elements
toggled in) = max(I) ∪ min(P∖I). By the standard identity
|min(P∖I)| = |max(Row(I))|, this gives

```text
toggle-size(I) = antichain-card(I) + antichain-card(Row(I))
```

Their Theorem 3.20 says antichain-card is homomesic with mean #P/h.
Their own Section 2.4 states, as a triviality used throughout the
paper, that (a) a homomesic statistic composed with the map itself is
homomesic with the same mean, and (b) sums of homomesic statistics are
homomesic with summed means. Applying both to the line above:

```text
toggle-size ≡ #P/h + #P/h = 2#P/h = 2|P|/h
```

— exactly Stone AW's finding, with no computation beyond what Defant–
Hopkins–Poznanović–Propp already proved.

## Verdict

Cite Theorem 3.20 of arXiv:2108.13227 for the underlying antichain-
cardinality homomesy (itself building on Hopkins 2017 and Rush 2015 for
the uniform minuscule case, both referenced in that paper's own related-
work discussion). The toggle-size statement itself doesn't need to be
in the literature verbatim — it's forced by their Theorem 3.20 plus
elementary closure properties of homomesy they state explicitly. Present
it in the draft as a corollary of Defant–Hopkins, not as an independent
finding.

— Ilya (with Claude), 2026-09-10
