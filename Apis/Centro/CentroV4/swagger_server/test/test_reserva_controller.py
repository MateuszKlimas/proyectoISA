# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.reserva import Reserva
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestReservaController(BaseTestCase):
    """ ReservaController integration test stubs """

    def test_obtener_reserva(self):
        """
        Test case for obtener_reserva

        Obtiene las reservas que se tienen
        """
        query_string = [('tamanoPagina', 56),
                        ('numeroPaginas', 56)]
        response = self.client.open('/Facultad/Reserva',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_reserva(self):
        """
        Test case for post_reserva

        Añade una reserva
        """
        reserva = Reserva()
        response = self.client.open('/Facultad/Reserva',
                                    method='POST',
                                    data=json.dumps(reserva),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_remove_reserva(self):
        """
        Test case for remove_reserva

        Eliminar la reserva
        """
        query_string = [('idReserva', 56)]
        response = self.client.open('/Facultad/Reserva',
                                    method='DELETE',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_reserva_cod_reserva_get(self):
        """
        Test case for reserva_cod_reserva_get

        Obtienes una asignatura a partir de su código
        """
        response = self.client.open('/Facultad/Reserva/{codReserva}'.format(codReserva=56),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_reserva(self):
        """
        Test case for update_reserva

        Actualizar los datos de una reserva.
        """
        reserva = Reserva()
        response = self.client.open('/Facultad/Reserva',
                                    method='PUT',
                                    data=json.dumps(reserva),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
