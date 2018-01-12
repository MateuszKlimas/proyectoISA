# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.universidad import Universidad
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestFacultadesController(BaseTestCase):
    """ FacultadesController integration test stubs """

    def test_crear_facultad(self):
        """
        Test case for crear_facultad

        Crea una facultad
        """
        facultad = Universidad()
        response = self.client.open('/Facultad/facultad',
                                    method='POST',
                                    data=json.dumps(facultad),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_facultad(self):
        """
        Test case for obtener_facultad

        Obtiene facultades
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Facultad/facultad',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_facultad(self):
        """
        Test case for remove_facultad

        Eliminar la asignatura
        """
        query_string = [('idAsignatura', 56)]
        response = self.client.open('/Facultad/facultad',
                                    method='DELETE',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_universidad_get_uni(self):
        """
        Test case for universidad_get_uni

        Devuelve una universidad a partir de su código
        """
        response = self.client.open('/Facultad/facultad/{codUni}'.format(codUni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_facultad(self):
        """
        Test case for update_facultad

        Actualizar facultad
        """
        universidad = Universidad()
        response = self.client.open('/Facultad/facultad',
                                    method='PUT',
                                    data=json.dumps(universidad),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
