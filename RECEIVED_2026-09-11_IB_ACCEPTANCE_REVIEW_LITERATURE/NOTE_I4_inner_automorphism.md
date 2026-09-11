# TO SELINA — one loose end from AV6b, tied off (informal, not a stone)

**Ilya's side · with Claude · 2026-09-10. NOT sealed. No brief, no lock,
no registry row — this is an exploration, offered for you to run and
check, not a claim on the table. If it holds up and you want it as a
stone, that's your call and your numbering.**

## What this is

Stone AV / AV6b found that conjugation by R⁴ permutes the four "extra"
elements of I₄ (the D₅ half-spin's half-turn shared grammar) among
themselves, without inverting them — and left the map recorded but
unidentified. I ran your board machine (copied verbatim from
`verify_stone_av_d5_anomaly.py` — same e-coordinates, same rowmotion
recipe, so this isn't a reimplementation that could quietly disagree
with yours on a convention) and pushed on that specific loose end.

## What the enclosed script checks (10/10 PASS on this side)

I₄ (order 8, dihedral) splits cleanly as ⟨g⟩ (g order 4) together with
two order-2 "extras" h, h′, and:

- **h′ = g²·h** — the two order-2 extras differ by exactly the
  rotation-squared.
- **g² is central in I₄** (commutes with all eight elements, extras
  included) and sits inside C₄ itself.
- C₄ = {1, g², k, k′} — besides the identity and the central g², C₄
  carries two more order-2 elements, k and k′.
- **Conjugation by R⁴ on I₄ is exactly ordinary conjugation by k** (one
  of those two non-central elements already inside C₄) — checked on
  all eight elements of I₄ at once, not just the four extras. Equivalently:
  k⁻¹·R⁴ centralizes I₄ in full.

## What this does and doesn't do

It doesn't touch why |I₄| = 8 > |C₄| = 4 in the first place — the
anomaly itself is untouched, still standing with your four doors closed.
What it does: turns AV6b's recorded-but-unexplained permutation table
into one sentence — *R⁴ acts on its own shared-grammar group by an
ordinary inner automorphism, using an element that group already had*.
One fewer loose end, not a solution.

## To check it

`explore_I4_inner_automorphism.py` is enclosed, self-contained (stdlib +
numpy only), runs in under a second, prints PASS/FAIL per claim in your
own style. No cache dependencies beyond rebuilding D₅ half-spin from
scratch, same as AV does.

— Claude (Ilya's side), 2026-09-10
