/*
Created: 12/12/2017
Modified: 12/12/2017
Model: Departamento Contable
Database: PostgreSQL 9.5
*/


-- Create tables section -------------------------------------------------

-- Table departamentoContable

CREATE TABLE "departamentoContable"(
 "id_departamentoContable" Integer NOT NULL,
 "nombreDepartamentoContable" Text NOT NULL,
 "descripcionDepartamentoContable" Text NOT NULL,
 "id_facultad" Integer NOT NULL
)
;

-- Add keys for table departamentoContable

ALTER TABLE "departamentoContable" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_departamentoContable")
;

-- Table contable

CREATE TABLE "contable"(
 "id_contable" Integer NOT NULL,
 "puestoContable" Text NOT NULL,
 "dniContable" Text NOT NULL,
 "nombreContable" Text NOT NULL,
 "apellidosContable" Text NOT NULL,
 "fechaIncorporacionContable" Date NOT NULL,
 "direccionContable" Text NOT NULL,
 "telefonoContable" Text NOT NULL,
 "id_departamentoContable" Integer
)
;

-- Create indexes for table contable

CREATE INDEX "IX_Relationship1" ON "contable" ("id_departamentoContable")
;

-- Add keys for table contable

ALTER TABLE "contable" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_contable")
;

-- Table pagoMatriculaAlumno

CREATE TABLE "pagoMatriculaAlumno"(
 "id_PagoMatriculaAlumno" Integer NOT NULL,
 "fechaPagoMatriculaAlumno" Date,
 "importeMatriculaAlumno" Integer NOT NULL,
 "pagoMatriculaAlumnoRealizado" Boolean NOT NULL,
 "id_departamentoContable" Integer,
 "id_alumno" Integer NOT NULL
)
;

-- Create indexes for table pagoMatriculaAlumno

CREATE INDEX "IX_Relationship2" ON "pagoMatriculaAlumno" ("id_departamentoContable")
;

-- Add keys for table pagoMatriculaAlumno

ALTER TABLE "pagoMatriculaAlumno" ADD CONSTRAINT "Key3" PRIMARY KEY ("id_PagoMatriculaAlumno")
;

-- Table nominaProfesor

CREATE TABLE "nominaProfesor"(
 "id_nominaProfesor" Integer NOT NULL,
 "fechaPagoNominaProfesor" Date,
 "importeNominaProfesor" Integer NOT NULL,
 "pagoNominaProfesorRealizado" Boolean NOT NULL,
 "id_departamentoContable" Integer,
 "id_profesor" Integer NOT NULL
)
;

-- Create indexes for table nominaProfesor

CREATE INDEX "IX_Relationship3" ON "nominaProfesor" ("id_departamentoContable")
;

-- Add keys for table nominaProfesor

ALTER TABLE "nominaProfesor" ADD CONSTRAINT "Key4" PRIMARY KEY ("id_nominaProfesor")
;

-- Table nominaPAS

CREATE TABLE "nominaPAS"(
 "id_nominaPAS" Integer NOT NULL,
 "fechaPagoNominaPAS" Date,
 "importeNominaPAS" Integer NOT NULL,
 "pagoNominaPASRealizado" Boolean NOT NULL,
 "id_departamentoContable" Integer,
 "id_pas" Integer NOT NULL
)
;

-- Create indexes for table nominaPAS

CREATE INDEX "IX_Relationship4" ON "nominaPAS" ("id_departamentoContable")
;

-- Add keys for table nominaPAS

ALTER TABLE "nominaPAS" ADD CONSTRAINT "Key5" PRIMARY KEY ("id_nominaPAS")
;

-- Table nominaContable

CREATE TABLE "nominaContable"(
 "id_nominaContable" Integer NOT NULL,
 "fechaPagoNominaContable" Date,
 "importNominaContable" Integer NOT NULL,
 "pagoNominaContableRealizado" Boolean NOT NULL,
 "id_departamentoContable" Integer,
 "id_contable" Integer
)
;

-- Create indexes for table nominaContable

CREATE INDEX "IX_Relationship5" ON "nominaContable" ("id_departamentoContable")
;

CREATE INDEX "IX_Relationship6" ON "nominaContable" ("id_contable")
;

-- Add keys for table nominaContable

ALTER TABLE "nominaContable" ADD CONSTRAINT "Key6" PRIMARY KEY ("id_nominaContable")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "contable" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_departamentoContable") REFERENCES "departamentoContable" ("id_departamentoContable") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "pagoMatriculaAlumno" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("id_departamentoContable") REFERENCES "departamentoContable" ("id_departamentoContable") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "nominaProfesor" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("id_departamentoContable") REFERENCES "departamentoContable" ("id_departamentoContable") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "nominaPAS" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("id_departamentoContable") REFERENCES "departamentoContable" ("id_departamentoContable") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "nominaContable" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("id_departamentoContable") REFERENCES "departamentoContable" ("id_departamentoContable") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "nominaContable" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("id_contable") REFERENCES "contable" ("id_contable") ON DELETE NO ACTION ON UPDATE NO ACTION
;




