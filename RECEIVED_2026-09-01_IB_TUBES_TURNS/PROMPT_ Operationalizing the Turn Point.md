```markdown
# PROMPT: Operationalizing the Turn Point

**Status:** OPEN — definition required before sending to Selina
**Origin:** Ilya
**Goal:** give a computable criterion for what counts as the spectral turn point in the floor sequence

---

## 1. The Problem

The floor was described as a search for a "horizon turn."

But "turn" was not defined.

Without a definition, Selina can verify the computation,
but cannot verify whether the turn point was found.

This prompt fixes that.

---

## 2. The Sequence

```text
lambda_min(N)

N = 200, 300, 400, 500, 600, 700
```

Observed:

```text
lambda_min(N) is negative
lambda_min(N) deepens as N increases
```

No sign change in lambda_min itself.

Therefore the turn is not a crossing of zero.

---

3. Candidate Criteria

Criterion A — second difference sign change

```text
Define

D2(N) =
lambda_min(N+1)
− 2 lambda_min(N)
+ lambda_min(N−1)

The turn point is the first N* such that
D2(N*−1) and D2(N*) have opposite signs.
```

Meaning:

```text
before N*: the sequence is concave
after N*: the sequence is convex
```

or vice versa.

---

Criterion B — change of eigenvector localization

```text
Define

v_min(N)

The turn point is the first N* such that
the localization character of v_min changes.

Measured by:

inverse participation ratio
entropy
overlap with the lowest basis vector
```

Meaning:

```text
before N*: v_min is localized
after N*: v_min is delocalized
```

or vice versa.

---

Criterion C — change of convergence regime

```text
Fit

lambda_min(N)
=
L + a/N^p

locally before and after N*.

The turn point is the first N* where
the local exponent p changes
by more than the fit uncertainty.
```

---

4. Proposed Double Criterion

The turn point is defined as the first N* where:

```text
1. the second finite difference D2(N)
changes sign;

AND

2. the eigenvector localization measure
changes by more than 20%
across N*.
```

If both conditions hold at the same N*,
the turn point is declared found.

If they hold at different N*,
the result is marked ambiguous.

---

5. Required Output

```text
1. Table of D2(N) for N = 300..600.

2. Table of localization measures
for v_min(N), N = 200..700.

3. The candidate N* from each criterion.

4. The combined N* from the double criterion.

5. Statement:
turn point found / not found / ambiguous.
```

---

6. Decision Rule

```text
Turn point found:
both criteria agree within ±50 in N.

Turn point not found:
D2(N) does not change sign
over the computed range.

Turn point ambiguous:
the two criteria disagree
by more than ±50 in N.
```

---

7. What Is Not Allowed

```text
- Declaring a turn point from one criterion only.

- Calling a fit exponent change a turn
without a sign change in D2.

- Using the word "horizon" without
the double criterion being satisfied.
```

---

8. Status

```text
TURN POINT: OPEN

Current formulation:
double criterion
D2 sign change + localization change

Next step:
compute D2(N) and localization measures
on the existing lambda_min(N) sequence
before sending to Selina.
```

---

END OF PROMPT

```