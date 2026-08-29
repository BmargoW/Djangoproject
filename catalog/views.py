from tracemalloc import get_object_traceback

from django.http import HttpResponseForbidden

from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from users.models import CustomUser
from .forms import ProductForm
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalogs:home_2")
#добавляем метод для привязки заполнения поля owner данными по текущему пользователю
    def form_valid(self, form):
        # Устанавливаем владельца продукта как текущего пользователя
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalogs:home_2")


def change_status_publications(request, pk):
    if request.method == "POST":
    #если пользователь не имеет права менять статус публикации - исключение
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У Вас нет прав на действие')
    #если имеет - переход на страницу заполнения статуса

    redirect("catalog/product_status.html")

    if request.method == "POST":
        product = get_object_or_404(Product, pk=pk)
        a = request.POST.get("status")
        product.status_publications = str(a)
        product.save()
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, 'catalog/product_status.html', context)

    return render(request, 'catalog/product_detail.html')

class ProductListView(ListView):
    model = Product
    template_name = "catalog/home_2.html"
    context_object_name = "product"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalogs:home_2")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalogs:home_2")


class ContactView(TemplateView):
    name = "name"
    phone = "phone"
    message = "message"
    template_name = "catalog/contacts.html"


