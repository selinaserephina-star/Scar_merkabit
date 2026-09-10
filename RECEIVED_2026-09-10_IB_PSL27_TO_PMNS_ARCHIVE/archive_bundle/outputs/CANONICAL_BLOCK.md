# CANONICAL_BLOCK — Verified Reference Constants for the PSL(2,7)→S₄ Lepton Project

**Purpose:** the single source of truth for the numerical constants and conventions used throughout this project. Read this FIRST before any new numerical work — check every constant against this file rather than recalling it from earlier context. If a computation needs a constant not listed here, derive it fresh and consider adding it.

**Status:** all values below independently re-verified this session (not carried from memory of earlier turns).

---

## 1. Group-theoretic setup

```text
PSL(2,7), order 168. chi8 (8-dim irrep) restricted to S4 subgroup:
  chi8|S4 = 2 (+) 3 (+) 3'      <- phi2 ~ 2, Phi3 ~ 3, Phi3' ~ 3'

Yukawa ratios (FIXED by PSL(2,7), not fitted):
  y2 : y3 : y3' = sqrt(3) : 1 : sqrt(2)
  y1 = 0   (structural zero, trace(Y_T)=0 forced)

Matrix conventions (established and used consistently throughout):
  Y2(v) = diag(2*v0, -v0+sqrt(3)*v1, -v0-sqrt(3)*v1)         for v=(v0,v1), the "2"
  Y3(v) = [[0,v2,v1],[v2,0,v0],[v1,v0,0]]                     for v=(v0,v1,v2), the "3"
  Y3'(v)= [[0,v2,-v1],[-v2,0,v0],[v1,-v0,0]]                  for v=(v0,v1,v2), the "3'"

Y_T = y2*Y2(phi2) + y3*Y3(Phi3) + y3'*Y3'(Phi3')
```

## 2. Established vacuum (axis choice, FN structure)

```text
phi2 direction:  (0, eps),  eps = 0.06        [phi1-component = 0]
Phi3 axis:       axis 2  (only 3rd component nonzero)   -- chi3 ~ eps^2 * c3
Phi3' axis:      axis 0  (only 1st component nonzero)   -- xi1  ~ eps * c3p

FN charges (established, NOT derived from first principles):
  phi2: charge 1     Phi3: charge 2     Phi3': charge 1
  ("+1 twist cost" rule -- economical assumption, NOT derived;
   7 messenger-based derivation attempts all failed, see MASTER_SUMMARY §3)
```

## 3. CORRECTED charged-lepton fit parameters ⚠️

```text
y2  = 8.043031
c3  = 0.64085776
c3p = 2.38809204        (this is c3', the Phi3' coefficient)

Physical VEV magnitudes at this point:
  phi2  = eps * (0, 1)                    = (0, 0.06)
  Phi3  = c3 * eps^2 * (0,0,1)             = (0, 0, 0.0023071)
  Phi3' = c3p * eps * (1,0,0)              = (0.1432855, 0, 0)

Verification: singular values of Y_T at these values EXACTLY match
  (m_e, m_mu, m_tau) = (0.000511, 0.1056584, 1.77686) GeV
  -- cost ~5e-32 (machine-precision exact), re-verified independently
     via fresh least_squares fit (not copied from memory).

*** WARNING: earlier turns in this long session used WRONG values
(y2~0.052, c3~0.537, c3p~1.884) for this same physical point. That
error was caught and corrected. If you see those old values anywhere,
they are WRONG -- use the values in this section instead. ***
```

## 4. CORRECTED neutrino-sector parameters (real-VEV / zero-phase point)

```text
M_nu = m0*I + m2*Y2(phi2) + m3*Y3(Phi3_axis) + mcross*Y3(chi x xi, normalized)

Best-fit (3000 restarts, confirmed structural limit -- matches the
independently-established "theta12/theta23 residual" finding from
earlier in this project):

  m0      =  41327.0475259
  m2      = -806652.32761013
  m3      = -70752.38857012
  mcross  =  5261.89134801

Resulting observables:
  theta12   = 32.728 deg   (target 33,   off by 0.27 deg)
  theta23   = 42.319 deg   (target 45,   off by 2.68 deg -- structural limit)
  theta13   = 8.455 deg    (target 8.5,  off by 0.05 deg)
  ratio     = 0.030000     (target 0.03, exact)
  deltaCP   = 0 deg        (exact, as required for real/zero-phase VEVs)
  Sum(m_nu) = 0.1519 eV    (target <0.072 eV -- NOT met, same standing
                             open item as before)
  cost      = 0.003646     (this IS the structural floor, confirmed by
                             3000 restarts -- not a search failure)
```

## 5. CRITICAL METHODOLOGICAL WARNING: eigh vs Takagi ⚠️⚠️⚠️

