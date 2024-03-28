from django.urls import path

from . import views

urlpatterns = [
    path("register_product", views.register_product, name="register_product"),
    path("list_products", views.list_products, name="list_products")
]
