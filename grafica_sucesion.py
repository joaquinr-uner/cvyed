import matplotlib.pyplot as plt
def grafica_sucesion(n,A_n,ejes = None):
    
    #Cantidad de terminos de la sucesion a graficar
    #N=100
    #Valor inicial del indice n de la sucesión
    #k=1
    # Creamos un rango de valores dentro del intervalo (k,k+N), 
    #nn = np.arange(k,k+N)
    
    #la expresion anterior lo que esta realizando es un bucle, donde se reemplaza el valor de n por cada uno de los elementos del rAngo definido.
    #a_n=[A_n for n in nn]
    a_n=A_n
    
    
    if(ejes == None):
        #Definimos una figura
        fig = plt.figure()
        axes = fig.gca()
        #Graficamos (mediante puntos) sucesión {1/n} en el intervalo que creamos: (k,k+n) con pasos de 1
        #axes.scatter(n, a_n, label="1/n",s = 10)
        axes.plot(n, a_n,marker='o',ls='--')# ls = estilo de linea
        #Definimos las etiquetasde los ejes
        plt.xlabel('n')
        plt.ylabel('a_n')
        #Define el rango de visualizacion de n
        axes.set_xlim(n[0],n[len(n)-1])
        #Agrega una grilla
        axes.grid()
        #Agrega una leyenda
        axes.legend()
    
        return None
    else:
        out = ejes.plot(n, a_n,marker='o',ls='--')# ls = estilo de linea
        return out
