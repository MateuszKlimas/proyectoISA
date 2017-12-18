import connexion
from swagger_server.models.pas import Pas
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def busqueda_pas(idPas):
    """
    Mostar un personal en concreto
    Buscar un personal de administracion y servicios dentro de la lista del personal
    :param idPas: Identificador del Personal
    :type idPas: int

    :rtype: Pas
    """
    return 'do some magic!'


def insertar_pas(pas):
    """
    Añadir un nuevo personal
    Insertar un nuevo personal en  la lista del personal de administracion  y servicios
    :param pas: 
    :type pas: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        pas = Pas.from_dict(connexion.request.get_json())
    return 'do some magic!'
