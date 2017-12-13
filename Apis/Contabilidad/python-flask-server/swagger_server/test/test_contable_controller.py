# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.contable import Contable
from swagger_server.models.nomina_contable import NominaContable
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestContableController(BaseTestCase):
    """ ContableController integration test stubs """

    def test_add_contable(self):
        """
        Test case for add_contable

        Añade un nuevo contable
        """
        contable = Contable()
        response = self.client.open('/miAplicacionContbilidad/contable',
                                    method='POST',
                                    data=json.dumps(contable),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_add_salario_contable(self):
        """
        Test case for add_salario_contable

        Añade un nueva nomina a un pas
        """
        query_string = [('nominaContable', 56)]
        response = self.client.open('/miAplicacionContbilidad/nomina_contable',
                                    method='POST',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_contableby_id(self):
        """
        Test case for find_contableby_id

        Devuelve el salario de un contable a partir de su codigo de identificacion.
        """
        query_string = [('id_contable', 56)]
        response = self.client.open('/miAplicacionContbilidad/contable',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_nomina_contableby_id(self):
        """
        Test case for find_nomina_contableby_id

        Devuelve el salario de un contable a partir de su codigo de identificacion.
        """
        query_string = [('id_contable', 56)]
        response = self.client.open('/miAplicacionContbilidad/nomina_contable',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
