from django.shortcuts import render, render_to_response, redirect

from django.http import HttpResponse
from django.http import Http404
# necesario para el AJAX
from django.views.decorators.csrf import csrf_exempt
# Resultado de AJAX en formato JSON
from django.core import serializers
from django.http import JsonResponse

# TIPOS de respesta a VISTAS---
from django.template import RequestContext, loader
# importamos el modelo BD
from portal.models import *

# PAGINACION
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Sirven para enviar en FORMATO JSON
import json
# para generar colores
import random


def mapa_view(request):
    datosblugares = []
    lugares = []
    listalugares = Localizacion.objects.distinct().all()

    #----------------------Empiezo yo--------------_#
    inicio = 20
    listalugares = Localizacion.objects.distinct().all()[:inicio]
    for lugar in listalugares:
        fklugar = lugar.provincia_id_provincia.id_provincia
        ilugar = lugar.id_localizacion
        # lista = AvesLocalizacion.objects.filter(localizacion_id_localizacion=ilugar)
        conteo = AvesLocalizacion.objects.filter(localizacion_id_localizacion=ilugar).count()
        # print "->\t", inicio
        inicio += 1
        # print "FK lugar\t", fklugar
        latitud = lugar.latitud
        latitud = str(latitud).replace(',', '.')
        longitud = lugar.longitud
        longitud = str(longitud).replace(',', '.')
        print "Coordenada:\t", latitud, " ", longitud
        listaprovincias = Provincia.objects.filter(id_provincia=fklugar)
        for provincia in listaprovincias:
            fkpais = provincia.pais_id_pais.id_pais
            nombpro = provincia.nombre
            listapaises = Pais.objects.filter(id_pais=fkpais)
            for pais in listapaises:
                lugares.append((pais, provincia, lugar, latitud, longitud, conteo))
    #----------------------Termino yo--------------_#

    provincias = Provincia.objects.all()
    for pro in provincias:
        idpro = pro.id_provincia
        # print idpro
        nombpro = pro.nombre
        idp = pro.pais_id_pais
        localidad = Localizacion.objects.filter(provincia_id_provincia=idpro).all()[0]
        conteo = AvesLocalizacion.objects.filter(localizacion_id_localizacion=localidad.id_localizacion).count()
        def r(): return random.randint(0, 255)
        colores = ('#%02X%02X%02X' % (r(), r(), r()))
        datosblugares.append((colores, idp, nombpro, conteo))

    dicmapa = {
        'datosblugares': datosblugares,
        'lugares': lugares,
    }
    return render(request, 'mapa.html', dicmapa)


def autores(request):
    dicAutores = {}
    estudio = []
    c = 0
    listautores = Autor.objects.distinct('nombre').all()[:10]
    for autor in listautores:
        iautor = autor.id_autor
        ave = Aves.objects.filter(avesautor__autor_id_autor=iautor).all()[0]
        c += 1
        # print "AVE: ", c, "\t", ave
        contautor = AvesAutor.objects.filter(autor_id_autor=iautor).count()
        estudio.append((autor, ave, contautor))
    dicAutores['listaestudios'] = estudio

    listafuentes = Source.objects.all()
    total = AvesSource.objects.all().count()
    arreglo = []
    for fuente in listafuentes:
        ifuente = fuente.id_source
        nfuente = fuente.nombre
        representa = AvesSource.objects.filter(source_id_source=ifuente).count()
        representa = (representa * 100)/total
        arreglo.append((representa, nfuente))
    arreglo.sort()
    uno = arreglo[3]
    dos = arreglo[2]
    tres = arreglo[1]
    valorA = uno[0]
    valorB = dos[0]
    valorC = tres[0]
    uno = uno[1]
    dos = dos[1]
    tres = tres[1]
    dicAutores['uno'] = uno
    dicAutores['dos'] = dos
    dicAutores['tres'] = tres
    dicAutores['valorA'] = valorA
    dicAutores['valorB'] = valorB
    dicAutores['valorC'] = valorC
    return render(request, 'autores.html', dicAutores)


