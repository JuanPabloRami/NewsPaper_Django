from django.http import HttpResponse
from django.shortcuts import render
from cgitb import text
from .models import Noticias
from .models import Publicidad



def index(request):
    return render(request,'index.html')

def deportes(request):
    
    noticias = Noticias.objects.all()
    publicidad = Publicidad.objects.all()

    dicciNoticia = {
        'noticias':noticias,
        'publicidad':publicidad
        }

    

    return render(request,'deportes.html',dicciNoticia)

def politica(request,nombre = "juan"):
    noticias = Noticias.objects.all()
    publicidad = Publicidad.objects.all()

    dicciNoticia = {
        'noticias':noticias,
        'publicidad':publicidad
        }
    return render(request,'politica.html',dicciNoticia)

def contacto(request):
    return render(request,'contacto.html')

# Create your views here.
