import json
import connexion
import psycopg2
import requests
import time

def casoUso():
    print("\n\n\n\n\n\n")
    n = input("\t\tPor favor, inserte su ID de alumno para ver las asignaturas disponibles para matricularse: ")
    print("\n\n\n")
    response = requests.get('http://localhost:8081/secretaria-alumnos/asignaturasdisponibles?id_alumno=' + n)

    json_data = json.loads(response.text)
    print("\t\t************************************\n")
    for i in range(len(json_data)):
        json1 = json_data[i]
        print("\t\tNombre de la asignatura: " + json1["nombreAsignatura"])
        print("\t\tTipo de asignatura: " + json1["tipoAsignatura"])
        print("\t\tCreditos de la asignatura: " + str(json1["creditosGrado"]))
        print("\t\tDescripcion de la asignatura: " + json1["descripcionAsignatura"])
        print("\n \t\t************************************ \n")
casoUso()