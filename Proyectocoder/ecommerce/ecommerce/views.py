from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products

def base(request):
    return render(request,"index.html",context={})
def about(request):
    return render(request,"about.html",context={})

def search_products(request):
    search=request.GET['search']
    product=Products.objects.filter(name__icontains=search)
    context={
        "product":product
        }
    return render(request, 'products/search_products.html',context=context)