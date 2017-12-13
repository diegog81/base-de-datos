import sqlite3

#cambio para probar git
base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

salas = "SELECT * FROM SALAS;"


def devolverCantidadDeButacas():
    """
    devuelve la cantidad de butacas de cada sala.
    """

    c.execute(salas)
    resp = c.fetchall()
    butacasDeSala1 = resp[0][2]
    butacasDeSala2 = resp[1][2]
    butacasDeSala3 = resp[2][2]
    return butacasDeSala1,butacasDeSala2,butacasDeSala3
