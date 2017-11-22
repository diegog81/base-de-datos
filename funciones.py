
import sqlite3
import cartelera
import formatos
import butacasDeFunciones
import elejirPelicula
import elejirFormato

base = sqlite3.connect('D:\Sqlite\cine.db')
c = base.cursor()


def fuinciones():
    butacasDeSala1, butacasDeSala2, butacasDeSala3 = butacasDeFunciones.devolverCantidadDeButacas()
    opcionesDeCompras = []
    cantidadDePelis = cartelera.ver_carteleras()
    opcion1 =0

    #Se elije pelicula y se agrega a la lista
    opcionesDeCompras.append(elejirPelicula.elejirPelicula(opcion1))

    #se imprime los formatos para despues elejir uno.
    formatos.ver_formatos()

    #Se elige formato y se agrega a la lista
    SalaSeleccionada = elejirFormato.elejirFormato()
    opcionesDeCompras.append(SalaSeleccionada)

    #Dependiendo el fromato(SALA) elegido se agrega las butacas de la misma a la lista
    if SalaSeleccionada == 1:
        opcionesDeCompras.append(butacasDeSala1)
    if SalaSeleccionada == 2:
        opcionesDeCompras.append(butacasDeSala2)
    if SalaSeleccionada == 3:
        opcionesDeCompras.append(butacasDeSala3)


    return opcionesDeCompras