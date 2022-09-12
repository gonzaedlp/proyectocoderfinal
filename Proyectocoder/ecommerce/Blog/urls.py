from django.urls import path
from Blog.views import create_article, listar_articulos, create_personal, listar_personal

   


urlpatterns = [
    path('listar_articulos/',listar_articulos,name="la"),
    path('crear_articulo/',create_article,name="ca"),
    path('listar_personal/',listar_personal,name="listarpersonal"),
    path('crear_personal/',create_personal,name="createpersonal"),
]
