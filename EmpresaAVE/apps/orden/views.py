# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from models import orden,producto,impuesto
import psycopg2, psycopg2.extras

def index(resquest):

	obj = orden.objects.all()
	obj1 = producto.objects.all()
	obj2 = impuesto.objects.all()
	#obj1 = producto.objects.all()
	i = 1
	vi=0
	vtp=0
	total=0

	for a in obj:
		obj_id_orden = a.id_orden
		obj_fecha = a.fecha
	
	for b in obj1:
		obj1_id_prod = b.id
		obj1_orden_id = b.orden_id
		obj1_descripcion = b.descripcion
		obj1_precio = b.precio

	for c in obj2:
		obj2_id_imp = c.id
		obj2_orden_id = c.id_orden_id
		obj2_nombre = c.nombre
		obj2_valor = c.valor
		vi=b.precio*c.valor
		vtp = b.precio+vi
		total += vtp
		print(vi)
		print(vtp)
		print(total)
		print("registro" ,i)
		print(orden.objects.all())
		print(producto.objects.all())
		print(b.orden_id)
		print(a.id_orden)
		print(a.fecha)
		print(b.descripcion)
		i += 1
		vi=b.precio*c.valor
		print(vi)
		vtp += b.precio+vi
		print(vtp)
		total += vtp
		print(total)
		context={
		
			"obj":obj,
			"obj1":obj1,
			"obj2":obj2,
			"obj_id_orden": obj_id_orden,
			"obj_fecha": obj_fecha,
			"obj1_id_prod": obj1_id_prod,
			"obj1_orden_id":obj1_orden_id,
			"obj1_descripcion": obj1_descripcion,
			"obj1_precio": obj1_precio,			
			"obj2_id_imp": obj2_id_imp,
			"obj2_orden_id":obj2_orden_id,
			"obj2_nombre": obj2_nombre,
			"obj2_valor": obj2_valor,
			"vi":vi,
			"vtp":vtp,
			"total":total,			
		}
	
			
	return render(resquest, "index.html",context)

def orden_list(resquest):
    db = psycopg2.connect(database='BaseAve',user='postgres',password='1234', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT id_orden,fecha,descripcion,precio FROM orden_orden, orden_impuesto,orden_producto WHERE id_orden=id_orden_id AND id_orden=orden_id')
    registro = [(row[0], row[1],row[2], row[3]) for row in cursor.fetchall()]
    print(registro)
    
    return render(resquest,"orden_list.html",{"registro":registro})