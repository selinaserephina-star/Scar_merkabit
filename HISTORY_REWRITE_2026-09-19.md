# HISTORY REWRITE — 2026-09-19

On Selina's word ("sort the old history issue"). GitHub refused every push since registry v0.30 because
`_stone_u_cache/kbar_elements.npy` (166.11 MB, added at v0.31 on 2026-09-01) exceeds the 100 MB file limit.
The 125 local commits after the remote head `5c7b31d` were rewritten with `git filter-branch --index-filter
'git rm --cached _stone_u_cache/kbar_elements.npy'`; the file is now gitignored and kept locally (it is
regenerable by Stone U's verifier). Pushed history (up to `5c7b31d`) is untouched. The pre-rewrite branch is
kept locally as `backup/pre-rewrite-2026-09-19` (never pushable). Commit messages, contents and order are
unchanged; only the hashes are. Registry and memory entries that cite the OLD short hashes map as follows
(newest first).

| old | new | subject |
|---|---|---|
| c3d4030 | c124bf4 | v2.0: Proposition 6.13's antipode identity cited to Theorem 5.1 and Lemma 3.1 (was Corollary 5.2) |
| b05e508 | 7e8e5c6 | registry v1.39: Stone BF executed and sealed (SM-070) - WHY FOUR, the commutation theorem: w_n = -(e2e3)(e4e5) |
| fabdca9 | 9c321e7 | registry v1.38: Stone BE executed and sealed (SM-069) - the 16-cube at the orbit level: free clock 32^2048, O1 |
| 986a237 | 9d9c063 | registry v1.37: Stone BD executed and sealed (SM-068) - the half-turn criterion: the shared grammar at the hal |
| 985680e | 66ceb54 | registry v1.36: IB's word for publication on Roof & Clock v2.0 (pre-Prop 6.7) received and filed; his "sec 11  |
| e4731d9 | 81ee242 | registry v1.35: Stone BC executed and sealed (SM-067) - the 4-cube anomaly does NOT recur on the 8-cube: I_k = |
| 60f6a6b | 104b04a | registry v1.34: the paper rewritten as a mathematics paper (Roof_and_Clock_MATH_v2, Theorems A-F, full proofs, |
| 63ed84f | be3f238 | registry v1.33: Stone BC staged (SM-067) - does the 4-cube anomaly recur on the 8-cube? brief locked, NEXT_MAP |
| 950c634 | d446634 | registry v1.32: joint paper v1.0 built on the Stenberg side (build_v1.py = the audited v0.8->v1.0 diff); sec 7 |
| 317ec48 | 0ce3b14 | registry v1.31: FANO-COEXISTENCE-AND-KLEIN envelope SENT on Selina's word; folder frozen. Pending his word on  |
| 536e42c | b291862 | registry v1.30: IB Fano Results 1-20 received (8 saves, -18 rebuilt 26/27, Result 20 script missing); coexiste |
| 3312a28 | 79d1cb3 | registry v1.29: FANO-QUARTIC-CORRECTION envelope SENT on Selina's word; folder frozen. Pending his word on the |
| 3c80d22 | 7abc7db | registry v1.28: Fano quartic bridge - Result 2 correction (5 quartics + 1 sextic) + Q_miss (chiral 6th = King- |
| 483a2e3 | fe330f4 | registry v1.27: IB consolidated acceptance filed - SM-057..066 all ten JOINT (065/066 seals closed); Fano sext |
| 0c8e6f1 | 0a99103 | registry v1.26: FANO-IDENTITY reply SENT on Selina's word; folder frozen. KCP re-pinned. |
| 724a0da | 26d1c4b | registry v1.25: Fano sextet re-run + Fano/bitangent identity settled; paper sec 11.9 |
| 23f00da | 4cc7695 | registry v1.24: HALFTURN envelope SENT (SM-066) on Selina's word; folder FROZEN. All units SM-001..066 with Il |
| 45ab513 | 162015d | registry v1.23: IB reply filed - SM-057..064 JOINT; sec 11.3/12 verified; Fano sextet received |
| 0ccc44e | 51d1d7b | registry v1.22: HALFTURN package PREPARED (SM-066), not sent |
| ddf1eeb | 52c6341 | registry v1.21: SM-066 STONE BB - the half-turn and the full-height orbit |
| 0162cff | 5e04b48 | joint paper v0.5: add §11, the Balashov-side tower and bitangent bridge |
| 7bc0361 | 094d5c7 | joint paper v0.4: add §11 Discussion (synthesis only) |
| 97942bc | 96f16b0 | KCP manifest migrated to spec 0.32 (content_hash pins, audience, x-house-scope) |
| 2157fcf | bcf6a5f | housekeeping: NEXT_MAP_2026-09-11.md - handoff map for the next session (state v1.20, everything with Ilya, pe |
| ab5c71d | 7071d4d | registry v1.20: HIERARCHY-AND-v0.3 envelope SENT on Selina's word - to_Ilya_HIERARCHY_AND_V03_2026-09-11.zip ( |
| d10789f | 8614af2 | registry v1.19: draft v0.3 built (joint_paper/Roof_and_Clock_DRAFT.md, 1,349 lines: sections 7.8-7.13 merged f |
| 082ea60 | d653708 | registry v1.18: IB's batch of 2026-09-10 filed (RECEIVED_2026-09-11_IB_ACCEPTANCE_REVIEW_LITERATURE, 6 files,  |
| 21e5e21 | a17b707 | registry v1.17: SM-065 STONE BA - the clock's Clifford hierarchy. The chain P_1 = W, P_{j+1} = {g in P_j : R^- |
| fec911f | 1e2db5a | registry v1.16: ANOMALY-BY-HAND envelope SENT on Selina's word - to_Ilya_ANOMALY_BY_HAND_2026-09-10.zip (e4ed1 |
| 80892bc | d658120 | registry v1.15: SM-063 and SM-064 SEALED in one envelope with their summary - to_Ilya_ANOMALY_BY_HAND_2026-09- |
| d4171e6 | a8d9849 | registry v1.14: SM-064 STONE AZ - the doubled clock: the vector boards' shared grammar is C_W(R^2k). Lemma C ( |
| 9229347 | 26a78b7 | registry v1.13: SM-063 STONE AY - the D5 anomaly by hand: the half-turn is a Weyl element on one orbit. On the |
| 119101c | ffbd033 | registry v1.12: both envelopes SENT on Selina's word - to_Ilya_C_EQUALS_T_2026-09-10.zip (29bd45bf..., SM-062  |
| 5909252 | 2def677 | housekeeping: NEXT_MAP_2026-09-10.md - handoff map for the next session (state v1.11, two prepared sends, pend |
| 239f9ec | d92af71 | registry v1.11: ARCHIVE reply prepared - to_Ilya_REPLY_ARCHIVE_2026-09-10.md (single markdown): his PSL27_to_P |
| 78587cc | 2000d72 | registry v1.10: SM-062 SEALED in an envelope with its summary - to_Ilya_C_EQUALS_T_2026-09-10.zip: cover (why  |
| f20fa63 | 33b97d6 | registry v1.09: SM-062 STONE AX - C = T, the reverser as a constraint on the grammar. Reversers of the clock i |
| d3f4cbb | f78f8c6 | registry v1.08: IB's PSL27_to_PMNS_full_archive.zip filed (sha b9b88a7c..., 188 files, extracted, no code run) |
| 9061659 | 9915499 | registry v1.07: ANOMALY-HOMOMESY envelope SENT on Selina's word (6fada4f6...), FROZEN; every sealed unit SM-00 |
| ff7de9c | 1d7c372 | registry v1.06: IB's 'memory channel' hypothesis on the D5 anomaly filed RECEIVED_2026-09-10_IB_D5_CHANNEL (ph |
| 63fd2af | bbb586f | registry v1.05: SM-060 + SM-061 SEALED in one envelope with their summary - to_Ilya_ANOMALY_HOMOMESY_2026-09-1 |
| df2264a | 49f7348 | registry v1.04: SM-060 STONE AV (the D5 anomaly on the 4-cube: located on the B4 spinor board = Aut(Q4) with t |
| 6c49270 | 7d6b335 | registry v1.03: reversals envelope SENT on Selina's word (to_Ilya_REVERSALS_2026-09-09.zip, sha 3771dc01...),  |
| dfcd735 | 478e2ce | registry v1.02: SM-058 + SM-059 SEALED in one envelope with their summary - to_Ilya_REVERSALS_2026-09-09.zip ( |
| 1ab1a1e | e520c93 | free exploration filed (NOT sealed): the D5 half-spin anomaly of SM-058 - rowmotion is not affine over F2 for  |
| 3bc271c | a39554a | registry v1.01: SM-059 STONE AU - the reversal theorem (w0 R w0 = R^-1 on every minuscule board, proved and ch |
| cd24d87 | 83280bd | registry v1.00: SM-058 STONE AT - the shared grammar across the minuscule family: the guess I_k = C_W(R^k) INV |
| 3aa05b0 | ed1f7d6 | registry v0.99: shared-grammar envelope SENT on Selina's word (to_Ilya_SHARED_GRAMMAR_2026-09-09.zip, sha 6bf4 |
| cc2983c | 2a7cc57 | registry v0.98: SM-057 SEALED in its own envelope with its summary - to_Ilya_SHARED_GRAMMAR_2026-09-09.zip (sh |
| c99d1e5 | 5247b3a | registry v0.97: theorems envelope SENT on Selina's word (to_Ilya_THEOREMS_2026-09-09.zip, sha d19a3e8e..., SM- |
| dadcd97 | 571dd16 | registry v0.96: SM-057 STONE AS - the shared grammar: W(E7) and Psi^k W Psi^-k meet in the identity alone for  |
| 1b7b5f1 | 7a45390 | registry v0.95: IB's Brief Reply filed RECEIVED_2026-09-09_IB_BRIEF_REPLY (pasted text, hash of the saved file |
| 47eb474 | 16a4453 | registry v0.94: paper draft v0.2 (joint_paper/Roof_and_Clock_DRAFT.md) - abstract and tier three restated; new |
| 9bc62e2 | afd4cc8 | registry v0.93: SM-056 SEALED in its own envelope with the summary of the theorems - to_Ilya_THEOREMS_2026-09- |
| d269255 | 7132f13 | registry v0.92: SM-056 STONE AR - the non-linearity theorems (merkabit side): rowmotion is a Weyl element iff  |
| b58960d | ff60dad | registry v0.91: both 09-09 envelopes SENT on Selina's word - to_Ilya_FRAMING_2026-09-09.zip (4b6cf0ec..., draf |
| 009786a | 227e8a5 | registry v0.90: SM-055 SEALED in its own envelope with the summary of all findings - to_Ilya_DEFECT_2026-09-09 |
| 3425c86 | c8259b1 | registry v0.89: SM-055 STONE AQ - the Rush-Shi defect across the minuscule family: 42 cases (A_n all omega_k n |
| bf03022 | 680b9f8 | registry v0.88: spine paper draft v0.1 (joint_paper/Roof_and_Clock_DRAFT.md) written in IB's three-tier shape  |
| 5086df9 | 1cfa54a | registry v0.87: IB's audits + publication response filed RECEIVED_2026-09-09_IB_AUDITS_PUBLICATION (8 files):  |
| b46a3ea | b0664bf | registry v0.86: reply package SENT on Selina's word (to_Ilya_CLOCK_CENTRALIZER_2026-09-07.zip, sha 401ed1b3... |
| 1422af8 | 017de66 | registry v0.85: reply package SEALED - to_Ilya_CLOCK_CENTRALIZER_2026-09-07.zip (sha 401ed1b3..., 118,585 B):  |
| 842f145 | b63b355 | registry v0.84: SM-054 STONE AP - the clock's linear centralizer: C_{S56}(Psi) (69,984) meets W(E7) in the ide |
| 6216189 | 5d4f756 | registry v0.83: IB's descent-ladder batch (57 docs) filed RECEIVED_2026-09-07_IB_DESCENT_LADDER_GENERATIONS +  |
| 40174a9 | f125adf | registry v0.82: IB's FINAL RESPONSE filed - SM-041..053 ACCEPTED IN FULL -> JOINT (byte-exact reproduction of  |
| 303ff9f | 9bba113 | registry v0.81: re-send package SENT on Selina's word (to_Ilya_RESEND_2026-09-06.zip, sha 2fa05793...), FROZEN |
| 262d17d | eeafaaa | registry v0.80: IB's September audit filed (SM-045..053 ACCEPTED -> JOINT; envelopes 2 and 3 recorded SENT on  |
| 233c5ba | 4c25dda | registry v0.79: coset-and-mirror package sealed (to_Ilya_COSET_AND_MIRROR_2026-09-06.zip) with FINDINGS_SUMMAR |
| 6d9af4c | 6adcebb | registry v0.78: SM-053 STONE AO - the mirror and the gates: pr = the E6 Dynkin diagram automorphism acting on  |
| 2d1cc8a | 9e4ef97 | registry v0.77: reply package SENT on Selina's word (to_Ilya_REPLY_2026-09-05.zip, sha 059b8d7c...), envelope  |
| 4ce718d | 1645ab3 | registry v0.76: SM-052 STONE AN - the ATLAS names: our fourteen twisted classes are the fourteen outer classes |
| c5ea9cc | 823a82a | registry v0.75: SM-051 STONE AM - the coset complete: the roof's twisted coset Omega.Phi is exactly FOURTEEN c |
| e5bb0cb | 930263f | registry v0.74: the roof's clocks package sealed (to_Ilya_ROOF_CLOCKS_2026-09-06.zip, sha 1c22c2df..., 238,098 |
| a4e0b40 | 11085e6 | registry v0.73: SM-050 STONE AL - the seven-beat clock's class and the turn's centralizer: C_Omega(Phi) = G2(2 |
| aa8ad73 | d7d47b7 | registry v0.72: SM-049 STONE AK - the two twenty-fours: the order-24 twisted elements are exactly two classes  |
| 0149919 | 733b3b7 | registry v0.71: SM-048 STONE AJ - the heart at the still point: G2(2) commutes with the turn, twisted orders l |
| 202edc1 | ff431dc | registry v0.70: SM-047 STONE AI - the class of the eighteen and the heart's centralizer: |C_Omega(x)| = 1944 e |
| 3e38dbf | 169c691 | registry v0.69: SM-046 STONE AH - the one heart: the E6 Coxeter power lies in the class of (Phi.c-bar)^6 and c |
| 6b9cc6a | 528b471 | registry v0.68: SM-045 STONE AG - the seven nines: a counting rhyme at order 9 (c-bar7^2 = F64 field element o |
| 0ee43fe | 1039af5 | registry v0.67: SM-044 STONE AF - the three eighteens: IB's 'what does Psi remember' = not a type (P 66.7 / S  |
| 75dad29 | 26dd7c7 | registry v0.66: reply package sealed (to_Ilya_REPLY_2026-09-05.zip, sha 059b8d7c..., 4,182,480 B): cover + SM- |
| 545ec25 | 617e331 | registry v0.65: SM-042 STONE AD (IB's forced-narrowing table: maximal 22/4/21/8/5/1/0, normal 2/10/2/4/3/2/1;  |
| b22f3c2 | 9eacd7d | v0.64 fixup: registry body written (the inserter's collision guard had tripped on 'PREPARED-NOT-SENT' and the  |
| c8c669b | 339bdf8 | registry v0.64: IB's 2026-09-03/04 batch filed (26 shas) - SM-038/039/040 ACCEPTED -> JOINT; 36<->36 closed hi |
| 0fe5eb5 | 0b1a6a8 | registry v0.63: SM-041 - STONE AC, the parity rule of the clock: Psi = rowmotion exactly; type flips iff toggl |
| 4aedc6f | 274af3b | registry v0.62: merkabit-under-the-still-point package sealed (SM-040); PREPARED-NOT-SENT |
| 55ac189 | 709574b | registry v0.61: SM-040 - STONE AB, the merkabit is the roof's vector block (56 = {B(u,v)=1}, iota = t_v); G2(2 |
| db145ff | 5b60ea4 | registry v0.60: still-point + clock package sealed (zip sha 108b9ddd...), erratum leading; PREPARED-NOT-SENT |
| fa05aec | 56ac073 | registry v0.59: beta-reply SENT (d669241c...), FROZEN; erratum (transition-magnitudes provenance) to lead the  |
| 9c1f366 | 39466de | registry v0.58: SM-039 - STONE AA, the turn acts on states: O8+(2):3 explicit on 360 points; still point = joi |
| 0fc9789 | ec6a395 | v0.57 fixup: Stone Z cache witnesses (y columns, involution table, PSL(2,7) fingerprints); G_rows.npy left unt |
| 3f9fde3 | 67500d2 | registry v0.57: SM-038 - STONE Z, the still point of the roof turn is G2(2) (index 120, exhaustive); turner no |
| 26b3875 | a4f132d | registry v0.56: beta-reply package sealed (zip sha d669241c...); PREPARED-NOT-SENT |
| 45fb110 | d41d096 | registry v0.55: SM-037 - STONE Y, the beta-register computed (17/17); at S3 and D4 it is the eps-table relabel |
| 3eb869b | 71a2991 | registry v0.54: five seals JOINT on IB's audit (SM-029/030/032/033/034); two-register model ACCEPTED; turner S |
| e88565c | a766f03 | registry v0.53: turner package sealed (zip sha c9dc0982...); PREPARED-NOT-SENT |
| 6cb9544 | 11e3d51 | registry v0.52: SM-036 - THE TURNER BUILT, twice over (Stone X) |
| d260429 | 761c554 | registry v0.51: still-point SENT (39da0899...), FROZEN; Stone X brief staged + sha-locked before code |
| 58ffd4d | 1fc5cb8 | registry v0.50: still-point addendum sealed in its own envelope (zip sha 39da0899...); PREPARED-NOT-SENT |
| 4a5e649 | 26f920e | registry v0.49: send record corrected - original b6429570 is the send of record (SENT+FROZEN, restored byte-ex |
| b556bca | 73f74f2 | registry v0.48: envelope resealed with SM-035 aboard (zip sha f5280d67..., supersedes unsent b6429570...); PRE |
| 715ed29 | b098d6b | registry v0.47: SM-035 - the two sevens are one (PSL(2,7) in G2, computed; canonical 3-form; seven-beat clock  |
| eb364ab | 5aa7725 | registry v0.46 fixup: changelog entry restored; KCP pin corrected |
| 29a7ae1 | 582f3a8 | registry v0.46: two-registers package sealed (zip sha b6429570...) PREPARED-NOT-SENT |
| 2cd91bd | b655f5a | registry v0.45: SM-034 - the two registers meet and COMMUTE (triality crystals); spiral-18 guess refuted; the  |
| 47f23b8 | f5317b9 | registry v0.44: SM-033 - THE LIFT LAW closed (epsilon necessary, not sufficient; commutator sign is the key) + |
| 7ab41d2 | 08a32ee | registry v0.43: SM-032 - THE TRIANGLE CLOSES (S3 closure) + turn-point Criterion A sealed |
| 7259e96 | fe42cda | registry v0.42: SM-031 JOINT (IB accepts three-shadows); tubes/turns batch filed + triaged; third-shadow send  |
| 7f3e534 | 45b9b00 | registry v0.41: floor-limit thread cross-referenced to the Riemanns lane; parallel session already verified +  |
| 8c9173e | cc1ee45 | registry v0.40: third-shadow package sealed (zip sha 89a01282...) |
| a5b9af9 | ba54953 | registry v0.39: Stone W - THE TWO SHADOWS ARE THREE (SM-031) |
| d4f1a4d | f9bc066 | Stone W brief staged and sha-locked before code (the third shadow) |
| b57c493 | 33ea3a3 | registry v0.38: IB FLOOR LIMIT filed - unverifiable as sent (A_fixed undefined); pi-hunt flags staged per hous |
| c160430 | a0503a0 | registry v0.37: roof reply SENT (zip sha b2c96141...); envelope FROZEN |
| 4187dae | 7d9d253 | registry v0.36: roof reply package sealed (PREPARED-NOT-SENT) |
| 93093b1 | 23e157c | registry v0.35: Stone V - THE ROOF FOUND: W+(E8) (SM-030) |
| f8e3d63 | 5c3981b | registry v0.34: SM-029 Schur-class pinning - hope inverted; the Fano class is the spinorial one |
| f1aa63f | 77d63fe | registry v0.33: choice theorem JOINT (We go up); Stone U send recorded; Stone V brief staged + locked; class-p |
| 829eea5 | 545b9bf | registry v0.32: Stone U reply package sealed (PREPARED-NOT-SENT) |
| 64e46c3 | 24cefea | registry v0.31: Stone U - 2.Sp6(2) BUILT + the choice theorem (SM-027); IB answers verified (SM-028) |
| 2e7c49d | 2e7c49d | Stone U brief staged and sha-locked before code (the other double cover) |
| 26a31a6 | 26a31a6 | kcp: repair utf-8 mojibake from the v0.30 pin refresh |
| 0e799ce | 0e799ce | registry v0.30: containment reply SENT (zip sha 147c5a7f...); envelope FROZEN |
| 3521f9e | 3521f9e | registry v0.29: containment reply package sealed (PREPARED-NOT-SENT) |
| 55a95da | 55a95da | registry v0.28: IB hinge/compression batch verified (SM-023..SM-026) |
