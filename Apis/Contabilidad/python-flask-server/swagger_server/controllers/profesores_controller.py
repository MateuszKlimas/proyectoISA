import connexion
from swagger_server.models.profesores import Profesores
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_salario(nominaProf):
    """
    Añade un nuevo salario
    Añades un nuevo salario a un profesor, pensado para ocasiones puntuales en los que haya que añadir un nuevo salrio.
    :param nominaProf: El salario que se va a añadir
    :type nominaProf: int

    :rtype: None
    """
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
