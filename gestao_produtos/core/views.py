from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm
from django.contrib.auth.decorators import login_required


def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)


@login_required()
def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


@login_required()
def insert_product(request):
    form = ProductForm(request.POST or None)
    template_name = 'core/cadastro-produto.html'

    if form.is_valid():
        form.save()
        msg = 'True'
        form = ProductForm()
        return render(request, template_name, {'form': form, 'msg': msg})
    return render(request, template_name, {'form': form})


@login_required()
def list_product(request):
    product = Product.objects.all()
    template_name = 'core/listar-produto.html'
    return render(request, template_name,  {'product': product})


@login_required()
def edit_product(request, id):
    data ={}
    template_name= 'core/atualizar-produto.html'
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    data['product'] = product
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_product')
    return render(request, template_name, data)


@login_required()
def delete_product(request, id):
    data = {}
    template_name = 'core/delete_confirm.html'
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    data['product'] = product
    data['form'] = form

    if request.method == 'POST':
        product.delete()
        return redirect('core_list_product')
    else:
        return render(request, template_name, {'obj': product})


def about(request):
    template_name = 'core/sobre.html'
    return render(request, template_name)
