import connexion
from swagger_server.models.alumnos import Alumnos
from swagger_server.models.profesores import Profesores
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_ingreso_alumno(salarioProfesores):
    """
    Añade un nuevo ingreso de un alumno
    Añades un nuevo ingreso de un alumno
    :param salarioProfesores: El ingreso que se va a añadir
    :type salarioProfesores: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        salarioProfesores = Alumnos.from_dict(connexion.request.get_json())
    return 'do some magic!'"""


def find_ingreso_alumno(status):
    """
    Devuelve los ingresos de un alumno a partir de su ID.
    Devuelve el ingreso de un alumno a partir de su codigo de identificacion.
    :param status: Devuelve los ingresos de un alumno
    :type status: List[str]

    :rtype: List[Alumnos]
    """
    return 'do some magic!'


def update_ingreso_alumno(body):
    """
    Actualiza el ingreso de un alumno
    Se cambia el ingreso actual por el nuevo ingreso, es decir, se actualiza el ingreso
    :param body: Actualizar ingreso
    :type body: dict | bytes

    :rtype: None"""
    """
    if connexion.request.is_json:
        body = Profesores.from_dict(connexion.request.get_json())"""    
    return 'do some magic!'
