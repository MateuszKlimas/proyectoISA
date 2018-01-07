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

	

	conexion.commit()
	conexion.close()

	"""
	[
		{
			"codigo_asignatura": 0,
			"creditos": "string",
			"nombre": "string",
			"tipo": "string"
		}
	]
	"""

	lista_json = []

	
	for row in cursor_rows:

		ip_puerto = 'localhost:8080'
		uri = 'http://' + ip_puerto + '/Facultad/asignatura/' + repr(row[0])
		solicitud = requests.get(uri)
		json_asignatura = solicitud.json()

		json1 = {
					"codigo_asignatura": row[0],
					"creditos": json_asignatura['creditosAsignaturas'],
					"nombre": json_asignatura['nombreAsignatura'],
					"nombreGrado": json_asignatura['nombreGrado'],
					"turnoAsignatura": json_asignatura['turnoAsignatura']
				}

		lista_json.append(json1)

	return lista_json

