import sqlite3
import os
base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

peliculas = "SELECT * FROM PELICULAS;"



def ver_carteleras():
    """
    imprime la cartelera de peliculas
    """
    os.system('clear')
    c.execute(peliculas)
    resp = c.fetchall()
    for i in resp:
        print(i)
    cantidadDePeliculas = len(resp)
    return cantidadDePeliculas