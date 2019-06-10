from django.urls import path, include
from .views import home, insert_product, list_product, edit_product, delete_product, index, about

urlpatterns = [
    path('', home, name='core_home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index', index, name='core_index'),
    path('cadastrar-produto', insert_product, name='core_insert_product'),
    path('listar-produto', list_product, name='core_list_product'),
    path('editar-produto/<int:id>', edit_product, name='core_edit_product'),
    path('excluir-produto/<int:id>', delete_product, name='core_delete_product'),
    path('sobre', about, name='core_about'),
]
