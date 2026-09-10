import numpy as np
from scipy.optimize import least_squares
from build_modular import Y_weight2
import warnings
warnings.filterwarnings('ignore')

def Y2mat(v): return np.diag([2*v[0], -v[0]+np.sqrt(3)*v[1], -v[0]-np.sqrt(3)*v[1]])
def Y3mat(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def Y3pmat(v): return np.array([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
me,mmu,mtau = 0.0005110,0.1056584,1.7768600

def cl_fit(t, nstarts=150, seed=0):
    tau=1j*t
    Y1,Y2,Y3,Y4,Y5 = Y_weight2(tau)
    def resid(p):
        y2,n2,n3,n3p = p
        y3=y2/np.sqrt(3); y3p=y2*np.sqrt(2/3)
        phi2 = n2*np.array([Y1.real,Y2.real])
        Phi3p = n3p*np.array([Y3.real,Y4.real,Y5.real])
        Phi3 = n3*np.array([(Y1*Y4-Y2*Y5).real,(Y1*Y5-Y2*Y3).real,(Y1*Y3-Y2*Y4).real])
        YT = y2*Y2mat(phi2) + y3*Y3mat(Phi3) + y3p*Y3pmat(Phi3p)
        sv = np.sort(np.linalg.svd(YT,compute_uv=False))
        return np.array([np.log(sv[0]/me),np.log(sv[1]/mmu),np.log(sv[2]/mtau)])
    best=None
    rng=np.random.default_rng(seed)
    for _ in range(nstarts):
        p0=np.array([rng.uniform(0.001,2), rng.uniform(0.01,20), rng.uniform(0.01,20), rng.uniform(0.01,20)])
        res=least_squares(resid,p0,method='trf',max_nfev=3000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if best is None or c<best[0]: best=(c,res.x)
    return best

print(f"{'t':>8}{'cost':>14}")
for t in np.arange(0.9, 4.01, 0.15):
    b = cl_fit(t, seed=int(t*1000))
    print(f"{t:>8.2f}{b[0]:>14.6e}")
