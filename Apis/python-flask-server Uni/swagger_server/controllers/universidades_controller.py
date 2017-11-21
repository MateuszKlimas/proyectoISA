import connexion
from swagger_server.models.universidad import Universidad
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_universidad(universidad):
    """
    Crea una universidad
    Añade una universidad a la lista de universidades.
    :param universidad: La universidad que se va a añadir.
    :type universidad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        universidad = Universidad.from_dict(connexion.request.get_json())
    return 'do some magic!'


def obtener_universidad(tamanoPagina, numeroPaginas):
    """
    Obtiene universidades
    Obtiene un listado de las universidades del sistema.
    :param tamanoPagina: Número de univesidades devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Universidad]
    """
    return 'do some magic!'


def universidad_get_uni(codUni):
    """
    Devuelve una universidad a partir de su código
    Devuelve una única universidad identificada por su codigo de universidad
    :param codUni: Codigo de la universidad
    :type codUni: int

    :rtype: Universidad
    """
    return 'do some magic!'
