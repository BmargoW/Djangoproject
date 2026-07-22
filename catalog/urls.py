from django.urls import path
from . import views

urlpatterns= [
    path('home_2/', views.home, name = 'home_2'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('product_detail/', views.product_detail, name = 'product_detail')
]