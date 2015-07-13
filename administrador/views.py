# -*- coding: utf-8 -*-
from datetime import datetime

from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from administrador.models import Banner, Aviso, Categoria, Inmueble
from administrador.forms import ContactForm


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Banner.objects.filter(activo=True)
    context_object_name = 'banners'

    def get_avisos(self):
        now = datetime.now()
        return Aviso.objects.filter(
            Q(fecha_publicacion__lte=now),
            Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
            Q(activo=True)
        ).order_by('fecha_publicacion')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context.update(
            {
                'avisos': self.get_avisos(),
            }
        )

        return context


class CatalogoListView(ListView):
    template_name = 'catalogos.html'
    context_object_name = 'catalogos'
    model = Categoria

    def get_categorias(self):
        categorias = Categoria.objects.all()
        now = datetime.now()

        for categoria in categorias:
            inmuebles = Inmueble.objects.filter(
                Q(fecha_publicacion__lte=now),
                Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
                Q(categoria=categoria),
                Q(activo=True)
            )

            inmueble = inmuebles.order_by('?').first()
            if inmueble:
                categoria.inmueble_demo = inmueble

            categoria.inmuebles_count = inmuebles.count()

        return categorias

    def get_context_data(self, **kwargs):
        context = super(CatalogoListView, self).get_context_data(**kwargs)

        context.update(
            {
                'catalogos': self.get_categorias()
            }
        )

        return context


class CatalogoDetailView(DetailView):
    template_name = 'catalogo.html'
    context_object_name = 'catalogo'
    model = Categoria

    def get_inmuebles(self):
        categoria = self.get_object()
        now = datetime.now()

        inmuebles = Inmueble.objects.filter(
            Q(fecha_publicacion__lte=now),
            Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
            Q(categoria=categoria),
            Q(activo=True)
        ).order_by('fecha_publicacion')

        return inmuebles

    def get_context_data(self, **kwargs):
        context = super(CatalogoDetailView, self).get_context_data(**kwargs)

        context.update(
            {
                'catalogo': self.get_object(),
                'inmuebles': self.get_inmuebles()
            }
        )

        print context

        return context


class InmuebleDetailView(DetailView):
    template_name = 'inmueble.html'
    context_object_name = 'inmueble'
    now = datetime.now()
    queryset = Inmueble.objects.filter(
        Q(fecha_publicacion__lte=now),
        Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
        Q(activo=True)
    ).order_by('fecha_publicacion')


class ContactView(FormView):
    template_name = 'contacto.html'
    form_class = ContactForm
    success_url = '/gracias/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
