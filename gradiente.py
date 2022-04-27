def gradiente(funcion_escalar, variables):
    matrix_funcion_escalar = sp.Matrix([funcion_escalar])#definimos una matriz de un solo elemento
    return matrix_funcion_escalar.jacobian(variables)
