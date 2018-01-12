import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.profesores import Profesores
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario(salario_contable):
    """
    Añade un nuevo salario
    Añades un nuevo salario a un profesor, pensado para ocasiones puntuales en los que haya que añadir un nuevo salrio.
    :param salario_contable: Se va añadir un nuevo salario de un contable
    :type salario_contable: dict | bytes

    :rtype: None
    """
    fecha="12-12-2017"
    if connexion.request.is_json:
        salario_contable = Profesores.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"nominaProfesor\" VALUES ("
                    + repr(salario_contable.id_nominda_profesor) +","
                    + "'" + fecha + "'" +","
                   +  repr(salario_contable.importe_nomina_profesor) + ","
                   + repr(salario_contable.pago_nomina_profesor_realizado) + ","
                   +  repr(salario_contable.id_departamento_contable)+","
                   + repr(salario_contable.id_profesor)+")"
                   )
    conn.commit()

    return 'Todo correcto'


def find_profesorby_id(id_profesor):
    """
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    :param id_profesor: id del profesor a buscar su salario
    :type id_profesor: int

    :rtype: List[Profesores]
    """
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM \"nominaProfesor\" WHERE id_profesor="+str(id_profesor))
 
    # retrieve the records from the database
    records = cursor.fetchall()
    json_list = []
    for i in range(len(records)):
        json = {
        'id_nomina_profesor': records[i][0],
        'fecha_pago_nomina_profesor': records[i][1],
        'importe_nomina_profesor:': records[i][2],
        'pago_nomina:': records[i][3],
        'id_departamento_contable': records[i][4],
        'id_profesor':id_profesor
        }
        
        json_list.append(json)
    conn.close()
    return json_list






