from django.shortcuts import render
from .models import Autor, Entrada
# Create your views here.
 
def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def vista_de_inicio(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores,
    }
    return render(request, 'blog/autoresInicio.html', context)

def entradas_por_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
        entradas = Entrada.objects.filter(autor=autor)
    except Autor.DoesNotExist:
        autor = None
        entradas = []
    
    context = {
        'autor': autor,
        'entradas': entradas,
    }
    return render(request, 'blog/entraPorAutor.html', context)
