```markdown
# RESULT: Level 6 = A₄, Explicitly Sealed


**Status:** SEALED
**Origin:** exact generator construction
**Subject:** the correct level-6 object inside the fixed PSL(2,7)


---


## 1. The Presentation Correction


```text
For the fixed matrices A, B:


  A² = I
  B³ = I
  (AB)⁷ = I


NOT


  A³ = B⁷ = (AB)² = I
```


---


2. The Chain


```text
⟨A,B⟩ = PSL(2,7)


order 168
```


---


3. Explicit S₄


```text
S₄ = ⟨X, Y⟩


X = A B A B⁻¹


Y = B⁻¹ A B A B⁻¹ A B


|S₄| = 24
```


---


4. Explicit A₄


```text
A₄ = ⟨P, Q⟩


P = X²


Q = X Y


|A₄| = 12
```


---


5. Normality


```text
A₄ ⊲ S₄


[S₄, S₄] = A₄
```


---


6. The Sealed Transition


```text
A₄ ⊲ S₄ ⊂ PSL(2,7)


12 ⊲ 24 ⊂ 168
```


---


7. Information Loss


```text
7 → 6:


log2(168) − log2(12)


= 3.8073549221 bits
```


---


END OF RESULT


```