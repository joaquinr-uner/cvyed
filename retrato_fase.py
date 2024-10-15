import matplotlib.pyplot as plt
import sympy as sp
from matplotlib import animation, rc
import IPython
import numpy as np
from scipy.integrate import odeint
from .grilla_2d import grilla_2d

def animate(U_,V_,cond_in,fig,axes,X=(-1,1),Y=(-1,1)):

  x_min, x_max = X
  y_min, y_max = Y
  def myODEs(vars,t,U_,V_):
      # Unpack the variables
      x,y = vars

      Ur = U_(x,y)
      Vr = V_(x,y)

      # Return the derivatives
      return [Ur, Vr]


  t = np.linspace(0, 100, 1000)
  Solutions = []
  for c in cond_in.T:
    solution = odeint(myODEs, c, t, args=(U_,V_))
    Solutions.append(solution)

  # Create the animation
  def update(frame):
      #axes.clear()
      #axes.streamplot(Xn,Yn,Un,Vn,
      #              arrowstyle='->', arrowsize=1.5)
      for sol in Solutions:
        axes.plot(sol[:frame, 0], sol[:frame, 1],'r')
      axes.set_xlim(x_min, x_max)
      axes.set_ylim(y_min, y_max)

      axes.set_xlabel('x')
      axes.set_ylabel('y')

  ani = animation.FuncAnimation(fig, update, frames=np.arange(0,1000,20), interval=100, blit=False, repeat=False)
  plt.show()
  rc('animation', html='jshtml')
  ani
  return ani

def retrato_fase(U,V,X=(sp.Symbol('x'),-1,1),Y=(sp.Symbol('y'),-1,1),densidad = 1, color= 'b', cond_in = [None,None], ejes = None, anim = False):
    if None not in cond_in:
      a,b = cond_in
      cond_in = np.array([a,b])
      if cond_in.ndim == 1:
        cond_in = np.expand_dims(cond_in,1)

    x, xmin, xmax = X
    y, ymin, ymax = Y

    Xn, Yn = grilla_2d(xmin,xmax,ymin,ymax,cantidad=100)

    variables = (x,y)
    U_ = sp.lambdify(variables, U, modules='numpy')
    V_ = sp.lambdify(variables, V, modules='numpy')

    Un = U_(Xn,Yn)
    Vn = V_(Xn,Yn)

    if(ejes == None):
        #Definimos una figura
        fig = plt.figure()
        axes = fig.gca()
        #ax0 = fig.add_subplot()
        if anim == False:
          axes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad, color='b',
                          arrowstyle='->', arrowsize=1.5)
          if None not in cond_in:
            axes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad, color='r',
                            start_points = cond_in.T, arrowstyle='->', arrowsize=1.5)
            axes.plot(cond_in[0], cond_in[1], 'bo')

          axes.set_xlabel('x')
          axes.set_ylabel('y')
          axes.plot([0,0],[Yn[0][0],Yn[len(Yn)-1][len(Yn)-1]],'k',lw=1.5,alpha=0.75)#Eje y
          axes.plot([Xn[0][0],Xn[len(Xn)-1][len(Xn)-1]],[0,0],'k',lw=1.5,alpha=0.75)#Eje x
          return None
        else:
          axes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad, color='b',
                          arrowstyle='->', arrowsize=1.5)

          axes.plot(cond_in[0], cond_in[1], 'bo')
          axes.set_xlabel('x')
          axes.set_ylabel('y')
          axes.plot([0,0],[Yn[0][0],Yn[len(Yn)-1][len(Yn)-1]],'k',lw=1.5,alpha=0.75)#Eje y
          axes.plot([Xn[0][0],Xn[len(Xn)-1][len(Xn)-1]],[0,0],'k',lw=1.5,alpha=0.75)#Eje x
          ani = animate(U_,V_,cond_in,fig,axes,(xmin,xmax),(ymin,ymax))
          return ani

    else:
        if anim == False:
          ejes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad, color='b',
                          arrowstyle='->', arrowsize=1.5)
          if None not in cond_in:
            ejes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad, color='r',
                            start_points = cond_in.T, arrowstyle='->', arrowsize=1.5)
            ejes.plot(cond_in[0], cond_in[1], 'bo')
            
          ejes.set_xlabel('x')
          ejes.set_ylabel('y')
          ejes.plot([0,0],[Yn[0][0],Yn[len(Yn)-1][len(Yn)-1]],'k',lw=1.5,alpha=0.75)#Eje y
          ejes.plot([Xn[0][0],Xn[len(Xn)-1][len(Xn)-1]],[0,0],'k',lw=1.5,alpha=0.75)#Eje x

          return out
        else:
          ejes.streamplot(Xn, Yn, Un, Vn,linewidth=1, density=densidad,color='b',
                          arrowstyle='->', arrowsize=1.5)
          ejes.plot(cond_in[0], cond_in[1], 'bo')
          ejes.set_xlabel('x')
          ejes.set_ylabel('y')
          ejes.plot([0,0],[Yn[0][0],Yn[len(Yn)-1][len(Yn)-1]],'k',lw=1.5,alpha=0.75)#Eje y
          ejes.plot([Xn[0][0],Xn[len(Xn)-1][len(Xn)-1]],[0,0],'k',lw=1.5,alpha=0.75)#Eje x

          ani = animate(U_,V_,cond_in,fig,ejes)
          return ani
