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
    d=np.array([v[0]**2,v[1]**2,v[2]**2]); d=d-np.mean(d)
    a=d[0]/2; b=(d[1]-d[2])/(2*np.sqrt(3))
    return np.array([a,b])
axis3 = [np.array([1.,0.,0.]), np.array([0.,1.,0.]), np.array([0.,0.,1.])]
pd = np.array([0.,1.]); phi = eps*pd

with open('UL_dict.pkl','rb') as f: UL_dict = pickle.load(f)
with open('charged_lepton_fits.pkl','rb') as f: ch_fits = pickle.load(f)
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
Dm31_phys = 2.53e-3
TARGET_MNU = 0.07   # safely within cosmological bounds -- the meaningful physical test

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),-1,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13

def build_Mnu(m0,m2,m3,mcross,m5, chi_axis, cx3_dir, ab2_dir):
    return (m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(axis3[chi_axis]) + mcross*Y3_of(cx3_dir)
            + m5*Y2_of(*ab2_dir))

def eval_point(p, chi_axis, cx3_dir, ab2_dir, UL):
    m0,m2,m3,mcross,m5 = p
    Mnu = build_Mnu(m0,m2,m3,mcross,m5, chi_axis, cx3_dir, ab2_dir)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    PMNS = UL.T@V
    th12,th23,th13=pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    if dm31<1e-30: return None
    rat=dm21/dm31
    k=np.sqrt(Dm31_phys/dm31)
    Summnu=np.sum(masses)*k
    return th12,th23,th13,rat,Summnu

def residual5(p, chi_axis, cx3_dir, ab2_dir, UL):
    r = eval_point(p, chi_axis, cx3_dir, ab2_dir, UL)
    if r is None: return np.array([10]*5)
    th12,th23,th13,rat,Summnu = r
    return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,
                      (rat-ratio_t)/ratio_t,(Summnu-TARGET_MNU)/TARGET_MNU])

print(f"=== AXIS STABILITY CHECK: new 2-channel operator, target Sum(mnu)={TARGET_MNU} ===\n")
print(f"{'chi':>4}{'xi':>4}{'cost':>12}{'th12':>8}{'th23':>8}{'th13':>8}{'Sum_mnu':>10}")

for chi_ax in range(3):
  for xi_ax in range(3):
    if chi_ax==xi_ax:
        print(f"{chi_ax:>4}{xi_ax:>4}   SKIPPED (degenerate)")
        continue
    c3p_here = ch_fits[(chi_ax,xi_ax)][1][2]
    chi_v = axis3[chi_ax]; xi_v = c3p_here*axis3[xi_ax]
    cx3 = cross3(chi_v,xi_v)
    if np.linalg.norm(cx3)<1e-12:
        print(f"{chi_ax:>4}{xi_ax:>4}   cross vanishes"); continue
    cx3_dir = cx3/np.linalg.norm(cx3)
    ab2 = channel2_from_squares(chi_v)  # Phi3 on ITS OWN axis for this combo
    if np.linalg.norm(ab2)<1e-12:
        print(f"{chi_ax:>4}{xi_ax:>4}   ab2 vanishes"); continue
    ab2_dir = ab2/np.linalg.norm(ab2)
    UL = UL_dict[(chi_ax,xi_ax)]
    best=None
    rng=np.random.default_rng(500+chi_ax*10+xi_ax)
    for _ in range(500):
        p0=rng.uniform(-30,30,5)
        try:
            res=least_squares(lambda p: residual5(p,chi_ax,cx3_dir,ab2_dir,UL),p0,method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    r = eval_point(best[1],chi_ax,cx3_dir,ab2_dir,UL)
    if r:
        print(f"{chi_ax:>4}{xi_ax:>4}{best[0]:>12.4e}{np.degrees(r[0]):>8.2f}{np.degrees(r[1]):>8.2f}{np.degrees(r[2]):>8.2f}{r[4]:>10.4f}")
