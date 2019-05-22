from django.urls import path, include

from .views import register

urlpatterns = [
    path('registrar', register, name='accounts_register'),
]
