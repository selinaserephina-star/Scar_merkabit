import numpy as np
from scipy.optimize import least_squares
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
cx3 = cross3(chi,xi)
cx3_dir = cx3/np.linalg.norm(cx3)
Traw = np.load('/home/claude/basis_match/T_2x3to3.npy')
new_v = np.einsum('ijk,j->ki', Traw, cx3_dir)[:,1]

import pickle
with open('UL_dict.pkl','rb') as f: UL_dict = pickle.load(f)
UL = UL_dict[(2,0)]
Dm31_phys = 2.53e-3

def build_Mnu(m0,m2,m3,mcross,m5):
    return (m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi) + mcross*Y3_of(cx3_dir) + m5*Y3_of(new_v))

def eval_point(p):
    m0,m2,m3,mcross,m5 = p
    Mnu = build_Mnu(m0,m2,m3,mcross,m5)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]
    masses_raw=np.abs(w[order])
    dm31=masses_raw[2]**2-masses_raw[0]**2
    if dm31 < 1e-30: return None
    k = np.sqrt(Dm31_phys/dm31)
    Summnu = np.sum(masses_raw)*k
    return Summnu

# Pure minimization of Sum(m_nu) alone, NO angle constraints at all --
# what's the absolute floor this 5-parameter family can reach?
def neg_summnu(p):
    s = eval_point(p)
    return s if s is not None else 10

best=None
rng=np.random.default_rng(123)
for _ in range(3000):
    p0 = rng.uniform(-30,30,5)
    try:
        res = least_squares(lambda p: [neg_summnu(p)], p0, method='lm', max_nfev=3000, xtol=1e-15,ftol=1e-15)
        val = neg_summnu(res.x)
        if best is None or val<best[0]:
            best=(val,res.x)
    except Exception: continue
print("Absolute minimum Sum(m_nu) reachable (ignoring angles entirely):", best[0], "eV")
print("params:", best[1])
