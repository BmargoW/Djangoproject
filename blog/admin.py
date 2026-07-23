from django.contrib import admin
from . models import BlogEntry

# Register your models here.
@ admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'creation_date', 'publication_status', 'number_of_views')
    list_filter = ('title',)
    search_fields = ('tutle','content',)