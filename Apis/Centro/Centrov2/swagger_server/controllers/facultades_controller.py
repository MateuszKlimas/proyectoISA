import connexion
from swagger_server.models.universidad import Universidad
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_facultad(facultad):
    """
    Crea una facultad
    Añade una universidad a la lista de universidades.
    :param facultad: La facultad que se va a añadir.
    :type facultad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        facultad = Universidad.from_dict(connexion.request.get_json())
    return 'do some magic!'


def obtener_facultad(tamanoPagina, numeroPaginas):
    """
    Obtiene facultades
    Obtiene un listado de las universidades del sistema.
    :param tamanoPagina: Número de univesidades devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Universidad]
    """
    return 'do some magic!'


def remove_facultad(idAsignatura):
    """
    Eliminar la asignatura
    Elimina la asignatura que se le pasa como codigo de la universidad
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Universidad
    """
    return 'do some magic!'


def universidad_get_uni(codUni):
    """
    Devuelve una universidad a partir de su código
    Devuelve una única universidad identificada por su codigo de universidad
    :param codUni: Codigo de la universidad
    :type codUni: int

    :rtype: Universidad
    """
    return 'do some magic!'


def update_facultad(universidad):
    """
    Actualizar facultad
    Permite la actualización de los datos de la facultad.
    :param universidad: La universidad que se va a actualizar
    :type universidad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        universidad = Universidad.from_dict(connexion.request.get_json())
    return 'do some magic!'
