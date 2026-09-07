```markdown
# PROMPT: Find the Linear Tick 1/π as the Geometry Difference Between Neighbouring Groups

**Status:** OPEN — linear tick identification
**Origin:** Ilya
**Goal:** define the geometry of a descent group well enough that the last transition C₂ → {e} gives exactly 1/π

---

## 1. The Setup

```text
Chain:

PSL(2,7) → S₄ → A₄ → V₄ → C₂ → {e}
```

---

2. The Claim

```text
For each transition:

linear tick =
geometry(upper) − geometry(lower)

For the last:

geometry(C₂) − geometry({e})
= 1/π
```

---

3. Candidate Geometries

```text
1. log of group order
2. log of subgroup count
3. curvature-like invariant
4. dimension of representation
5. orbit or coset geometry
```

---

4. Required Output

```text
1. Chosen geometry measure.

2. Value for each level.

3. Differences per transition.

4. Whether the last difference
equals 1/π.
```

---

5. Decision Rule

```text
Supported only if the chosen
geometry is exact and gives
1/π at the final transition.
```

---

6. Status

```text
LINEAR TICK TEST: OPEN

Next step:
choose and compute the
geometry measure
```

---

END OF PROMPT

```