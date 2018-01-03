import connexion
import psycopg2 
import json
import pprint
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.asignatura_cod_grado import AsignaturaCodGrado
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def asignatura_id_asignatura_get(idAsignatura):
    """
    Obtienes una asignatura a partir de su código
    Devuelve un objeto del tipo asignatura con todos sus datos, a partir del código del grado.
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Asignatura
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	# print the connection string we will use to connect
    print ("Connecting to database\n")
	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
	# execute our Query
    query = "SELECT * FROM \"asignatura\" WHERE id_asignatura="+str(idAsignatura)+";"
    cursor.execute(query)
	# retrieve the records from the database
    records = cursor.fetchall()
    cadena = records
    query = "SELECT * FROM \"grado_asignatura\" WHERE id_asignatura="+str(idAsignatura)+";"
    cursor.execute(query)
    records = cursor.fetchall()
    query = "SELECT * FROM \"asignatura\" WHERE id_asignatura="+str(idAsignatura)+";"
    cursor.execute(query)
    records2 = cursor.fetchall()
    query = "SELECT * FROM \"grado\" WHERE id_grado="+str(records[0][4])+";"
    cursor.execute(query)
    records3 = cursor.fetchall()
    json1 = {
        "idAsignatura" : records[0][5],
        "idGrado" : records[0][4],
        "creditosAsignaturas" : records[0][1],
        "turnoAsignatura" : records[0][3],
        "nombreAsignatura" : records2[0][1],
        "nombreGrado" : records3[0][1]
    }
    conn.close()
	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
    return json1
def gradoasignatura_id_grado_asignatura_get(idGradoAsignatura):
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	# print the connection string we will use to connect
    print ("Connecting to database\n")
	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
	# execute our Query
    query = "SELECT * FROM \"grado_asignatura\" WHERE \"id_gradoAsignatura\"="+str(idGradoAsignatura)+";"
    cursor.execute(query)
    records = cursor.fetchall()
    json1 = {
        "idAsignatura" : records[0][5],
        "idGrado" : records[0][4],
        "idGradoAsignatura" : records[0][0],
        "creditosAsignaturas" : records[0][1],
        "turnoAsignatura" : records[0][3],
    }
    return json1
def get_asignaturas(tamanoPagina, numeroPaginas):
    """
    Obtiene un listado de todas las asignaturas de la Base de datos
    Devuelve una lista con las asignaturas.
    :param tamanoPagina: Número de grados devueltos
    :type tamanoPagina: int
    :param numeroPaginas: Número de páginas devueltos
    :type numeroPaginas: int

    :rtype: List[Asignatura]
    """
    jsons = []
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	    # print the connection string we will use to connect
    print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
        # execute our Query
    query = "Select * from \"grado_asignatura\";"
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return jsons


def post_asignatura(asignatura):
    """
    Añadir una asignatura a nuestra Base de datos.
    Añade una asignatura a nuestra base de datos.
    :param asignatura: La asignatura que se va a añadir, en el grado especificado.
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = AsignaturaCodGrado.from_dict(connexion.request.get_json())
        conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	    # print the connection string we will use to connect
        print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        # execute our Query
        query = "Insert Into \"asignatura\" Values ( "+str(asignatura.id_asignatura)+",'"+str(asignatura.nombre)+"','hola');"
        cursor.execute(query)
        conn.commit()
        query = "Insert Into \"grado_asignatura\" Values ( "+str(asignatura.id_asignatura+2*asignatura.cod_grado)+",'"+str(asignatura.num_creditos)+"','"+str(asignatura.tipo_asignatura)+"','Mañana',"+str(asignatura.cod_grado)+","+str(asignatura.id_asignatura)+");"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return json.dumps("TodoCorrecto")


def remove_asignatura(idAsignatura):
    """
    Eliminar la asignatura
    Elimina la asignatura que se le pasa como codigo de la universidad
    :param idAsignatura: Codigo de la asignatura
    :type idAsignatura: int

    :rtype: Asignatura
    """
    conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	    # print the connection string we will use to connect
    print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
        # execute our Query
    query = "DELETE FROM \"grado_asignatura\" where id_asignatura="+str(idAsignatura)+";"
    cursor.execute(query)
    conn.commit()
    query = "DELETE  from \"asignatura\" where id_asignatura="+str(idAsignatura)+";"
    cursor.execute(query)
    conn.commit()
    conn.close()

    return json.dumps("Eliminacion correcta")


def update_asignatura(asignatura):
    """
    Actualizar los datos de una asignatura
    Actualiza los datos de la asignatura
    :param asignatura: Codigo de la asignatura
    :type asignatura: dict | bytes

    :rtype: Asignatura
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
        conn_string = "host='localhost' dbname='Centros' user='ISA' password='1234'"
	    # print the connection string we will use to connect
        print ("Connecting to database\n")
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        # execute our Query
        query = "UPDATE \"asignatura\" SET \"nombreAsignatura\"='"+ str(asignatura.nombre) + "',\"descripcionAsignatura\"='HOLA' WHERE id_asignatura="+ str(asignatura.id_asignatura)+";"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return json.dumps("TodoCorrecto")
    return 'do some magic!'
