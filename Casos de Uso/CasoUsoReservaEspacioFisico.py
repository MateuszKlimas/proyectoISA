import json
import connexion
import psycopg2
import requests
import time
import random


def verMediosFisicos():
    ### Esto mostrará por pantalla las facultades existentes en la base de datos.
    id_facultad = input("Introduzca el ID de la facultad donde quiere hacer la reserva: ")

    response = requests.get('http://localhost:8082/Facultad/MedioFisico/' + id_facultad)

    print("\nLos medios fisicos de esta facultad son los siguientes:")
    json_data = json.loads(response.text)

    for i in range(len(json_data)):
        stri = json_data[i]
        print("ID Medio -> " + str(stri['id_medio']) + " Nombre -> " + str(stri['nombreMedioFisico']) + " Tipo -> " + str(stri['tipoMedioFisico']) + " Precio -> " + str(stri['precioMedioFisico']) + " Capacidad -> " + str(stri['capacidadMedioFisico']))
    n = input("Introduzca el ID del medio que desea reservar: ")

    print("\nAccediendo...\n")
    reservaMedioFisico(n)

    print("Exit")
    print("\n")
    mostrarMiniMenu()


def reservaMedioFisico(idMedio):
    ###Esta función añadirá una nueva reserva con los datos que se introduzcan.

    if int(idMedio) != 0:
        nombre = input("Introduzca su nombre como titular de la reserva: ")
        horaInicio = input("Introduzca la hora de inicio de la reserva (formato hh:mm): ")
        horaFin = input("Introduzca la hora de fin de la reserva (formato hh:mm): ")
        fecha = input("Introduzca la fecha de la reserva (formato dd/mm/aaaa): ")
        res = random.randint(1000,2000)

        headers = { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        data = { 
            "id_reserva": int(res),
            "titular_reserva": str(nombre), 
            "hora_inicio": str(horaInicio),
            "hora_fin": str(horaFin),
            "fecha_reserva": str(fecha),
            "id_medio": int(idMedio)
        }
        response = requests.post('http://localhost:8082/Facultad/Reserva', headers=headers, data=json.dumps(data))
        print(str(response.content))
    else:
        print("Error, saliendo del sistema")
        time.sleep(1)
        exit()
    

def mostrarMenu():

    for i in range(5):
        print("\n")
    print("\t \t ----------------------------------")
    print("\t \t Menu de reserva de medios físicos:")
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
        verMediosFisicos()
        n = input("Introduzca la opción que desea: ")
print("Saliendo del sistema.")
time.sleep(1)