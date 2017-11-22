import sqlite3
base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

peliculas = "SELECT * FROM PELICULAS;"
salas = "SELECT * FROM SALAS;"
funciones = """SELECT  SALAS.FORMATO, PELICULAS.NOMBRE, BUTACAS_LIBRES, FECHA_HORA FROM FUNCIONES
               INNER JOIN PELICULAS ON FUNCIONES.ID_PELICULAS = PELICULAS.ID
               INNER JOIN SALAS ON SALAS.ID = ID_SALAS;"""

def mostrarFunciones():
    c.execute(funciones)
    resp = c.fetchall()
    for i in resp:
        print(i)

mostrarFunciones()