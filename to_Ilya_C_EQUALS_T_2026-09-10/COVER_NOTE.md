# TO ILYA — C = T: THE REVERSER AND YOUR GRAMMAR (2026-09-10)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `C_EQUALS_T_SUMMARY_2026-09-10.md` — SM-062 written as §7.11 of
the draft; **SM-062 Stone AX** (brief + lock + verifier + log +
first-run log + findings + cache); the CHANNEL reply of 09-10 folded in
unchanged, with the chirality exploration and its log it promised
(`_explore_d5_chirality_2026-09-10.py/.log`, NOT sealed); registry
snapshot v1.09; SHA256SUMS.txt (LF). **Dependencies:** the verifier
loads the `Minuscule` class from SM-055's verifier file (DEFECT
envelope), the board block from SM-054's (CLOCK_CENTRALIZER envelope),
reads `scar56_data.json` (0a817fc5…) and the bridge pair from
SM-054's cache `_stone_ap_cache/witnesses_ap.json` — a copy of that
cache is in `caches/` here so the stone reruns from this package plus
the two verifier files. The W(E₇) enumeration (SM-057) and the sheet
reversal (SM-059) are copied inline, verbatim. Runtime about 100 s.

---

## 1. Why this stone

Your archive's honesty note said the model has a C — the conjugation
of the flavon representations, 3 ↔ 3̄, the outer automorphism of
PSL(2,7) — and nothing that could be called a clock. SM-059 said the
board's time reversal is the antipode, which is what charge
conjugation does to weights. So I asked the one question that could
be computed on both sides at once: what does the board's C = T do to
your grammar, and does the board carry your C at all?

## 2. What it found

**The board carries your C, all of it, and nothing more.** The
normaliser of the bridge PSL(2,7) in W(E₇) has order 672 and is
2 × PGL(2,7): every automorphism of your flavour group is a Weyl
element, and no other Weyl element normalises it. This was the
registered guess, from the projective line over F₇ (your seven plus
infinity), and it was confirmed to the element. The outer coset holds
56 involutions — 28 with eight fixed states on the 56, 28 with none —
and one PGL(2,7) complement lies inside Sp₆(2), the other outside.

**But the board's C = T and your C are different elements.** The
board's ι is central: it conjugates every state and does nothing to
any subgroup, yours included. Your C is a Weyl element c that neither
commutes with the clock nor reverses it (inside the 672, the only
reverser is ι and nothing but the identity commutes with Ψ). And your
C has no triplet to act on: the 56 restricted to your group is
2(χ₁ + 2χ₆ + χ₇ + χ₈), SM-013's erratum seen again on the 28 pairs.
It acts on the group, not on the states.

**Across the family** the reversers inside W are the coset w₀·C_W(R),
and conjugation by the reverser is the diagram automorphism: trivial
exactly on seven boards (D₄, D₆, and the 56), the 27 ↔ 27̄ flip on E₆.
One FAIL is mine: the brief counted D₈ among the boards, which is not
in the family; the number is seven, not ten, corrected post-reveal.
One thing beyond the brief that you should know for your own audits:
on five self-dual boards (A₃ ω₂, A₅ ω₃, A₇ ω₄, D₅ ω₁, D₇ ω₁) the
antipode reverses the clock but is not a Weyl element, and there the
isometry criterion for W-membership overcounts by exactly that
element. Our sealed stones use the criterion on E₇ only, where it is
a theorem; I checked.

## 3. The constraint, stated once

Any reading of your model on this board must give charge conjugation
of the states and time reversal to the same operation, and that
operation must act trivially on the flavour group. Your model has the
flavour conjugation (as the outer automorphism) and has nothing to be
the other, because it has no clock. That is either the end of the
reading or the exact shape of what it lacks. It is a computable
sentence, which is more than we had.

## 4. Standing

Your word on SM-035/036/037/054, then 055..062 at your pace; the
review of v0.2 (§§7.8–7.11 now exist as four summaries, to be merged
into v0.3 after your pass); the toggle-size homomesy against
Defant–Hopkins. No new asks. The CHANNEL reply is folded in here in
case it has not reached you on its own.

## In your cadence

The board keeps every way of turning your seven over,
and keeps one more that turns the whole board and leaves your seven alone:
that one is time running backwards,
and it does not know your name.

— S. (with Claude), 2026-09-10
