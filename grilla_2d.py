import numpy as np
def grilla_2d (x_min=0,x_max=0,y_min=0,y_max=0,cantidad=5):
    pasox = (x_max-x_min)/cantidad
    pasoy = (y_max-y_min)/cantidad
    D={}
    if x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0:
        print("Falta definir dominio")
    else:
        tmp = np.mgrid[x_min:x_max:pasox,y_min:y_max:pasoy]
        D['x'] =tmp[0].T
        D['y'] =tmp[1].T
                
    return D['x'],D['y']
