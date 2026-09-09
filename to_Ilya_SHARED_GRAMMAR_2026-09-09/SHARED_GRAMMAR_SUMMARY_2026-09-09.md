# THE SHARED GRAMMAR — SUMMARY (SM-057, Stone AS)

**Stenberg side · with Claude · 2026-09-09 · registry v0.97. A
self-contained statement of the results of SM-057 and what they say,
written to serve as §7.8 of `Roof_and_Clock_DRAFT.md` (after the
non-linearity theorems of §7.6 and the family table of §7.7). Every
statement is [C], computed by `verify_stone_as_shared_grammar.py`
(14/14) on the full enumeration of W(E₇) on the 56; the one [P] input is
the isometry criterion for W-membership (Aut of the E₇ weight
configuration is W(E₇)).**

---

## Setting

W = W(E₇), order 2,903,040, acting on the 56 states of the board (the
weights of the minuscule representation). W is the board's *grammar*:
every symmetry, every Weyl-invariant selection rule, every descent
marker (the involutions of a bridge PSL(2,7)), and the mirror up to one
bit, lie in it. The clock Ψ is rowmotion on the E₇ minuscule poset
(SM-041); it is not in W (SM-044) and commutes with nothing in W
(SM-054). After k ticks the grammar is the conjugate W_k = Ψ^k W Ψ^{−k},
an isomorphic copy of W inside S₅₆.

## Result 1 (what two instants share)

  W ∩ Ψ^k W Ψ^{−k} = {1}      for k = 1, …, 8 and 10, …, 17;
  W ∩ Ψ⁹ W Ψ^{−9} = {1, ι}.

Computed by conjugating every element of W by Ψ^k and testing linearity;
for k ≠ 9 the cheap necessary test (the conjugate still commutes with ι)
already leaves only the identity. The half-turn's ι is forced: Ψ⁹
commutes with ι (SM-044), and ι is central in W. Consecutive instants of
the machine share no symmetry at all; the eighteen instants are eighteen
copies of W(E₇) in S₅₆ meeting pairwise in the identity (in ⟨ι⟩ at
distance 9), all with one spectrum.

Corollaries checked directly: no reflection of W (0 of 63) is a symmetry
after any tick k = 1..17; none of the 21 involutions of a bridge
PSL(2,7) — the C₂'s of Ilya's descent — is a symmetry at any later
instant short of the full cycle. SM-054 said no marker is *fixed* by the
clock; this says no marker is even a *symmetry* one tick later.

## Result 2 (the clock is universal, the mirror is not)

  ⟨W, Ψ⟩ = A₅₆,      ⟨W, pr⟩ = 2²⁸ ⋊ Sp₆(2),      ⟨W, Ψ, pr⟩ = S₅₆.

Ψ, ι and the reflections are even permutations of the 56, pr is odd. The
clock with the grammar generates every even permutation of the states:
relative to the symmetry group, the clock is a universal gate — the
permutation-group form of "the Clifford group plus one non-Clifford gate
is universal". The mirror with the grammar generates a group of order
2²⁸·|Sp₆(2)| = 2³⁷·3⁴·5·7, and its structure is explicit: pr fixes
exactly the two poles, which form an antipodal pair; pr composed with
the swap of the poles is a Weyl element (SM-016's altitude ν(pr) = 2,
completed); W is transitive on the 28 antipodal pairs with image Sp₆(2)
and kernel ⟨ι⟩; so the normal closure of the pole swap in ⟨W, pr⟩ is the
full group of 2²⁸ pair-flips, meeting W in ⟨ι⟩, and ⟨W, pr⟩ = (2²⁸)·W.
The mirror is one Pauli-type flip times a Clifford-type element; it
lives in the sign-flip group of the 28 bitangents and cannot leave it.

## What it means

- The early resource theory of the machine — structure is free, time is
  expensive; Ψ-depth 2, W-depth 4 (SM-009..014) — is the shadow of a
  dichotomy that is now a theorem on the board: everything linear sits
  in one finite Clifford-type world, the mirror one bit outside it, and
  the clock is the single operation outside that world, universal with
  it, rewriting all of it at every step.
- What the clock preserves of the grammar is exactly what the earlier
  stones measured: the spectrum (Rush–Shi: the orbits and the period of
  a Coxeter element), and a parity's worth of the pairwise relations
  (SM-041: 65 %, by an exact rule). Nothing else: not one non-trivial
  symmetry.
- For the Scar side: a selection rule is a statement about one instant
  of the machine. A choice made in the grammar — a marker, a generation
  axis — does not exist as a symmetry at any other instant. If the clock
  is to carry such a choice, what it carries is not a symmetry but an
  orbit, and the orbit leaves the symmetry group at the first tick.

## Not claimed

Nothing about other minuscule boards (E₆'s sheets, D_n, A_n): the same
computation is possible there and is the next stone, with the registered
guess that W ∩ R^k W R^{−k} = C_W(R^k) in general (it fits every number
here, the half-turn included). The isomorphism type of ⟨W, pr⟩ beyond
"the 2²⁸ flips extended by W with ⟨ι⟩ amalgamated" is not claimed.
