"""
_explore_kingluhn_sqrt7_derivation_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A, final: reproduce King-Luhn's exact top-alignment relation
    kappa_2 = kappa_3 = kappa_4 + kappa_5/sqrt7
from their RAW definitions (arXiv:0912.1344, eqs 4.1-4.7 and the top VEV 2.10),
transcribed verbatim from the arXiv HTML. Method: build their six quartic
invariants in their own chi-basis, impose that <chi_top> is a critical point
of the general potential (grad V = 0), and read off the linear relations forced
on the couplings. Reproducing kappa_2=kappa_3 and kappa_2=kappa_4+kappa_5/sqrt7
BOTH confirms the sqrt(7) analytically AND validates the transcription.

Invariants (their eqs):
  Upsilon = sum_i chi_i^2                 (holomorphic singlet)
  Theta, Theta' : the two quadratic 6->6 maps (eqs 4.x), transcribed below
  I1 = |Upsilon|^2
  I2 = |Theta|^2 = sum conj(Theta_i) Theta_i
  I3 = |Theta'|^2
  I4 = (1/sqrt2) sum (conj(Theta')_i Theta_i + Theta'_i conj(Theta)_i) = sqrt2 * Re<Theta'|Theta>
  I5 = (i/sqrt2) sum (conj(Theta')_i Theta_i - Theta'_i conj(Theta)_i) = -sqrt2 * Im<Theta'|Theta>
  I0 = (sum |chi_i|^2)^2                  (modulus; the potential's reference term)
(octet I6 omitted: it does not enter King-Luhn's top-alignment relation.)
"""
import numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=140)
s2,s3,s7,s14,s21=[np.sqrt(x) for x in (2,3,7,14,21)]

def Theta(c):
    c1,c2,c3,c4,c5,c6=c
    return np.array([
        -2*s21*c1*c5 - 6*c1*c6,
         2*s21*c2*c5 - 6*c2*c6,
         2*s14*c3*c4 + 8*c3*c6,
         s14*c3**2 - s14*c4**2 + 8*c4*c6,
        -s21*c1**2 + s21*c2**2 - 6*c5*c6,
        -3*c1**2 - 3*c2**2 + 4*c3**2 + 4*c4**2 - 3*c5**2 + c6**2,
    ])
def Thetap(c):
    c1,c2,c3,c4,c5,c6=c
    return np.array([
        2*s21*c2*c3 + 2*s7*c1*c4 - 2*s2*c1*c6,
        2*s21*c1*c3 + 2*s7*c2*c4 - 2*s2*c2*c6,
        2*s21*c1*c2 + 2*s7*c3*c4 - 2*s2*c3*c6,
        s7*c1**2 + s7*c2**2 + s7*c3**2 - s7*c4**2 - 2*s7*c5**2 - 2*s2*c4*c6,
        -4*s7*c4*c5 - 2*s2*c5*c6,
        -s2*c1**2 - s2*c2**2 - s2*c3**2 - s2*c4**2 - s2*c5**2 + 5*s2*c6**2,
    ])
def Ups(c): return np.sum(c*c)                      # holomorphic sum of squares

def I0(c): return (np.sum(np.abs(c)**2))**2
def I1(c): return np.abs(Ups(c))**2
def I2(c): return np.real(np.vdot(Theta(c),Theta(c)))
def I3(c): return np.real(np.vdot(Thetap(c),Thetap(c)))
def I4(c): return np.sqrt(2)*np.real(np.vdot(Thetap(c),Theta(c)))
def I5(c): return -np.sqrt(2)*np.imag(np.vdot(Thetap(c),Theta(c)))
def MASS(c): return np.sum(np.abs(c)**2)
INV=[('I0',I0),('I1',I1),('I2',I2),('I3',I3),('I4',I4),('I5',I5)]

# ---- top vacuum (2.10) ----
b7=(-1+1j*s7)/2
chi_top=((1-1j)/(3*s2))*np.array([1, 1j*s3, -1j*s3/b7, -s3/b7, -s2, 0],dtype=complex)

