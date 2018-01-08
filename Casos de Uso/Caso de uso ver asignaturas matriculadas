def get_asignaturas_matriculadas(id_alumno):
    """
    Asignaturas matriculadas
    Devuelve una lista con las asignaturas en las que esta matriculado el alumno
    :param id_alumno: id del alumno
    :type id_alumno: str
    :rtype: List[Asignatura]
    """
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    conexion = psycopg2.connect(conn_string)
    cursor = conexion.cursor()
    cursor.execute("SELECT \"id_gradoAsignatura\" FROM matriculacion WHERE (id_alumno =" + repr(id_alumno) + ")")
    cursor_rows = cursor.fetchall()
    lista_json = []
    for i in range(len(records)):
        ip_puerto='localhost:5003'
        direccion= ('http://'+ip_puerto+'/Facultad/asignatura/'+ str(records[i][0]))
        solicitud = requests.get(direccion)
        json_solicitud = solicitud.json()
        json1 = {
            "Codigo_Asignatura":records[i][0],
            "Creditos": json_solicitud['creditosAsignaturas'],
            "NombreAsignatura": json_solicitud['nombreAsignatura'],
            "NombreGrado": json_solicitud['nombreGrado'],
            "TurnoAsignatura":json_solicitud['turnoAsignatura']
            }
        json_list.append(json1)
        
    return(json_list)
