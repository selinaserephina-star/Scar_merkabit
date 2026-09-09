# AMENDMENT — STONE AT (2026-09-09, before any reveal)

**Locked in `AMENDMENT_STONE_AT_LOCK.sha256` before the verifier is run.
Brief lock 3f6f47b7… unchanged.**

While writing the verifier, before running it, the executor noticed that
bar AT4 of the brief overstates one clause. The brief says: "on boards
with −1 ∉ W the antipode is not a permutation of Wλ at all (it maps λ to
the dual orbit)". That is true when λ is not self-dual (D_n half-spins
with n odd; E₆ ω₁, ω₆; A_n ω_k with 2k ≠ n+1), but for the self-dual
cases with −1 ∉ W — A₃ ω₂, A₅ ω₃, A₇ ω₄ — the antipode w ↦ −w IS a
permutation of Wλ (since −λ = w₀λ lies in the orbit); it simply is not
an element of W.

The verifier therefore tests AT4 exactly as written (expected to FAIL on
those three cases, to be reported as a FAIL of the brief's wording) and
adds **AT4b (amended statement):** the antipode is a permutation of Wλ
iff λ is self-dual (−λ ∈ Wλ); whenever it is, ι R ι = R^{−1}; and it lies
in W iff −1 ∈ W. The registered predictions of AT3 are unchanged (they
depend only on whether −1 ∈ W, which was stated correctly).

No other change.
