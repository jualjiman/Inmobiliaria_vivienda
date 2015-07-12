# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from administrador.views import (
    HomeView, CatalogoListView, CatalogoDetailView, InmuebleDetailView,
    ContactView,
)


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^catalogos/$', CatalogoListView.as_view(), name='catalogos'),

    url(
        r'^catalogos/(?P<slug>[-\w]+)/$',
        CatalogoDetailView.as_view(),
        name='catalogo'
    ),

    url(
        r'^inmueble/(?P<slug>[-\w]+)/$',
        InmuebleDetailView.as_view(),
        name='inmueble'
    ),

    url(r'^contacto/$', ContactView.as_view(), name='contacto'),

    url(
        r'^gracias/$',
        TemplateView.as_view(template_name="gracias.html"),
        name='gracias'
    ),

    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }
    ),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }
    ),
]