# ---- exact real gradient (12 reals = Re,Im) via 2-step Richardson (exact for quartics) ----
def grad12(func, c):
    x=np.concatenate([c.real,c.imag])
    def f(xx):
        cc=xx[:6]+1j*xx[6:]; return func(cc)
    g=np.zeros(12)
    for k in range(12):
        e=np.zeros(12); e[k]=1.0
        def d(h): return (f(x+h*e)-f(x-h*e))/(2*h)
        h1,h2=1e-3,2e-3
        g[k]=(h2**2*d(h1)-h1**2*d(h2))/(h2**2-h1**2)
    return g

# ---- criticality: grad V = c0 G_I0 + c1 G_I1 + ... + c5 G_I5 - m^2 G_mass = 0 ----
cols=[]
labels=[]
for nm,fn in INV:
    cols.append(grad12(fn,chi_top)); labels.append(nm)
cols.append(-grad12(MASS,chi_top)); labels.append('m2')
Mgrad=np.array(cols).T   # 12 x 7 ; columns = gradients of [I0,I1,I2,I3,I4,I5, -mass]
print(f"[1] gradient matrix at chi_top: shape {Mgrad.shape}, rank {np.linalg.matrix_rank(Mgrad,tol=1e-7)}")

# null space = coupling vectors (c0,c1,c2,c3,c4,c5,m2) making chi_top critical
u,sv,vt=np.linalg.svd(Mgrad)
tol=1e-6*sv[0]
null=vt[np.array([True]*7) & (np.concatenate([sv,[0]*(7-len(sv))])<tol)] if False else vt[len(sv[sv>tol]):]
ns=vt[[i for i in range(7) if (i>=len(sv) or sv[i]<tol)]]
print(f"    singular values: {np.round(sv,4)}")
print(f"    null-space dimension (allowed coupling families) = {ns.shape[0]}")

# ---- check King-Luhn's relations on the null space ----
idx={nm:i for i,nm in enumerate(labels)}
print("\n[2] For each null-space basis vector, the shape couplings (kappa_1..5 = c1..c5):")
print(f"    {'k1':>9}{'k2':>9}{'k3':>9}{'k4':>9}{'k5':>9}   {'k2-k3':>9}{'k2-(k4+k5/sqrt7)':>16}")
for v in ns:
    v=v/ (v[idx['I2']] if abs(v[idx['I2']])>1e-9 else 1.0)   # normalise by k2 when possible
    k1,k2,k3,k4,k5=[v[idx[x]] for x in ('I1','I2','I3','I4','I5')]
    print(f"    {k1:9.4f}{k2:9.4f}{k3:9.4f}{k4:9.4f}{k5:9.4f}   {k2-k3:9.2e}{k2-(k4+k5/s7):16.2e}")

# ---- also: general potential (free couplings) - do the criticality relations FORCE the KL relations? ----
# Solve for the two combos we care about: is {k2=k3} and {k2=k4+k5/sqrt7} satisfied by EVERY null vector?
r23=[abs((v/ (v[idx['I2']] if abs(v[idx['I2']])>1e-9 else 1))[idx['I2']]-(v/ (v[idx['I2']] if abs(v[idx['I2']])>1e-9 else 1))[idx['I3']]) for v in ns]
print(f"\n[3] max |k2 - k3| over null space           = {max(r23):.2e}")
rrel=[]
for v in ns:
    vv=v/(v[idx['I2']] if abs(v[idx['I2']])>1e-9 else 1)
    rrel.append(abs(vv[idx['I2']]-(vv[idx['I4']]+vv[idx['I5']]/s7)))
print(f"    max |k2 - (k4 + k5/sqrt7)| over null space = {max(rrel):.2e}")
print(f"    sqrt(7) = {s7:.6f}")
verdict = (max(r23)<1e-4 and max(rrel)<1e-4)
print(f"\n[4] King-Luhn relation  kappa_2 = kappa_3 = kappa_4 + kappa_5/sqrt7  "
      f"{'REPRODUCED from raw eqs + top VEV (transcription validated).' if verdict else 'NOT reproduced (transcription/basis issue - see values).'}")
print("\nDone. [free exploration; not a sealed stone]")
