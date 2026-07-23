from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from blog.models import BlogEntry

class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'publication_status',
              'number_of_views']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogEntryListView(ListView):
    model = BlogEntry
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return BlogEntry.objects.filter(publication_status=True)

class BlogEntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'publication_status',
              'number_of_views']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')