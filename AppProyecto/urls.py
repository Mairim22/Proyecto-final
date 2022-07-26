from re import template
from django.urls import path
from AppProyecto import views
from django.contrib.auth.views import LoginView, LogoutView


#from .views import buscar

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('mensaje', views.mensaje, name="Mensaje"),
    path('mensaje2', views.mensaje2, name="Mensaje2"),
    path('mensaje3', views.mensaje3, name="Mensaje3"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('contacto', views.contacto, name="Contacto"),
    path('registro', views.registro, name="Registro"),
    path('clases', views.clases, name="Clases"),
    path('login', views.login, name="Login"),
    path('login', LoginView.as_view(template_name='AppProyecto/login.html'), name="Login"),
    path('logout', LogoutView.as_view(template_name='AppProyecto/inicio.html'), name="Logout"),
    path('contactoFormulario', views.contacto, name="ContactoFormulario"),
    path('buscar/', views.buscar),

    # Login

    path('user', views.defUser, name="user"),
    path('new', views.defNew, name="new"),
    path('options', views.ListarClase.as_view(), name="options"),
    path('editprofile', views.editarPerfil, name='editprofile'),
    path(r'^(?P<pk>\d+)$', views.DetalleProductos.as_view(), name='detail'),
    path(r'^update/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='update'),
    path(r'^delete/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='delete'),

]