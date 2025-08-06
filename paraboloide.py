import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl import tri_write
from scipy.spatial import Delaunay
def paraboloide(a=1,b=1, h=1, xc = 0, yc = 0, zc = 0, normal=0, ejes = None, archivo = None):
    """Genera un paraboloide elíptico con centro en (xc,yc,zc) y altura h.
    La orientación del paraboloide se determina indicando el vector normal a la base del cilindro.
    normal == +-1 -> Paralelo al eje z (a en el sentido del eje x y orientado según el signo).
    normal == +-2 -> Paralelo al eje x (a en el sentido del eje y y orientado según el signo).
    normal == +-3 -> Paralelo al eje y (a en el sentido del eje x y orientado según el signo).
    La variable archivo permite exportar la figura en formato .stl.
    El nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""
    
    r = np.linspace(0, np.sqrt(h), endpoint=True, num=100)
    v = np.linspace(0, 2.0 * np.pi, endpoint=True, num=100)
    r, v = np.meshgrid(r, v)
    r, v = r.flatten(), v.flatten()

    # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
    # triple
    if np.abs(normal) == 1:
        X = xc + (r/a)*np.cos(v)
        Y = yc + (r/b)*np.sin(v)
        Z = zc + normal/normal * r**2

    if np.abs(normal) == 2:
        X = xc + normal/normal * r**2
        Y = yc + (r/a)*np.cos(v)
        Z = zc + (r/b)*np.sin(v)

    if np.abs(normal) == 3:
        X = xc + (r/a)*np.cos(v)
        Y = yc + normal/normal * r**2
        Z = zc + (r/b)*np.sin(v)        
        
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(r, v)
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([r, v]).T)
        #surf2stl.tri_write(archivo, X, Y, Z, delaunay_tri)     
        tri_write(archivo, X, Y, Z, delaunay_tri)
    
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return None
    else:
        out = ejes.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out
