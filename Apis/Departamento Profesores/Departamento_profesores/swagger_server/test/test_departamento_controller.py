# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento import Departamento
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoController(BaseTestCase):
    """ DepartamentoController integration test stubs """

    def test_busqueda_departamento(self):
        """
        Test case for busqueda_departamento

        Muestra los datos de un departamento a partir de un id de departamento
        """
        query_string = [('id_departamento', 56)]
        response = self.client.open('/DepartamentoProfesores/mostrarDepartamento',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_departamento(self):
        """
        Test case for crear_departamento

        Registrar un nuevo departamento
        """
        departamento = Departamento()
        response = self.client.open('/DepartamentoProfesores/crearDepartamento',
                                    method='POST',
                                    data=json.dumps(departamento),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
