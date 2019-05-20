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
        msg = 'True'
        form = ProductForm()
        return render(request, template_name, {'form': form, 'msg': msg})
    return render(request, template_name, {'form': form})


def list_product(request):
    product = Product.objects.all()
    template_name = 'core/listar-produto.html'
    return render(request, template_name,  {'product': product})
