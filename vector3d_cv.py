def vector3d_cv (x1,x2,x3,y1,y2,y3,ejes = None, color='b',x_min=-5,x_max=5,y_min=-5,y_max=5,z_min=-5,z_max=5):
    #posibles colores: 'b' blue 'g' green 'r' red 'c' cyan 'm' magenta 'y' yellow 'k' black 'w' white
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(y_min,y_max)
        ax.set_zlim(z_min,z_max)    
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.quiver(x1,x2,x3,(y1-x1),(y2-x2),(y3-x3), color = color)
        return None
    else:
        out = ejes.quiver(x1,x2,x3,(y1-x1),(y2-x2),(y3-x3), color = color)
        return out
