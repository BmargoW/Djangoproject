from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.number_of_views is not None:
            self.object.number_of_views += 1
        else:
            self.object.number_of_views = 0
        return self.object



class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'publication_status',
              'number_of_views']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args = [self.kwargs.get('pk')])



class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')