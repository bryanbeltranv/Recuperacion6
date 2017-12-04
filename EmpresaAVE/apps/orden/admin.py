# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import orden, producto,impuesto



class ProductoInline(admin.StackedInline):
	model = producto
	extra = 3

class ImpuestoInline(admin.StackedInline):
	model = impuesto
	extra = 3

class OrdenAdmin(admin.ModelAdmin):
	list_display = ('id_orden' , 'fecha')
	inlines = [ProductoInline, ImpuestoInline]


admin.site.register(orden,OrdenAdmin)
admin.site.register(producto)
admin.site.register(impuesto)
