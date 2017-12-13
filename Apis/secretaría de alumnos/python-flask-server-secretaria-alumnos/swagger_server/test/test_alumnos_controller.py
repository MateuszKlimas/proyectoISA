# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_crear_alumno(self):
        """
        Test case for crear_alumno

        Registrar alumno
        """
        alumno = Alumno()
        response = self.client.open('/alumnos/crearcuenta',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_login_alumno(self):
        """
        Test case for login_alumno

        Login
        """
        query_string = [('nombre_usuario', 'nombre_usuario_example'),
                        ('contrasea', 'contrasea_example')]
        response = self.client.open('/alumnos/login',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_logout_alumno(self):
        """
        Test case for logout_alumno

        Logout
        """
        response = self.client.open('/alumnos/logout',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
