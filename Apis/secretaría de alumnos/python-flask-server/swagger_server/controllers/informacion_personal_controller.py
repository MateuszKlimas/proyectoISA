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
    
    
    """for i in range(len(records)): 
        direccion= ('http://localhost:5003/Facultad/asignatura/'+ records[i][0])
        solicitud = requests.get(direccion)
        retorno.add(solicitud)


    records2=json.dumps(retorno)"""

    return(records)

    


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
 
    cursor.execute("SELECT matriculacion.aprobado, matriculacion.\"id_gradoAsignatura\",matriculacion.\"numConvocatoria\",matriculacion.\"notaAlumno\" FROM matriculacion WHERE id_alumno="+id_alumno)
 
	# retrieve the records from the database
    records = json.dumps(cursor.fetchall())

    return(records)

    



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
