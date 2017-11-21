# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.grado import Grado
from swagger_server.models.universidad import Universidad
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGradosController(BaseTestCase):
    """ GradosController integration test stubs """

    def test_get_grados(self):
        """
        Test case for get_grados

        Obtiene una lista de todos los grados del sistema.
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Universidad/grado',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_grado_cod_grado_get(self):
        """
        Test case for grado_cod_grado_get

        Obtienes un grado a partir de su código
        """
        response = self.client.open('/Universidad/grado/{codGrado}'.format(codGrado=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_grado(self):
        """
        Test case for post_grado

        Añade un grado a la base de datos.
        """
        grado = Grado()
        response = self.client.open('/Universidad/grado',
                                    method='POST',
                                    data=json.dumps(grado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
