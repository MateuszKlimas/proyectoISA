
import connexion
import requests
import psycopg2
import sys
import pprint
import json
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_alumno(alumno):
    """
    Registrar alumno
    
    :param alumno: 
    :type alumno: dict | bytes

    :rtype: None
    """
    nulo= 'null'
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)#Nos conectamos 
    cursor = conn.cursor()
    cursor.execute("SELECT id_alumno FROM public.alumno order by id_alumno desc;")
    records =cursor.fetchall()
    id_alumno=int(records[0][0]) + 1
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    
    cursor.execute("INSERT INTO alumno VALUES (" + str(id_alumno) +","+repr(alumno.dni)+ ","+ repr(alumno.nombre) + ","+  repr(alumno.apellido)
                   + ","+ repr(alumno.direccion) +","+ repr(alumno.correo)+","+ repr(alumno.telefono)+ ","+str(0)+ ")")
    conn.commit()
    texto= "Su id de alumno será --> "+ str(id_alumno)
    return texto
