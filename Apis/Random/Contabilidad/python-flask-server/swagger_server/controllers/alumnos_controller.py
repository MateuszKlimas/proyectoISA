import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.alumnos import Alumnos
from swagger_server.models.profesores import Profesores
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime



def add_ingreso_alumno(salarioProfesores):
    """
    Añade un nuevo ingreso de un alumno
    Añades un nuevo ingreso de un alumno
    :param salarioProfesores: El ingreso que se va a añadir
    :type salarioProfesores: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        salarioProfesores = Alumnos.from_dict(connexion.request.get_json())"""
    return 'do some magic!'


def find_ingreso_alumno(status):
    """
    Devuelve los ingresos de un alumno a partir de su ID.
    Devuelve el ingreso de un alumno a partir de su codigo de identificacion.
    :param status: Devuelve los ingresos de un alumno
    :type status: List[str]

    :rtype: List[Alumnos]
    """
    conn_string = "host='localhost' dbname='prueba1' user='postgres' password='1234'"
	# print the connection string we will use to connect
    print ("Connecting to database\n")
 
	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
 
	# execute our Query
    cursor.execute("SELECT * FROM \"PERSONAL\" WHERE numero_personal =1")
 
	# retrieve the records from the database
    records = json.dumps(cursor.fetchall())
 
	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
    #pprint.pprint(records)

    return records

def update_ingreso_alumno(body):
    """
    Actualiza el ingreso de un alumno
    Se cambia el ingreso actual por el nuevo ingreso, es decir, se actualiza el ingreso
    :param body: Actualizar ingreso
    :type body: dict | bytes

    :rtype: None"""
    """
    if connexion.request.is_json:
        body = Profesores.from_dict(connexion.request.get_json())"""
    return 'do some magic!'
