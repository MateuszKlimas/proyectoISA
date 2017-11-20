import connexion
from swagger_server.models.pas import PAS
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario_pas(salarioPAS):
    """
    Añade un nuevo salario de un PAS
    Añades un nuevo salario a un PAS, pensado para ocasiones puntuales en los que haya que añadir un nuevo salrio.
    :param salarioPAS: El salario que se va a añadir
    :type salarioPAS: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        salarioPAS = PAS.from_dict(connexion.request.get_json())
    return 'do some magic!'


def find_pa_sby_id(status):
    """
    Devuelve el salario de un PAS a partir de su codigo de identificacion.
    Devuelve el salario de un PAS a partir de su codigo de identificacion.
    :param status: Devuelve el salario del PAS
    :type status: List[str]

    :rtype: List[PAS]
    """
    return 'do some magic!'


def update_salario_pas(body):
    """
    Actualiza el salario de un PAS
    Se cambia el salario actual por el nuevo salario, es decir, se actualiza el salario
    :param body: Se actualizara el salario
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PAS.from_dict(connexion.request.get_json())
    return 'do some magic!'
