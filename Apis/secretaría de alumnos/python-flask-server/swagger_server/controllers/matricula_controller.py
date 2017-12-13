import connexion
from swagger_server.models.asignatura_matricula import AsignaturaMatricula
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def realizar_automatricula(id_usuario, asignaturas=None):
    """
    Automatricula
    Permite a un alumno realizar su automatricula
    :param id_usuario: nombre del usuario
    :type id_usuario: str
    :param asignaturas: 
    :type asignaturas: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignaturas = [AsignaturaMatricula.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
