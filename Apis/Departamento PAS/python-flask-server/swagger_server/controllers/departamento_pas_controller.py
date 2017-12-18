import connexion
from swagger_server.models.departamento_pas import DepartamentoPas
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def busqueda_departamento_pas(idDepartamento):
    """
    Mostrar un deparatamento en concreto
    Buscar un departamento dentro de la lista de departamentos del personal
    :param idDepartamento: Identificador del Departamento del Personal
    :type idDepartamento: int

    :rtype: DepartamentoPas
    """
    return 'do some magic!'


def insertar_departamento_pas(departamento):
    """
    Añadir un nuevo departamento
    Insertar un nuevo departamento en  lista de departamentos del personal
    :param departamento: 
    :type departamento: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento = DepartamentoPas.from_dict(connexion.request.get_json())
    return 'do some magic!'
