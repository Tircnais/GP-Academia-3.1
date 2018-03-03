# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
                ('bibliografia', models.CharField(max_length=500, null=True, blank=True)),
                ('observaciones', models.CharField(max_length=450, null=True, blank=True)),
            ],
            options={
                'db_table': 'autor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aves',
            fields=[
                ('id_aves', models.IntegerField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=45, null=True, blank=True)),
                ('sinonimo', models.CharField(max_length=100, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('morfometria', models.CharField(max_length=100, null=True, blank=True)),
                ('endemismo', models.CharField(max_length=100, null=True, blank=True)),
                ('migracion', models.CharField(max_length=100, null=True, blank=True)),
                ('ecologia', models.CharField(max_length=100, null=True, blank=True)),
                ('behaviur', models.CharField(max_length=100, null=True, blank=True)),
                ('anio_publicacion', models.CharField(max_length=45, null=True, blank=True)),
                ('anio_collecion', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AvesAutor',
            fields=[
                ('id_aves_autor', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'aves_autor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AvesLocalizacion',
            fields=[
                ('id_aves_localizacion', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'aves_localizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AvesSource',
            fields=[
                ('id_aves_source', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'aves_source',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id_especies', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'especies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EspeciesFotos',
            fields=[
                ('id_especie_fotos', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'especies_fotos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id_familia', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'familia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id_fotos', models.IntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'db_table': 'fotos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id_localizacion', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('latitud', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
                ('toponimo', models.CharField(max_length=150, null=True, blank=True)),
                ('altitud', models.FloatField(null=True, blank=True)),
                ('max_altitud', models.FloatField(null=True, blank=True)),
                ('min_altitud', models.FloatField(null=True, blank=True)),
                ('ecosistema', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'localizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oorder',
            fields=[
                ('id_order', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'oorder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id_source', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'source',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uicn',
            fields=[
                ('id_uicn', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'uicn',
                'managed': False,
            },
        ),
    ]
