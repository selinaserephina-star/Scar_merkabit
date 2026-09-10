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

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[0,0],U[0,1],U[0,2]; Umu3,Utau3=U[1,2],U[2,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),0,1)); th12=np.arctan2(np.abs(Ue2),np.abs(Ue1)); th23=np.arctan2(np.abs(Umu3),np.abs(Utau3))
    return th12,th23,th13

def cl_resid(p, a2,b3,g1):
    y2,c3,c3p = p
    y3=y2/np.sqrt(3); y3pv=y2*np.sqrt(2/3)
    phi2 = np.array([0, eps*np.exp(1j*a2)])
    Phi3 = np.array([0,0, c3*eps**2*np.exp(1j*b3)])
    Phi3p = np.array([c3p*eps*np.exp(1j*g1), 0, 0])
    YT = y2*Y2mat(phi2) + y3*Y3mat(Phi3) + y3pv*Y3pmat(Phi3p)
    sv = np.sort(np.linalg.svd(YT,compute_uv=False))
    return np.array([sv[0]-me, sv[1]-mmu, sv[2]-mtau])

def evaluate_point(a2,b3,g1, cl_starts=100, nu_starts=100, seed=0):
    best_cl=None
    rng=np.random.default_rng(seed)
    for _ in range(cl_starts):
        p0=np.array([rng.uniform(1,20), rng.uniform(0.01,3), rng.uniform(0.1,5)])
        res=least_squares(cl_resid,p0,args=(a2,b3,g1),method='lm',max_nfev=2000,xtol=1e-14,ftol=1e-14)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best_cl is None or c<best_cl[0]): best_cl=(c,res.x)
    if best_cl is None or best_cl[0] > 1e-12:
        return None  # masses not achievable at this phase point
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
        w,V=np.linalg.eigh(Mnu); order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
        masses=np.abs(w); PMNS=UL.conj().T@V
        th12,th23,th13=pmns_angles(PMNS)
        dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
        rat=dm21/dm31 if dm31>1e-30 else 1e6
        return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,(rat-ratio_t)/ratio_t])
    best_nu=None
    for _ in range(nu_starts):
        p0=rng.uniform(-100,100,4)
        res=least_squares(nu_resid,p0,method='lm',max_nfev=3000,xtol=1e-14,ftol=1e-14)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best_nu is None or c<best_nu[0]): best_nu=(c,res.x)
    if best_nu is None: return None
    m0,m2,m3,mcross = best_nu[1]
    Mnu = m0*np.eye(3)+m2*Y2mat(phi2)+m3*Y3mat(chi_n)+mcross*Y3mat(cx3n)
    H = Mnu.conj().T @ Mnu
    d2, W = np.linalg.eigh(H); d2=np.clip(d2,0,None)
    Dc = W.T @ Mnu @ W; ph=np.angle(np.diag(Dc)+1e-300)
    Wt = W*np.exp(-1j*ph/2)[None,:]
    dnu = np.sqrt(d2); order2=np.argsort(dnu); dnu=dnu[order2]; Wt=Wt[:,order2]
    PMNS = UL.conj().T @ Wt
    Ue3=PMNS[0,2]; th13=np.arcsin(np.clip(np.abs(Ue3),0,1))
    th12=np.arctan2(np.abs(PMNS[0,1]),np.abs(PMNS[0,0]))
    th23=np.arctan2(np.abs(PMNS[1,2]),np.abs(PMNS[2,2]))
    J = np.imag(PMNS[0,0]*PMNS[1,1]*np.conj(PMNS[0,1])*np.conj(PMNS[1,0]))
    s12,c12=np.sin(th12),np.cos(th12); s23,c23=np.sin(th23),np.cos(th23); s13,c13=np.sin(th13),np.cos(th13)
    denom = c12*s12*c23*s23*c13**2*s13
    sind = np.clip(J/denom,-1,1) if abs(denom)>1e-12 else np.nan
    deltaCP = np.degrees(np.arcsin(sind)) if np.isfinite(sind) else np.nan
    dm21=dnu[1]**2-dnu[0]**2; dm31=dnu[2]**2-dnu[0]**2
    rat=dm21/dm31; k=np.sqrt(Dm31_phys/dm31) if dm31>0 else np.nan
    Summnu=np.sum(dnu)*k if np.isfinite(k) else np.nan
    return dict(cl_cost=best_cl[0], nu_cost=best_nu[0], th12=np.degrees(th12),th23=np.degrees(th23),
                th13=np.degrees(th13), J=J, deltaCP=deltaCP, ratio=rat, Summnu=Summnu)

if __name__=="__main__":
    results = {}
    grid = np.linspace(0, 2*np.pi, 7, endpoint=False)
    count=0
    for a2 in grid:
        for b3 in grid:
            for g1 in grid:
                count+=1
                r = evaluate_point(a2,b3,g1, cl_starts=40, nu_starts=40, seed=count)
                if r is not None:
                    results[(round(a2,3),round(b3,3),round(g1,3))] = r
                    print(f"a2={a2:.2f} b3={b3:.2f} g1={g1:.2f}: cl={r['cl_cost']:.2e} nu={r['nu_cost']:.4f} "
                          f"th12={r['th12']:.1f} th23={r['th23']:.1f} th13={r['th13']:.1f} "
                          f"J={r['J']:.2e} dCP={r['deltaCP']:.1f} Smnu={r['Summnu']:.3f}")
    with open('phase_scan_results.pkl','wb') as f: pickle.dump(results,f)
    print(f"\nTotal viable points: {len(results)} / {count}")
