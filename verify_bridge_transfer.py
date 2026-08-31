# -*- coding: utf-8 -*-
r"""verify_bridge_transfer.py

Computes the BRIDGE SPECIFICATION transfer table for the Scar-Cat spine, from
group theory ONLY (no physical / conceptual labels). For each consecutive pair
of spine groups it enumerates every subgroup up to isomorphism type and reports
which types SURVIVE (shared), are LOST (upper-only), and APPEAR (lower-only).

Spine groups (from SPINE MAP v0.1):
  L7 PSL(2,7)  L6 C6xZ2  L5 A5  L4 S4  L3 A4  L2 Z2  L1 {e}

Method: every subgroup here is <=2-generated, so the full set of subgroup
iso-types = { type(<x,y>) : x,y in G }. Iso-type fingerprint = (order,
element-order profile), which separates all types that occur. Not RH/GRH.

Run:  python -X utf8 verify_bridge_transfer.py
"""

def compose(p, q): return tuple(p[q[i]] for i in range(len(p)))
def order_of(p, e):
    x = p; k = 1
    while x != e: x = compose(x, p); k += 1
    return k

class Group:
    def __init__(self, name, elements):
        self.name = name
        self.el = list(elements); self.n = len(self.el)
        deg = len(self.el[0]); self.e0 = tuple(range(deg))
        self.idx = {g: i for i, g in enumerate(self.el)}
        self.e = self.idx[self.e0]
        self.ord = [order_of(g, self.e0) for g in self.el]
        self.mul = [[self.idx[compose(a, b)] for b in self.el] for a in self.el]
    def closure(self, gens):
        G = {self.e} | set(gens); fr = list(G)
        while fr:
            a = fr.pop()
            for g in gens:
                b = self.mul[a][g]
                if b not in G: G.add(b); fr.append(b)
        return frozenset(G)
    def fp(self, H):
        prof = {}
        for i in H: prof[self.ord[i]] = prof.get(self.ord[i], 0) + 1
        return (len(H), tuple(sorted(prof.items())))
    def subgroup_types(self):
        types = {self.fp(frozenset([self.e]))}
        cyc = {}
        for i in range(self.n):
            H = self.closure([i]); cyc[i] = H; types.add(self.fp(H))
        for a in range(self.n):
            Ca = cyc[a]
            for b in range(a + 1, self.n):
                if b in Ca: continue                 # <a,b> = <a>
                types.add(self.fp(self.closure([a, b])))
        return types

def name(fp):
    order, items = fp; prof = dict(items)
    h = lambda k: prof.get(k, 0)
    if order == 1: return "1"
    if order == 2: return "C2"
    if order == 3: return "C3"
    if order == 4: return "C4" if h(4) else "V4"
    if order == 5: return "C5"
    if order == 6: return "C6" if h(6) else "S3"
    if order == 7: return "C7"
    if order == 8: return "D4" if h(4) == 2 else ("Q8" if h(4) == 6 else f"?8")
    if order == 10: return "C10" if h(10) else "D5"
    if order == 12:
        if prof == {1:1,2:3,3:8}: return "A4"
        if h(6) == 2 and h(2) == 7: return "D6"
        if h(4) == 6: return "Dic3"
        if h(12): return "C12"
        if h(6) == 6: return "C6xC2"
        return "?12"
    if order == 20: return "F20(5:4)"
    if order == 21: return "F21(7:3)"
    if order == 24: return "S4" if h(2) == 9 else "?24"
    if order == 60: return "A5"
    if order == 168: return "PSL(2,7)"
    return f"?{order}"

def named_types(G):
    return {name(fp) for fp in G.subgroup_types()}

# ---- build the spine groups ----
def gen(perms): return Group.__init__  # unused
S5 = [None]
# S5 to slice A5
def closure_perms(gens):
    n = len(gens[0]); e = tuple(range(n)); G = {e}; fr = [e]
    while fr:
        a = fr.pop()
        for g in gens:
            b = compose(a, g)
            if b not in G: G.add(b); fr.append(b)
    return G
