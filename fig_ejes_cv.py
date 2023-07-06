def fig_ejes_cv(color='r',x_min=-5,x_max=5,y_min=-5,y_max=5):
    #fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    fig, ax = plt.subplots()
    ax = fig.gca()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")

    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)
    return fig , ax

