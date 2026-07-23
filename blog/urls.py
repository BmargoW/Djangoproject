from django.urls import path
from blog.views import BlogEntryCreateView, BlogEntryListView, BlogEntryDetailView, BlogEntryDeleteView, BlogEntryUpdateView

app_name = 'blog'

urlpatterns= [
    path('blogentry/', BlogEntryCreateView.as_view(), name = 'blog_greate'),
    path('blogentry_list/', BlogEntryListView.as_view(), name='blog_list'),
    path('blogentry_detail/<int:pk>/', BlogEntryDetailView.as_view(), name='blog_detail'),
    path('blogentry_delete/<int:pk>/', BlogEntryDeleteView.as_view(), name='blog_delete'),
    path('blogentry_update/<int:pk>/', BlogEntryUpdateView.as_view(), name='blog_update'),
    # path('product_detail/', views.product_detail, name = 'product_detail')
]
