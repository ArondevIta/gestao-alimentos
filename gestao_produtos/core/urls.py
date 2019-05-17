from django.urls import path
from .views import home, insert_product

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar-produto', insert_product, name='core_insert_product'),
]
