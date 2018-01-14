import json
import connexion
import psycopg2
import requests
import time
import random


def verAulas():
    ### Esto mostrará por pantalla las facultades existentes en la base de datos.
    num_alumnos = input("Introduzca el numero de alumnos del que dispone: ")

    response = requests.get('http://localhost:8082/Facultad/MedioFisicoAulas/' + num_alumnos)

    print("\nLas aulas disponibles para ese numero de alumnos son las siguientes: ")
    json_data = json.loads(response.text)

    for i in range(len(json_data)):
        stri = json_data[i]
        print("ID Aula -> " + str(stri['id_medio']) + " Nombre -> " + str(stri['nombreMedioFisico']) + " Precio -> " + str(stri['precioMedioFisico']) + " Capacidad -> " + str(stri['capacidadMedioFisico']) + " Centro -> " + str(stri['id_centro']))
    n = input("Introduzca el ID del aula para la asignacion: ")

    print("\nAccediendo...\n")
    reservaAula(n)

    print("Exit")
    print("\n")
    mostrarMiniMenu()


def reservaAula(idMedio):
    ###Esta función añadirá una nueva reserva con los datos que se introduzcan.

    if int(idMedio) != 0:
        nombre = input("Introduzca su nombre para la asignacion de aula: ")
        asig = random.randint(1000,2000)

        headers = { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        data = { 
            "id_reserva": int(asig), 
            "titular_reserva": str(nombre), 
            "id_medio": int(idMedio)
        }
        response = requests.post('http://localhost:8082/Facultad/reserva', headers=headers, data=json.dumps(data))
        print(str(response.content))
    else:
        print("Error, saliendo del sistema")
        time.sleep(1)
        exit()
    

def mostrarMenu():

    for i in range(5):
        print("\n")
    print("\t \t ----------------------------------")
    print("\t \t Menu de asignacion de aulas:")
    print("\t \t ----------------------------------")

    for i in range(3):
        print("\n")
    mostrarMiniMenu()

def mostrarMiniMenu():
    print("Pulse 1 para continuar")
    print("Pulse 0 para salir del sistema")



mostrarMenu()
n = input("Introduzca la opción que desea: ")
while int(n) != 0:
    if int(n) == 1:
        verAulas()
        n = input("Introduzca la opción que desea: ")
print("Saliendo del sistema.")
time.sleep(1)