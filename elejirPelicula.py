import sqlite3

base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

peliculas = "SELECT * FROM PELICULAS;"



def ver_carteleras():
    c.execute(peliculas)
    resp = c.fetchall()
    cantidadDePeliculas = len(resp)
    return cantidadDePeliculas

def elejirPelicula(opcion):
    """
    devuelve una opcion de la lista de peliculas, valida.

    """
    menu =  ver_carteleras()
    while menu !=0:
        try:
            opcion = int(input("Seleccione pelicula"))
        except:
            continue
        if int(opcion) > 0 and int(opcion) <= (menu):
            return opcion
        else:
            continue

