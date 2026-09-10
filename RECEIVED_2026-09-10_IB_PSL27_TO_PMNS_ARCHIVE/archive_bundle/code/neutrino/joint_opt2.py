import numpy as np
from scipy.optimize import least_squares
import pickle
import warnings
warnings.filterwarnings('ignore')

eps=0.06
lam_targets = np.array([0.010205748966120776, 0.0006068677466217874, 2.935024434079641e-06])
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
axc = np.array([0.,1.,0.]); axx = np.array([1.,0.,0.])
def Y2_of(a,b): return np.diag([2*a,-a+np.sqrt(3)*b,-a-np.sqrt(3)*b])
def Y3_of(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def Y3p_of(v): return np.array([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
def cross3(chi,xi):
    return np.array([chi[1]*xi[2]-chi[2]*xi[1], chi[2]*xi[0]-chi[0]*xi[2], chi[0]*xi[1]-chi[1]*xi[0]])
def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3,Utau3=U[1,2],U[0,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),-1,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13
def full_residual(p):
    th_phi,y2,c3,c3p,m0,m2,m3,mcross = p
    pd = np.array([np.cos(th_phi), np.sin(th_phi)])
    phi = eps*pd
    chi = eps**2*c3*axc
    xi  = eps**1*c3p*axx
    y3,y3pp = y2/np.sqrt(3), y2*np.sqrt(2/3)
    YT = y2*Y2_of(*phi) + y3*Y3_of(chi) + y3pp*Y3p_of(xi)
    sv = np.sort(np.linalg.svd(YT,compute_uv=False))[::-1]
    sv = np.clip(sv,1e-30,None)
    r_charged = np.log(sv/lam_targets)
    cx3 = cross3(axc, c3p*axx)
    Mnu = m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(axc) + mcross*Y3_of(cx3)
    w,V = np.linalg.eigh(Mnu)
    order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    U,svv,Vt = np.linalg.svd(YT)
    orderc = np.argsort(-svv)
    UL = U[:,orderc]
    PMNS = UL.T@V
    th12,th23,th13 = pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    ratio = dm21/dm31 if dm31!=0 else 1e6
    r_nu = np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,(ratio-ratio_t)/ratio_t])
    return np.concatenate([r_charged, r_nu])

best=None
rng = np.random.default_rng(7)
for trial in range(150):
    p0 = np.array([rng.uniform(0,2*np.pi), rng.uniform(-0.2,0.2), rng.uniform(-3,3), rng.uniform(-3,3),
                   rng.uniform(-15,15), rng.uniform(-15,15), rng.uniform(-15,15), rng.uniform(-15,15)])
    try:
        res = least_squares(full_residual, p0, method='trf', max_nfev=3000, xtol=1e-14, ftol=1e-14)
        cost = np.sum(res.fun**2)
        if np.isfinite(cost) and (best is None or cost<best[0]):
            best=(cost,res.x)
            with open('joint_fit.pkl','wb') as f: pickle.dump(best,f)
            print(f"trial {trial}: cost={best[0]:.6e}", flush=True)
            if cost < 1e-15:
                break
    except Exception: continue

print("DONE. Final:", best[0])
