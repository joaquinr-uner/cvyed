import matplotlib.pyplot as plt
import sympy as sp
from matplotlib import animation, rc
import IPython
import numpy as np
from .grilla_2d import grilla_2d

def animar_edp(u,range_t,range_x,fig=plt.figure(),axes=fig.gca()):

  t, t_in, t_fin = range_t
  x, x_min, x_max = range_x
  
  u_ = sp.lambdify((t,x), u, modules='numpy')
  
  n = 1000

  xi, ti = grilla_2d(x_min,x_max,t_in,t_fin,cantidad=100)
  un = u_(ti,xi)

  u_max, u_min = np.max(un), np.min(un)
  
  xn = np.linspace(x_min,x_max,n)
  tn = np.linspace(t_in,t_fin,n//10)
  # Create the animation
  def update(frame):
    #axes.clear()
    #axes.streamplot(Xn,Yn,Un,Vn,
    #              arrowstyle='->', arrowsize=1.5)
    Uf = u_(frame,xn)
    axes.clear()
    axes.plot(xn,Uf,'b',label=f't = {frame:.2f}')
    axes.set_xlim(x_min, x_max)
    axes.set_ylim(u_min, u_max)
    axes.set_xlabel('x')
    axes.set_ylabel('u(x,t)')
    axes.set_title('u')
    axes.legend()

  ani = animation.FuncAnimation(fig, update, frames=tn, interval=50, blit=False, repeat=True)
  plt.show()
  rc('animation', html='jshtml')
  ani
  return ani
