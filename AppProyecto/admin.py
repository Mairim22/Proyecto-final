from django.contrib import admin
from AppProyecto.views import Clases, Contacto
from  .models import * 

# Register your models here.

admin.site.register(Clases)

admin.site.register(Contacto)