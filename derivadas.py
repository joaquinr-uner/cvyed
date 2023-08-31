def derivadas(func,orden):
    for sym in f.free_symbols:
        t = sym
    derivadas = []
    #derivada[0]=func
    for i in range(orden):
        derivadas.append(func.diff(t,i))
    return derivadas
