```markdown
# COMPRESSION OPERATOR TASK v0.1


**Status:** formalization task — OPEN
**Purpose:** define a group-theoretic compression operator C and test it on the first bridge


---


## 1. The Goal


```text
Find an operator C
such that:


C(G_left, G_right)
=
the unique surviving
structural class
after maximal compression.
```


---


2. Requirements


```text
C must:


1. Be group-theoretic.


2. Make no choices.


3. Use only subgroups,
   quotients,
   and shared structure.


4. Be the same
   for all six bridges.


5. Not use physical labels.
```


---


3. First Test


```text
Input:


(PSL(2,7), C₆×ℤ₂)


Required output:


- the survivor;
- whether it is unique;
- whether it matches
  the observed common floor:


  {1, C₂, C₃, V₄}
```


---


4. Candidate Definitions


```text
Candidates for C:


A. common subgroup lattice
   after removing non-shared
   types.


B. maximal shared subgroup
   under the gcd bound.


C. the kernel of all
   possible morphisms
   between the two groups.


D. the intersection
   of normal closures.


E. the unique maximal
   shared class
   after eliminating
   all non-surviving types.
```


---


5. Required Output


```text
For the first bridge:


1. Chosen definition of C.


2. The computed survivor.


3. Uniqueness proof
   or failure.


4. Match with observation:


   YES / NO
```


---


6. What Is NOT Allowed


```text
- No choosing C
  after seeing the survivor.


- No using the later bridges
  to tune C.


- No physical interpretation.
```


---


7. Status


```text
COMPRESSION OPERATOR:
OPEN


NEXT STEP:
define C
and run it
on 7↔6.
```


---


8. Final Rule


```text
Compression must be
a machine.


Same machine for every bridge.


Then the descent
is not a story.
It is an output.
```


---


END OF COMPRESSION OPERATOR TASK v0.1


```



