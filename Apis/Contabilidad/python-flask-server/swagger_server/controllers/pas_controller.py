import connexion
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
    if connexion.request.is_json:
        salario_pas = PAS.from_dict(connexion.request.get_json())
    return 'do some magic!'


def find_pasby_id(id_pas):
    """
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    :param id_pas: id del pas a buscar su salario
    :type id_pas: int

    :rtype: List[PAS]
    """
    return 'do some magic!'
