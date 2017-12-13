import connexion
from swagger_server.models.pas import PAS
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario_pas(nominaPas):
    """
    Añade un nueva nomina a un pas
    Añades un nuevo salario a un pas.
    :param nominaPas: El salario que se va a añadir
    :type nominaPas: int

    :rtype: None
    """
    return 'do some magic!'


def find_pasby_id(id_profesor):
    """
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    Devuelve el salario de un pas a partir de su codigo de identificacion.
    :param id_profesor: id del profesor a buscar su salario
    :type id_profesor: int

    :rtype: List[PAS]
    """
    return 'do some magic!'
