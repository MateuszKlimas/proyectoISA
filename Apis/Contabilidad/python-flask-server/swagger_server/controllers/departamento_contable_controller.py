import connexion
from swagger_server.models.departamento_contable import DepartamentoContable
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_departamento_contable(departamento_contable):
    """
    Añade un nuevo departamento contable
    Añade un nuevo ingreso de matricula
    :param departamento_contable: Se va añadir un nuevo departamento contable
    :type departamento_contable: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento_contable = DepartamentoContable.from_dict(connexion.request.get_json())
    return 'do some magic!'


def find_departamento_contable(id_departamento_contable):
    """
    Devuelve el departamento contable
    Devuelve el departamento contable
    :param id_departamento_contable: id del departamento contable
    :type id_departamento_contable: int

    :rtype: List[DepartamentoContable]
    """
    return 'do some magic!'
