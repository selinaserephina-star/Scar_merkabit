"""
_explore_fano_coexistence_why_2026-09-14.py   [FREE EXPLORATION, NOT SEALED]

Fork A, open end 3: WHY does Ilya's coexistence window (two structurally
distinct stable vacua from one potential) sit where it does?

Built directly on his fano_coexistence_region.py definitions (same V4-slice,
same potential incl. the sextic I_prod, same S4/S2 vacua, same stability test).

Two questions:
  (Q1) BRACKETING: along the A->B interpolation, track the S4 vacuum's least
       Hessian eigenvalue and the S2 vacuum's least eigenvalue. The window
       should be exactly the overlap {S4 stable} ∩ {S2 exists & stable};
       its two edges are (left) the S2 minimum turning stable / appearing,
       (right) the S4 minimum destabilising. That *is* "why there".
  (Q2) IS THE SEXTIC NEEDED? Ilya's window has kappa_prod=-0.007 (tiny).
       Set kappa_prod=0 (pure-quartic-in-5 potential), re-fix m^2 for S4
       criticality, and test whether coexistence survives. Scan kappa_prod
       to map the coexistence boundary in that coupling.
"""
import numpy as np
from scipy.optimize import fsolve, brentq

lines=[[0,3,4],[1,3,5],[0,1,2],[2,4,5],[2,3,6],[0,5,6],[1,4,6]]
complement=[1,2,5,6]
def build_phi(a,b,c):
    d=-(a+b+c)/4; phi=[0.0]*7; phi[0]=a; phi[3]=b; phi[4]=c
    for p in complement: phi[p]=d
    return phi
def I_g1(p): return (sum(x**2 for x in p))**2
def I_g2(p): return sum(x**4 for x in p)
def I_line(p): return sum((p[x]+p[y]+p[z])**4 for (x,y,z) in lines)
def I_prod(p): return sum(p[x]*p[y]*p[z] for (x,y,z) in lines)**2
def I_mixed(p):
    total=sum(x**2 for x in p); return sum((p[x]+p[y]+p[z])**2*(total-p[x]**2-p[y]**2-p[z]**2) for (x,y,z) in lines)
def V7(phi7,m2,k1,k2,k3,k4,k5):
    return -m2*sum(x**2 for x in phi7)+k1*I_g1(phi7)+k2*I_g2(phi7)+k3*I_line(phi7)+k4*I_prod(phi7)+k5*I_mixed(phi7)
def V_abc(a,b,c,m2,k): return V7(build_phi(a,b,c),m2,*k)
def grad3(a,b,c,m2,k,h=1e-5):
    return [(V_abc(a+h,b,c,m2,k)-V_abc(a-h,b,c,m2,k))/(2*h),
            (V_abc(a,b+h,c,m2,k)-V_abc(a,b-h,c,m2,k))/(2*h),
            (V_abc(a,b,c+h,m2,k)-V_abc(a,b,c-h,m2,k))/(2*h)]
def full_hessian(phi7,m2,k,h=1e-4):
    n=7; H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            p1=list(phi7);p1[i]+=h;p1[j]+=h; p2=list(phi7);p2[i]+=h;p2[j]-=h
            p3=list(phi7);p3[i]-=h;p3[j]+=h; p4=list(phi7);p4[i]-=h;p4[j]-=h
            H[i,j]=(V7(p1,m2,*k)-V7(p2,m2,*k)-V7(p3,m2,*k)+V7(p4,m2,*k))/(4*h*h)
    return H
def min_eig(phi7,m2,k): return float(np.min(np.linalg.eigvalsh(full_hessian(phi7,m2,k))))
def is_stable(phi7,m2,k):
    return all(e>-1e-4*max(1,abs(e)) for e in np.linalg.eigvalsh(full_hessian(phi7,m2,k)))
def find_s4(k,m2):
    def f(t): return grad3(t,t,t,m2,k)[0]
    ts=np.linspace(0.01,3,400); vals=[f(t) for t in ts]; roots=[]
    for i in range(len(ts)-1):
        if vals[i]*vals[i+1]<0: roots.append(brentq(f,ts[i],ts[i+1]))
    return roots
