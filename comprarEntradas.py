import sqlite3
import mostrarFunciones

base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()


funciones = """SELECT  FUNCIONES.ID, SALAS.FORMATO, PELICULAS.NOMBRE, BUTACAS_LIBRES, FECHA_HORA FROM FUNCIONES
               INNER JOIN PELICULAS ON FUNCIONES.ID_PELICULAS = PELICULAS.ID
               INNER JOIN SALAS ON SALAS.ID = ID_SALAS;"""

def modificarTablaFuncionesButacasLibres(butacasLibres,idFunciones):
    c.execute("UPDATE FUNCIONES SET BUTACAS_LIBRES = "+str(butacasLibres)+" WHERE ID ="+str(idFunciones)+" ;")
    base.commit()

def ingresarDatosATablaEntradas(idFunciones,cantidadEntradas):
    c.execute("INSERT INTO ENTRADAS (ID_FUNCION, CANTIDAD) VALUES( " + str(idFunciones) + " , " + str(cantidadEntradas) + " );")
    base.commit()

def mostrarFuncioness():
    c.execute(funciones)
    resp = c.fetchall()
    listaEntradas = []
    for x, i in enumerate(resp):
        listaAux = []
        listaAux.append(x+1)
        listaAux.append(i)
        listaEntradas.append(listaAux)

    return listaEntradas

def limiteButacas(butacasLibres):
    disponible = 1
    while disponible != 0:
        try:
            cantidadDeEntradas = int(input("Cuantas entradas?\nDisponibles: " + str(butacasLibres)))
        except:
            print("Ingreso una opcion invalida")
            disponible = 1
            continue
        if cantidadDeEntradas <= butacasLibres and cantidadDeEntradas > 0:

            return cantidadDeEntradas
        else:
            print("Supera la cantidad de butacas disponibles")

def limiteFunciones(menu):
    if menu == []:
        return "a"
    disponible = 1
    while disponible != 0:
        try:
            eleccion = int(input("Elija funcion: "))
        except:
            print("ingreso una opcion invalida")
            disponible = 1
            continue
        for x in range(len(menu)):
            if menu[x][0] == eleccion:
                return eleccion
        print("Opcion elejida no existe")
        disponible = 1


def comprarEntradas():
    mostrarFunciones.mostrarFunciones()

    menu = mostrarFuncioness()

    eleciion = limiteFunciones(menu)
    if eleciion != "a":

        idFunciones = menu[eleciion-1][1][0]

        butacasLibre = menu[eleciion-1][1][3]

        #se elige cantidad de entradas que no superen las buracas libres
        cantidadDeEntradas = limiteButacas(butacasLibre)

        butacasLibre -= cantidadDeEntradas

        modificarTablaFuncionesButacasLibres(butacasLibre,idFunciones)


        ingresarDatosATablaEntradas(idFunciones,cantidadDeEntradas)




