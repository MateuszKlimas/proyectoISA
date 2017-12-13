# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.medios_fisicos import MediosFisicos
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMediosFisicosController(BaseTestCase):
    """ MediosFisicosController integration test stubs """

    def test_add_ingreso_medio_fisico(self):
        """
        Test case for add_ingreso_medio_fisico

        Añade un nuevo ingreso para un medio fisico
        """
        ingresoMedioFisico = MediosFisicos()
        response = self.client.open('/miAplicacionContbilidad/MediosFisicos',
                                    method='POST',
                                    data=json.dumps(ingresoMedioFisico),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_disponibilidad_id_medio_fisico(self):
        """
        Test case for find_disponibilidad_id_medio_fisico

        Devuelve la disponibilidad a partir de una fecha introducida.
        """
        query_string = [('status', 'available')]
        response = self.client.open('/miAplicacionContbilidad/MediosFisicos/disponibilidad',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_id_medio_fisico(self):
        """
        Test case for find_id_medio_fisico

        Devuelve el precio de un medio fisico a partir de su ID.
        """
        query_string = [('status', 'available')]
        response = self.client.open('/miAplicacionContbilidad/MediosFisicos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_ingreso_medio_fisico(self):
        """
        Test case for update_ingreso_medio_fisico

        Actualiza el ingreso para un medio fisico
        """
        body = MediosFisicos()
        response = self.client.open('/miAplicacionContbilidad/MediosFisicos',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
