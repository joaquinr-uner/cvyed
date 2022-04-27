import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot3d_parametric_line_CV(X=0,Y=0,Z=0,p=np.linspace(0, 2,100),ejes = None):
    x = np.ones_like(p)*X
    y = np.ones_like(p)*Y
    z = np.ones_like(p)*Z
    if(ejes == None):
        fig = plt.figure()
        ax3d = fig.add_subplot(projection='3d')
        #ax3d = fig.gca(projection='3d')
        ax3d.plot(x, y, z)
    
        return None
    else:
        out = ejes.plot(x, y, z)
        return out
