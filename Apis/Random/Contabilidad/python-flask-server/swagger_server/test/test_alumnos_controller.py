# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumnos import Alumnos
from swagger_server.models.profesores import Profesores
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_add_ingreso_alumno(self):
        """
        Test case for add_ingreso_alumno

        Añade un nuevo ingreso de un alumno
        """
        salarioProfesores = Alumnos()
        response = self.client.open('/miAplicacionContbilidad/alumnos',
                                    method='POST',
                                    data=json.dumps(salarioProfesores),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_ingreso_alumno(self):
        """
        Test case for find_ingreso_alumno

        Devuelve los ingresos de un alumno a partir de su ID.
        """
        query_string = [('status', 'available')]
        response = self.client.open('/miAplicacionContbilidad/alumnos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_ingreso_alumno(self):
        """
        Test case for update_ingreso_alumno

        Actualiza el ingreso de un alumno
        """
        body = Profesores()
        response = self.client.open('/miAplicacionContbilidad/alumnos',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
