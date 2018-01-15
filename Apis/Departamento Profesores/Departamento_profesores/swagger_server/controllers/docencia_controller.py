import connexion
import psycopg2 
import json
import pprint
from swagger_server.models.docencia import Docencia
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def agregar_docencia(docencia):
    """
    Agrega una relacion de un profesor con una asignatura
    
    :param docencia: 
    :type docencia: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        docencia = Docencia.from_dict(connexion.request.get_json())
    return 'do some magic!'


def busqueda_docencia(id_profesor):
    """
    Devuelve relacion de profesor con asignaturas
    
    :param id_profesor: id del profesor
    :type id_profesor: int

    :rtype: Docencia
    """
    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
	# print the connection string we will use to connect
    print ("Connecting to database\n")
	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
	# execute our Query
    query = "SELECT \"id_gradoAsignatura\" FROM \"docencia\" WHERE id_profesor="+str(id_profesor)+";"
    cursor.execute(query)
	# retrieve the records from the database
    records = cursor.fetchall()
    jsons = []
    for row in range(cursor.rowcount):
        json1 = {
            "id_gradoAsignatura" : records[row][0]
        }
        jsons.append(json1)
    conn.close()

    return jsons
