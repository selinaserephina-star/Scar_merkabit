# TO ILYA — THE ANOMALY BY HAND, AND THE DOUBLED CLOCK (2026-09-10)

**Stenberg side · with Claude. Status: SEALED (PREPARED; the send is
Selina's word, recorded in the registry when made).** Package: this
cover; `ANOMALY_BY_HAND_SUMMARY_2026-09-10.md` — SM-063 and SM-064
written as §7.12 of the draft; **SM-063 Stone AY** and **SM-064 Stone
AZ**, each with brief + lock + verifier + log + first-run log +
findings + cache; registry snapshot v1.14; SHA256SUMS.txt (LF).
**Dependencies:** both verifiers load, verbatim by slice, the
e-coordinate board machine from SM-060's verifier file (ANOMALY_HOMOMESY
envelope), the `Minuscule` class from SM-055's (DEFECT envelope) and the
numpy enumeration from SM-058's (REVERSALS envelope); both read
SM-058's table `_stone_at_cache/table_at.json` — a copy is in
`caches/` here, so the stones rerun from this package plus those three
verifier files. Runtimes 250 s and 110 s.

---

## 1. Why these stones

Your memory-channel note read SM-058's D₅ anomaly as a channel rather
than a defect, and the CHANNEL reply tested the half of it that could
be tested. What neither of us had was a reason the anomaly exists.
SM-060 had cornered it on the sixteen corners of the 4-cube and closed
four explanations; the handoff map called it "computed, not
understood". Stone AY is the understanding, derived by hand before any
code and then checked. Stone AZ is the thread AY left loose, closed
the same way.

## 2. What they found

**The half-turn is a Weyl element on one orbit.** On the 4-cube the
clock has two orbits of eight. On the orbit that does not contain the
highest weight, the half-turn R⁴ coincides with −τ, an element of its
own centralizer; on the other orbit it coincides with no Weyl element
at all. That orbit affinely spans F₂⁴, so a Weyl element is known by
what it does there — and from that one fact the whole anomaly follows
by a three-line lemma: the shared grammar is the Weyl centralizer of
the correction (−τ)R⁴, eight elements, twice C₄, and the half-turn
acts on it as conjugation by τ. Every fact SM-060 recorded about the
four extras is now derived: the two reflections swap, the two
4-cycles invert, and an extra commutes with the half-turn up to the
antipode. The D₅ lag-3 survivor falls to the same lemma with the
nearest Weyl element. And the anomaly lives on B₄, where −1 is
central: it has nothing to do with D₅'s non-central reverser.

**The vector boards' grammar is the centralizer of the doubled clock.**
Wherever an involution centralizes W and reverses the clock (the
boards with −1 ∈ W, and the five whose antipode is not a Weyl
element), I_k ⊆ C_W(R^{2k}), three lines. On the D_n vector boards it is
an equality, because the transport commutes with the antipode and has
even sign on the 2n points. That makes SM-058's "gcd(k, n−1) pattern"
on the vectors a theorem, and it says what the transports that no
Weyl group realises are: the clock trades two negative j-cycles for
one positive 2j-cycle — a transposition for a double flip on D₃ — which
no signed permutation can copy. At the lags coprime to n − 1 the
grammar is dihedral of order 2(n−1); for n odd the clock acts on it
as the outer automorphism swapping the two reflection classes, for n
even as conjugation by the half-turn itself.

## 3. One error of mine, at full size

Stone AY's brief stated a "Lemma A": the shared grammar is the union
of the Weyl centralizers of the corrections R^k w⁻¹. The proof was
wrong — it read "the transport lands in W" as "the transport is
conjugation by a Weyl element", which is the easy direction only. The
inclusion holds; equality holds exactly when every transport is
W-conjugate to its element, which is true on B₄ and D₅ and false on
B₃, A₃ω₂ and the odd D_n vectors. The machine caught it (the first run
hung on the impossible cover the error produced; that log is in the
package). Nothing else in either stone used the false statement; the
mechanism rests on Lemma B, which is proved. It is in the registry row
and the summary as a FAIL beside the passes, per the house rule. Your
audits should not need the union identity anywhere.

## 4. Standing

Your word on SM-035/036/037/054, then 055..064 at your pace; the
review of v0.2 (§§7.8–7.12 now exist as five summaries, to be merged
into v0.3 after your pass); the toggle-size homomesy against
Defant–Hopkins; your answer on the discriminant audit. No new asks.

## In your cadence

The board turns over, and for half of it the turning is one of its own;
the other half it borrows, and pays back with a double flip.
Where the only mirror is the antipode, two instants share
what the clock at double speed keeps — and nothing more.

— S. (with Claude), 2026-09-10
