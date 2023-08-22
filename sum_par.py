import numpy as np
import sympy as sp
def sum_par(a_n,inicio,final):
    # definimos la sumatora que va desde el inicio al valor final.

    n = sp.Symbol('n')
    lista = []
    #Define una variable donde se acumula la suma
    suma = 0

    #definimos una iteracion para sumar los terminos de la serie
    for i in range(inicio,final+1):
        suma += a_n.subs(n,i)
        lista.append(suma)
    return np.array(lista)
