import json
import connexion
import psycopg2
import requests
import time

def verDocencia():
    ### Esto mostrará por pantalla las docencias disponibles para el profesor.
    response = requests.get('http://localhost:8081/DepartamentoProfesores/mostrarDocencia?id_profesor=6')

    print("\nLas asignaturas asignadas a usted son las siguientes,:")
    json_data = json.loads(response.text)
    for i in range(len(json_data)):
        stri = json_data[i]
        response2 = requests.get('http://localhost:8080/Facultad/Gradoasignatura/'+str(stri['id_gradoAsignatura']))
        json_data2 = json.loads(response2.text)
        print("La asignatura con id gradoAsignatura: "+ str(stri['id_gradoAsignatura'])+"  "+str(json_data2["nombreAsignatura"])+"  "+str(json_data2["nombreGrado"]))
    n=input("Introduzca la opción que desea, pulse 0 para salir: ")
    while int(n)!=0:
            print("\nHa elegido usted acceder a sus asignaturas, por favor espere...")
            entrarEnAsingnatura(int(n))
    print("Saliendo de ver docencias...")
    print("\n")
    mostrarMiniMenu()






def entrarEnAsingnatura(id_gradoAsignatura):
    ###Esta función sacará todas las matrículas con ese id de grado_asignatura
    response = requests.get('http://localhost:8084/secretaria-alumnos/getMatriculaidAsignatura?idgradoAsignatura='+str(id_gradoAsignatura))
    response2 = requests.get('http://localhost:8080/Facultad/Gradoasignatura/'+str(id_gradoAsignatura))
    json_data = json.loads(response.text)
    json_data2 = json.loads(response2.text)
    print("\nLos alumnos que están matrículados son los siguientes:")
    for i in range(len(json_data)):
        stri= json_data[i]
        print(str(i+1)+"."+str(stri["NombreAlumno"]+" con DNI: "+str(stri["DNI"]+" e id de matrícula: "+str(stri["idMatricula"])+".")))
    ponerNota(input("\nIntroduzca la matrícula que desea puntuar, o pulse 0 para salir "))
    n=input("\n¿Que desea hacer ahora? Pulse 0 para salir o 9 para volver a la lista de alumnos: ")
    n=int(n)
    while n!=9 or n!=0:
        if(n==9):
            entrarEnAsingnatura(id_gradoAsignatura)
        if (n==0):
            print("Saliendo del sistema.")
            time.sleep(1)
            exit()
            entrarEnAsingnatura(id_gradoAsignatura)
        n=input("\n¿Que desea hacer ahora? Pulse 0 para salir o 9 para volver a la lista de alumnos: ")
        n=int(n)
    

def ponerNota(idMatriculacion):
    if int(idMatriculacion)!=0:
        nota= input("\nIntroduzca la nota que quiere poner a la matrícula con id "+ str(idMatriculacion)+": ")
        headers = { 
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        data = { 
            "idGradoAsignatura": 1, 
            "idMatricula": int(idMatriculacion), 
            "nota": float(nota)
        }
        response = requests.post('http://localhost:8084/secretaria-alumnos/Notas', headers=headers, data=json.dumps(data))
        print(str(response.content))
    else:
        print("Saliendo del sistema.")
        time.sleep(1)
        exit()


def mostrarMenu():
    for i in range(5):
        print("\n")
    print("\t \t Bienvenido al menu de profesor:")
    for i in range(3):
        print("\n")
    print("Se ha logeado usted como Flavius")
    mostrarMiniMenu()

def mostrarMiniMenu():
    print("Estas son las opciones de las que dispone:")
    print("Pulse 1 para ver sus asignaturas")
    print("Pulse 0 para salir del sistema")


##ponerNota(1)

mostrarMenu()
n=input("Introduzca la opción que desea: ")
while int(n)!=0:
    if int(n)==1:
        print("Ha elegido usted ver sus asignaturas, conectando con el servidor, por favor espere...")
        verDocencia()
        n=input("Introduzca la opción que desea: ")
print("Saliendo del sistema.")
time.sleep(1)
