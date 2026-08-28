from django.urls import path
from catalog.views import ProductDetailView, ProductListView, ContactView, ProductCreateView, ProductUpdateView, ProductDeleteView
from . import views

app_name = "catalogs"

urlpatterns = [
    path("home_2/", ProductListView.as_view(), name="home_2"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "product_form/", ProductCreateView.as_view(), name="product_form"
    ),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "product_change_status/<int:pk>/", views.change_status_publications, name="change_status"),
]
