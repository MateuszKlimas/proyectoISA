def consultar_notas(id_alumno):
    """
    consulta las notas
    Consulta las notas de todas las asignaturas matriculadas, así como otra información relacionada con las notas de la asignatura, como el número de créditos de la asignatura etc.
    :param id_alumno: id del alumno
    :type id_alumno: str
    :rtype: List[Nota]
    """
    conn_string = "host='localhost' dbname='SecretariaAlumnos' user='ISA' password='1234'"
    
 
    conn = psycopg2.connect(conn_string)#Nos conectamos 
 
    cursor = conn.cursor()
 
    cursor.execute("SELECT matriculacion.aprobado, matriculacion.\"id_gradoAsignatura\",matriculacion.\"numConvocatoria\",matriculacion.\"notaAlumno\" FROM matriculacion WHERE id_alumno="+str(id_alumno))
    json_list=[]
    records =cursor.fetchall()
 
    for i in range(len(records)):
        direccion= ('http://localhost:5003/Facultad/asignatura/'+ str(records[i][1]))
        solicitud = requests.get(direccion)
        json_solicitud = solicitud.json()
        json1 = {
        "Aprobado":records[i][0],
	"Nombre asignatura": json_solicitud['nombreAsignatura'],
        "Convocatoria":records[i][2],
        "Creditos": json_solicitud['creditosAsignaturas'],
        "Nota":records[i][3],
        "Tipo":json_solicitud['turnoAsignatura']
	}
        json_list.append(json1)
        
    return(json_list)
