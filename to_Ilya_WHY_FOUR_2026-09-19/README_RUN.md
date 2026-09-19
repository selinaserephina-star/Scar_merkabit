# How to run

Each `SM-0xx_STONE_*/` folder is self-contained: `python -X utf8 verify_stone_*.py` from inside the folder re-checks the
brief's SHA-256 against the lock first, then every bar. No caches are read (the `witnesses_*.json` files are outputs).
Requirements: Python 3, numpy (sympy is imported by none of these four). Wall times on a laptop: SM-067 about 13 minutes
(the D9 enumeration), SM-068 about 45 seconds, SM-069 about 30 seconds, SM-070 about 3 seconds.
`SM-070_STONE_BF/_explore_bf_witness_2026-09-19.py` is the free exploration that found the theorem; it is enclosed as
provenance, not as a sealed unit.
