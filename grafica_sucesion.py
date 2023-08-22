import matplotlib.pyplot as plt
import numpy as np
def grafica_sucesion(nn,A_n,ejes = None, label = ''):
    
    if type(A_n) is list:
        a_n=A_n
    else:
        a_n  = [A_n.subs(n,i) for i in nn]
    
    
    if(ejes == None):
        #Definimos una figura
        fig = plt.figure()
        axes = fig.gca()
        #Graficamos (mediante puntos) sucesión {1/n} en el intervalo que creamos: (k,k+n) con pasos de 1
        #axes.scatter(n, a_n, label="1/n",s = 10)
        axes.plot(nn, a_n,label=label,marker='o',ls='--')# ls = estilo de linea
        #Definimos las etiquetasde los ejes
        plt.xlabel('n')
        plt.ylabel('a_n')
        #Define el rango de visualizacion de n
        axes.set_xlim(nn[0],nn[len(nn)-1])
        #Agrega una grilla
        axes.grid()
        #Agrega una leyenda
        axes.legend()
    
        return None
    else:
        out = ejes.plot(n, a_n,label=label,marker='o',ls='--')# ls = estilo de linea
        return out
