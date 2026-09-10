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
c3p = 1.8842
chi = axis3[2]; xi = c3p*axis3[0]
cx3 = cross3(chi,xi); cx3_dir = cx3/np.linalg.norm(cx3)
ab2_dir = np.load('cand_2channel.npy')  # NEW direction in the (a,b) "2"-channel plane

with open('UL_dict.pkl','rb') as f: UL_dict = pickle.load(f)
UL = UL_dict[(2,0)]
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
Dm31_phys = 2.53e-3

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),-1,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13

def build_Mnu(m0,m2,m3,mcross,m5):
    # NEW: m5 multiplies a DIFFERENT direction in the "2" channel (not proportional to phi2's own)
    return (m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi) + mcross*Y3_of(cx3_dir)
            + m5*Y2_of(*ab2_dir))

def eval_point(p):
    m0,m2,m3,mcross,m5 = p
    Mnu = build_Mnu(m0,m2,m3,mcross,m5)
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

def residual5(p,target_mnu):
    r = eval_point(p)
    if r is None: return np.array([10]*5)
    th12,th23,th13,rat,Summnu = r
    return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,
                      (rat-ratio_t)/ratio_t,(Summnu-target_mnu)/target_mnu])

print("--- NEW candidate: second (a,b)-direction in the '2' channel (from (Phi3 Phi3)_2, axis2) ---")
print(f"{'target':>10}{'cost':>10}{'th12':>8}{'th23':>8}{'th13':>8}{'Sum_mnu':>10}")
for target in [0.06,0.07,0.072,0.08,0.10,0.129]:
    best=None
    rng=np.random.default_rng(int(target*10000))
    for _ in range(500):
        p0=rng.uniform(-30,30,5)
        try:
            res=least_squares(lambda p: residual5(p,target),p0,method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    r = eval_point(best[1])
    print(f"{target:>10.3f}{best[0]:>10.4f}{np.degrees(r[0]):>8.2f}{np.degrees(r[1]):>8.2f}{np.degrees(r[2]):>8.2f}{r[4]:>10.4f}")
