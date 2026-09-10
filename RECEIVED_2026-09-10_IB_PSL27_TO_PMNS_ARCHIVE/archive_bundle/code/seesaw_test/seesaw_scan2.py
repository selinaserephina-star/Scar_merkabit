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
axis3 = [np.array([1.,0.,0.]), np.array([0.,1.,0.]), np.array([0.,0.,1.])]
pd = np.array([0.,1.]); phi = eps*pd

with open('/home/claude/neutrino/UL_dict.pkl','rb') as f: UL_dict = pickle.load(f)
with open('/home/claude/neutrino/charged_lepton_fits.pkl','rb') as f: ch_fits = pickle.load(f)
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
Dm31_phys = 2.53e-3

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),0,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(U[0,2]))
    return th12,th23,th13

def build_Mnu_seesaw(yD1,yD2,yD3,MN,chi_ax,cx3_dir):
    YD = yD1*Y3_of(axis3[chi_ax]) + yD2*Y3_of(cx3_dir) + yD3*Y2_of(*phi)
    Mnu = -(YD @ YD.T) / MN
    return Mnu

def eval_point(p, chi_ax, cx3_dir, UL):
    yD1,yD2,yD3,MN = p
    if MN <= 0: return None
    Mnu = build_Mnu_seesaw(yD1,yD2,yD3,MN,chi_ax,cx3_dir)
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

def residual5(p, chi_ax, cx3_dir, UL, target_mnu):
    r = eval_point(p,chi_ax,cx3_dir,UL)
    if r is None: return np.array([10]*5)
    th12,th23,th13,rat,Summnu = r
    return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,
                      (rat-ratio_t)/ratio_t,(Summnu-target_mnu)/target_mnu])

def best_fit(chi_ax, xi_ax, target_mnu, nstarts=250, seed=0):
    c3p_here = ch_fits[(chi_ax,xi_ax)][1][2]
    chi_v = axis3[chi_ax]; xi_v = c3p_here*axis3[xi_ax]
    cx3 = cross3(chi_v,xi_v)
    if np.linalg.norm(cx3)<1e-12: return None
    cx3_dir = cx3/np.linalg.norm(cx3)
    UL = UL_dict[(chi_ax,xi_ax)]
    best=None
    rng=np.random.default_rng(seed)
    for _ in range(nstarts):
        p0 = np.array([rng.uniform(-5,5), rng.uniform(-5,5), rng.uniform(-5,5), 10**rng.uniform(-2,3)])
        try:
            res=least_squares(residual5,p0,args=(chi_ax,cx3_dir,UL,target_mnu),
                               method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    if best is None: return None
    r = eval_point(best[1],chi_ax,cx3_dir,UL)
    return best[0], best[1], r

print("=== Seesaw + phi2-Dirac term, target Sum(mnu)=0.06 eV ===\n")
print(f"{'chi':>4}{'xi':>4}{'cost':>12}{'th12':>8}{'th23':>8}{'th13':>8}{'Sum_mnu':>10}")
results = {}
for chi_ax in range(3):
  for xi_ax in range(3):
    if chi_ax==xi_ax: continue
    r = best_fit(chi_ax,xi_ax,0.06,nstarts=250,seed=chi_ax*10+xi_ax+100)
    if r is None:
        print(f"{chi_ax:>4}{xi_ax:>4}   FAILED"); continue
    cost,p,obs = r
    results[(chi_ax,xi_ax)] = (cost,p,obs)
    print(f"{chi_ax:>4}{xi_ax:>4}{cost:>12.5f}{np.degrees(obs[0]):>8.2f}{np.degrees(obs[1]):>8.2f}{np.degrees(obs[2]):>8.2f}{obs[4]:>10.4f}")

with open('seesaw_results2.pkl','wb') as f: pickle.dump(results,f)
