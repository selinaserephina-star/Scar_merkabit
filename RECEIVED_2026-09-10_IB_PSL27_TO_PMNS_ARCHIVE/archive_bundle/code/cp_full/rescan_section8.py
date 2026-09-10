import numpy as np
from scipy.optimize import least_squares
import warnings, pickle
warnings.filterwarnings('ignore')

eps=0.06
def Y2mat(v): return np.diag([2*v[0], -v[0]+np.sqrt(3)*v[1], -v[0]-np.sqrt(3)*v[1]])
def Y3mat(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def Y3pmat(v): return np.array([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
def cross3(a,b): return np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
me,mmu,mtau = 0.0005110,0.1056584,1.7768600
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
Dm31_phys = 2.53e-3

def takagi(Mnu):
    H = Mnu.conj().T @ Mnu
    d2, W = np.linalg.eigh(H); d2=np.clip(d2,0,None)
    Dc = W.T @ Mnu @ W; ph=np.angle(np.diag(Dc)+1e-300)
    Wt = W*np.exp(-1j*ph/2)[None,:]
    dnu=np.sqrt(d2); order=np.argsort(dnu)
    return dnu[order], Wt[:,order]

def pmns_full(PMNS):
    ph_rows = np.angle(PMNS[:,0]); R = PMNS*np.exp(-1j*ph_rows)[:,None]
    th13=np.arcsin(np.clip(np.abs(R[0,2]),0,1)); th12=np.arctan2(np.abs(R[0,1]),np.abs(R[0,0]))
    th23=np.arctan2(np.abs(R[1,2]),np.abs(R[2,2])); deltaCP=-np.degrees(np.angle(R[0,2]))
    return th12,th23,th13,deltaCP

def cl_resid(p, a2,b3,g1):
    y2,c3,c3p = p
    y3=y2/np.sqrt(3); y3pv=y2*np.sqrt(2/3)
    phi2 = np.array([0, eps*np.exp(1j*a2)])
    Phi3 = np.array([0,0, c3*eps**2*np.exp(1j*b3)])
    Phi3p = np.array([c3p*eps*np.exp(1j*g1), 0, 0])
    YT = y2*Y2mat(phi2) + y3*Y3mat(Phi3) + y3pv*Y3pmat(Phi3p)
    sv = np.sort(np.linalg.svd(YT,compute_uv=False))
    return np.array([sv[0]-me, sv[1]-mmu, sv[2]-mtau])

CL_WARM = np.array([8.043031, 0.64085776, 2.38809204])
NU_WARM = np.array([41327.05, -806652.33, -70752.39, 5261.89])

def evaluate_point(a2,b3,g1, seed=0):
    best_cl=None
    rng=np.random.default_rng(seed)
    for p0 in [CL_WARM, CL_WARM*1.05, CL_WARM*0.95, CL_WARM*(-1)]:
        res=least_squares(cl_resid,p0,args=(a2,b3,g1),method='lm',max_nfev=3000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best_cl is None or c<best_cl[0]): best_cl=(c,res.x)
    if best_cl[0] > 1e-15:
        for _ in range(40):
            p0=np.array([rng.uniform(1,20), rng.uniform(-3,3), rng.uniform(-5,5)])
            res=least_squares(cl_resid,p0,args=(a2,b3,g1),method='lm',max_nfev=3000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and c<best_cl[0]: best_cl=(c,res.x)
    if best_cl[0] > 1e-12: return None
    y2,c3,c3p = best_cl[1]
    y3=y2/np.sqrt(3); y3pv=y2*np.sqrt(2/3)
    phi2 = np.array([0, eps*np.exp(1j*a2)])
    Phi3 = np.array([0,0, c3*eps**2*np.exp(1j*b3)])
    Phi3p = np.array([c3p*eps*np.exp(1j*g1), 0, 0])
    YT = y2*Y2mat(phi2) + y3*Y3mat(Phi3) + y3pv*Y3pmat(Phi3p)
    U,sv,Vh = np.linalg.svd(YT); order=np.argsort(sv); UL=U[:,order]
    chi_n = Phi3/np.linalg.norm(Phi3)
    cx3 = cross3(Phi3,Phi3p); ncx3=np.linalg.norm(cx3)
    if ncx3<1e-14: return None
    cx3n = cx3/ncx3

    def nu_resid(p):
        m0,m2,m3,mcross = p
        Mnu = m0*np.eye(3)+m2*Y2mat(phi2)+m3*Y3mat(chi_n)+mcross*Y3mat(cx3n)
        dnu,Wt = takagi(Mnu)
        PMNS = UL.conj().T@Wt
        th12,th23,th13,_ = pmns_full(PMNS)
        dm21=dnu[1]**2-dnu[0]**2; dm31=dnu[2]**2-dnu[0]**2
        rat=dm21/dm31 if dm31>1e-30 else 1e6
        return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,(rat-ratio_t)/ratio_t])
    best_nu=None
    for p0 in [NU_WARM, NU_WARM*1.1, NU_WARM*0.9, NU_WARM*(-1)]:
        res=least_squares(nu_resid,p0,method='lm',max_nfev=3000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best_nu is None or c<best_nu[0]): best_nu=(c,res.x)
    for _ in range(40):
        p0=rng.uniform(-3e5,3e5,4)
        res=least_squares(nu_resid,p0,method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best_nu is None or c<best_nu[0]): best_nu=(c,res.x)
    if best_nu is None: return None
    m0,m2,m3,mcross = best_nu[1]
    Mnu = m0*np.eye(3)+m2*Y2mat(phi2)+m3*Y3mat(chi_n)+mcross*Y3mat(cx3n)
    dnu, Wt = takagi(Mnu)
    PMNS = UL.conj().T @ Wt
    th12,th23,th13,deltaCP = pmns_full(PMNS)
    dm21=dnu[1]**2-dnu[0]**2; dm31=dnu[2]**2-dnu[0]**2
    rat=dm21/dm31; k=np.sqrt(Dm31_phys/dm31) if dm31>0 else np.nan
    Summnu=np.sum(dnu)*k if np.isfinite(k) else np.nan
    return dict(cl_cost=best_cl[0], nu_cost=best_nu[0], th12=np.degrees(th12),th23=np.degrees(th23),
                th13=np.degrees(th13), deltaCP=deltaCP, ratio=rat, Summnu=Summnu)

if __name__=="__main__":
    results = {}
    rng_master = np.random.default_rng(42)  # SAME seed as original section 8 scan
    N = 150
    pts = rng_master.uniform(0, 2*np.pi, size=(N,3))
    for i,(a2,b3,g1) in enumerate(pts):
        r = evaluate_point(a2,b3,g1, seed=i*7+1)
        if r is not None:
            results[(round(a2,4),round(b3,4),round(g1,4))] = r
            flag = " <<<< TARGET" if -174<=r['deltaCP']<=-122 else ""
            print(f"[{i}] a2={a2:.2f} b3={b3:.2f} g1={g1:.2f}: cl={r['cl_cost']:.1e} nu={r['nu_cost']:.4f} "
                  f"th12={r['th12']:.1f} th23={r['th23']:.1f} th13={r['th13']:.1f} ratio={r['ratio']:.4f} "
                  f"dCP={r['deltaCP']:.1f} Smnu={r['Summnu']:.3f}{flag}", flush=True)
    with open('rescan_section8_results.pkl','wb') as f: pickle.dump(results,f)
    print(f"\nTotal viable: {len(results)}/{N}")
