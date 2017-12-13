import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.creditos import Creditos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def consultar_creditos_asignatura(nombre_asignatura):
    """
    creditos de cada asignatura
    Permite consultar cuantos creditos tiene cada asigntura
    :param nombre_asignatura: nombre de la asignatura buscada
    :type nombre_asignatura: str

    :rtype: Creditos
    """
    return 'do some magic!'


def get_asignaturas_disponibles(id_alumno):
    """
    Asignaturas disponibles para matricular
    Devuelve una lista con las asignaturas en las que puede matricularse un alumno
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: List[Asignatura]
    """
    return 'do some magic!'


def get_asignaturas_matriculadas(id_alumno):
    """
    Asignaturas matriculadas
    Devuelve una lista con las asignaturas en las que esta matriculado el alumno
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: List[Asignatura]
    """
    return 'do some magic!'