def find_s2(k,m2):
    res=[]
    def eqs(v):
        a,b=v; g=grad3(a,b,b,m2,k); return [g[0],g[1]]
    for a0 in [0.1,0.5,1.0,-0.5,-1.0,1.5,2.0]:
        for b0 in [-0.5,0.1,-1.0,0.5,-0.2,-0.05]:
            try:
                sol,info,ier,msg=fsolve(eqs,[a0,b0],full_output=True)
                if ier==1 and max(abs(x) for x in eqs(sol))<1e-6 and np.linalg.norm(sol)>1e-3 and abs(sol[0]-sol[1])>1e-2:
                    if not any(abs(sol[0]-r[0])<1e-3 and abs(sol[1]-r[1])<1e-3 for r in res): res.append(tuple(sol))
            except Exception: pass
    return res

kA=np.array([1,2/3,0.1,0,1]); m2A=brentq(lambda m2:grad3(1,1,1,m2,kA)[0],0.001,1000)
kB=np.array([1.933,0.890,0.697,-0.055,1.699]); m2B=4.368
print(f"[0] endpoints: m2A={m2A:.4f}, m2B={m2B}")

# ---------- Q1: bracketing along the interpolation ----------
print("\n[Q1] tracking S4 and S2 stability along A->B (min Hessian eigenvalue):")
print(f"    {'t':>6} {'S4 exists':>9} {'S4 minEig':>10} {'S4 stab':>8} | {'S2 exists':>9} {'S2 minEig':>10} {'S2 stab':>8} | coexist")
left=right=None
for t in np.linspace(0.0,0.30,31):
    k=(1-t)*kA+t*kB; m2=(1-t)*m2A+t*m2B
    s4=find_s4(k,m2)
    s4e=max([min_eig(build_phi(r,r,r),m2,k) for r in s4],default=None) if s4 else None
    s4ok=any(is_stable(build_phi(r,r,r),m2,k) for r in s4)
    s2=find_s2(k,m2)
    s2e=max([min_eig(build_phi(a,b,b),m2,k) for (a,b) in s2],default=None) if s2 else None
    s2ok=any(is_stable(build_phi(a,b,b),m2,k) for (a,b) in s2)
    co="  <== BOTH" if (s4ok and s2ok) else ""
    if co and left is None: left=t
    if co: right=t
    def fmt(x): return f"{x:10.3f}" if x is not None else f"{'--':>10}"
    print(f"    {t:6.3f} {str(bool(s4)):>9} {fmt(s4e)} {str(s4ok):>8} | {str(bool(s2)):>9} {fmt(s2e)} {str(s2ok):>8} |{co}")
print(f"\n    => coexistence window t in [{left},{right}]. Left edge = S2 min turns stable; right edge = S4 min destabilises.")

# ---------- Q2: is the sextic kappa_prod needed? ----------
t=0.125; k_mid=(1-t)*kA+t*kB; m2_mid=(1-t)*m2A+t*m2B
print(f"\n[Q2] at the window point t=0.125, k_prod={k_mid[3]:.4f} (tiny). Vary k_prod, refix m2 for S4 criticality:")
def coexists(k):
    # refix m2 so S4 point at scale ~ current S4 root is critical (fix at scale 1 like point A convention)
    try: m2=brentq(lambda m2:grad3(1,1,1,m2,k)[0],-1000,1000)
    except Exception: return None,None,None
    s4=find_s4(k,m2); s4ok=any(is_stable(build_phi(r,r,r),m2,k) for r in s4)
    s2=find_s2(k,m2); s2ok=any(is_stable(build_phi(a,b,b),m2,k) for (a,b) in s2)
    return s4ok,s2ok,m2
print(f"    {'k_prod':>9} {'m2':>9} {'S4 stab':>8} {'S2 stab':>8}  coexist")
for kp in [-0.10,-0.05,-0.02,-0.007,0.0,0.007,0.02,0.05]:
    k=k_mid.copy(); k[3]=kp
    s4ok,s2ok,m2=coexists(k)
    co="  <== BOTH" if (s4ok and s2ok) else ""
    print(f"    {kp:9.3f} {(m2 if m2 else 0):9.3f} {str(s4ok):>8} {str(s2ok):>8}{co}")

# ---------- Q2b: pure-quartic (k_prod=0) full interpolation-style search ----------
print(f"\n[Q2b] with k_prod=0 identically, scan t in [0,0.3] (refix m2 at scale 1) for any coexistence:")
found=[]
for t in np.linspace(0.0,0.30,31):
    k=(1-t)*kA+t*kB; k[3]=0.0
    s4ok,s2ok,m2=coexists(k)
    if s4ok and s2ok: found.append(round(t,3))
print(f"    pure-quartic coexistence at t = {found if found else 'NONE FOUND'}")
print("\nDone. [free exploration; not a sealed stone]")
