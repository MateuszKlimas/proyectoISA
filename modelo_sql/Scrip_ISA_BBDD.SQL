-- Create tables section -------------------------------------------------

-- Table facultad

CREATE TABLE "facultad"(
 "id_facultad" Integer NOT NULL,
 "nombreFacultad" Text NOT NULL,
 "direccionFacultad" Text NOT NULL
)
;

-- Add keys for table facultad

ALTER TABLE "facultad" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_facultad")
;

ALTER TABLE "facultad" ADD CONSTRAINT "nombreFacultad" UNIQUE ("nombreFacultad")
;

-- Table medioFisico

CREATE TABLE "medioFisico"(
 "id_medio" Integer NOT NULL,
 "nombreMedioFisico" Text NOT NULL,
 "tipoMedioFisico" Text NOT NULL,
 "precioMedioFisico" Integer NOT NULL,
 "capacidadMedioFisico" Integer NOT NULL,
 "id_facultad" Integer
)
;

-- Create indexes for table medioFisico

CREATE INDEX "IX_Relationship1" ON "medioFisico" ("id_facultad")
;

-- Add keys for table medioFisico

ALTER TABLE "medioFisico" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_medio")
;

-- Table reservas

CREATE TABLE "reservas"(
 "id_reserva" Integer NOT NULL,
 "titularReserva" Text NOT NULL,
 "horaInicioReserva" Time NOT NULL,
 "horaFinReserva" Time NOT NULL,
 "fechaReserva" Date NOT NULL,
 "id_medio" Integer
)
;

-- Create indexes for table reservas

CREATE INDEX "IX_Relationship2" ON "reservas" ("id_medio")
;

-- Add keys for table reservas

ALTER TABLE "reservas" ADD CONSTRAINT "Key3" PRIMARY KEY ("id_reserva")
;

-- Table grado

CREATE TABLE "grado"(
 "id_grado" Integer NOT NULL,
 "nombreGrado" Text NOT NULL,
 "numCreditosObligatorios" Integer NOT NULL,
 "numCreditosTransversales" Integer NOT NULL,
 "numCreditosOptativos" Integer NOT NULL,
 "id_facultad" Integer
)
;

-- Create indexes for table grado

CREATE INDEX "IX_Relationship3" ON "grado" ("id_facultad")
;

-- Add keys for table grado

ALTER TABLE "grado" ADD CONSTRAINT "Key4" PRIMARY KEY ("id_grado")
;

-- Table grado_asignatura

CREATE TABLE "grado_asignatura"(
 "id_gradoAsignatura" Integer NOT NULL,
 "creditosAsignatura" Integer NOT NULL,
 "tipoAsignatura" Text NOT NULL,
 "id_grado" Integer,
 "id_asignatura" Integer
)
;

-- Create indexes for table grado_asignatura

CREATE INDEX "IX_Relationship4" ON "grado_asignatura" ("id_grado")
;

CREATE INDEX "IX_Relationship5" ON "grado_asignatura" ("id_asignatura")
;

-- Add keys for table grado_asignatura

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Key5" PRIMARY KEY ("id_gradoAsignatura")
;

-- Table alumno

CREATE TABLE "alumno"(
 "id_alumno" Integer NOT NULL,
 "dniAlumno" Text NOT NULL,
 "nombreAlumno" Text NOT NULL,
 "apellidosAlumno" Text NOT NULL,
 "direccionAlumno" Text NOT NULL,
 "correoAlumno" Text NOT NULL,
 "telefonoAlumno" Text NOT NULL
)
;

-- Add keys for table alumno

ALTER TABLE "alumno" ADD CONSTRAINT "Key6" PRIMARY KEY ("id_alumno")
;

-- Table asignatura

CREATE TABLE "asignatura"(
 "id_asignatura" Integer NOT NULL,
 "nombre" Text NOT NULL
)
;

-- Add keys for table asignatura

ALTER TABLE "asignatura" ADD CONSTRAINT "Key7" PRIMARY KEY ("id_asignatura")
;

-- Table matriculacion

CREATE TABLE "matriculacion"(
 "id_matriculacion" Integer NOT NULL,
 "numConvocatoria" Integer NOT NULL,
 "numMatricula" Integer NOT NULL,
 "id_alumno" Integer,
 "id_gradoAsignatura" Integer
)
;

-- Create indexes for table matriculacion

CREATE INDEX "IX_Relationship6" ON "matriculacion" ("id_alumno")
;

CREATE INDEX "IX_Relationship7" ON "matriculacion" ("id_gradoAsignatura")
;

-- Add keys for table matriculacion

ALTER TABLE "matriculacion" ADD CONSTRAINT "Key8" PRIMARY KEY ("id_matriculacion")
;

-- Table pagoMatricula

CREATE TABLE "pagoMatricula"(
 "id_pagoMatricula" Integer NOT NULL,
 "fechaPagoMatricula" Date NOT NULL,
 "importePagoMatricula" Integer NOT NULL,
 "estadoPagoMatricula" Boolean NOT NULL,
 "id_alumno" Integer
)
;

-- Create indexes for table pagoMatricula

CREATE INDEX "IX_Relationship8" ON "pagoMatricula" ("id_alumno")
;

-- Add keys for table pagoMatricula

ALTER TABLE "pagoMatricula" ADD CONSTRAINT "Key9" PRIMARY KEY ("id_pagoMatricula")
;

-- Table departamento

