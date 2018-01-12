import connexion
from swagger_server.models.medio_fisico_centro import MedioFisicoCentro
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def medio_fisico_cod_medio_get(codMedio):
    """
    Obtienes una asignatura a partir de su código
    Devuelve un objeto del tipo asignatura con todos sus datos, a partir del código del grado.
    :param codMedio: Codigo de la asignatura
    :type codMedio: int

    :rtype: MedioFisicoCentro
    """
    return 'do some magic!'


def obtener_medios(tamanoPagina, numeroPaginas):
    """
    Obtiene los medios Fisicos que se tienen
    Devuelve todos los medios fisicos.
    :param tamanoPagina: Número de medios devueltos
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[MedioFisicoCentro]
    """
    return 'do some magic!'


def post_medio(medioFisico):
    """
    Añade un medio fisico
    Añade un nuevo medio fisico
    :param medioFisico: El medio que se va a añadir, en el centro especificado.
    :type medioFisico: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medioFisico = MedioFisicoCentro.from_dict(connexion.request.get_json())
    return 'do some magic!'


def remove_medio(idMedio):
    """
    Eliminar el medio
    Elimina el medio que se le pasa como codigo del medio
    :param idMedio: Codigo del medio
    :type idMedio: int

    :rtype: MedioFisicoCentro
    """
    return 'do some magic!'


def update_medio(Medio):
    """
    Actualizar los datos de un medio fisico
    Actualiza los datos de un medio fisico
    :param Medio: Medio a Actualizar
    :type Medio: dict | bytes

    :rtype: MedioFisicoCentro
    """
    if connexion.request.is_json:
        Medio = MedioFisicoCentro.from_dict(connexion.request.get_json())
    return 'do some magic!'
