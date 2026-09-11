# TO SELINA — REVIEW: ROOF AND CLOCK DRAFT v0.2 (2026-09-10)

**Ilya's side · with Claude.**

---

**v0.2 is approved. Merge §§7.8–7.12 and go to v0.3.**

## What this review covers, and what it doesn't repeat

Every computational unit v0.2 cites is now independently reproduced on
this side across three audit passes: the 2026-09-08 checkpoint and
part-2 audits (SM-030, 035–041, 047–053) and this session's fresh
re-run of SM-055/056 (§§7.6–7.7). I'm not re-litigating those here —
they stand as filed. This pass is the review a co-author owes the prose
and structure on top of that: framing, claim grading, and one piece of
independent mathematical cross-checking the computational audits didn't
already do.

## Independent check performed for this review

Verified Theorem 3's two closed forms directly against your own §7.7
table, not just against the verifier's output — a different kind of
check than "does the code reproduce":

```text
kappa(D_n w1) = 1 - 2(n-1)/(n(2n-1)):  n=5,6,7 -> 37/45, 28/33, 79/91
kappa(A_n w2) = 1 - (3n^2-9n+4)/C(C(n+1,2),2):  n=4,5,6 -> 29/45, 71/105, 76/105
```
All six match the table exactly. Good — this is the kind of check a
referee would do by hand on a couple of cases; doing it on three each
leaves no reasonable doubt the closed forms and the table agree.

## Framing — no issues found

The three-tier structure (§1) is applied consistently: I did not find a
place where computed content is described as more than "identification"
when it should be "classical," or where the "not found by three
non-specialist searches" hedge (§7.4) is dropped elsewhere in the text
when a stronger claim would have been easier to write. §11's refutation
list matches what I independently confirmed in the two September 8
audits. §12's "what is not claimed" is honest and, if anything, slightly
conservative — good, for a first joint paper.

## Division of labour — yes (this was owed explicitly, not just in substance)

Yes to the proposal in FRAMING §2: you draft, I audit and hold the
literature side, including arranging the specialist MathSciNet/zbMATH
check of §7. Both names on the paper, both words before it moves. This
was already "yes in substance" per your own registry note on my brief
reply — formal word, now given in full, not just implied by doing the
audits.

## One correction for v0.3

Appendix A's last line — "SM-055... and SM-056... awaiting the second
author's word" — is now stale on this side: both are audited and
accepted (see the companion note sent with this batch). Update that
line to JOINT when you fold in v0.3; no need to hold anything for it.

## Nothing else held back

I don't have a substantive objection anywhere in the 614 lines. The
proofs of Theorems 1–3 are the kind of thing I'd want a specialist's
eyes on before final submission (as §7.4 itself asks), but nothing in
them looks wrong on inspection, and the one place I could check
independently (the closed forms against the table) came back clean.

Go ahead and build v0.3 with §§7.8–7.12 folded in.

— Ilya (with Claude), 2026-09-10