CREATE TABLE "departamento"(
 "id_departamento" Integer NOT NULL,
 "nombreDepartamento" Text NOT NULL,
 "despachoDepartamento" Text NOT NULL,
 "id_facultad" Integer
)
;

-- Create indexes for table departamento

CREATE INDEX "IX_Relationship9" ON "departamento" ("id_facultad")
;

-- Add keys for table departamento

ALTER TABLE "departamento" ADD CONSTRAINT "Key10" PRIMARY KEY ("id_departamento")
;

-- Table empleado

CREATE TABLE "empleado"(
 "id_empleado" Integer NOT NULL,
 "dniEmpleado" Text NOT NULL,
 "nombreEmpleado" Text NOT NULL,
 "apellidosEmpleado" Text NOT NULL,
 "antiguedadEmpleado" Integer NOT NULL,
 "direccionEmpleado" Text NOT NULL,
 "telefonoEmpleado" Text NOT NULL
)
;

-- Add keys for table empleado

ALTER TABLE "empleado" ADD CONSTRAINT "Key11" PRIMARY KEY ("id_empleado")
;

-- Table profesor

CREATE TABLE "profesor"(
 "id_profesor" Integer NOT NULL,
 "categoriaProfesor" Text NOT NULL,
 "puestoProfesor" Text NOT NULL,
 "id_empleado" Integer,
 "id_departamento" Integer
)
;

-- Create indexes for table profesor

CREATE INDEX "IX_Relationship11" ON "profesor" ("id_empleado")
;

CREATE INDEX "IX_Relationship12" ON "profesor" ("id_departamento")
;

-- Add keys for table profesor

ALTER TABLE "profesor" ADD CONSTRAINT "Key12" PRIMARY KEY ("id_profesor")
;

-- Table docencia

CREATE TABLE "docencia"(
 "id_docencia" Integer NOT NULL,
 "id_profesor" Integer,
 "id_gradoAsignatura" Integer
)
;

-- Create indexes for table docencia

CREATE INDEX "IX_Relationship13" ON "docencia" ("id_profesor")
;

CREATE INDEX "IX_Relationship14" ON "docencia" ("id_gradoAsignatura")
;

-- Add keys for table docencia

ALTER TABLE "docencia" ADD CONSTRAINT "Key13" PRIMARY KEY ("id_docencia")
;

-- Table pas

CREATE TABLE "pas"(
 "id_pas" Integer NOT NULL,
 "categoriaPAS" Text NOT NULL,
 "puestoPAS" Text NOT NULL,
 "id_empleado" Integer,
 "id_facultad" Integer
)
;

-- Create indexes for table pas

CREATE INDEX "IX_Relationship15" ON "pas" ("id_empleado")
;

CREATE INDEX "IX_Relationship16" ON "pas" ("id_facultad")
;

-- Add keys for table pas

ALTER TABLE "pas" ADD CONSTRAINT "Key14" PRIMARY KEY ("id_pas")
;

-- Table pagoEmpleado

CREATE TABLE "pagoEmpleado"(
 "id_pagoEmpleado" Integer NOT NULL,
 "fechaPagoEmpleado" Date NOT NULL,
 "importePagoEmpleado" Integer NOT NULL,
 "estadoPagoEmpleado" Boolean NOT NULL,
 "id_empleado" Integer
)
;

-- Create indexes for table pagoEmpleado

CREATE INDEX "IX_Relationship17" ON "pagoEmpleado" ("id_empleado")
;

-- Add keys for table pagoEmpleado

ALTER TABLE "pagoEmpleado" ADD CONSTRAINT "Key15" PRIMARY KEY ("id_pagoEmpleado")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "medioFisico" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_facultad") REFERENCES "facultad" ("id_facultad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "reservas" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("id_medio") REFERENCES "medioFisico" ("id_medio") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("id_facultad") REFERENCES "facultad" ("id_facultad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("id_grado") REFERENCES "grado" ("id_grado") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("id_asignatura") REFERENCES "asignatura" ("id_asignatura") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "matriculacion" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("id_alumno") REFERENCES "alumno" ("id_alumno") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "matriculacion" ADD CONSTRAINT "Relationship7" FOREIGN KEY ("id_gradoAsignatura") REFERENCES "grado_asignatura" ("id_gradoAsignatura") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "pagoMatricula" ADD CONSTRAINT "Relationship8" FOREIGN KEY ("id_alumno") REFERENCES "alumno" ("id_alumno") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "departamento" ADD CONSTRAINT "Relationship9" FOREIGN KEY ("id_facultad") REFERENCES "facultad" ("id_facultad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "profesor" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "profesor" ADD CONSTRAINT "Relationship12" FOREIGN KEY ("id_departamento") REFERENCES "departamento" ("id_departamento") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "docencia" ADD CONSTRAINT "Relationship13" FOREIGN KEY ("id_profesor") REFERENCES "profesor" ("id_profesor") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "docencia" ADD CONSTRAINT "Relationship14" FOREIGN KEY ("id_gradoAsignatura") REFERENCES "grado_asignatura" ("id_gradoAsignatura") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "pas" ADD CONSTRAINT "Relationship15" FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "pas" ADD CONSTRAINT "Relationship16" FOREIGN KEY ("id_facultad") REFERENCES "facultad" ("id_facultad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "pagoEmpleado" ADD CONSTRAINT "Relationship17" FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado") ON DELETE NO ACTION ON UPDATE NO ACTION
;




