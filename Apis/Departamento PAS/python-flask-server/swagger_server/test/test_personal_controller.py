# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.pas import Pas
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPersonalController(BaseTestCase):
    """ PersonalController integration test stubs """

    def test_busqueda_pas(self):
        """
        Test case for busqueda_pas

        Mostar un personal en concreto
        """
        query_string = [('idPas', 56)]
        response = self.client.open('/Pas/pas',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_insertar_pas(self):
        """
        Test case for insertar_pas

        Añadir un nuevo personal
        """
        pas = Pas()
        response = self.client.open('/Pas/pas',
                                    method='POST',
                                    data=json.dumps(pas),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
