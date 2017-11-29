import sqlite3
base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()


funciones = """SELECT  FUNCIONES.ID, SALAS.FORMATO, PELICULAS.NOMBRE, BUTACAS_LIBRES, FECHA_HORA FROM FUNCIONES
               INNER JOIN PELICULAS ON FUNCIONES.ID_PELICULAS = PELICULAS.ID
               INNER JOIN SALAS ON SALAS.ID = ID_SALAS;"""

def mostrarFunciones():
    c.execute(funciones)
    resp = c.fetchall()

    for x, i in enumerate(resp):

        print(x+1, "Pelicula: ",i[2], "Formato: ", i[1], "Butacas libres: ", i[3], "Fecha: ", i[4])
