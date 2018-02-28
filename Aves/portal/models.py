# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Amenazas(models.Model):
    idamenaza = models.AutoField(primary_key=True)
    clasificacion = models.CharField(
        unique=True, max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amenazas'

    def __unicode__(self):
        return "%s - %s" % (self.idamenaza, self.clasificacion)


class Autores(models.Model):
    idautor = models.AutoField(primary_key=True)
    autor = models.CharField(unique=True, max_length=25)
    bibliografia = models.CharField(max_length=445, blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    a_opublicacion = models.CharField(
        db_column='a\xf1opublicacion', max_length=8, blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    a_orecoleccion = models.CharField(
        db_column='a\xf1orecoleccion', max_length=10, blank=True, null=True)
    fecha = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autores'

    def __unicode__(self):
        return "%s - %s -%s - %s - %s - %s" % (self.idautor, self.autor, self.bibliografia, self.a_opublicacion, self.a_orecoleccion, self.fecha)


class AutoresAves(models.Model):
    idestudio = models.AutoField(primary_key=True)
    idautor = models.ForeignKey(Autores, db_column='idautor')
    fuente = models.CharField(max_length=15, blank=True, null=True)
    idave = models.ForeignKey('Aves', db_column='idave')

    class Meta:
        managed = False
        db_table = 'autores_aves'

    def __unicode__(self):
        return "%s - %s -%s - %s " % (self.idestudio, self.idautor, self.fuente, self.idave)


class Aves(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigoespecie = models.CharField(unique=True, max_length=10)
    clase = models.CharField(max_length=4)
    namebird = models.CharField(max_length=35, blank=True, null=True)
    sinonimo = models.CharField(max_length=55, blank=True, null=True)
    utm_wgs = models.CharField(max_length=3, blank=True, null=True)
    utm_zone = models.CharField(max_length=17, blank=True, null=True)
    migracion = models.CharField(max_length=15)
    endemica = models.CharField(max_length=15)
    morfometrica = models.CharField(max_length=3, blank=True, null=True)
    ecologia = models.CharField(max_length=3, blank=True, null=True)
    comportamiento = models.CharField(max_length=3, blank=True, null=True)
    llamada = models.CharField(max_length=3, blank=True, null=True)
    observacion = models.CharField(max_length=400, blank=True, null=True)
    amenaza = models.ForeignKey(Amenazas, db_column='amenaza')

    class Meta:
        managed = False
        db_table = 'aves'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.codigo, self.codigoespecie, self.clase, self.namebird, self.sinonimo, self.utm_wgs, self.utm_zone, self.migracion, self.endemica, self.morfometrica, self.ecologia, self.comportamiento, self.llamada, self.observacion, self.amenaza)


class Denominacion(models.Model):
    iddenominacion = models.AutoField(primary_key=True)
    ordenclade = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'denominacion'

    def __unicode__(self):
        return "%s - %s" % (self.iddenominacion, self.ordenclade)


class Especies(models.Model):
    idespecie = models.AutoField(primary_key=True)
    nombespecie = models.CharField(unique=True, max_length=35)
    idfamilia = models.ForeignKey('Familias', db_column='idfamilia')

    class Meta:
        managed = False
        db_table = 'especies'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idespecie, self.nombespecie, self.idfamilia)


class EspeciesAves(models.Model):
    idclasificacion = models.AutoField(primary_key=True)
    idave = models.ForeignKey(Aves, db_column='idave')
    idespecie = models.ForeignKey(Especies, db_column='idespecie')

    class Meta:
        managed = False
        db_table = 'especies_aves'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idclasificacion, self.idave, self.idespecie)


class Familias(models.Model):
    idfamilia = models.AutoField(primary_key=True)
    nombfamilia = models.CharField(unique=True, max_length=20)
    iddenominacion = models.ForeignKey(
        Denominacion, db_column='iddenominacion')

    class Meta:
        managed = False
        db_table = 'familias'

    def __unicode__(self):
        return "%s - %s - %s" % (self.idfamilia, self.nombfamilia, self.iddenominacion)


class Localidades(models.Model):
    idlocalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=75)
    idpro = models.ForeignKey('Provincias', db_column='idpro')

    class Meta:
        managed = False
        db_table = 'localidades'

    def __unicode__(self):
        return "%s - %s -- %s" % (self.idlocalidad, self.nombre, self.idpro)


class LocalidadesAves(models.Model):
    idlocal = models.AutoField(primary_key=True)
    ecosistema = models.CharField(max_length=75)
    nombftecoord = models.CharField(max_length=5, blank=True, null=True)
    toponim = models.CharField(max_length=30, blank=True, null=True)
    latitud = models.CharField(max_length=15)
    longitud = models.CharField(max_length=15)
    altitud = models.CharField(max_length=15)
    altitudmax = models.CharField(max_length=15)
    altitudmin = models.CharField(max_length=15)
    idlocalidad = models.ForeignKey(Localidades, db_column='idlocalidad')
    idave = models.ForeignKey(Aves, db_column='idave')

    class Meta:
        managed = False
        db_table = 'localidades_aves'

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.idlocal, self.ecosistema, self.nombftecoord, self.toponim, self.latitud, self.longitud, self.altitud, self.altitudmax, self.altitudmin, self.idlocalidad, self.idave)


class Paises(models.Model):
    idpais = models.CharField(primary_key=True, max_length=3)
    nombpais = models.CharField(
        unique=True, max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paises'

    def __unicode__(self):
        return "%s -- %s" % (self.idpais, self.nombpais)


class Provincias(models.Model):
    idpro = models.AutoField(primary_key=True)
    idpais = models.ForeignKey(
        Paises, db_column='idpais', blank=True, null=True)
    nombprovincia = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'provincias'

    def __unicode__(self):
        return "%s -- %s -- %s" % (self.idpro, self.idpais, self.nombprovincia)


class Urls(models.Model):
    idurl = models.AutoField(primary_key=True)
    url = models.CharField(max_length=150)
    idave = models.ForeignKey(Aves, db_column='idave')

    class Meta:
        managed = False
        db_table = 'urls'

    def __unicode__(self):
        return "%s - %s -- %s" % (self.idurl, self.url, self.idave)
