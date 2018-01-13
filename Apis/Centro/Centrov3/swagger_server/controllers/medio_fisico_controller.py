import connexion
import psycopg2
from swagger_server.models.medio_fisico_centro import MedioFisicoCentro
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def medio_fisico_id_centro_get(idCentro):
    """
    Obtiene un listado de todos los medios existentes en una facultad 
    Devuelve una lista con los medios fisicos
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
        # print the connection string we will use to connect
    print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
        # execute our Query
    cursor.execute("SELECT id_medio, \"nombreMedioFisico\", \"tipoMedioFisico\", \"precioMedioFisico\", \"capacidadMedioFisico\", id_centro FROM centro WHERE id_centro = idCentro ORDER BY id_centro DESC;")
    records = cursor.fetchall()
    jsons = []

    for row in range(cursor.rowcount):
        json1 = {
        "idMedio" : records[row][0],
        "nombreMedio" : records[row][1],
        "tipoMedio" : records[row][2],
        "precioMedio" : records[row][3],
        "capacidad" : records[row][4],
        "idCentro" : records[row][5],
        }
        jsons.append(json1)
    conn.close()
    return jsons


def obtener_medios(idCentro):
    """
    Obtener el medio
    Obtiene el medio que se le pasa como codigo del centro
    :param idMedio: Codigo del medio
    :type idMedio: int

    :rtype: MedioFisicoCentro
    """
    return 'do some magic!'

def post_medio(medioFisico):
    """
    Añade un medio fisico
    Añade un nuevo medio fisico
    :param medioFisico: El medio que se va a añadir, en el centro especificado.
    :type medioFisico: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medioFisico = MedioFisicoCentro.from_dict(connexion.request.get_json())
    return 'do some magic!'


def remove_medio(idMedio):
    """
    Eliminar el medio
    Elimina el medio que se le pasa como codigo del medio
    :param idMedio: Codigo del medio
    :type idMedio: int

    :rtype: MedioFisicoCentro
    """
    return 'do some magic!'


def update_medio(Medio):
    """
    Actualizar los datos de un medio fisico
    Actualiza los datos de un medio fisico
    :param Medio: Medio a Actualizar
    :type Medio: dict | bytes

    :rtype: MedioFisicoCentro
    """
    if connexion.request.is_json:
        Medio = MedioFisicoCentro.from_dict(connexion.request.get_json())
    return 'do some magic!'
