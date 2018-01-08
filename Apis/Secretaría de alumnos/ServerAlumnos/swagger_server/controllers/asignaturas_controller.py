import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.creditos import Creditos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import psycopg2
import json
import requests

def consultar_creditos_asignatura(nombre_asignatura):
	"""
	creditos de cada asignatura
	Permite consultar cuantos creditos tiene cada asigntura
	:param nombre_asignatura: nombre de la asignatura buscada
	:type nombre_asignatura: str

	:rtype: Creditos
	"""
	return 'do some magic!'


def get_asignaturas_disponibles(id_alumno):
	"""
	Asignaturas disponibles para matricular
	Devuelve una lista con las asignaturas en las que puede matricularse un alumno
	:param id_alumno: id del alumno
	:type id_alumno: str

	:rtype: List[Asignatura]
	"""
	return 'do some magic!'


def get_asignaturas_matriculadas(id_alumno):
    """
    Asignaturas matriculadas
    Devuelve una lista con las asignaturas en las que esta matriculado el alumno
    :param id_alumno: id del alumno
    :type id_alumno: str
    :rtype: List[Asignatura]
    """
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    conexion = psycopg2.connect(conn_string)
    cursor = conexion.cursor()
    cursor.execute("SELECT \"id_gradoAsignatura\" FROM matriculacion WHERE (id_alumno =" + repr(id_alumno) + ")")
    cursor_rows = cursor.fetchall()
    lista_json = []
    for i in range(len(records)):
        ip_puerto='localhost:5003'
        direccion= ('http://'+ip_puerto+'/Facultad/asignatura/'+ str(records[i][0]))
        solicitud = requests.get(direccion)
        json_solicitud = solicitud.json()
        json1 = {
            "Codigo_Asignatura":records[i][0],
            "Creditos": json_solicitud['creditosAsignaturas'],
            "NombreAsignatura": json_solicitud['nombreAsignatura'],
            "NombreGrado": json_solicitud['nombreGrado'],
            "TurnoAsignatura":json_solicitud['turnoAsignatura']
            }
        json_list.append(json1)
        
    return(json_list)

