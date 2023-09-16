import matplotlib.pyplot as plt
def retrato_fase(X,Y,U,V,densidad = 1, color= 'b', cond_in = [None,None], ejes = None):
    if None not in cond_in:
      a,b = cond_in
      cond_in = np.array([a,b])
      if cond_in.ndim == 1:
        cond_in = np.expand_dims(cond_in,1)

    if(ejes == None):
        #Definimos una figura
        fig = plt.figure()
        axes = fig.gca()
        #ax0 = fig.add_subplot()
        if None not in cond_in:
          axes.streamplot(X, Y, U, V,linewidth=1, density=densidad, color=color,
                          start_points = cond_in.T, arrowstyle='->', arrowsize=1.5)
          axes.plot(cond_in[0], cond_in[1], 'bo')
        else:
          axes.streamplot(X, Y, U, V,linewidth=1, density=densidad, color=color,
                          arrowstyle='->', arrowsize=1.5)
        #ax0.plot(0,0,"red", marker = "o", markersize = 10.0)
        axes.plot([0,0],[Y[0][0],Y[len(Y)-1][len(Y)-1]],'k',lw=3,alpha=0.25)#Eje y 
        axes.plot([X[0][0],X[len(X)-1][len(X)-1]],[0,0],'k',lw=3,alpha=0.25)#Eje x
        return None
    else:
        if None not in cond_in:
          out = ejes.streamplot(X, Y, U, V,linewidth=1, density=densidad, color=color,
                        start_points = cond_in.T, arrowstyle='->', arrowsize=1.5)
          ejes.plot(cond_in[0], cond_in[1], 'bo')
        else:
          out = ejes.streamplot(X, Y, U, V,linewidth=1, density=densidad, color=color,
                        arrowstyle='->', arrowsize=1.5)
        
        ejes.plot([0,0],[Y[0][0],Y[len(Y)-1][len(Y)-1]],'k',lw=3,alpha=0.25)#Eje y 
        ejes.plot([X[0][0],X[len(X)-1][len(X)-1]],[0,0],'k',lw=3,alpha=0.25)#Eje x
        return out
