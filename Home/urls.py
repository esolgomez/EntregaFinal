from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
]