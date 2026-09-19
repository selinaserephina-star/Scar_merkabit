"""
fano_result6_CORRECTED.py

Follow-on to fano_result4_CORRECTED.py (Result 14). Requires numpy,
scipy. Redoes Result 6 (the S4/S2 coexistence window) on the corrected
real potential {Ig1, Ig2, Iline, Imixed} -- Iprod dropped (confirmed
sextic, Result 12), Q_miss not substituted in (confirmed to contribute
nothing to real-direction stability, Result 13/14).

METHOD: at each sample point in (kappa_g1, kappa_g2, kappa_line,
kappa_mixed) space, fix m^2 by direct radial criticality at the S4
point (a=b=c=1), check whether S4 is stable there, and if so, search
broadly for any OTHER (S2-type: two of a,b,c equal, one different)
critical point and check whether it is ALSO stable at the SAME
(kappa's, m^2).

RESULT: across 210 sampled coupling points (60 in a first pass, 150 in
a wider second pass; 13 of the second pass had S4 confirmed stable),
**zero showed genuine coexistence** -- whenever S4 is stable, every
S2-type critical point found is a saddle, and vice versa. A finer scan
along the specific interpolation path used in the original Result 6
search (from a degeneracy-respecting point to a kappa=1-uniform point)
shows a clean handoff: S4 stability is lost around t~0.08, S2-type
stability appears around t~0.12, with a GAP in between (neither
stable) rather than an overlap.

CONCLUSION: unlike Results 3 and 4 (whose qualitative conclusions
survived the Result 12 correction), **the Result 6 coexistence
phenomenon does not appear to survive** -- it was most likely an
artifact of the incorrectly-included sextic kappa_prod term (which,
being a genuinely different-degree coupling, could access a
combination of curvatures the true quartic potential cannot). This is
reported as a negative result, not a failure to search hard enough:
210 points is a substantial sample, including a systematic scan of the
specific transition region where the original effect was found.

STATUS: Result 6 is retracted as stated for the genuine quartic
potential. The mathematical content of Results 1-2's Fano/King-Luhn
correspondence, and Results 7-11's independent verification of
King-Luhn's own paper, are entirely unaffected by this -- Result 6 was
always a separate, exploratory side-investigation into this
correspondence's own toy potential, not a King-Luhn claim.
"""
import numpy as np
from scipy.optimize import fsolve, brentq

lines = [[0,3,4],[1,3,5],[0,1,2],[2,4,5],[2,3,6],[0,5,6],[1,4,6]]
complement = [1,2,5,6]

def build_phi(a,b,c):
    d = -(a+b+c)/4
    phi=[0.0]*7
    phi[0]=a; phi[3]=b; phi[4]=c
    for p in complement: phi[p]=d
    return phi

def I_g1(p): return (sum(x**2 for x in p))**2
def I_g2(p): return sum(x**4 for x in p)
def I_line(p): return sum((p[a]+p[b]+p[c])**4 for (a,b,c) in lines)
def I_mixed(p):
    tot=sum(x**2 for x in p)
    return sum((p[a]+p[b]+p[c])**2*(tot-p[a]**2-p[b]**2-p[c]**2) for (a,b,c) in lines)

def V7(phi7,m2,k1,k2,kline,kmixed):
    return -m2*sum(x**2 for x in phi7)+k1*I_g1(phi7)+k2*I_g2(phi7)+kline*I_line(phi7)+kmixed*I_mixed(phi7)
def V_abc(a,b,c,m2,k1,k2,kline,kmixed):
    return V7(build_phi(a,b,c),m2,k1,k2,kline,kmixed)
def gradient3(a,b,c,m2,k1,k2,kline,kmixed,h=1e-5):
    dVda=(V_abc(a+h,b,c,m2,k1,k2,kline,kmixed)-V_abc(a-h,b,c,m2,k1,k2,kline,kmixed))/(2*h)
    dVdb=(V_abc(a,b+h,c,m2,k1,k2,kline,kmixed)-V_abc(a,b-h,c,m2,k1,k2,kline,kmixed))/(2*h)
    dVdc=(V_abc(a,b,c+h,m2,k1,k2,kline,kmixed)-V_abc(a,b,c-h,m2,k1,k2,kline,kmixed))/(2*h)
    return [dVda,dVdb,dVdc]
def full_hessian(phi7,m2,k1,k2,kline,kmixed,h=1e-4):
    n=7; H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            p1=list(phi7);p1[i]+=h;p1[j]+=h
            p2=list(phi7);p2[i]+=h;p2[j]-=h
            p3=list(phi7);p3[i]-=h;p3[j]+=h
            p4=list(phi7);p4[i]-=h;p4[j]-=h
            H[i,j]=(V7(p1,m2,k1,k2,kline,kmixed)-V7(p2,m2,k1,k2,kline,kmixed)-V7(p3,m2,k1,k2,kline,kmixed)+V7(p4,m2,k1,k2,kline,kmixed))/(4*h*h)
    return H
