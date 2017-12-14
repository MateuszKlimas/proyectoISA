import connexion
import psycopg2
import json
from swagger_server.models.departamento_contable import DepartamentoContable
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_departamento_contable(departamento_contable):
    """
    Añade un nuevo departamento contable
    Añade un nuevo ingreso de matricula
    :param departamento_contable: Se va añadir un nuevo departamento contable
    :type departamento_contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento_contable = DepartamentoContable.from_dict(connexion.request.get_json())
    
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    dep = departamento_contable
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"departamentoContable\" VALUES (" + repr(dep.id_departamento_contable) + "," + "'" + dep.nombre_departamento_contable + "'" + ","+  "'" + dep.descripcion_departamento_contable + "'" + ","+ repr(dep.id_facultad) + ")")    
    conn.commit()
    conn.close()
    return ""


def find_departamento_contable(id_departamento_contable):
    """
    Devuelve el departamento contable
    Devuelve el departamento contable
    :param id_departamento_contable: id del departamento contable
    :type id_departamento_contable: int

    :rtype: List[DepartamentoContable]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"departamentoContable\" where \"departamentoContable\".\"id_departamentoContable\" = " + str(id_departamento_contable))

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)
