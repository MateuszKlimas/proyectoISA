import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario(salarioProfesores):
    """
    Añade un nuevo salario
    Añades un nuevo salario a un profesor, pensado para ocasiones puntuales en los que haya que añadir un nuevo salrio.
    :param salarioProfesores: El salario que se va a añadir
    :type salarioProfesores: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        salarioProfesores = salarioProfesores.from_dict(connexion.request.get_json())
    return 'do some magic!'"""


def find_profesorby_id(status):
    """
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    Devuelve el salario de un profesor a partir de su codigo de identificacion.
    :param status: Devuelve el salario del docente a buscar
    :type status: List[str]

    :rtype: List[Profesores]
    """
    return 'do some magic!'


def update_salario(body):
    """
    Actualiza el salario de un docente
    Se cambia el salario actual por el nuevo salario, es decir, se actualiza el salario
    :param body: El salario a actualizar sera añadido
    :type body: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        body = Profesores.from_dict(connexion.request.get_json())
    return 'do some magic!'"""
