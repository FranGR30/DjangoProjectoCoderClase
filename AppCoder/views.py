from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

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

def leerProfesores(request):
    profesores=Profesor.objects.all()
    return render(request,'AppCoder/profesores.html',{'profesores':profesores})

def eliminarProfesor(request,nombre):
    profesor=Profesor.objects.get(nombre = nombre)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request,'AppCoder/profesores.html',{'profesores':profesores})

def editarProfesor(request,nombre):
    profesor=Profesor.objects.get(nombre = nombre)
    if request.method == 'POST':
        miFormulario = ProfeFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request,'AppCoder/profesores.html',{'profesores':profesores})
    else:
        miFormulario = ProfeFormulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'email':profesor.email,'profesion':profesor.profesion})
        return render(request,'AppCoder/editarProfesor.html',{'formulario':miFormulario,'nombre':nombre})

class EstudiantesList(ListView):
    model = Estudiantes
    template_name = 'AppCoder/estudiante_list.html'

class EstudianteDetalle(DetailView):
    model = Estudiantes
    template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
    model = Estudiantes
    success_url = reverse_lazy('estudiante_listar')
    fields = ['nombre','apellido','email']

class EstudiantesEdicion(UpdateView):
    model = Estudiantes
    success_url = reverse_lazy('estudiante_listar')
    fields = ['nombre','apellido','email']

class EstudiantesEliminacion(DeleteView):
    model = Estudiantes
    success_url = reverse_lazy('estudiante_listar')
    fields = ['nombre','apellido','email']