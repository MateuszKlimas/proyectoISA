import connexion
from swagger_server.models.departamento import Departamento
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def agregar_profesor(profesor):
    """
    Agrega un profesor a la base de datos
    
    :param profesor: 
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    return 'do some magic!'


def busqueda_profesor(id_profesor):
    """
    Muestra un profesor a partir de un id de profesor
    
    :param id_profesor: id del profesor
    :type id_profesor: int

    :rtype: Departamento
    """
    return 'do some magic!'
