from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Formulario_productos
from django.contrib.auth.decorators import login_required

@login_required
def create_products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_productos(request.POST, request.FILES)

            if form.is_valid():
                Products.objects.create(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    stock=form.cleaned_data['stock'],
                    image=form.cleaned_data['image'],
                )
                return redirect(listar_productos)

        elif request.method == 'GET':  
            form = Formulario_productos()
            context={'form':form}
            return render(request, 'products/crear_producto.html', context=context)
    else: return redirect ('login')

def listar_productos(request):
    listar_productos= Products.objects.all()
    context={
        'listar_productos':listar_productos
    }
    return render(request, 'products/listar_productos.html', context=context)

def primer_formulario(request):
    return render(request, 'primer_formulario.html', context={})

def search_products(request):
    search=request.GET['search']
    products=Products.objects.filter(name__icontains=search)
    context={
        "products":products
        }
    return render(request, 'products/search_products.html',context=context)

def delete_products(request,pk):
    if request.method == 'GET':
        product=Products.objects.get(pk=pk)
        context={'product':product}
        return render(request, 'products/delete_products.html', context=context)

    elif request.method =='POST':
        product=Products.objects.get(pk=pk)
        product.delete()
        return redirect(listar_productos)

def update_products(request,pk):
    if request.method=='POST':
        form=Formulario_productos(request.POST,request.FILES)
        if form.is_valid():
            product=Products.objects.get(pk=pk)
            product.name=form.cleaned_data['name']
            product.price=form.cleaned_data['price']
            product.stock=form.cleaned_data['stock']
            product.image=form.cleaned_data['image']
            product.save()
    
            return redirect(listar_productos)

    elif request.method=='GET':
        product=Products.objects.get(pk=pk)
        form=Formulario_productos(initial={'name':product.name, 'price':product.price, 'stock':product.stock})
        context={'form':form}
        return render(request, 'products/update_products.html', context=context)
