#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pprint

def parsear_fichero_formacion(rutaFichero):
    """Parsea el fichero de formación en formato texto y genera el clp 
    """

    # Intentamos abrir el fichero
    try:
        fichero = open(rutaFichero, "r")    
    except IOError:
        return ""

    # Lista con la cantidad de fichas permitidas de cada tipo
    fichasPermitidas = {
        1:1,
        2:8,
        3:2,
        4:2,
        5:2,
        6:1    
    }

    # Creamos el contenedor para las fichas
    fichas = {}

    # Inicializamos las listas vacías en el contenedor de fichas
    for q in range(1,7):
        fichas[q] = []

    # Creamos una matriz de posiciones ocupadas, inicialmente toda a cero
    posicionesOcupadas = [[0 for y in range(1,3)] for x in range(1, 9)]

    # Diseñamos la expresión regular para leer el fichero
    expReg = re.compile (r"^([1-6]):([1-8]),([1-2])$")

    # Por cada línea del fichero
    for linea in fichero.readlines():

        # Quitamos los espacios en blanco y retornos de carro
        linea = linea.rstrip().replace(" ", "")

        # Comprobamos que la línea se ajuste a la regexp
        m = expReg.match(linea)
        if m:
            # Leemos los datos de la expresión regular
            ficha = int(m.group(1))
            x = int(m.group(2))
            y = int(m.group(3))

            # Si en la posición indicada no había una ficha previamente definida
            # y todavía es posible añadir fichas de ese tipo
            if (posicionesOcupadas[x-1][y-1] == 0 and
                len(fichas[ficha]) < fichasPermitidas[ficha]):
                
                # Añadimos la ficha al conjunto
                fichas[ficha].append((x,y))

                # Marcamos la posición como ocupada
                posicionesOcupadas[x-1][y-1] = 1


    # Una vez leído el fichero, vamos a comprobar si faltan fichas por añadir
    # Vamos iterando por cada tipo de ficha, mirando si el usuario ha definido
    # el número correcto de ellas.
    for ficha in fichas.keys():
        print "Comprobando fichas del tipo", ficha
        
        # Si faltan fichas del tipo concreto
        if len(fichas[ficha]) < fichasPermitidas[ficha]:
            
            # Miramos cuántas fichas faltan
            cantidad_faltante = fichasPermitidas[ficha] - len(fichas[ficha])
            print " Faltan", cantidad_faltante, "fichas de este tipo"
            
            for f in range(cantidad_faltante):
                posicion_libre = buscar_posicion_libre(posicionesOcupadas)
                posicionesOcupadas[posicion_libre[0] - 1][posicion_libre[1] - 1] = 1
                fichas[ficha].append(posicion_libre)
                print "  Añadiendo una ficha en la posición", posicion_libre
            
        # En teoría esto es imposible que pase
        #
        # elif len(fichas[ficha]) > fichasPermitidas[ficha]:
        #     pprint.pprint(fichas)
        #     del fichas[ficha][fichasPermitidas[ficha]:]
        #     pprint.pprint(fichas)
        
        else:
            print " El número de fichas del tipo", ficha, "es correcto"

        print 
    

    # El último paso es convertir el hash de fichas en una matriz
    matrizFinal = [[0,0] for p in range(8)]

    for f in fichas.keys():
        for coord in fichas[f]:
            cx = coord[0] - 1
            cy = coord[1] - 1

            matrizFinal[cx][cy] = f

    return matrizFinal

def buscar_posicion_libre(posicionesOcupadas):
    for i, col in enumerate(posicionesOcupadas):
        if posicionesOcupadas[i][0] == 0:
            return (i+1,1)
        elif posicionesOcupadas[i][1] == 0:
            return (i+1, 2)
        
def main():
    datos = parsear_fichero_formacion("formacionEquipo")
    
if __name__ == '__main__':
    main()
