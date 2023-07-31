import numpt as np
def grilla_3d (x_min=0,x_max=0,y_min=0,y_max=0,z_min=0,z_max=0,cantidad=5):
    pasox = (x_max-x_min)/cantidad
    pasoy = (y_max-y_min)/cantidad
    pasoz = (z_max-z_min)/cantidad
    D={}
    if x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0:
        print("Falta definir dominio")
    elif (x_min != 0 or x_max != 0) and (y_min != 0 or y_max != 0) and (z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['x'] =tmp[0]
        D['y'] =tmp[1]
        D['z'] =tmp[2]
    elif x_min == 0 and x_max == 0 and (y_min != 0 or y_max != 0 or z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['y'] =tmp[1]
        D['z'] =tmp[2]
    elif y_min == 0 and y_max == 0 and (x_min != 0 or x_max != 0 or z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['x'] =tmp[1]
        D['z'] =tmp[2]
    elif z_min == 0 and z_max == 0 and (x_min != 0 or x_max != 0 or y_min != 0 or y_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['x'] =tmp[1]
        D['y'] =tmp[2]
    elif y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0 and (x_min != 0 or x_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['x'] =tmp[2]
    elif y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0 and (y_min != 0 or y_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['y'] =tmp[2]
    elif x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0 and (z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max+pasox:pasox,y_min:y_max+pasoy:pasoy,z_min:z_max+pasoz:pasoz]
        D['z'] =tmp[2]        
                
    return D['x'],D['y'],D['z']
