import connexion
import psycopg2
import json
from swagger_server.models.ingreso import IngresoAlumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

def add_ingreso(pago_Matricula):
	"""
	Añade un nuevo ingreso en pagoMatriculaAlumno
    """

	if connexion.request.is_json:
    	pago_Matricula = IngresoAlumno.from_dict(connexion.request.get_json())
    
    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    pago = pago_Matricula
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"pagoMatriculaAlumno\" VALUES (" + repr(pago.id_PagoMatriculaAlumno) + "," + "'" + repr(pago.fechaPagoMatriculaAlumno) + "'" + "," + repr(pago.importeMatriculaAlumno) + "," + repr(pago.pagoMatriculaAlumnoRealizado) + "," + repr(pago.id_departamentoContable) + "," + repr(pago.id_alumno) + ");")    
    conn.commit()
    conn.close()
    return "" 


def get_ingreso_id(id_pago_matricula):
	"""
	Permite buscar ingresos por id_PagoMatriculaAlumno
 	"""

	conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"pagoMatriculaAlumno\" WHERE \"pagoMatriculaAlumno\".\"id_PagoMatriculaAlumno\" = " + str(id_pago_matricula) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)

def get_ingreso_alumno(id_Alum):
	"""
	Permite buscar ingresps por id_alumno
	"""

	conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"pagoMatriculaAlumno\" WHERE \"pagoMatriculaAlumno\".\"id_alumno\" = " + str(id_Alum) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)

def get_ingreso_dep(id_dep_cont):
	"""
	Permite buscar ingresos por id_departamentoContable
	"""

	conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("SELECT * FROM \"pagoMatriculaAlumno\" WHERE \"pagoMatriculaAlumno\".\"id_departamentoContable\" = " + str(id_dep_cont) + ";")

    # retrieve the records from the database
    records = cursor.fetchall()
    conn.close()
    return json.dumps(records)

def actualizar_ingreso(pago_Matricula):

    if connexion.request.is_json:
        pago_Matricula = IngresoAlumno.from_dict(connexion.request.get_json())

    conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    pago = pago_Matricula
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("UPDATE \"pagoMatriculaAlumno\" SET \"pagoMatriculaAlumno\".\"id_PagoMatriculaAlumno\" = " + repr(pago.id_PagoMatriculaAlumno) + ", \"pagoMatriculaAlumno\".\"fechaPagoMatriculaAlumno\" = '" + repr(pago.fechaPagoMatriculaAlumno) "', \"pagoMatriculaAlumno\".\"importeMatriculaAlumno\" = " + repr(pago.importeMatriculaAlumno) + ", \"pagoMatriculaAlumno\".\"pagoMatriculaAlumnoRealizado\" = " + repr(pago.pagoMatriculaAlumnoRealizado) + "," + "\"pagoMatriculaAlumno\".\"id_departamentoContable\" = " + repr(pago.id_departamentoContable) + ", \"pagoMatriculaAlumno\".\"id_alumno\" = " + repr(pago.id_alumno) + " WHERE id_PagoMatriculaAlumno = " + repr(pago.id_PagoMatriculaAlumno) + ";")    
    conn.commit()
    conn.close()
    return ""

def eliminar_ingreso(id_pago_matricula):

 	conn_string = "host='localhost' dbname='DepartamentoContable' user='ISA' password='1234'"
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute("DELETE FROM \"pagoMatriculaAlumno\" where \"pagoMatriculaAlumno\".\"id_PagoMatriculaAlumno\" = " + str(id_pago_matricula) + ";")
    conn.commit()
    conn.close()
    return "" 
