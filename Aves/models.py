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


class Autor(models.Model):
    id_autor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    bibliografia = models.CharField(max_length=500, blank=True, null=True)
    observaciones = models.CharField(max_length=450, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Aves(models.Model):
    id_aves = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    sinonimo = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    morfometria = models.CharField(max_length=100, blank=True, null=True)
    endemismo = models.CharField(max_length=100, blank=True, null=True)
    migracion = models.CharField(max_length=100, blank=True, null=True)
    ecologia = models.CharField(max_length=100, blank=True, null=True)
    behaviur = models.CharField(max_length=100, blank=True, null=True)
    anio_publicacion = models.CharField(max_length=45, blank=True, null=True)
    anio_collecion = models.CharField(max_length=45, blank=True, null=True)
    familia_id_familia = models.ForeignKey('Familia', db_column='familia_id_familia')
    especies_id_especies = models.ForeignKey('Especies', db_column='especies_id_especies')
    uicn_id_uicn = models.ForeignKey('Uicn', db_column='uicn_id_uicn')

    class Meta:
        managed = False
        db_table = 'aves'


class AvesAutor(models.Model):
    id_aves_autor = models.IntegerField(primary_key=True)
    aves_id_aves = models.ForeignKey(Aves, db_column='aves_id_aves')
    autor_id_autor = models.ForeignKey(Autor, db_column='autor_id_autor')

    class Meta:
        managed = False
        db_table = 'aves_autor'


class AvesLocalizacion(models.Model):
    id_aves_localizacion = models.IntegerField(primary_key=True)
    aves_id_aves = models.ForeignKey(Aves, db_column='aves_id_aves')
    localizacion_id_localizacion = models.ForeignKey('Localizacion', db_column='localizacion_id_localizacion')

    class Meta:
        managed = False
        db_table = 'aves_localizacion'


class AvesSource(models.Model):
    id_aves_source = models.IntegerField(primary_key=True)
    aves_id_aves = models.ForeignKey(Aves, db_column='aves_id_aves')
    source_id_source = models.ForeignKey('Source', db_column='source_id_source')

    class Meta:
        managed = False
        db_table = 'aves_source'


class Especies(models.Model):
    id_especies = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies'


class EspeciesFotos(models.Model):
    id_especie_fotos = models.IntegerField(primary_key=True)
    especie_id_especies = models.ForeignKey(Especies, db_column='especie_id_especies')
    fotos_id_fotos = models.ForeignKey('Fotos', db_column='fotos_id_fotos')

    class Meta:
        managed = False
        db_table = 'especies_fotos'


class Familia(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    order_id_order = models.ForeignKey('Oorder', db_column='order_id_order')

    class Meta:
        managed = False
        db_table = 'familia'


class Fotos(models.Model):
    id_fotos = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fotos'


class Localizacion(models.Model):
    id_localizacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    toponimo = models.CharField(max_length=150, blank=True, null=True)
    altitud = models.FloatField(blank=True, null=True)
    max_altitud = models.FloatField(blank=True, null=True)
    min_altitud = models.FloatField(blank=True, null=True)
    ecosistema = models.CharField(max_length=100, blank=True, null=True)
    provincia_id_provincia = models.ForeignKey('Provincia', db_column='provincia_id_provincia')

    class Meta:
        managed = False
        db_table = 'localizacion'


class Oorder(models.Model):
    id_order = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oorder'


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    pais_id_pais = models.ForeignKey(Pais, db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'provincia'


class Source(models.Model):
    id_source = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source'


class Uicn(models.Model):
    id_uicn = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uicn'
