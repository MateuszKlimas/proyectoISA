import json
import connexion
import psycopg2
import requests

def verDocencia():
    ### Esto mostrará por pantalla las docencias disponibles para el profesor.
    print("Hola")






def entrarEnAsingnatura(id_gradoAsignatura):
    ###Esta función sacará todas las matrículas con ese id de grado_asignatura




    print("Hola")

    ####EN ESTE METODO LLAMO A QUE ME DEVUELVA TODAS LAS MATRÍCULAS CON SU NOMBRE

def ponerNota(idMatriculacion):
    nota= input("Introduzca la nota que quiere poner a la matrícula con id "+ str(idMatriculacion)+": ")
    headers = { 
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    data = { 
        "idGradoAsignatura": 1, 
        "idMatricula": 2, 
        "nota": 3
    }
    response = requests.post('http://localhost:8080/secretaria-alumnos/Notas', headers=headers, data=json.dumps(data))
    print(str(response.content))
    ###Hago la request para ponerle la nota.

ponerNota(1)