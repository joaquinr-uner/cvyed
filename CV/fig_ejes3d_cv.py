def fig_ejes3d_cv(color='r',x_min=-5,x_max=5,y_min=-5,y_max=5,z_min=-5,z_max=5):
    #fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    #fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)
    ax.set_zlim(z_min,z_max)
    return fig , ax
