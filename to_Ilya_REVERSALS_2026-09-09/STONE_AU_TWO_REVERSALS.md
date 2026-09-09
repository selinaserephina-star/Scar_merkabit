# STONE AU — THE REVERSAL THEOREM, THE SHADOW, AND THE MIRROR AS THE PRODUCT OF TWO REVERSALS

**Stenberg side · with Claude · 2026-09-09. Brief
`BRIEF_STONE_AU_TWO_REVERSALS.md` sha-locked 90061d87… BEFORE code, the
free exploration `_explore_two_reversals_2026-09-09.py` disclosed in it;
no amendment. Verifier `verify_stone_au_two_reversals.py`, log: 10 PASS +
0 FAIL, the registered guess AU5 CONFIRMED; 37 s; no first-run stop.
Machines: Stone AQ's class verbatim (42 boards); the AP board block
verbatim with `scar56_data.json` READ-ONLY; W(E₆) and W(E₇) enumerated
on the 56. Own cache `_stone_au_cache/witnesses_au.json`. Registry row
SM-059. Merkabit-side mathematics.**

## 0. Discipline

Not RH/GRH. Rule 3: "time", "reversal", "mirror", "shadow" label
rowmotion, w₀, pr and Wλ/±. The theorem is [P] with its proof in the
brief; every step and every consequence is re-checked as [C]. No
physical claim is made: "the board remembers a sign its shadow forgets"
is a statement about a double cover.

## 1. One paragraph

**Theorem.** On every simply-laced minuscule board the longest element
w₀, acting on weights as −σ (σ the diagram automorphism), reverses
rowmotion: w₀ R w₀ = R⁻¹. Proof: w₀ is an antiautomorphism of the weight
lattice (the antipode reverses the root order, σ preserves it), and any
antiautomorphism of a poset exchanges the minimal elements of complements
with the maximal elements of ideals, which is exactly the exchange of R
with R⁻¹. Checked on all 42 boards. **Corollary 1:** w₀ commutes with the
half-turn and with no other non-trivial power, which is SM-058's
half-turn survivor. **Corollary 2:** the clock never descends to the
shadow Wλ/±: R^k preserves the antipodal pair of w iff R^{2k} w = w, so
the pairs preserved at lag k are half the fixed points of the double lag
— on E₇, one pair for k = 1..8 and all 28 at k = 9, SM-044's column
re-derived. Then the 56-board itself. The sheet clock Ψ₆, rowmotion on
each 27-sheet, has its own reversal w₀(E₆) ∈ W(E₆), which reverses Ψ₆
and not Ψ; ι = w₀(E₇) reverses both; and **the mirror is the product of
the two reversals times the swap of the poles: pr = ι ∘ w₀(E₆) ∘ t,
exactly.** This names SM-016's nearest Weyl element to the mirror
(ι∘w₀(E₆), a fixed-point-free involution of W(E₇)), explains SM-053's
inverted guess (pr commutes with Ψ₆ because both its factors reverse it),
and re-reads SM-054's AP7 (pr keeps exactly a transposition's 1432/1540
because pr is an isometry times the transposition of one antipodal
pair). The registered guess that the reversers are unique — ι alone in
W(E₇) for Ψ, w₀(E₆) alone in W(E₆) for Ψ₆ — was CONFIRMED by full
enumeration.

## 2. Bars

