import connexion

import psycopg2
import sys
import pprint
import json
from swagger_server.models.alumno import Alumno
from swagger_server.models.creditos import Creditos
from swagger_server.models.nota import Nota
from swagger_server.models.pago import Pago
from swagger_server.models.resumen_pagos import ResumenPagos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def consultar_creditos_reconocidos(id_alumno):
    """
	creditos convalidados
	muestra una lista de los creditos convalidados del alimno asi como la asignatura a la que pertenecen
	:param id_alumno: id del usuario
	:type id_alumno: str
	:rtype: List[Creditos]
	"""
	retorno=[]
	conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
	conn = psycopg2.connect(conn_string)#Nos conectamos 
	cursor = conn.cursor()
	cursor.execute("SELECT matriculacion.\"id_gradoAsignatura\" FROM matriculacion WHERE id_alumno="+id_alumno+" AND aprobado=True")
	records =cursor.fetchall()

	lista_json = []
	for row in records:
		direccion = 'localhost::8080'
		uri= ('http://' + direccion +  '/Facultad/asignatura/'+ row[0])
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
	return(lista_json)
    


def consultar_info(id_alumno):
    """
    Consulta información personal de un alumno
    Devuelve un json con la información personal de un alumno
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: Alumno
    """
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    
 
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM alumno WHERE id_alumno="+id_alumno)
 
	# retrieve the records from the database
    records = json.dumps(cursor.fetchall())

    return(records)


def consultar_notas(id_alumno):
    """
    consulta las notas
    Consulta las notas de todas las asignaturas matriculadas, así como otra información relacionada con las notas de la asignatura, como el número de créditos de la asignatura etc.
    :param id_alumno: id del alumno
    :type id_alumno: str
    :rtype: List[Nota]
    """
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    
 
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT matriculacion.aprobado, matriculacion.\"id_gradoAsignatura\",matriculacion.\"numConvocatoria\",matriculacion.\"notaAlumno\" FROM matriculacion WHERE id_alumno="+str(id_alumno))
    json_list=[]
    records =cursor.fetchall()
 
    for i in range(len(records)):
        direccion= ('http://localhost:5003/Facultad/asignatura/'+ str(records[i][1]))
        solicitud = requests.get(direccion)
        json_solicitud = solicitud.json()
        json1 = {
        "Aprobado":records[i][0],
	"Nombre asignatura": json_solicitud['nombreAsignatura'],
        "Convocatoria":records[i][2],
        "Creditos": json_solicitud['creditosAsignaturas'],
        "Nota":records[i][3],
        "Tipo":json_solicitud['turnoAsignatura']
	}
        json_list.append(json1)
        
    return(json_list)

    



def consultar_pagos(id_alumno):
    """
    Consuta informacion económica de la matrícula
    Consulta el importe total de la matrícula y el importe de los pagos a plazos
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: ResumenPagos
    """
    #Acceder a la api que me de la informacion economica
    return 'Falta realizar api de contabilidad Alumnos'


def find_pago(id_usuario, mes):
    """
    Devuelve un recibo
    Devuelve el recibo del mes que se especifique en la llamada
    :param id_usuario: id del usuario
    :type id_usuario: str
    :param mes: mes correspondiente al pago buscado
    :type mes: int
    

    :rtype: Pago
    """
    #Acceder a la api que me de esta informacion economica
    return 'Falta realizar api de contabilidad Alumnos'
