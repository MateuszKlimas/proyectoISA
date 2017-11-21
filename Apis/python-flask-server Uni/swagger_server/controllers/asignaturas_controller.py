import connexion
from swagger_server.models.asignatura import Asignatura
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


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


def post_asignatura(asignatura):
    """
    Añadir una asignatura a nuestra Base de datos.
    Añade una asignatura a nuestra base de datos.
    :param asignatura: La asignatura que se va a añadir.
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    return 'do some magic!'
