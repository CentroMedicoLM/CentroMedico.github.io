from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def comunidad(request):
    return render(request, 'comunidad.html')

def revista(request):
    return render(request, 'revista.html')

def calendario(request):
    return render(request, 'calendario.html')

def reportes(request):
    return render(request, 'reportes.html')