# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento_contable import DepartamentoContable
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoContableController(BaseTestCase):
    """ DepartamentoContableController integration test stubs """

    def test_add_departamento_contable(self):
        """
        Test case for add_departamento_contable

        Añade un nuevo departamento contable
        """
        departamento_contable = DepartamentoContable()
        response = self.client.open('/miAplicacionContbilidad/departamento_contable',
                                    method='POST',
                                    data=json.dumps(departamento_contable),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_find_departamento_contable(self):
        """
        Test case for find_departamento_contable

        Devuelve el departamento contable
        """
        query_string = [('id_departamento_contable', 56)]
        response = self.client.open('/miAplicacionContbilidad/departamento_contable',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
