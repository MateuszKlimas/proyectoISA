# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.universidad import Universidad
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUniversidadesController(BaseTestCase):
    """ UniversidadesController integration test stubs """

    def test_crear_universidad(self):
        """
        Test case for crear_universidad

        Crea una universidad
        """
        universidad = Universidad()
        response = self.client.open('/Universidad/universidad',
                                    method='POST',
                                    data=json.dumps(universidad),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_universidad(self):
        """
        Test case for obtener_universidad

        Obtiene universidades
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Universidad/universidad',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_universidad_get_uni(self):
        """
        Test case for universidad_get_uni

        Devuelve una universidad a partir de su código
        """
        response = self.client.open('/Universidad/universidad/{codUni}'.format(codUni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
