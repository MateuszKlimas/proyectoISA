# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_add_matricula(self):
        """
        Test case for add_matricula

        Añade un nuevo ingreso de matricula
        """
        contable = Alumno()
        response = self.client.open('/miAplicacionContbilidad/matricula',
                                    method='POST',
                                    data=json.dumps(contable),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_matricula(self):
        """
        Test case for find_matricula

        Devuelve el ingreso de matricula de un alumno
        """
        query_string = [('id_alumno', 56)]
        response = self.client.open('/miAplicacionContbilidad/matricula',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
