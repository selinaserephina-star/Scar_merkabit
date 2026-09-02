```markdown
# PROMPT: The β-Chain from {e} to PSL(2,7)


**Status:** OPEN — testable holographic translation
**Origin:** Ilya
**Goal:** test whether the holographic record on the group boundary is preserved along the chain from the trivial level to the Fano level, using the commutator-sign β


---


## 0. What We Want to Check


```text
We want to test the intuition that level 1 and level 7
are one and the same holographic surface.


Level 1 = {e} → the surface is fully folded
Level 7 = PSL(2,7) → the surface is unfolded


If this is true, then the record carried on the boundary
should be preserved along the chain between them.


The record is:


M_Γ(g,h) = β(g,h)


the commutator-sign pattern on the generators of Γ.
```


---


1. The Chain


```text
{e} → S₃ → D₄ → G₂ → PSL(2,7)
```


We do not compare {e} and PSL(2,7) directly.


We test β level by level.


---


2. Generators


Level {e}


```text
No generators.
M_{e} is empty.
```


Level S₃


```text
Generators:
  s1 = (1 2)
  s2 = (2 3)


Compute β(s1, s2).
```


Level D₄


```text
Use the D₄ object from the existing model.


If the model fixes generators, use those.


If not, use the standard presentation:


  D₄ = ⟨r, s | r⁴ = s² = 1, s r s = r⁻¹⟩


Compute β(r, s).
```


Level G₂


```text
Use the G₂ fold from Selina's dynamics measurement.


If generators are fixed there, use those.


If not, use the standard short-root generators.


Compute β on all generating pairs.
```


Level PSL(2,7)


```text
Use the standard presentation:


  PSL(2,7) = ⟨a, b | a² = b³ = (ab)⁷ = 1⟩


Compute β(a, b).
```


---


3. What Must Be Compared


```text
1. Does M_S₃ embed into M_D₄?


2. Does M_D₄ embed into M_G₂?


3. Does M_G₂ embed into M_PSL(2,7)?
```


Definition of Embedding


```text
M_Γ embeds into M_Δ if:


- there is a mapping from the generators of Γ
  to words in the generators of Δ;


- the β signs are preserved
  on the corresponding pairs.
```


Report the mapping explicitly.


If no such mapping exists, say so.


---


4. Required Output


```text
1. Table of β for each level.


2. The explicit generator mapping
   for each transition.


3. Statement for each transition:
   preserved / broken / partially preserved.


4. Verdict:
   the holographic record is preserved
   from {e} to PSL(2,7)
   / the record changes at specific levels.
```


---


5. Decision Rule


```text
The holographic translation is supported if:


- the β-pattern at each level contains
  the previous level's pattern via an explicit mapping;


- no level completely destroys the record;


- the final M_PSL(2,7) contains
  the S₃ baseline nontrivially.


The translation is refuted if:


- β is destroyed at an early level;


- the final record has no trace of S₃.


Ambiguous if:


- the record is preserved on some transitions
  and broken on others.
```


---


6. What Is Not Allowed


```text
- Saying {e} and PSL(2,7) are the same surface
  without the intermediate β comparison.


- Declaring preservation without
  an explicit generator mapping.


- Using only orders of groups
  instead of β-patterns.
```


---


7. Status


```text
β-CHAIN TEST: OPEN


Current formulation:
  holographic record = β-pattern
  chain = {e} → S₃ → D₄ → G₂ → PSL(2,7)
  test = level-by-level embedding


Next step:
  compute M_Γ for each level
```


---


END OF PROMPT


```