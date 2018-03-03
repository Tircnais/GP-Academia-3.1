-- -----------------------------------------------------
-- Create DateBase academia
-- -----------------------------------------------------
/*
DROP DATABASE if EXISTS aves;
DROP USER if EXISTS academia;

-- -----------------------------------------------------
-- Create Usuarios academia
-- -----------------------------------------------------
CREATE USER academia with password '1234';
CREATE DATABASE aves owner academia;
*/
-- -----------------------------------------------------
-- DROP SCHEMA gpaves
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS gpaves CASCADE;


-- -----------------------------------------------------
-- Schema gpaves
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS gpaves AUTHORIZATION academia;
ALTER USER academia SET search_path TO gpaves;
-----------------------------------------------------
-- Table `Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Oorder (
  id_order INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  PRIMARY KEY (id_order))
;
ALTER TABLE gpaves.Oorder OWNER TO academia;

-- -----------------------------------------------------
-- Table `Familia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Familia (
  id_familia INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  order_id_order INT NOT NULL,
  PRIMARY KEY (id_familia)
 ,
  CONSTRAINT fk_Familia_Oorder1
    FOREIGN KEY (order_id_order)
    REFERENCES gpaves.Oorder (id_order)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Familia OWNER TO academia;


-- -----------------------------------------------------
-- Table `Especies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Especies (
  id_especies INT NOT NULL UNIQUE,
  nombre VARCHAR(100) NULL,
  PRIMARY KEY (id_especies)
  );
ALTER TABLE gpaves.Especies OWNER TO academia;

-- -----------------------------------------------------
-- Table `Fotos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Fotos (
  id_fotos INT NOT NULL UNIQUE,
  url VARCHAR(400) NULL
  PRIMARY KEY (id_fotos)
  );
ALTER TABLE gpaves.Fotos OWNER TO academia;

-- -----------------------------------------------------
-- Table `Especie_fotos`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS gpaves.Especies_Fotos (
  id_Especie_Fotos INT NOT NULL,
  Especie_id_especies INT NOT NULL,
  Fotos_id_fotos INT NOT NULL,
  PRIMARY KEY (id_Especie_Fotos)
 ,
  CONSTRAINT fk_Especies_Aves
    FOREIGN KEY (Especie_id_especies)
    REFERENCES gpaves.Especies (id_especies)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Fotos
    FOREIGN KEY (Fotos_id_fotos)
    REFERENCES gpaves.Fotos (id_fotos)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Especies_Fotos OWNER TO academia;


-- -----------------------------------------------------
-- Table `Pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Pais (
  id_pais INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  PRIMARY KEY (id_pais))
;
ALTER TABLE gpaves.Pais OWNER TO academia;

-- -----------------------------------------------------
-- Table `Provincia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Provincia (
  id_provincia INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  Pais_id_pais INT NOT NULL,
  PRIMARY KEY (id_provincia)
 ,
  CONSTRAINT fk_Provincia_Pais1
    FOREIGN KEY (Pais_id_pais)
    REFERENCES gpaves.Pais (id_pais)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Provincia OWNER TO academia;

-- -----------------------------------------------------
-- Table `Autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Autor (
  id_autor INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  bibliografia VARCHAR(500) NULL,
  observaciones VARCHAR(450) NULL,
  PRIMARY KEY (id_autor))
;
ALTER TABLE gpaves.Autor OWNER TO academia;

-- -----------------------------------------------------
-- Table `Source`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Source (
  id_source INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  PRIMARY KEY (id_source))
;
ALTER TABLE gpaves.Source OWNER TO academia;

-- -----------------------------------------------------
-- Table `UICN`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.UICN (
  id_UICN INT NOT NULL UNIQUE,
  nombre VARCHAR(45) NULL,
  PRIMARY KEY (id_UICN))
;
ALTER TABLE gpaves.UICN OWNER TO academia;

-----------------------------------------------------
-- Table `Aves`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Aves (
  id_aves INT NOT NULL UNIQUE,
  codigo VARCHAR(45) NULL,
  sinonimo VARCHAR(100) NULL,
  nombre VARCHAR(100) NULL,
  morfometria VARCHAR(100) NULL,
  endemismo VARCHAR(100) NULL,
  migracion VARCHAR(100) NULL,
  ecologia VARCHAR(100) NULL,
  behaviur VARCHAR(100) NULL,
  anio_publicacion VARCHAR(45) NULL,
  anio_collecion VARCHAR(45) NULL,
  familia_id_familia INT NOT NULL,
  especies_id_especies INT NOT NULL,
  uicn_id_UICN INT NOT NULL,
  PRIMARY KEY (id_aves)
 ,
  CONSTRAINT fk_Aves_Familia
    FOREIGN KEY (familia_id_familia)
    REFERENCES gpaves.Familia (id_familia)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Aves_Especies1
    FOREIGN KEY (especies_id_especies)
    REFERENCES gpaves.Especies (id_especies)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Aves_UICN
    FOREIGN KEY (uicn_id_UICN)
    REFERENCES gpaves.UICN (id_UICN)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Aves OWNER TO academia;

-- -----------------------------------------------------
-- Table `Aves_Autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Aves_Autor (
  id_Aves_Autor INT NOT NULL,
  Aves_id_aves INT NOT NULL,
  Autor_id_autor INT NOT NULL,
  PRIMARY KEY (id_Aves_Autor)
 ,
  CONSTRAINT fk_Aves_has_Autor_Aves1
    FOREIGN KEY (Aves_id_aves)
    REFERENCES gpaves.Aves (id_aves)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Aves_has_Autor_Autor1
    FOREIGN KEY (Autor_id_autor)
    REFERENCES gpaves.Autor (id_autor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Aves_Autor OWNER TO academia;

-- -----------------------------------------------------
-- Table `Aves_Source`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Aves_Source (
  id_Aves_Source INT NOT NULL,
  Aves_id_aves INT NOT NULL,
  Source_id_source INT NOT NULL,
  PRIMARY KEY (id_Aves_Source)
 ,
  CONSTRAINT fk_Aves_has_Source_Aves1
    FOREIGN KEY (Aves_id_aves)
    REFERENCES gpaves.Aves (id_aves)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Aves_has_Source_Source1
    FOREIGN KEY (Source_id_source)
    REFERENCES gpaves.Source (id_source)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Aves_Source OWNER TO academia;

-- -----------------------------------------------------
-- Table `Localizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Localizacion (
  id_localizacion INT NOT NULL UNIQUE,
  nombre VARCHAR(100) NULL,
  latitud DOUBLE PRECISION NULL,
  longitud DOUBLE PRECISION NULL,
  toponimo VARCHAR(150) NULL,
  altitud DOUBLE PRECISION NULL,
  max_altitud DOUBLE PRECISION NULL,
  min_altitud DOUBLE PRECISION NULL,
  ecosistema VARCHAR(100) NULL,
  Provincia_id_provincia INT NOT NULL,
  PRIMARY KEY (id_localizacion)
 ,
  CONSTRAINT fk_Localizacion_Provincia1
    FOREIGN KEY (Provincia_id_provincia)
    REFERENCES gpaves.Provincia (id_provincia)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Localizacion OWNER TO academia;

-- -----------------------------------------------------
-- Table `Aves_Localizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gpaves.Aves_Localizacion (
  id_Aves_Localizacion INT NOT NULL UNIQUE,
  Aves_id_aves INT NOT NULL,
  Localizacion_id_localizacion INT NOT NULL,
  PRIMARY KEY (id_Aves_Localizacion)
 ,
  CONSTRAINT fk_Aves_has_Localizacion_Aves1
    FOREIGN KEY (Aves_id_aves)
    REFERENCES gpaves.Aves (id_aves)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Aves_has_Localizacion_Localizacion1
    FOREIGN KEY (Localizacion_id_localizacion)
    REFERENCES gpaves.Localizacion (id_localizacion)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
ALTER TABLE gpaves.Aves_Localizacion OWNER TO academia;


-- -----------------------------------------------------
-- INSERTS
-- -----------------------------------------------------

\COPY gpaves.Oorder(id_order,nombre) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Order.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Familia(id_familia,nombre,order_id_order) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Familia.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Especies(id_especies,nombre) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Especies.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Fotos(id_fotos,url) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Fotos.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Especies_Fotos(id_Especie_Fotos,Especie_id_especies ,Fotos_id_fotos) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Especie_fotos.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Pais(id_pais,nombre) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Paises.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Provincia(id_provincia,nombre,pais_id_pais) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Provincias.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Autor(id_autor,nombre, bibliografia, observaciones) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Autores.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Source(id_source,nombre) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Source.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.UICN(id_UICN,nombre) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/UICN.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Aves(id_aves,codigo,sinonimo,nombre,morfometria,endemismo,migracion,ecologia,behaviur,anio_publicacion,anio_collecion,familia_id_familia,especies_id_especies,uicn_id_UICN) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Aves.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Aves_Autor(id_Aves_Autor,Aves_id_aves,Autor_id_autor) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Aves_Autor.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Aves_Source(id_Aves_Source,Aves_id_aves,Source_id_source) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Aves_Source.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Localizacion(id_localizacion,nombre,latitud,longitud,toponimo,altitud,max_altitud,min_altitud,ecosistema,Provincia_id_provincia) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Localizacion.csv' DELIMITER ',' CSV HEADER;
\COPY gpaves.Aves_Localizacion(id_Aves_Localizacion,Aves_id_aves,Localizacion_id_localizacion) FROM '/home/pc/Documentos/GP-Academia-3.1-1/Anexos/Aves_Localizacion.csv' DELIMITER ',' CSV HEADER;


-- -----------------------------------------------------
-- DROPS
-- -----------------------------------------------------

/*
drop table gpaves.Aves_Localizacion cascade;
drop table gpaves.Oorder cascade;
drop table gpaves.Source cascade;
drop table gpaves.Fotos cascade;
drop table gpaves.Pais cascade;
drop table gpaves.Provincia cascade;
drop table gpaves.Autor cascade;
drop table gpaves.Especies cascade;
drop table gpaves.Especies_fotos cascade;
drop table gpaves.Localizacion cascade;
drop table gpaves.UICN cascade;
drop table gpaves.Aves_Localizacion cascade;
drop table gpaves.Aves_Autor cascade;
drop table gpaves.Aves_Source cascade;
drop table gpaves.Aves cascade;
*/
