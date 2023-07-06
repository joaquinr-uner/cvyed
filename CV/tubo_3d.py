import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import surf2stl
from scipy.spatial import Delaunay

def tubo_3d(x,y,z,t1=-10,t2=10,radio=1, ejes = None, archivo = None):
    """Genera un tubo de radio r en la dirección de la curva en el espacio dada por <x,y,z>."""
    """Las varias x,y,z deben escribirse como funciones de Sympy"""   
    """el nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""
    u = sp.symbols('u',real=True)#se puede hacer la acalración de que t pertenece a los reales.
    t = sp.symbols('t')
    a=radio
    c = sp.Matrix([x,y,z])
    cp = sp.diff(c,t)
    cpp = sp.diff(cp,t)
    n=cpp/cpp.norm()
    b=cp.cross(n)/cp.norm()
    s=c+a*n*sp.cos(u)+a*b*sp.sin(u)
    
    variables = (u, t)
    X1_ = sp.lambdify(variables, s[0], modules='numpy')
    X2_ = sp.lambdify(variables, s[1], modules='numpy')
    X3_ = sp.lambdify(variables, s[2], modules='numpy')
    
    
    u_num = np.linspace(0, 2.0 * np.pi, endpoint=True, num=100)
    t_num = np.linspace(float(t1), float(t2), endpoint=True, num=100)
    u_num, t_num = np.meshgrid(u_num, t_num)
    u_num, t_num = u_num.flatten(), t_num.flatten()
    
    X1_num = np.array([X1_(u_num[i],t_num[i]) for i in range(10000)])
    X2_num = np.array([X2_(u_num[i],t_num[i]) for i in range(10000)])
    X3_num = np.array([X3_(u_num[i],t_num[i]) for i in range(10000)])

    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u_num,t_num)
    
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u_num, t_num]).T)
        surf2stl.tri_write(archivo, X1_num, X2_num, X3_num, delaunay_tri) 
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_box_aspect([np.ptp(X1_num),np.ptp(X2_num),np.ptp(X3_num)]) 
        ax.plot_trisurf(X1_num, X2_num, X3_num, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return c,cp,cpp,n,b,s
    else:
        out = ejes.plot_trisurf(X1_num, X2_num, X3_num, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out
