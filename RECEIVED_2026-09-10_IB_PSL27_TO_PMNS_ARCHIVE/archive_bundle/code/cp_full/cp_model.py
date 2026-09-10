import numpy as np

eps = 0.06
c3 = 0.53650154
c3p = 1.8842209812516129
y2v = 0.05200811
y3v = y2v/np.sqrt(3)
y3pv = y2v*np.sqrt(2/3)

def Y2mat(v): return np.diag([2*v[0], -v[0]+np.sqrt(3)*v[1], -v[0]-np.sqrt(3)*v[1]])
def Y3mat(v): return np.array([[0,v[2],v[1]],[v[2],0,v[0]],[v[1],v[0],0]])
def Y3pmat(v): return np.array([[0,v[2],-v[1]],[-v[2],0,v[0]],[v[1],-v[0],0]])
def cross3(a,b): return np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])

me,mmu,mtau = 0.0005110,0.1056584,1.7768600
th12_t=33.0; th23_t=45.0; th13_t=8.5; ratio_t=0.03
Dm31_phys = 2.53e-3

# best-fit neutrino params established earlier (axis chi=2,xi=0, computed kappa)
m0_n, m2_n, m3_n, mcross_n = 94.37, -1810.92, 136.47, 15.43

def build_YT(a2,b3,g1):
    phi2 = np.array([0, eps*np.exp(1j*a2)])
    Phi3 = np.array([0,0, c3*np.exp(1j*b3)])
    Phi3p = np.array([c3p*eps*np.exp(1j*g1), 0, 0])
    YT = y2v*Y2mat(phi2) + y3v*Y3mat(Phi3) + y3pv*Y3pmat(Phi3p)
    return YT, phi2, Phi3, Phi3p

def charged_lepton_obs(a2,b3,g1):
    YT,_,_,_ = build_YT(a2,b3,g1)
    sv = np.linalg.svd(YT, compute_uv=False)
    return np.sort(sv)

def full_obs(a2,b3,g1):
    YT, phi2, Phi3, Phi3p = build_YT(a2,b3,g1)
    U,sv,Vh = np.linalg.svd(YT)
    order = np.argsort(sv)
    sv = sv[order]; U = U[:,order]
    UL = U  # left singular vectors -> charged lepton diagonalization matrix
    cx3 = cross3(Phi3, Phi3p)
    if np.linalg.norm(cx3) < 1e-14:
        cx3n = np.zeros(3, dtype=complex)
    else:
        cx3n = cx3/np.linalg.norm(cx3)
    Mnu = m0_n*np.eye(3) + m2_n*Y2mat(phi2) + m3_n*Y3mat(Phi3) + mcross_n*Y3mat(cx3n)
    # Takagi decomposition of complex symmetric Mnu
    H = Mnu.conj().T @ Mnu
    d2, W = np.linalg.eigh(H)
    d2 = np.clip(d2, 0, None)
    Dc = W.T @ Mnu @ W
    ph = np.angle(np.diag(Dc) + 1e-300)
    Wt = W * np.exp(-1j*ph/2)[None,:]
    dnu = np.sqrt(d2)
    order2 = np.argsort(dnu)
    dnu = dnu[order2]; Wt = Wt[:,order2]
    PMNS = UL.conj().T @ Wt
    # standard PMNS parametrization extraction
    Ue3 = PMNS[0,2]
    th13 = np.arcsin(np.clip(np.abs(Ue3),0,1))
    Ue1,Ue2 = PMNS[0,0],PMNS[0,1]
    th12 = np.arctan2(np.abs(Ue2), np.abs(Ue1))
    Umu3, Utau3 = PMNS[1,2], PMNS[2,2]
    th23 = np.arctan2(np.abs(Umu3), np.abs(Utau3))
    # Jarlskog invariant (standard definition using e,mu / 1,3 indices)
    J = np.imag(PMNS[0,0]*PMNS[1,1]*np.conj(PMNS[0,1])*np.conj(PMNS[1,0]))
    # extract delta_CP via standard formula from J and angles
    s12,c12 = np.sin(th12), np.cos(th12)
    s23,c23 = np.sin(th23), np.cos(th23)
    s13,c13 = np.sin(th13), np.cos(th13)
    denom = c12*s12*c23*s23*c13**2*s13
    sind = J/denom if abs(denom)>1e-14 else np.nan
    sind = np.clip(sind,-1,1)
    deltaCP = np.degrees(np.arcsin(sind))
    dm21 = dnu[1]**2-dnu[0]**2; dm31 = dnu[2]**2-dnu[0]**2
    rat = dm21/dm31 if abs(dm31)>1e-30 else np.nan
    k = np.sqrt(Dm31_phys/dm31) if dm31>0 else np.nan
    Summnu = np.sum(dnu)*k if np.isfinite(k) else np.nan
    return dict(masses=sv, th12=np.degrees(th12), th23=np.degrees(th23), th13=np.degrees(th13),
                J=J, deltaCP=deltaCP, ratio=rat, Summnu=Summnu, dnu=dnu)

if __name__=="__main__":
    print("=== Reproduce earlier test point (0.1,0.1,0.1) rad ===")
    r = full_obs(0.1,0.1,0.1)
    print(f"masses (should match me,mmu,mtau): {r['masses']}")
    print(f"targets: {me},{mmu},{mtau}")
    print(f"th12={r['th12']:.4f} th23={r['th23']:.4f} th13={r['th13']:.4f}")
    print(f"J={r['J']:.6e}  deltaCP={r['deltaCP']:.4f}")
    print(f"ratio={r['ratio']:.6f}  Sum_mnu={r['Summnu']:.6f}")
