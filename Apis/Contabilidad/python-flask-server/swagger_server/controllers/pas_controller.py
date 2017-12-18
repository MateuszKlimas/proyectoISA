import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.pas import PAS
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario_pas(salario_pas):
    """
    Añade un nueva nomina a un pas
    Añades un nuevo salario a un pas.
    :param salario_pas: Se va añadir un nuevo salario de un pas
    :type salario_pas: dict | bytes

    :rtype: None
    """
    fecha="2017-12-12"
    if connexion.request.is_json:
        salario_pas = PAS.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()

    cursor.execute("INSERT INTO \"nominaPAS\" VALUES (" + repr(salario_pas.id_nominda_pas) +
                   "," + "'" + fecha + "'" + ","+ repr(salario_pas.importe_nomina_pas)
                   + ","+ repr(salario_pas.pago_nomina_pas_realizado) + ","+  repr(salario_pas.id_departamento_contable)
                   + ","+ repr(salario_pas.id_pas) + ")")
    conn.commit()
    return 'Todo correcto'


def find_pasby_id(id_pas):
    """
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    :param id_pas: id del pas a buscar su salario
    :type id_pas: int

    :rtype: List[PAS]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT \"nominaPAS\".\"importeNominaPAS\" FROM \"nominaPAS\" WHERE id_pas="+str(id_pas))
 
    # retrieve the records from the database
    records = json.dumps(cursor.fetchall())
    

    return records





