import sqlite3

base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

salas = "SELECT * FROM SALAS;"

def ver_formatos():
    """
    muuestra los formtas de las salas
    """
    c.execute(salas)
    resp = c.fetchall()
    for i in resp:
        print(i[0],i[1])
