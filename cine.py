import sqlite3
import cartelera
import formatos
import funciones
import mostrarFunciones
import comprarEntradas

base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()

peliculas = "SELECT * FROM PELICULAS;"
salas = "SELECT * FROM SALAS;"


def opcionesDeBienvenida():
    print("Bienvenido a CINE DB")
    print()
    print("Elegir Opción: ")
    print("1- Ver Carteleras")
    print("2- Ver Formatos")
    print("3- Crear función")
    print("4- Ver Funciones")
    print("5- Comprar Entradas")
    print("6- Salir")

def cine():
    opcion = 1
    while opcion != 5:
        print()
        opcionesDeBienvenida()
        print()
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            cartelera.ver_carteleras()
        elif opcion == "2":
            formatos.ver_formatos()
        elif opcion == "3":
            opcionesDeCompras = funciones.fuinciones()
            c.execute("INSERT INTO FUNCIONES (ID_PELICULAS, ID_SALAS, BUTACAS_LIBRES, FECHA_HORA) VALUES ({},{},{},{});".format(opcionesDeCompras[0],opcionesDeCompras[1],opcionesDeCompras[2],"20170303"))
            base.commit()
        elif opcion == "4":
            mostrarFunciones.mostrarFunciones()
        elif opcion == "5":

            comprarEntradas.comprarEntradas()
        elif opcion == "6":
            break
        else:
            print("no ingreso ninguna opción")


cine()