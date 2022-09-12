from django.shortcuts import render, redirect
from Blog.models import Articles, Personal
from Blog.forms import Formulario_articles, Formulario_personal
from django.contrib.auth.decorators import login_required

@login_required
def create_article(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_articles(request.POST)
            if form.is_valid():
                Articles.objects.create(
                titulo=form.cleaned_data['titulo'], 
                descripcion=form.cleaned_data['descripcion'],
                autor=form.cleaned_data['autor']
                )
                return redirect(listar_articulos)

        elif request.method == 'GET':  
            form = Formulario_articles()
            context={'form':form}
            return render(request, 'Blog/crear_articulo.html', context=context)
    else: return redirect ('login')


def listar_articulos(request):
    listar_articulos= Articles.objects.all()
    context={
        'listar_articulos':listar_articulos
    }
    return render(request, 'Blog/listar_articulos.html', context=context)

def create_personal(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_personal(request.POST)

            if form.is_valid():
                Personal.objects.create(
                    nombre=form.cleaned_data['nombre'],
                    apellido=form.cleaned_data['apellido'],
                    puesto=form.cleaned_data['puesto']
                )
                return redirect(listar_personal)

        elif request.method == 'GET':  
            form = Formulario_personal()
            context={'form':form}
            return render(request, 'Blog/crear_personal.html', context=context)
    else: return redirect ('login')

def listar_personal(request):
    listar_personal= Personal.objects.all()
    context={
        'listar_personal':listar_personal
    }
    return render(request, 'Blog/listar_personal.html', context=context)
