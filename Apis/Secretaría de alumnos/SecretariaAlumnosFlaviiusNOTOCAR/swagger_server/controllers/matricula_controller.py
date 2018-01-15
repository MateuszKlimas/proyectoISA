import connexion
import psycopg2 
import json
import pprint
from swagger_server.models.asignatura_matricula import AsignaturaMatricula
from swagger_server.models.matricula_asignatura import MatriculaAsignatura
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def cambiar_matricula(id_usuario, datos=None):
    """
    Cambios en matricula
    Permite la modificacion de los datos de la matricula
    :param id_usuario: id del usuario
    :type id_usuario: str
    :param datos: 
    :type datos: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        datos = AsignaturaMatricula.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_matriculas(idgradoAsignatura):
    jsons = []
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
	    # print the connection string we will use to connect
    print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
        # execute our Query
    query = "SELECT id_matriculacion,\"notaAlumno\",(SELECT \"nombreAlumno\" FROM alumno WHERE id_alumno=matriculacion.id_alumno) as nombre,(SELECT \"dniAlumno\" FROM alumno WHERE id_alumno=matriculacion.id_alumno) as dni FROM matriculacion WHERE \"id_gradoAsignatura\"="+str(idgradoAsignatura)+";"
    cursor.execute(query)
    records = cursor.fetchall()
    for row in range(cursor.rowcount):
        json1 = {
        "idMatricula" : records[row][0],
        "NombreAlumno" : records[row][2],
        "DNI" : records[row][3],
        "notas" : records[row][1]
        }
        jsons.append(json1)
    conn.close()
    return jsons


def poner_nota(matriculaAsignatura):
    """
    Pone la nota a un alumno con el id de matrícula
    Puntúa al alumno con la nota correspondiente
    :param matriculaAsignatura: objeto que consta de idMatricula,idGradoAsignatura y nota a poner
    :type matriculaAsignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matriculaAsignatura = MatriculaAsignatura.from_dict(connexion.request.get_json())
        conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
	    # print the connection string we will use to connect
        print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        # execute our Query
        query = "UPDATE matriculacion SET \"notaAlumno\"="+str(matriculaAsignatura.nota)+"WHERE id_matriculacion="+str(matriculaAsignatura.id_matricula)+";"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return 'InserccionCorrecta'
    


def realizar_automatricula(id_usuario, asignaturas=None):
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    """
    Automatricula
    Permite a un alumno realizar su automatricula
    :param id_usuario: nombre del usuario
    :type id_usuario: str
    :param asignaturas: 
    :type asignaturas: list | bytes

    :rtype: None
    """
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
 
	# execute our Query
    for i in asignaturas:
        #Hay que eliminar el id de alumno del array de asignaturas
        cursor.execute("INSERT INTO matriculacion VALUES (" + str(i['id_matriculacion']) + "," + str(i['numero_convocatoria']) + "," + str(i['numero_convocatoria']) + 
        "," + str(i['nota']) + "," + str(i['aprobado']) + "," + str(id_usuario) + "," + str(i['codigo_asignatura']) + ")")
    cursor.execute("SELECT * from matriculacion")
    records = json.dumps(cursor.fetchall())
    conn.commit()
    return records
