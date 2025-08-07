import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl import tri_write
from scipy.spatial import Delaunay
def anillo_3d(xc, yc, zc, rm=0, rM=1, normal = 0, angulo=2*sp.pi, cmap=plt.cm.Spectral, ejes = None, archivo = None):
    """Genera un anillo de radio exterior rM y radio interior rm cuyo centro es (xc,yc,zc).
    La variable ángulo permite generar un anillo incompleto.
    La orientación del disco se determina indicando el valor normal.
    normal == 1 -> Paralelo al eje z.
    normal == 2 -> Paralelo al eje x.
    normal == 3 -> Paralelo al eje y.
    La variable archivo permite exportar la figura en formato .stl.
    El nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""
     
    
    # Make a mesh in the space of parameterisation variables u and v
    u = np.linspace(0, float(angulo), endpoint=True, num=50)
    v = np.linspace(rm, rM, endpoint=True, num=50)
    
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()
      
    if normal == 1:
        # vector normal del anillo perpendicular al plano xy
        x = xc + v*np.cos(u) 
        y = yc + v*np.sin(u)
        z = np.repeat(zc, 2500)
        
    if normal == 2:
        # vector normal del anillo perpendicular al plano zy
        x = np.repeat(xc, 2500)
        y = yc + v*np.cos(u) 
        z = zc + v*np.sin(u)
        
    if normal == 3:
        # vector normal del anillo perpendicular al plano xz
        x = xc + v*np.cos(u) 
        y = np.repeat(yc, 2500)
        z = zc + v*np.sin(u)
        
    
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v)
    
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u, v]).T)
        #surf2stl.tri_write(archivo, x, y, z, delaunay_tri)    
        tri_write(archivo, x, y, z, delaunay_tri) 
    

    if(ejes == None):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=cmap)
        return None
    else:
        out = ejes.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=cmap)
        return out   