```text
M_nu is a complex SYMMETRIC matrix (M = M^T) once any VEV phase is
nonzero -- it is NOT Hermitian (M != M^dagger) in general.

numpy.linalg.eigh(M_nu) is for HERMITIAN matrices. Using it directly
on a complex-phased M_nu returns mathematically well-defined but
PHYSICALLY MEANINGLESS eigenvalues/eigenvectors.

For REAL M_nu (zero phases), M_nu IS Hermitian (real symmetric =
Hermitian), so eigh() is fine there -- the bug ONLY bites once phases
are nonzero.

CORRECT METHOD (Takagi decomposition for complex symmetric matrices):

    def takagi(Mnu):
        H = Mnu.conj().T @ Mnu
        d2, W = np.linalg.eigh(H)
        d2 = np.clip(d2, 0, None)
        Dc = W.T @ Mnu @ W
        ph = np.angle(np.diag(Dc) + 1e-300)
        Wt = W * np.exp(-1j*ph/2)[None,:]
        dnu = np.sqrt(d2)
        order = np.argsort(dnu)
        return dnu[order], Wt[:,order]

ALWAYS use this (not plain eigh) for M_nu whenever ANY complex phase
is present anywhere in the construction -- including INSIDE any
optimizer residual function, not just for final/display computation.
This exact bug produced unreliable delta_CP and ratio values in an
earlier complex-VEV scan this session (150 points) before being
caught and fixed.
```

## 6. δ_CP extraction convention

```text
Do NOT use delta_CP = arcsin(J/denom) -- mathematically restricted to
+-90 deg by construction, cannot represent the true range.

CORRECT: standard PDG-like rephasing -- make the first PMNS column
real and positive, then read delta_CP from the rephased U_e3:

    ph_rows = np.angle(PMNS[:,0])
    R = PMNS * np.exp(-1j*ph_rows)[:,None]
    deltaCP = -np.degrees(np.angle(R[0,2]))     # R[0,2] = rephased U_e3

This recovers the full +-180 deg range.
```

## 7. Known degeneracy in the neutrino fit (complex-phase case)

```text
At FIXED nonzero flavon phases, the 4-parameter (m0,m2,m3,mcross) fit
to (theta12,theta23,theta13,ratio) generically has (at least) a
two-fold degeneracy: solutions come in pairs with

    deltaCP_A + deltaCP_B = 180 deg   (exactly, at IDENTICAL cost)

Confirmed directly (e.g. 46.26 deg and -133.74 deg, cost=3.773e-07
for both, at the same phase point). Not a bug -- a genuine structural
feature. A "good fit" at fixed phases is generically found in pairs,
not uniquely -- do not assume a single optimizer run has found "the"
solution; check for the paired partner if the specific delta_CP value
matters.
```

## 8. Winding numbers (det(Y_T) as a function of complex VEVs)

```text
Discriminant locus D = det(Y_T) = 0 is a genuine codim-1 hypersurface
in the 8 complex VEVs (homogeneous cubic polynomial, 16 terms).

Winding number of D around its nearest zero to the physical point,
in the phi1 direction: w = 1 (simple zero, confirmed by contour
integration at 3 radii).

Winding number of D as EACH VEV phase circles 0->2pi (others fixed),
confirmed at MULTIPLE independent base points (point-independent,
structural):

  w(alpha2) = 1   [phi2's phase -- enters 2 diagonal Y_T entries]
  w(beta3)  = 2   [Phi3's phase -- enters a symmetric off-diagonal
                    PAIR of entries that co-occur in one determinant
                    monomial, doubling the winding]
  w(gamma1) = 0   [Phi3''s phase -- STRICT identity, not "zero net
                    winding despite dependence": D is machine-precision
                    CONSTANT in gamma1, because phi1=0 always makes the
                    only xi1-dependent term in D ("2*phi1*xi1^2")
                    vanish identically]
```

## 9. Standard physical targets used throughout

```text
theta12 ~ 33.0 deg      theta23 ~ 45.0 deg      theta13 ~ 8.5 deg
Dm21^2/Dm31^2 (ratio) ~ 0.03      Dm31^2_phys = 2.53e-3 eV^2
Sum(m_nu) target: < 0.072 eV  (cosmological bound; NO-favored delta_CP
                                region: ~212 deg +- 26 deg, i.e. -174
                                to -122 deg in the +-180 convention)
charged lepton masses: m_e=0.000511, m_mu=0.1056584, m_tau=1.77686 GeV
```

---

*Before starting new numerical work on this project: read this file, use these constants, and if you derive something that should become canonical (a new verified constant, a corrected value, a new convention), update this file explicitly rather than letting it drift into only the narrative FINDING files.*
