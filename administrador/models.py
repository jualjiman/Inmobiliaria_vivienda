# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify


class Banner(models.Model):

    imagen = ImageField(
        upload_to="banners"
    )

    link = models.CharField(
        max_length=300,
        blank=True,
        help_text=u'Liga hacia la que envia el banner al darle click.'
    )

    fecha_publicacion = models.DateTimeField(
        default=datetime.now(),
        help_text=u'Fecha y hora en que el banner se mostrará.'
    )

    fecha_fin = models.DateTimeField(
        blank=True,
        null=True,
        help_text=(
            'Fecha y hora en la que dejará de ser mostrado el banner.'
            'Si se deja en blanco este campo el banner será permanente.'
        )
    )

    activo = models.BooleanField(
        default=True,
        help_text=u'¿Deberá ser mostrado?'
    )


class Categoria(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        editable=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Inmueble(models.Model):

    nombre = models.CharField(
        max_length=100,
        help_text=u'Nombre del inmueble.'
    )

    descripcion = models.TextField(
        help_text=u'Descripcion del inmueble (ubicación, precio, etc).'
    )

    categoria = models.ForeignKey(Categoria)

    imagen_principal = ImageField(
        upload_to='inmuebles'
    )

    imagen1 = ImageField(
        upload_to='inmuebles',
        blank=True
    )

    imagen2 = ImageField(
        upload_to='inmuebles',
        blank=True
    )

    imagen3 = ImageField(
        upload_to='inmuebles',
        blank=True
    )

    fecha_publicacion = models.DateTimeField(
        default=datetime.now(),
        help_text=u'Fecha y hora en que el inmueble se mostrará.'
    )

    fecha_fin = models.DateTimeField(
        blank=True,
        null=True,
        help_text=(
            'Fecha y hora en la que dejará de ser mostrado el inmueble.'
            'Si se deja en blanco este campo el inmueble será permanente.'
        )
    )

    activo = models.BooleanField(
        default=True,
        help_text=u'¿Deberá ser mostrado?.'
    )

    slug = models.SlugField(
        editable=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Inmueble, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Aviso(models.Model):

    texto = models.CharField(
        max_length=80
    )

    fecha_publicacion = models.DateTimeField(
        default=datetime.now(),
        help_text=u'Fecha y hora en que el aviso se mostrará.'
    )

    fecha_fin = models.DateTimeField(
        blank=True,
        null=True,
        help_text=(
            'Fecha y hora en la que dejará de ser mostrado el aviso.'
            'Si se deja en blanco este campo el aviso será permanente.'
        )
    )

    activo = models.BooleanField(
        default=True,
        help_text=u'¿Deberá ser mostrado?.'
    )

    def __unicode__(self):
        return self.texto
