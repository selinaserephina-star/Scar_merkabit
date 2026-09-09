# TO ILYA — THE SHARED GRAMMAR (2026-09-09, fourth envelope of the day)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `SHARED_GRAMMAR_SUMMARY_2026-09-09.md` — the results of SM-057 and
what they say, written as §7.8 of the draft; **SM-057 Stone AS** with
brief + pre-code lock + verifier + log + findings + cache
(`caches/_stone_as_cache/witnesses_as.json`) and the disclosed free
exploration that preceded the brief (`_explore_clock_universal_2026-09-09.py`,
NOT sealed); registry snapshot v0.97; SHA256SUMS.txt (LF). **Cache
dependencies of the verifier:** the board block is loaded verbatim from
SM-054's verifier file (`verify_stone_ap_clock_centralizer.py`, in the
CLOCK_CENTRALIZER envelope you hold; sha logged), the bridge pair from
`_stone_ap_cache/witnesses_ap.json` (same envelope), and
`scar56_data.json`; nothing else. No new asks.

---

## 1. The question, and the answer

You wrote that you would review the draft tomorrow. This envelope is
the one result I would want in front of you while you read, because it
is the sentence the whole paper has been circling.

The Weyl group W(E₇) on the 56 is the board's grammar — your selection
rules, your descent markers, the mirror up to one bit, all of it. The
clock is not in W and commutes with nothing in W (SM-054). So after k
ticks the grammar is the conjugate Ψ^k W Ψ^{−k}. **How much do two
instants share?** Computed exactly, by conjugating all 2,903,040 Weyl
elements and testing linearity: **nothing.** W ∩ Ψ^k W Ψ^{−k} is the
identity for every k from 1 to 17 except the half-turn, where it is
{1, ι} — and ι is forced, since Ψ⁹ commutes with it. The registered
guess said exactly this and was confirmed.

Consequences you will care about: no reflection of W is a symmetry one
tick later; none of the 21 C₂'s of a bridge PSL(2,7) — your markers — is
a symmetry at any later instant short of the full cycle. SM-054 said the
clock fixes no marker. This says a marker is not even a symmetry at the
next instant. A choice made in the grammar does not exist, as a
symmetry, at any other time.

## 2. The two gates placed

With the grammar, the clock generates every even permutation of the 56:
⟨W, Ψ⟩ = A₅₆. The clock is universal relative to the symmetry group —
the permutation-group form of "Clifford plus one non-Clifford gate is
universal". With the grammar, the mirror generates the sign-flip group
of the 28 bitangents, 2²⁸ ⋊ Sp₆(2), because pr is a Weyl element
composed with one swap of the two poles (SM-016's altitude 2, now a
structure theorem). Mirror: one Pauli-type flip times a Clifford-type
element. Clock: the T-gate. ⟨W, Ψ, pr⟩ = S₅₆.

So the machine's oldest slogan, structure is free and time is expensive,
is a dichotomy with proofs on both sides. What the clock keeps of the
grammar is what the earlier stones measured — the spectrum (Rush–Shi)
and a parity's worth of the pair relations (SM-041) — and not one
symmetry besides.

## 3. For the draft

The summary is §7.8; with §7.6 (SM-056) and §7.7 (SM-055) it completes
tier three: when the Rush–Shi bijection is an isometry, how far it is
otherwise, and what survives between instants. v0.3 will carry it if
your pass on v0.2 agrees.

## 4. Next on our side, for your information

The same computation on the other minuscule boards, with the guess
registered that what survives k ticks is exactly the centralizer of
R^k in W. Stone AR already says where it must fail to be trivial: on
chains everything survives, on the vector representations everything
survives the half-turn.

## In your cadence

Eighteen grammars, one spectrum, no shared word:
the clock is the one gate that is universal,
and universality here means that nothing is kept
except the count of what returns.

— S. (with Claude), 2026-09-09
