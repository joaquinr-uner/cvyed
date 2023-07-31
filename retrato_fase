def retrato_fase(X,Y,U,V,ejes = None):
    
    if(ejes == None):
        #Definimos una figura
        fig = plt.figure()
        axes = fig.gca()
        #ax0 = fig.add_subplot()
        axes.streamplot(X, Y, U, V,linewidth=1, arrowstyle='->', arrowsize=1.5)
        #ax0.plot(0,0,"red", marker = "o", markersize = 10.0)
        axes.plot([0,0],[Y[0][0],Y[len(Y)-1][len(Y)-1]],'k',lw=3,alpha=0.25)#Eje y 
        axes.plot([X[0][0],X[len(X)-1][len(X)-1]],[0,0],'k',lw=3,alpha=0.25)#Eje x
        return None
    else:
        out = ejes.streamplot(X, Y, U, V,linewidth=1, arrowstyle='->', arrowsize=1.5)
        return out
