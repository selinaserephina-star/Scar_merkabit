# FINDING: No Natural, Independent Second Contribution to M_ν Exists — A Linearity Argument Closes Most of the Search Space at Once

**Status:** Systematic negative result, with a clean structural explanation unifying several previously-separate findings
**Key tool:** Y₂(v) and Y₃(v) are **linear** maps — this single fact, verified explicitly, shows that most "new bilinear operator" candidates are not independent physics at all, just relabeled versions of mechanisms already tested and already rejected.

---

## 1–2. Candidate-by-candidate analysis

### A. Dimension-6 Weinberg, (LLHHΦΦ)/Λ² — collapses to already-tested mechanisms

Systematically computed every self- and cross-bilinear at the established vacuum:

```text
(Phi3  Phi3 )_1 = 5.32e-06        (Phi3  Phi3 )_2 = nonzero, 240 deg   (Phi3  Phi3 )_3 = 0 EXACTLY
(Phi3' Phi3')_1 = 2.05e-02        (Phi3' Phi3')_2 = nonzero, 0 deg     (Phi3' Phi3')_3 = 0 EXACTLY
(phi2  phi2 )_1 = 3.60e-03        (phi2  phi2 )_2 = nonzero, 180 deg
```

**The "3"-channel self-bilinears vanish identically** for both Φ₃ and Φ₃′ (same single-axis obstruction as everywhere else this session). The **"1"-channel** pieces are indistinguishable from the existing m₀ constant (just another number added to it) — not new structure by definition. The **"2"-channel** pieces are nonzero and point in genuinely different directions (240°, 0°, 180° — none coincide) — but here the **linearity argument bites**: since m₂·Y₂(v₁) + m₂′·Y₂(v₂) = Y₂(m₂v₁ + m₂′v₂) exactly, **any second "2"-channel operator, regardless of which flavon bilinear produced it, is mathematically identical to simply letting the effective "2"-channel direction float freely** — which is precisely the mechanism already tested (free-φ₂-angle, and separately the channel-2/240° 5th operator) and already found to destroy axis discrimination via overfitting. **Candidate A does not introduce new physics — it re-derives already-rejected mechanisms under a new name.**

### B. Second seesaw (new field N′) — the one structurally distinct candidate, already tested and still failing

Unlike A/C/E, a seesaw contribution M_ν⊃−Y_D·M_N⁻¹·Y_D^T is **not** linear in the flavons (it's built from a matrix product and inverse) — genuinely different in kind, not reducible to the linearity argument above. **This was already tested in this session** (three variants: minimal seesaw, extended 3-Yukawa seesaw, non-universal heavy mass) — all failed to simultaneously achieve good θ₁₃/θ₂₃ fits AND favor axis (2,0); see archive §4 for the full account. Still the conceptually correct "natural second contribution" in ordinary model-building terms (many realistic neutrino models do combine two mass-generation mechanisms) — just not yet a *working* one in this specific construction.

### C. Φ₃′² in Sym²(3′)=1⊕2⊕3 — fully computed, fully exhausted

This is a special case of Candidate A, computed explicitly above: channel-3 is **exactly zero**, channel-1 degenerates with m₀, channel-2 degenerates with m₂ **by the same linearity argument** — this rigorously *explains* (not just restates) the earlier finding "channel 2 is numerically degenerate with m₂." No viable independent contribution here.

### D. Gravitational (Planck-suppressed, no flavon insertion)

A bare LLHH/M_Planck term contributes **only to the "1" channel** (no flavon direction at all) — indistinguishable from m₀ by construction, and additionally suppressed by (v_EW/M_Planck)² relative to the flavon-suppressed terms, making it numerically negligible even if included. Not a source of new structure under any circumstance.

### E. Other flavon combinations

The remaining two-flavon cross-bilinears (φ₂⊗Φ₃, φ₂⊗Φ₃′, in their "3" channels) were **already tested as 5th-operator candidates earlier this session** and found **bit-for-bit identical** to the existing m₃+m_cross combination (linear-algebra fact: those two already span the full accessible "3" channel at this vacuum). The (1′)-channel of Φ₃⊗Φ₃′ is antisymmetric — not usable in LL — by the same Λ²(3′)=3′ obstruction that ruled out Φ₃′ entering linearly in the first place. No new candidate found here beyond what's already in A/B/C.

## 3–4. Table

| Candidate | S₄ channels present | Symmetric (usable)? | Order in 1/Λ | Natural size | Viable? |
|---|---|---|---|---|---|
| A. ΦΦ dim-6 (general) | 1,2 (3 vanishes) | 1,2 only | Λ⁻² | O(ε²) | **No — collapses to already-tested free-direction mechanisms** |
| B. Second seesaw (N′) | depends on N′'s rep | yes, by construction | Λ⁻¹ (via M_N′) | model-dependent | **Structurally distinct, but already tested and failing** |
| C. Φ₃′² | 1,2 (3 vanishes) | 1,2 only | Λ⁻² | O(ε²) | **No — exhausted, degenerate with m₀/m₂** |
| D. Gravitational | 1 only | yes | M_Planck⁻¹ | negligible | **No — indistinguishable from m₀, irrelevantly small** |
| E. φ₂⊗Φ₃, φ₂⊗Φ₃′ | 3 (already used) | yes | Λ⁻² | O(ε²) | **No — already tested, redundant with m₃+m_cross** |

## Best candidate

**B (second seesaw) is the only structurally-distinct option** — everything else in A/C/D/E reduces, via the exact linearity of Y₂/Y₃, to mechanisms already tried and already found to destroy axis discrimination or duplicate existing terms. B has itself already been tested (three variants, see archive) and does not yet work either, but it remains the right *type* of extension to keep exploring (e.g., with S₄-representation content for N′ not yet tried) rather than any further degree-2 flavon bilinear.

## Verdict

```text
No candidate provides a genuine, natural, WORKING second contribution to
M_nu. More importantly, the search is now provably more complete than a
simple list of failed attempts would suggest: the linearity of Y2 and Y3
means EVERY degree-2 flavon-bilinear candidate (A, C, E, and D trivially)
reduces to one of only two possibilities -- an addition to m0 (the "1"
channel, always degenerate) or a free-floating direction in the "2" or
"3" channel (already tested via free-phi2-angle and the channel-2/240deg
operator, both destroying axis discrimination the same way).

This is a genuine structural closure, not just an exhausted list: any
FUTURE degree-2 bilinear candidate, however it's constructed, will
provably reduce to one of these same two outcomes by the same linearity
argument -- there is no need to test further degree-2 bilinears
individually.

The only way to escape this closure is to go outside the linear-Y2/Y3
framework entirely: a second seesaw (candidate B, genuinely nonlinear,
already tried and not yet working) or genuinely higher-degree (>=3)
flavon combinations not reducible to a linear re-expression, neither of
which was found to work in this session's attempts, but both remain the
only categories not closed off by this argument.
```

---

END OF FINDING
