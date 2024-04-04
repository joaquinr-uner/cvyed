import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl import tri_write
from scipy.spatial import Delaunay
def cilindro(r=1, h=5, xc=0, yc=0, zc=0, normal = 0, ejes = None, archivo = None):
    """Genera un cilindro de radio r, cuyo base se centra en el punto (xc,yc,zc) y su altura es h."""
    """La orientación del cilindro se determina indicando el vector normal a la base del cilindro."""
    """el nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""


    # Make a mesh in the space of parameterisation variables u and v
    u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
    
    if normal == 0:
        # vector normal del cilindro perpendicular al plano xy
        v = np.linspace(zc, zc+h, endpoint=True, num=50)
        
    if normal == 1:
        # vector normal del cilindro perpendicular al plano zy
        v = np.linspace(xc, xc+h, endpoint=True, num=50)
       
    if normal == 2:
        # vector normal del cilindro perpendicular al plano xz
        v = np.linspace(yc, yc+h, endpoint=True, num=50)    
    
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()
      
    if normal == 0:
        # vector normal del cilindro perpendicular al plano xy
        x = xc + r*np.cos(u) 
        y = yc + r*np.sin(u)
        z = v
        
    if normal == 1:
        # vector normal del cilindro perpendicular al plano zy
        x = v
        y = yc + r*np.cos(u) 
        z = zc + r*np.sin(u)
        
    if normal == 2:
        # vector normal del cilindro perpendicular al plano xz
        x = xc + r*np.cos(u) 
        y = v
        z = zc + r*np.sin(u)
        
    
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v)
    
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u, v]).T)
        #surf2stl.tri_write(archivo, x, y, z, delaunay_tri)    
        tri_write(archivo, x, y, z, delaunay_tri) 
    

    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return None
    else:
        out = ejes.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out   
