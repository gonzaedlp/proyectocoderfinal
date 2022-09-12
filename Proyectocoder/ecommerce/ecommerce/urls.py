from django.contrib import admin
from django.urls import path, include
from ecommerce.views import base, about
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base ,name="saludo"),
    path('about/',about ,name="about"),
    path('products/', include('products.urls')),
    path('Blog/', include('Blog.urls')),
    path('users/', include('users.urls')),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
