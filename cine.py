import sqlite3
#cambio para probar git
base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

peliculas = "SELECT * FROM PELICULAS;"
salas = "SELECT * FROM SALAS;"
#cargar_pelicula = "INSERT INTO FUNCIONES(ID_PELICULAS, ID_SALAS, FECHA_HORA, BUTACAS_LIBRES) VALUES(1);"

def opcionesDeBienvenida():
    print("Bienvenido a CINE DB")
    print()
    print("Elegir Opción: ")
    print("1- Ver Carteleras")
    print("2- Ver Formatos")
    print("3- Crear función")
    print("4- Entradas")
    print("5- Salir")

def ver_carteleras():
    c.execute(peliculas)
    resp = c.fetchall()
    for i in resp:
        print(i)
    cantidadDePeliculas = len(resp)
    return cantidadDePeliculas

def ver_formatos():
    c.execute(salas)
    resp = c.fetchall()
    for i in resp:
        print(i[0],i[1])

def devolverCantidadDeButacas():

    c.execute(salas)
    resp = c.fetchall()
    butacasDeSala1 = resp[0][2]
    butacasDeSala2 = resp[1][2]
    butacasDeSala3 = resp[2][2]
    return butacasDeSala1,butacasDeSala2,butacasDeSala3


opcion = 1
butacasDeSala1, butacasDeSala2, butacasDeSala3 = devolverCantidadDeButacas()
while opcion != 5:
    opcionesDeCompras = []
    print()
    opcionesDeBienvenida()
    print()
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        ver_carteleras()
    elif opcion == "2":
        ver_formatos()
    elif opcion == "3":
        cantidadDePelis = ver_carteleras()
        opcion1 = input("Seleccione una opción de pelicula ")
        if int(opcion1) > 0 and int(opcion1) <= cantidadDePelis:
            opcionesDeCompras.append(opcion1)
            cantidadDeSalas = ver_formatos()
            SalaSeleccionada = input("Seleccione una sala: ")
            if int(SalaSeleccionada) > 0 and int(SalaSeleccionada) <= 3:
                opcionesDeCompras.append(SalaSeleccionada)
                if SalaSeleccionada == "1":
                    print("Butacas Disponible de la Sala 1 es: ",butacasDeSala1)
                    cantidadDeEntradas = input("Cuantas Entradas desea comprar?: ")
                    butacasDeSala1 = butacasDeSala1 - int(cantidadDeEntradas)
                    opcionesDeCompras.append(butacasDeSala1)
                if SalaSeleccionada == "2":
                    print("Butacas Disponible de la Sala 2 es: ", butacasDeSala2)
                    cantidadDeEntradas = input("Cuantas Entradas desea comprar?: ")
                    butacasDeSala2 = butacasDeSala2 - int(cantidadDeEntradas)
                    opcionesDeCompras.append(butacasDeSala2)
                if SalaSeleccionada == "3":
                    print("Butacas Disponible de la Sala 3 es: ",butacasDeSala3)
                    cantidadDeEntradas = input("Cuantas Entradas desea comprar?: ")
                    if (int(cantidadDeEntradas)<=butacasDeSala3):
                        butacasDeSala3 = butacasDeSala3 - int(cantidadDeEntradas)
                        opcionesDeCompras.append(butacasDeSala3)
                    else:
                        print("No hay capacidad")


        else:
            continue
        print(opcionesDeCompras)
        c.execute("INSERT INTO FUNCIONES (ID_PELICULAS, ID_SALAS, BUTACAS_LIBRES, FECHA_HORA) VALUES ({},{},{},{});".format(opcionesDeCompras[0],opcionesDeCompras[1],opcionesDeCompras[2],"20170303"))
        base.commit()
    elif opcion == "5":
        break
    else:
        print("no ingreso ninguna opción")


