import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_matricula(ingreso_matricula):
    """
    Añade un nuevo ingreso de matricula
    Añade un nuevo ingreso de matricula
    :param ingreso_matricula: Se va añadir un nuevo ingreso de matricula
    :type ingreso_matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ingreso_matricula = Alumno.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    pago = ingreso_matricula
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"pagoMatriculaAlumno\" VALUES ("
     + repr(pago.id_pago_matricula_alumno) + "," + "'"
      + "12-12-2016" + "'" + ","
      + repr(pago.importe_matricula_alumno) + "," 
      + repr(pago.pago_matricula_alumno_realizado) + ","
       + repr(pago.id_departamento_contable) + ","
        + repr(pago.id_alumno) + ");")    
    conn.commit()
    conn.close()
    return "Inserccion realizada con exito" 


def find_matricula(id_alumno):
    """
    Devuelve el ingreso de matricula de un alumno
    Devuelve el ingreso de matricula de un alumno
    :param id_alumno: id del alumno a buscar su ingreso
    :type id_alumno: int

    :rtype: List[Alumno]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"pagoMatriculaAlumno\" WHERE \"pagoMatriculaAlumno\".\"id_alumno\" = " + str(id_alumno) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    json_list = []
    for i in range(len(records)):
        json = {
        'id_pago_matricula': records[i][0],
        'fecha_pago_matricula': records[i][1],
        'importe_matricula': records[i][1],
        'pago_matricula_realizado:': records[i][2],
        'id_departamento_contable:': records[i][3],
        'id_alumno':id_alumno
        }
        
        json_list.append(json)
    conn.close()
    return json_list

