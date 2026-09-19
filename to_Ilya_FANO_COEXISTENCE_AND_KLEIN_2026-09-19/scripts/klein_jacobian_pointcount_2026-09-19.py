"""
klein_jacobian_pointcount_2026-09-19.py   [BSD folder, exploration grade; Stenberg side with Claude]

Check of IB's FINDING (2026-09-15) "Klein Quartic Jacobian: J ~ E x A, A a simple CM surface,
Hom(E,A)=0", which was verified only over F_37.

Test: the classical statement is J(X(7)) ~ E^3 geometrically, E = 49a1 (CM by Q(sqrt-7)), with the
isogeny defined over the cubic field Q(zeta_7)^+ (not over Q, not over Q(sqrt-7)).  Then for a prime p:
  * p = 1 (mod 7): p splits completely in Q(zeta_7)^+, the isogeny is defined over F_p, and
        a_1(J) = p + 1 - #X(7)(F_p) = 3 a_p(E).
  * p of order 3 mod 7 (p = 2, 4 mod 7): p is inert in Q(zeta_7)^+, the split happens only over F_{p^3},
        the Frobenius eigenvalues are {alpha w^k, alphabar w^k}, so a_1(J) = 0 and P_J(T) is a polynomial in T^3.
Both are decided by counting points on x^3 y + y^3 z + z^3 x = 0 and on E: y^2 + xy = x^3 - x^2 - 2x - 1.
No tables used; pure Python.
"""
import sympy as sp

def klein_count(p):
    n = 0
    for x in range(p):
        x3 = x*x*x % p
        for y in range(p):
            if (x3*y + y*y*y + x) % p == 0:      # affine chart z = 1
                n += 1
    return n + 2                                  # z = 0: x^3 y = 0 -> (1:0:0), (0:1:0)

def ap_49a1(p):
    n = 0
    for x in range(p):
        rhs = (x*x*x - x*x - 2*x - 1) % p
        d = (x*x + 4*rhs) % p                     # discriminant of y^2 + x y - rhs
        if d == 0: n += 1
        elif pow(d, (p-1)//2, p) == 1: n += 2
    return p + 1 - (n + 1)

print(f"{'p':>4} {'p mod 7':>7} {'#X(7)(F_p)':>10} {'a1(J)':>6} {'a_p(49a1)':>9} {'3 a_p':>6}  reading")
fails = 0
for p in [29, 37, 43, 53, 71, 79, 113, 127]:
    c = klein_count(p); a1 = p + 1 - c; ae = ap_49a1(p)
    if p % 7 == 1:
        ok = (a1 == 3*ae); reading = "p=1 mod 7: a1 = 3 a_p  -> E^3 split over F_p"
    elif pow(p, 3, 7) == 1:
        ok = (a1 == 0);    reading = "order 3 mod 7: a1 = 0  -> split only over F_{p^3} (cubic twist)"
    else:
        ok = True;         reading = "order 6 mod 7 (not tested here)"
    fails += (not ok)
    print(f"{p:>4} {p%7:>7} {c:>10} {a1:>6} {ae:>9} {3*ae:>6}  {reading}{'' if ok else '   <-- FAIL'}")

# IB's own F_37 data: P_J(T) = 50653 T^6 - 450 T^3 + 1 -- a polynomial in T^3, and (1+6T+37T^2) | P_J
T = sp.symbols('T')
PJ = 50653*T**6 - 450*T**3 + 1
E37 = 1 + 6*T + 37*T**2
q, r = sp.div(PJ, E37, T)
print("\nIB's P_J over F_37 factors as", sp.factor(PJ), "; remainder of P_J / E(T):", r)
al = sp.symbols('alpha')
# with alpha + alphabar = -6, alpha*alphabar = 37:  alpha^3 + alphabar^3 = (-6)^3 - 3*37*(-6) = 450
print("alpha^3 + alphabar^3 for E at 37 =", (-6)**3 - 3*37*(-6), " (matches the -450 T^3 coefficient: P_J = (1 - alpha^3 T^3)(1 - alphabar^3 T^3))")
assert fails == 0
print("\nPASS: J(X(7)) ~ E_49^3 geometrically; the F_37 'E x simple A, Hom(E,A)=0' is the cubic-twist shadow of E^3 over a field without zeta_7^+.")
print("Consequence for the cycle count: rank NS(E^3) = 3 + 3*rank End(E) = 3 + 6 = 9 -- IB's 'nine classes' -- of which six are the cross classes from Hom(E,E) that the E x A picture would set to zero.")
