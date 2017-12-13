# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura_matricula import AsignaturaMatricula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculaController(BaseTestCase):
    """ MatriculaController integration test stubs """

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
