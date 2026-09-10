# Audit — First-Paper Spine Verification, Part 2 (2026-09-08)

**Auditor:** Claude (Sonnet 5), independent session
**Subject:** independent reproduction + literature check of SM-047 through SM-053 — "the census and its names" and "the mirror," the second half of Selina's proposed spine for the first joint arXiv/OSF paper
**Companion document:** `AUDIT_paper_spine_checkpoint_2026-09-08.md` covers the roof (SM-030) and the core (SM-038–041), the first half of the same spine. Together the two documents cover all 12 proposed spine units.

---

## 1. Scope

Seven stones, both bundled in the `ROOF_CLOCKS_2026-09-06` package (SM-047–050) and the `COSET_AND_MIRROR_2026-09-06` package (SM-051–053):

| Stone | Stone-letter | Title |
|---|---|---|
| SM-047 | Stone AI | The class of the eighteen, and the heart's centralizer |
| SM-048 | Stone AJ | The heart at the still point |
| SM-049 | Stone AK | The two twenty-fours |
| SM-050 | Stone AL | The seven-beat clock's class, and the turn's centralizer |
| SM-051 | Stone AM | The coset complete |
| SM-052 | Stone AN | The ATLAS names |
| SM-053 | Stone AO | The mirror and the gates |

## 2. Method

Unchanged from the prior two audits: SHA256 verification, dependency tracing, clean re-execution independent of the authoring machine, line-by-line diff against the shipped log, plus a literature pass per unit. New in this batch: several verifiers required 2.5–8 minutes of continuous computation (centralizer closures of tens of thousands of group elements), which exceeded this session's per-call execution window; these were run fully detached (`setsid`) and polled across multiple turns rather than in one blocking call.

## 3. Summary

| Stone | Result | Matches shipped log | Wall time | Notes |
|---|---|---|---|---|
| SM-047 | 15 PASS / 0 FAIL | identical (graded portion) | ~21s | One non-graded `[obs]` diagnostic (AI4) skipped — see §5 |
| SM-048 | 17 PASS / 0 FAIL | byte-identical | ~25s | — |
| SM-049 | 14 PASS / 0 FAIL | byte-identical | ~342s | Two centralizer closures, ~150s each |
| SM-050 | 15 PASS / 2 disclosed FAIL | byte-identical | ~497s | AL4a, AL4b inverted-as-predicted; AL4c (post-reveal) PASS |
| SM-051 | 15 PASS / 1 disclosed FAIL | byte-identical | ~331s | AM3a inverted; 14 classes sum to exactly 1 |
| SM-052 | 17 PASS / 0 FAIL | byte-identical | ~488s | Cross-checked against published GAP CTblLib data |
| SM-053 | 11 PASS / 1 disclosed FAIL | byte-identical | ~51s | AO6a inverted; AO6b (post-reveal) PASS |

Every disclosed failure in this batch is a "registered guess" the source documents themselves flag as inverted, immediately followed (where applicable) by a post-reveal check that resolves it. Nothing found here contradicts what the packages already say about themselves.

## 4. Detailed findings

