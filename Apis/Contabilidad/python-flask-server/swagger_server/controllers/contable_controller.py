import connexion
import psycopg2
import json
from swagger_server.models.contable import Contable
from swagger_server.models.nomina_contable import NominaContable
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_contable(contable):
    """
    Añade un nuevo contable
    Añades un nuevo contable.
    :param contable: Se va añadir un nuevo contable
    :type contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        contable = Contable.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contable VALUES (" + repr(contable.id_contable) + "," + "'" + contable.puesto_contable + "'" + ","+  "'" + contable.dni_contable + "'" + ","+  "'" + contable.nombre_contable + "'" + ","+  "'" + contable.apellidos_contable + "'" + ","+  "'" + contable.fecha_incorporacion_contable + "'" + ","+  "'" + contable.direccion_contable + "'" + ","+  "'" + contable.telefono_contable + "'" + ","+ repr(contable.id_departamento_contable) + ")")    
    conn.commit()
    conn.close()
    return "inserccion realizada con exito"


def add_salario_contable(salario_contable):
    """
    Añade un nueva nomina a un pas
    Añades un nuevo salario a un contable.
    :param nominaContable: El salario que se va a añadir
    :type nominaContable: int

    :rtype: None
    """
    if connexion.request.is_json:
        salario_contable = NominaContable.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"nominaContable\" VALUES (" + repr(salario_contable.id_nominda_contable) + "," + "'" + str(salario_contable.fecha_pago_nomina) + "'" + ","+ repr(salario_contable.importe_nomina_contable)  + ","+ repr(salario_contable.pago_nomina_contable_realizado) + ","+  repr(salario_contable.id_departamento_contable)+ ","+ repr(salario_contable.id_contable) + ")")    
    conn.commit()
    conn.close()
    return "inserccion realizada con exito"


def find_contableby_id(id_contable):
    """
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    :param id_contable: id del contable a buscar su salario
    :type id_contable: int

    :rtype: List[Contable]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM contable where contable.id_contable = " + str(id_contable))

    # retrieve the records from the database
    records = cursor.fetchall()
    
   
    json = {
    'id_contable':id_contable,
    'puesto_contable': records[0][1],
    'dni_contable': records[0][2],
    'nombre_contable:': records[0][3],
    'apellidos_contable:': records[0][4],
    'fecha_incorporacion_contable': records[0][5],
    'direccion_contable': records[0][6],
    'telefono_contable': records[0][7],
    'id_departamento_contable': records[0][8],
    
    }
        
    conn.close()
    return json


def find_nomina_contableby_id(id_contable):
    """
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    :param id_contable: id del contable a buscar su salario
    :type id_contable: int

    :rtype: List[NominaContable]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='isa' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"nominaContable\" where \"nominaContable\".\"id_nominaContable\" = " + str(id_contable))

    # retrieve the records from the database
    records = cursor.fetchall()
    json_list = []
    for i in range(len(records)):
        json = {
        'id_nomina': records[i][0],
        'fecha_pago_nomina': records[i][1],
        'importe_nomina:': records[i][2],
        'pago_nomina:': records[i][3],
        'id_departamento_contable': records[i][4],
        'id_contable':id_contable
        }
        
        json_list.append(json)
    conn.close()
    return json_list
