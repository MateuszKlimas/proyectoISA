import connexion
from swagger_server.models.alumno import Alumno
from swagger_server.models.creditos import Creditos
from swagger_server.models.nota import Nota
from swagger_server.models.pago import Pago
from swagger_server.models.resumen_pagos import ResumenPagos
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import psycopg2


def consultar_creditos_reconocidos(id_alumno):
    """
    creditos convalidados
    muestra una lista de los creditos convalidados del alimno asi como la asignatura a la que pertenecen
    :param id_alumno: id del usuario
    :type id_alumno: str

    :rtype: List[Creditos]
    """
    return 'do some magic!'


def consultar_info(id_alumno):
    """
    Consulta información personal de un alumno
    Devuelve un json con la información personal de un alumno
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: Alumno
    """
    return 'do some magic!'


def consultar_notas(id_alumno):
    """
    consulta las notas
    Consulta las notas de todas las asignaturas matriculadas, así como otra información relacionada con las notas de la asignatura, como el número de créditos de la asignatura etc.
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: List[Nota]
    """
    return 'do some magic!'


def consultar_pagos(id_alumno):
    """
    Consuta informacion económica de la matrícula
    Consulta el importe total de la matrícula y el importe de los pagos a plazos
    :param id_alumno: id del alumno
    :type id_alumno: str

    :rtype: ResumenPagos
    """
    return 'do some magic!'


def find_pago(id_usuario, mes):
    """
    Devuelve un recibo
    Devuelve el recibo del mes que se especifique en la llamada
    :param id_usuario: id del usuario
    :type id_usuario: str
    :param mes: mes correspondiente al pago buscado
    :type mes: int

    :rtype: Pago
    """
    return 'do some magic!'
def grado_alumno(id_grado):
    conn_string = "host='localhost' dbname='SecretariaDeAlumnos' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # execute our Query
    cursor.execute("SELECT \"dniAlumno\",\"nombreAlumno\",\"apellidosAlumno\" FROM alumno WHERE id_grado = "+str(id_grado))
    records = cursor.fetchall();
    json1 = {
        "dniAlumno": records[0][0],
        "nombreAlumno": records[0][1],
        "apellidosAlumno": records[0][2]
    }
    conn.close()
    return json1
