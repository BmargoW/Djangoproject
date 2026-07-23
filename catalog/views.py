
from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_2.html'
    context_object_name = 'product'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalogs:home_2')


class ContactView(TemplateView):
       name = "name"
       phone = "phone"
       message = "message"
       template_name = 'catalog/contacts.html'
      # return HttpResponse (f"Спасибо {name}, ваш номер {phone} зарегистрирован!")


