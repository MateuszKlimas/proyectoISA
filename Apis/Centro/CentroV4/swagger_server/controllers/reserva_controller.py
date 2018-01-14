import connexion
import psycopg2
import sys
import pprint
import json
from swagger_server.models.reserva import Reserva
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def obtener_reserva(tamanoPagina, numeroPaginas):
    """
    Obtiene las reservas que se tienen
    Devuelve todos los medios fisicos.
    :param tamanoPagina: Número de medios devueltos
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltas
    :type numeroPaginas: int

    :rtype: List[Reserva]
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT id_reserva, \"titularReserva\", \"fechaReserva\",id_medio   FROM reserva")
 
    # retrieve the records from the database
    records = cursor.fetchall()
    json_list = []
    for i in range(len(records)):
        json = {
            'fecha_reserva:': records[0][2],
            #'hora_inicio_reserva': records[0][1],
            #'hora_fin_reserva:': records[0][2],
            'id_medio': records[0][3],
            'id_reserva': records[0][0],
            'titular_reserva': records[0][1]
        }
        json_list.append(json)
    conn.commit()    
    conn.close()
    return json_list


def post_reserva(reserva):
    """
    Añade una reserva
    Añade un nueva reserva
    :param Reserva: La reserva que se va a añadir, en el medio.
    :type Reserva: dict | bytes
    :rtype: None
    """

    if connexion.request.is_json:
        reserva = Reserva.from_dict(connexion.request.get_json())

    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    print("Connecting to database\n")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reserva VALUES (" + str(reserva.id_reserva) + ", '" + str(reserva.titular_reserva) + "', '" + str(reserva.hora_inicio) + "', '" + str(reserva.hora_fin) + "', '" + str(reserva.fecha_reserva) + "', " + str(reserva.id_medio) + ");")
    conn.commit()
    conn.close()
    return 'Reserva realizada con exito'

def post_asignacion(reserva):
    """
    Añade una reserva
    Añade un nueva reserva
    :param Reserva: La reserva que se va a añadir, en el medio.
    :type Reserva: dict | bytes
    :rtype: None
    """

    if connexion.request.is_json:
        reserva = Reserva.from_dict(connexion.request.get_json())

    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    print("Connecting to database\n")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reserva VALUES (" + str(reserva.id_reserva) + ", 'Aula Reservada Curso Entero Profesor: " + str(reserva.titular_reserva) + "', '00:00', '00:00', '01/01/2018', " + str(reserva.id_medio) + ");")
    conn.commit()
    conn.close()
    return 'Asignacion realizada con exito'


def remove_reserva(idReserva):
    """
    Eliminar la reserva
    Elimina la reserva que se le pasa como codigo de la universidad
    :param idReserva: Codigo de la reserva
    :type idReserva: int

    :rtype: Reserva
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("delete FROM reserva WHERE id_reserva="+str(idReserva))
    conn.commit()
    conn.close()
    return 'Eliminacion correcta de la reserva'


def reserva_cod_reserva_get(codReserva):
    """
    Obtienes una asignatura a partir de su código
    Devuelve un objeto del tipo reserva con todos sus datos, a partir del código del grado.
    :param codReserva: Codigo de la reserva
    :type codReserva: int

    :rtype: Reserva
    """
    if connexion.request.is_json:
        reserva = Reserva.from_dict(connexion.request.get_json())
    
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT \"titularReserva\", \"fechaReserva\",id_medio   FROM reserva WHERE id_reserva="+str(codReserva))
 
    # retrieve the records from the database
    records = cursor.fetchall()
    if len(records) == 0: 
        return 'El codigo de reserva no existe'
    else:
        
        json = {
            'fecha_reserva:': records[0][1],
            #'hora_inicio_reserva': records[0][1],
            #'hora_fin_reserva:': records[0][2],
            'id_medio': records[0][2],
            'id_reserva':codReserva,
            'titular_reserva': records[0][0]
            }
            
        conn.close()
        return json
        

def update_reserva(reserva):
    """
    Actualizar los datos de una reserva.
    Actualiza los datos de una reserva
    :param reserva: Reserva a Actualizar
    :type reserva: dict | bytes

    :rtype: Reserva
    """
    if connexion.request.is_json:
        reserva = Reserva.from_dict(connexion.request.get_json())
    
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("UPDATE reserva SET id_reserva = " + repr(reserva.id_reserva) + "," "\"titularReserva\" = " + "'" + reserva.titulae_reserva + "'" +
     ","+ "\"horaInicioReserva\" = " +  "'" + reserva.hora_inicio + "'" + ","+ "\"horaFinReserva\" = "+ "'" + reserva.hora_fin + "'" + ","+ "\"fechaReserva\" =" + "'" + reserva.fecha_reserva + "'" + "," 
     + " id_medio ="+ repr(reserva.id_medio) )
    conn.commit()
    conn.close()
    return 'Actualizacion realizada con exito'  
