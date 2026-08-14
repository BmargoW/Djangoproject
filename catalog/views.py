from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalogs:home_2")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
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


