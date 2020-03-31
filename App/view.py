"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 6")
    print("1- Cargar información")
    print("2- Consultar accidentes, por ciudad, en un rango de fechas")


    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input('Seleccione una opción para continuar\n')
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            print("Recursion Limit:",sys.getrecursionlimit())
            catalog = initCatalog ()
            loadData (catalog)
            #print ('Tamaño Lista libros cargados: ' + str(lt.size(catalog['booksList'])))
            #print ('Tamaño árbol Libros por titulo: ' + str(map.size(catalog['booksTitleTree'])))
            print ('Tamaño árbol accidentes por fecha : ' + str(map.size(catalog['dateTree'])))
            #print ('Altura árbol por titulo: ' + str(map.height(catalog['booksTitleTree'])))
            print ('Altura árbol por fecha: ' + str(map.height(catalog['dateTree'])))
        elif int(inputs[0])==2:
            dates = input("Ingrese los las fechas desde y hasta (YYYY-MM-DD YYYY-MM-DD):")
            counter = controller.getAccidentsByDateRange(catalog, dates) 
            if counter:
                print("Cantidad de accidentes entre las fechas por ciudad",dates,":\n",counter)
            else:
                print("No se encontraron accidentes para el rango de fechas",dates) 
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    #sys.setrecursionlimit(11000)
    main()