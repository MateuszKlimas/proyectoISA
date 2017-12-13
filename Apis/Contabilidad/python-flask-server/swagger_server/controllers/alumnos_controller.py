import connexion
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_matricula(contable):
    """
    Añade un nuevo ingreso de matricula
    Añade un nuevo ingreso de matricula
    :param contable: Se va añadir un nuevo ingreso de matricula
    :type contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        contable = Alumno.from_dict(connexion.request.get_json())
    return 'do some magic!'


def find_matricula(id_alumno):
    """
    Devuelve el ingreso de matricula de un alumno
    Devuelve el ingreso de matricula de un alumno
    :param id_alumno: id del alumno a buscar su ingreso
    :type id_alumno: int

    :rtype: List[Alumno]
    """
    return 'do some magic!'