| bar | content | outcome |
|---|---|---|
| AU0 | brief locked | PASS (90061d87…) |
| AU1 | w₀ = −σ ∈ W, top ↦ bottom, w₀ R w₀ = R⁻¹ on all 42 boards | PASS |
| AU2 | on the 12 self-dual boards, every k: pairs preserved by R^k = fix(R^{2k})/2; E₇: 1⁸, 28, 1⁸ | PASS |
| AU3a | node-7 coweight: poles ±3/2, sheets ±1/2 | PASS |
| AU3b | Ψ₆ (sheet rowmotion, poles fixed): type [12,12,3]²·1², order 12 | PASS |
| AU3c | w₀(E₆) ∈ W(E₆) on the 56 (51,840), an involution | PASS |
| AU3d | w₀(E₆) reverses Ψ₆, not Ψ; ι reverses both | PASS |
| **AU4** | **pr = ι ∘ w₀(E₆) ∘ t exactly; pr∘t = ι∘w₀(E₆) ∈ W(E₇); agreement without t 54/56** | **PASS** |
| AU5 (guess) | exactly one element of W(E₇) reverses Ψ (ι); exactly one of W(E₆) reverses Ψ₆ (w₀(E₆)) | **CONFIRMED** (1 and 1) |
| AU6 | pr commutes with Ψ₆, neither commutes with nor reverses Ψ; pr² = 1; ι, w₀(E₆), t pairwise commute | PASS |
| AU7 [obs] | ι: 2²⁸; w₀(E₆): 2²⁴1⁸; ι∘w₀(E₆): 2²⁸ linear; t: 2¹1⁵⁴; pr: 2²⁷1²; orders: w₀(E₆)·Ψ = 4, ι∘w₀(E₆)·Ψ = 585, pr·Ψ₆ = 12; two elements of W(E₇) reverse Ψ₆ (ι and w₀(E₆)) | recorded |

## 3. The three gates, named

| gate | what it is | linear? | role |
|---|---|---|---|
| Ψ | rowmotion on the E₇ minuscule poset | no (SM-044); generates A₅₆ with W (SM-057) | time |
| ι | w₀(E₇) = −1, the antipode | yes, central | the reversal of time; the only one |
| pr | ι ∘ w₀(E₆) ∘ t | no, but one pole swap from the product of the two reversals | the mirror: board reversal × sheet reversal, up to the poles |

With w₀(E₆), the reversal of the sheet clock, as the fourth object that
ties them: the mirror is what you get by reversing time on the whole
board and then reversing it again on each sheet, so that the sheets end
up going forward and only their labelling is exchanged — which is the
E₆ diagram automorphism SM-053 saw as pr's colour map.

## 4. What was learned

- **Time reversal on the board is the antipode, and it is unique.** The
  clock has exactly one reversal in the symmetry group, and it is the
  gate the machine had called chirality since SM-005. Reversing time is
  flipping every state's chirality bit.
- **The shadow has no clock.** The clock cannot act on the 28 antipodal
  pairs (it preserves one of them per tick, the axis), because its
  reversal is the map that identifies the pairs. The board can reverse
  time only because it carries the sign its shadow forgets; the shadow,
  where SM-015 found ι acting trivially, is timeless in this exact
  sense.
- **The mirror is made of reversals.** It is not a fourth kind of thing:
  it is the ratio of the board's reversal to the sheets' reversal,
  corrected at the two poles, which is why it commutes with the sheet
  clock, why it is one transposition from linear, why its kept fraction
  is a transposition's, and why it swaps the sheets with the E₆ diagram
  automorphism as its colour map. Four sealed observations (SM-016 ν = 2,
  SM-053 AO6a/AO6b, SM-054 AP7) become one identity.
- **The reversal theorem is general.** It uses nothing about E₇: on every
  minuscule board the longest element runs the clock backwards.

## 5. Not claimed

Nothing physical. Nothing about the non-simply-laced boards. Nothing
about which other antiautomorphisms of J(P) exist beyond w₀ (they all
reverse R by the same proof; whether any lies in W besides w₀ is
answered negatively here only for E₆ and E₇ by AU5). The order 585 of
ι∘w₀(E₆)·Ψ is recorded, not read.

## 6. Synthesis line

The longest word is the reversal of time, the antipode is its face on
the 56, the shadow that forgets the sign forgets the clock with it — and
the mirror, the last unnamed gate, turns out to be two reversals of time
disagreeing only at the poles.
