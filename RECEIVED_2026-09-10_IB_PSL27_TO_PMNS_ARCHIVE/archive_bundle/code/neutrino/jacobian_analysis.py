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
chi_ax = 2
chi = axis3[chi_ax]; xi = c3p*axis3[0]
cx3 = cross3(chi,xi)
cx3_dir = cx3/np.linalg.norm(cx3)

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

def build_Mnu4(p):   # REAL model, 4 params: m0,m2,m3,mcross
    m0,m2,m3,mcross = p
    return m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi) + mcross*Y3_of(cx3_dir)

def observables4(p):
    Mnu = build_Mnu4(p)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    PMNS = UL.T@V
    th12,th23,th13=pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    rat = dm21/dm31 if dm31>1e-30 else np.nan
    k = np.sqrt(Dm31_phys/dm31) if dm31>1e-30 else np.nan
    Summnu = np.sum(masses)*k
    return th12,th23,th13,rat,Summnu

TARGETS4 = ['theta12','theta23','theta13','ratio']
TVAL4 = {'theta12':th12_t,'theta23':th23_t,'theta13':th13_t,'ratio':ratio_t}

def residuals4(p, names):
    th12,th23,th13,rat,Summnu = observables4(p)
    d = {'theta12':th12,'theta23':th23,'theta13':th13,'ratio':rat,'Summnu':Summnu}
    return np.array([(d[n]-TVAL4[n])/(abs(TVAL4[n]) if n!='Summnu' else 1) for n in names])

# ==== VARIANT A-equivalent for the REAL model: 4 params (m0,m2,m3,mcross), 4 targets (angles+ratio) ====
print("="*70)
print("REAL MODEL -- Variant analogous to A: 4 free params, 4 targets")
print("(m0,m2,m3,mcross) -> (theta12,theta23,theta13,ratio)")
print("="*70)
best=None
rng=np.random.default_rng(0)
for _ in range(300):
    p0 = rng.uniform(-30,30,4)
    try:
        res=least_squares(lambda p: residuals4(p,TARGETS4), p0, method='lm', max_nfev=5000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
    except Exception: continue
print("best cost:", best[0], " params:", best[1])
p_best4 = best[1]

def numjac(p, names, h=1e-6):
    n=len(p); m=len(names)
    J=np.zeros((m,n))
    for j in range(n):
        hh = h*max(1,abs(p[j]))
        pp=p.copy(); pp[j]+=hh
        pm=p.copy(); pm[j]-=hh
        J[:,j] = (residuals4(pp,names)-residuals4(pm,names))/(2*hh)
    return J

J4 = numjac(p_best4, TARGETS4)
U_,S_,Vt_ = np.linalg.svd(J4)
print("\nJacobian shape:", J4.shape, " singular values:", S_)
rank4 = np.sum(S_ > 1e-8*S_[0])
print("rank =", rank4, " nullity =", len(p_best4)-rank4)
