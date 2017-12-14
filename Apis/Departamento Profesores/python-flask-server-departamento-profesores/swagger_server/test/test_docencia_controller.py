# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.docencia import Docencia
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDocenciaController(BaseTestCase):
    """ DocenciaController integration test stubs """

    def test_agregar_docencia(self):
        """
        Test case for agregar_docencia

        Agrega una relacion de un profesor con una asignatura
        """
        docencia = Docencia()
        response = self.client.open('/DepartamentoProfesores/agregarDocencia',
                                    method='POST',
                                    data=json.dumps(docencia),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_busqueda_docencia(self):
        """
        Test case for busqueda_docencia

        Devuelve relacion de profesor con asignaturas
        """
        query_string = [('id_profesor', 56),
                        ('id_asignaturaGrado', 56)]
        response = self.client.open('/DepartamentoProfesores/mostrarDocencia',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
