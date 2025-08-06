import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from .surf2stl import tri_write
from scipy.spatial import Delaunay
def cilindro(r=1, h=5, xc=0, yc=0, zc=0, normal = 0, a=1, b=1, t=2*np.pi, ejes = None, archivo = None):
    """Genera un cilindro de radio r, cuyo base se centra en el punto (xc,yc,zc) y su altura es h.
    También podemos generar un cilindro elíptico pasando parámetros a y b distintos.
    La orientación del cilindro se determina indicando el vector normal a la base del cilindro.
    normal == 0 -> Paralelo al eje z.
    normal == 1 -> Paralelo al eje x.
    normal == 2 -> Paralelo al eje y.
    La variable archivo permite exportar la figura en formato .stl.
    El nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""


    # Make a mesh in the space of parameterisation variables u and v
    u = np.linspace(0, t, endpoint=True, num=50)
    
    if normal == 1:
        # vector normal del cilindro perpendicular al plano xy
        v = np.linspace(zc, zc+h, endpoint=True, num=50)
        
    if normal == 2:
        # vector normal del cilindro perpendicular al plano zy
        v = np.linspace(xc, xc+h, endpoint=True, num=50)
       
    if normal == 3:
        # vector normal del cilindro perpendicular al plano xz
        v = np.linspace(yc, yc+h, endpoint=True, num=50)    
    
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()
      
    if normal == 0:
        # ecuaciones parámetricas del cilindro perpendicular al plano xy
        x = xc + a*r*np.cos(u) 
        y = yc + b*r*np.sin(u)
        z = zc + v
        
    if normal == 1:
        # ecuaciones parámetricas del cilindro perpendicular al plano zy
        x = xc + v
        y = yc + a*r*np.cos(u) 
        z = zc + b*r*np.sin(u)
        
    if normal == 2:
        # ecuaciones parámetricas del cilindro perpendicular al plano xz
        x = xc + a*r*np.cos(u) 
        y = yc + v
        z = zc + b*r*np.sin(u)
        
    
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v)
    
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u, v]).T)
        #surf2stl.tri_write(archivo, x, y, z, delaunay_tri)    
        tri_write(archivo, x, y, z, delaunay_tri) 
    

    if(ejes == None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return None
    else:
        out = ejes.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out   
