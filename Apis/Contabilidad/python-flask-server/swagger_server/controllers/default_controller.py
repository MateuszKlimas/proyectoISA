import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.person import Person
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def persons_get(pageSize=None, pageNumber=None):
    """
    Gets some persons
    Returns a list containing all persons.
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def persons_username_get(username):
    """
    Gets a person
    Returns a single person for its username
    :param username: The person&#39;s username
    :type username: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def persons_username_post(person=None):
    """
    Creates a person
    Adds a new person to the persons list.
    :param person: The person to create.
    :type person: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())
    return 'do some magic!'
