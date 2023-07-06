def dominio (x_min=0,x_max=0,y_min=0,y_max=0,z_min=0,z_max=0):
    D={}
    if x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0:
        print("Falta definir dominio")
    elif (x_min != 0 or x_max != 0) and (y_min != 0 or y_max != 0) and (z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['x'] =tmp[0]
        D['y'] =tmp[1]
        D['z'] =tmp[2]
    elif x_min == 0 and x_max == 0 and (y_min != 0 or y_max != 0 or z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['y'] =tmp[1]
        D['z'] =tmp[2]
    elif y_min == 0 and y_max == 0 and (x_min != 0 or x_max != 0 or z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['x'] =tmp[1]
        D['z'] =tmp[2]
    elif z_min == 0 and z_max == 0 and (x_min != 0 or x_max != 0 or y_min != 0 or y_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['x'] =tmp[1]
        D['y'] =tmp[2]
    elif y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0 and (x_min != 0 or x_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['x'] =tmp[2]
    elif y_min == 0 and y_max == 0 and z_min == 0 and z_max == 0 and (y_min != 0 or y_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['y'] =tmp[2]
    elif x_min == 0 and x_max == 0 and y_min == 0 and y_max == 0 and (z_min != 0 or z_max != 0):
        tmp = np.mgrid[x_min:x_max:100j,y_min:y_max:100j,z_min:z_max:100j]
        D['z'] =tmp[2]        
                
    return D['x'],D['y'],D['z']
