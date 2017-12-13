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
    
    conn_string = "host='localhost' dbname='DepartamentoContable' user='postgres' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    dep = departamento_contable
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("insert into departamentoContable"+ "values(" + dep[0] + "," + dep[1] + ","+ dep[2] + ","+ dep[3] + ")")    
    return 'do some magic!'


def find_departamento_contable(id_departamento_contable):
    """
    Devuelve el departamento contable
    Devuelve el departamento contable
    :param id_departamento_contable: id del departamento contable
    :type id_departamento_contable: int

    :rtype: List[DepartamentoContable]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='postgres' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"departamentoContable\"s")

    # retrieve the records from the database
    records = cursor.fetchall()
    return json.dumps(records)
