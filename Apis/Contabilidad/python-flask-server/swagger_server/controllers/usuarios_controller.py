import connexion
from swagger_server.models.usuario import Usuario
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

# My imports:


DB = {}

def crear_usuario(usuario):
    """
    Crea un usuario
    Añade un usuario a la lista de usuarios.
    :param usuario: El usuario que se va a añadir.
    :type usuario: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        #print("Convirtiendo usuario")
        usuario = Usuario.from_dict(connexion.request.get_json())
    #print(usuario.first_name)
    #print(dir(usuario))
    #TODO Check the username does not exist.
    DB[usuario.username] = usuario
    return 'Usuario {} creado'.format(usuario.username)


def obtener_usuario(tamanoPagina=None, numeroPaginas=None):
    """
    Obtiene usuarios
    Obtiene un listado de usuarios del sistema.
    :param tamanoPagina: Número de personas devueltas
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Usuario]
    """

    return [user for _, user in DB.items()]


def usuario_username_get(username):
    """
    Devuelve un usuario
    Devuelve un único usuario identificado por su nombre de usuario
    :param username: Nombre de usuario del usuario
    :type username: str

    :rtype: Usuario
    """
    return DB[username]
