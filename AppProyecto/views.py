from django.shortcuts import render
from AppProyecto.models import Clases, Contacto
from AppProyecto.forms import  ContactoFormulario, ClaseFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib import messages


# INICIO
def inicio(request):
    return render(request, "AppProyecto/inicio.html")

def clases(request):
    cls = Clases.objects.all()
    return render(request, "AppProyecto/clases.html", {"cls": cls})

def mensaje3(request):

    return render(request, "AppProyecto/mensaje3.html")

#ABOUT
def nosotros(request):
    return render(request, "AppProyecto/nosotros.html")


 #CONTACTO

def mensaje(request):

    return render(request, "AppProyecto/mensaje.html")

def contacto(request):
    
    if request.method == 'POST':
        
        Formulario5 = ContactoFormulario(request.POST)
        print(Formulario5)
        
        if Formulario5.is_valid:

            informacion = Formulario5.cleaned_data
            
            contacto = Contacto(nombre=informacion['nombre'], email=informacion['email'], texto=informacion['texto'])
            contacto.save()
           
            return render(request, "AppProyecto/mensaje.html")
            
    else:
        Formulario5 = ContactoFormulario() 
        return render(request, "AppProyecto/contacto.html", {"Formulario5":Formulario5})

# LOGIN Y REGISTRO
def registro(request):
    if request.method == 'POST':
        Formulario2 = UserRegisterForm(request.POST)

        if Formulario2.is_valid():
            Formulario2.save()
            username = Formulario2.cleaned_data['username']
            messages.success(request, f"Usuario {username} creado")
            return render(request, "AppProyecto/mensaje2.html")
    else:
        Formulario2 = UserRegisterForm()
    return render(request, "AppProyecto/registro.html", {"Formulario2":Formulario2})

def mensaje2(request):

    return render(request, "AppProyecto/mensaje2.html")


def login(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                

                return render(request,"AppProyecto/user.html", {"mensaje":usuario})
            
            else:

                return render(request, "AppProyecto/login.html", {"mensaje":"Datos incorrectos"})

        else:
            formulario = AuthenticationForm()
            return render(request, "AppProyecto/login.html", {"mensaje":"Datos incorrectos", 'form':formulario})
    
    formulario = AuthenticationForm()

    return render(request, "AppProyecto/login.html", {'form':formulario})

#Buscador

def buscar(request):
    
    if request.POST['nombre']:

        nombre = request.POST['nombre']
        print(nombre)
        clase = Clases.objects.filter(grupo__icontains=nombre)
        print(clase.values())
        return render(request, "AppProyecto/clases.html", {"clases": clase.values()})
        

    else:
        respuesta = "No enviaste datos"
    return render(request,"AppProyecto/clases.html", {"respuesta":respuesta})





def defUser (request):
    return render(request, "AppProyecto/user.html")

def defNew (request):
    if request.method == 'POST':
        new = ClaseFormulario(request.POST)
        print(new)
        if new.is_valid:
            datos = new.cleaned_data
            print(datos)
            newClase= Clases(nombre=datos['nombre'],horario=datos['horario'],descripcion=datos['descripcion']) 
            newClase.save()
            new = ClaseFormulario()
            return render(request, "AppProyecto/new.html",{"new":new})
    else:
        new = ClaseFormulario()
        return render(request, "AppProyecto/new.html", {"new":new})

def defDelete (request):
    if request.GET.get("deleteAlum"):
        peticion = request.GET.get("deleteAlum")
        try:
            deleteClase = Clases.objects.get(name=peticion)
            deleteClase.delete()
            codigos = Clases.objects.all()
            return render(request, "AppProyecto/delete.html", {'codigoshtml':codigos})
        except:
            codigos = [{'name':'NO EXISTE EL ALUMNO', 'name':peticion}]
            return render(request, "AppProyecto/delete.html", {'codigoshtml':codigos})
    else:
        codigos = Clases.objects.all()
        return render(request, "AppProyecto/delete.html", {'codigoshtml':codigos})


class ListarClase(ListView):
    model = Clases
    template_name = "AppProyecto/moreoptions.html"

class DetalleProductos(DetailView):
    model = Clases
    template_name = "AppProyecto/detail.html"

class ProductoUpdate(UpdateView):
    model = Clases
    success_url = "/AppProyecto/options"
    fields = ['nombre', 'horario', 'descripcion']

class ProductoDelete(DeleteView):
    model = Clases
    success_url = "/AppProyecto/options"


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        edit = UserEditForm(request.POST)

        if edit.is_valid:
            
            inf = edit.cleaned_data

            usuario.email = inf['email']
            usuario.password1 = inf['password1']
            usuario.password2 = inf['password2']
            usuario.save()

            return render(request, "AppProyecto/user.html")

    else:

        edit =UserEditForm(initial={'email': usuario.email})

    return render(request, "AppProyecto/editarperfil.html", {"edit":edit, "usuario":usuario})


