```markdown
# RESPONSE TO SELINA — A_fixed, Protocol, and Pre-Registration


**From:** Ilya
**Re:** Floor L = 15.480 ± 0.006 — request for independent audit
**Status:** operator construction supplied; full independent run pending b(p^m) artifacts


---


## 1. The operator A_fixed


The exact construction is as follows.


### Basis


Even Hermite functions:


```text
psi_k(x) = c_k H_{2k}(x) exp(−x^2/2)


c_k = 1 / sqrt( sqrt(pi) 2^{2k} (2k)! )


k = 0, 1, 2, ..., N
```


Fourier transform


```text
psi_hat_k(u) = (−1)^k sqrt(2 pi) psi_k(u)
```


Kernel


```text
h_ij(u) = F[ psi_i psi_j ](u)
        = (1 / (2 pi)) ( psi_hat_i * psi_hat_j )(u)
```


Matrix size


```text
N + 1
```


The index set is i, j = 0, ..., N.


---


2. Matrix parts


A_cond


```text
A_cond[i,j] = ( log N_cond / pi ) delta_ij
```


where


```text
N_cond = 3^9 * 7^10
log N_cond = 29.346612088566...
```


A_arch


```text
A_arch[i,j]
=
(4 / pi)
∫_0^{U_max}
h_ij(u)
Re[ digamma(1/2 + iu) ]
du


+


(4 log(2 / pi) / pi)
∫_0^{U_max}
h_ij(u)
du
```


with


```text
U_max = 10
```


A_prime


```text
A_prime[i,j]
=
sum_{ p <= P_max }
sum_{ m = 1 }^{ M_p }


( 2 log p / p^{m/2} )
Re( b(p^m) )
h_ij( m log p )
```


with


```text
P_max = 10^5


M_p = floor( log(10^5) / log p )
```


Ramified primes


```text
b(3^m) = 0
b(7^m) = 0
```


For unramified p, b(p^m) is determined by the cycle type of


```text
f(x) = x^7 − 7x + 3


mod p
```


via


```text
b(p^m) = tr( Frob_p^m | rho_8 )
```


---


3. Full operator


```text
A_fixed = A_cond + A_arch − A_prime
```


---


4. Compute protocol


```text
STEP 1. Build the basis psi_0, ..., psi_N.


STEP 2. Compute the kernel h_ij(u) by Fourier convolution.


STEP 3. Build A_cond as a diagonal matrix.


STEP 4. Build A_arch by numerical integration
        to U_max = 10.


STEP 5. Build A_prime by summation over p <= 10^5
        and m <= M_p.


STEP 6. Form A_fixed = A_cond + A_arch − A_prime.


STEP 7. Diagonalize A_fixed.


STEP 8. Record lambda_min(N).


STEP 9. Repeat for N = 300, 400, 500, 600, 700.


STEP 10. Fit
         −lambda_min(N) = L − k / N^p
         and extract L.
```


---


5. Current known result


```text
N = 300 −lambda_min = 14.095273
N = 400 −lambda_min = 14.429690
N = 500 −lambda_min = 14.631510
N = 600 −lambda_min = 14.768492
N = 700 −lambda_min = 14.866000


L = 15.480 ± 0.006
p ≈ 0.9595
```


---


6. What is required for the independent run


The only external ingredient is the table


```text
b(p^m) = tr( Frob_p^m | rho_8 )


for p <= 10^5, m <= M_p
```


Everything else is analytic and reproducible from the formulas above.


I am locating the saved artifact for b(p^m) and will transmit it as:


```text
b_pm_table.csv
```


together with the generating script.


---


7. Pre-registration for the pi test


Before any comparison of L = 15.480 with constants:


```text
1. Candidate list is fixed in advance.


2. Tolerance is fixed in advance.


3. A control is computed:
   base rate of accidental matches
   for random numbers in the same range
   under the same tolerance.
```


No candidate is added after seeing L.


No constant is declared structural without passing the control.


---


8. Fit stress tests


Before sealing the floor, two further checks will be run:


```text
1. Systematic error:
   compare L under at least two alternative
   asymptotic forms, not only L − k/N^p.


2. Drop N = 300:
   refit on N = 400, 500, 600, 700
   and report the shift in L.
```


---


9. Status


```text
The floor is filed as:


L = 15.480 ± 0.006


measured, not yet proven structural.


Independent audit requires:
  - b(p^m) artifact;
  - full rebuild of A_fixed;
  - second-engine diagonalization.
```


I will send the artifact next.


---


END OF RESPONSE


```