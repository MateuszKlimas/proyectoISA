import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.universidad import Universidad
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_facultad(facultad):
    """
    Crea una facultad
    Añade una universidad a la lista de universidades.
    :param facultad: La facultad que se va a añadir.
    :type facultad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        facultad = Universidad.from_dict(connexion.request.get_json())

        
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    print ("Connecting to database\n")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO centro VALUES ("+ repr(facultad.cod_uni)+","+"'"+facultad.name+"'"+","+"'"+(facultad.dir)+"'"+")")
    conn.commit()
    return 'Insert realizado '


def obtener_facultad(tamanoPagina, numeroPaginas):
    """
    Obtiene facultades
    Obtiene un listado de las universidades del sistema.
    :param tamanoPagina: Número de univesidades devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Universidad]
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT * FROM centro")

    records = json.dumps(cursor.fetchall())


    return(records)


def remove_facultad(idAsignatura):
    """
    Eliminar la asignatura
    Elimina la asignatura que se le pasa como codigo de la universidad
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Universidad
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("DELETE FROM centro where centro.id_centro = " + str(idAsignatura))
    conn.commit()

    
    return 'Borrado'



def universidad_get_uni(codUni):
    """
    Devuelve una universidad a partir de su código
    Devuelve una única universidad identificada por su codigo de universidad
    :param codUni: Codigo de la universidad
    :type codUni: int

    :rtype: Universidad
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT \"nombreCentro\" FROM centro WHERE id_centro=" + str(codUni))


    records = json.dumps(cursor.fetchall())
    return records


def update_facultad(universidad):
    """
    Actualizar facultad
    Permite la actualización de los datos de la facultad.
    :param universidad: La universidad que se va a actualizar
    :type universidad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        universidad = Universidad.from_dict(connexion.request.get_json())

    conn_string = ("host='localhost' dbname='Centros' user='ISA' password='1234'")
    print ("Connecting to database\n")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("UPDATE public.centro set id_centro =" +str(universidad.cod_uni)+ ",\"nombreCentro\" ="+"'"+universidad.name+"'"+
                   ",\"direccionCentro\" ="+"'"+ universidad.dir+"'"+"WHERE id_centro= "+str(universidad.cod_uni))
    conn.commit()
    return 'Cambio bien realizdo'

