from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('products/plants/', views.products_plants, name="products-plants"),
    path('products/gardeningtools/', views.products_gardeningtools, name="products-gardeningtools"),
    path('product/', views.product, name="product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)