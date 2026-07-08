from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home_2.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse (f"Спасибо {name}, ваш номер {phone} зарегистрирован!")
    return render(request, 'catalog/contacts.html')

def product_detail(request):
    product = Product.objects.get(id = 1)
    context = {'product': product}
    return render (request, 'catalog/product_detail.html', context)

# def product_list(request):
#
#     return rende