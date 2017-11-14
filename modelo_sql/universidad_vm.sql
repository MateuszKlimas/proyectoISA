/*
Created		14/11/2017
Modified		14/11/2017
Project		
Model			
Company		
Author		
Version		
Database		PostgreSQL 8.1 
*/



/* Drop Referential Integrity Triggers */





/* Drop User-Defined Triggers */



/* Drop Domains */



/* Drop Procedures */



/* Drop Views */



/* Drop Indexes */



/* Drop Tables */
Drop table "pas_nomina" Restrict;
Drop table "profesor_nomina" Restrict;
Drop table "asignaturas_profes" Restrict;
Drop table "nomina" Restrict;
Drop table "pas" Restrict;
Drop table "profesor" Restrict;
Drop table "departamento" Restrict;
Drop table "asignaturas_grado" Restrict;
Drop table "medios_fisicos" Restrict;
Drop table "reservas" Restrict;
Drop table "grados" Restrict;
Drop table "facultad" Restrict;
Drop table "asignaturas" Restrict;



/* Create Domains */



/* Create Tables */


Create table "asignaturas"
(
	"id_asignatura" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
 primary key ("id_asignatura")
) Without Oids;


Create table "facultad"
(
	"id_facultad" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"direccion" Char(20) NOT NULL,
 primary key ("id_facultad")
) Without Oids;


Create table "grados"
(
	"id_grado" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"num_creditos_obligatorios" Char(20) NOT NULL,
	"num_creditos_transversales" Char(20) NOT NULL,
	"num_creditos_optativos" Char(20) NOT NULL,
	"id_facultad" Char(20) NOT NULL,
 primary key ("id_grado")
) Without Oids;


Create table "reservas"
(
	"titular" Char(20) NOT NULL,
	"tipo" Char(20) NOT NULL,
	"hora_inicio" Time NOT NULL,
	"hora_fin" Time NOT NULL,
	"fecha_inicio" Date NOT NULL,
	"dia_semana" Char(20),
	"id_reserva" Char(20) NOT NULL,
	"id_medio" Char(20) NOT NULL,
 primary key ("id_reserva")
) Without Oids;


Create table "medios_fisicos"
(
	"id_medio" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"tipo" Char(20) NOT NULL,
	"precio_hora" Numeric,
	"capacidad" Integer NOT NULL,
	"id_facultad" Char(20) NOT NULL,
 primary key ("id_medio")
) Without Oids;


Create table "asignaturas_grado"
(
	"creditos" Integer NOT NULL,
	"tipo" Char(20) NOT NULL,
	"id_asignatura" Char(20) NOT NULL,
	"id_grado" Char(20) NOT NULL
) Without Oids;


Create table "departamento"
(
	"id_departamento" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"despacho" Char(20) NOT NULL,
	"id_facultad" Char(20) NOT NULL,
 primary key ("id_departamento")
) Without Oids;


Create table "profesor"
(
	"numero_tramos_docentes" Integer NOT NULL,
	"numero_tramos_investigacion" Integer NOT NULL,
	"dni" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"apellidos" Char(20) NOT NULL,
	"categoria" Char(20) NOT NULL,
	"antiguedad" Char(20) NOT NULL,
	"codigo_profesor" Char(20) NOT NULL,
	"id_departamento" Char(20) NOT NULL,
 primary key ("codigo_profesor")
) Without Oids;


Create table "pas"
(
	"dni" Char(20) NOT NULL,
	"nombre" Char(20) NOT NULL,
	"apellido" Char(20) NOT NULL,
	"categoria" Char(20) NOT NULL,
	"antiguedad" Char(20) NOT NULL,
	"codigo_pas" Char(20) NOT NULL,
 primary key ("codigo_pas")
) Without Oids;


Create table "nomina"
(
	"codigo_nomina" Char(20) NOT NULL,
	"importe" Money NOT NULL,
	"fecha" Date NOT NULL,
	"paga_extra" Boolean NOT NULL,
 primary key ("codigo_nomina")
) Without Oids;


Create table "asignaturas_profes"
(
	"codigo_profesor" Char(20) NOT NULL,
	"id_asignatura" Char(20) NOT NULL
) Without Oids;


Create table "profesor_nomina"
(
	"codigo_nomina" Char(20) NOT NULL,
	"codigo_profesor" Char(20) NOT NULL
) Without Oids;


Create table "pas_nomina"
(
	"codigo_pas" Char(20) NOT NULL,
	"codigo_nomina" Char(20) NOT NULL
) Without Oids;



/* Create Tab 'Others' for Selected Tables */


/* Create Alternate Keys */



/* Create Indexes */



/* Create Foreign Keys */

Alter table "asignaturas_profes" add  foreign key ("id_asignatura") references "asignaturas" ("id_asignatura") on update restrict on delete restrict;

Alter table "asignaturas_grado" add  foreign key ("id_asignatura") references "asignaturas" ("id_asignatura") on update restrict on delete restrict;

Alter table "medios_fisicos" add  foreign key ("id_facultad") references "facultad" ("id_facultad") on update restrict on delete restrict;

Alter table "grados" add  foreign key ("id_facultad") references "facultad" ("id_facultad") on update restrict on delete restrict;

Alter table "departamento" add  foreign key ("id_facultad") references "facultad" ("id_facultad") on update restrict on delete restrict;

Alter table "asignaturas_grado" add  foreign key ("id_grado") references "grados" ("id_grado") on update restrict on delete restrict;

Alter table "reservas" add  foreign key ("id_medio") references "medios_fisicos" ("id_medio") on update restrict on delete restrict;

Alter table "profesor" add  foreign key ("id_departamento") references "departamento" ("id_departamento") on update restrict on delete restrict;

Alter table "asignaturas_profes" add  foreign key ("codigo_profesor") references "profesor" ("codigo_profesor") on update restrict on delete restrict;

Alter table "profesor_nomina" add  foreign key ("codigo_profesor") references "profesor" ("codigo_profesor") on update restrict on delete restrict;

Alter table "pas_nomina" add  foreign key ("codigo_pas") references "pas" ("codigo_pas") on update restrict on delete restrict;

Alter table "profesor_nomina" add  foreign key ("codigo_nomina") references "nomina" ("codigo_nomina") on update restrict on delete restrict;

Alter table "pas_nomina" add  foreign key ("codigo_nomina") references "nomina" ("codigo_nomina") on update restrict on delete restrict;



/* Create Procedures */



/* Create Views */



/* Create Referential Integrity Triggers */





/* Create User-Defined Triggers */



/* Create Roles */



/* Add Roles To Roles */



/* Create Role Permissions */
/* Role permissions on tables */

/* Role permissions on views */

/* Role permissions on procedures */






