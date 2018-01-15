import connexion
from swagger_server.models.reserva import Reserva
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def obtener_reserva(tamanoPagina, numeroPaginas):
    """
    Obtiene las reservas que se tienen
    Devuelve todos los medios fisicos.
    :param tamanoPagina: Número de medios devueltos
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Reserva]
    """
    return 'do some magic!'


def post_reserva(Reserva):
    """
    Añade una reserva
    Añade un nueva reserva
    :param Reserva: La reserva que se va a añadir, en el medio.
    :type Reserva: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Reserva = Reserva.from_dict(connexion.request.get_json())
    return 'do some magic!'


def remove_reserva(idReserva):
    """
    Eliminar la reserva
    Elimina la reserva que se le pasa como codigo de la universidad
    :param idReserva: Codigo de la reserva
    :type idReserva: int

    :rtype: Reserva
    """
    return 'do some magic!'


def reserva_cod_reserva_get(codReserva):
    """
    Obtienes una asignatura a partir de su código
    Devuelve un objeto del tipo reserva con todos sus datos, a partir del código del grado.
    :param codReserva: Codigo de la reserva
    :type codReserva: int

    :rtype: Reserva
    """
    return 'do some magic!'


def update_reserva(Reserva):
    """
    Actualizar los datos de una reserva.
    Actualiza los datos de una reserva
    :param Reserva: Reserva a Actualizar
    :type Reserva: dict | bytes

    :rtype: Reserva
    """
    if connexion.request.is_json:
        Reserva = Reserva.from_dict(connexion.request.get_json())
    return 'do some magic!'
