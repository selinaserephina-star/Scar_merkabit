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
Dm31_phys = 2.53e-3
Summnu_t = 0.07

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),-1,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13

TVAL = {'theta12':th12_t,'theta23':th23_t,'theta13':th13_t,'ratio':ratio_t,'Summnu':Summnu_t}
TARGETS5 = ['theta12','theta23','theta13','ratio','Summnu']

def make_stuff(chi_ax, xi_ax, c3p_here):
    chi = axis3[chi_ax]; xi = c3p_here*axis3[xi_ax]
    cx3 = cross3(chi,xi)
    if np.linalg.norm(cx3)<1e-10: return None
    cx3_dir = cx3/np.linalg.norm(cx3)
    a6,b6 = channel2_from_squares(chi)
    return chi, cx3_dir, a6, b6

def observables(p, chi, cx3_dir, a6, b6, UL):
    m0,m2,m3,mcross,m6 = p
    Mnu = m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi) + mcross*Y3_of(cx3_dir) + m6*Y2_of(a6,b6)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    PMNS = UL.T@V
    th12,th23,th13=pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    if dm31<1e-30: return None
    rat = dm21/dm31
    k = np.sqrt(Dm31_phys/dm31)
    return th12,th23,th13,rat,np.sum(masses)*k

def residuals(p, chi,cx3_dir,a6,b6,UL, names):
    r = observables(p, chi,cx3_dir,a6,b6,UL)
    if r is None: return np.array([10]*len(names))
    d = {'theta12':r[0],'theta23':r[1],'theta13':r[2],'ratio':r[3],'Summnu':r[4]}
    return np.array([(d[n]-TVAL[n])/abs(TVAL[n]) for n in names])

print("="*70)
print("HONEST test: 5 params (m0,m2,m3,mcross,m6), 5 TARGETS incl Sum_mnu=0.07")
print("Checked across ALL 9 axis combinations")
print("="*70)
print(f"{'chi':>4}{'xi':>4}{'ch.cost':>12}{'nu.cost':>10}{'rank':>6}{'null(m2)':>10}{'th12':>8}{'th23':>8}{'th13':>8}{'Summnu':>8}")

for chi_ax in range(3):
  for xi_ax in range(3):
    if chi_ax==xi_ax:
        print(f"{chi_ax:>4}{xi_ax:>4}   SKIPPED")
        continue
    c3p_here = ch_fits[(chi_ax,xi_ax)][1][2]
    ch_cost = ch_fits[(chi_ax,xi_ax)][0]
    stuff = make_stuff(chi_ax,xi_ax,c3p_here)
    if stuff is None:
        print(f"{chi_ax:>4}{xi_ax:>4}   cross vanishes")
        continue
    chi,cx3_dir,a6,b6 = stuff
    UL = UL_dict[(chi_ax,xi_ax)]
    best=None
    rng=np.random.default_rng(2000+chi_ax*10+xi_ax)
    for _ in range(400):
        p0 = rng.uniform(-30,30,5)
        try:
            res=least_squares(lambda p: residuals(p,chi,cx3_dir,a6,b6,UL,TARGETS5),p0,method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    if best is None:
        print(f"{chi_ax:>4}{xi_ax:>4}   fit failed")
        continue
    # jacobian
    def numjac(p,h=1e-6):
        n=5; m=5
        J=np.zeros((m,n))
        for j in range(n):
            hh=h*max(1,abs(p[j]))
            pp=p.copy(); pp[j]+=hh
            pm=p.copy(); pm[j]-=hh
            J[:,j]=(residuals(pp,chi,cx3_dir,a6,b6,UL,TARGETS5)-residuals(pm,chi,cx3_dir,a6,b6,UL,TARGETS5))/(2*hh)
        return J
    J = numjac(best[1])
    S = np.linalg.svd(J,compute_uv=False)
    rank = np.sum(S>1e-8*S[0])
    U_,S_,Vt_ = np.linalg.svd(J)
    null_m2 = abs(Vt_[-1,1]) if rank<5 else 0.0
    r = observables(best[1],chi,cx3_dir,a6,b6,UL)
    print(f"{chi_ax:>4}{xi_ax:>4}{ch_cost:>12.2e}{best[0]:>10.4f}{rank:>6}{null_m2:>10.3f}{np.degrees(r[0]):>8.2f}{np.degrees(r[1]):>8.2f}{np.degrees(r[2]):>8.2f}{r[4]:>8.4f}")
