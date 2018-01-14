import connexion
from swagger_server.models.departamento import Departamento
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def busqueda_departamento(id_departamento):
    """
    Muestra los datos de un departamento a partir de un id de departamento
    
    :param id_departamento: id del departamento
    :type id_departamento: int

    :rtype: Departamento
    """
    return 'do some magic!'


def crear_departamento(departamento):
    """
    Registrar un nuevo departamento
    
    :param departamento: 
    :type departamento: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento = Departamento.from_dict(connexion.request.get_json())
    return 'do some magic!'
