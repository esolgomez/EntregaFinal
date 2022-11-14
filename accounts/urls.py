from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('ingreso/', views.mi_login, name='ingreso'),
    path('registrar/', views.registrar, name='registrar'),
    path('salida/', LogoutView.as_view(template_name='accounts/salida.html') , name='salida'),
]
