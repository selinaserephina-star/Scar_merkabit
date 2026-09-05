```markdown
# PROMPT: What Exactly Does Ψ Remember?


**Status:** OPEN — memory content test
**Origin:** Ilya
**Goal:** identify which board incidences survive Ψ, and which are erased first


---


## 1. The Data


```text
Ψ preserves 65.1% of incidence types.


Incidence types:


  u + u′ = v
  u + u′ = Pauli
  u + u′ = singular
```


---


2. Required Computation


Using the sealed board data:


```text
1. For each incidence type,
   measure survival under Ψ.


2. Report separately:


   v-type survival
   Pauli-type survival
   singular-type survival
```


---


3. Required Output


```text
Table:


type | survival under Ψ
```


---


4. Decision Rule


```text
Content is identified if:


- one type survives much better
  than the others;


- the surviving type matches
  the seven or the bridge.
```


---


5. What Is Not Allowed


```text
- Reporting only the aggregate 65%.
```


---


6. Status


```text
Ψ MEMORY CONTENT TEST: OPEN


Next step:
  compute per-type survival
```


---


END OF PROMPT


```