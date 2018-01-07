import json
import connexion
import psycopg2
import requests

def verDocencia():
    ### Esto mostrará por pantalla las docencias disponibles para el profesor.
    response = requests.get('http://localhost:8080/DepartamentoProfesores/mostrarDocencia?id_profesor=1')

    print("Las asignaturas asignadas a usted son las siguientes,:")
    json_data = json.loads(response.text)
    for i in range(len(json_data)):
        stri = json_data[i]
        print("La asignatura con id gradoAsignatura: "+ str(stri['id_gradoAsignatura']))
    entrarEnAsingnatura(input("Introduzca la asignatura en la que quiere acceder: "))






def entrarEnAsingnatura(id_gradoAsignatura):
    ###Esta función sacará todas las matrículas con ese id de grado_asignatura
    response = requests.get('http://localhost:8081/secretaria-alumnos/getMatriculaidAsignatura?idgradoAsignatura='+str(id_gradoAsignatura))
    json_data = json.loads(response.text)
    print("Los alumnos que están matrículados son los siguientes:")
    for i in range(len(json_data)):
        stri= json_data[i]
        print(str(i+1)+"."+str(stri["NombreAlumno"]+"con DNI: "+str(stri["DNI"]+"e id de matrícula: "+str(stri["idMatricula"])+".")))
    ponerNota(input("Introduzca la matrícula que desea puntuar: "))
    

def ponerNota(idMatriculacion):
    nota= input("Introduzca la nota que quiere poner a la matrícula con id "+ str(idMatriculacion)+": ")
    headers = { 
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    data = { 
        "idGradoAsignatura": 1, 
        "idMatricula": int(idMatriculacion), 
        "nota": float(nota)
    }
    response = requests.post('http://localhost:8081/secretaria-alumnos/Notas', headers=headers, data=json.dumps(data))
    print(str(response.content))
    ###Hago la request para ponerle la nota.

##ponerNota(1)
verDocencia()