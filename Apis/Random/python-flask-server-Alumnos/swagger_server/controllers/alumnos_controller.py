import connexion
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_alumno(alumno):
    """
    Registrar alumno
    
    :param alumno: 
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    return 'do some magic!'


def login_alumno(nombre_usuario, contrasea):
    """
    Login
    
    :param nombre_usuario: nombre del usuario
    :type nombre_usuario: str
    :param contrasea: contraseña del usuario
    :type contrasea: str

    :rtype: None
    """
    return 'do some magic!'


def logout_alumno():
    """
    Logout
    

    :rtype: None
    """
    return 'do some magic!'
