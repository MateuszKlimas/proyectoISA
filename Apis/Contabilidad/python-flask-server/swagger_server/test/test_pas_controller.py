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

        Añade un nueva nomina a un pas
        """
        query_string = [('nominaPas', 56)]
        response = self.client.open('/miAplicacionContbilidad/nomina_pas',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_pasby_id(self):
        """
        Test case for find_pasby_id

        Devuelve el salario de un pas a partir de su codigo de identificacion.
        """
        query_string = [('id_profesor', 56)]
        response = self.client.open('/miAplicacionContbilidad/nomina_pas',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
