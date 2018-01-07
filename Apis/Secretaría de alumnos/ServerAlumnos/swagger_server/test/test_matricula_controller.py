# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura_matricula import AsignaturaMatricula
from swagger_server.models.matricula_asignatura import MatriculaAsignatura
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculaController(BaseTestCase):
    """ MatriculaController integration test stubs """

    def test_cambiar_matricula(self):
        """
        Test case for cambiar_matricula

        Cambios en matricula
        """
        datos = AsignaturaMatricula()
        query_string = [('id_usuario', 'id_usuario_example')]
        response = self.client.open('/secretaria-alumnos/cambiarmatricula',
                                    method='PUT',
                                    data=json.dumps(datos),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_poner_nota(self):
        """
        Test case for poner_nota

        Pone la nota a un alumno con el id de matrícula
        """
        matriculaAsignatura = MatriculaAsignatura()
        response = self.client.open('/secretaria-alumnos/Notas',
                                    method='POST',
                                    data=json.dumps(matriculaAsignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_realizar_automatricula(self):
        """
        Test case for realizar_automatricula

        Automatricula
        """
        asignaturas = [AsignaturaMatricula()]
        query_string = [('id_usuario', 'id_usuario_example')]
        response = self.client.open('/secretaria-alumnos/matricula',
                                    method='POST',
                                    data=json.dumps(asignaturas),
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
