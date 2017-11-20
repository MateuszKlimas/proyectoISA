# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.pas import PAS
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPASController(BaseTestCase):
    """ PASController integration test stubs """

    def test_add_salario_pas(self):
        """
        Test case for add_salario_pas

        Añade un nuevo salario de un PAS
        """
        salarioPAS = PAS()
        response = self.client.open('/miAplicacionContbilidad/pas',
                                    method='POST',
                                    data=json.dumps(salarioPAS),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_pa_sby_id(self):
        """
        Test case for find_pa_sby_id

        Devuelve el salario de un PAS a partir de su codigo de identificacion.
        """
        query_string = [('status', 'available')]
        response = self.client.open('/miAplicacionContbilidad/pas',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_salario_pas(self):
        """
        Test case for update_salario_pas

        Actualiza el salario de un PAS
        """
        body = PAS()
        response = self.client.open('/miAplicacionContbilidad/pas',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
