from django.urls import path
from .views import home, insert_product, list_product, edit_product

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar-produto', insert_product, name='core_insert_product'),
    path('listar-produto', list_product, name='core_list_product'),
    path('editar-produto/<int:id>', edit_product, name='core_edit_product'),
]
