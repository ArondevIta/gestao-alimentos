from django.shortcuts import render
from .models import Product
from .form import ProductForm

def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)


def insert_product(request):
    form = ProductForm(request.POST or None)
    template_name = 'core/cadastro-produto.html'
    data = {
        'form':form
    }

    if form.is_valid():
            form.save()
    return render(request, template_name, data)
