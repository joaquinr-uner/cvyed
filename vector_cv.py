def vector_cv (x1,x2,y1,y2,ejes = None,color='b',x_min=-5,x_max=5,y_min=-5,y_max=5):
    #posibles colores: 'b' blue 'g' green 'r' red 'c' cyan 'm' magenta 'y' yellow 'k' black 'w' white
    
    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca()
        ax.set_aspect('equal')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_position("zero")

        for spine in ["right", "top"]:
            ax.spines[spine].set_color("none")
        ax.grid()
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(y_min,y_max)
        ax.quiver(x1,x2,(y1-x1),(y2-x2), color = color, angles='xy', scale_units='xy', scale=1)
        return None
    else:
        out = ejes.quiver(x1,x2,(y1-x1),(y2-x2), color = color, angles='xy', scale_units='xy', scale=1)
        return out
        
