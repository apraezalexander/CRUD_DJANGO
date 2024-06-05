from django.shortcuts import render, HttpResponse

# Create your views here.

def holaMundo(request):
    return HttpResponse("Bienvenidos a la tienda virtual")

def inicio(request):
    return render(request, 'inicio.html')