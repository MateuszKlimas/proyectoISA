import connexion
import psycopg2
import json
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
    
    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    doce = docencia
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"docencia\" VALUES (" + repr(doce.id_docencia) + "," + repr(doce.id_profesor) + "," + repr(doce.id_gradoAsignatura) + ");")    
    conn.commit()
    conn.close()
    return ""


def get_docencia_idProf(id_profesor):
    """
    Devuelve relacion de profesor con asignaturas
    
    :param id_profesor: id del profesor
    :type id_profesor: int

    :rtype: Docencia
    """
    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"docencia\" WHERE \"docencia\".\"id_profesor\" = " + str(id_profesor) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)

def get_docencia_idAsig(id_asignaturaGrado):
    """
    Devuelve relacion de profesor con asignaturas

    :param id_asignaturaGrado: id de la asignatura de un grado
    :type id_asignaturaGrado: int

    :rtype: Docencia
    """

    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"docencia\" WHERE \"docencia\".\"id_gradoAsignatura\" = " + str(id_asignaturaGrado) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)

def actualizar_docencia(docencia):

    if connexion.request.is_json:
        docencia = Docencia.from_dict(connexion.request.get_json())

    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    doce = docencia
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    ###cursor.execute("UPDATE \"docencia\" SET \"docencia\".\"id_docencia\" = " + str(doce.id_docencia+ ", \"docencia\".\"id_profesor\" = " + str(doce.id_profesor) ", \"docencia\".\"id_gradoAsignatura\" = " + str(doce.id_gradoAsignatura) + " WHERE id_docencia = " + str(doce.id_docencia) + ";")
    conn.commit()
    conn.close()
    return ""

def eliminar_ingreso(idDocencia):

    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("DELETE FROM \"docencia\" where \"docencia\".\"id_docencia\" = " + str(idDocencia) + ";")
    conn.commit()
    conn.close()
    return "" 
