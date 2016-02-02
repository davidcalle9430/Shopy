from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .forms import ProductForm
from .models import Product

def  hello_world( request ):
    #return HttpResponse('Hello World!')
    #return render(request, 'index.html')
    products = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'products' : products
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    product = get_object_or_404( Product, pk=pk )
    template = loader.get_template('product_detail.html')
    context = {
        "product" : product
    }
    return HttpResponse( template.render(context, request) )

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    template = loader.get_template('new_product.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))
