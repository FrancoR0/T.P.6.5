"""
1) Hacer un programa que gestiones datos para una escuela. El programa tiene que ser capaz
de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, Apellido,
fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las notas, cantidad de
faltas, cantidad de amonestaciones recibidas.
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos
f) Dar Persistencia a los Datos del programa mediante la implementación Archivos
"""
lista_de_alumnos = {}

def agregar(lista_de_alumnos, nombre, apellido, fecha_de_nacimineto, dni, tutor, notas, faltas, amonestaciones):
        lista_de_alumnos[dni] = nombre
        lista_de_alumnos[apellido] = fecha_de_nacimineto
        lista_de_alumnos[tutor] = notas
        lista_de_alumnos[faltas] = amonestaciones
while True:
    opcion = input("\na) Agregar nuevo alumno o modificar " \
    "\nb) Mostar los alumnos " \
    "\nc) Expulsar ")
    if opcion == "a" or opcion == "A": #agregar o modificar
        dni = int(input("numero de DNI: "))
        if dni in lista_de_alumnos:
             modificar = input("¿que decua modificar?"
                               "\na) nombre"
                               "\nb)apellido "
                               "\nc)tutor "
                               "\nd)notas "
                               "\ne)faltas" 
                               "\nf)amonestaciones")
             if modificar == "a" or modificar == "A":
                  nombre = input("nombre: ")
                  agregar(lista_de_alumnos, nombre)
                  print("se a modificado con exito")
             elif modificar == "b" or modificar == "B":
                  apellido = int(input("apellido: "))
                  agregar(lista_de_alumnos, apellido)
                  print("se a modificado con exito")
             elif modificar == "c" or modificar == "C":
                  tutor = input("nombre de tutor: ")
                  agregar(lista_de_alumnos, tutor)
                  print("se a modificado con exito")
             elif modificar == "d" or modificar == "D":
                  notas = input("agregar nueva nota: ")
                  agregar(lista_de_alumnos, notas)
                  print("se a modificado con exito")
             elif modificar == "e" or modificar == "E":
                  faltas = int(input("faltas: "))
                  agregar(lista_de_alumnos, faltas)
                  print("se a modificado con exito")
             elif modificar == "f" or modificar == "F":
                  amonestaciones = int(input("numero de amonestaciones: "))
                  agregar(lista_de_alumnos, amonestaciones)
                  print("se a modificado con exito")
        else:
             nombre = input("nombre: ")
             apellido = input("apellido: ")
             fecha_de_nacimineto = input("fecha de nacimiento: ")        
             tutor = input("nombre de tutor: ")
             notas = input("agregar nueva nota: ")
             faltas = int(input("faltas: "))
             amonestaciones = int(input("numero de amonestaciones: "))
             agregar(lista_de_alumnos, nombre, apellido, fecha_de_nacimineto, dni, tutor, notas, faltas, amonestaciones)
             print("se a ingresado correctamente")
    elif opcion == "b" or opcion == "B": #lista
        print(lista_de_alumnos)

    elif opcion == "c" or opcion == "C": #expulsar
        dni = input("dni del alumno expulsado: ")
        lista_de_alumnos.pop(dni)
        print("el alumno fue expulsado")
    else:
        print("opcion no valida")
