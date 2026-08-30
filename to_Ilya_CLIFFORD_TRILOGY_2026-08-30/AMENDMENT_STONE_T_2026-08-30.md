# AMENDMENT — STONE T (2026-08-30, pre-reveal)

Filed BEFORE the verifier's first run; no result has been seen.

1. **TB4 sample reduced from T-count <= 4 to T-count <= 3** (528 elements
   instead of 1,104). Reason: runtime instantiation only — the double-coset
   orbit ground truth costs 576 exact matrix products per element and the
   session's execution budget is bounded. The bar's logic is unchanged;
   the sample is still declared in the run log. Extending to k = 4 is a
   successor computation, not a design change.
2. **BFS cap instantiated at cumulative 30,000 elements**, which reaches
   K = 9 (the brief targeted K >= 7 and left K to the run's declaration —
   this item is a record of the instantiation, not a deviation).

Nothing else changes. Bars, expectations, and the locked TB3 protocol
stand exactly as in BRIEF_STONE_T_TGATE.md (sha fa6816e9...).
