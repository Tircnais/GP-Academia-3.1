from django.conf.urls import include, url, patterns

from portal import views

urlpatterns = patterns('portal.views',
                       url(r'^$', views.index, name='home'),
                       url(r'^mapa', views.mapa_view, name='mapa'),
                       url(r'^fotos', views.fotos, name='fotos'),
                       url(r'^especies', views.clasificacion, name='especies'),
                       url(r'^cont', views.proconteo, name='cont'),
                       url(r'^autores', views.autores, name='autores'),
                       )
