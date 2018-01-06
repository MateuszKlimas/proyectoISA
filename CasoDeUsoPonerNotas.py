import json
import connexion
import psycopg2

def verDocencia():
    ### Esto mostrará por pantalla las docencias disponibles para el profesor.
    print("Hola")






def entrarEnAsingnatura(id_gradoAsignatura):
    ###Esta función sacará todas las matrículas con ese id de grado_asignatura
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    print ("Connecting to database\n")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query = "SELECT \"id_alumno\" FROM MATRICULACION WHERE \"id_gradoAsignatura\"="+str(id_gradoAsignatura)+";"
    cursor.execute(query)
	# retrieve the records from the database
    records = cursor.fetchall()
    for row in range(cursor.rowcount):


