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
        #print(x+1, "Pelicula: ",i[1], "Formato: ", i[0], "Butacas libres: ", i[2], "Fecha: ", i[3])
        listaAux.append(x+1)
        listaAux.append(i)
        listaEntradas.append(listaAux)

    #print(listaEntradas[3][1][0])
    return listaEntradas


def comprarEntradas():
    mostrarFunciones.mostrarFunciones()
    eleciion = int(input("Elija una Funcion: "))
    menu = mostrarFuncioness()
    #print(menu)
    idFunciones = menu[eleciion-1][1][0]
    butacasLibre = menu[eleciion-1][1][3]
    #print(idFunciones)
    #print(butacasLibre)
    cantidadDeEntradas = int(input("Cuantas entradas?\nDisponibles: " + str(butacasLibre)))
    butacasLibre -= cantidadDeEntradas
    modificarTablaFuncionesButacasLibres(butacasLibre,idFunciones)
    print(butacasLibre)
    ingresarDatosATablaEntradas(idFunciones,cantidadDeEntradas)




