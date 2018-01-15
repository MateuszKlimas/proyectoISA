import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.creditos import Creditos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import psycopg2
import json
import requests


def consultar_creditos_asignatura(nombre_asignatura):
    """
    creditos de cada asignatura
    Permite consultar cuantos creditos tiene cada asigntura
    :param nombre_asignatura: nombre de la asignatura buscada
    :type nombre_asignatura: str

    :rtype: Creditos
    """
    return 'do some magic!'


def get_asignaturas_disponibles(id_alumno):
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    asignaturas = []
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()    
    cursor.execute("SELECT id_grado from alumno where id_alumno=" + id_alumno)
    records = cursor.fetchall()
    id_grado = records[0][0]
    response = requests.get('http://localhost:8082/Facultad/asignaturasGrado?idGrado=' + str(id_grado))
    json_data = json.loads(response.text)
    cursor.execute("SELECT \"id_gradoAsignatura\",aprobado from matriculacion where id_alumno=" + str(id_alumno))
    records = cursor.fetchall()

    aprobadas=[]
    for i in range(len(records)):
        if records[i][1]:
            aprobadas.append(records[i][0])
    print(aprobadas)

    for i in range(len(json_data)):
        json1 = json_data[i]
        if json1["idAsignatura"] not in aprobadas:
            asignaturas.append(json1)
    return asignaturas


def get_asignaturas_matriculadas(id_alumno):
    """
    Asignaturas matriculadas
    Devuelve una lista con las asignaturas en las que esta matriculado el alumno
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: List[Asignatura]
    """
    return 'do some magic!'
