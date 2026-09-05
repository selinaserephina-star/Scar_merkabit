# DATA — what the seven-under-Ψ test needs, and how the caches regenerate

**Enclosed (byte-identical to the Stenberg lane, 2026-09-05; hashes in
`../SHA256SUMS.txt`):**

```text
scar56_data.json            SM-005, the sealed 56-machine (verts, EDGES, PSI, IOTA, COMP)
                            sha256 0a817fc5… — the same file as in the COMPLETE package of 2026-08-30
_stone_u_cache/             Stone U (SM-027/028) WITHOUT kbar_elements.npy (174 MB), kbar_orders.npy,
                            kbar_signrow.npy — everything the later verifiers read is here
                            (stab_derived_gens.npz, witnesses.json, the H_*/k0_*/we6_*/we8_* npz)
_stone_v_cache/             Stone V (SM-030), complete
_stone_x_cache/             Stone X (SM-036): witnesses_x.json
_stone_z_cache/             Stone Z (SM-038): G_rows.npy (the still point: 12,096 permutations of the
                            120 nonsingular vectors, uint8), turner_normalized.json, witnesses_z.json
_stone_aa_cache/            Stone AA (SM-039): phi360.npy, coset_sample.json
_stone_ab_cache/            Stone AB (SM-040): witnesses_ab.json
_stone_ac_cache/            Stone AC (SM-041): witnesses_ac.json
_stone_ad_cache/, _stone_ae_cache/   this envelope's stones
```

**Regeneration order (each verifier reads the caches before it READ-ONLY
and writes only its own):**

```text
verify_stone_u_2cover.py      -> _stone_u_cache/   (rebuilds the three kbar_*.npy; minutes)
verify_stone_v_we8_roof.py    -> _stone_v_cache/
verify_stone_w_third_shadow.py-> _stone_w_cache/   (not read by the stones below)
verify_stone_x_turner.py      -> _stone_x_cache/
verify_stone_z_stillpoint.py  -> _stone_z_cache/   (G_rows.npy in ~7 s)
verify_stone_aa_roofclock.py  -> _stone_aa_cache/
verify_stone_ab_merkabit.py   -> _stone_ab_cache/  (needs U, V, X, Z caches + scar56_data.json)
verify_stone_ac_parity_rule.py-> _stone_ac_cache/  (needs ONLY scar56_data.json)
verify_stone_ae_his_chain.py  -> _stone_ae_cache/  (needs Z cache only)
```

Place `scar56_data.json` and the `_stone_*_cache/` folders next to the
verifiers (the sent packages of 2026-09-01..03 carry the U/V/X/Z/AA/AB
verifiers; this envelope carries AC/AD/AE). Every verifier runs with
`python -X utf8 <name>.py` and needs only numpy (Stone U also sympy).

**For the seven-under-Ψ test specifically:** the 56-board as the 56
nonsingular u with B(u,v) = 1, the bijection to `scar56_data.json` by
Dynkin label, the PSL(2,7) copies inside G₂(2) and the Ψ permutation are
all reachable from `scar56_data.json` + `_stone_z_cache/G_rows.npy` + the
E₈-mask replay that `verify_stone_ab_merkabit.py` and
`verify_stone_ae_his_chain.py` both contain verbatim. Nothing below Z
needs to be rebuilt.
