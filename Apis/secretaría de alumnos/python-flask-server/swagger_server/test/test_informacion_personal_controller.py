# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from swagger_server.models.creditos import Creditos
from swagger_server.models.nota import Nota
from swagger_server.models.pago import Pago
from swagger_server.models.resumen_pagos import ResumenPagos
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestInformacionPersonalController(BaseTestCase):
    """ InformacionPersonalController integration test stubs """

    def test_consultar_creditos_reconocidos(self):
        """
        Test case for consultar_creditos_reconocidos

        creditos convalidados
        """
        query_string = [('id_alumno', 'id_alumno_example')]
        response = self.client.open('/secretaria-alumnos/creditos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_consultar_info(self):
        """
        Test case for consultar_info

        Consulta información personal de un alumno
        """
        query_string = [('id_alumno', 'id_alumno_example')]
        response = self.client.open('/secretaria-alumnos/info',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_consultar_notas(self):
        """
        Test case for consultar_notas

        consulta las notas
        """
        query_string = [('id_alumno', 'id_alumno_example')]
        response = self.client.open('/secretaria-alumnos/notas',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_consultar_pagos(self):
        """
        Test case for consultar_pagos

        Consuta informacion económica de la matrícula
        """
        query_string = [('id_alumno', 'id_alumno_example')]
        response = self.client.open('/secretaria-alumnos/cobros',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_pago(self):
        """
        Test case for find_pago

        Devuelve un recibo
        """
        query_string = [('id_usuario', 'id_usuario_example'),
                        ('mes', 56)]
        response = self.client.open('/secretaria-alumnos/findpago',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
