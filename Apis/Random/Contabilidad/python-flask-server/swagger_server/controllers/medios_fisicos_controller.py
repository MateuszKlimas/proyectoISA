import connexion
from swagger_server.models.medios_fisicos import MediosFisicos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_ingreso_medio_fisico(MediosFisicos):
    """
    Añade un nuevo ingreso para un medio fisico
    Añades un nuevo ingreso para un medio fisico
    :param ingresoMedioFisico: El ingreso del medio fisico que se va a añadir
    :type ingresoMedioFisico: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        ingresoMedioFisico = MediosFisicos.from_dict(connexion.request.get_json())"""
    return 'do some magic!'


def find_disponibilidad_id_medio_fisico(status):
    """
    Devuelve la disponibilidad a partir de una fecha introducida.
    Devuelve la disponibilidad a partir de una fecha introducida.
    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[MediosFisicos]
    """
    return 'do some magic!'


def find_id_medio_fisico(status):
    """
    Devuelve el precio de un medio fisico a partir de su ID.
    Devuelve el precio de un medio fisico a partir de su ID.
    :param status: Devuelve el precio de un medio fisico
    :type status: List[str]

    :rtype: List[MediosFisicos]
    """
    return 'do some magic!'


def update_ingreso_medio_fisico(body):
    """
    Actualiza el ingreso para un medio fisico
    Se cambia el ingreso actual por el nuevo ingreso, es decir, se actualiza el ingreso
    :param body: El precio del medio fisico que se va a actualizar
    :type body: dict | bytes

    :rtype: None
    """"""
    if connexion.request.is_json:
        body = MediosFisicos.from_dict(connexion.request.get_json())"""
    return 'do some magic!'
