import numpy as np
from scipy.optimize import least_squares
import warnings
warnings.filterwarnings('ignore')

def theta2(tau, nterms=20):
    s=0
    for n in range(-nterms,nterms+1): s += np.exp(2j*np.pi*tau*(n+0.5)**2)
    return s
def theta3(tau, nterms=20):
    s=0
    for n in range(-nterms,nterms+1): s += np.exp(2j*np.pi*tau*n**2)
    return s
def Y_forms(tau):
    t2,t3 = theta2(tau), theta3(tau)
    return (t3**4+t2**4)/np.sqrt(2), -np.sqrt(3)*t2**2*t3**2, (t3**4-t2**4)/np.sqrt(2), -np.sqrt(2)*t2*t3**3, -np.sqrt(2)*t2**3*t3

our_tau = 1j*1.797
Y1,Y2,Y3,Y4,Y5 = Y_forms(our_tau)

def lam_matrix(alpha,beta,gamma,Y1,Y2,Y3,Y4,Y5):
    return np.array([[alpha*Y3, alpha*Y5, alpha*Y4],
        [beta*(Y1*Y4-Y2*Y5), beta*(Y1*Y3-Y2*Y4), beta*(Y1*Y5-Y2*Y3)],
        [gamma*(Y1*Y4+Y2*Y5), gamma*(Y1*Y3+Y2*Y4), gamma*(Y1*Y5+Y2*Y3)]], dtype=complex)
def Yuk_nu(g,gp,Y1,Y2,Y3,Y4,Y5):
    base = np.array([[0,Y1,Y2],[Y1,Y2,0],[Y2,0,Y1]],dtype=complex)
    cross = np.array([[0,Y5,-Y4],[-Y5,0,Y3],[Y4,-Y3,0]],dtype=complex)
    return g*base + gp*cross
def M_heavy(): return 2*np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex)

th12_t=np.radians(33.44); th23_t=np.radians(49.20); th13_t=np.radians(8.57); ratio_t=0.0295
me,mmu,mtau = 0.000511,0.105658,1.77686
def pmns_angles(U):
    Ue1,Ue2,Ue3=U[0,0],U[0,1],U[0,2]; Umu3,Utau3=U[1,2],U[2,2]
    th13=np.arcsin(np.clip(abs(Ue3),0,1)); th12=np.arctan2(abs(Ue2),abs(Ue1)); th23=np.arctan2(abs(Umu3),abs(Utau3))
    return th12,th23,th13

def residual(p):
    logbeta,loggamma,logg,logabsgp,arggp,logLambdaScale,logalphaScale = p
    beta=10**logbeta; gamma=10**loggamma; alpha=1.0
    g=10**logg; gp=10**logabsgp*np.exp(1j*arggp)
    LambdaScale=10**logLambdaScale; alphaScale=10**logalphaScale
    lam = lam_matrix(alpha,beta,gamma,Y1,Y2,Y3,Y4,Y5)
    Me = alphaScale*lam.conj().T
    ml = np.sort(np.linalg.svd(Me,compute_uv=False))
    if np.any(ml<1e-30): return np.array([1e3]*7)
    Yy = Yuk_nu(g,gp,Y1,Y2,Y3,Y4,Y5)
    Mh = M_heavy()
    Mnu = -LambdaScale*(Yy.T@np.linalg.inv(Mh)@Yy)
    UL,_,_=np.linalg.svd(Me)
    H=Mnu.conj().T@Mnu
    if not np.all(np.isfinite(H)): return np.array([1e3]*7)
    d2,U=np.linalg.eigh(H)
    Dc=U.T@Mnu@U; ph=np.angle(np.diag(Dc)+1e-300); U2=U*np.exp(-1j*ph/2)[None,:]
    dnu=np.sqrt(np.clip(d2,0,None)); order=np.argsort(dnu); dnu=dnu[order]; U2=U2[:,order]
    PMNS=UL.conj().T@U2
    th12,th23,th13=pmns_angles(PMNS)
    dm21=dnu[1]**2-dnu[0]**2; dm31=dnu[2]**2-dnu[0]**2
    rat=dm21/dm31 if dm31>1e-30 else 1e6
    return np.array([np.log(ml[0]/me),np.log(ml[1]/mmu),np.log(ml[2]/mtau),
                      np.log(abs(rat)/ratio_t),(th12-th12_t)/th12_t,(th23-th23_t)/th23_t,(th13-th13_t)/th13_t])

best=None
rng=np.random.default_rng(42)
for trial in range(3000):
    p0=np.array([rng.uniform(-3,3),rng.uniform(-3,3),rng.uniform(-3,3),rng.uniform(-3,3),
                 rng.uniform(-np.pi,np.pi),rng.uniform(-3,1),rng.uniform(-3,1)])
    try:
        res=least_squares(residual,p0,method='lm',max_nfev=3000,xtol=1e-15,ftol=1e-15)
        c=np.sum(res.fun**2)
        if np.isfinite(c) and (best is None or c<best[0]):
            best=(c,res.x)
    except Exception: continue
print(f"Best cost (3000 restarts): {best[0]:.6f}")
print(f"params: {best[1]}")
