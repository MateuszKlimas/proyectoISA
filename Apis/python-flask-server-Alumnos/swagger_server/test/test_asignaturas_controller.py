# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.creditos import Creditos
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturasController(BaseTestCase):
    """ AsignaturasController integration test stubs """

    def test_consultar_creditos_asignatura(self):
        """
        Test case for consultar_creditos_asignatura

        creditos de cada asignatura
        """
        query_string = [('nombre_asignatura', 'nombre_asignatura_example')]
        response = self.client.open('/alumnos/creditosasignatura',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
