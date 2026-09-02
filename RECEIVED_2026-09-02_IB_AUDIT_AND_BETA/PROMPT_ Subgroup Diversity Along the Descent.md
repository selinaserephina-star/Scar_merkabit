```markdown
# PROMPT: Subgroup Diversity Along the Descent


**Status:** OPEN
**Origin:** Ilya
**Goal:** test whether subgroup diversity decreases along the descent levels


---


## 1. The Level Groups


```text
7: PSL(2,7), |G| = 168
6: C₆ × Z₂ ← candidate label, NOT sealed
5: A₅, |G| = 60
4: S₄, |G| = 24
3: A₄, |G| = 12
2: Z₂, |G| = 2
1: {e}, |G| = 1
```


Note:


```text
Level 6 is label-unstable in the registry.


If subgroup counts depend on the choice of L6,
compute for C₆ × Z₂ and state that alternative
L6 labels are not tested here.
```


---


2. What to Compute


For each level:


```text
1. Number of subgroups.


2. Number of conjugacy classes of subgroups.


3. Number of maximal subgroups.


4. Number of normal subgroups.
```


---


3. Required Output


```text
Table:


level | |G| | #subgroups | #conj classes | #maximal | #normal
```


---


4. Decision Rule


```text
Diversity narrowing is supported if:


- the number of subgroups decreases
  from level 7 to level 1;


- the number of conjugacy classes of subgroups
  also decreases.


Not supported if:


- diversity increases at some level;


- the pattern is not monotone.
```


---


5. What Is Not Allowed


```text
- Comparing only group orders.


- Ignoring levels where diversity increases.


- Using only normal subgroups
  instead of all subgroups.


- Treating level 6 as sealed
  when its label is still open.
```


---


6. Status


```text
SUBGROUP DIVERSITY TEST: OPEN


Next step:
  compute subgroup counts
  for all seven levels
```


---


END OF PROMPT


```