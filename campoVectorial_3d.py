import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from .grilla_3d import grilla_3d
def campoVectorial_3d (F1,F2,F3,X1,X2,X3,ejes = None, color='b',normalizar = False):
    # F1, F2, F3: Componentes del campo vectorial 3d
    # X1, X2, X3: variables y rango de variación. Debe pasarse como una tupla con estructura (x, x_min, x_max)
    #posibles colores: 'b' blue 'g' green 'r' red 'c' cyan 'm' magenta 'y' yellow 'k' black 'w' white
  x1,x1_min,x1_max = X1
  x2,x2_min,x2_max = X2
  x3,x3_min,x3_max = X3

  x_max = np.max([x1_max,x2_max,x3_max,np.abs(x1_min),np.abs(x2_min),np.abs(x3_min)])
  F1l = sp.lambdify([(x1,x2,x3)],F1)
  F2l = sp.lambdify([(x1,x2,x3)],F2)
  F3l = sp.lambdify([(x1,x2,x3)],F3)

  x1n,x2n,x3n = grilla_3d(x1_min,x1_max,x2_min,x2_max,x3_min,x3_max,5)
  F1n = F1l((x1n,x2n,x3n))
  F2n = F2l((x1n,x2n,x3n))
  F3n = F3l((x1n,x2n,x3n))

  if(ejes == None):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(x1n[0][0][0],x1n[-1][-1][-1])
    ax.set_ylim(x2n[0][0][0],x2n[-1][-1][-1])
    ax.set_zlim(x3n[0][0][0],x3n[-1][-1][-1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.quiver(x1n,x2n,x3n,F1n,F2n,F3n,color = color,length=x_max/5,normalize=normalizar)
    return None
  else:
    out = ejes.quiver(x1n,x2n,x3n,F1n,F2n,F3n, color = color,length=x_max/5,normalize=normalizar)
    return out 
