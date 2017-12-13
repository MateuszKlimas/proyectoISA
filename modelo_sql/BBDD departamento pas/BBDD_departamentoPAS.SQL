/*
Created: 12/12/2017
Modified: 12/12/2017
Model: Departamento PAS
Database: PostgreSQL 9.5
*/


-- Create tables section -------------------------------------------------

-- Table departamentoPAS

CREATE TABLE "departamentoPAS"(
 "id_departamentoPAS" Integer NOT NULL,
 "nombreDepartamentoPAS" Text NOT NULL,
 "descripcionDepartamentoPAS" Text NOT NULL,
 "id_facultad" Integer NOT NULL
)
;

-- Add keys for table departamentoPAS

ALTER TABLE "departamentoPAS" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_departamentoPAS")
;

-- Table pas

CREATE TABLE "pas"(
 "id_pas" Integer NOT NULL,
 "categoriaPAS" Text NOT NULL,
 "puestoPAS" Text NOT NULL,
 "dniPAS" Text NOT NULL,
 "nombrePAS" Text NOT NULL,
 "apellidosPAS" Text NOT NULL,
 "fechaIncorporacionPAS" Date NOT NULL,
 "direccionPAS" Text NOT NULL,
 "telefonoPAS" Text NOT NULL,
 "id_departamentoPAS" Integer
)
;

-- Create indexes for table pas

CREATE INDEX "IX_Relationship1" ON "pas" ("id_departamentoPAS")
;

-- Add keys for table pas

ALTER TABLE "pas" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_pas")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "pas" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_departamentoPAS") REFERENCES "departamentoPAS" ("id_departamentoPAS") ON DELETE NO ACTION ON UPDATE NO ACTION
;




