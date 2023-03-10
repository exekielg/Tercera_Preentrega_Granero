from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, 'TiendaApp/home.html')

def servicios(request):
    return render(request, 'TiendaApp/servicios.html')

def tienda(request):
    return render(request, 'TiendaApp/tienda.html')

def contacto(request):
        return render(request, 'TiendaApp/contacto.html')
