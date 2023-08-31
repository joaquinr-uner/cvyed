def derivadas(func,orden):
    derivadas = []
    #derivada[0]=func
    for i in range(orden):
        derivadas.append(func.diff(x,i))
    return derivadas
