from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso = Curso(nombre = "Desarrollo web",camada = 11111)
    curso.save()
    dacumentoDeTexto = f'{curso.nombre} {curso.camada}'
    return HttpResponse(dacumentoDeTexto)