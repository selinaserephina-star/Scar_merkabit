# Audit — `to_Ilya_CLOCK_CENTRALIZER_2026-09-07.zip` (Stone AP)

**Auditor:** Claude (Sonnet 5), independent session
**Date:** 2026-09-08
**Subject:** integrity and computational reproducibility of Stone AP ("the clock's linear centralizer")

---

## 1. Scope

This audit covers only the package `to_Ilya_CLOCK_CENTRALIZER_2026-09-07.zip`, specifically:
- file integrity of all 15 shipped files against `SHA256SUMS.txt`
- independent re-execution of `verify_stone_ap_clock_centralizer.py`
- comparison of that re-execution against the shipped `.log` files

It does **not** cover the correctness of the framework-level premises the script takes as given (e.g. results cited from earlier stones SM-012, SM-013, SM-040), and it does **not** evaluate the interpretive/physical material elsewhere in the batch (crystal-ladder claims, 1/π framing, flavon model) — the package itself marks those as parked or unsourced.

## 2. Method

1. Extracted the archive; listed all files.
2. Ran `sha256sum -c SHA256SUMS.txt` against every file in the package.
3. Read the verifier script's header to identify its inputs.
4. Found it requires `scar56_data.json`, **not included in this archive**.
5. Located that file in a separate, earlier package (`to_Ilya_REPLY_2026-09-05.zip`, `DATA/scar56_data.json`), copied it in.
6. Ran `python3 -X utf8 verify_stone_ap_clock_centralizer.py` fresh, in a clean environment (Python 3.12, numpy), independent of any machine the package was authored on.
7. Compared the resulting console output / regenerated log against the shipped `verify_stone_ap_clock_centralizer.log`.

## 3. Findings

### 3.1 File integrity — PASS

All 15 files match their declared SHA256 hashes exactly. No corruption or tampering detected.

### 3.2 Undeclared cross-package dependency

The verifier cannot run from this archive alone. It requires `scar56_data.json`, which ships only in the earlier `to_Ilya_REPLY_2026-09-05.zip` package. `COVER_NOTE.md` does not flag this dependency. Anyone holding only the CLOCK_CENTRALIZER package cannot reproduce the result without also retrieving the 09-05 package.

**Recommendation:** either bundle the data file with each package that depends on it, or state the cross-package dependency explicitly in the cover note.

### 3.3 Independent re-execution — reproduces

With the dependency supplied, the script completes and reports:

```
RESULT: 22 checks passed, 2 failed  FAILED: ['AP7', 'AP4d']
```

This matches the shipped log. The central claim (AP3a/AP3b) reproduced exactly:

- `C_S56(Ψ)` has 69,984 elements (cycle type [18,18,18,2]).
- Exactly **one** of them lies in W(E₇): the identity.
- None of its 231 involutions is linear (in W(E₇)).

The two `FAIL` entries are not concealed errors — the script itself frames both as disclosed, registered predictions that turned out wrong:

| Check | Registered prediction | Measured | Status |
|---|---|---|---|
| AP7 | Best linear-agreement involution has pr's structure (type 2²⁷1²) | Same score (1432/1540) but a *different* structural origin — the transposition of Ψ's own axis pair | Disclosed inversion |
| AP4d | Fixed-point spectrum of bridge PSL(2,7) copy on the 56, by class: (56,8,2,**4**,0,0) | (56,8,2,**0**,0,0) — matches the character-theoretic prediction 2(χ₁+2χ₆+χ₇+χ₈) | Disclosed sign/typo slip |

So: the two failures are self-reported and match what the documents (COVER_NOTE.md, TRIAGE) already say about them — nothing was found here that isn't already acknowledged in the package.

## 4. What this audit does and does not establish

**Established:** the code is internally consistent, runs cleanly on an independent machine, and reproduces its own claimed numeric output byte-for-byte on the results that matter (69,984 / 1 / 231 / 0, and the 22/24 pass count). This is a genuine, finite, brute-force group-theory computation — re-execution is a meaningful check here, not a formality.

**Not established by this audit:**
- Whether the framework premises the script assumes (e.g. "every C₂ lies in a PSL(2,7) acting on the 56 through W(E₇)," cited to SM-013/SM-040) are themselves correct — those originate outside this package and were taken as given.
- Any of the physical-interpretation material (crystal transitions, 1/π, flavon/Yukawa layer) — explicitly parked in the package itself, unsourced as shipped.

## 5. Verdict

The Stone AP computational claim — C_{W(E₇)}(Ψ) = {1}, i.e. no linear map commutes with the clock — is reproducible from the supplied code, given the one dependency file sourced from the 2026-09-05 package. File integrity is clean. The two self-reported failures are genuine and already disclosed, not hidden.

## 6. Outstanding (not addressed by this audit)

- SM-035 / SM-036 / SM-037 recheck — still pending your word.
- Source papers for the three crystal-ladder claims (langbeinite, Rochelle salt, Tl₂Cd₂(SO₄)₃) — requested in `TRIAGE_IB_BATCH_2026-09-07.md` §D.
- Direction and publication decisions — carried over unchanged from the 2026-09-06 acceptance note.
