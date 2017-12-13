import connexion
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
