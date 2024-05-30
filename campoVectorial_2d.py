import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from .grilla_2d import grilla_2d
def campoVectorial_2d (F1,F2,X1,X2,ejes = None,color='b', angles='xy', scale_units='xy', scale=1, npuntos = 10, normalizar=True):
    # F1, F2: Componentes del campo vectorial 2d
    # X1, X2: variables y rango de variación. Debe pasarse como una tupla con estructura (x, x_min, x_max)
    #posibles colores: 'b' blue 'g' green 'r' red 'c' cyan 'm' magenta 'y' yellow 'k' black 'w' white
    
    x1,x1_min,x1_max = X1
    x2,x2_min,x2_max = X2

    x_max = np.max([x1_max,x2_max,np.abs(x1_min),np.abs(x2_min)])
    F1l = sp.lambdify([(x1,x2)],F1)
    F2l = sp.lambdify([(x1,x2)],F2)
    
    x1n,x2n = grilla_2d(x1_min,x1_max,x2_min,x2_max,npuntos)
    F1n = F1l((x1n,x2n))
    F2n = F2l((x1n,x2n))

    if normalizar==True:
        F1n = F1n/(np.sqrt(F1n**2+F2n**2))
        F2n = F2n/(np.sqrt(F1n**2+F2n**2))
    
    F1n[np.isnan(F1n)] = 0
    F2n[np.isnan(F2n)] = 0
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca()
        ax.set_aspect('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_position("zero")

        for spine in ["right", "top"]:
            ax.spines[spine].set_color("none")
        ax.grid()
        #ax.set_xlim(x1[0][0],x1[-1][-1])
        #ax.set_ylim(x2[0][0],x2[-1][-1])
        ax.quiver(x1n,x2n,F1n,F2n, color = color,angles=angles, scale_units=scale_units, scale=scale)
        return None
    else:
        out = ejes.quiver(x1n,x2n,F1n,F2n, color = color,angles=angles, scale_units=scale_units, scale=scale)
        return out 
