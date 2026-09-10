import numpy as np
from scipy.optimize import minimize
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
Dm31_phys = 2.53e-3

def build_Mnu(m0,m2,m3,mcross,m5):
    return (m0*np.eye(3) + m2*Y2_of(*phi) + m3*Y3_of(chi) + mcross*Y3_of(cx3_dir) + m5*Y3_of(new_v))

def summnu(p):
    m0,m2,m3,mcross,m5 = p
    Mnu = build_Mnu(m0,m2,m3,mcross,m5)
    w = np.linalg.eigvalsh(Mnu)
    masses_raw = np.sort(np.abs(w))
    dm31 = masses_raw[2]**2 - masses_raw[0]**2
    if dm31 < 1e-8: return 10.0
    k = np.sqrt(Dm31_phys/dm31)
    return np.sum(masses_raw)*k

best=None
rng=np.random.default_rng(7)
for _ in range(300):
    p0 = rng.uniform(-30,30,5)
    res = minimize(summnu, p0, method='Nelder-Mead', options={'maxiter':5000,'xatol':1e-10,'fatol':1e-12})
    if best is None or res.fun<best[0]:
        best=(res.fun,res.x)
print("Absolute floor of Sum(m_nu), ignoring ALL angle constraints:", best[0],"eV")
print("params:",best[1])
