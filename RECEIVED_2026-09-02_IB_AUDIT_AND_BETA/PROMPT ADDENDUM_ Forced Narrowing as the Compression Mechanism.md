```markdown
# PROMPT ADDENDUM: Forced Narrowing as the Compression Mechanism


**Status:** OPEN — mechanistic hypothesis
**Origin:** Ilya
**Goal:** test whether subgroup narrowing is not just an observed pattern, but the mechanism that forces geometric compression


---


## 1. The Hypothesis


```text
Subgroup diversity narrows along the descent.


This narrowing is not a side effect.


It is the cause of geometric compression.
```


---


2. The Causal Chain


```text
narrower group
→ fewer allowed symmetries
→ fewer allowed configurations
→ smaller geometric variety
→ compression
```


---


3. What Must Be Tested


For each descent step:


```text
1. How many subgroup classes are lost?


2. What geometric symmetries are lost?


3. Does the loss of symmetry
   correspond to a reduction in form?
```


---


4. Concrete Test


Use the subgroup counts from the main prompt.


For each transition:


```text
level n → level n−1


lost subgroups =
#subgroups(n) − #subgroups(n−1)


geometric prediction:
larger loss ⇒ stronger compression
```


Compare with the known transition magnitudes:


```text
168 → 144 loss 24
144 → 16 loss 128
16 → 12 loss 4
12 → 14 gain 2
14 → 10 loss 4
10 → 1 loss 9
```


---


5. Required Output


```text
Table:


transition | lost subgroups | transition magnitude
```


Test:


```text
Does a larger lost-subgroup count
correspond to a larger geometric transition?
```


---


6. Decision Rule


```text
The mechanism is supported if:


- the largest subgroup loss occurs at
  the largest compression transition;


- the smallest subgroup loss occurs at
  the smallest or reversing transition.


The mechanism is refuted if:


- there is no correspondence between
  subgroup loss and transition size.


Ambiguous if:


- the correspondence holds for some
  transitions but not all.
```


---


7. What Is Not Allowed


```text
- Declaring causation without the table.


- Ignoring the 12 → 14 expansion
  when testing the mechanism.


- Comparing transition sizes
  without subgroup counts.
```


---


8. Status


```text
FORCED NARROWING MECHANISM: OPEN


Next step:
  compute subgroup loss per transition,
  compare with transition magnitudes
```


---


END OF ADDENDUM


```