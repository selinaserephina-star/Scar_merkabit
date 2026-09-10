import numpy as np
from scipy.optimize import least_squares
import pickle
import warnings
warnings.filterwarnings('ignore')

eps=0.06
def Y2_of(a,b): return np.diag([2*a,-a+np.sqrt(3)*b,-a-np.sqrt(3)*b])
def Y3_of(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def cross3(chi,xi):
    return np.array([chi[1]*xi[2]-chi[2]*xi[1], chi[2]*xi[0]-chi[0]*xi[2], chi[0]*xi[1]-chi[1]*xi[0]])
def channel2_from_squares(v):
    d = np.array([v[0]**2,v[1]**2,v[2]**2]); d=d-np.mean(d)
    return d[0]/2, (d[1]-d[2])/(2*np.sqrt(3))
axis3 = [np.array([1.,0.,0.]), np.array([0.,1.,0.]), np.array([0.,0.,1.])]
pd = np.array([0.,1.]); phi = eps*pd

with open('UL_dict.pkl','rb') as f: UL_dict = pickle.load(f)
with open('charged_lepton_fits.pkl','rb') as f: ch_fits = pickle.load(f)
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),-1,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13

def build_Mnu(m0,m2,m3,mdiag2,chi_ax,xi_ax,c3p):
    chi = axis3[chi_ax]; xi = c3p*axis3[xi_ax]
    cx3 = cross3(chi,xi)
    mcross = (eps*c3p)*m3
    a2b2 = channel2_from_squares(xi)
    return (m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi)
            + mcross*Y3_of(cx3) + mdiag2*Y2_of(*a2b2))

def residual(p, chi_ax, xi_ax, UL, c3p):
    m0,m2,m3,mdiag2 = p
    Mnu = build_Mnu(m0,m2,m3,mdiag2,chi_ax,xi_ax,c3p)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    PMNS = UL.T@V
    th12,th23,th13=pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    rat = dm21/dm31 if dm31!=0 else 1e6
    return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,(rat-ratio_t)/ratio_t])

Dm31_phys = 2.53e-3
print(f"{'chi':>4}{'xi':>4}{'ch.cost':>12}{'nu.cost':>10}{'Sum_mnu(meV)':>14}")
for chi_ax in range(3):
  for xi_ax in range(3):
    if chi_ax==xi_ax:
        print(f"{chi_ax:>4}{xi_ax:>4}   SKIPPED (degenerate)")
        continue
    c3p_here = ch_fits[(chi_ax,xi_ax)][1][2]
    ch_cost = ch_fits[(chi_ax,xi_ax)][0]
    UL = UL_dict[(chi_ax,xi_ax)]
    best=None
    rng=np.random.default_rng(chi_ax*10+xi_ax+50)
    for _ in range(500):
        p0 = rng.uniform(-30,30,4)
        try:
            res=least_squares(residual,p0,args=(chi_ax,xi_ax,UL,c3p_here),method='lm',max_nfev=5000,xtol=1e-15,ftol=1e-15)
            cost=np.sum(res.fun**2)
            if np.isfinite(cost) and (best is None or cost<best[0]): best=(cost,res.x)
        except Exception: continue
    nu_cost,p=best
    m0,m2,m3,mdiag2=p
    Mnu=build_Mnu(m0,m2,m3,mdiag2,chi_ax,xi_ax,c3p_here)
    w,V=np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]; masses=np.abs(w)
    dm31 = masses[2]**2-masses[0]**2
    k = np.sqrt(Dm31_phys/dm31) if dm31>0 else np.nan
    summnu = np.sum(masses*k)*1000 if dm31>0 else np.nan
    print(f"{chi_ax:>4}{xi_ax:>4}{ch_cost:>12.2e}{nu_cost:>10.6f}{summnu:>14.2f}")
