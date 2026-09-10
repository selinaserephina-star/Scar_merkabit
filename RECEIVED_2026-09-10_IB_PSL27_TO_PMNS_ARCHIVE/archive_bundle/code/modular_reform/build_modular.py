import numpy as np

def theta2(tau, nterms=20):
    s=0
    for n in range(-nterms,nterms+1): s += np.exp(2j*np.pi*tau*(n+0.5)**2)
    return s
def theta3(tau, nterms=20):
    s=0
    for n in range(-nterms,nterms+1): s += np.exp(2j*np.pi*tau*n**2)
    return s

def Y_weight2(tau):
    t2,t3 = theta2(tau), theta3(tau)
    Y1 = (t3**4+t2**4)/np.sqrt(2)
    Y2 = -np.sqrt(3)*t2**2*t3**2
    Y3 = (t3**4-t2**4)/np.sqrt(2)
    Y4 = -np.sqrt(2)*t2*t3**3
    Y5 = -np.sqrt(2)*t2**3*t3
    return Y1,Y2,Y3,Y4,Y5

def build_VEVs(tau, norm2, norm3, norm3p):
    Y1,Y2,Y3,Y4,Y5 = Y_weight2(tau)
    phi2 = norm2*np.array([Y1,Y2])
    Phi3p = norm3p*np.array([Y3,Y4,Y5])
    Phi3 = norm3*np.array([Y1*Y4-Y2*Y5, Y1*Y5-Y2*Y3, Y1*Y3-Y2*Y4])
    return phi2, Phi3, Phi3p

if __name__ == "__main__":
    tau_test = 1j*1.797
    phi2,Phi3,Phi3p = build_VEVs(tau_test, 1,1,1)
    print("At tau=1.797i (all real theta functions):")
    print("phi2 =", phi2)
    print("Phi3 =", Phi3)
    print("Phi3prime =", Phi3p)
