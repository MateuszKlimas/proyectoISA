import connexion
from swagger_server.models.contable import Contable
from swagger_server.models.nomina_contable import NominaContable
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_contable(contable):
    """
    Añade un nuevo contable
    Añades un nuevo contable.
    :param contable: Se va añadir un nuevo contable
    :type contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        contable = Contable.from_dict(connexion.request.get_json())
    return 'do some magic!'


def add_salario_contable(nominaContable):
    """
    Añade un nueva nomina a un pas
    Añades un nuevo salario a un contable.
    :param nominaContable: El salario que se va a añadir
    :type nominaContable: int

    :rtype: None
    """
    return 'do some magic!'


def find_contableby_id(id_contable):
    """
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    :param id_contable: id del contable a buscar su salario
    :type id_contable: int

    :rtype: List[Contable]
    """
    return 'do some magic!'


def find_nomina_contableby_id(id_contable):
    """
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    Devuelve el salario de un contable a partir de su codigo de identificacion.
    :param id_contable: id del contable a buscar su salario
    :type id_contable: int

    :rtype: List[NominaContable]
    """
    return 'do some magic!'
