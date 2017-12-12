/*
Created: 12/12/2017
Modified: 12/12/2017
Model: Departamento Profesores
Database: PostgreSQL 9.5
*/


-- Create tables section -------------------------------------------------

-- Table departamento

CREATE TABLE "departamento"(
 "id_departamento" Integer NOT NULL,
 "nombreDepartamento" Text NOT NULL,
 "descripcionDepartamento" Text NOT NULL,
 "id_facultad" Integer NOT NULL
)
;

-- Add keys for table departamento

ALTER TABLE "departamento" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_departamento")
;

-- Table profesor

CREATE TABLE "profesor"(
 "id_profesor" Integer NOT NULL,
 "puestoProfesor" Text NOT NULL,
 "categoriaProfesor" Text NOT NULL,
 "dniProfesor" Text NOT NULL,
 "nombreProfesor" Text NOT NULL,
 "apellidosProfesor" Text NOT NULL,
 "fechaComienzoDocencia" Date NOT NULL,
 "direccionProfesor" Text NOT NULL,
 "telefonoProfesor" Text NOT NULL,
 "id_departamento" Integer
)
;

-- Create indexes for table profesor

CREATE INDEX "IX_Relationship1" ON "profesor" ("id_departamento")
;

-- Add keys for table profesor

ALTER TABLE "profesor" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_profesor")
;

-- Table docencia

CREATE TABLE "docencia"(
 "id_docencia" Integer NOT NULL,
 "id_profesor" Integer NOT NULL,
 "id_gradoAsignatura" Integer NOT NULL
)
;

-- Create indexes for table docencia

CREATE INDEX "IX_Relationship2" ON "docencia" ("id_profesor")
;

-- Add keys for table docencia

ALTER TABLE "docencia" ADD CONSTRAINT "Key3" PRIMARY KEY ("id_docencia")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "profesor" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_departamento") REFERENCES "departamento" ("id_departamento") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "docencia" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("id_profesor") REFERENCES "profesor" ("id_profesor") ON DELETE NO ACTION ON UPDATE NO ACTION
;




