from django.urls import path
from catalog.views import ProductDetailView, ProductListView, ContactView, ProductCreateView, ProductUpdateView

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
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update")
]
