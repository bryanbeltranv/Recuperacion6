from django.conf.urls import url,include
from . import views

urlpatterns = [
url(r'^productos$', views.orden_list, name="productos"),
url(r'^$', views.index, name="index" ),

 ]