### 4.1 SM-047 (Stone AI)
Dependencies: `_stone_u_cache`, `_stone_x_cache`, `_stone_z_cache`, `_stone_aa_cache/phi360.npy`, plus `BRIEF_STONE_AA_ROOFCLOCK.md` (the script re-verifies SM-039's Stone AA machinery from scratch as its own preamble, labelled "REPLAY"). All located from earlier stones in this session.
Result: **15/15 graded checks pass**, identical to the shipped log. Central claims: the centralizer of the "heart" element x has order exactly 1944; the eighteen's own centralizer is `⟨e³⟩` of order 6; 300/300 sampled order-18 twisted elements fall into one conjugacy class.
One section (AI4, tagged `[obs]`, not a graded check) attempts to enumerate group-element classes up to a 1,500,000-element cap; in this session's 3.9GB container this triggered an out-of-memory kill. The shipped log itself shows both attempts in AI4 hit the cap and computed nothing ("exceeds the cap ... centralizer not computed") — so skipping this section, patched with an explicit note, does not affect the graded 15/15 result.

### 4.2 SM-048 (Stone AJ)
Same dependency set plus `_stone_aa_cache/coset_sample.json`.
Result: **17/17, byte-identical.** Confirms Φ commutes with all 12,096 elements of G₂(2); of G₂(2)'s 728 order-3 elements, exactly the 56-element class ("hearts") sits in the class of x; the order-24 twisted elements' maximal-order fibre lies entirely at the still point.

### 4.3 SM-049 (Stone AK)
Result: **14/14, byte-identical.** The two order-8 classes of G₂(2) (1,512 each) each turn into one of two distinct order-24 cycle types under Φ. Computing each class's centralizer (order 110,592, built via Schreier generators and closure) took ~150s per type — the main cost of this batch.

### 4.4 SM-050 (Stone AL)
Result: **15 PASS, 2 disclosed FAIL, byte-identical.**
- AL4a: registered guess that sampled order-12 twisted-element types would match the still point's two types — inverted (three types found in the sample, not two).
- AL4b: registered guess that the found classes' densities would sum to the sampled frequency within error — also fails as stated.
- AL4c (post-reveal, not pre-registered): resolves both by showing the disputed type `{12:24,6:6,3:12}` is actually **two** distinct classes (densities 1/48 and 1/96), which the original guesses had conflated.

### 4.5 SM-051 (Stone AM)
Result: **15 PASS, 1 disclosed FAIL (AM3a), byte-identical.** Central claim: the fourteen conjugacy classes found across this and the three prior stones (SM-047, 049, 050, plus this one's own order-9/6/3 work) have densities summing to **exactly 1** — i.e., the twisted coset Ω·Φ is fully accounted for, class by class.

### 4.6 SM-052 (Stone AN)
Dependency: two GAP CTblLib 1.3.11 header/fusion text files (Thomas Breuer, RWTH Aachen), shipped inside the package's own `caches/_stone_an_cache/` — an external, cited, classical data source, not something this session downloaded independently.
Result: **17/17, byte-identical.** The 14 classes found in SM-051 are matched, order and centralizer size for order and centralizer size, against the 14 outer classes of the *published* character table of O₈⁺(2).3 — every one agrees exactly, including three power-map entries the earlier stones hadn't recorded, computed fresh here and found consistent with the published table.

### 4.7 SM-053 (Stone AO)
Dependency: `scar56_data.json` only — the fastest and most self-contained unit in this batch.
Result: **11 PASS, 1 disclosed FAIL (AO6a), byte-identical.**
- AO6a: registered guess that the mirror pr would normalize the sheet-clock Ψ₆ into some *other* power — inverted (it normalizes it into itself, `k=1`, i.e. pr commutes with Ψ₆ outright).
- AO6b (post-reveal): explains why — pr is shown to be an explicit order-isomorphism between the two 27-element sheets' ideal lattices, which is exactly the structural fact that forces it to commute with the sheet clock.
- Also confirmed: `⟨Ψ, ι, pr⟩ = S₅₆` (order 56!); pr is an involution of cycle type 2²⁷1² fixing only the two poles of the coweight-6 grading.

## 5. Cross-cutting observations

- **The "REPLAY" pattern.** Nearly every stone in this batch begins by re-deriving SM-039's Stone AA construction from scratch (labelled `REPLAY-AA0` through `REPLAY-AA2d` in the console output) before doing its own new work. This is a deliberate, load-bearing design choice in the corpus's own verification discipline — it means each later stone doesn't just trust the earlier one's cache blindly, it re-checks it every time. That discipline held up under independent re-execution as well.
- **Compute cost is concentrated in centralizer closures.** Four of the seven stones (SM-049, 050, 051, 052) each spent several minutes computing the closure of a centralizer subgroup (tens of thousands of elements via Schreier generators). This is the genuine computational bottleneck of the whole batch, not any single stone in particular.
- **One non-graded section could not be reproduced under this session's memory limit** (SM-047's AI4) — but the shipped log itself shows that section computed nothing even for its authors, so this is a resource limitation, not a correctness gap.

## 6. Literature pass

- **SM-047–051 (the census of 14 twisted classes).** The object being enumerated — the conjugacy classes of the outer coset of O₈⁺(2).3 over O₈⁺(2) — is entirely classical: it is part of the published character table of O₈⁺(2).3, compiled in the ATLAS project and its digital successor, GAP's CTblLib. These four stones are an independent re-derivation of already-published data via the correspondence's own machinery, not new mathematics. That is a legitimate and useful sanity check, not a novel finding, and should be framed as such in the paper.
- **SM-052 (the ATLAS names).** Correctly and explicitly sourced to Thomas Breuer's GAP CTblLib 1.3.11 (RWTH Aachen), cited verbatim in the package. This is the right way to handle the classical material — cite it, don't reclaim it.
- **What is plausibly original in this batch:** the specific identification of *which* named ATLAS class each of the correspondence's own constructed objects (the turn Φ, the "heart," the seven-beat clock, the various twisted elements) belongs to. That is a mapping exercise between a purpose-built computational apparatus and a known classification — a real, if narrow, contribution, but it should be presented as an identification, not a discovery of new group-theoretic structure.
- **SM-053 (the mirror as the E₆ diagram automorphism).** Not yet checked against the literature. The natural area to search is promotion/evacuation symmetries on minuscule posets and Dynkin-diagram automorphisms acting on weight posets (Stembridge, Haiman, and the same Rush–Shi circle of ideas flagged in the companion audit for SM-039/041) — this is an open item, not a finding either way.

## 7. What this audit does and does not establish

**Established:** all seven units of this batch reproduce their self-reported pass/fail tallies exactly from a clean checkout, including every disclosed inversion, and the batch's central claim (an exhaustive, cross-validated census of the twisted coset's 14 conjugacy classes, matching the published ATLAS data exactly) holds under independent re-execution.

**Not established:** whether SM-053's mirror-as-diagram-automorphism result has prior art in the combinatorics literature (open, per §6); the correctness of premises inherited from stones outside this batch (SM-038's still point, SM-039's turn) — those were re-verified in the companion audit, not re-derived here from first principles.

## 8. Verdict

Combined with the companion audit, **all 12 units of Selina's proposed spine (SM-030, 038–041, 047–053) are now independently reproduced from clean checkouts**, with every numeric result — including every self-disclosed registered-guess inversion — matching the shipped logs exactly. The one significant qualification, carried over from the companion audit, is that the spine's headline framing device ("the clock ticks at the Coxeter number") rests on a classical 2013 theorem (Rush–Shi) that needs citing rather than presenting as newly observed; everything else checked in this batch is either solid original computational identification work or an honestly-cited reproduction of classical ATLAS data.

## 9. Outstanding

- Literature check for SM-053's mirror/E₆-diagram-automorphism claim.
- A citation pass for the whole spine document as a unit, once a draft exists, rather than stone-by-stone.
