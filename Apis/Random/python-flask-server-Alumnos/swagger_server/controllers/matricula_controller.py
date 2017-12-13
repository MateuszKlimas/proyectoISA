import connexion
from swagger_server.models.asignatura import Asignatura
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def realizar_automatricula(nombre_usuario, contrasea, asignaturas=None):
    """
    Automatricula
    Permite a un alumno realizar su automatricula
    :param nombre_usuario: nombre del usuario
    :type nombre_usuario: str
    :param contrasea: contraseña del usuario
    :type contrasea: int
    :param asignaturas: 
    :type asignaturas: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignaturas = [Asignatura.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
