from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm

def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)


def insert_product(request):
    form = ProductForm(request.POST or None)
    template_name = 'core/cadastro-produto.html'

    if form.is_valid():
        form.save()
        form = ProductForm()
        return render(request, template_name, {'form': form})
    return render(request, template_name, {'form': form})
