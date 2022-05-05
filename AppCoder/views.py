from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from .forms import CursoFormulario

# Create your views here.
def curso(self):
    curso = Curso(nombre = "Desarrollo web",camada = 11111)
    curso.save()
    dacumentoDeTexto = f'{curso.nombre} {curso.camada}'
    return HttpResponse(dacumentoDeTexto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso (nombre = informacion['nombre'], camada = informacion['comision'])
            curso.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()
    return render(request, 'AppCoder/cursos.html',{'formulario':miFormulario})

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(camada = comision)
        return render(request,'AppCoder/inicio.html',{'cursos':cursos,'comision':comision})
    else:
        respuesta = "No enviaste dato/s"
    return render(request,'AppCoder/inicio.html',{'respuesta':respuesta})