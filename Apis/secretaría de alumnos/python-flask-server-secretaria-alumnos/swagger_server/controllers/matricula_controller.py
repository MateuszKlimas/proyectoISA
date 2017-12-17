import connexion
from swagger_server.models.asignatura_matricula import AsignaturaMatricula
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import psycopg2
import json
conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"


def realizar_automatricula(id_usuario, asignaturas):
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
        dato = i['codigo_asignatura']
        print(dato)
        cursor.execute("INSERT INTO matriculacion VALUES (1,0,0,0,false," + str(id_usuario) + "," + str(dato) + ")")
    cursor.execute("SELECT * from matriculacion")
    records = json.dumps(cursor.fetchall())
    conn.commit()

    return(records)
    
    
