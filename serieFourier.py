import sympy as sp
def serieFourier(ft,L,n):
    x,m = sp.symbols('x,m')
    a0 = 1/L*sp.integrate(ft,(x,-L,L))
    am = 1/L*sp.integrate(ft*sp.cos(m*sp.pi*x/L),(x,-L,L))
    bm = 1/L*sp.integrate(ft*sp.sin(m*sp.pi*x/L),(x,-L,L))

    serie = (a0/2)
    for i in range(1, n+1):
        i
        serie = serie + (am*sp.cos(m*sp.pi*x/L)+(bm*sp.sin(m*sp.pi*x/L))).subs(m, i)
    return serie
