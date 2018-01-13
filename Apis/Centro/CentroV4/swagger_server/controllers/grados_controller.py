import connexion
import psycopg2
import json
from swagger_server.models.grado import Grado
from swagger_server.models.universidad import Universidad
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_grados(tamanoPagina, numeroPaginas):
    """
    Obtiene una lista de todos los grados del sistema.
    Obtiene un listado de los grados del sistema.
    :param tamanoPagina: Número de grados devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Grado]
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grado")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(str(records))


def grado_cod_grado_get(codGrado):
    """
    Obtienes un grado a partir de su código
    Devuelve un objeto del tipo grado con todos sus datos, a partir del código del grado.
    :param codGrado: Codigo del grado
    :type codGrado: int

    :rtype: Grado
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grado where grado.id_grado = " + str(codGrado))

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(str(records))


def post_grado(grado):
    """
    Añade un grado a la base de datos.
    Añade un grado a nuestra base de datos
    :param grado: El grado  que se va a añadir.
    :type grado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        grado = Grado.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grado VALUES (" + repr(grado.cod_grado) +
    ","+ "'" + grado.nombre + "'"  + ","+ repr(grado.num_cred_obligatorios) + ","+  repr(grado.num_cred_transversales)+ 
    ","+ repr(grado.num_cread_optativos) + "," + repr(grado.id_universidad) +  ")")    
    conn.commit()
    conn.close()
    return "inserccion realizada con exito"


def remove_grado(idGrado):
    """
    Eliminar el grado
    Elimina la asignatura que se le pasa como codigo de la universidad
    :param idGrado: Codigo del grado
    :type idGrado: int

    :rtype: Grado
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("delete FROM grado where grado.id_grado = " + str(idGrado))
    conn.commit()
    conn.close()
    return "borrado con exito"


def update_grado(grado):
    """
    Actualizar grado
    Permite la actualización de los datos del  grado.
    :param grado: El grado que se va a actualizar
    :type grado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        grado = Universidad.from_dict(connexion.request.get_json())
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("update grado set  \"nombreGrado\" = " + "'" + str(grado.name) + "'" + 
    ", id_centro = " + str(grado.cod_uni)) 
    conn.commit()
    conn.close()
    return "update realizado con exito"
