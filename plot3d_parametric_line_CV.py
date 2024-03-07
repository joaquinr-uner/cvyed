import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot3d_parametric_line_CV(X=0,Y=0,Z=0,p=np.linspace(0, 2,100),ejes = None):
    if X is not
    X1_ = sp.lambdify(t, X, modules='numpy')
    X2_ = sp.lambdify(t, Y, modules='numpy')
    X3_ = sp.lambdify(t, Z, modules='numpy')
    
    t_num = np.linspace(float(t1), float(t2), endpoint=True, num=100)
    
    X1_num = np.array([X1_(t_num[i]) for i in range(100)])
    X2_num = np.array([X2_(t_num[i]) for i in range(100)])
    X3_num = np.array([X3_(t_num[i]) for i in range(100)])
    
    
    #x = np.ones_like(p)*X
    #y = np.ones_like(p)*Y
    #z = np.ones_like(p)*Z
    
    
    
    if(ejes == None):
        fig = plt.figure()
        ax3d = fig.gca(projection='3d')
        ax3d.plot(X1_num, X2_num, X3_num)
    
        return None
    else:
        out = ejes.plot(X1_num, X2_num, X3_num)
        return out
