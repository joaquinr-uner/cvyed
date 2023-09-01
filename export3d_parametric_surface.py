import numpy as np
import sympy as sp
from .surf2stl import tri_write
from scipy.spatial import Delaunay 
import matplotlib.tri as mtri
def export3d_parametric_surface(x,y,z,u,v,nu=100,nv=100,show=False,archivo=None):

    us, u1, u2 = u
    vs, v1, v2 = v

    u1, u2, v1, v2 = float([u1, u2, v1, v2])
    unum = np.linspace(u1, u2, endpoint=True, num=nu)
    vnum = np.linspace(v1, v2, endpoint=True, num=nv)
    unum, vnum = np.meshgrid(unum,vnum)
    unum, vnum = unum.flatten(), vnum.flatten()

    # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
    # triple

    X_ = sp.lambdify([us,vs],x, modules='numpy')
    Y_ = sp.lambdify([us,vs],y, modules='numpy')
    Z_ = sp.lambdify([us,vs],z, modules='numpy')

    X_num = np.array([X_(unum[i],vnum[i]) for i in range(len(unum))])
    Y_num = np.array([Y_(unum[i],vnum[i]) for i in range(len(unum))])
    Z_num = np.array([Z_(unum[i],vnum[i]) for i in range(len(unum))])


    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(unum, vnum, triangles=None)
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([unum, vnum]).T)
        tri_write(archivo, X_num, Y_num, Z_num, delaunay_tri)    

    if show:
      sp.plotting.plot3d_parametric_surface(x,y,z,(us,u1,u2),(vs,v1,v2))
