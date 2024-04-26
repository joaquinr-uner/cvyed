import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl import tri_write
from scipy.spatial import Delaunay
def esfera(xc,yc,zc,radio=1, ejes = None, archivo = None):
    """Genera una esfera de radio r con centro en (xc,yc,zc).
    La variable archivo permite exportar la figura en formato .stl.
    El nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""
    
    u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=100)
    v = np.linspace(0, 2.0 * np.pi, endpoint=True, num=100)
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()

    # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
    # triple
    X = xc+radio*np.cos(u)*np.sin(v)
    Y = yc+radio*np.sin(u)*np.sin(v)
    Z = zc+radio*np.cos(v)
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v, triangles=None)
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u, v]).T)
        tri_write(archivo, X, Y, Z, delaunay_tri)     
    
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return None
    else:
        out = ejes.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out
