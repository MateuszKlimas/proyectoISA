# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento import Departamento
from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_agregar_profesor(self):
        """
        Test case for agregar_profesor

        Agrega un profesor a la base de datos
        """
        profesor = Profesor()
        response = self.client.open('/DepartamentoProfesores/agregarProfesor',
                                    method='POST',
                                    data=json.dumps(profesor),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_busqueda_profesor(self):
        """
        Test case for busqueda_profesor

        Muestra un profesor a partir de un id de profesor
        """
        query_string = [('id_profesor', 56)]
        response = self.client.open('/DepartamentoProfesores/mostrarProfesor',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
