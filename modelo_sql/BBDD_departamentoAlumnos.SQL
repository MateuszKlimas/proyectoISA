/*
Created: 12/12/2017
Modified: 12/12/2017
Model: Departamento Alumnos
Database: PostgreSQL 9.5
*/


-- Create tables section -------------------------------------------------

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

ALTER TABLE "alumno" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_alumno")
;

-- Table matriculacion

CREATE TABLE "matriculacion"(
 "id_matriculacion" Integer NOT NULL,
 "numConvocatoria" Integer NOT NULL,
 "numMatricula" Integer NOT NULL,
 "id_alumno" Integer,
 "id_gradoAsignatura" Integer NOT NULL
)
;

-- Create indexes for table matriculacion

CREATE INDEX "IX_Relationship1" ON "matriculacion" ("id_alumno")
;

-- Add keys for table matriculacion

ALTER TABLE "matriculacion" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_matriculacion")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "matriculacion" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_alumno") REFERENCES "alumno" ("id_alumno") ON DELETE NO ACTION ON UPDATE NO ACTION
;




