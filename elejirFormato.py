
def elejirFormato():

    seleccionDeFormato = 1

    while seleccionDeFormato !=0 :
        try:
            seleccionDeFormato = int(input("Seleccione un formato"))
        except:
            continue
        if seleccionDeFormato > 0 and seleccionDeFormato <=3:
            return seleccionDeFormato
        else:
            continue