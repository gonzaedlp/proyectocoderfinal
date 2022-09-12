from django.urls import path
from .views import delete_products
from products.views import create_products, listar_productos, search_products, delete_products, update_products

urlpatterns = [
    path('listar_productos/',listar_productos,name="listarproductos"),
    path('crear_producto/',create_products,name="createproducts"),
    path('search-products/',search_products,name='search_products' ),
    path('delete-products/<int:pk>/',delete_products,name='delete_products' ),
    path('update-products/<int:pk>/',update_products,name='update_products' ),
]
