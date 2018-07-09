from django.urls import path
from Examen import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listar', views.listar, name='listar'),
]