S5set = closure_perms([(1,2,3,4,0), (1,0,2,3,4)])
def even(g): return sum(1 for i in range(5) for j in range(i+1,5) if g[i]>g[j]) % 2 == 0
A5 = Group("A5", [g for g in S5set if even(g)])
S4 = Group("S4", closure_perms([(1,2,3,0), (1,0,2,3)]))
A4 = Group("A4", closure_perms([(1,2,0,3), (0,2,3,1)]))
Z2 = Group("Z2", closure_perms([(1,0)]))
E1 = Group("1", closure_perms([(0,)]))
# C6 x Z2 on 8 points: 6-cycle on 0..5, swap 6,7
C6Z2 = Group("C6xZ2", closure_perms([(1,2,3,4,5,0,6,7), (0,1,2,3,4,5,7,6)]))
# PSL(2,7) as Mobius maps on P^1(F7) = {0..6, oo=7}
def inv7(k): return pow(k % 7, 5, 7)
def mobius(M):
    a,b,c,d = M; img = []
    for x in range(8):
        if x == 7: img.append(7 if c % 7 == 0 else (a*inv7(c)) % 7)
        else:
            den = (c*x+d) % 7
            img.append(7 if den == 0 else ((a*x+b) % 7 * inv7(den)) % 7)
    return tuple(img)
SL27 = [(a,b,c,d) for a in range(7) for b in range(7) for c in range(7) for d in range(7) if (a*d-b*c) % 7 == 1]
PSL27 = Group("PSL(2,7)", {mobius(M) for M in SL27})

SPINE = [("7", PSL27), ("6", C6Z2), ("5", A5), ("4", S4), ("3", A4), ("2", Z2), ("1", E1)]
print("Enumerating subgroup iso-types per spine level...")
T = {}
for lvl, G in SPINE:
    T[lvl] = named_types(G)
    print(f"  L{lvl} {G.name:9s} |G|={G.n:3d}  types: {sorted(T[lvl], key=lambda s:(len(s),s))}")

# each group's own iso-type NAME (so inclusion tests match the type-name sets)
selftype = {lvl: name(G.fp(frozenset(range(G.n)))) for lvl, G in SPINE}

print()
print("=" * 78)
print("BRIDGE TRANSFER TABLE (subgroup iso-types; descent upper -> lower)")
print("=" * 78)
rows = []
for (lu, Gu), (ll, Gl) in zip(SPINE, SPINE[1:]):
    up, lo = T[lu], T[ll]
    survives = sorted(up & lo, key=lambda s: (len(s), s))
    lost     = sorted(up - lo, key=lambda s: (len(s), s))
    appears  = sorted(lo - up, key=lambda s: (len(s), s))
    # structural type signals (compare each group's own iso-type name)
    lo_in_up = selftype[ll] in up     # lower group embeds in upper (inclusion)
    up_in_lo = selftype[lu] in lo
    rows.append((lu, ll, Gu.name, Gl.name, survives, lost, appears, lo_in_up, up_in_lo))
    print(f"\n{lu}<->{ll}   {Gu.name}  ->  {Gl.name}")
    print(f"   SURVIVES ({len(survives)}): {', '.join(survives)}")
    print(f"   LOST     ({len(lost)}): {', '.join(lost) or '-'}")
    print(f"   APPEARS  ({len(appears)}): {', '.join(appears) or '-'}")
    incl = ("inclusion: lower<=upper" if lo_in_up else
            ("inclusion: upper<=lower" if up_in_lo else "neither embeds in the other (crossing)"))
    print(f"   structure: {incl}"
          + ("  [appears=empty => pure descent by loss]" if not appears else ""))

print("\n" + "=" * 78)
print("Markdown table")
print("=" * 78)
print("| bridge | upper | lower | survives | lost | appears | structure |")
print("|---|---|---|---|---|---|---|")
for lu, ll, gu, gl, s, l, a, loin, upin in rows:
    st = "lower⊆upper" if loin else ("upper⊆lower" if upin else "crossing")
    print(f"| {lu}↔{ll} | {gu} | {gl} | {', '.join(s)} | {', '.join(l) or '—'} "
          f"| {', '.join(a) or '—'} | {st} |")

print("\n" + "=" * 78)
print("Two structural observations (group theory only):")
print("- The SHARED FLOOR of every bridge is {1, C2, C3, V4} at the top two")
print("  bridges and grows downward; 7<->6 and 6<->5 share EXACTLY {1,C2,C3,V4}")
print("  -> the '7<->6 quantum gap' is not 'no common subgroup' (they share the")
print("  small abelian floor + V4); it is: neither embeds in the other AND no")
print("  order-6 / mediator type bridges them (PSL(2,7) has no C6).")
print("- With the SPINE-MAP choice L6 = C6xZ2 (abelian), S3 is LOST at 7<->6.")
print("  But the 7<->6 BRIDGE file uses L6 = W(E6) and reports the intersection")
print("  = S3 = N(<z3>). Same 'level 6', two different groups -> the S3 either")
print("  survives (W(E6) reading) or is lost (C6xZ2 reading). This is the level-")
print("  label inconsistency, made concrete. Reconcile L6 before sealing.")
print("Not RH/GRH.")
