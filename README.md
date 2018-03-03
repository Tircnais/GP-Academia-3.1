# Proyecto Gestión Productiva Academia 3.1 
# Trabajado con Python 2.7

### Tema: Aves del Ecuador.


 1. Instalacion de librerias en Ubuntu 16.04 
    
    `sudo apt-get update
    sudo apt-get install python-dev
    sudo apt-get install python-setuptools
    sudo apt-get install postgresql
    sudo apt-get install postgresql-server-dev-9.3`

 2. Instalación de librerías de python en todo el SO
 
    `sudo easy_install pip
     sudo pip install virtualenv`

 3. Creación de entorno virtual
 
    `virtualenv /ruta/nombre_entorno
     source /ruta/nombre_entorno/bin/activate
     deactivate`

 4. Instalación de librerías en un entornos (virtualenv)   
 
    `pip install psycopg2
     pip install django==1.8
     pip install ipython`

 5. Clonar el proyecto

    `git clone https://github.com/programacion-taw-utpl-001/gp31-final-grupo003.git`

 5. Ejecutar el sql para la base de datos
````sql
		
                
        -- -------------------------------------------------
        -- Schema gpaves
        -- -------------------------------------------------
        CREATE SCHEMA IF NOT EXISTS gpaves AUTHORIZATION academia;
        ALTER USER academia SET search_path TO gpaves;
        USE gpaves ;
        
        -- -----------------------------------------------------
		-- Table gpaves.paises
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.paises (
		  idpais character varying(3) PRIMARY KEY,
		  nombpais character varying(60) NULL DEFAULT 'N/A' UNIQUE);
		ALTER TABLE gpaves.paises OWNER TO academia;
		COMMENT ON COLUMN gpaves.paises.idpais IS 'Codigo asignado al paises (Ejemplo: Ecuador "EC").';
		COMMENT ON COLUMN gpaves.paises.nombpais IS 'Nombre del paises.';
		COMMENT ON TABLE gpaves.paises IS 'Catalogo con las provincias del Ecuador.';
		CREATE INDEX IF NOT EXISTS index_paises ON gpaves.paises(nombpais);

		-- -------------------------------------------------
		-- Table gpaves.provincias
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.provincias (
		  idpro SERIAL PRIMARY KEY,
		  idpais character varying(2),
		  nombprovincia character varying(100) NOT NULL UNIQUE,
		  CONSTRAINT fkprovincia_to_paises
		    FOREIGN KEY (idpais)
		    REFERENCES gpaves.paises (idpais)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.provincias OWNER TO academia;
		COMMENT ON COLUMN gpaves.provincias.idpro IS 'PK. Codigo asignado a la provincia.';
		COMMENT ON COLUMN gpaves.provincias.idpais IS 'FK Llave foranea a paises. Ej. "EC"';
		COMMENT ON COLUMN gpaves.provincias.nombprovincia IS 'Nombre de la provincia.';
		COMMENT ON TABLE gpaves.provincias IS 'De momento es un catalogo con las provincias encontradoas del DataSet.';
		CREATE INDEX IF NOT EXISTS index_provincia ON gpaves.provincias(nombprovincia);

		-- -------------------------------------------------
		-- Table gpaves.localidades
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.localidades (
		  idlocalidad SERIAL PRIMARY KEY,
		  nombre character varying(75) NOT NULL UNIQUE,
		  idpro INTEGER NOT NULL,
		  CONSTRAINT fklocalidades_to_provincia
		    FOREIGN KEY (idpro)
		    REFERENCES gpaves.provincias (idpro)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.localidades  OWNER TO academia;
		COMMENT ON COLUMN gpaves.localidades.idlocalidad IS 'campo autoincrementable, para identificar la localidad.';
		COMMENT ON COLUMN gpaves.localidades.nombre IS 'Nombre de la localidad.';
		COMMENT ON COLUMN gpaves.localidades.idpro IS 'Llave foranea a Provincia.';
		COMMENT ON TABLE gpaves.localidades IS 'Tabla para localidades encontradas.';
		CREATE INDEX IF NOT EXISTS index_autor ON gpaves.localidades(nombre);


		-- -------------------------------------------------
		-- Table gpaves.amenazas
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.amenazas (
		  idamenaza SERIAL PRIMARY KEY,
		  clasificacion character varying(3) NULL DEFAULT 'N/A' UNIQUE);
		ALTER TABLE gpaves.amenazas OWNER TO academia;
		COMMENT ON COLUMN gpaves.amenazas.idamenaza IS 'PK. codigo autoincrementable para el UICN del ave.';
		COMMENT ON COLUMN gpaves.amenazas.clasificacion IS 'nombre del UICN  denominado como amenaza del ave.';
		COMMENT ON TABLE gpaves.amenazas IS 'Registro de la clasificación de ave.';

		-- -------------------------------------------------
		-- Table gpaves.especie
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.aves (
		  codigo SERIAL PRIMARY KEY,
		  codigoespecie character varying(10) NOT NULL UNIQUE,
		  clase character varying(4) NOT NULL DEFAULT 'Aves',
		  namebird character varying(35) NULL DEFAULT 'N/A',
		  sinonimo character varying(55) NULL DEFAULT 'N/A',
		  utm_wgs character varying(3) NULL DEFAULT 'N/A',
		  utm_zone character varying(17) NULL DEFAULT 'N/A',
		  migracion character varying(15) NOT NULL,
		  endemica character varying(15) NOT NULL,
		  morfometrica character varying(3) NULL DEFAULT 'N/A',
		  ecologia character varying(3) NULL DEFAULT 'N/A',
		  comportamiento character varying(3) NULL DEFAULT 'N/A',
		  llamada character varying(3) NULL DEFAULT 'N/A',
		  observacion character varying(400) NULL DEFAULT 'N/A',
		  amenaza INTEGER NOT NULL,
		  CONSTRAINT fkaves_to_amenazas
		    FOREIGN KEY (amenaza)
		    REFERENCES gpaves.amenazas (idamenaza)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.aves OWNER TO academia;
		COMMENT ON COLUMN gpaves.aves.codigo IS 'PK parte 1, codigo autoincrementable para la especie.';
		COMMENT ON COLUMN gpaves.aves.codigoespecie IS 'Codigo de especie asiganado a un ave en particular.';
		COMMENT ON COLUMN gpaves.aves.clase IS 'Clase de ave que es por defecto "N/A".';
		COMMENT ON COLUMN gpaves.aves.namebird IS 'nombre del ave.';
		COMMENT ON COLUMN gpaves.aves.sinonimo IS 'nombre del sinonimo del ave.';
		COMMENT ON COLUMN gpaves.aves.utm_wgs IS 'UTM-WGS encontrada.';
		COMMENT ON COLUMN gpaves.aves.utm_zone IS 'UTM-Zone encontrada.';
		COMMENT ON COLUMN gpaves.aves.migracion IS 'nombre asignado a su migracion.';
		COMMENT ON COLUMN gpaves.aves.endemica IS 'nombre asignado al ave.';
		COMMENT ON COLUMN gpaves.aves.morfometrica IS 'El ave presenta una morfometrica Si, No, N/A (no aplica).';
		COMMENT ON COLUMN gpaves.aves.ecologia IS 'El ave tiene ecologia Si, No, N/A (no aplica).';
		COMMENT ON COLUMN gpaves.aves.comportamiento IS 'El ave presenta un comportamiento Si, No, N/A (no aplica).';
		COMMENT ON COLUMN gpaves.aves.llamada IS 'El ave tiene una llamada (canto) Si, No, N/A (no aplica).';
		COMMENT ON COLUMN gpaves.aves.observacion IS 'Comentario realizado sobre el ave.';
		COMMENT ON COLUMN gpaves.aves.observacion IS 'FK a amenazas.';
		COMMENT ON TABLE gpaves.aves IS 'Registro de todos los codigos de especie encontrados, en los Datos.';
		CREATE INDEX IF NOT EXISTS idxcaractmorfometrica ON gpaves.aves(morfometrica);
		CREATE INDEX IF NOT EXISTS idxcaractecologia ON gpaves.aves(ecologia);
		CREATE INDEX IF NOT EXISTS idxcaractcomportamiento ON gpaves.aves(comportamiento);
		CREATE INDEX IF NOT EXISTS idxcaractllamada ON gpaves.aves(llamada);

		-- -------------------------------------------------
		-- Table gpaves.localidades_aves
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.localidades_aves (
		  idlocal SERIAL PRIMARY KEY,
		  ecosistema character varying(75) NOT NULL,
		  nombftecoord character varying(5) NULL DEFAULT 'N/A',
		  toponim character varying(30) NULL DEFAULT 'N/A',
		  latitud character varying(15) NOT NULL,
		  longitud character varying(15) NOT NULL,--NUMERIC NOT NULL
		  altitud character varying(15) NOT NULL,
		  altitudmax character varying(15) NOT NULL,
		  altitudmin character varying(15) NOT NULL,
		  idlocalidad INTEGER NOT NULL,
		  codespecie character varying(10) NOT NULL,
		  CONSTRAINT fkthis_to_aves
		    FOREIGN KEY (codespecie)
		    REFERENCES gpaves.aves (codigoespecie)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION,
		  CONSTRAINT fkhere_to_localidades
		    FOREIGN KEY (idlocalidad)
		    REFERENCES gpaves.localidades (idlocalidad)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.localidades_aves OWNER TO academia;
		COMMENT ON COLUMN gpaves.localidades_aves.idlocal IS 'PK de Localidad_aves.';
		COMMENT ON COLUMN gpaves.localidades_aves.ecosistema IS 'Nombre del ecosistema econtrado.';
		COMMENT ON COLUMN gpaves.localidades_aves.toponim IS 'nombre del toponimo encontrado.';
		COMMENT ON COLUMN gpaves.localidades_aves.nombftecoord IS 'Nombre de la fuente de la coordenada.';
		COMMENT ON COLUMN gpaves.localidades_aves.latitud IS 'Latitud registra.';
		COMMENT ON COLUMN gpaves.localidades_aves.longitud IS 'Longitud registra.';
		COMMENT ON COLUMN gpaves.localidades_aves.altitud IS 'altitud registrada.';
		COMMENT ON COLUMN gpaves.localidades_aves.altitudmax IS 'altitud maxima registrada.';
		COMMENT ON COLUMN gpaves.localidades_aves.altitudmin IS 'altitud maxima registrada.';
		COMMENT ON COLUMN gpaves.localidades_aves.idlocalidad IS 'FK a localidades';
		COMMENT ON COLUMN gpaves.localidades_aves.codespecie IS 'FK a aves.';
		COMMENT ON TABLE gpaves.localidades_aves IS 'Muchas aves, viven dentro de la misma localidad.';

		-- -------------------------------------------------
		-- Table gpaves.denominacion
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.denominacion (
		  iddenominacion SERIAL PRIMARY KEY,
		  ordenclade character varying(25) NOT NULL UNIQUE);
		ALTER TABLE gpaves.denominacion OWNER TO academia;
		COMMENT ON COLUMN gpaves.denominacion.iddenominacion IS 'codigo autoincrementable para el orden/clado del ave.';
		COMMENT ON COLUMN gpaves.denominacion.ordenclade IS 'PK nombre del orden/clado del ave.';
		COMMENT ON TABLE gpaves.denominacion IS 'Registro de los grupos de orden/clado encontrados.';


		-- -------------------------------------------------
		-- Table gpaves.familias
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.familias (
		  idfamilia SERIAL PRIMARY KEY,
		  nombfamilia character varying(20) NOT NULL UNIQUE,
		  iddenominacion INTEGER NOT NULL,
		  CONSTRAINT fkfam_to_den
		    FOREIGN KEY (iddenominacion)
		    REFERENCES gpaves.denominacion (iddenominacion)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.familias OWNER TO academia;
		COMMENT ON COLUMN gpaves.familias.idfamilia IS 'codigo autoincrementable para el orden/clado del ave.';
		COMMENT ON COLUMN gpaves.familias.nombfamilia IS 'PK nombre de la familia del ave.';
		COMMENT ON COLUMN gpaves.familias.iddenominacion IS 'FK a orden.';
		COMMENT ON TABLE gpaves.familias IS 'Registro de los grupos de familias encontradas.';


		-- -------------------------------------------------
		-- Table gpaves.especies
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.especies (
		  idespecie SERIAL PRIMARY KEY,
		  nombespecie character varying(35) NOT NULL UNIQUE,
		  idfamilia INTEGER NOT NULL,
		  CONSTRAINT fkesp_to_fam
		    FOREIGN KEY (idfamilia)
		    REFERENCES gpaves.familias (idfamilia)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.especies OWNER TO academia;
		COMMENT ON COLUMN gpaves.especies.idespecie IS 'PK codigo autoincrementable para el orden/clado del ave.';
		COMMENT ON COLUMN gpaves.especies.nombespecie IS 'nombre de la especie del ave.';
		COMMENT ON COLUMN gpaves.especies.idfamilia IS 'FK a familia.';
		COMMENT ON TABLE gpaves.especies IS 'Registro de los grupos de especies encontradas.';

		-- -------------------------------------------------
		-- Table gpaves.especies_aves
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.especies_aves (
		  idclasificacion SERIAL PRIMARY KEY,
		  codespecie character varying(10) NOT NULL,
		  idespecie INTEGER NOT NULL,
		  CONSTRAINT fkthere_to_aves
		    FOREIGN KEY (codespecie)
		    REFERENCES gpaves.aves (codigoespecie)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION,
		  CONSTRAINT fkhere_to_especies
		    FOREIGN KEY (idespecie)
		    REFERENCES gpaves.especies (idespecie)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.especies_aves OWNER TO academia;
		COMMENT ON COLUMN gpaves.especies_aves.idclasificacion IS 'PK de Localidad_aves.';
		COMMENT ON COLUMN gpaves.especies_aves.codespecie IS 'FK a aves.';
		COMMENT ON COLUMN gpaves.especies_aves.idespecie IS 'FK a especies.';
		COMMENT ON TABLE gpaves.especies_aves IS 'Un ave, puede clasificarse dentro de una o mas especies; a esa especie corresponden muchas aves.';

		-- -------------------------------------------------
		-- Table gpaves.autores
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.autores (
		  idautor SERIAL PRIMARY KEY,
		  autor character varying(25) NOT NULL UNIQUE,
		  bibliografia character varying(445) NULL DEFAULT 'N/A',
		  añopublicacion character varying(8) NULL DEFAULT 'N/A',
		  añorecoleccion character varying(10) NULL DEFAULT 'N/A',
		  fecha character varying(35) NULL);
		ALTER TABLE gpaves.autores OWNER TO academia;
		COMMENT ON COLUMN gpaves.autores.idautor IS 'Codigo autoincrementable para el auotor.';
		COMMENT ON COLUMN gpaves.autores.autor IS 'PK. Nombre del autor.';
		COMMENT ON COLUMN gpaves.autores.bibliografia IS 'bibliografia del mismo.';
		COMMENT ON COLUMN gpaves.autores.añopublicacion IS 'Año de publicación del estudio.';
		COMMENT ON COLUMN gpaves.autores.añorecoleccion IS 'Año en que fue recolectado.';
		COMMENT ON COLUMN gpaves.autores.fecha IS 'Fecha posible en la que se registro.';
		COMMENT ON TABLE gpaves.autores IS 'Registro de autores encontrados.';
		CREATE INDEX IF NOT EXISTS idxautor ON gpaves.autores(autor);

		-- -------------------------------------------------
		-- Table gpaves.autores_aves
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.autores_aves (
		  idestudio SERIAL PRIMARY KEY,
		  idautor INTEGER NOT NULL,
		  fuente character varying(15) NULL DEFAULT 'N/A',
		  codespecie character varying(10) NOT NULL,
		  CONSTRAINT fkthis_to_autores
		    FOREIGN KEY (idautor)
		    REFERENCES gpaves.autores (idautor)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION,
		  CONSTRAINT fkthis_to_aves
		    FOREIGN KEY (codespecie)
		    REFERENCES gpaves.aves (codigoespecie)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.autores_aves OWNER TO academia;
		COMMENT ON COLUMN gpaves.autores_aves.idestudio IS 'PK. Codigo autoincrementable para registrar el estudio y su autor.';
		COMMENT ON COLUMN gpaves.autores_aves.idautor IS 'FK a autores.';
		COMMENT ON COLUMN gpaves.autores_aves.fuente IS 'Nombre de la fuente que proviene.';
		COMMENT ON COLUMN gpaves.autores_aves.codespecie IS 'FK a Aves';
		COMMENT ON TABLE gpaves.autores_aves IS 'Un autor estudio muchas aves. Un ave fue estudiada por varios autores';
		CREATE INDEX IF NOT EXISTS idxnautor ON gpaves.autores_aves(idautor);
		-- -------------------------------------------------
		-- Table gpaves.URLS
		-- -------------------------------------------------
		CREATE TABLE IF NOT EXISTS gpaves.urls (
		  idurl SERIAL PRIMARY KEY,
		  url character varying(150) NOT NULL,
		  codespecie character varying(10) NOT NULL,
		  CONSTRAINT fkcaract_to_aves
		    FOREIGN KEY (codespecie)
		    REFERENCES gpaves.aves (codigoespecie)
		    ON DELETE NO ACTION
		    ON UPDATE NO ACTION);
		ALTER TABLE gpaves.urls OWNER TO academia;
		COMMENT ON COLUMN gpaves.urls.idurl IS 'PK. Codigo autoincrementable asignado al registro';
		COMMENT ON COLUMN gpaves.urls.url IS 'URL de la especie';
		COMMENT ON COLUMN gpaves.urls.codespecie IS 'FK a ecodigospecies';
		COMMENT ON TABLE gpaves.urls IS 'Catalogo con las provincias del Ecuador.';
		CREATE INDEX IF NOT EXISTS idx_urls ON gpaves.urls(url);````

7. Ejecutar El proyecto
 
    
    `configurar toda la base
     python manage.py inspectdb > models.py
     python manage.py makemigrations portal
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py runserver`