def proconteo(request):
    contEc = []
    contPe = []
    paisymas = []
    dicConteo = {}
    #-----------------PARA EL CUADRO---------------------#
    listapais = []
    listaprov = []
    listalocalidades = []
    acum = ''
    paises = Pais.objects.all()
    for pais in paises:
        ipais = pais.id_pais
        provincias = Provincia.objects.filter(pais_id_pais=ipais)
        for provincia in provincias:
            iprovincia = provincia.id_provincia
            lugares = Localizacion.objects.filter(provincia_id_provincia=iprovincia)
            for x in lugares:
                ilugar = x.id_localizacion
                nombre = x.nombre
                nombre = unicode(nombre)
                cont = AvesLocalizacion.objects.filter(localizacion_id_localizacion=ilugar).count()
                cont = str(cont)
                acum = '{' + nombre + ',' + cont + '},'
                # print "idpais ", pais.nombre, " provincia ", provincia.nombre, " Lugar ", nombre, " Cant AVES", cont
                listalocalidades.append((nombre, cont))
            listaprov.append((provincia, listalocalidades))
        listapais.append((pais, listaprov))
    dicConteo['listapais'] = listapais


    #____________________CONTENIDO TABLAS___________________#
    for pais in paises:
        idp = pais.id_pais
        npais = pais.nombre
        provincias = Provincia.objects.filter(pais_id_pais=idp)
        for provincia in provincias:
            idpro = provincia.id_provincia
            nombpro = provincia.nombre
            listalugares = ""
            caves = 0
            if 'EC' in npais:
                listalugares = Localizacion.objects.filter(provincia_id_provincia=idpro)
                for x in listalugares:
                    ilugar = x.id_localizacion
                    conteo = Localizacion.objects.filter(id_localizacion=ilugar).count()
                    localidades = Localizacion.objects.filter(id_localizacion=ilugar)
                    caves += conteo
                contEc.append((idpro, nombpro, caves))
                # print "pais\t",pais
            else:
                listalugares = Localizacion.objects.filter(provincia_id_provincia=idpro)
                for x in listalugares:
                    ilugar = x.id_localizacion
                    conteo = Localizacion.objects.filter(id_localizacion=ilugar).count()
                    localidades = Localizacion.objects.filter(id_localizacion=ilugar)
                    caves += conteo
                contPe.append((idpro, nombpro, caves))
    dicConteo['contEc'] = contEc
    dicConteo['contPe'] = contPe


    # -----------------AMENAZAS----------------------#
    datosamenaza = []
    listamenazas = Uicn.objects.all()
    colorN = 0
    for amenaza in listamenazas:
        idamenaza = amenaza.id_uicn
        nombamenza = amenaza.nombre
        numAvesAmenazadas = Aves.objects.filter(uicn_id_uicn=idamenaza).count()
        colorN += 1
        datosamenaza.append((idamenaza, nombamenza, numAvesAmenazadas, colorN))
    dicConteo['datosamenaza'] = datosamenaza
    return render(request, "conteo.html", dicConteo)


def clasificacion(request):
    datosclasifica = []
    conteo = []
    listaespecie = Especies.objects.all()
    for especie in listaespecie:
        iespecie = especie.id_especies
        cont = Aves.objects.filter(especies_id_especies=iespecie).count()
        if cont > 200:
            conteo.append((especie, cont))

    listordenes = Oorder.objects.all()
    for orden in listordenes:
        iorden = orden.id_order
        listafamilias = Familia.objects.filter(order_id_order=iorden).all()
        contorden = Familia.objects.filter(order_id_order=iorden).count()
        for familia in listafamilias:
            ifamilia = familia.id_familia
            contAves = Aves.objects.filter(familia_id_familia=ifamilia).count()
            if contAves > 500:
                datosclasifica.append((familia, contAves))

    datosarbol = []
    datosfamilia = []
    listordenes = Oorder.objects.all()[:4]
    for orden in listordenes:
        iorden = orden.id_order
        listafamilias = Familia.objects.filter(order_id_order=iorden)
        contFamilia = Familia.objects.filter(order_id_order=iorden).count()
        for familia in listafamilias:
            ifamilia = familia.id_familia
            contAves = Aves.objects.filter(familia_id_familia=ifamilia).count()
            # if contAves > 500:
            datosfamilia.append((familia, contAves))
        datosarbol.append((orden, datosfamilia, contFamilia))
    dicinfo = {
        'datosclasifica': datosclasifica,
        'listaespecie': conteo,
        'datosarbol': datosarbol
    }

    #, context_instance=RequestContext(request)
    return render(request, "clasificacion.html", dicinfo)


def index(request):
    totales = []
    mejoresautores = []
    numAves = Aves.objects.distinct('nombre').all().count()
    numAmenazas = Uicn.objects.all().count()
    numOrden = Oorder.objects.all().count()
    numFamilias = Familia.objects.all().count()
    numEspecies = Especies.objects.all().count()
    numAutores = Autor.objects.all().count()
    listautores = Autor.objects.all().distinct('nombre')
    for autor in listautores:
        iautor = autor.id_autor
        contautor = AvesAutor.objects.filter(autor_id_autor=iautor).count()
        # print autor.nombre
        mejoresautores.append((autor, contautor))
    totales.append(("Aves", numAves))
    totales.append(("Amenazas", numAmenazas))
    totales.append(("Orden", numOrden))
    totales.append(("Familias", numFamilias))
    totales.append(("Especies", numEspecies))
    totales.append(("Autores", numAutores))

    dicinfo = {
        'totales': totales,
        'listautores': listautores,
        'mejoresautores': mejoresautores,
    }

    #, context_instance=RequestContext(request)
    return render(request, "index.html", dicinfo)


def fotos(request):
    urlfotos = Fotos.objects.distinct('url').all()[:12]
    # cont = 1
    detalle = []
    for foto in urlfotos:
        ifoto = foto.id_fotos
        # print "-->", ifoto
        especie = Especies.objects.filter(especiesfotos__fotos_id_fotos__id_fotos=ifoto)[0]
        iespecie = especie.id_especies
        ave = Aves.objects.filter(especies_id_especies=iespecie)[0]
        # print especie.nombre
        # print cont
        # cont += 1
        detalle.append((foto, especie, ave))
    # Muestra 12 fotos por pagina (multiplos de 3 por el responsive)
    paginator = Paginator(urlfotos, 4)
    page = request.GET.get('page')
    try:
        imagenes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        imagenes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        imagenes = paginator.page(paginator.num_pages)
    imagenes = imagenes
    cntxtFoto = {
        'paginas': imagenes,
        'listafotos': detalle,
    }
    return render(request, "galeria.html", cntxtFoto)

