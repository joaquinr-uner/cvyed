import numpy as np

def sup_nivel_cv(x=np.linspace(-5, 5,100),y=np.linspace(1, 2,100),Z=0):

    n_radii = 8
    n_angles = 36

    # Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
    #radii = np.linspace(0.125, 1.0, n_radii)
    #angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

    # Convert polar (radii, angles) coords to cartesian (x, y) coords.
    # (0, 0) is manually added at this stage,  so there will be no duplicate
    # points in the (x, y) plane.
    #x = np.append(0, (radii*np.cos(angles)).flatten())
    #y = np.append(0, (radii*np.sin(angles)).flatten())

    # Compute z to make the pringle surface.
    #z = 1/2*(x**2 + y**2)**(1/2)
    z=Z
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

    plt.show()
    return None
