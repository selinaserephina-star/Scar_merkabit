# REPLY — agreed; let's fill the table jointly (Stenberg → Balashov)

**2026-08-31. Compute, never assert; a verifier for every row. Not RH/GRH.**

Ilya —

Agreed on both, and now it's settled on both sides:

- **Level 6 = C₆×ℤ₂** on the spine; the other level-6 groups (W(E₆), the
  covers) live in the parallel towers. Two towers, kept apart.
- **7↔6:** *PSL(2,7) has no element of order 6, therefore no C₆ mediator; the
  common floor {1, C₂, C₃, V₄} remains.* That's the exact statement.

And we're already partway into the table — two towers now stand machine-checked
side by side: **Tower A** (the spine's six bridges: survives / lost / appears,
`verify_bridge_transfer.py`, SM-020) and **Tower B** (the covers & bridges:
SL(2,p) Schur covers over the odd levels, `verify_tower_b.py`, SM-021).

**Yes — let's fill the full BRIDGE SPECIFICATION table jointly, a verifier for
every row.** A proposed shape so our columns line up:

1. **One row per bridge**, split into the two towers (spine rows / cover rows),
   your ten fields: left · right · type · common object · shared subgroup(s) ·
   direction · reversibility · survives · lost · appears.
2. **The computed columns** — shared-subgroup floor (= survives), lost, appears,
   direction, reversibility — come straight out of the subgroup-lattice engine
   we already have. Done for the spine; extends to the covers.
3. **The `type` field (T1–T6) as a *computed output*, not an asserted label** —
   derived from the data (does lower embed in upper? upper in lower? is there a
   mediating shared subgroup? does the quotient exist?). This honours your own
   rule — *no declaring a bridge type from one example* — by making the type a
   theorem of the row, not a name we pick.
4. **The `common object` field tagged [I]** (named / cited: "28 bitangents",
   etc.) and kept *separate* from the computed columns, per Rule 3 — so the
   geometry annotates the table without ever grading it.

On method, I'd suggest the house mode that served the Stones: **each side
implements the table independently, then we compare** — same rows, two engines,
differences become findings. Or we split the fields if you'd rather. Tell me
your row format and I'll match it exactly; or say the word and I'll send a first
full-table draft (all ten fields, both towers, every cell a verifier or an
explicit [I]) for you to check against yours.

One line I'd keep at the top of the table, since it's what the computation keeps
returning: **the common floor {1, C₂, C₃, V₄} survives every upper bridge, and
V₄ is the deepest piece to fall.** Whatever the table says, it says that.

— Selina (with Claude)

*Not RH/GRH; the wall untouched.*
