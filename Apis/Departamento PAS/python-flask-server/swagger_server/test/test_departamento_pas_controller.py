# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento_pas import DepartamentoPas
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoPASController(BaseTestCase):
    """ DepartamentoPASController integration test stubs """

    def test_busqueda_departamento_pas(self):
        """
        Test case for busqueda_departamento_pas

        Mostrar un deparatamento en concreto
        """
        query_string = [('idDepartamento', 56)]
        response = self.client.open('/Pas/departamento',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_insertar_departamento_pas(self):
        """
        Test case for insertar_departamento_pas

        Añadir un nuevo departamento
        """
        departamento = DepartamentoPas()
        response = self.client.open('/Pas/departamento',
                                    method='POST',
                                    data=json.dumps(departamento),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
