import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.asignatura_cod_grado import AsignaturaCodGrado
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import psycopg2
import json
conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"

def asignatura_id_asignatura_get(idAsignatura):
    """
    Obtienes una asignatura a partir de su código
    Devuelve un objeto del tipo asignatura con todos sus datos, a partir del código del grado.
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Asignatura
    """
    return 'do some magic!'


def get_asignaturas(tamanoPagina, numeroPaginas):
    """
    Obtiene un listado de todas las asignaturas de la Base de datos
    Devuelve una lista con las asignaturas.
    :param tamanoPagina: Número de grados devueltos
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltos
    :type numeroPaginas: int

    :rtype: List[Asignatura]
    """
    return 'do some magic!'


def gradoasignatura_id_grado_asignatura_get(idGradoAsignatura):
    """
    Obtienes una asignatura a partir de su código de grado_asignatura
    Devuelve un objeto del tipo asignatura con todos sus datos, a partir del código del grado.
    :param idGradoAsignatura: Codigo del grado_asignatura
    :type idGradoAsignatura: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_asignaturas_grado(idGrado):
    asignaturas = []
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()    
    cursor.execute("select id_asignatura, \"nombreAsignatura\", \"creditosAsignatura\",\"tipoAsignatura\",\"descripcionAsignatura\" from asignatura natural join grado_asignatura natural join grado where id_grado=" + str(idGrado))
    records = cursor.fetchall()
    for row in range(cursor.rowcount):
        json = {
            "idAsignatura" : records[row][0],
            "nombreAsignatura" : records[row][1],
            "creditosGrado" : records[row][2],
            "tipoAsignatura" : records[row][3],
            "descripcionAsignatura" : records[row][4]
        }
        asignaturas.append(json)
    conn.commit()
    conn.close()
    return asignaturas


def post_asignatura(asignatura):
    """
    Añadir una asignatura a nuestra Base de datos.
    Añade una asignatura a nuestra base de datos.
    :param asignatura: La asignatura que se va a añadir, en el grado especificado.
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = AsignaturaCodGrado.from_dict(connexion.request.get_json())
    return 'do some magic!'


def remove_asignatura(idAsignatura):
    """
    Eliminar la asignatura
    Elimina la asignatura que se le pasa como codigo de la universidad
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Asignatura
    """
    return 'do some magic!'


def update_asignatura(asignatura):
    """
    Actualizar los datos de una asignatura
    Actualiza los datos de la asignatura
    :param asignatura: Codigo de la asignatura
    :type asignatura: dict | bytes

    :rtype: Asignatura
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    return 'do some magic!'
