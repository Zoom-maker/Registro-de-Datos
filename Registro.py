#----------------------------- NOTAS:

# Para el Char by CHar investigar el modulo split de python
# Usar - len(Datos) - para el tamaño de la lista en numero
# Path.seek(32) - Para leer el archivo a partir de que byte, de 8 en 8, cada 8 bytes una linea

#----------------------------- MODULOS:

import sys
import os
import os.path as path
import re


#-----------------------------  INSTRUCCIONES:
# V1:
# Solo capturar
# Cedula: 546546
# Nombres: 4646
# Edad: 564
# Grabar? Y/N

# V2:
# v1 + Listado + Busqueda (Cedula)


#----------------------------- FUNCIONES:

def Agrupar(cedula, name, age):
    
    Datos.append('\n' + str(cedula) + ", ")
    Datos.append(str(name) + ", ")
    Datos.append(str(age)) 

    return Escribir(Datos)

def Escribir(list = []):
     
    Path = open(File, "a+")
    for x in range(len(Datos)):

        Path.write(Datos[x])

    Path.close()


#----------------------------- 

args,(File)= sys.argv                                   # Obtener nombre del archivo por la linea de comando
File = ("/Users/Dell/Desktop/" + File + ".txt")         # Indica la ruta y el nombre del archivo que se creará

Path = open(File, "a") #Abro el archivo. La 'w' indica que es para escribir, osea "Write".
Path.close() # Verificar si elimino esta parte 
Path = open(File, "r") # Verificar si se puede escribir open(File, "ar")
content = Path.read()

if content == '':

    Path = open(File, "w")
    Path.write("Cedula ---- Nombre -- Edad")
    Path.close()


#----------------------------- 
 
Opt = int(input("(1) Capturar" + '\n' + "(2) Listar " + '\n' + "(3) Busqueda" + '\n'))

#----------------------------- CAPTURAR:
if Opt == 1:

    while True:

        cedula = int(input("Ingrese la Cedula: "))
        print()
        name = str(input("Introduce tu nombre: ")) 
        print()
        age = int(input("Ingresa tu edad: "))
        print()

        Datos = []              # Esta es una lista

        choise = input("Deseas guardar los datos? (y/n): ")

    #----------------------------- CONDICIONES:

        if choise == 'y':
    
            Agrupar(cedula, name, age)

            print("Datos guardados!")


        elif choise == 'n':

            print("Datos no guardados!")

        else: 
            print("Respuesta no aceptada")

        Continue = input("Desea Agregar mas datos? (y/n): ")

        if Continue == 'n':

            Path.close()
            break
#----------------------------- LISTAR:

elif Opt == 2: 
    
    Listado = open(File, "r")
    
    for lines in Listado:
       
        print(lines)

    Listado.close()


#----------------------------- BUSQUEDA:

elif Opt == 3:

    ced = str(input("Ingrese la cedula que se va a buscar: "))

    Listado = open(File, "r")

    comp = r'' + ced

    for line in Listado:

        find = re.findall(comp, line)
        result = "".join(find)

        if result == ced:

            print(line)