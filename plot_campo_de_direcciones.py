import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
def plot_campo_de_direcciones(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
    """Esta función dibuja el campo de dirección de una EDO"""
    
    f_np = sp.lambdify((x, y_x), f_xy, modules='numpy')#Define una función anónima
    x_vec = np.linspace(x_lim[0], x_lim[1], 20)#Crea un array, que estará formado por 20 valores equiespaciados dentro de los limites dados.
    y_vec = np.linspace(y_lim[0], y_lim[1], 20)#Crea un array, que estará formado por 20 valores equiespaciados dentro de los limites dados.
    
    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))
    
    dx = x_vec[1] - x_vec[0]
    dy = y_vec[1] - y_vec[0]
    
    for m, xx in enumerate(x_vec):
        for n, yy in enumerate(y_vec):
            Dy = f_np(xx, yy) * dx
            Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
            Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
            ax.plot([xx - Dx/2, xx + Dx/2],
                    [yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
    
    #ax.axis('tight')
    #ax.set_title(r"$%s$" %
              #   (sp.latex(sympy.Eq(y(x).diff(x), f_xy))),
               #  fontsize=18)#Agrega como título a la ecuación en cuestión
    
    return ax
