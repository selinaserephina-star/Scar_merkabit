import numpy as np
from scipy.optimize import least_squares
import sys
sys.path.insert(0,'/home/claude/modular_reform')
from build_modular import Y_weight2

def Y2mat(v): return np.diag([2*v[0], -v[0]+np.sqrt(3)*v[1], -v[0]-np.sqrt(3)*v[1]])
def Y3mat(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def Y3pmat(v): return np.array([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
def cross3(a,b): return np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])

me,mmu,mtau = 0.0005110,0.1056584,1.7768600
th12_t=np.radians(33.0); th23_t=np.radians(45.0); th13_t=np.radians(8.5); ratio_t=0.03
Dm31_phys = 2.53e-3

def pmns_angles(U):
    Ue1,Ue2,Ue3=U[2,0],U[2,1],U[2,2]; Umu3=U[1,2]
    th13=np.arcsin(np.clip(np.abs(Ue3),0,1))
    th12=np.arctan2(np.abs(Ue2),np.abs(Ue1))
    th23=np.arctan2(np.abs(Umu3),np.abs(U[0,2]))
    return th12,th23,th13

def get_VEVs(t, norm2, norm3, norm3p):
    tau = 1j*t
    Y1,Y2,Y3,Y4,Y5 = Y_weight2(tau)
    phi2 = norm2*np.array([Y1.real,Y2.real])
    Phi3p = norm3p*np.array([Y3.real,Y4.real,Y5.real])
    Phi3 = norm3*np.array([(Y1*Y4-Y2*Y5).real,(Y1*Y5-Y2*Y3).real,(Y1*Y3-Y2*Y4).real])
    return phi2, Phi3, Phi3p

def charged_lepton_fit(t, nstarts=60, seed=0):
    def resid(p):
        y2,n2,n3,n3p = p
        y3=y2/np.sqrt(3); y3p=y2*np.sqrt(2/3)
        phi2,Phi3,Phi3p = get_VEVs(t,n2,n3,n3p)
        YT = y2*Y2mat(phi2) + y3*Y3mat(Phi3) + y3p*Y3pmat(Phi3p)
        sv = np.sort(np.linalg.svd(YT,compute_uv=False))
        return np.array([np.log(sv[0]/me),np.log(sv[1]/mmu),np.log(sv[2]/mtau)])
    best=None
    rng=np.random.default_rng(seed)
    for _ in range(nstarts):
        p0=np.array([rng.uniform(0.01,0.5), rng.uniform(0.1,3), rng.uniform(0.1,3), rng.uniform(0.1,3)])
        try:
            res=least_squares(resid,p0,method='lm',max_nfev=2000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    return best

def full_fit(t, nstarts_cl=60, nstarts_nu=150, seed=0):
    cl = charged_lepton_fit(t,nstarts_cl,seed)
    if cl is None or cl[0]>1e-10: return None
    y2,n2,n3,n3p = cl[1]
    phi2,Phi3,Phi3p = get_VEVs(t,n2,n3,n3p)
    y3=y2/np.sqrt(3); y3p=y2*np.sqrt(2/3)
    YT = y2*Y2mat(phi2)+y3*Y3mat(Phi3)+y3p*Y3pmat(Phi3p)
    UL,_,_ = np.linalg.svd(YT)
    cx3 = cross3(Phi3,Phi3p)
    if np.linalg.norm(cx3)<1e-10: return None
    cx3n = cx3/np.linalg.norm(cx3)
    def resid_nu(p):
        m0,m2,m3,mcross = p
        Mnu = m0*np.eye(3)+m2*Y2mat(phi2)+m3*Y3mat(Phi3)+mcross*Y3mat(cx3n)
        w,V=np.linalg.eigh(Mnu); order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
        masses=np.abs(w)
        PMNS=UL.T@V
        th12,th23,th13=pmns_angles(PMNS)
        dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
        rat=dm21/dm31 if dm31>1e-30 else 1e6
        return np.array([(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t,(rat-ratio_t)/ratio_t])
    best=None
    rng=np.random.default_rng(seed+500)
    for _ in range(nstarts_nu):
        p0=rng.uniform(-30,30,4)
        try:
            res=least_squares(resid_nu,p0,method='lm',max_nfev=3000,xtol=1e-15,ftol=1e-15)
            c=np.sum(res.fun**2)
            if np.isfinite(c) and (best is None or c<best[0]): best=(c,res.x)
        except Exception: continue
    if best is None: return None
    m0,m2,m3,mcross = best[1]
    Mnu = m0*np.eye(3)+m2*Y2mat(phi2)+m3*Y3mat(Phi3)+mcross*Y3mat(cx3n)
    w,V=np.linalg.eigh(Mnu); order=np.argsort(np.abs(w)); w=w[order]; V=V[:,order]
    masses=np.abs(w)
    PMNS=UL.T@V
    th12,th23,th13=pmns_angles(PMNS)
    dm21=masses[1]**2-masses[0]**2; dm31=masses[2]**2-masses[0]**2
    rat=dm21/dm31
    k=np.sqrt(Dm31_phys/dm31)
    Summnu=np.sum(masses)*k
    return best[0], (th12,th23,th13,rat,Summnu)

if __name__=="__main__":
    print(f"{'t':>8}{'nu_cost':>12}{'th12':>8}{'th23':>8}{'th13':>8}{'ratio':>9}{'Sum_mnu':>10}")
    for t in np.arange(1.0, 3.01, 0.2):
        r = full_fit(t, seed=int(t*100))
        if r is None:
            print(f"{t:>8.2f}   FAILED"); continue
        cost,(th12,th23,th13,rat,smnu) = r
        print(f"{t:>8.2f}{cost:>12.5f}{np.degrees(th12):>8.2f}{np.degrees(th23):>8.2f}{np.degrees(th13):>8.2f}{rat:>9.4f}{smnu:>10.4f}")
