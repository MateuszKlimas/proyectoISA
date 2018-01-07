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
		
	querie = ""
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()

	#    if datos['id_matriculacion'] != "":
	#    querie += "\"id_matriculacion\"=" + str(datos['id_matriculacion']) + ", "
	#    if datos['numero_convocatoria'] != -1:
	#    querie += "\"numConvocatoria\"=" + str(datos['numero_convocatoria']) + ", "
	#    if datos['numero_matricula'] != -1:
	#    querie += "\"numMatricula\"=" + str(datos['numero_matricula']) + ", "
	#    if datos['nota'] != -1:
	#    querie += "\"notaAlumno\"=" + str(datos['nota']) + ", "
	#    if datos['id_alumno'] != "":
	#    querie += "\"id_alumno\"=" + str(datos['id_alumno']) + ", "
	#    if datos['codigo_asignatura'] != "":
	#    querie += "\"id_gradoAsignatura\"='" + str(datos['codigo_asignatura']) + "', "

	#cursor.execute("UPDATE matriculacion SET " + querie + " \"aprobado\"=" + str(datos['aprobado']) + " WHERE id_alumno=" + str(id_usuario) + " AND \"numMatricula\"="
	#               + str(datos['numero_matricula']))
	cursor.execute("UPDATE matriculacion SET \"notaAlumno\"=" + str(datos['nota']) + ", aprobado=" + str(datos['aprobado']) + ", \"id_gradoAsignatura\"="+ str(datos['codigo_asignatura'])
				   +  ", \"numConvocatoria\"=" + str(datos['numero_convocatoria']) + ", \"numMatricula\"=" +
				   str(datos['numero_matricula'])+ " where id_alumno=4 AND id_matriculacion=" + str(datos['id_matriculacion']))
	conn.commit()
	conn.close()

	
	return 'OK' 


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
	return 'do some magic!'


def realizar_automatricula(id_usuario, asignaturas=None):
	"""
	Automatricula
	Permite a un alumno realizar su automatricula
	:param id_usuario: id del usuario
	:type id_usuario: str
	:param asignaturas: 
	:type asignaturas: list | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		asignaturas = [AsignaturaMatricula.from_dict(d) for d in connexion.request.get_json()]
		
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	
	# execute our Query
	for i in asignaturas:
		#Hay que eliminar el id de alumno del array de asignaturas
		cursor.execute("INSERT INTO matriculacion VALUES (" + str(i['id_matriculacion']) + "," + str(i['numero_convocatoria']) + "," + str(i['numero_convocatoria']) +
					   "," + str(i['nota']) + "," + str(i['aprobado']) + "," + str(id_usuario) + "," + str(i['codigo_asignatura']) + ")")
	conn.commit()
	conn.close()
	return 'OK'