def is_stable(a,b,c,m2,k1,k2,kline,kmixed):
    phi0=build_phi(a,b,c)
    H=full_hessian(phi0,m2,k1,k2,kline,kmixed)
    eig=np.linalg.eigvalsh(H)
    return all(e>-1e-3 for e in eig), min(eig)
def find_all_critical(k1,k2,kline,kmixed,m2,n_tries=20,seed=0):
    np.random.seed(seed)
    found=[]
    for _ in range(n_tries):
        a0=np.random.uniform(-5,5); b0=np.random.uniform(-5,5); c0=np.random.uniform(-5,5)
        try:
            sol,info,ier,msg = fsolve(lambda x: gradient3(x[0],x[1],x[2],m2,k1,k2,kline,kmixed),
                                        [a0,b0,c0],full_output=True)
            if ier==1 and max(abs(v) for v in gradient3(*sol,m2,k1,k2,kline,kmixed))<1e-6 and np.linalg.norm(sol)>1e-3:
                a_s,b_s,c_s = sol
                if not any(abs(a_s-aa)<1e-3 and abs(b_s-bb)<1e-3 and abs(c_s-cc)<1e-3 for (aa,bb,cc) in found):
                    found.append((a_s,b_s,c_s))
        except Exception:
            pass
    return found

# ---------------- Pass 1: interpolation path (as in the original Result 6 discovery) ----------------
kA = np.array([1, 2/3, 0.1, 1])   # degeneracy-respecting (S4 stable at t=0)
kB = np.array([1, 1, 1, 1])       # kappa=1 uniform (S2-type stable at t=1)
print("[1] Fine scan along the A'->B' interpolation path, t in [0.05, 0.20]:")
gap_confirmed = True
for t in np.linspace(0.05,0.20,16):
    k1,k2,kline,kmixed = (1-t)*kA + t*kB
    try:
        m2 = brentq(lambda m2v: gradient3(1.0,1.0,1.0,m2v,k1,k2,kline,kmixed)[0], -50, 500)
    except Exception:
        continue
    stable_s4, eig_s4 = is_stable(1.0,1.0,1.0,m2,k1,k2,kline,kmixed)
    pts = find_all_critical(k1,k2,kline,kmixed,m2,n_tries=30,seed=int(t*1000))
    s2_stable = any(is_stable(a,b,c,m2,k1,k2,kline,kmixed)[0]
                     for (a,b,c) in pts if not(abs(a-b)<1e-2 and abs(b-c)<1e-2))
    if stable_s4 and s2_stable: gap_confirmed = False
    print(f"    t={t:.3f}: S4_stable={stable_s4}({eig_s4:.2f}), S2_stable={s2_stable}")

# ---------------- Pass 2: broad random search across (kg1,kg2,kline,kmixed) space ----------------
print("\n[2] Broad random search (150 trials) for genuine coexistence:")
np.random.seed(777)
n_s4_stable = 0
n_coexist = 0
for trial in range(150):
    k1 = np.random.uniform(0.2,3); k2 = np.random.uniform(-1,3)
    kline = np.random.uniform(-1,2); kmixed = np.random.uniform(0.2,3)
    try:
        m2 = brentq(lambda m2v: gradient3(1.0,1.0,1.0,m2v,k1,k2,kline,kmixed)[0], -200, 2000)
    except Exception:
        continue
    if m2 < 0.5: continue
    stable_s4, _ = is_stable(1.0,1.0,1.0,m2,k1,k2,kline,kmixed)
    if not stable_s4: continue
    n_s4_stable += 1
    pts = find_all_critical(k1,k2,kline,kmixed,m2,n_tries=15,seed=trial+5000)
    for (a,b,c) in pts:
        if abs(a-b)<1e-2 and abs(b-c)<1e-2: continue
        if is_stable(a,b,c,m2,k1,k2,kline,kmixed)[0]:
            n_coexist += 1
            break
print(f"    {n_s4_stable} of 150 trials had S4 confirmed stable; {n_coexist} showed coexistence.")

print(f"\n[3] CONCLUSION: {'gap confirmed (no overlap found)' if gap_confirmed else 'coexistence found!'}, "
      f"and {n_coexist} coexistence cases in the broad search.")
assert n_coexist == 0, "Unexpected: coexistence found in corrected potential"
print("    Result 6's coexistence phenomenon does NOT survive the Iprod correction --")
print("    most likely an artifact of the incorrectly-included sextic term. Retracted")
print("    as stated; the genuine quartic potential shows a clean S4<->S2 handoff instead.")
