def esfera(x,y,z,a=1,b=1,z=0.5, ejes = None, archivo = None):
    """Genera una esfera de radio r con centro en (x,y,z)."""
    """el nombre del archivo debe contener la extensión .stl y escribirse entre comillas simples 'archivo.stl'"""
    
    u = np.linspace(0, np.pi, endpoint=True, num=100)
    v = np.linspace(0, 2.0 * np.pi, endpoint=True, num=100)
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()

    # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
    # triple
    X = a*np.sin(u)*np.cos(v)
    Y = b*np.sin(u)*np.sin(v)
    Z = c*np.cos(u)
    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v)
    if(archivo != None):
        #surf2stl.write(archivo, X, Y, Z)
        delaunay_tri = Delaunay(np.array([u, v]).T)
        #surf2stl.tri_write(archivo, X, Y, Z, delaunay_tri)     
        tri_write(archivo, X, Y, Z, delaunay_tri)
    
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return None
    else:
        out = ejes.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)
        return out
