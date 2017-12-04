# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class orden(models.Model):
	id_orden = models.AutoField(primary_key=True, unique=True)
	fecha = models.DateField()

class producto(models.Model):
	orden = models.ForeignKey(orden, on_delete=models.CASCADE, null=True, blank=True) 
	descripcion = models.CharField(max_length=25)
	precio = models.FloatField()

class impuesto(models.Model):
	id_orden= models.ForeignKey(orden, on_delete=models.CASCADE, null=True, blank=True) 
	nombre = models.CharField(max_length=25)
	valor = models.FloatField()
	