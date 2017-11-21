import connexion
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

    :rtype: List[Universidad]
    """
    return 'do some magic!'


def grado_cod_grado_get(codGrado):
    """
    Obtienes un grado a partir de su código
    Devuelve un objeto del tipo grado con todos sus datos, a partir del código del grado.
    :param codGrado: Codigo del grado
    :type codGrado: int

    :rtype: Grado
    """
    return 'do some magic!'


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
    return 'do some magic!'
