import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.departamento import Departamento
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def agregar_profesor(profesor):
    """
    Agrega un profesor a la base de datos
    
    :param profesor: 
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    return 'do some magic!'


def busqueda_profesor(id_profesor):
    """
    Muestra un profesor a partir de un id de profesor
    
    :param id_profesor: id del profesor
    :type id_profesor: int

    :rtype: Departamento
    """
    return 'do some magic!'


def busqueda_profesores(id_departamento):
    """
    Muestra la lista de profesores de un departamento
    
    :param id_departamento: id del departamento
    :type id_departamento: int

    :rtype: Departamento
    """
    jsons = []
    conn_string = "host='localhost' dbname='DepartamentoProfesores' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query = "SELECT \'id_profesor\' FROM profesor WHERE id_departamento="+id_departamento+";"
    cursor.execute(query)
    records = cursor.fetchall()
    
    for row in range(cursor.rowcount):
        json1 = {
        "id_profesor" : records[row][0]
        }
        jsons.append(json1)
    conn.close()
    return jsons

