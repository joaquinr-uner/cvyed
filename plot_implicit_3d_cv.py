def plot_implicit_3d_cv (f,x1,x2,x3,cantidad_etiquetas=5):
    #La Expresió de f debe ser escriba con funciones de numpy. Por ejemplo: np.cos()
    #La función f debe contener las variables 'x','y','z'
     
    fig = mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1), size=(600, 400))
    mlab.contour3d(x1,x2,x3, f, contours=[0],opacity=0.1)
    mlab.outline(color=(0.8, 0.8, 0.8))
    mlab.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=cantidad_etiquetas)
    return fig
