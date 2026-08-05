from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalogs:home_2")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalogs:home_2")

class ProductListView(ListView):
    model = Product
    template_name = "catalog/home_2.html"
    context_object_name = "product"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalogs:home_2")


class ContactView(TemplateView):
    name = "name"
    phone = "phone"
    message = "message"
    template_name = "catalog/contacts.html"


# return HttpResponse (f"Спасибо {name}, ваш номер {phone} зарегистрирован!")
