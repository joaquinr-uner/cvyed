import numpy as np
def euler(a, b, h, y0,fun):
    """ Metodo de Euler en el intervalo [a, b] usando un paso de h y condición inicial y0 """
    
    N = int((b - a)/h) # definimos la cantidad de iteraciones necesarias para recorrer el intervalo [ a , b ]

    # inicializacion el vector de variables independientes x correspondiente al paso definido 
    # y al respectivo vector de variables dependientes que tendra el resultado que estamos buscando.

    x = np.zeros( N+1 ) # Genera un vector completo de cero, con una cantidad de elementos igual a N+1 
    y = np.zeros( N+1 ) # Se le suma una, pues se deben cubrir la cantidad de pasos y además considerar a la condición inicial dada.

    x[0] = a # variable independiente asociada a la condición inicial.
    y[0] = y0 # valor inicial.
    
    # Metodo de Euler
    for n in range( N) :
        y[n+1] = y[n] + h * fun(x[n], y[n])
        x[n+1] = x[n] + h

    return (x, y)
