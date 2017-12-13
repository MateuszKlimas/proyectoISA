# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.person import Person
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_persons_get(self):
        """
        Test case for persons_get

        Gets some persons
        """
        query_string = [('pageSize', 56),
                        ('pageNumber', 56)]
        response = self.client.open('/openapi101/persons',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_persons_username_get(self):
        """
        Test case for persons_username_get

        Gets a person
        """
        response = self.client.open('/openapi101/persons/{username}'.format(username='username_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_persons_username_post(self):
        """
        Test case for persons_username_post

        Creates a person
        """
        person = Person()
        response = self.client.open('/openapi101/persons/{username}',
                                    method='POST',
                                    data=json.dumps(person),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
