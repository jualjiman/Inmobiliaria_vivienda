from django.contrib import admin
from .models import Banner, Inmueble, Categoria, Aviso

from sorl.thumbnail.shortcuts import get_thumbnail


class BannerAdmin(admin.ModelAdmin):
    list_display = ('miniatura', 'activo',)

    def miniatura(self, model_instance):
        return (
            "<img src='%s' />" % (
                get_thumbnail(
                    model_instance.imagen,
                    '250x100',
                    crop='center'
                ).url,
            )
        )

    miniatura.allow_tags = True


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('miniatura', 'nombre', 'activo')
    search_fields = ('nombre', 'descripcion', )

    def miniatura(self, model_instance):
        return (
            "<img src='%s' />" % (
                get_thumbnail(
                    model_instance.imagen_principal,
                    '180x100',
                    crop='center'
                ).url,
            )
        )

    miniatura.allow_tags = True


class AvisoAdmin(admin.ModelAdmin):
    list_display = ('texto', 'activo')
    search_fields = ('texto', )

admin.site.register(Banner, BannerAdmin)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Categoria)
admin.site.register(Aviso, AvisoAdmin)
