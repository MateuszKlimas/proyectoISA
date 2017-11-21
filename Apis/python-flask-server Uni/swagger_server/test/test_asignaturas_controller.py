# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturasController(BaseTestCase):
    """ AsignaturasController integration test stubs """

    def test_asignatura_id_asignatura_get(self):
        """
        Test case for asignatura_id_asignatura_get

        Obtienes una asignatura a partir de su código
        """
        response = self.client.open('/Universidad/asignatura/{idAsignatura}'.format(idAsignatura=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_asignaturas(self):
        """
        Test case for get_asignaturas

        Obtiene un listado de todas las asignaturas de la Base de datos
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Universidad/asignatura',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_asignatura(self):
        """
        Test case for post_asignatura

        Añadir una asignatura a nuestra Base de datos.
        """
        asignatura = Asignatura()
        response = self.client.open('/Universidad/asignatura',
                                    method='POST',
                                    data=json.dumps(asignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
