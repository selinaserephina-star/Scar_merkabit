```markdown
# PROMPT: Total Work of the Roof Dynamics


**Status:** OPEN — testable formulation
**Origin:** Ilya
**Goal:** show that the roof dynamics has a total work equal to S = 6037, computed from the three vectors and the six descent transitions


---


## 1. The Roof


```text
The roof is the Klein quartic before scattering.


It contains:
  - three vectors
  - a potential (Mexican hat)
  - a pulse generator
```


---


2. The Three Vectors


```text
V1 = downward pull → force along the descent
V2 = surface integrity → resistance
V3 = periodic strike → pulse
```


---


3. The Work Hypothesis


```text
Total work after the roof dynamics:


W_roof = Σ forces × displacements
       = Σ g(n) · σ(n)
       = 6037
```


where the sum is over the six descent transitions:


```text
n = 7, 6, 5, 4, 3, 2
```


---


4. Required Computation


Step 1


```text
Identify which vector contributes to each g(n).
```


Step 2


```text
Identify which displacement is measured by each σ(n).
```


Step 3


```text
Compute the product g(n)·σ(n) for each level.
```


Step 4


```text
Sum the six products.
```


Step 5


```text
Verify that the sum equals 6037.
```


---


5. Required Output


```text
1. Table: n, vector contribution, g(n), σ(n), product.


2. Total sum.


3. Comparison with S = 6037.


4. Statement:
   the roof dynamics has total work 6037
   / the identification fails.
```


---


6. Decision Rule


```text
Supported if:


- each g(n) receives a vector contribution;


- each σ(n) is a displacement;


- the total equals 6037 without adjustment.


Not supported if:


- the three vectors cannot be matched to g(n);


- the total differs from 6037;


- adjustments are required to force the match.
```


---


7. What Is Not Allowed


```text
- Redefining σ(n) to force the sum.


- Ignoring the sign structure of σ(n).


- Treating S = 6037 as a target
  instead of an output.
```


---


8. Status


```text
ROOF WORK TEST: OPEN


Current formulation:
  three vectors → forces
  six transitions → displacements
  total work → 6037


Next step:
  match vectors to g(n),
  compute the sum,
  compare with 6037
```


---


END OF PROMPT


```