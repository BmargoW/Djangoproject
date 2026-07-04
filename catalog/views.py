from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

def home(request):
    five_products = Product.objects.order_by('created_ad')[:5]
    print(five_products)
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse (f"Спасибо {name}, ваш номер {phone} зарегистрирован!")
    return render(request, 'catalog/contacts.html')

