import connexion
from swagger_server.models.profesores import Profesores
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario(salario_contable):
    """
    Añade un nuevo salario
    Añades un nuevo salario a un profesor, pensado para ocasiones puntuales en los que haya que añadir un nuevo salrio.
    :param salario_contable: Se va añadir un nuevo salario de un contable
    :type salario_contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        salario_contable = Profesores.from_dict(connexion.request.get_json())
    return 'do some magic!'


def find_profesorby_id(id_profesor):
    """
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    :param id_profesor: id del profesor a buscar su salario
    :type id_profesor: int

    :rtype: List[Profesores]
    """
    return 'do some magic!'
