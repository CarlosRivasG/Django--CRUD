from django.contrib import admin
from django.urls import path 
from django import views
from . import views


urlpatterns =  [
    path('', views.index, name="index"),
    path('listar', views.listar, name="listar"),
    path('actualizar/<int:idUsuarios>', views.actualizar, name="actualizar"),
    path('agregar', views.agregar, name="agregar"),
    path('eliminar/<int:idUsuarios>', views.eliminar, name="eliminar"),
]