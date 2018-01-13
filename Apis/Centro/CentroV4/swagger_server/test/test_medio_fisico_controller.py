# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.medio_fisico_centro import MedioFisicoCentro
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMedioFisicoController(BaseTestCase):
    """ MedioFisicoController integration test stubs """

    def test_medio_fisico_id_centro_get(self):
        """
        Test case for medio_fisico_id_centro_get

        Obtienes una asignatura a partir de su código
        """
        response = self.client.open('/Facultad/MedioFisico/{idCentro}'.format(idCentro=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_medios(self):
        """
        Test case for obtener_medios

        Obtiene los medios Fisicos que se tienen
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Facultad/MedioFisico',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_medio(self):
        """
        Test case for post_medio

        Añade un medio fisico
        """
        medioFisico = MedioFisicoCentro()
        response = self.client.open('/Facultad/MedioFisico',
                                    method='POST',
                                    data=json.dumps(medioFisico),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_medio(self):
        """
        Test case for remove_medio

        Eliminar el medio
        """
        query_string = [('idMedio', 56)]
        response = self.client.open('/Facultad/MedioFisico',
                                    method='DELETE',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_medio(self):
        """
        Test case for update_medio

        Actualizar los datos de un medio fisico
        """
        Medio = MedioFisicoCentro()
        response = self.client.open('/Facultad/MedioFisico',
                                    method='PUT',
                                    data=json.dumps(Medio),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
