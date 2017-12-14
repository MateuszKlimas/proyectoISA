import connexion
from swagger_server.models.docencia import Docencia
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def agregar_docencia(docencia):
    """
    Agrega una relacion de un profesor con una asignatura
    
    :param docencia: 
    :type docencia: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        docencia = Docencia.from_dict(connexion.request.get_json())
    return 'do some magic!'


def busqueda_docencia(id_profesor, id_asignaturaGrado):
    """
    Devuelve relacion de profesor con asignaturas
    
    :param id_profesor: id del profesor
    :type id_profesor: int
    :param id_asignaturaGrado: id de la asignatura de un grado
    :type id_asignaturaGrado: int

    :rtype: Docencia
    """
    return 'do some magic!'
