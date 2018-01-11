# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.profesores import Profesores
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesoresController(BaseTestCase):
    """ ProfesoresController integration test stubs """

    def test_add_salario(self):
        """
        Test case for add_salario

        Añade un nuevo salario
        """
        salario_contable = Profesores()
        response = self.client.open('/miAplicacionContbilidad/nomina_profesores',
                                    method='POST',
                                    data=json.dumps(salario_contable),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_profesorby_id(self):
        """
        Test case for find_profesorby_id

        Devuelve el salario de un profesor a partir de su codigo de identificacion.
        """
        query_string = [('id_profesor', 56)]
        response = self.client.open('/miAplicacionContbilidad/nomina_profesores',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
