from django.shortcuts import render, redirect
from .models import Libro
# Create your views here.

def home(request):
    librosListados = Libro.objects.all()
    return render(request, "gestionLibro.html", {"libros": librosListados})

def registrarLibro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']
    editorial = request.POST['txtEditorial']
    calificacion = request.POST['numCalificacion']

    libro = Libro.objects.create(
        codigo=codigo, nombre=nombre, autor=autor, editorial=editorial, calificacion=calificacion)
    return redirect('/')

def edicionLibro(request, codigo):
   libro = Libro.objects.get(codigo=codigo)
   return render(request, "edicionLibro.html", {"libro": libro})

def editarLibro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']
    editorial = request.POST['txtEditorial']
    calificacion = request.POST['numCalificacion']

    libro = Libro.objects.get(codigo=codigo)
    
    libro.nombre=nombre
    libro.autor=autor
    libro.editorial=editorial
    libro.calificacion=calificacion
    libro.save()
    return redirect('/')

def eliminacionLibro(request, codigo):
    libro = Libro.objects.get(codigo=codigo)
    libro.delete()
    return redirect('/')