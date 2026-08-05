from django.urls import path
from blog.views import (
    BlogEntryCreateView,
    BlogEntryListView,
    BlogEntryDetailView,
    BlogEntryDeleteView,
    BlogEntryUpdateView,
)

app_name = "blog"

urlpatterns = [
    path("blog/", BlogEntryCreateView.as_view(), name="blog_greate"),
    path("blog/list/", BlogEntryListView.as_view(), name="blog_list"),
    path(
        "blog/detail/<int:pk>/", BlogEntryDetailView.as_view(), name="blog_detail"
    ),
    path(
        "blog/delete/<int:pk>/", BlogEntryDeleteView.as_view(), name="blog_delete"
    ),
    path(
        "blog/update/<int:pk>/", BlogEntryUpdateView.as_view(), name="blog_update"
    ),

]
