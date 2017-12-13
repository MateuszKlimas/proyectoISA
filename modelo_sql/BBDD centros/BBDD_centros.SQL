/*
Created: 12/12/2017
Modified: 12/12/2017
Model: Centros
Database: PostgreSQL 9.5
*/


-- Create tables section -------------------------------------------------

-- Table centro

CREATE TABLE "centro"(
 "id_centro" Integer NOT NULL,
 "nombreCentro" Text NOT NULL,
 "direccionCentro" Text NOT NULL
)
;

-- Add keys for table centro

ALTER TABLE "centro" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_centro")
;

-- Table medioFisico

CREATE TABLE "medioFisico"(
 "id_medio" Integer NOT NULL,
 "nombreMedioFisico" Text NOT NULL,
 "tipoMedioFisico" Text NOT NULL,
 "precioMedioFisico" Double precision NOT NULL,
 "capacidadMedioFisico" Integer NOT NULL,
 "id_centro" Integer
)
;

-- Create indexes for table medioFisico

CREATE INDEX "IX_Relationship1" ON "medioFisico" ("id_centro")
;

-- Add keys for table medioFisico

ALTER TABLE "medioFisico" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_medio")
;

-- Table reserva

CREATE TABLE "reserva"(
 "id_reserva" Integer NOT NULL,
 "titularReserva" Text NOT NULL,
 "horaInicioReserva" Time NOT NULL,
 "horaFinReserva" Time NOT NULL,
 "fechaReserva" Date NOT NULL,
 "id_medio" Integer
)
;

-- Create indexes for table reserva

CREATE INDEX "IX_Relationship2" ON "reserva" ("id_medio")
;

-- Add keys for table reserva

ALTER TABLE "reserva" ADD CONSTRAINT "Key3" PRIMARY KEY ("id_reserva")
;

-- Table grado

CREATE TABLE "grado"(
 "id_grado" Integer NOT NULL,
 "nombreGrado" Text NOT NULL,
 "numCreditosObligatorios" Integer NOT NULL,
 "numCreditosTransversales" Integer NOT NULL,
 "numCreditoOptativos" Integer NOT NULL,
 "id_centro" Integer
)
;

-- Create indexes for table grado

CREATE INDEX "IX_Relationship3" ON "grado" ("id_centro")
;

-- Add keys for table grado

ALTER TABLE "grado" ADD CONSTRAINT "Key4" PRIMARY KEY ("id_grado")
;

-- Table grado_asignatura

CREATE TABLE "grado_asignatura"(
 "id_gradoAsignatura" Integer NOT NULL,
 "creditosAsignatura" Double precision NOT NULL,
 "tipoAsignatura" Text NOT NULL,
 "turnoAsignatura" Text NOT NULL,
 "id_grado" Integer,
 "id_asignatura" Integer
)
;

-- Create indexes for table grado_asignatura

CREATE INDEX "IX_Relationship4" ON "grado_asignatura" ("id_grado")
;

CREATE INDEX "IX_Relationship6" ON "grado_asignatura" ("id_asignatura")
;

-- Add keys for table grado_asignatura

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Key5" PRIMARY KEY ("id_gradoAsignatura")
;

-- Table asignatura

CREATE TABLE "asignatura"(
 "id_asignatura" Integer NOT NULL,
 "nombreAsignatura" Text NOT NULL,
 "descripcionAsignatura" Text NOT NULL
)
;

-- Add keys for table asignatura

ALTER TABLE "asignatura" ADD CONSTRAINT "Key6" PRIMARY KEY ("id_asignatura")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "medioFisico" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_centro") REFERENCES "centro" ("id_centro") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "reserva" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("id_medio") REFERENCES "medioFisico" ("id_medio") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("id_centro") REFERENCES "centro" ("id_centro") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("id_grado") REFERENCES "grado" ("id_grado") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "grado_asignatura" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("id_asignatura") REFERENCES "asignatura" ("id_asignatura") ON DELETE NO ACTION ON UPDATE NO ACTION
;




