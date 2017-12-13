# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Asignatura(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, nombre: str=None, codigo_asignatura: int=None, turno: str=None):
        """
        Asignatura - a model defined in Swagger

        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        :param codigo_asignatura: The codigo_asignatura of this Asignatura.
        :type codigo_asignatura: int
        :param turno: The turno of this Asignatura.
        :type turno: str
        """
        self.swagger_types = {
            'nombre': str,
            'codigo_asignatura': int,
            'turno': str
        }

        self.attribute_map = {
            'nombre': 'nombre',
            'codigo_asignatura': 'codigo_asignatura',
            'turno': 'turno'
        }

        self._nombre = nombre
        self._codigo_asignatura = codigo_asignatura
        self._turno = turno

    @classmethod
    def from_dict(cls, dikt) -> 'Asignatura':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Asignatura of this Asignatura.
        :rtype: Asignatura
        """
        return deserialize_model(dikt, cls)

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Asignatura.

        :return: The nombre of this Asignatura.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Asignatura.

        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def codigo_asignatura(self) -> int:
        """
        Gets the codigo_asignatura of this Asignatura.

        :return: The codigo_asignatura of this Asignatura.
        :rtype: int
        """
        return self._codigo_asignatura

    @codigo_asignatura.setter
    def codigo_asignatura(self, codigo_asignatura: int):
        """
        Sets the codigo_asignatura of this Asignatura.

        :param codigo_asignatura: The codigo_asignatura of this Asignatura.
        :type codigo_asignatura: int
        """

        self._codigo_asignatura = codigo_asignatura

    @property
    def turno(self) -> str:
        """
        Gets the turno of this Asignatura.

        :return: The turno of this Asignatura.
        :rtype: str
        """
        return self._turno

    @turno.setter
    def turno(self, turno: str):
        """
        Sets the turno of this Asignatura.

        :param turno: The turno of this Asignatura.
        :type turno: str
        """

        self._turno = turno
