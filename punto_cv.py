def punto_cv (x1,x2,color='r',ejes = None, x_min=-5,x_max=5,y_min=-5,y_max=5):
    """
    A helper function to make a graph.
    """
    #posibles colores: 'b' blue 'g' green 'r' red 'c' cyan 'm' magenta 'y' yellow 'k' black 'w' white
    if(ejes == None):
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_aspect('equal')
        for spine in ["left", "bottom"]:
            ax.spines[spine].set_position("zero")

        for spine in ["right", "top"]:
            ax.spines[spine].set_color("none")
        ax.grid()
        ax.set_xlim(x_min,x_max)
        ax.set_ylim(y_min,y_max)
        ax.plot(x1, x2, marker="o", color=color)
        return None
    else:
        out = ejes.plot(x1, x2, marker="o", color=color)
        return out

