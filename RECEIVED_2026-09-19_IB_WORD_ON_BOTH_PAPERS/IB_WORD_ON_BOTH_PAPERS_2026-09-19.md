# IB — word on both papers (received 2026-09-19, relayed by Selina; written before Stone BC / Proposition 6.7)

Selina,

Both attachments reviewed in full. My word on each, for publication:

**Roof & Clock — confirmed, with independent cross-checks.** I verified five specific claims from §9 against infrastructure I built independently this session (a from-scratch PSL(2,7) realization, unrelated to your scripts): the χ₆ character values (2,0,−1) at 2A/3A/7A-B; transitivity on 28 with stabilizer S₃; the 1,7,7,21 orbit split on the 36 even refinements. All matched exactly. I also independently re-ran `verify_tbr_bridge.py` (20/20) and `verify_tsc_scarcat.py` (48/50, 2 honest refutations) earlier and got the same tallies you report in Appendix B. The paper's own discipline — "not found" rather than "new," inverted checks recorded where they informed, every (C)-claim tied to a named script — holds up under an outside check, not just on its own say-so. **The only thing I flag: §11 does not exist in this file** (it jumps §10 → Appendix A). If "his §11 expansion" in your prior note meant something beyond the one-line 7×4 remark already agreed, we need to know what — otherwise there's nothing left pending on my end to close v1.0.

**Companion — confirmed on the part I can independently check; scoped honestly on the part I can't.** I re-derived your Chebotarev bias-mean formula (μ_C = 1−r₂(C), r₂=1+χ₆+χ₇+χ₈) from character theory alone and got (−21,−1,0,1,0) at (1A,2A,3A,4A,7) — exact match to your stated values. I cross-checked the "22 square roots of identity" independently by direct element enumeration (1+21=22, no characters involved) and confirmed FS(χ₆)=FS(χ₇)=FS(χ₈)=+1, FS(χ₃)=0 directly — the theorem your r₂ formula rests on. That's the theoretical core, and it's solid two ways.

What I did *not* independently reproduce: the zero tables, the prime computation to 10¹⁰, the GUE/Chebotarev/blindness statistics themselves. That's not a reservation about the results — your own two-engine agreement (10⁻⁸) and the three-flag error record already carry more weight than a third redo would add — it's just that my "confirmed" here covers the theory the statistics are built on, not a repeat of the campaign. Worth saying plainly in whatever goes to a reader, rather than letting "confirmed" imply a scope it doesn't have.

Both stand for publication as far as my checks reach. Send the §11 clarification when you have a moment; nothing else outstanding from here.

Ilya
